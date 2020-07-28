import math

from gennav.planners.base import Planner
from gennav.utils import RobotState, Trajectory
from gennav.utils.graph import Graph
from gennav.utils.graph_search.astar import astar


class PRMStar(Planner):
    """PRM-Star Class.
    Attributes:
        sample_area (tuple): area for sampling random points (min,max)
        sampler (function): function to sample random points in sample_area
        c (float): a constant for radius determination
        n (int): total no. of nodes to be sampled in sample_area
    """

    def __init__(self, sample_area, sampler, c, n):
        """Init PRM-Star Parameters."""

        self.sample_area = sample_area
        self.sampler = sampler
        self.n = n
        self.c = c

    def construct(self, env):
        """Constructs PRM-Star graph.
        Args:
            env (gennav.envs.Environment): Base class for an envrionment.
        Returns:
            graph (dict): A dict where the keys correspond to nodes and
                the values for each key is a list of the neighbour nodes
        """
        nodes = []
        graph = Graph()
        i = 0
        # samples points from the sample space until n points
        # outside obstacles are obtained
        while i < self.n:
            sample = self.sampler(self.sample_area)
            if not env.get_status(RobotState(position=sample)):
                continue
            else:
                i += 1
                nodes.append(sample)

        # finds neighbours for each node in a dynamic radius
        for node1 in nodes:
            for node2 in nodes:
                if node1 != node2:
                    r = self.c * math.sqrt(math.log(self.n) / self.n)
                    dist = math.sqrt(
                        (node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2
                    )
                    if dist < r:
                        n1 = RobotState(position=node1)
                        n2 = RobotState(position=node2)
                        traj = Trajectory([n1, n2])
                        if env.get_traj_status(traj):
                            if n1 not in graph.nodes:
                                graph.add_node(n1)

                            if n2 not in graph.nodes:
                                graph.add_node(n2)

                            if n2 not in graph.edges[n1] and n1 not in graph.edges[n2]:
                                graph.add_edge(
                                    n1, n2,
                                )

        return graph

    def plan(self, start, goal, env):
        """Constructs a graph avoiding obstacles and then plans path from start to goal within the graph.
        Args:
            start (gennav.utils.RobotState): tuple with start point coordinates.
            goal (gennav.utils.RobotState): tuple with end point coordinates.
            env (gennav.envs.Environment): Base class for an envrionment.
        Returns:
            gennav.utils.Trajectory: The planned path as trajectory
        """
        # construct graph
        graph = self.construct(env)
        # find collision free point in graph closest to start_point
        min_dist = float("inf")
        for node in graph.nodes:
            dist = math.sqrt(
                (node.position.x - start.position.x) ** 2
                + (node.position.y - start.position.y) ** 2
            )
            traj = Trajectory([node, start])
            if dist < min_dist and (env.get_traj_status(traj)):
                min_dist = dist
                s = node
        # find collision free point in graph closest to end_point
        min_dist = float("inf")
        for node in graph.nodes:
            dist = math.sqrt(
                (node.position.x - goal.position.x) ** 2
                + (node.position.y - goal.position.y) ** 2
            )
            traj = Trajectory([node, goal])
            if dist < min_dist and (env.get_traj_status(traj)):
                min_dist = dist
                e = node
        # add start_point to path
        path = [start]
        traj = Trajectory(path)
        # perform astar search
        p = astar(graph, s, e)
        if len(p.path) == 1:
            return traj
        else:
            traj.path.extend(p.path)
        # add end_point to path
        traj.path.append(goal)
        return traj