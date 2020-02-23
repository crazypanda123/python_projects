class bank(object):
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield '$100'

if __name__ == '__main__':
    hsbc = bank()
    corner_street_atm = hsbc.create_atm()
    print(corner_street_atm.next())
    for cash in corner_street_atm:
        print cash                  