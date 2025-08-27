from datetime import datetime

def mostrar_hora():
  """Imprime a hora atual do sistema."""
  agora = datetime.now()
  print(f"A hora atual é: {agora.strftime('%H:%M:%S')}")


mostrar_hora()