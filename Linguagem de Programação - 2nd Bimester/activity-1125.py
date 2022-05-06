# Cálculo de notas
# By: Ariel Paixão
# GitHub: ArielMn2

notaDosTrabalhos = float(input())
notaDaProvaRegular = float(input())

NOTA_MAXIMA_SUBSTITUTIVA = 10

media = (notaDosTrabalhos + notaDaProvaRegular) / 2

if (media >= 6):
  print('aprovado')
elif ((notaDosTrabalhos + NOTA_MAXIMA_SUBSTITUTIVA) / 2 >= 6):
  print('talvez com a sub')
else:
  print('reprovado')