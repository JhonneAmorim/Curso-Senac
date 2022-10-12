class EscalaDeMedida:

  def __init__(self):
    medida_cm = 0

  def converter_medida(self):
    
    mm = self.medida_cm * 10
    dm = self.medida_cm / 10
    m = self.medida_cm / 100
    dam = self.medida_cm / 1000
    hm = self.medida_cm / 10000
    km = self.medida_cm / 100000

    print(f"O valor da medida em mm {mm}")
    print(f"O valor da medida em dm {dm}")
    print(f"O valor da medida em m {m}")
    print(f"O valor da medida em dam {dam}")
    print(f"O valor da medida em hm {hm}")
    print(f"O valor da medida em km {km}")
