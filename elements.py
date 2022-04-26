class Element:
    boiling_t = 0
    melting_t = 0

    def agg_state(self, t, scale):
        if scale == 'K':
            self.boiling_t -= 237.15
            self.melting_t -= 237.15
        if scale == 'F':
            self.boiling_t = self.boiling_t * 1.8 + 32
            self.melting_t = self.boiling_t * 1.8 + 32
        else:
            pass

        if t <= self.melting_t:
            return 'SOLID'
        elif self.melting_t < t < self.boiling_t:
            return 'LIQUID'
        elif t >= self.boiling_t:
            return 'GAS'



class Chlorine(Element):
    boiling_t = -34.04
    melting_t = -101.5
class Oxygen(Element):
    boiling_t = -183
    melting_t = -218
class Iron(Element):
    boiling_t = 2861
    melting_t = 1538

elem = Chlorine()
print(elem.agg_state(-70, 'C'))
print(elem.agg_state(-150, 'F'))
print(elem.agg_state(-20, 'K'))
