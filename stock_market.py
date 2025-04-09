import random


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


class CommandPrompt:
    def __init__(self, buy, sell, wait):
        self.choices = (buy, sell, wait)

    def ask(self):
        while True:
            choice = input('Decision [b/s/w/buy/sell/wait]: ')
            if not any(choice in group for group in self.choices):
                print(f'Invalid choice: {choice}')
            elif choice in self.choices[0]:
                return 'buy'
            elif choice in self.choices[1]:
                return 'sell'
            elif choice in self.choices[2]:
                return 'wait'
            

class Wallet:
    def __init__(self, pln, usd):
        self.wallet_pln = pln
        self.wallet_usd = usd

    def convert_pln_to_usd(self, usdpln_rate):
        self.wallet_usd += self.wallet_pln / usdpln_rate
        self.wallet_pln = 0

    def convert_usd_to_pln(self, usdpln_rate):
        self.wallet_pln += self.wallet_usd * usdpln_rate
        self.wallet_usd = 0


def main(usdpln_rates):
    wallet = Wallet(100.0, 0.0)
    command_prompt = CommandPrompt(('b', 'buy'), ('s', 'sell'), ('w', 'wait', ''))

    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(wallet.wallet_pln, 2)} PLN, ${round(wallet.wallet_usd, 2)}, rate {usdpln_rate}')
        choice = command_prompt.ask()
        if choice in ('b', 'buy'):
            wallet.convert_pln_to_usd(usdpln_rate)
        elif choice in ('s', 'sell'):
            wallet.convert_usd_to_pln(usdpln_rate)
            

    wallet.wallet_pln += wallet.wallet_usd * usdpln_rate
    wallet.wallet_usd = 0
    print(f'Your result: {wallet.wallet_pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)
    