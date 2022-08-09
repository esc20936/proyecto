import metodoFuerzaBruta as mfb
import DPLL

formula = [{("p", True), ("q", False)}, {("p", True), ("r", True)}]
formula2 = [{("r", True)}, {("p", False), ("r", False)},{("p", False), ("q", True), ("r", False)},{("q",True)}]


print(mfb.fuerzaBruta(formula2))
print(DPLL.dpll(formula2))