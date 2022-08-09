import metodoFuerzaBruta as mfb
import DPLL





inciso1 = [{("r", True)}, {("p", False), ("r", False)},{("p", False), ("q", True), ("r", False)},{("q",True)}]
inciso2= [{('r',True)},{('q',False),('r',False)},{('p',False),('q',True),('r',False)},{('q',True)}]
inciso3= [{('p',True)},{('p',False)}]



print(mfb.fuerzaBruta(inciso1))
print(mfb.fuerzaBruta(inciso2))
print(mfb.fuerzaBruta(inciso3))


print(DPLL.dpll(inciso1))
print(DPLL.dpll(inciso2))
print(DPLL.dpll(inciso3))