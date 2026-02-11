
class DFA:
    def __init__(self):
      
        self.q0 = 0
        self.q1 = 1
        self.q2 = 2
        self.q3 = 3  

        self.estado_inicial = self.q0
        self.estados_finales = {self.q0, self.q2}

  
        self.transiciones = {
            (self.q0, 'a'): self.q1,
            (self.q0, 'b'): self.q2,
            (self.q0, 'c'): self.q0,

            (self.q1, 'a'): self.q0,
            (self.q1, 'b'): self.q2,
            (self.q1, 'c'): self.q1,

            (self.q2, 'a'): self.q1,
            (self.q2, 'b'): self.q2,
            (self.q2, 'c'): self.q3,  

            (self.q3, 'a'): self.q3,
            (self.q3, 'b'): self.q3,
            (self.q3, 'c'): self.q3,
        }

    def acepta(self, cadena):
        estado = self.estado_inicial

        for simbolo in cadena:
            if simbolo not in {'a','b','c'}:
                raise ValueError(f"Símbolo inválido: {simbolo}")
            estado = self.transiciones[(estado, simbolo)]

        return estado in self.estados_finales


# ---------- Pruebas ----------
if __name__ == "__main__":
    dfa = DFA()

    pruebas = ["", "aa", "aba", "abba", "ab", "abc", "abbc", "aab", "bbaaa"]

    for p in pruebas:
        print(f"{p!r} ->", "ACEPTA" if dfa.acepta(p) else "RECHAZA")
