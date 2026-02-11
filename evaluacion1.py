class Automata:
    def __init__(self):
        self.transiciones = {
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q1', 'b': 'q2'},
            'q2': {'a': 'q2', 'b': 'q2'}
        }
        self.estado_final = 'q2'

    def validar(self, cadena):
        estado = 'q0'
        for simbolo in cadena:
            if simbolo in self.transiciones[estado]:
                estado = self.transiciones[estado][simbolo]
            else:
                return False
        return estado == self.estado_final

dfa = Automata()

aceptadas = ["bb", "ababa", "baaaab"]
rechazadas = ["a", "aba", "aaaaaa"]

print("--- CADENAS ACEPTADAS ---")
for c in aceptadas:
    print(f"'{c}': {dfa.validar(c)}")

print("\n--- CADENAS RECHAZADAS ---")
for r in rechazadas:
    print(f"'{r}': {dfa.validar(r)}")
