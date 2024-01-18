class tamboresana:
    def __init__(self, valgi, rindas, fig="bumba"):
        self.valgi = valgi
        self.rindas = rindas
        self.fig = fig
        self.raksts = []

    def generate_raksts(self):
        for _ in range(self.rindas):
            rinda = []
            for _ in range(self.valgi):
                rinda.append(self.random_valgi())
            self.raksts.append(rinda)

    def valdzini(self):
        valgi = ['sc', 'dc', 'tr', 'sl st', 'hdc', 'dc2tog', 'tr2tog'] #visi valdziņu veidi(angliski)
        return valgi[self.valgi % len(valgi)]

    def print_raksts(self):
        for rinda in self.raksts:
            print(' '.join(rinda))

    def generate_fig(self):
        if self.fig == "bumba":
            self.valgi = 1
            for i in range(self.rindas):
                rinda = []
                for _ in range(self.valgi):
                    rinda.append(self.valdzini())
                    self.raksts.append(rinda)

                    if i < self.rindas // 2:
                        self.valgi += 2
                    else:
                        self.valgi -= 2

        elif self.fig == "kvadrats":
            self.valgi = 1
            for i in range(self.rindas):
                rinda = []
                for _ in range(self.valgi):
                    rinda.append(self.valdzini())
                self.raksts.append(rinda)

        elif self.fig == "trijsturis":
            self.valgi = 1
            for i in range(self.rindas):
                rinda = []
                for _ in range(self.valgi):
                    rinda.append(self.valdzini())
                self.raksts.append(rinda)

                if i < self.rindas // 2:
                    self.valgi += 1


if __name__ == "__main__":
    fig = input("Kādu figūru veidosiet?")
    raksts = tamboresana(10, 10, fig)
    if fig == 'bumba' or fig == 'kvadrats' or fig == 'trijsturis':
        raksts.generate_fig() 
    else:
        raksts.generate_raksts()
    raksts.print_raksts() 