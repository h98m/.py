import telebot
import requests
import uuid, random
from telebot import types

bot_token = "6139618894:AAFoba1LKhcJUlhZWUqtIhjOHmnAgTrbzLw"
user_agents = [
'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    'Instagram 113.0.0.39.122 Android (22/5.0.1; 640dpi; 1440x2560; samsung; SM-N920C; noblelte; exynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 640dpi; 1440x2560; samsung; SM-N950N; greatlteks; qcom; ko_KR)',
    'Instagram 113.0.0.39.122 Android (23/6.0; 640dpi; 1440x2560; samsung; SM-G920F; zeroflte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (28/9; 420dpi; 1080x2160; HUAWEI; EVA-L09; HWEVA; hi3660; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x2160; Xiaomi; MI 6; sagit; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 320dpi; 720x1280; HUAWEI; TAG-L21; HWTAG-L6753; mt6753; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935F; hero2lte; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (28/9; 320dpi; 720x1280; HUAWEI; DRA-L21; HWDRA-M; mt6735; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955F; dream2lte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G920I; zerofltexx; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G930F; herolte; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G9350; hero2qltechn; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (22/5.1.1; 320dpi; 720x1280; samsung; SM-G531H; fortuna3g; sc8830; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930V; heroltevzw; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 320dpi; 720x1280; samsung; SM-J510FN; j5xnlte; samsungexynos7580; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0; 480dpi; 1080x1920; samsung; SM-G900F; klte; samsungexynos5422; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930F; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G935P; hero2qltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (22/5.1.1; 320dpi; 720x1280; samsung; SM-G361H; coreprimeve3g; sc8830; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-A510F; a5xelte; samsungexynos7580; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0; 480dpi; 1080x1920; samsung; SM-G900P; kltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G935T; hero2qltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G930T; heroltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0; 320dpi; 720x1280; samsung; SM-G531F; grandprimeve3g; sc8830; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920G; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920I; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G930V; heroltevzw; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 320dpi; 720x1280; samsung; SM-J510FN; j5xnlte; samsungexynos7580; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0; 480dpi; 1080x1920; samsung; SM-G900F; klte; samsungexynos5422; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930F; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G935P; hero2qltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (22/5.1.1; 320dpi; 720x1280; samsung; SM-G361H; coreprimeve3g; sc8830; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-A510F; a5xelte; samsungexynos7580; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0; 480dpi; 1080x1920; samsung; SM-G900P; kltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G935T; hero2qltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G930T; heroltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0; 320dpi; 720x1280; samsung; SM-G531F; grandprimeve3g; sc8830; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920G; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920I; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 480dpi; 1080x1920; samsung; SM-G920T; zeroltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (22/5.1.1; 320dpi; 720x1280; samsung; SM-G531H; fortuna3g; sc8830; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 320dpi; 720x1280; samsung; SM-J500F; j5lte; samsungexynos3475; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930T1; heroltezt; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930U; herolte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 320dpi; 720x1280; samsung; SM-G935L; hero2ltektt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G935V; hero2qltevzw; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 320dpi; 720x1280; samsung; SM-J710F; j7xelte; samsungexynos7870; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-N950U1; greatqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935T; hero2ltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930P; nobleltespr; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950F; dreamlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950F; greatlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950F; greatltexx; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930U; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930W8; heroltebmc; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955U; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-J500M; j5lte; samsungexynos3475; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935U; hero2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930R6; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935S; hero2lteskt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920L; noblelteskt; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950U; dreamqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G955U1; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930V; nobleltevzw; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930T; nobleltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935K; hero2ltektt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U1; greatqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935T; hero2ltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950F; dreamlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950F; greatlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950F; greatltexx; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930U; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930W8; heroltebmc; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955U; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-J500M; j5lte; samsungexynos3475; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935U; hero2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930R6; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935S; hero2lteskt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920L; noblelteskt; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950U; dreamqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G955U1; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930V; nobleltevzw; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930T; nobleltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935K; hero2ltektt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U1; greatqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950F; greatltexx; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950F; dreamlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950F; greatlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930U; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930W8; heroltebmc; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955U; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-J500M; j5lte; samsungexynos3475; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935U; hero2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930R6; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935S; hero2lteskt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920L; noblelteskt; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950U; dreamqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G955U1; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930V; nobleltevzw; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930T; nobleltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935K; hero2ltektt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U1; greatqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950F; greatltexx; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950F; dreamlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950F; greatlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930U; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930W8; heroltebmc; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955U; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-J500M; j5lte; samsungexynos3475; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935U; hero2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930R6; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935S; hero2lteskt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920L; noblelteskt; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950U; dreamqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G955U1; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930V; nobleltevzw; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930T; nobleltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935K; hero2ltektt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U1; greatqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950F; greatltexx; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950F; dreamlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950F; greatlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930U; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930W8; heroltebmc; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955U; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-J500M; j5lte; samsungexynos3475; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935U; hero2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930R6; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935S; hero2lteskt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920L; noblelteskt; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950U; dreamqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G955U1; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930V; nobleltevzw; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930T; nobleltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935K; hero2ltektt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U1; greatqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950F; greatltexx; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950F; dreamlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950F; greatlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930U; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930W8; heroltebmc; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955U; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-J500M; j5lte; samsungexynos3475; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935U; hero2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G930R6; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935S; hero2lteskt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N920L; noblelteskt; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950U; dreamqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G955U1; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-N930V; nobleltevzw; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930T; nobleltetmo; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.2; 480dpi; 1080x1920; samsung; SM-G935K; hero2ltektt; samsungexynos8890; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U1; greatqlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-N950F; greatltexx; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930P; heroltespr; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 480dpi; 1080x1920; samsung; SM-G950F; dreamlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950F; greatlte; samsungexynos8895; en_US)',
    'Instagram 113.0.0.39.122 Android (27/8.1.0; 480dpi; 1080x1920; samsung; SM-N950U; greatqlte; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-N930U; noblelte; samsungexynos7420; en_US)',
    'Instagram 113.0.0.39.122 Android (25/7.1.1; 480dpi; 1080x1920; samsung; SM-G930W8; heroltebmc; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (26/8.0.0; 640dpi; 1440x2560; samsung; SM-G955U; dream2qlteue; qcom; en_US)',
    'Instagram 113.0.0.39.122 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-J500M; j5lte; samsungexynos3475; en_US)',    
    ]    
def get_random_user_agent():
    return random.choice(user_agents)
bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: message.text == "ريست")
def start(message):
    user_name = message.from_user.first_name
    
    ms=f"""
    
    <b>• مرحبًا {user_name} !</b>
    
- قم بارسال اليوزر او الايميل لعمل ريست
    
<b>• ملاحضه : يجب الرد على رسالة البوت بالايميل المراد عمل ريست اليه</b>
    
    
    """
    
    bot.reply_to(message, f'{ms}', parse_mode='HTML')

@bot.message_handler(func=lambda message: True)
def reset_password(message):
    if message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id:
        username = message.text
        headers = {
            "user-agent": get_random_user_agent()
        }
        data = {"user_email": username, "guid": uuid.uuid4(), "device_id": uuid.uuid4()}
        req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=headers, data=data)
        if 'Please wait a few minutes before you try again.' in req.text:
            bot.reply_to(message, "<b>يرجى الانتظار بضع دقائق قبل المحاولة مرة أخرى.</b>", parse_mode='HTML')
        elif 'obfuscated_email' in req.text:
            subscribe_button = types.InlineKeyboardButton("قناة المطور", url="https://t.me/b_azoka")
            markup = types.InlineKeyboardMarkup().add(subscribe_button)
            bot.reply_to(message, "<b>تم إرسال الريست ✅ </b>", parse_mode='HTML', reply_markup=markup)
        else:
            bot.reply_to(message, "<b>اليوزر خطأ او هناك خلل اخر ❌ </b>", parse_mode='HTML')

bot.polling()
