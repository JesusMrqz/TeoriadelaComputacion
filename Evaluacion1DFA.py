class AFD:
    def __init__(self, states, alphabet, transitions, initial_state, acceptance_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.acceptance_states = acceptance_states

    def process(self, string):
        current_state = self.initial_state
        for char in string:
            if char not in self.alphabet:
                return False
            current_state = self.transitions.get((current_state, char))
            if current_state is None:
                return False
        return current_state in self.acceptance_states

# Ejemplo para el Ejercicio 2 (n_a par, no "bc")
states = {'q_par', 'q_impar', 'q_par_b', 'q_impar_b', 'q_error'}
alphabet = {'a', 'b', 'c'}
transitions = {
    ('q_par', 'a'): 'q_impar', ('q_par', 'b'): 'q_par_b', ('q_par', 'c'): 'q_par',
    ('q_impar', 'a'): 'q_par', ('q_impar', 'b'): 'q_impar_b', ('q_impar', 'c'): 'q_impar',
    ('q_par_b', 'a'): 'q_impar', ('q_par_b', 'b'): 'q_par_b', ('q_par_b', 'c'): 'q_error',
    ('q_impar_b', 'a'): 'q_par', ('q_impar_b', 'b'): 'q_impar_b', ('q_impar_b', 'c'): 'q_error',
    ('q_error', 'a'): 'q_error', ('q_error', 'b'): 'q_error', ('q_error', 'c'): 'q_error'
}

afd_ej2 = AFD(states, alphabet, transitions, 'q_par', {'q_par', 'q_par_b'})

# Pruebas
test_strings = ["aa", "ab", "abc", "ba", "ac"]
for s in test_strings:
    print(f"Cadena '{s}': {'Aceptada' if afd_ej2.process(s) else 'Rechazada'}")
