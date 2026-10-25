
detector = {'TT':'температура', 
            'PT':'давление', 
            'LT':'уровень', 
            'FT':'расход'}

check_list = ['TT', 'PT', 'LT', 'FT']

def parse_tag(tag):
    plant, type1, parametr = tag.split('.')
    value, number = type1.split('_')
    detect = detector.get(value,'неизвестно')
    return (plant, value, number, detect, parametr)


if __name__ == "__main__":
    tags = [
    "KTP2.TT_101.PV",
    "KTP2.PT_204.PV", 
    "NS1.LT_12.SP", 
    "NS1.FT_7.PV", 
    "VODOKANAL3.PT_1.PV", 
    "K1.QT_55.PV"
]
    for t in tags:
        parts = parse_tag(t)
        print(" | ".join(parts))
    
    
    


    
