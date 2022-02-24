import json


class Persona:
    __persona_name = ''
    __persona_surname = ''
    __persona_telefono = ''
    __persona_email = ''
    __address = None
    #per evitare di sprecare risorse, l'init è vuoto e viene caricato solo ciò che è strettamente necessario
    def __init__(self):
        pass
    # metodi get necessari per prendere i valori privati
    def get_persona_name(self):
        return self.__persona_name

    def get_persona_surname(self):
        return self.__persona_surname

    def get_persona_email(self):
        return self.__persona_email
    
    def get_persona_address(self):
        return self.__address

    def get_telefono(self):
        return self.__persona_telefono
    #metodi set per impostare degli attributi privati
    def set_persona_name(self,persona_name):
        self.__persona_name = persona_name

    def set_persona_surname(self,persona_surname):
        self.__persona_surname = persona_surname
        
    def set_persona_email(self,email):
        self.__persona_email = email
        
    def set_persona_address(self,persona_address):
        self.__address = persona_address

    def set_persona_telefono(self,telefono):
        self.__persona_telefono = telefono
    #metodo per ricavare il json della persona
    def get_json(self):
        addr = {}
        people= {}

        for c in self.__dict__:
            people[c] = self.__dict__[c]

        for a in self.__address.__dict__:
            addr[a] = self.__address.__dict__[a]

        people['_Persona__address'] = addr
        return json.dumps(people)
    #metodo per caricare il json partendo da una stringa json
    def set_json(self,jsonstr):
        load = json.loads(jsonstr)
        if '_Persona__address' in load.keys():
            addr = Address()
            self.__address = addr.set_from_dict(load['_Persona__address'])
            print(self.__dict__)
        if '_Persona__persona_name' in load.keys():
            self.__persona_name = load['_Persona__persona_name']
        if '_Persona__persona_surname' in load.keys():
            self.__persona_surname = load['_Persona__persona_surname']
        if '_Persona__persona_email' in load.keys():
            self.__persona_email = load['_Persona__persona_email']
        if '_Persona__persona_telefono' in load.keys():
            self.__persona_telefono = load['_Persona__persona_telefono']
        
#come sopra, solo che con un indirizzo anzichè con una persona
class Address:
    __addr_line_1 = ''
    __addr_line_2 = ''
    __addr_line_3 = ''
    __city = ''
    __zip = ''
    __state_province_country = ''
    __country = ''
    __other_addr_details = ''


    def __init__(self):
        pass

    def get_addr_line_1(self):
        return self.__addr_line_1

    def get_addr_line_2(self):
        return self.__addr_line_2

    def get_addr_line_3(self):
        return self.__addr_line_3

    def get_city(self):
        return self.__city

    def get_zip(self):
        return self.__zip

    def get_state_country_prov(self):
        return self.__state_province_country

    def get_country(self):
        return self.__country

    def get_other_details(self):
        return self.__other_addr_details

    #setter
    def set_addr_line_1(self,addr_line_1):
        self.__addr_line_1 = addr_line_1

    def set_addr_line_2(self,addr_line_2):
        self.__addr_line_2 = addr_line_2

    def set_addr_line_3(self,addr_line_3):
        self.__addr_line_3 = addr_line_3

    def set_city(self,city):
        self.__city = city

    def set_zip(self,zipp):
        self.__zip = zipp

    def set_state_country_prov(self,state_province_country):
        self.__state_province_country = state_province_country

    def set_country(self,country):
        self.__country = country

    def set_other_details(self,details):
       self.__other_addr_details = details

    def set_from_dict(self,diz):
        if '_Address__addr_line_1' in diz:
            self.__addr_line_1 = diz['_Address__addr_line_1']
        if '_Address__addr_line_2' in diz:
            self.__addr_line_2 = diz['_Address__addr_line_2']
        if '_Address__addr_line_3' in diz:
            self.__addr_line_3 = diz['_Address__addr_line_3']
        if '_Address__city' in diz:
            self.__city = diz['_Address__city']
        if '_Address__zip' in diz:
            self.__zip = diz['_Address__zip']
        if '_Address__state_province_country' in diz:
            self.__state_province_country = diz['_Address__state_province_country']
        if '_Address__country' in diz:
            self.__country = diz['_Address__country']
        if '_Address__other_addr_details' in diz:
            self.__other_addr_details = diz['_Address__other_addr_details']
        return self