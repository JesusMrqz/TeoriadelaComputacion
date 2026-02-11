class AutomataComplejo:
    def __init__(self):
        self.transiciones = {
            'q0': {'0': 'q1', '1': 'q2'},
            'q1': {'1': 'q3'},
            'q2': {'0': 'q3'},
            'q3': {'0': 'q0', '1': 'q1'}
        }
        self.estado_final = 'q3'

    def validar(self, cadena):
        estado_actual = 'q0'
        try:
            for simbolo in cadena:
                estado_actual = self.transiciones[estado_actual][simbolo]
            return estado_actual == self.estado_final
        except KeyError:
            return False

dfa = AutomataComplejo()

aceptadas = ["01", "10", "111"] 

rechazadas = ["0", "1", "010"]

print("--- RESULTADOS DEL SEGUNDO DIAGRAMA ---")
print("Aceptadas (llegan a q3):", [c for c in aceptadas if dfa.validar(c)])
print("Rechazadas (no llegan a q3):", [r for r in rechazadas if not dfa.validar(r)])
