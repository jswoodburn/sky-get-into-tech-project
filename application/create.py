from application import db
from application.models import User, Journal, JournalTheme
from datetime import datetime

# EVERYONE RUN THIS TO GET DBS SYNCED UP
db.drop_all()
db.create_all()


users = {
    User(google_id='103378718328184231125', email='jackie.woodburn@gmail.com', first_name='Jackie'),
    User(google_id='103378718328184231126', email='jake.peralta@gmail.com', first_name='Jake'),
    User(google_id='103378718328184231127', email='amy.santiago@gmail.com', first_name='Amy'),
    User(google_id='103378718328184231128', email='raymond.holt@gmail.com', first_name='Ray'),
    User(google_id='103378718328184231129', email='terry.jeffords@gmail.com', first_name='Terry'),
    User(google_id='103378718328184231130', email='rosa.diaz@gmail.com', first_name='Rosa'),
    User(google_id='103378718328184231131', email='charles.boyle@gmail.com', first_name='Charles'),
    User(google_id='101399590782175635237', email='jessieauguste@gmail.com', first_name='Jessie')
}
db.session.add_all(users)
db.session.commit()


journals = {Journal(date_created="2021-01-14", time_created="18:45:01", author_id=1,
                    title="My first blog", entry="Nam quis massa ac mi laoreet finibus et id nibh. Nam a mi elementum, gravida augue nec, cursus elit. Nulla sodales, augue dictum iaculis pulvinar, risus metus suscipit lacus, in suscipit enim metus at dolor. In ac fermentum leo. Donec facilisis nibh quis mauris malesuada efficitur. Integer bibendum magna nec condimentum porta. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas."),
            Journal(date_created="2021-01-18", time_created="19:55:38", author_id=1,
                    title="Another day, another journal", entry="Vivamus rhoncus sem at tellus eleifend hendrerit. Nam a aliquet augue. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse volutpat, felis consequat posuere volutpat, leo dolor mattis arcu, vel commodo metus ipsum sed urna. Cras efficitur lectus nec turpis dignissim dignissim. Nunc viverra dictum libero, non ultrices urna placerat ut. Nullam dapibus quam diam, eget dictum neque tempor rutrum."),
            Journal(date_created="2021-01-25", time_created="11:35:21", author_id=2,
                    title="Mindfulness and Yoga", entry="Morbi viverra sem sit amet ante consectetur malesuada. Donec sit amet auctor nisi. Suspendisse in lorem commodo, pellentesque tortor sit amet, egestas nulla. Praesent eros purus, suscipit sed mattis ut, auctor sed enim. Mauris elementum placerat lectus, dapibus fermentum erat suscipit non. Pellentesque nec pharetra lorem. Sed ornare efficitur consectetur. Fusce mollis a nisl non facilisis. Mauris elementum nibh nec risus consequat fringilla. Duis volutpat enim eget mattis placerat. Aenean ut tincidunt enim, quis laoreet mi. Ut pulvinar bibendum ligula in cursus. Etiam feugiat massa purus, imperdiet blandit magna posuere non. Sed eget ante in justo varius mattis."),
            Journal(date_created="2021-01-26", time_created="17:24:52", author_id=1, deleted=True,
                    title="Mindful exercise", entry="Ut tempus massa eu maximus sollicitudin. Pellentesque viverra facilisis augue, ac iaculis lorem commodo at. Proin convallis at dolor et pretium. Etiam ultricies et enim quis accumsan. Mauris dui ante, vestibulum et dictum a, tincidunt a nisl. Duis sapien augue, varius id condimentum eget, sagittis in augue. Quisque mollis malesuada mi, id tempus dolor aliquet et. Maecenas gravida dui sit amet metus iaculis, vel dapibus nisi elementum. Integer aliquam tortor vel sapien finibus porttitor. Fusce eu justo et massa viverra fermentum in eget nisi. Vivamus commodo elit id elit ultricies, non sollicitudin elit rhoncus."),
            Journal(date_created="2021-02-03", time_created="00:15:20", author_id=1,
                    title="Taking a break", entry="Curabitur at purus vitae tellus vestibulum porta. Nulla non urna a leo maximus sagittis vel sit amet ex. Sed quis ultricies lorem. Sed vel mollis mauris. Mauris rhoncus pharetra tristique. Nam nec auctor erat. Ut suscipit risus et quam facilisis tempus. Donec efficitur pulvinar luctus."),
            Journal(date_created="2021-02-04", time_created="08:51:32", author_id=2,
                    title="Gardening brings me joy", entry="Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In magna nibh, fermentum a odio sit amet, rhoncus luctus nunc. Curabitur posuere aliquet nibh, at semper eros ultricies non. Fusce fringilla dui et ex feugiat feugiat. Integer non eros rutrum, facilisis nisi eu, tempus tortor. Phasellus congue laoreet ultricies. Etiam eget dignissim eros. Sed molestie nec nisl quis molestie. Pellentesque pharetra mauris ut ultrices feugiat. Vivamus sed commodo est. Praesent sodales vestibulum odio, et blandit nisi vehicula eu. Sed euismod lectus sed dolor convallis placerat. Sed nibh sapien, euismod eu ligula vitae, laoreet pharetra diam. Cras dictum pharetra felis eget tincidunt. Sed ac nibh quis augue pharetra sodales. Aenean eu iaculis magna, eleifend mollis lacus."),
            Journal(date_created="2021-02-05", time_created="09:44:44", author_id=5, deleted=True,
                    title="Minimising screentime", entry="Maecenas cursus ex feugiat erat venenatis, ultrices volutpat dui sagittis. Donec auctor nisi nunc, et posuere odio placerat tincidunt. Vivamus vitae quam sit amet erat ullamcorper sodales sed a lacus. Mauris tincidunt nisi quis pretium convallis. Nullam tellus ex, euismod nec elementum at, rhoncus ut mi. Maecenas vel consectetur sapien. Fusce ut finibus erat. Nunc ornare, sem faucibus pulvinar laoreet, nibh ligula congue nulla, id rutrum augue est a augue. Proin lectus justo, condimentum ut blandit a, cursus vitae velit. Etiam varius tortor nec lacus consequat ultrices. Curabitur luctus mauris ac arcu pellentesque, quis molestie ipsum faucibus. Aliquam tristique velit dolor, eu accumsan risus sodales eget."),
            Journal(date_created="2021-02-09", time_created="09:52:11", author_id=2,
                    title="Breathing in my lunch break", entry="Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent ipsum metus, mattis a lacus sit amet, auctor convallis odio. Etiam ut placerat tellus, at dignissim nibh. Nulla posuere orci vel ipsum posuere, eu feugiat neque ultrices. Integer eleifend ipsum urna, eu scelerisque dolor varius nec. Phasellus mauris arcu, scelerisque id arcu et, iaculis venenatis odio. Pellentesque efficitur, elit non pellentesque vestibulum, quam ipsum pellentesque nisl, eu sodales metus risus quis orci."),
            Journal(date_created="2021-02-19", time_created="15:45:17", author_id=3,
                    title="Making space for me", entry="Nullam in neque laoreet dui fermentum laoreet non vitae dolor. Sed sit amet lectus id nunc rutrum venenatis vel a magna. Nam in erat commodo, mattis eros id, venenatis nulla. Vestibulum eleifend eleifend purus sed semper. Nulla dui tellus, imperdiet non maximus ut, rutrum ac est. Nam ut nibh in tortor accumsan feugiat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec luctus leo sit amet aliquam bibendum. Suspendisse placerat condimentum ipsum sit amet placerat. Donec nec diam quis ex tincidunt hendrerit ut et nunc. Proin molestie aliquam sapien nec sollicitudin. Maecenas ut lorem vel diam feugiat volutpat non vitae augue. Aliquam ultrices efficitur nibh ac sagittis. Maecenas ornare consectetur consectetur. Pellentesque suscipit risus in molestie hendrerit. Proin in urna libero."),
            Journal(date_created="2021-02-22", time_created="16:50:37", author_id=1,
                    title="How to be more grounded...", entry="Fusce libero velit, scelerisque id nibh sit amet, imperdiet molestie diam. Morbi sit amet nisl ac felis tristique auctor. Sed luctus sagittis nulla quis ultrices. Ut ultrices lacus non elit vestibulum viverra. Proin auctor orci neque, sit amet facilisis mi vestibulum et. Mauris id erat ultricies, iaculis augue nec, mattis tellus. Praesent euismod urna sodales congue aliquet. Fusce in neque consequat, commodo velit in, accumsan odio. Fusce risus massa, aliquet ut gravida id, laoreet at massa. Praesent iaculis dignissim cursus. Suspendisse pellentesque turpis a neque dignissim interdum."),
            Journal(date_created="2021-02-25", time_created="20:30:21", author_id=4,
                    title="Blue light bad", entry="Ut quis ultrices tellus, ac euismod dui. Sed lorem diam, pellentesque fringilla lectus sed, condimentum interdum arcu. Mauris sodales dui a sapien vulputate accumsan. Quisque eu dignissim quam, quis semper diam. Aliquam mollis finibus orci, ut aliquam elit volutpat sed. Morbi feugiat, nunc commodo viverra varius, justo ante interdum quam, quis fermentum mi lectus id leo. Cras vulputate dolor nec odio tempor, a sollicitudin dui vestibulum. Nullam lobortis dictum vehicula."),
            Journal(date_created="2021-03-01", time_created="21:13:56", author_id=4,
                    title="How Digital Health helped me", entry="Donec auctor risus nec sem feugiat fringilla. Curabitur viverra mollis viverra. Nulla facilisi. Donec efficitur laoreet dolor nec molestie. Duis sit amet pulvinar tellus. Nam maximus ullamcorper augue at dignissim. Etiam dapibus ullamcorper purus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas vehicula arcu id risus faucibus, id molestie dui tempor. Sed leo erat, tristique vitae dui eget, molestie vulputate orci. Suspendisse at viverra urna, et posuere nulla."),
            Journal(date_created="2021-03-03", time_created="19:08:54", author_id=5,
                    title="How to take more breaks from the screen", entry="Phasellus volutpat augue nunc, quis fringilla massa vestibulum imperdiet. Sed ante mi, dignissim vel rhoncus suscipit, luctus nec est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In nisl ante, condimentum nec nunc nec, convallis pellentesque turpis. Ut interdum mollis sem fringilla blandit. Pellentesque odio augue, elementum at dui nec, pellentesque efficitur arcu. Pellentesque convallis facilisis nunc, sit amet volutpat lacus pulvinar ut. Maecenas mi lacus, auctor vel fermentum sed, molestie sit amet metus. Duis ultrices, felis sit amet aliquet congue, nibh libero porta justo, ac efficitur urna lorem non sapien. Sed ultricies, elit accumsan dapibus laoreet, augue elit posuere ante, sit amet interdum urna erat non lorem. Fusce fermentum dui vel vulputate interdum. In ornare, erat at vulputate cursus, odio est blandit dolor, vitae mattis enim felis at turpis."),
            Journal(date_created="2021-03-07", time_created="22:09:18", author_id=8, deleted=True,
                    title="Meditation and mindfulness", entry="Nam vitae sem a sapien tincidunt malesuada non ut massa. Phasellus rhoncus convallis maximus. Morbi ac feugiat nibh, vel blandit odio. Duis massa turpis, dignissim congue neque nec, posuere accumsan velit. Nulla dolor dui, dignissim nec urna eget, efficitur venenatis justo. Donec mattis, nisi gravida posuere dictum, purus massa malesuada ex, a mattis mi orci non justo. Nulla facilisi. Curabitur erat lacus, pulvinar a tellus quis, consectetur sagittis orci. Aenean rutrum vestibulum urna ut luctus. Aliquam sit amet tincidunt ipsum. Aliquam a magna felis. Vestibulum egestas feugiat finibus. Aliquam pharetra id lectus fringilla suscipit."),
            Journal(date_created="2021-03-08", time_created="22:01:43", author_id=3,
                    title="Self-compassion via meditation", entry="Vestibulum viverra nulla laoreet scelerisque varius. Pellentesque rutrum at elit vel volutpat. Nunc consequat risus quis metus ultrices posuere. Ut quis arcu lacus. Cras mollis lectus in libero auctor placerat. Sed ac nisi enim. Nam sagittis ullamcorper laoreet. Integer non mattis tortor. Praesent nec pulvinar velit. Integer dignissim est et nibh mollis viverra. Donec efficitur fermentum mauris, eget laoreet mi tempus vel. Nulla ac lectus sit amet dui mattis tincidunt. Fusce tempus massa non rhoncus porta."),
            Journal(date_created="2021-03-11", time_created="23:56:02", author_id=7,
                    title="Handiwork as mindfulness", entry="Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean sed mauris non lorem vulputate tincidunt vitae eu quam. Integer a varius justo. Vestibulum condimentum sagittis augue vel molestie. Vivamus consectetur suscipit turpis vel dapibus. Pellentesque ultricies euismod euismod. Donec porttitor et mauris eu vestibulum. Integer nec gravida purus. Aliquam dignissim sapien convallis, consectetur nisi id, viverra neque. Etiam eu volutpat felis. Praesent pulvinar justo augue, ut posuere nulla fermentum vitae. Duis aliquam mauris sed dui blandit dapibus. Quisque condimentum mauris nisi, in suscipit libero iaculis ac. In vel magna commodo, sagittis nunc in, ultrices sapien. Integer a justo elementum, varius lorem at, commodo turpis. Sed nec mi massa."),
            Journal(date_created="2021-03-12", time_created="11:51:32", author_id=7,
                    title="Caring for houseplants; caring for yourself", entry="Duis convallis ut felis sollicitudin tempor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam nunc ligula, rhoncus eu dolor a, consectetur suscipit metus. Aenean posuere arcu quis lectus interdum, vitae rhoncus tellus auctor. Vivamus nisl purus, convallis ut nulla sit amet, vulputate volutpat enim. Curabitur suscipit pretium dui rutrum pretium. Maecenas tristique aliquet nulla et imperdiet. Integer rhoncus felis arcu, vel volutpat massa accumsan nec. Praesent eget nisi porttitor, aliquet sem sed, ullamcorper tortor."),
            Journal(date_created="2021-03-22", time_created="14:51:29", author_id=5,
                    title="Music recommendations for meditation", entry="Donec non urna et urna convallis suscipit. Proin facilisis mattis dui nec ullamcorper. Vivamus nec dictum est, non pellentesque magna. Proin molestie tortor ut porttitor luctus. Praesent finibus varius pulvinar. Cras nec nibh convallis, varius est in, accumsan elit. Vestibulum id massa tortor. Vivamus et felis lacinia, tincidunt nibh vehicula, facilisis purus. Nulla viverra ipsum eu ante commodo mollis. Sed maximus aliquam tincidunt. Vivamus finibus at arcu at tempor."),
            Journal(date_created="2021-03-28", time_created="18:23:19", author_id=8,
                    title="Breaking out of the doom-scrolling cycle", entry="Nam auctor, massa et efficitur placerat, mauris nunc pharetra orci, a placerat dui sem vel est. Etiam vitae vulputate felis, eget porta velit. Sed sed eros elit. Sed scelerisque ultricies placerat. Donec viverra purus mauris, eu porta lorem facilisis semper. Ut pellentesque turpis vitae vestibulum blandit. Etiam libero mi, finibus quis purus non, maximus bibendum dui. Donec tristique dictum enim vel vehicula. In molestie metus vel interdum aliquet. Mauris ultrices leo et justo tincidunt, ut euismod est lacinia."),
            Journal(date_created="2021-03-30", time_created="21:34:30", author_id=8,
                    title="How art helped me take a break from the screen", entry="Suspendisse nunc elit, consectetur in pharetra nec, volutpat a elit. Aliquam bibendum venenatis ligula in blandit. Nam vitae neque at augue tempor consequat eu id leo. Donec eleifend non nibh eget pharetra. Duis facilisis lobortis nibh, quis feugiat neque tristique et. Aliquam lobortis quis dolor eu viverra. Aliquam aliquam tortor ut velit commodo mollis. Nulla efficitur est est, et porta leo vehicula eget. Ut mattis pellentesque egestas. Donec nunc nunc, feugiat vitae ornare a, blandit in ligula."),
            Journal(date_created="2021-04-01", time_created="16:56:49", author_id=3,
                    title="Meditation in yoga: how it differs from daily meditation", entry="Integer a dictum ipsum, euismod venenatis ex. Ut imperdiet, odio a maximus ultricies, magna nibh sodales nulla, sit amet accumsan purus massa et dolor. Etiam fringilla iaculis enim, id bibendum diam consectetur at. Praesent velit urna, iaculis euismod massa consequat, pharetra lobortis dui. Morbi convallis, arcu in sagittis fringilla, leo mauris cursus lorem, at consectetur mi lorem vitae odio. Maecenas rhoncus consectetur enim, vitae faucibus lorem iaculis eget. Mauris tristique laoreet eleifend. Aenean vitae orci varius, pretium metus in, egestas mauris. Morbi interdum urna lobortis ipsum tristique commodo. Phasellus auctor a augue sed ultricies. Aliquam a massa in ipsum cursus volutpat in molestie eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum condimentum, dui a semper porttitor, elit sem maximus nisi, vitae cursus diam turpis sit amet dui."),
            Journal(date_created="2021-04-10", time_created="06:35:18", author_id=8,
                    title="Self-compassion vs. self-discipline", entry="Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam ut massa cursus, iaculis risus quis, euismod orci. Donec eget orci ut nunc venenatis gravida vel eget risus. Quisque sit amet mattis sapien, eu sodales mauris. Nunc varius bibendum felis, nec scelerisque risus congue eget. Vivamus porttitor, ante id posuere gravida, arcu risus scelerisque nisi, et porta massa mauris vel libero. Sed est nulla, rhoncus et lacinia in, tincidunt vel augue. Suspendisse potenti. Aenean dapibus nisi ut ante efficitur efficitur. Morbi ac justo imperdiet, dapibus arcu eu, vehicula turpis. Curabitur id turpis ac nunc lobortis suscipit a in eros. Sed eget urna et lacus elementum ultrices. Nullam vitae ligula sed risus luctus luctus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc mollis eleifend aliquet."),
            Journal(date_created="2021-04-11", time_created="09:51:24", author_id=8,
                    title="Making space for me-time", entry="In hac habitasse platea dictumst. Nunc eget leo lobortis, sodales massa in, ultrices nisi. Pellentesque maximus libero vel augue iaculis gravida. Aenean bibendum orci a lorem ornare vehicula. Vivamus urna nibh, ornare non ornare eget, imperdiet eget risus. Nam lacus diam, lacinia sed erat ac, molestie vehicula dui. Duis malesuada posuere risus id vulputate. Pellentesque scelerisque ante eget consequat imperdiet. Maecenas sit amet odio risus."),
            Journal(date_created="2021-04-14", time_created="07:25:28", author_id=2,
                    title="Today was a bad day, but...", entry="Donec tellus libero, vulputate vel mollis ut, semper vitae lorem. Integer ut mi erat. Fusce ut enim a enim bibendum elementum ut quis mauris. Aliquam dictum nunc eros, ac blandit nulla pretium a. Donec congue justo blandit, bibendum nisi ac, ullamcorper metus. Vivamus semper tempor ipsum, nec rutrum nisl sollicitudin eu. Fusce mattis purus in mattis finibus. Nulla eget commodo elit. Sed lobortis orci sollicitudin maximus interdum. Pellentesque quis pulvinar ipsum, eget hendrerit nisi. Fusce et iaculis enim. Mauris hendrerit luctus tortor, ut porttitor dolor varius in. In volutpat, sem at consectetur sodales, enim felis fringilla turpis, ut molestie quam metus ac mi. Suspendisse accumsan tortor urna, sit amet suscipit arcu molestie a. Suspendisse tellus lectus, cursus et diam nec, tempus pellentesque tellus."),
            Journal(date_created="2021-04-18", time_created="07:18:59", author_id=5,
                    title="Reflecting on the hard times", entry="Nullam sagittis, odio eget interdum fringilla, dui augue dapibus dui, convallis scelerisque dui enim quis arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed interdum condimentum neque non aliquam. Aliquam rhoncus ex at metus finibus, sit amet rutrum mauris laoreet. Fusce lacinia porttitor euismod. Donec ut feugiat neque. Aliquam erat volutpat. Suspendisse potenti."),
            Journal(date_created="2021-04-29", time_created="20:45:33", author_id=2,
                    title="Taking a break from breaking news", entry="Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras semper faucibus urna eu sollicitudin. In quis commodo felis. Quisque egestas, lectus id tincidunt tempus, purus nisl dignissim sem, eget congue nisi orci ac est. Ut ut tortor ipsum. Nulla laoreet, diam eu tempus dictum, erat risus volutpat nulla, non semper dui enim sit amet metus. Suspendisse in maximus nibh. In turpis diam, ultricies id pretium a, posuere a mi. Donec vel tristique lectus. Nunc euismod urna odio, vel vehicula leo accumsan id. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Integer molestie nisi urna. Integer fermentum dui felis, vitae ornare nisl sodales id. Ut iaculis sem eget sem porta, sit amet sagittis arcu molestie. Morbi quis elementum est, in congue eros. Maecenas eu malesuada leo."),
            Journal(date_created="2021-05-01", time_created="05:44:55", author_id=4,
                    title="From fast-paced to the slow-lane", entry="Sed vitae mauris cursus, porttitor nibh id, ornare massa. Suspendisse suscipit hendrerit eros, nec scelerisque neque. Nulla lobortis augue pharetra sem egestas ultrices. Pellentesque vitae libero est. Pellentesque sit amet porttitor arcu. Mauris sit amet arcu sit amet nunc tempor iaculis quis eu arcu. Proin erat erat, facilisis eu justo sit amet, porta finibus risus. Aliquam laoreet pharetra nibh tempor tincidunt. Integer tellus lorem, suscipit in tellus et, euismod consequat nibh. Integer facilisis libero eget metus iaculis, at convallis tellus ullamcorper. Etiam eget iaculis ante, eu malesuada nisi. Sed dignissim dignissim molestie. Duis lacus nisl, dapibus pharetra sagittis non, semper vel dui. Aenean lobortis, purus aliquet aliquet bibendum, tellus ante convallis eros, id viverra metus ligula a diam."),
            Journal(date_created="2021-05-03", time_created="16:56:21", author_id=7,
                    title="How to lessen blue light in your life...", entry="Quisque volutpat tempus sagittis. Etiam ultricies malesuada purus, sed fermentum turpis. Donec vitae luctus sem. Integer metus metus, tincidunt at malesuada nec, pellentesque in magna. Vestibulum orci nisi, volutpat hendrerit risus nec, congue molestie ante. Aenean volutpat finibus porttitor. Proin pharetra orci ut nisi elementum posuere. Aenean vitae mi et massa faucibus convallis.")
}
db.session.add_all(journals)
db.session.commit()


themes = {
    JournalTheme(theme='What things make me feel alive and fulfilled?'),
    JournalTheme(theme='What things in my life can I be grateful for today?'),
    JournalTheme(theme='Inner Strength'),
    JournalTheme(theme='Self Care'),
    JournalTheme(theme='Checking in with yourself'),
    JournalTheme(theme='What might challenge me today?'),
    JournalTheme(theme='What are my most important values?'),
    JournalTheme(theme='How am I impacting other people around me daily?'),
    JournalTheme(theme='Connection')
}
db.session.add_all(themes)
db.session.commit()
