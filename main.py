from persona import Address,Persona

addr = Address()
addr.set_addr_line_1("via Customer1")
addr.set_city("Milano")
addr.set_country("Italia")
addr.set_zip('20100')
people = Persona()
people.set_persona_name('Mario')
people.set_persona_surname('Rossi')
people.set_persona_address(addr)

newaddr = Address()

newaddr.set_city('Milano')

newaddr.set_addr_line_2('n.36')

newpeople = Persona()

newpeople.set_persona_address(newaddr)

newpeople.set_persona_email('000')

prova = newpeople.get_json()
# nome di fantasia per testare che funzioni il caricamento da jsonstring
ciccio = Persona()

ciccio.set_json(prova)
print(ciccio.get_json())

"""
To do :
    classe Agenda che è un insieme di Persone
    selezione di agenda per andare a modificare un contatto
    persistence
    delete
    prettyprint agenda, prettyprint persona
    
    """