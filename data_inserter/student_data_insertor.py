from pymongo import MongoClient

client = MongoClient("mongodb+srv://dinesh_23:tc97386@cluster0.7a7ovpk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mess"]


collection_students = db["students"]
data_students = [
    {
        "name": "Fdruzs",
        "roll_no": "CS24BTECH11001",
        "email": "cs24btech11001@iith.ac.in",
        "passwd": "H%r!#ba",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Flvxlg",
        "roll_no": "CS24BTECH11002",
        "email": "cs24btech11002@iith.ac.in",
        "passwd": ")x%@/*f",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Uhaydj",
        "roll_no": "CS24BTECH11003",
        "email": "cs24btech11003@iith.ac.in",
        "passwd": ";K|`p73",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Dniism",
        "roll_no": "CS24BTECH11004",
        "email": "cs24btech11004@iith.ac.in",
        "passwd": "G]1},j8",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cdtbav",
        "roll_no": "CS24BTECH11005",
        "email": "cs24btech11005@iith.ac.in",
        "passwd": "VDZ(vx#",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Oifcwp",
        "roll_no": "CS24BTECH11006",
        "email": "cs24btech11006@iith.ac.in",
        "passwd": "o\\8)p72",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Bffqmc",
        "roll_no": "CS24BTECH11007",
        "email": "cs24btech11007@iith.ac.in",
        "passwd": "2]1j&|}",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Tkcolm",
        "roll_no": "CS24BTECH11008",
        "email": "cs24btech11008@iith.ac.in",
        "passwd": "~[u.Ft}",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sljvxc",
        "roll_no": "CS24BTECH11009",
        "email": "cs24btech11009@iith.ac.in",
        "passwd": "Fk'wuUX",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ryehjr",
        "roll_no": "CS24BTECH11010",
        "email": "cs24btech11010@iith.ac.in",
        "passwd": "<Y#|+CD",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xkwhan",
        "roll_no": "CS24BTECH11011",
        "email": "cs24btech11011@iith.ac.in",
        "passwd": "p[bcIIB",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Yecmps",
        "roll_no": "CS24BTECH11012",
        "email": "cs24btech11012@iith.ac.in",
        "passwd": "m}N50ST",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Imvpdi",
        "roll_no": "CS24BTECH11013",
        "email": "cs24btech11013@iith.ac.in",
        "passwd": "y/\"\"QFV",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vlieyf",
        "roll_no": "CS24BTECH11014",
        "email": "cs24btech11014@iith.ac.in",
        "passwd": "GCJ;(gJ",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Uctnks",
        "roll_no": "CS24BTECH11015",
        "email": "cs24btech11015@iith.ac.in",
        "passwd": "Z5dQWYq",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Pmqwcc",
        "roll_no": "CS24BTECH11016",
        "email": "cs24btech11016@iith.ac.in",
        "passwd": "\\r^dwU)",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Nazdij",
        "roll_no": "CS24BTECH11017",
        "email": "cs24btech11017@iith.ac.in",
        "passwd": "zW]\\j/w",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Kuuxtc",
        "roll_no": "CS24BTECH11018",
        "email": "cs24btech11018@iith.ac.in",
        "passwd": "]yrqIw7",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qhnrop",
        "roll_no": "CS24BTECH11019",
        "email": "cs24btech11019@iith.ac.in",
        "passwd": "8c^YXxa",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Lytqwz",
        "roll_no": "CS24BTECH11020",
        "email": "cs24btech11020@iith.ac.in",
        "passwd": "0{,f3v'",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Gmbvmo",
        "roll_no": "CS24BTECH11021",
        "email": "cs24btech11021@iith.ac.in",
        "passwd": "L3+??YV",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Hslvgz",
        "roll_no": "CS24BTECH11022",
        "email": "cs24btech11022@iith.ac.in",
        "passwd": "w7kes%O",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Rmzsye",
        "roll_no": "CS24BTECH11023",
        "email": "cs24btech11023@iith.ac.in",
        "passwd": "l,{qpr|",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xkrqex",
        "roll_no": "CS24BTECH11024",
        "email": "cs24btech11024@iith.ac.in",
        "passwd": "5H:&B<e",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ephowc",
        "roll_no": "CS24BTECH11025",
        "email": "cs24btech11025@iith.ac.in",
        "passwd": "vS%_K*\"",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ucycsq",
        "roll_no": "CS24BTECH11026",
        "email": "cs24btech11026@iith.ac.in",
        "passwd": ".N>QwB-",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mkhwwn",
        "roll_no": "CS24BTECH11027",
        "email": "cs24btech11027@iith.ac.in",
        "passwd": "7K}zql7",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ewuqlg",
        "roll_no": "CS24BTECH11028",
        "email": "cs24btech11028@iith.ac.in",
        "passwd": "$,%=%`6",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Zazotz",
        "roll_no": "CS24BTECH11029",
        "email": "cs24btech11029@iith.ac.in",
        "passwd": ".>bf%^5",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Kjtjff",
        "roll_no": "CS24BTECH11030",
        "email": "cs24btech11030@iith.ac.in",
        "passwd": "e39oE2M",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wacpgn",
        "roll_no": "CS24BTECH11031",
        "email": "cs24btech11031@iith.ac.in",
        "passwd": "~d~H~(H",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vebmuh",
        "roll_no": "CS24BTECH11032",
        "email": "cs24btech11032@iith.ac.in",
        "passwd": "=\"-lb)L",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vpqtny",
        "roll_no": "CS24BTECH11033",
        "email": "cs24btech11033@iith.ac.in",
        "passwd": "gU>,ctV",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Lxporj",
        "roll_no": "CS24BTECH11034",
        "email": "cs24btech11034@iith.ac.in",
        "passwd": "M,{;\\P\"",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Yjkzis",
        "roll_no": "CS24BTECH11035",
        "email": "cs24btech11035@iith.ac.in",
        "passwd": ")@jZyT>",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vadglq",
        "roll_no": "CS24BTECH11036",
        "email": "cs24btech11036@iith.ac.in",
        "passwd": "X2ab_jU",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bjkjkb",
        "roll_no": "CS24BTECH11037",
        "email": "cs24btech11037@iith.ac.in",
        "passwd": "]AotKQ(",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Glxxne",
        "roll_no": "CS24BTECH11038",
        "email": "cs24btech11038@iith.ac.in",
        "passwd": "lwKDemS",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ktlgqu",
        "roll_no": "CS24BTECH11039",
        "email": "cs24btech11039@iith.ac.in",
        "passwd": "5QxT,x#",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Prxrwk",
        "roll_no": "CS24BTECH11040",
        "email": "cs24btech11040@iith.ac.in",
        "passwd": "UQ!cqt_",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wrzljz",
        "roll_no": "CS24BTECH11041",
        "email": "cs24btech11041@iith.ac.in",
        "passwd": "N3{%$D>",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tmemvg",
        "roll_no": "CS24BTECH11042",
        "email": "cs24btech11042@iith.ac.in",
        "passwd": "K:wN)o6",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wlktzn",
        "roll_no": "CS24BTECH11043",
        "email": "cs24btech11043@iith.ac.in",
        "passwd": "m4t:7:V",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Huzgpu",
        "roll_no": "CS24BTECH11044",
        "email": "cs24btech11044@iith.ac.in",
        "passwd": ",p1bWUQ",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Sjecyk",
        "roll_no": "CS24BTECH11045",
        "email": "cs24btech11045@iith.ac.in",
        "passwd": "g`NL5l0",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ykgjhu",
        "roll_no": "CS24BTECH11046",
        "email": "cs24btech11046@iith.ac.in",
        "passwd": ",-s0_N@",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ppwzto",
        "roll_no": "CS24BTECH11047",
        "email": "cs24btech11047@iith.ac.in",
        "passwd": "46mp0*1",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Yjgdbh",
        "roll_no": "CS24BTECH11048",
        "email": "cs24btech11048@iith.ac.in",
        "passwd": "2X#fm#w",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vbehci",
        "roll_no": "CS24BTECH11049",
        "email": "cs24btech11049@iith.ac.in",
        "passwd": "@\"H+8T_",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jbnkwe",
        "roll_no": "CS24BTECH11050",
        "email": "cs24btech11050@iith.ac.in",
        "passwd": "fA*l0S1",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Uczedm",
        "roll_no": "CS24BTECH11051",
        "email": "cs24btech11051@iith.ac.in",
        "passwd": ";\\4DUBa",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Nkhiwn",
        "roll_no": "CS24BTECH11052",
        "email": "cs24btech11052@iith.ac.in",
        "passwd": "nQDIB)C",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jucyhu",
        "roll_no": "CS24BTECH11053",
        "email": "cs24btech11053@iith.ac.in",
        "passwd": "_'MxtjA",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Utipyy",
        "roll_no": "CS24BTECH11054",
        "email": "cs24btech11054@iith.ac.in",
        "passwd": "Z\"2.MdY",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vftyfa",
        "roll_no": "CS24BTECH11055",
        "email": "cs24btech11055@iith.ac.in",
        "passwd": "mq+(Gtf",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Tokiuo",
        "roll_no": "CS24BTECH11056",
        "email": "cs24btech11056@iith.ac.in",
        "passwd": "%0?:$*1",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sslsza",
        "roll_no": "CS24BTECH11057",
        "email": "cs24btech11057@iith.ac.in",
        "passwd": "OBjD9yl",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Nkuofp",
        "roll_no": "CS24BTECH11058",
        "email": "cs24btech11058@iith.ac.in",
        "passwd": "0'e.MSj",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Xptjkh",
        "roll_no": "CS24BTECH11059",
        "email": "cs24btech11059@iith.ac.in",
        "passwd": "arP`.\\r",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Kyvman",
        "roll_no": "CS24BTECH11060",
        "email": "cs24btech11060@iith.ac.in",
        "passwd": "%%88aQ>",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ilnjoq",
        "roll_no": "CS24BTECH11061",
        "email": "cs24btech11061@iith.ac.in",
        "passwd": "f5nrd?4",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rkyadx",
        "roll_no": "CS24BTECH11062",
        "email": "cs24btech11062@iith.ac.in",
        "passwd": "<Pk$^v$",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Nikfdg",
        "roll_no": "CS24BTECH11063",
        "email": "cs24btech11063@iith.ac.in",
        "passwd": "!\\0R}QV",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Aphnap",
        "roll_no": "CS24BTECH11064",
        "email": "cs24btech11064@iith.ac.in",
        "passwd": "|SiMOpT",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Hxrtxk",
        "roll_no": "CS24BTECH11065",
        "email": "cs24btech11065@iith.ac.in",
        "passwd": "Ut6~fl,",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Imikkq",
        "roll_no": "AI24BTECH11001",
        "email": "ai24btech11001@iith.ac.in",
        "passwd": "#Uxu`du",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Yyvdfx",
        "roll_no": "AI24BTECH11002",
        "email": "ai24btech11002@iith.ac.in",
        "passwd": "NGLL;&S",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vgvfrx",
        "roll_no": "AI24BTECH11003",
        "email": "ai24btech11003@iith.ac.in",
        "passwd": "}:!\"iwL",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Anshii",
        "roll_no": "AI24BTECH11004",
        "email": "ai24btech11004@iith.ac.in",
        "passwd": "C7*gGd~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Eivrjv",
        "roll_no": "AI24BTECH11005",
        "email": "ai24btech11005@iith.ac.in",
        "passwd": "BGMk3g^",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gllrmd",
        "roll_no": "AI24BTECH11006",
        "email": "ai24btech11006@iith.ac.in",
        "passwd": "h\"`eP{a",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ooxqib",
        "roll_no": "AI24BTECH11007",
        "email": "ai24btech11007@iith.ac.in",
        "passwd": "L8yqv1Y",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jncvwq",
        "roll_no": "AI24BTECH11008",
        "email": "ai24btech11008@iith.ac.in",
        "passwd": "goDE?fV",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vksoro",
        "roll_no": "AI24BTECH11009",
        "email": "ai24btech11009@iith.ac.in",
        "passwd": "k'$]9x~",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Eeanuk",
        "roll_no": "AI24BTECH11010",
        "email": "ai24btech11010@iith.ac.in",
        "passwd": "n<ApJk@",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Arhfnj",
        "roll_no": "AI24BTECH11011",
        "email": "ai24btech11011@iith.ac.in",
        "passwd": "EM;\"O]*",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Auhutp",
        "roll_no": "AI24BTECH11012",
        "email": "ai24btech11012@iith.ac.in",
        "passwd": "5UdW#Su",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Exexxq",
        "roll_no": "AI24BTECH11013",
        "email": "ai24btech11013@iith.ac.in",
        "passwd": "[rB@Cb}",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Fdburo",
        "roll_no": "AI24BTECH11014",
        "email": "ai24btech11014@iith.ac.in",
        "passwd": "m(1C{xD",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Smbtbb",
        "roll_no": "AI24BTECH11015",
        "email": "ai24btech11015@iith.ac.in",
        "passwd": "{;,VZiO",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Evlmlq",
        "roll_no": "AI24BTECH11016",
        "email": "ai24btech11016@iith.ac.in",
        "passwd": "GR.'Wrg",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xmbfss",
        "roll_no": "AI24BTECH11017",
        "email": "ai24btech11017@iith.ac.in",
        "passwd": "1zUUlBr",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ozekfy",
        "roll_no": "AI24BTECH11018",
        "email": "ai24btech11018@iith.ac.in",
        "passwd": "!Nl&%C3",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xiliwk",
        "roll_no": "AI24BTECH11019",
        "email": "ai24btech11019@iith.ac.in",
        "passwd": "}PoW^#L",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Evsknc",
        "roll_no": "AI24BTECH11020",
        "email": "ai24btech11020@iith.ac.in",
        "passwd": "6<q$aiJ",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gaocyi",
        "roll_no": "AI24BTECH11021",
        "email": "ai24btech11021@iith.ac.in",
        "passwd": "AH4p7a'",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wdlsjh",
        "roll_no": "AI24BTECH11022",
        "email": "ai24btech11022@iith.ac.in",
        "passwd": "9|WpyNU",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cttxvr",
        "roll_no": "AI24BTECH11023",
        "email": "ai24btech11023@iith.ac.in",
        "passwd": "t\"eGh\"%",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Pwiytf",
        "roll_no": "AI24BTECH11024",
        "email": "ai24btech11024@iith.ac.in",
        "passwd": "\\7*^[qm",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wyzyhw",
        "roll_no": "AI24BTECH11025",
        "email": "ai24btech11025@iith.ac.in",
        "passwd": "o)1dy\\+",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Keazan",
        "roll_no": "AI24BTECH11026",
        "email": "ai24btech11026@iith.ac.in",
        "passwd": "\\zWp\\(P",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pqshoo",
        "roll_no": "AI24BTECH11027",
        "email": "ai24btech11027@iith.ac.in",
        "passwd": "[9d`KOI",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sdyhcl",
        "roll_no": "AI24BTECH11028",
        "email": "ai24btech11028@iith.ac.in",
        "passwd": "_#B`;Q8",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Klilgd",
        "roll_no": "AI24BTECH11029",
        "email": "ai24btech11029@iith.ac.in",
        "passwd": "|X--$-^",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vkwakp",
        "roll_no": "AI24BTECH11030",
        "email": "ai24btech11030@iith.ac.in",
        "passwd": "R-[9Tb(",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Rnkyhy",
        "roll_no": "AI24BTECH11031",
        "email": "ai24btech11031@iith.ac.in",
        "passwd": "h:lKB(~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nbgtmt",
        "roll_no": "AI24BTECH11032",
        "email": "ai24btech11032@iith.ac.in",
        "passwd": "Z;dmrEl",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vbyfye",
        "roll_no": "AI24BTECH11033",
        "email": "ai24btech11033@iith.ac.in",
        "passwd": "E={{HK;",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qieiyz",
        "roll_no": "AI24BTECH11034",
        "email": "ai24btech11034@iith.ac.in",
        "passwd": "Eg?gtVh",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Uspcyj",
        "roll_no": "AI24BTECH11035",
        "email": "ai24btech11035@iith.ac.in",
        "passwd": "Vu/4r\\p",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Cmhgxt",
        "roll_no": "AI24BTECH11036",
        "email": "ai24btech11036@iith.ac.in",
        "passwd": "a<a<mGU",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rsdgyl",
        "roll_no": "AI24BTECH11037",
        "email": "ai24btech11037@iith.ac.in",
        "passwd": "iin$r5S",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Lfwldd",
        "roll_no": "AI24BTECH11038",
        "email": "ai24btech11038@iith.ac.in",
        "passwd": "zdtd.G!",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Poipgm",
        "roll_no": "AI24BTECH11039",
        "email": "ai24btech11039@iith.ac.in",
        "passwd": "R]A=V>Z",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wvuosp",
        "roll_no": "AI24BTECH11040",
        "email": "ai24btech11040@iith.ac.in",
        "passwd": ")Kt}7bY",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vjlkwj",
        "roll_no": "AI24BTECH11041",
        "email": "ai24btech11041@iith.ac.in",
        "passwd": "D,-~21e",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wjyrbq",
        "roll_no": "AI24BTECH11042",
        "email": "ai24btech11042@iith.ac.in",
        "passwd": "]6mi2+x",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wjzuhf",
        "roll_no": "AI24BTECH11043",
        "email": "ai24btech11043@iith.ac.in",
        "passwd": "zxgGMe.",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jawfoq",
        "roll_no": "AI24BTECH11044",
        "email": "ai24btech11044@iith.ac.in",
        "passwd": "}zuVin~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vmqzgs",
        "roll_no": "AI24BTECH11045",
        "email": "ai24btech11045@iith.ac.in",
        "passwd": "n]=\\;<-",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vngxlk",
        "roll_no": "AI24BTECH11046",
        "email": "ai24btech11046@iith.ac.in",
        "passwd": "P9jTsWJ",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Pggvun",
        "roll_no": "AI24BTECH11047",
        "email": "ai24btech11047@iith.ac.in",
        "passwd": "gGgJND6",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mgxscq",
        "roll_no": "AI24BTECH11048",
        "email": "ai24btech11048@iith.ac.in",
        "passwd": "|q3~P-u",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dojjou",
        "roll_no": "AI24BTECH11049",
        "email": "ai24btech11049@iith.ac.in",
        "passwd": "vSXh)qE",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nglxft",
        "roll_no": "AI24BTECH11050",
        "email": "ai24btech11050@iith.ac.in",
        "passwd": "g('sq&6",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rpeqdy",
        "roll_no": "AI24BTECH11051",
        "email": "ai24btech11051@iith.ac.in",
        "passwd": "xGEgpZ:",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Kpmejl",
        "roll_no": "AI24BTECH11052",
        "email": "ai24btech11052@iith.ac.in",
        "passwd": "1j2oh&&",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Teuatb",
        "roll_no": "AI24BTECH11053",
        "email": "ai24btech11053@iith.ac.in",
        "passwd": "H.9YKw4",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ouyqjt",
        "roll_no": "AI24BTECH11054",
        "email": "ai24btech11054@iith.ac.in",
        "passwd": "qq{U_1D",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Cnihxx",
        "roll_no": "AI24BTECH11055",
        "email": "ai24btech11055@iith.ac.in",
        "passwd": "78~O4Ra",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dnomnx",
        "roll_no": "AI24BTECH11056",
        "email": "ai24btech11056@iith.ac.in",
        "passwd": "CdeAIXk",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Kkzwxn",
        "roll_no": "AI24BTECH11057",
        "email": "ai24btech11057@iith.ac.in",
        "passwd": "Wj%ZR[[",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mlizxs",
        "roll_no": "AI24BTECH11058",
        "email": "ai24btech11058@iith.ac.in",
        "passwd": "g-0+%R=",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qqaaqi",
        "roll_no": "AI24BTECH11059",
        "email": "ai24btech11059@iith.ac.in",
        "passwd": "4Zpe$6k",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pjnstb",
        "roll_no": "AI24BTECH11060",
        "email": "ai24btech11060@iith.ac.in",
        "passwd": "8/bwQ4e",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ezwoly",
        "roll_no": "AI24BTECH11061",
        "email": "ai24btech11061@iith.ac.in",
        "passwd": "{bJA9Y]",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Onjycl",
        "roll_no": "AI24BTECH11062",
        "email": "ai24btech11062@iith.ac.in",
        "passwd": "^PsKAK.",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Auofpk",
        "roll_no": "AI24BTECH11063",
        "email": "ai24btech11063@iith.ac.in",
        "passwd": "x[vluLF",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qgijac",
        "roll_no": "AI24BTECH11064",
        "email": "ai24btech11064@iith.ac.in",
        "passwd": "t3BnPN2",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cabavs",
        "roll_no": "CO24BTECH11001",
        "email": "co24btech11001@iith.ac.in",
        "passwd": "sGo8DZv",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Foslxe",
        "roll_no": "CO24BTECH11002",
        "email": "co24btech11002@iith.ac.in",
        "passwd": "Ym(:&DC",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Dppvsv",
        "roll_no": "CO24BTECH11003",
        "email": "co24btech11003@iith.ac.in",
        "passwd": "zLb^[j4",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Xmrjwx",
        "roll_no": "CO24BTECH11004",
        "email": "co24btech11004@iith.ac.in",
        "passwd": "91f_mpQ",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dkctuz",
        "roll_no": "CO24BTECH11005",
        "email": "co24btech11005@iith.ac.in",
        "passwd": "o4X{0(J",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wyvvtm",
        "roll_no": "CO24BTECH11006",
        "email": "co24btech11006@iith.ac.in",
        "passwd": "4;b|lD,",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Prghpk",
        "roll_no": "CO24BTECH11007",
        "email": "co24btech11007@iith.ac.in",
        "passwd": "I,;]O[l",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ekeosg",
        "roll_no": "CO24BTECH11008",
        "email": "co24btech11008@iith.ac.in",
        "passwd": "uK3(%{/",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Uqfgyu",
        "roll_no": "CO24BTECH11009",
        "email": "co24btech11009@iith.ac.in",
        "passwd": "m>&=v7<",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Modkrd",
        "roll_no": "CO24BTECH11010",
        "email": "co24btech11010@iith.ac.in",
        "passwd": "uc[H<^J",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pfvbzl",
        "roll_no": "CO24BTECH11011",
        "email": "co24btech11011@iith.ac.in",
        "passwd": "GU~zX(g",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gmueuy",
        "roll_no": "CO24BTECH11012",
        "email": "co24btech11012@iith.ac.in",
        "passwd": ">($N<(U",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wxmpsf",
        "roll_no": "CO24BTECH11013",
        "email": "co24btech11013@iith.ac.in",
        "passwd": "gHpG%!8",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Eazouw",
        "roll_no": "CO24BTECH11014",
        "email": "co24btech11014@iith.ac.in",
        "passwd": "Nz)P)mh",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Syvukx",
        "roll_no": "CO24BTECH11015",
        "email": "co24btech11015@iith.ac.in",
        "passwd": "-m;oQ2d",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Atcpgn",
        "roll_no": "CO24BTECH11016",
        "email": "co24btech11016@iith.ac.in",
        "passwd": ")jt8{CN",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nhoyai",
        "roll_no": "CO24BTECH11017",
        "email": "co24btech11017@iith.ac.in",
        "passwd": "l!BctLh",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mkxvzc",
        "roll_no": "CO24BTECH11018",
        "email": "co24btech11018@iith.ac.in",
        "passwd": "C:;\"to?",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Zadrlc",
        "roll_no": "CO24BTECH11019",
        "email": "co24btech11019@iith.ac.in",
        "passwd": "{MgYG25",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Xxyacl",
        "roll_no": "CO24BTECH11020",
        "email": "co24btech11020@iith.ac.in",
        "passwd": "c$xQtr_",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Agrqjx",
        "roll_no": "CO24BTECH11021",
        "email": "co24btech11021@iith.ac.in",
        "passwd": "XY/T|P8",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Fmgsvb",
        "roll_no": "CO24BTECH11022",
        "email": "co24btech11022@iith.ac.in",
        "passwd": "-LbE}ic",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wwidcb",
        "roll_no": "CO24BTECH11023",
        "email": "co24btech11023@iith.ac.in",
        "passwd": "-3Q5wt<",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vitpdz",
        "roll_no": "CO24BTECH11024",
        "email": "co24btech11024@iith.ac.in",
        "passwd": "UyTJ\\^>",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mlfzjm",
        "roll_no": "CO24BTECH11025",
        "email": "co24btech11025@iith.ac.in",
        "passwd": "r%\\RFRG",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tkyrfd",
        "roll_no": "CO24BTECH11026",
        "email": "co24btech11026@iith.ac.in",
        "passwd": "}VVpuJ4",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Aguagf",
        "roll_no": "CO24BTECH11027",
        "email": "co24btech11027@iith.ac.in",
        "passwd": "247if\\2",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qkgtpv",
        "roll_no": "CO24BTECH11028",
        "email": "co24btech11028@iith.ac.in",
        "passwd": "f[bpxY4",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Hioelr",
        "roll_no": "CO24BTECH11029",
        "email": "co24btech11029@iith.ac.in",
        "passwd": "D{-KG(V",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pyzbcr",
        "roll_no": "CO24BTECH11030",
        "email": "co24btech11030@iith.ac.in",
        "passwd": "hxgm&>p",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Zxpknc",
        "roll_no": "CO24BTECH11031",
        "email": "co24btech11031@iith.ac.in",
        "passwd": "'\"=:~`0",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sqzuei",
        "roll_no": "CO24BTECH11032",
        "email": "co24btech11032@iith.ac.in",
        "passwd": "v3d(%6k",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dbkxna",
        "roll_no": "CO24BTECH11033",
        "email": "co24btech11033@iith.ac.in",
        "passwd": ")Si#VI;",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wpsppz",
        "roll_no": "CO24BTECH11034",
        "email": "co24btech11034@iith.ac.in",
        "passwd": "^&u?gQf",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ompuso",
        "roll_no": "CO24BTECH11035",
        "email": "co24btech11035@iith.ac.in",
        "passwd": "&:%oD3:",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mklhip",
        "roll_no": "CO24BTECH11036",
        "email": "co24btech11036@iith.ac.in",
        "passwd": "]^zPYBu",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dhrfbm",
        "roll_no": "CO24BTECH11037",
        "email": "co24btech11037@iith.ac.in",
        "passwd": "QJtoa\"+",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qwqrmm",
        "roll_no": "CO24BTECH11038",
        "email": "co24btech11038@iith.ac.in",
        "passwd": "twn|FmB",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Anudkj",
        "roll_no": "CO24BTECH11039",
        "email": "co24btech11039@iith.ac.in",
        "passwd": "VEK'x`H",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nydfub",
        "roll_no": "CO24BTECH11040",
        "email": "co24btech11040@iith.ac.in",
        "passwd": "|!j+z:q",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vprzjs",
        "roll_no": "CO24BTECH11041",
        "email": "co24btech11041@iith.ac.in",
        "passwd": "_iUoka@",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Snpazo",
        "roll_no": "CO24BTECH11042",
        "email": "co24btech11042@iith.ac.in",
        "passwd": "wj=Q.7c",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qeknsv",
        "roll_no": "CO24BTECH11043",
        "email": "co24btech11043@iith.ac.in",
        "passwd": "Ud'Pm'5",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mansjz",
        "roll_no": "CO24BTECH11044",
        "email": "co24btech11044@iith.ac.in",
        "passwd": "L27j!Xk",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Yisfhx",
        "roll_no": "CO24BTECH11045",
        "email": "co24btech11045@iith.ac.in",
        "passwd": "5$$%l9&",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sucalg",
        "roll_no": "CO24BTECH11046",
        "email": "co24btech11046@iith.ac.in",
        "passwd": "c-]NQ_>",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Oficmc",
        "roll_no": "CO24BTECH11047",
        "email": "co24btech11047@iith.ac.in",
        "passwd": "*b\"-_pw",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jvpywj",
        "roll_no": "CO24BTECH11048",
        "email": "co24btech11048@iith.ac.in",
        "passwd": "cPf[-{g",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Csdpte",
        "roll_no": "CO24BTECH11049",
        "email": "co24btech11049@iith.ac.in",
        "passwd": "jN:}?.X",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Lhthji",
        "roll_no": "CO24BTECH11050",
        "email": "co24btech11050@iith.ac.in",
        "passwd": "?A4w93@",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wzenly",
        "roll_no": "CO24BTECH11051",
        "email": "co24btech11051@iith.ac.in",
        "passwd": "?pdr>rg",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xzemjf",
        "roll_no": "CO24BTECH11052",
        "email": "co24btech11052@iith.ac.in",
        "passwd": "q,A/%eG",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Msvyro",
        "roll_no": "CO24BTECH11053",
        "email": "co24btech11053@iith.ac.in",
        "passwd": "&|pMCB2",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vvdwgp",
        "roll_no": "CO24BTECH11054",
        "email": "co24btech11054@iith.ac.in",
        "passwd": "]{mSm]A",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Sattsy",
        "roll_no": "CO24BTECH11055",
        "email": "co24btech11055@iith.ac.in",
        "passwd": ";,F@sD~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Hljyjw",
        "roll_no": "CO24BTECH11056",
        "email": "co24btech11056@iith.ac.in",
        "passwd": "()d-K&T",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wcxbfr",
        "roll_no": "CO24BTECH11057",
        "email": "co24btech11057@iith.ac.in",
        "passwd": "O+q/&e5",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pnewnq",
        "roll_no": "CO24BTECH11058",
        "email": "co24btech11058@iith.ac.in",
        "passwd": "xEfh7ys",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Treuld",
        "roll_no": "CO24BTECH11059",
        "email": "co24btech11059@iith.ac.in",
        "passwd": "s<=bV1A",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Omaurg",
        "roll_no": "CO24BTECH11060",
        "email": "co24btech11060@iith.ac.in",
        "passwd": "*l,~ByW",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Jaixzu",
        "roll_no": "CO24BTECH11061",
        "email": "co24btech11061@iith.ac.in",
        "passwd": "9`sPmqv",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pptkyv",
        "roll_no": "CO24BTECH11062",
        "email": "co24btech11062@iith.ac.in",
        "passwd": "F.-aJFD",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Kdcops",
        "roll_no": "CO24BTECH11063",
        "email": "co24btech11063@iith.ac.in",
        "passwd": "Ya@[Q.=",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Olmbqk",
        "roll_no": "CO24BTECH11064",
        "email": "co24btech11064@iith.ac.in",
        "passwd": "!gf\\:2{",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ricuof",
        "roll_no": "ME24BTECH11001",
        "email": "me24btech11001@iith.ac.in",
        "passwd": "gWm2_S2",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xfxslu",
        "roll_no": "ME24BTECH11002",
        "email": "me24btech11002@iith.ac.in",
        "passwd": "k=ej`da",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mhtlhg",
        "roll_no": "ME24BTECH11003",
        "email": "me24btech11003@iith.ac.in",
        "passwd": "Ui224:5",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zalrlf",
        "roll_no": "ME24BTECH11004",
        "email": "me24btech11004@iith.ac.in",
        "passwd": "v,=/K{2",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sdlpmk",
        "roll_no": "ME24BTECH11005",
        "email": "me24btech11005@iith.ac.in",
        "passwd": "htTo<iA",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vufelh",
        "roll_no": "ME24BTECH11006",
        "email": "me24btech11006@iith.ac.in",
        "passwd": "Fq35#*a",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cjzpqt",
        "roll_no": "ME24BTECH11007",
        "email": "me24btech11007@iith.ac.in",
        "passwd": "Kw+cWkr",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mahmrr",
        "roll_no": "ME24BTECH11008",
        "email": "me24btech11008@iith.ac.in",
        "passwd": "X\"8X@~D",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ikoftf",
        "roll_no": "ME24BTECH11009",
        "email": "me24btech11009@iith.ac.in",
        "passwd": "eYb2Ek~",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Cvzlju",
        "roll_no": "ME24BTECH11010",
        "email": "me24btech11010@iith.ac.in",
        "passwd": "e*7Uv4,",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bhonql",
        "roll_no": "ME24BTECH11011",
        "email": "me24btech11011@iith.ac.in",
        "passwd": "V~w{paG",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Helbtf",
        "roll_no": "ME24BTECH11012",
        "email": "me24btech11012@iith.ac.in",
        "passwd": "v65{{cB",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Birfdd",
        "roll_no": "ME24BTECH11013",
        "email": "me24btech11013@iith.ac.in",
        "passwd": "qLyS1@-",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ffojrc",
        "roll_no": "ME24BTECH11014",
        "email": "me24btech11014@iith.ac.in",
        "passwd": "DBn`2p/",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Xxphtr",
        "roll_no": "ME24BTECH11015",
        "email": "me24btech11015@iith.ac.in",
        "passwd": "E\"0L)P=",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Iolzjo",
        "roll_no": "ME24BTECH11016",
        "email": "me24btech11016@iith.ac.in",
        "passwd": "fz.ngU[",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Aftoty",
        "roll_no": "ME24BTECH11017",
        "email": "me24btech11017@iith.ac.in",
        "passwd": ")yU;po;",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ukjykj",
        "roll_no": "ME24BTECH11018",
        "email": "me24btech11018@iith.ac.in",
        "passwd": ")2=h7Pd",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Bgkwcn",
        "roll_no": "ME24BTECH11019",
        "email": "me24btech11019@iith.ac.in",
        "passwd": "hiL)Ulf",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ewcyvz",
        "roll_no": "ME24BTECH11020",
        "email": "me24btech11020@iith.ac.in",
        "passwd": "e}n!:nZ",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Snerri",
        "roll_no": "ME24BTECH11021",
        "email": "me24btech11021@iith.ac.in",
        "passwd": "wv]9$V8",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zzkrnw",
        "roll_no": "ME24BTECH11022",
        "email": "me24btech11022@iith.ac.in",
        "passwd": "^_@L-t8",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qfvjkb",
        "roll_no": "ME24BTECH11023",
        "email": "me24btech11023@iith.ac.in",
        "passwd": "8u{?*2j",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tycphj",
        "roll_no": "ME24BTECH11024",
        "email": "me24btech11024@iith.ac.in",
        "passwd": "vSrZH|d",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sxqcah",
        "roll_no": "ME24BTECH11025",
        "email": "me24btech11025@iith.ac.in",
        "passwd": "Lc=\\(e$",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ziztef",
        "roll_no": "ME24BTECH11026",
        "email": "me24btech11026@iith.ac.in",
        "passwd": "H>!p+4T",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Borqki",
        "roll_no": "ME24BTECH11027",
        "email": "me24btech11027@iith.ac.in",
        "passwd": "jGF?Pfg",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mncpqo",
        "roll_no": "ME24BTECH11028",
        "email": "me24btech11028@iith.ac.in",
        "passwd": "U*AAbCm",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qtjayo",
        "roll_no": "ME24BTECH11029",
        "email": "me24btech11029@iith.ac.in",
        "passwd": "IW,Dv|l",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Eallek",
        "roll_no": "ME24BTECH11030",
        "email": "me24btech11030@iith.ac.in",
        "passwd": "y;ed$jP",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Crygdd",
        "roll_no": "ME24BTECH11031",
        "email": "me24btech11031@iith.ac.in",
        "passwd": "2UW8Jm_",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rxfwai",
        "roll_no": "ME24BTECH11032",
        "email": "me24btech11032@iith.ac.in",
        "passwd": "+`-a+pg",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bcqaek",
        "roll_no": "ME24BTECH11033",
        "email": "me24btech11033@iith.ac.in",
        "passwd": "yP>_Eg^",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jxwxka",
        "roll_no": "ME24BTECH11034",
        "email": "me24btech11034@iith.ac.in",
        "passwd": ".sKA5Rh",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Yjlyrx",
        "roll_no": "ME24BTECH11035",
        "email": "me24btech11035@iith.ac.in",
        "passwd": "4V/.yU[",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sjojty",
        "roll_no": "ME24BTECH11036",
        "email": "me24btech11036@iith.ac.in",
        "passwd": "_gic75@",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Tkpmhk",
        "roll_no": "ME24BTECH11037",
        "email": "me24btech11037@iith.ac.in",
        "passwd": "0o/Wc*V",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wxayhl",
        "roll_no": "ME24BTECH11038",
        "email": "me24btech11038@iith.ac.in",
        "passwd": "tnAVw0.",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Cyaamg",
        "roll_no": "ME24BTECH11039",
        "email": "me24btech11039@iith.ac.in",
        "passwd": "%lWdI7I",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gtgctn",
        "roll_no": "ME24BTECH11040",
        "email": "me24btech11040@iith.ac.in",
        "passwd": "2:Ama2x",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Angwlj",
        "roll_no": "ME24BTECH11041",
        "email": "me24btech11041@iith.ac.in",
        "passwd": "SM8JM:\\",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ncpems",
        "roll_no": "ME24BTECH11042",
        "email": "me24btech11042@iith.ac.in",
        "passwd": "=tirJb}",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bewrrx",
        "roll_no": "ME24BTECH11043",
        "email": "me24btech11043@iith.ac.in",
        "passwd": "%5pKW:q",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Zfoves",
        "roll_no": "ME24BTECH11044",
        "email": "me24btech11044@iith.ac.in",
        "passwd": "gjyazJk",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nagqvs",
        "roll_no": "ME24BTECH11045",
        "email": "me24btech11045@iith.ac.in",
        "passwd": "9gYvV<O",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tyrvkl",
        "roll_no": "ME24BTECH11046",
        "email": "me24btech11046@iith.ac.in",
        "passwd": "P=b2jgm",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ptsucu",
        "roll_no": "ME24BTECH11047",
        "email": "me24btech11047@iith.ac.in",
        "passwd": "rLp\\frx",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gxfted",
        "roll_no": "ME24BTECH11048",
        "email": "me24btech11048@iith.ac.in",
        "passwd": "sff?tLT",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Kiqfhw",
        "roll_no": "ME24BTECH11049",
        "email": "me24btech11049@iith.ac.in",
        "passwd": "V1r+BU&",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Dmcaup",
        "roll_no": "ME24BTECH11050",
        "email": "me24btech11050@iith.ac.in",
        "passwd": "CVab}B0",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ylepur",
        "roll_no": "ME24BTECH11051",
        "email": "me24btech11051@iith.ac.in",
        "passwd": "mpHn3iH",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Fnrloe",
        "roll_no": "ME24BTECH11052",
        "email": "me24btech11052@iith.ac.in",
        "passwd": "1>0g@*.",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qedqwh",
        "roll_no": "ME24BTECH11053",
        "email": "me24btech11053@iith.ac.in",
        "passwd": "qC@j8D5",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Jxgpju",
        "roll_no": "ME24BTECH11054",
        "email": "me24btech11054@iith.ac.in",
        "passwd": "8)W(STC",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mxyoyd",
        "roll_no": "ME24BTECH11055",
        "email": "me24btech11055@iith.ac.in",
        "passwd": "b3N?bVl",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Kempaz",
        "roll_no": "ME24BTECH11056",
        "email": "me24btech11056@iith.ac.in",
        "passwd": "\"G>V\"El",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ywzprf",
        "roll_no": "ME24BTECH11057",
        "email": "me24btech11057@iith.ac.in",
        "passwd": ",{GGhFe",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ktbjvr",
        "roll_no": "ME24BTECH11058",
        "email": "me24btech11058@iith.ac.in",
        "passwd": "tJP=HIE",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wxmvmn",
        "roll_no": "ME24BTECH11059",
        "email": "me24btech11059@iith.ac.in",
        "passwd": "6h8fU>E",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Arhllg",
        "roll_no": "ME24BTECH11060",
        "email": "me24btech11060@iith.ac.in",
        "passwd": "L9Q6H.*",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Yohinu",
        "roll_no": "ME24BTECH11061",
        "email": "me24btech11061@iith.ac.in",
        "passwd": "hl{cDwC",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qgamel",
        "roll_no": "ME24BTECH11062",
        "email": "me24btech11062@iith.ac.in",
        "passwd": "@#8y3+U",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mmefwm",
        "roll_no": "ME24BTECH11063",
        "email": "me24btech11063@iith.ac.in",
        "passwd": "klY]q|[",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Betjvx",
        "roll_no": "ME24BTECH11064",
        "email": "me24btech11064@iith.ac.in",
        "passwd": "#Zd1}S{",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Rdbjof",
        "roll_no": "EE24BTECH11001",
        "email": "ee24btech11001@iith.ac.in",
        "passwd": "S@wOu,p",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Kciybb",
        "roll_no": "EE24BTECH11002",
        "email": "ee24btech11002@iith.ac.in",
        "passwd": "H4}?I{2",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Lnpqle",
        "roll_no": "EE24BTECH11003",
        "email": "ee24btech11003@iith.ac.in",
        "passwd": "^[+dG.2",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wxstfu",
        "roll_no": "EE24BTECH11004",
        "email": "ee24btech11004@iith.ac.in",
        "passwd": "fzsyv*l",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tdaknd",
        "roll_no": "EE24BTECH11005",
        "email": "ee24btech11005@iith.ac.in",
        "passwd": ":=9%H[U",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qszlil",
        "roll_no": "EE24BTECH11006",
        "email": "ee24btech11006@iith.ac.in",
        "passwd": "|\"Hb._X",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Fpnygo",
        "roll_no": "EE24BTECH11007",
        "email": "ee24btech11007@iith.ac.in",
        "passwd": "pUg\\X|J",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Pektsq",
        "roll_no": "EE24BTECH11008",
        "email": "ee24btech11008@iith.ac.in",
        "passwd": "AIFKb&}",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gqissj",
        "roll_no": "EE24BTECH11009",
        "email": "ee24btech11009@iith.ac.in",
        "passwd": "Dq/gkrM",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bxlwjt",
        "roll_no": "EE24BTECH11010",
        "email": "ee24btech11010@iith.ac.in",
        "passwd": "q_i~lsE",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Uogvak",
        "roll_no": "EE24BTECH11011",
        "email": "ee24btech11011@iith.ac.in",
        "passwd": "kFqktyd",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Fpriap",
        "roll_no": "EE24BTECH11012",
        "email": "ee24btech11012@iith.ac.in",
        "passwd": ".E{[/no",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vfvotg",
        "roll_no": "EE24BTECH11013",
        "email": "ee24btech11013@iith.ac.in",
        "passwd": "q*\\!9_?",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gibppc",
        "roll_no": "EE24BTECH11014",
        "email": "ee24btech11014@iith.ac.in",
        "passwd": "g^;W,?P",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ltvsba",
        "roll_no": "EE24BTECH11015",
        "email": "ee24btech11015@iith.ac.in",
        "passwd": "Py#`sD#",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zibxdw",
        "roll_no": "EE24BTECH11016",
        "email": "ee24btech11016@iith.ac.in",
        "passwd": "g1uGBl|",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bvwwgi",
        "roll_no": "EE24BTECH11017",
        "email": "ee24btech11017@iith.ac.in",
        "passwd": "&S*0c=u",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Kyigqo",
        "roll_no": "EE24BTECH11018",
        "email": "ee24btech11018@iith.ac.in",
        "passwd": "F*kS9U9",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nmjxoq",
        "roll_no": "EE24BTECH11019",
        "email": "ee24btech11019@iith.ac.in",
        "passwd": ")6szT(@",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wmxtve",
        "roll_no": "EE24BTECH11020",
        "email": "ee24btech11020@iith.ac.in",
        "passwd": "2h8~Hc~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Yvgzoo",
        "roll_no": "EE24BTECH11021",
        "email": "ee24btech11021@iith.ac.in",
        "passwd": "wxa4hUx",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Snyffn",
        "roll_no": "EE24BTECH11022",
        "email": "ee24btech11022@iith.ac.in",
        "passwd": "+$z`]Ya",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mnubgd",
        "roll_no": "EE24BTECH11023",
        "email": "ee24btech11023@iith.ac.in",
        "passwd": "h+&2XMm",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Erfgbz",
        "roll_no": "EE24BTECH11024",
        "email": "ee24btech11024@iith.ac.in",
        "passwd": "k8Hyv>g",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Glhtlp",
        "roll_no": "EE24BTECH11025",
        "email": "ee24btech11025@iith.ac.in",
        "passwd": "Z}WVeh-",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jjtfoc",
        "roll_no": "EE24BTECH11026",
        "email": "ee24btech11026@iith.ac.in",
        "passwd": "SC{8pCZ",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vpvncs",
        "roll_no": "EE24BTECH11027",
        "email": "ee24btech11027@iith.ac.in",
        "passwd": "|j9``ik",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Pummjo",
        "roll_no": "EE24BTECH11028",
        "email": "ee24btech11028@iith.ac.in",
        "passwd": "q/c+M?#",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bhtegy",
        "roll_no": "EE24BTECH11029",
        "email": "ee24btech11029@iith.ac.in",
        "passwd": "aADpQ%[",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gmklvw",
        "roll_no": "EE24BTECH11030",
        "email": "ee24btech11030@iith.ac.in",
        "passwd": "ZHZz8\\+",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pfjjqr",
        "roll_no": "EE24BTECH11031",
        "email": "ee24btech11031@iith.ac.in",
        "passwd": "Tu2f9Sf",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tulddb",
        "roll_no": "EE24BTECH11032",
        "email": "ee24btech11032@iith.ac.in",
        "passwd": "l]T7+a/",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Swhejq",
        "roll_no": "EE24BTECH11033",
        "email": "ee24btech11033@iith.ac.in",
        "passwd": "7xf(pk4",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rtefcz",
        "roll_no": "EE24BTECH11034",
        "email": "ee24btech11034@iith.ac.in",
        "passwd": "9l\\iYk{",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cdgroy",
        "roll_no": "EE24BTECH11035",
        "email": "ee24btech11035@iith.ac.in",
        "passwd": ".'VS^)]",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wiapfx",
        "roll_no": "EE24BTECH11036",
        "email": "ee24btech11036@iith.ac.in",
        "passwd": "Wp79gj#",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Mjqffb",
        "roll_no": "EE24BTECH11037",
        "email": "ee24btech11037@iith.ac.in",
        "passwd": "\\;c!c^}",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rjthlr",
        "roll_no": "EE24BTECH11038",
        "email": "ee24btech11038@iith.ac.in",
        "passwd": "ifb'l58",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Isvcef",
        "roll_no": "EE24BTECH11039",
        "email": "ee24btech11039@iith.ac.in",
        "passwd": "|\"-nUo-",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ghtrps",
        "roll_no": "EE24BTECH11040",
        "email": "ee24btech11040@iith.ac.in",
        "passwd": "%+2ko9\"",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ezdqhg",
        "roll_no": "EE24BTECH11041",
        "email": "ee24btech11041@iith.ac.in",
        "passwd": "rDX366L",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vcucid",
        "roll_no": "EE24BTECH11042",
        "email": "ee24btech11042@iith.ac.in",
        "passwd": "Ev2h)QN",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wlfwzq",
        "roll_no": "EE24BTECH11043",
        "email": "ee24btech11043@iith.ac.in",
        "passwd": "uE3L4y$",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Nbbilc",
        "roll_no": "EE24BTECH11044",
        "email": "ee24btech11044@iith.ac.in",
        "passwd": "Kza+RG>",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Xryymo",
        "roll_no": "EE24BTECH11045",
        "email": "ee24btech11045@iith.ac.in",
        "passwd": ")n^x%>d",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Hywmyh",
        "roll_no": "EE24BTECH11046",
        "email": "ee24btech11046@iith.ac.in",
        "passwd": "L!rjTg(",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Hrfjpz",
        "roll_no": "EE24BTECH11047",
        "email": "ee24btech11047@iith.ac.in",
        "passwd": "x!3hyD4",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vhidbw",
        "roll_no": "EE24BTECH11048",
        "email": "ee24btech11048@iith.ac.in",
        "passwd": "KKRL`,+",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Csakny",
        "roll_no": "EE24BTECH11049",
        "email": "ee24btech11049@iith.ac.in",
        "passwd": "(*JM7yO",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Oqjfyy",
        "roll_no": "EE24BTECH11050",
        "email": "ee24btech11050@iith.ac.in",
        "passwd": "rTWCF/y",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jrwiiz",
        "roll_no": "EE24BTECH11051",
        "email": "ee24btech11051@iith.ac.in",
        "passwd": "<5Wx;#}",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ozigry",
        "roll_no": "EE24BTECH11052",
        "email": "ee24btech11052@iith.ac.in",
        "passwd": "g0$P0*^",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dtctvz",
        "roll_no": "EE24BTECH11053",
        "email": "ee24btech11053@iith.ac.in",
        "passwd": "c}4JMB7",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qtptee",
        "roll_no": "EE24BTECH11054",
        "email": "ee24btech11054@iith.ac.in",
        "passwd": "+vOl'9^",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vbtheg",
        "roll_no": "EE24BTECH11055",
        "email": "ee24btech11055@iith.ac.in",
        "passwd": "xoTd,g8",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dbbwgu",
        "roll_no": "EE24BTECH11056",
        "email": "ee24btech11056@iith.ac.in",
        "passwd": "!]B[2bK",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Imzein",
        "roll_no": "EE24BTECH11057",
        "email": "ee24btech11057@iith.ac.in",
        "passwd": "H\\cajkV",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dgwjqv",
        "roll_no": "EE24BTECH11058",
        "email": "ee24btech11058@iith.ac.in",
        "passwd": "UU&#ijO",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ekhden",
        "roll_no": "EE24BTECH11059",
        "email": "ee24btech11059@iith.ac.in",
        "passwd": "{i4{9@\\",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Aqropo",
        "roll_no": "EE24BTECH11060",
        "email": "ee24btech11060@iith.ac.in",
        "passwd": "o.AYxXV",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wzgule",
        "roll_no": "EE24BTECH11061",
        "email": "ee24btech11061@iith.ac.in",
        "passwd": "1%5Jm&u",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qujycu",
        "roll_no": "EE24BTECH11062",
        "email": "ee24btech11062@iith.ac.in",
        "passwd": "-yz>}Q;",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pnanps",
        "roll_no": "EE24BTECH11063",
        "email": "ee24btech11063@iith.ac.in",
        "passwd": "/BTJ6.Z",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Hvfuzz",
        "roll_no": "EE24BTECH11064",
        "email": "ee24btech11064@iith.ac.in",
        "passwd": "%\\#?l~\"",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Tcqdqz",
        "roll_no": "IC24BTECH11001",
        "email": "ic24btech11001@iith.ac.in",
        "passwd": "%?vsmy1",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Msfmdt",
        "roll_no": "IC24BTECH11002",
        "email": "ic24btech11002@iith.ac.in",
        "passwd": "s7!WXO4",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Geutbq",
        "roll_no": "IC24BTECH11003",
        "email": "ic24btech11003@iith.ac.in",
        "passwd": "_IwJa\\G",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xfvwgf",
        "roll_no": "IC24BTECH11004",
        "email": "ic24btech11004@iith.ac.in",
        "passwd": ")g8n0nm",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Hzsato",
        "roll_no": "IC24BTECH11005",
        "email": "ic24btech11005@iith.ac.in",
        "passwd": "kVk7ucQ",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Lgxiie",
        "roll_no": "IC24BTECH11006",
        "email": "ic24btech11006@iith.ac.in",
        "passwd": "x5g&i<F",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ajqevu",
        "roll_no": "IC24BTECH11007",
        "email": "ic24btech11007@iith.ac.in",
        "passwd": "1_G#/y6",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zanmns",
        "roll_no": "IC24BTECH11008",
        "email": "ic24btech11008@iith.ac.in",
        "passwd": "\"WwqZ7o",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Niznnx",
        "roll_no": "IC24BTECH11009",
        "email": "ic24btech11009@iith.ac.in",
        "passwd": "#Ug-=+?",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tuxlhl",
        "roll_no": "IC24BTECH11010",
        "email": "ic24btech11010@iith.ac.in",
        "passwd": "g%d\"|YI",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zroiff",
        "roll_no": "IC24BTECH11011",
        "email": "ic24btech11011@iith.ac.in",
        "passwd": "A[L3jL[",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rbbxth",
        "roll_no": "IC24BTECH11012",
        "email": "ic24btech11012@iith.ac.in",
        "passwd": "W8_e}0v",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Iohipx",
        "roll_no": "IC24BTECH11013",
        "email": "ic24btech11013@iith.ac.in",
        "passwd": "`V5\"NI6",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Plmvxi",
        "roll_no": "IC24BTECH11014",
        "email": "ic24btech11014@iith.ac.in",
        "passwd": "ivo{tc~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ebqxfh",
        "roll_no": "IC24BTECH11015",
        "email": "ic24btech11015@iith.ac.in",
        "passwd": "%OH}l'{",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dzqdts",
        "roll_no": "IC24BTECH11016",
        "email": "ic24btech11016@iith.ac.in",
        "passwd": "AslNn!g",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Htcqjw",
        "roll_no": "IC24BTECH11017",
        "email": "ic24btech11017@iith.ac.in",
        "passwd": "n<c5G>h",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Obmwps",
        "roll_no": "IC24BTECH11018",
        "email": "ic24btech11018@iith.ac.in",
        "passwd": "Sx}.TRf",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Epvtfw",
        "roll_no": "IC24BTECH11019",
        "email": "ic24btech11019@iith.ac.in",
        "passwd": "/+dxWL%",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Bsraos",
        "roll_no": "IC24BTECH11020",
        "email": "ic24btech11020@iith.ac.in",
        "passwd": "&97KS_~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bnacms",
        "roll_no": "IC24BTECH11021",
        "email": "ic24btech11021@iith.ac.in",
        "passwd": "V+gS2&!",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Fuzulb",
        "roll_no": "IC24BTECH11022",
        "email": "ic24btech11022@iith.ac.in",
        "passwd": "ZYDU&J`",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Zeraeu",
        "roll_no": "IC24BTECH11023",
        "email": "ic24btech11023@iith.ac.in",
        "passwd": "-vCl-R^",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Apbsco",
        "roll_no": "IC24BTECH11024",
        "email": "ic24btech11024@iith.ac.in",
        "passwd": "TeS8/|@",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wksoqn",
        "roll_no": "IC24BTECH11025",
        "email": "ic24btech11025@iith.ac.in",
        "passwd": "xw>mTt(",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wkrscs",
        "roll_no": "IC24BTECH11026",
        "email": "ic24btech11026@iith.ac.in",
        "passwd": "h)sV%cr",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Cqbcqb",
        "roll_no": "IC24BTECH11027",
        "email": "ic24btech11027@iith.ac.in",
        "passwd": "g)NwhW/",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Knkfxg",
        "roll_no": "IC24BTECH11028",
        "email": "ic24btech11028@iith.ac.in",
        "passwd": "#C=9zR0",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Bvbcqm",
        "roll_no": "IC24BTECH11029",
        "email": "ic24btech11029@iith.ac.in",
        "passwd": "@7N`Vh`",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vjliok",
        "roll_no": "IC24BTECH11030",
        "email": "ic24btech11030@iith.ac.in",
        "passwd": "`Ce9x[M",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ogoqhf",
        "roll_no": "IC24BTECH11031",
        "email": "ic24btech11031@iith.ac.in",
        "passwd": "m(f7c<Q",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cblkie",
        "roll_no": "IC24BTECH11032",
        "email": "ic24btech11032@iith.ac.in",
        "passwd": "[h1*Df~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xlxaea",
        "roll_no": "IC24BTECH11033",
        "email": "ic24btech11033@iith.ac.in",
        "passwd": "w:r>_|+",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Xoroen",
        "roll_no": "IC24BTECH11034",
        "email": "ic24btech11034@iith.ac.in",
        "passwd": "]n_\\Apn",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Urdzeg",
        "roll_no": "IC24BTECH11035",
        "email": "ic24btech11035@iith.ac.in",
        "passwd": "d5Hhtw;",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nuncky",
        "roll_no": "IC24BTECH11036",
        "email": "ic24btech11036@iith.ac.in",
        "passwd": "pE8pVpT",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zcplad",
        "roll_no": "IC24BTECH11037",
        "email": "ic24btech11037@iith.ac.in",
        "passwd": "aThaB_4",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Gbgryt",
        "roll_no": "IC24BTECH11038",
        "email": "ic24btech11038@iith.ac.in",
        "passwd": "HjHJ`D-",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Uqmrrz",
        "roll_no": "IC24BTECH11039",
        "email": "ic24btech11039@iith.ac.in",
        "passwd": "jd$ol,h",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Pdnhut",
        "roll_no": "IC24BTECH11040",
        "email": "ic24btech11040@iith.ac.in",
        "passwd": "h={}5L2",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Kcchih",
        "roll_no": "IC24BTECH11041",
        "email": "ic24btech11041@iith.ac.in",
        "passwd": "U%F{o6D",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Hrwskf",
        "roll_no": "IC24BTECH11042",
        "email": "ic24btech11042@iith.ac.in",
        "passwd": ".Chu&NJ",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Spxeyp",
        "roll_no": "IC24BTECH11043",
        "email": "ic24btech11043@iith.ac.in",
        "passwd": "TiTo[\\{",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nlaxti",
        "roll_no": "IC24BTECH11044",
        "email": "ic24btech11044@iith.ac.in",
        "passwd": "[P0*phj",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Wvkuhg",
        "roll_no": "IC24BTECH11045",
        "email": "ic24btech11045@iith.ac.in",
        "passwd": "a)fg}2o",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bynami",
        "roll_no": "IC24BTECH11046",
        "email": "ic24btech11046@iith.ac.in",
        "passwd": "K{`2pr=",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qhhwrp",
        "roll_no": "IC24BTECH11047",
        "email": "ic24btech11047@iith.ac.in",
        "passwd": "C.u-}=P",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Biageo",
        "roll_no": "IC24BTECH11048",
        "email": "ic24btech11048@iith.ac.in",
        "passwd": "U{=bg[(",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Eshrgv",
        "roll_no": "IC24BTECH11049",
        "email": "ic24btech11049@iith.ac.in",
        "passwd": "gp'hMtx",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Nsnjnv",
        "roll_no": "IC24BTECH11050",
        "email": "ic24btech11050@iith.ac.in",
        "passwd": "R#-Awmc",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Jztbfw",
        "roll_no": "IC24BTECH11051",
        "email": "ic24btech11051@iith.ac.in",
        "passwd": "._<f*R0",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Opozbu",
        "roll_no": "IC24BTECH11052",
        "email": "ic24btech11052@iith.ac.in",
        "passwd": "~nL}pBp",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Yxazan",
        "roll_no": "IC24BTECH11053",
        "email": "ic24btech11053@iith.ac.in",
        "passwd": "yO+^nM(",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cearvv",
        "roll_no": "IC24BTECH11054",
        "email": "ic24btech11054@iith.ac.in",
        "passwd": "aY,McI+",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Babspw",
        "roll_no": "IC24BTECH11055",
        "email": "ic24btech11055@iith.ac.in",
        "passwd": "WKwxFR9",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Diluag",
        "roll_no": "IC24BTECH11056",
        "email": "ic24btech11056@iith.ac.in",
        "passwd": "2{:^(1o",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Rglydy",
        "roll_no": "IC24BTECH11057",
        "email": "ic24btech11057@iith.ac.in",
        "passwd": ",K(+`yo",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Rcifgt",
        "roll_no": "IC24BTECH11058",
        "email": "ic24btech11058@iith.ac.in",
        "passwd": ";`V1;^y",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wttopp",
        "roll_no": "IC24BTECH11059",
        "email": "ic24btech11059@iith.ac.in",
        "passwd": "|'g-z0m",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Kofnzn",
        "roll_no": "IC24BTECH11060",
        "email": "ic24btech11060@iith.ac.in",
        "passwd": ".o!acf4",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Umvbto",
        "roll_no": "IC24BTECH11061",
        "email": "ic24btech11061@iith.ac.in",
        "passwd": "aH;;8xK",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Rxlbco",
        "roll_no": "IC24BTECH11062",
        "email": "ic24btech11062@iith.ac.in",
        "passwd": "1aYA@b(",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Jnzghg",
        "roll_no": "IC24BTECH11063",
        "email": "ic24btech11063@iith.ac.in",
        "passwd": "mNec.VI",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vjycoz",
        "roll_no": "IC24BTECH11064",
        "email": "ic24btech11064@iith.ac.in",
        "passwd": "qzi%nRt",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zzmpaj",
        "roll_no": "CH24BTECH11001",
        "email": "ch24btech11001@iith.ac.in",
        "passwd": "{N[}Y.)",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Dkqyfc",
        "roll_no": "CH24BTECH11002",
        "email": "ch24btech11002@iith.ac.in",
        "passwd": "Gy=6.e(",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Tsearm",
        "roll_no": "CH24BTECH11003",
        "email": "ch24btech11003@iith.ac.in",
        "passwd": "+I4[s_(",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Kkxocj",
        "roll_no": "CH24BTECH11004",
        "email": "ch24btech11004@iith.ac.in",
        "passwd": "`>WI:9E",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Elldpl",
        "roll_no": "CH24BTECH11005",
        "email": "ch24btech11005@iith.ac.in",
        "passwd": "<DwV=vK",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Pdllzz",
        "roll_no": "CH24BTECH11006",
        "email": "ch24btech11006@iith.ac.in",
        "passwd": "qw'jid,",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Plogwf",
        "roll_no": "CH24BTECH11007",
        "email": "ch24btech11007@iith.ac.in",
        "passwd": "-TWwyfU",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vlmlhs",
        "roll_no": "CH24BTECH11008",
        "email": "ch24btech11008@iith.ac.in",
        "passwd": "F{mN)mw",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qtifbn",
        "roll_no": "CH24BTECH11009",
        "email": "ch24btech11009@iith.ac.in",
        "passwd": "aC{U_<N",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ivpbak",
        "roll_no": "CH24BTECH11010",
        "email": "ch24btech11010@iith.ac.in",
        "passwd": "CQ.\"Bfn",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mmdgic",
        "roll_no": "CH24BTECH11011",
        "email": "ch24btech11011@iith.ac.in",
        "passwd": "$vS6l5x",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Zyrtab",
        "roll_no": "CH24BTECH11012",
        "email": "ch24btech11012@iith.ac.in",
        "passwd": "K&*'vG`",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Fuoauz",
        "roll_no": "CH24BTECH11013",
        "email": "ch24btech11013@iith.ac.in",
        "passwd": "{^2l`eR",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Nbofya",
        "roll_no": "CH24BTECH11014",
        "email": "ch24btech11014@iith.ac.in",
        "passwd": "^gxN#jr",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pydbcd",
        "roll_no": "CH24BTECH11015",
        "email": "ch24btech11015@iith.ac.in",
        "passwd": "?2yI97F",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Uivdof",
        "roll_no": "CH24BTECH11016",
        "email": "ch24btech11016@iith.ac.in",
        "passwd": "iv7cB)S",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Sxhpvn",
        "roll_no": "CH24BTECH11017",
        "email": "ch24btech11017@iith.ac.in",
        "passwd": "hOll~9j",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Vycewm",
        "roll_no": "CH24BTECH11018",
        "email": "ch24btech11018@iith.ac.in",
        "passwd": "hZEjbV-",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Jziwsh",
        "roll_no": "CH24BTECH11019",
        "email": "ch24btech11019@iith.ac.in",
        "passwd": "V#Q&iX}",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Opojgc",
        "roll_no": "CH24BTECH11020",
        "email": "ch24btech11020@iith.ac.in",
        "passwd": "`fg'!TC",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Pelvjn",
        "roll_no": "CH24BTECH11021",
        "email": "ch24btech11021@iith.ac.in",
        "passwd": "&jHBcOS",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Tsiyjj",
        "roll_no": "CH24BTECH11022",
        "email": "ch24btech11022@iith.ac.in",
        "passwd": "l}HEz<`",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ttfpzp",
        "roll_no": "CH24BTECH11023",
        "email": "ch24btech11023@iith.ac.in",
        "passwd": "[W[#|Y}",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Juwnie",
        "roll_no": "CH24BTECH11024",
        "email": "ch24btech11024@iith.ac.in",
        "passwd": "_c[P6a*",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Obpxsw",
        "roll_no": "CH24BTECH11025",
        "email": "ch24btech11025@iith.ac.in",
        "passwd": "kMXVvgJ",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Zbrejw",
        "roll_no": "CH24BTECH11026",
        "email": "ch24btech11026@iith.ac.in",
        "passwd": "Y|G,fJr",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qcjzun",
        "roll_no": "CH24BTECH11027",
        "email": "ch24btech11027@iith.ac.in",
        "passwd": "cfc^u7U",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Hodevi",
        "roll_no": "CH24BTECH11028",
        "email": "ch24btech11028@iith.ac.in",
        "passwd": ".,/T%tW",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Qdvtcd",
        "roll_no": "CH24BTECH11029",
        "email": "ch24btech11029@iith.ac.in",
        "passwd": "%<s[`J+",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Tuaboy",
        "roll_no": "CH24BTECH11030",
        "email": "ch24btech11030@iith.ac.in",
        "passwd": "6yAJ03k",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ipzatl",
        "roll_no": "CH24BTECH11031",
        "email": "ch24btech11031@iith.ac.in",
        "passwd": "JM%hx&>",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Timson",
        "roll_no": "CH24BTECH11032",
        "email": "ch24btech11032@iith.ac.in",
        "passwd": "(P#s%XO",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qlrved",
        "roll_no": "CH24BTECH11033",
        "email": "ch24btech11033@iith.ac.in",
        "passwd": "p->rsM{",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sybevv",
        "roll_no": "CH24BTECH11034",
        "email": "ch24btech11034@iith.ac.in",
        "passwd": ":-dDW|g",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Aemqzz",
        "roll_no": "CH24BTECH11035",
        "email": "ch24btech11035@iith.ac.in",
        "passwd": "sB7:/G0",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sbxddp",
        "roll_no": "CH24BTECH11036",
        "email": "ch24btech11036@iith.ac.in",
        "passwd": ")57Or=M",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ltazvi",
        "roll_no": "CH24BTECH11037",
        "email": "ch24btech11037@iith.ac.in",
        "passwd": "{fOoi*L",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Zwdoho",
        "roll_no": "CH24BTECH11038",
        "email": "ch24btech11038@iith.ac.in",
        "passwd": "v@Y[=(A",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Dkbqyj",
        "roll_no": "CH24BTECH11039",
        "email": "ch24btech11039@iith.ac.in",
        "passwd": "'Q2^Z2k",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Oubjgv",
        "roll_no": "CH24BTECH11040",
        "email": "ch24btech11040@iith.ac.in",
        "passwd": "}(M~\\oX",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sezhwi",
        "roll_no": "CH24BTECH11041",
        "email": "ch24btech11041@iith.ac.in",
        "passwd": "C3L4<d{",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ilgzrc",
        "roll_no": "CH24BTECH11042",
        "email": "ch24btech11042@iith.ac.in",
        "passwd": "gqy9(7,",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Nkjrin",
        "roll_no": "CH24BTECH11043",
        "email": "ch24btech11043@iith.ac.in",
        "passwd": "Jb7ws*~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Cilaoh",
        "roll_no": "CH24BTECH11044",
        "email": "ch24btech11044@iith.ac.in",
        "passwd": "Hs1u(LB",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Cqpsbp",
        "roll_no": "CH24BTECH11045",
        "email": "ch24btech11045@iith.ac.in",
        "passwd": "5OzNCA~",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Xdnfmg",
        "roll_no": "CH24BTECH11046",
        "email": "ch24btech11046@iith.ac.in",
        "passwd": "P9Dob9u",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Tbbkhg",
        "roll_no": "CH24BTECH11047",
        "email": "ch24btech11047@iith.ac.in",
        "passwd": "VV_6/7&",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Jrbmit",
        "roll_no": "CH24BTECH11048",
        "email": "ch24btech11048@iith.ac.in",
        "passwd": "<,hX)nH",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Diwryk",
        "roll_no": "CH24BTECH11049",
        "email": "ch24btech11049@iith.ac.in",
        "passwd": "!E)?EWl",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Ronbnh",
        "roll_no": "CH24BTECH11050",
        "email": "ch24btech11050@iith.ac.in",
        "passwd": "]6yaqn;",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Rhmmbl",
        "roll_no": "CH24BTECH11051",
        "email": "ch24btech11051@iith.ac.in",
        "passwd": "Dm:FZ\"b",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Iqfbrd",
        "roll_no": "CH24BTECH11052",
        "email": "ch24btech11052@iith.ac.in",
        "passwd": "Z;-qCaj",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Qqjeoq",
        "roll_no": "CH24BTECH11053",
        "email": "ch24btech11053@iith.ac.in",
        "passwd": "Zj:9d|(",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Ioznzb",
        "roll_no": "CH24BTECH11054",
        "email": "ch24btech11054@iith.ac.in",
        "passwd": "[l?.-v]",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Wbldip",
        "roll_no": "CH24BTECH11055",
        "email": "ch24btech11055@iith.ac.in",
        "passwd": "Yitqx4\\",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Bzjtva",
        "roll_no": "CH24BTECH11056",
        "email": "ch24btech11056@iith.ac.in",
        "passwd": "V|~Yq6c",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Akvexq",
        "roll_no": "CH24BTECH11057",
        "email": "ch24btech11057@iith.ac.in",
        "passwd": "w~p\"UD\\",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Xqiyqe",
        "roll_no": "CH24BTECH11058",
        "email": "ch24btech11058@iith.ac.in",
        "passwd": "\"w=z)3C",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Mrgqfc",
        "roll_no": "CH24BTECH11059",
        "email": "ch24btech11059@iith.ac.in",
        "passwd": "mqD/C`_",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vdfvzx",
        "roll_no": "CH24BTECH11060",
        "email": "ch24btech11060@iith.ac.in",
        "passwd": "Cjw(Kil",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Sinzhr",
        "roll_no": "CH24BTECH11061",
        "email": "ch24btech11061@iith.ac.in",
        "passwd": "f@(/|(]",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Atbfzf",
        "roll_no": "CH24BTECH11062",
        "email": "ch24btech11062@iith.ac.in",
        "passwd": ">zed?2l",
        "previous_mess": "MESS-B",
        "current_mess": "MESS-B",
        "mess_feedback": []
    },
    {
        "name": "Vzewvv",
        "roll_no": "CH24BTECH11063",
        "email": "ch24btech11063@iith.ac.in",
        "passwd": "DkyRi%!",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-A",
        "mess_feedback": []
    },
    {
        "name": "Lsecqu",
        "roll_no": "CH24BTECH11064",
        "email": "ch24btech11064@iith.ac.in",
        "passwd": "O&zxdUZ",
        "previous_mess": "MESS-A",
        "current_mess": "MESS-B",
        "mess_feedback": []
    }
]


collection_students.insert_many(data_students)
print("Inserted students data into database")