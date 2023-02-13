""" Crie uma classe que represente uma viagem de avião, onde temos como atributos os aeroportos de origem e de destino. Caso queiramos somar uma viagem de A para B com uma de B para C, o resultado precisa ser uma viagem de A para C. """

class Travel:
    def __init__(self, origin:str, destiny:str) -> None:
        self.origin = origin
        self.destiny = destiny
        
    def __add__(self, other):
        if self.destiny != other.origin:
            raise ValueError(f"Não há uma conexão direta entre {self.destiny} e {other.origin}")
        return Travel(self.origin, other.destiny)
    
    def __repr__(self):
        return f'Embargue: {self.origin}, Desembargue: {self.destiny}'

a = Travel('brasil', 'new york')
b = Travel('new york', 'mexico')
c = a + b

print(f'a: {a}\nb: {b}\nc: {c}')