class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_rule(self, antecedent, consequent):
        self.rules.append((antecedent, consequent))

    def add_fact(self, fact):
        self.facts.add(fact)

    def forward_chain(self):
        new_fact_found = True
        while new_fact_found:
            new_fact_found = False
            for ante, cons in self.rules:
                if isinstance(ante, list):
                    condition_met = all(condition in self.facts for condition in ante)
                else:
                    condition_met = ante in self.facts
                if condition_met and cons not in self.facts:
                    self.facts.add(cons)
                    new_fact_found = True
                    print(f"Inferred new fact: {cons}")
        print("\nInference complete. Final facts:")
        for fact in sorted(self.facts):
            print(f"  {fact}")

if __name__ == "__main__":
    system = RuleBasedSystem()
    
    system.add_rule("has_scales", "is_reptile")
    system.add_rule(["is_reptile", "no_legs"], "is_snake")
    system.add_rule(["is_snake", "venomous"], "is_venomous_snake")
    system.add_rule(["is_snake", "constrictor"], "is_constrictor_snake")
    system.add_rule(["is_snake", "lays_eggs"], "is_oviparous_snake")
    system.add_rule(["is_snake", "gives_live_birth"], "is_viviparous_snake")
    system.add_rule(["is_snake", "has_rattle"], "is_rattlesnake")
    system.add_rule(["is_snake", "is_large", "constrictor"], "is_python")

    system.add_fact("has_scales")
    system.add_fact("no_legs")
    system.add_fact("constrictor")
    system.add_fact("is_large")
    system.add_fact("lays_eggs")

    system.forward_chain()