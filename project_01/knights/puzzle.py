from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave), # A must be either a knight or a knave
    Implication(AKnight, And(AKnight, AKnave)) # If A is a knight, then A is both a knight and a knave, which is paradoxical so we know A is a knave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)), # A and B can be either knights or knaves
    Biconditional(And(AKnave, BKnave), AKnight), # If A is telling the truth, both A and B are knaves, A is a knight (paradoxical)
    Implication(AKnave, BKnight) # if A is a knave then B must be a knight since knaves can't tell the truth
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)), # A and B can be either knights or knaves
    Biconditional(And(AKnight, BKnight), AKnight), # If A and B are knights, A is a knight
    Biconditional(And(AKnave, BKnave), AKnight),  # If A and B are knaves, A is a knight (paradoxical)
    Implication(AKnave, BKnight) # if A is a knave then B must be a knight since knaves can't tell the truth
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

#     A is a Knave
#     B is a Knight
#     C is a Knave

#todo update logic

knowledge3 = And(
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)), # A, B, and C can be either knights or knaves
    Biconditional(And(AKnave, CKnave), BKnight), # If A and C are knaves, B is a knight
    Biconditional(And(AKnave, BKnave), AKnight), # If A and B are knaves, A is a knight
    Implication(AKnave, CKnave) # If A is a knave then C is a knave
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
