x = float (input('Kwota:'))

VAT = (x/100)*23

txt = "Kwota jest: {} i Vat23% : {:.2f} "

print(txt.format(x,VAT))