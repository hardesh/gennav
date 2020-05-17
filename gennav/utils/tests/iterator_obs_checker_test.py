import unittest
from gennav.utils.iterator_obs_checker import CheckIndividualPoints
from geometry_msgs.msg import Point32, PoseArray, Point, Quaternion, Pose

class SimpleTest(unittest.TestCase):
    
    def setUp(self):
        pass
        # print("Setting Tests for Iterator")

    def test_length(self):
        o = CheckIndividualPoints(viz=True)
        inf = float('inf')
        o.scan=[inf, inf, inf, inf, inf, inf, 2.122950792312622, 1.8218177556991577, 1.59413743019104, 1.423231601715088, 1.323502540588379, 1.3081393241882324, 1.3145588636398315, 1.3490028381347656, 1.335472822189331, 1.319705605506897, 1.3400593996047974, 1.3491653203964233, 1.3466880321502686, 1.3696467876434326, 1.3745601177215576, 1.3833107948303223, 1.3923722505569458, 1.4062138795852661, 1.3897963762283325, 1.4243078231811523, 1.4298373460769653, 1.4416676759719849, 1.450016736984253, 1.471937656402588, 1.5024218559265137, 1.4850928783416748, 1.5270593166351318, 1.5272008180618286, 1.5350757837295532, 1.5613079071044922, 1.58877432346344, 1.6090070009231567, 1.6587506532669067, 1.6668319702148438, 1.6823045015335083, 1.711564540863037, 1.7509064674377441, 1.7584381103515625, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.650038242340088, 2.6445717811584473, 2.631784677505493, 2.6164636611938477, 2.6125850677490234, 2.5924696922302246, 2.5889229774475098, 2.5727877616882324, 2.5825552940368652, 2.5913491249084473, 2.5679054260253906, 2.575549840927124, 2.5961365699768066, 2.578033447265625, 2.563906669616699, 2.576000690460205, 2.586289644241333, 2.5772287845611572, 2.5811655521392822, 2.5825459957122803, 2.588222026824951, 2.5943994522094727, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.9890737533569336, 2.9071550369262695, 2.8188626766204834, 2.7494678497314453, 2.67634916305542, 2.6266491413116455, 2.5653467178344727, 2.5333642959594727, 2.4661786556243896, 2.4012131690979004, 2.3687829971313477, 2.323002338409424, 2.2887566089630127, 2.2677664756774902, 2.296781539916992, 2.3500185012817383, 2.360821008682251, 2.453289031982422, 2.4872214794158936, 2.548398017883301, 2.6022679805755615, 2.6568949222564697, 2.7322375774383545, 2.7981326580047607, 2.8849222660064697, 2.9328646659851074, 3.0372416973114014, inf, inf, inf, inf, inf, 3.4685451984405518, 3.4392693042755127, 3.423564910888672, 3.389524221420288, 3.3799402713775635, 3.355445146560669, 3.335869073867798, 3.295499086380005, 3.285273551940918, 3.2675883769989014, 3.2415120601654053, 3.2439682483673096, 3.21799898147583, 3.207578659057617, 3.2076492309570312, 3.3214356899261475, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1.7193019390106201, 1.679825782775879, 1.650679349899292, 1.6179615259170532, 1.5983997583389282, 1.5532128810882568, 1.5364797115325928, 1.5386948585510254, 1.5013322830200195, 1.4845850467681885, 1.4534012079238892, 1.444892168045044, 1.4262295961380005, 1.4062203168869019, 1.4057549238204956, 1.3824982643127441, 1.367220163345337, 1.3536320924758911, 1.3183528184890747, 1.3393183946609497, 1.312820553779602, 1.3034974336624146, 1.2918084859848022, 1.2986373901367188, 1.2754086256027222, 1.271276831626892, 1.2715413570404053, 1.2496140003204346, 1.220840334892273, 1.259627103805542, 1.2267930507659912, 1.2130810022354126, 1.2276153564453125, 1.2212096452713013, 1.281704306602478, 1.3779208660125732, 1.5410783290863037, 1.7324031591415405, 1.9674873352050781, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.966913938522339, 2.879478931427002, 2.812376022338867, 2.7323076725006104, 2.667478322982788, 2.613341808319092, 2.5557971000671387, 2.4918932914733887, 2.439162492752075, 2.3888156414031982, 2.3447256088256836, 2.304054021835327, 2.2600510120391846, 2.2221076488494873, 2.216076374053955, 2.2552261352539062, 2.31876802444458, 2.357189178466797, 2.396010398864746, 2.4466495513916016, 2.4985275268554688, 2.564828395843506, 2.634127140045166, 2.671659231185913, 2.7563955783843994, 2.829598903656006, 2.9014203548431396, 2.9869801998138428, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
        # o.scan = [0.7917926907539368, 0.7726407051086426, 0.8007383942604065, 0.7757819890975952, 0.7830960154533386, 0.7950111627578735, 0.7710974812507629, 0.7821449041366577, 0.7940475344657898, 0.7871696352958679, 0.7946920990943909, 0.7939556241035461, 0.8017406463623047, 0.7900116443634033, 0.8042625188827515, 0.7939649224281311, 0.7992954254150391, 0.8047687411308289, 0.8192911744117737, 0.8124468922615051, 0.832947313785553, 0.8400328755378723, 0.8291249871253967, 0.8525338172912598, 0.8497345447540283, 0.8600257635116577, 0.8569619059562683, 0.84441739320755, 0.8655028343200684, 0.8765812516212463, 0.8914832472801208, 0.8948587775230408, 0.8999851942062378, 0.9281346201896667, 0.9281526207923889, 0.94456946849823, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0.7172327041625977, 0.6576916575431824, 0.6279259920120239, 0.5956767201423645, 0.5892089605331421, 0.582546055316925, 0.5535716414451599, 0.5537811517715454, 0.5175555348396301, 0.5199891924858093, 0.508025586605072, 0.5082530379295349, 0.4872489869594574, 0.4842735826969147, 0.4685569107532501, 0.4653099477291107, 0.4716358482837677, 0.4698590636253357, 0.4596976339817047, 0.4707720875740051, 0.45507994294166565, 0.45707738399505615, 0.43959370255470276, 0.4444326162338257, 0.4340273141860962, 0.45207709074020386, 0.4311233162879944, 0.4439700245857239, 0.42915064096450806, 0.4158700108528137, 0.4352162182331085, 0.4193679690361023, 0.4123806059360504, 0.43130481243133545, 0.4267236292362213, 0.4229433536529541, 0.42877185344696045, 0.43627050518989563, 0.4371483027935028, 0.4480079710483551, 0.43388620018959045, 0.4475741386413574, 0.4533146321773529, 0.44968777894973755, 0.45370855927467346, 0.4468438923358917, 0.44578778743743896, 0.4511876106262207, 0.46346813440322876, 0.45497870445251465, 0.4704459011554718, 0.47878298163414, 0.47747379541397095, 0.4946269094944, 0.49690258502960205, 0.520801305770874, 0.5343156456947327, 0.5379177927970886, 0.5409355759620667, 0.5648964047431946, 0.5832909345626831, 0.5975152850151062, 0.6262582540512085, 0.6456323266029358, 0.6851587891578674, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 3.155334711074829, 3.0794477462768555, 2.999210834503174, 2.9282569885253906, 2.874490261077881, 2.782564401626587, 2.7169501781463623, 2.6661229133605957, 2.6084835529327393, 2.565688371658325, 2.505488634109497, 2.4565773010253906, 2.4241886138916016, 2.3942196369171143, 2.472306728363037, 2.48545241355896, 2.550550937652588, 2.580857038497925, 2.6243693828582764, 2.6946756839752197, 2.7529048919677734, 2.828749656677246, 2.8939626216888428, 2.96391224861145, 3.032355785369873, 3.1407675743103027, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0.9335517287254333, 0.9271457195281982, 0.8968163728713989, 0.9022393822669983, 0.9015713334083557, 0.8831477761268616, 0.88071608543396, 0.8636232018470764, 0.8638914227485657, 0.8579421043395996, 0.8423982262611389, 0.831680417060852, 0.8549240827560425, 0.822076141834259, 0.831861674785614, 0.8259243965148926, 0.8318639397621155, 0.8131091594696045, 0.7962908148765564, 0.8082799315452576, 0.7972084283828735, 0.8051087856292725, 0.7902615666389465, 0.79496830701828, 0.8023881316184998, 0.7880768179893494, 0.8002429008483887, 0.7811141610145569, 0.788637101650238, 0.7853605151176453]
        # o.scan = [0.8995394110679626, 0.8951486349105835, 0.903544545173645, 0.9036981463432312, 0.8950802087783813, 0.9182512760162354, 0.9235526323318481, 0.9172112941741943, 0.9063653945922852, 0.9126484990119934, 0.913860559463501, 0.9084697961807251, 0.9218591451644897, 0.9305413961410522, 0.9209679961204529, 0.925327718257904, 0.9510976076126099, 0.9550263285636902, 0.939818263053894, 0.9555159211158752, 0.9531345367431641, 0.9708322286605835, 0.9721596240997314, 1.0026278495788574, 0.9957859516143799, 1.0222132205963135, 0.997529149055481, 1.0227926969528198, 1.0208500623703003, 1.0485786199569702, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1.2352955341339111, 1.1913726329803467, 1.1483317613601685, 1.106541395187378, 1.0812039375305176, 1.0803948640823364, 1.0424354076385498, 1.0263440608978271, 1.0057766437530518, 0.9869506359100342, 1.0059523582458496, 0.9912660717964172, 0.972260057926178, 0.9771614670753479, 0.9703279733657837, 0.9403745532035828, 0.9574133157730103, 0.9525114893913269, 0.9529781937599182, 0.957824170589447, 0.9679775834083557, 0.9581012725830078, 0.9523892998695374, 0.9379926323890686, 0.9668952226638794, 0.9608214497566223, 0.9630183577537537, 0.9833088517189026, 0.9999158978462219, 0.9966202974319458, 1.0132396221160889, 1.0330312252044678, 1.031238317489624, 1.0463762283325195, 1.0800780057907104, 1.0879473686218262, 1.1306825876235962, 1.1658782958984375, 1.2193794250488281, 1.308205485343933, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.3014514446258545, 2.2776880264282227, 2.2405195236206055, 2.2132420539855957, 2.2124600410461426, 2.175757884979248, 0.9962849617004395, 0.9888795018196106, 0.9854515790939331, 0.9751061797142029, 0.9647365808486938, 0.9706140756607056, 0.9565560817718506, 0.9623816609382629, 0.9755213260650635, 0.9464287161827087, 0.9509914517402649, 0.9282284379005432, 0.9228813052177429, 0.9346316456794739, 0.9302662014961243, 0.9279423356056213, 0.9192213416099548, 0.9009017944335938, 0.9173764586448669, 0.9018693566322327, 0.9037917256355286, 0.9196485877037048, 0.900570809841156, 0.8940187096595764, 0.8984976410865784, 0.887376606464386, 0.8933980464935303, 0.9133570194244385, 0.9112231731414795]

        self.assertEqual(len(o.scan), 360)
        check_poses = PoseArray()
        check_poses.poses = [Pose(Point(0,0,0), Quaternion(0,0,0,1)), Pose(Point(-2,0,0), Quaternion(0,0,0,1)), Pose(Point(-2,-1,0), Quaternion(0,0,0,1))]
        self.assertEqual (False, o.point_collide(Point32(0,0,0)))
        self.assertEqual (False, o.path_collide(check_poses))

        check_poses.poses = [Pose(Point(0,0,0), Quaternion(0,0,0,1)), Pose(Point(-1,-1,0), Quaternion(0,0,0,1))]
        self.assertEqual (True, o.path_collide(check_poses))

        check_poses.poses = [Pose(Point(0,0,0), Quaternion(0,0,0,1)), Pose(Point(-2,-1,0), Quaternion(0,0,0,1))]
        self.assertEqual (False, o.path_collide(check_poses))

        check_poses.poses = [Pose(Point(0,0,0), Quaternion(0,0,0,1)), Pose(Point(-1,-2,0), Quaternion(0,0,0,1))]
        self.assertEqual (True, o.path_collide(check_poses))

if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)