const buildings = [
  "경영관",
  "사회과학관",
  "과학관",
  "다향관",
  "만해관",
  "명진관",
  "문화관",
  "법학관",
  "본관",
  "상록원",
  "신공학관",
  "원흥관",
  "정보문화관",
  "중앙도서관",
  "학림관",
  "학생회관",
  "학술관",
  "혜화관",
];
const convenients = [
  "복사기",
  "유인복사실",
  "열람실",
  "atm",
  "증명서 자동발급기",
  "제세동기",
  "식당",
  "카페",
  "매점",
];
const pinPositionData = [
  ["경영관", 97, 251],
  ["사회과학관", 150, 251],
  ["과학관", 265, 110],
  ["다향관", 384, 198],
  ["만해관", 261, 192],
  ["명진관", 294, 137],
  ["문화관", 133, 302],
  ["법학관", 289, 203],
  ["본관", 378, 142],
  ["상록원", 232, 95],
  ["신공학관", 350, 61],
  ["원흥관", 412, 126],
  ["정보문화관P", 472, 134],
  ["정보문화관Q", 511, 130],
  ["중앙도서관", 336, 116],
  ["학림관", 523, 246],
  ["학생회관", 550, 129],
  ["학술관", 119, 345],
  ["혜화관", 210, 238],
  ["정보문화관", 492, 133],
  ["계산관A", 554, 248],
  ["계산관B", 531, 200],
  ["고시반 기숙사", 295, 342],
  ["기숙사", 371, 84],
  ["금강관", 426, 242],
  ["대운동장", 174, 160],
  ["동국백년비", 225, 191],
  ["만해광장", 484, 187],
  ["만해시비", 408, 182],
  ["박물관", 237, 289],
  ["반야관", 496, 297],
  ["법학생활관", 278, 337],
  ["보현 보살코끼리상", 339, 206],
  ["생활협동조합", 94, 177],
  ["원흥별관", 413, 112],
  ["정각원", 241, 213],
  ["정문", 40, 257],
  ["충무로 영상상센터", 624, 121],
  ["팔정도", 326, 172],
  ["혜화별관", 193, 212],
  ["후문", 610, 292],
];

const buildingInfo = {
  Business01: {
    name: "경영관",
    복사기: true,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: true,
    매점: false,
  },
  Science02: {
    name: "과학관",
    복사기: true,
    유인복사실: true,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: true,
    식당: false,
    카페: true,
    매점: false,
  },
  Dahyang03: {
    name: "다향관",
    복사기: false,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: false,
    매점: true,
  },
  Manhae04: {
    name: "만해관",
    복사기: true,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: false,
    매점: false,
  },
  Myeongjin05: {
    name: "명진관",
    복사기: true,
    유인복사실: true,
    열람실: true,
    atm: true,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: false,
    매점: false,
  },
  Munhwa06: {
    name: "문화관",
    복사기: true,
    유인복사실: false,
    열람실: false,
    atm: true,
    증명서자동발급기: true,
    제세동기: true,
    식당: false,
    카페: false,
    매점: false,
  },
  Law07: {
    name: "법학관",
    복사기: false,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: true,
    식당: false,
    카페: false,
    매점: true,
  },
  Main08: {
    name: "본관",
    복사기: false,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: true,
    식당: false,
    카페: true,
    매점: false,
  },
  SocialScience09: {
    name: "사회과학관",
    복사기: true,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: true,
    제세동기: true,
    식당: false,
    카페: false,
    매점: false,
  },
  Sanglokwon10: {
    name: "상록원",
    복사기: false,
    유인복사실: false,
    열람실: false,
    atm: true,
    증명서자동발급기: false,
    제세동기: false,
    식당: true,
    카페: false,
    매점: true,
  },
  NewEngineering11: {
    name: "신공학관",
    복사기: true,
    유인복사실: false,
    열람실: false,
    atm: true,
    증명서자동발급기: false,
    제세동기: false,
    식당: true,
    카페: true,
    매점: true,
  },
  Wonheung12: {
    name: "원흥관",
    복사기: true,
    유인복사실: false,
    열람실: true,
    atm: true,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: false,
    매점: false,
  },
  InformationEngineering13: {
    name: "정보문화관",
    복사기: true,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: false,
    매점: false,
  },
  Library14: {
    name: "중앙도서관",
    복사기: true,
    유인복사실: true,
    열람실: false,
    atm: false,
    증명서자동발급기: true,
    제세동기: false,
    식당: false,
    카페: false,
    매점: true,
  },
  Haklim15: {
    name: "학림관",
    복사기: true,
    유인복사실: false,
    열람실: true,
    atm: true,
    증명서자동발급기: true,
    제세동기: true,
    식당: false,
    카페: false,
    매점: true,
  },
  Student16: {
    name: "학생회관",
    복사기: true,
    유인복사실: false,
    열람실: true,
    atm: false,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: false,
    매점: false,
  },
  Haksul17: {
    name: "학술관",
    복사기: true,
    유인복사실: false,
    열람실: false,
    atm: false,
    증명서자동발급기: false,
    제세동기: false,
    식당: true,
    카페: true,
    매점: false,
  },
  Hyehwa18: {
    name: "혜화관",
    복사기: true,
    유인복사실: false,
    열람실: true,
    atm: true,
    증명서자동발급기: false,
    제세동기: false,
    식당: false,
    카페: true,
    매점: true,
  },
};

const closeOrder = {
  ListBuisness01: [
    buildingInfo.Business01,
    buildingInfo.Hyehwa18,
    buildingInfo.SocialScience09,
    buildingInfo.Munhwa06,
    buildingInfo.Manhae04,
    buildingInfo.Myeongjin05,
    buildingInfo.Haksul17,
    buildingInfo.Law07,
    buildingInfo.Science02,
    buildingInfo.Dahyang03,
    buildingInfo.Library14,
    buildingInfo.NewEngineering11,
    buildingInfo.Main08,
    buildingInfo.Sanglokwon10,
    buildingInfo.Wonheung12,
    buildingInfo.InformationEngineering13,
    buildingInfo.Student16,
    buildingInfo.Haklim15,
  ],
  ListScience02: [
    buildingInfo.Science02,
    buildingInfo.Myeongjin05,
    buildingInfo.Sanglokwon10,
    buildingInfo.Manhae04,
    buildingInfo.Law07,
    buildingInfo.Library14,
    buildingInfo.NewEngineering11,
    buildingInfo.Main08,
    buildingInfo.Dahyang03,
    buildingInfo.Wonheung12,
    buildingInfo.InformationEngineering13,
    buildingInfo.Hyehwa18,
    buildingInfo.Business01,
    buildingInfo.SocialScience09,
    buildingInfo.Student16,
    buildingInfo.Haklim15,
    buildingInfo.Munhwa06,
    buildingInfo.Haksul17,
  ],
  ListDahyang03: [
    buildingInfo.Dahyang03,
    buildingInfo.Law07,
    buildingInfo.Main08,
    buildingInfo.Manhae04,
    buildingInfo.Myeongjin05,
    buildingInfo.Library14,
    buildingInfo.Wonheung12,
    buildingInfo.NewEngineering11,
    buildingInfo.InformationEngineering13,
    buildingInfo.Sanglokwon10,
    buildingInfo.Science02,
    buildingInfo.Student16,
    buildingInfo.Haklim15,
    buildingInfo.Hyehwa18,
    buildingInfo.Business01,
    buildingInfo.SocialScience09,
    buildingInfo.Munhwa06,
    buildingInfo.Haksul17,
  ],
  ListManhae04: [
    buildingInfo.Manhae04,
    buildingInfo.Law07,
    buildingInfo.Myeongjin05,
    buildingInfo.Science02,
    buildingInfo.Dahyang03,
    buildingInfo.Library14,
    buildingInfo.NewEngineering11,
    buildingInfo.Main08,
    buildingInfo.Sanglokwon10,
    buildingInfo.Wonheung12,
    buildingInfo.Hyehwa18,
    buildingInfo.Business01,
    buildingInfo.SocialScience09,
    buildingInfo.InformationEngineering13,
    buildingInfo.Munhwa06,
    buildingInfo.Student16,
    buildingInfo.Haklim15,
    buildingInfo.Haksul17,
  ],
  ListMyeongjin05: [
    buildingInfo.Myeongjin05,
    buildingInfo.Science02,
    buildingInfo.Manhae04,
    buildingInfo.Library14,
    buildingInfo.Law07,
    buildingInfo.NewEngineering11,
    buildingInfo.Sanglokwon10,
    buildingInfo.Main08,
    buildingInfo.Dahyang03,
    buildingInfo.Wonheung12,
    buildingInfo.InformationEngineering13,
    buildingInfo.Student16,
    buildingInfo.Haksul17,
    buildingInfo.Hyehwa18,
    buildingInfo.Business01,
    buildingInfo.SocialScience09,
    buildingInfo.Munhwa06,
    buildingInfo.Haksul17,
  ],
  ListMunhwa06: [
    buildingInfo.Munhwa06,
    buildingInfo.SocialScience09,
    buildingInfo.Hyehwa18,
    buildingInfo.Haksul17,
    buildingInfo.Business01,
    buildingInfo.Manhae04,
    buildingInfo.Myeongjin05,
    buildingInfo.Law07,
    buildingInfo.Science02,
    buildingInfo.Dahyang03,
    buildingInfo.Library14,
    buildingInfo.NewEngineering11,
    buildingInfo.Main08,
    buildingInfo.Sanglokwon10,
    buildingInfo.Wonheung12,
    buildingInfo.InformationEngineering13,
    buildingInfo.Student16,
    buildingInfo.Haksul17,
  ],
};
export { pinPositionData, buildings, buildingInfo, convenients, closeOrder };
