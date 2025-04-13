def get_concepts():
    import openai
    import os
    import wikipedia
    return {
        "first law of thermodynamics": "The First Law states that energy cannot be created or destroyed—only transformed. Mathematically: ΔU = Q - W, where ΔU is change in internal energy, Q is heat added, and W is work done by the system.",
        "second law of thermodynamics": "The Second Law states that entropy of an isolated system always increases over time. It introduces the concept of irreversibility in natural processes.",
        "third law of thermodynamics": "The Third Law states that as temperature approaches absolute zero, the entropy of a perfect crystal approaches zero.",
        "zeroth law of thermodynamics": "The Zeroth Law states that if two systems are each in thermal equilibrium with a third, then they are in thermal equilibrium with each other.",
        "isentropic process": "An isentropic process is both adiabatic and reversible, meaning there is no change in entropy (ΔS = 0). It's ideal for modeling compressors and turbines.",
        "isothermal process": "In an isothermal process, temperature remains constant (ΔT = 0). Heat added equals work done by the gas.",
        "adiabatic process": "In an adiabatic process, no heat is exchanged (Q = 0). All energy transfer is in the form of work.",
        "enthalpy": "Enthalpy (H) is the total heat content of a system. H = U + PV, where U is internal energy, P is pressure, and V is volume.",
        "entropy": "Entropy is a measure of disorder or randomness in a system. It determines the direction of thermodynamic processes.",
        "internal energy": "Internal energy is the total energy stored within a system, including kinetic and potential energy of molecules."
    }

def explain_concept(user_input):
    concepts = get_concepts()
    user_input = user_input.lower().strip()

    for concept, explanation in concepts.items():
        if user_input in concept:
            return f"\n📘 Concept: {concept.title()}\n{explanation}"

    return "\n❌ Concept not found. Try terms like 'First Law of Thermodynamics' or 'Entropy'."

def main():
    print("🌡 Thermodynamics Concept Explainer")
    print("Type a concept (e.g., 'First Law of Thermodynamics') to learn more.\n")

    while True:
        user_input = input("🔍 Enter concept (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("👋 Goodbye! Stay cool under pressure.")
            break
        print(explain_concept(user_input))

if _name_ == "_main_":
    main()
