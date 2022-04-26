from abc import ABC, abstractmethod

class Material(ABC):

    @abstractmethod
    def agg_state(self, t, scale):
        pass

class Chlorine(Material):
    boiling_t = -34.04
    melting_t = -101.5
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


material = Chlorine()
print(material.agg_state(-70, 'C'))
print(material.agg_state(-150, 'F'))
print(material.agg_state(-20, 'K'))
