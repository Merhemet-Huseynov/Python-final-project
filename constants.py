# Tort növləri və onların qiymətləri, hazırlama vaxtı və maya qiyməti
class ORDER:
    ORDERS_AVİLABLE = {
        "Ad günü tortu": {"Satış qiyməti": 18,
                          "Maya qiyməti": 10,
                          "Hazırlanma vaxtı": 3
                        },

        "Toy üçün tort": {"Satış qiyməti": 20, 
                          "Maya qiyməti": 11, 
                          "Hazırlanma vaxtı": 5
                        }
    }


# Tort dekorasiyaları
class DECORATIONS:
    POSSIBLE_DECORATIONS = [
        "Üzərində çiçək dekorasiyaları", 
        "Üzərində açıq rəngli çiçəklər",
        "Üzərində ağ şokolad parçaları", 
        "Üzərində tünd şokoladlı parçalar", 
        "Üzərində çiyələklər", 
        "Üzərində kivi və ananas",  
        "Üzərində şəkərdən hazırlanmış fiqurlar", 
    ]


# Şirniyat növləri, maya qiyməti və satış qiymətləri 
class SWEETS:
    SWEETS_AVELIABLE = {
        "Şəkərbura": {
                    "Maya dəyəri": 6,
                    "Satış qiymət": 11,
        },
        "Paxlava": {
                    "Maya dəyəri": 6,
                    "Satış qiymət": 12,
        },
        "Ağ şokoladlı ekler": {
                    "Maya dəyəri": 9,
                    "Satış qiymət": 14,
        },
        "Türk paxlavası": {
                    "Maya dəyəri": 10,
                    "Satış qiymət": 16,
        },
        "Çiyələkli tart": {
                    "Maya dəyəri": 5,
                    "Satış qiymət": 10,
        },
        "Candy waffle": {
                    "Maya dəyəri": 10,
                    "Satış qiymət": 16,
        },
        "Şokoladlı ekler": {
                    "Maya dəyəri": 6,
                    "Satış qiymət": 12,
        }
    }


# Tort növləri, maya qiyməti və satış qiymətləri 
class CAKE:
    CAKE_AVELIABLE = {
        "Napoleon tortu": {
                    "Maya dəyəri": 9,
                    "Satış qiymət": 15,
        },
        "Ballı tort": {
                    "Maya dəyəri": 6,
                    "Satış qiymət": 10,
        },
        "Şokoladlı tort": {
                    "Maya dəyəri": 8,
                    "Satış qiymət": 13,
        },
        "Banalı tort": {
                    "Maya dəyəri": 6,
                    "Satış qiymət": 11,
        },
        "Lemonlu tort": {
                    "Maya dəyəri": 10,
                    "Satış qiymət": 15,
        }
    }   


class MENU:
    BEVERAGES = {
            "limonad": {
                "Maya Dəyəri": 1.5,
                "Satış Qiyməti": 3
            },
            "kola": {
                "Maya Dəyəri": 1,
                "Satış Qiyməti": 2
            },
            "çay": {
                "Maya Dəyəri": 1,
                "Satış Qiyməti": 2
            },
            "kofe": {
                "Maya Dəyəri": 1.5,
                "Satış Qiyməti": 3
            },
            "kapuçino": {
                "Maya Dəyəri": 2,
                "Satış Qiyməti": 4
        }
    }
    
    SWEETS_MENU = {
            "çizkeyk": {
                "Maya Dəyəri": 3,
                "Satış Qiyməti": 6
            },
            "şokoladlı kek": {
                "Maya Dəyəri": 2.5,
                "Satış Qiyməti": 5
            },
            "ağ ekler": {
                "Maya Dəyəri": 1.5,
                "Satış Qiyməti": 4
            },
            "qara ekler": {
                "Maya Dəyəri": 4,
                "Satış Qiyməti": 8
        }
    }