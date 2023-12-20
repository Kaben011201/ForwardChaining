class Rule:
    def __init__(self, antecedent, consequent, name):
        self.antecedent = antecedent
        self.consequent = consequent
        self.name = name

class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_rule(self, antecedent, consequent, name):
        rule = Rule(antecedent, consequent, name)
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.add(fact)

    def apply_rules(self):
        while True:
            new_facts = set()

            for rule in self.rules:
                if rule.antecedent.issubset(self.facts) and rule.consequent not in self.facts:
                    new_facts.add(rule.consequent)
                    print(f"Applying rule '{rule.name}': {rule.antecedent} => {rule.consequent}")

            if not new_facts:
                break

            self.facts.update(new_facts)

if __name__ == "__main__":
    # Contoh penggunaan
    system = RuleBasedSystem()

    # Menentukan aturan-aturan
    system.add_rule({"A", "B"}, "C", "Rule 1")
    system.add_rule({"C"}, "D", "Rule 2")
    system.add_rule({"D"}, "E", "Rule 3")

    # Menambahkan fakta awal
    system.add_fact("A")
    system.add_fact("B")

    # Melakukan forward chaining
    system.apply_rules()

    # Menampilkan fakta-fakta akhir
    print("Fakta Akhir:", system.facts)
