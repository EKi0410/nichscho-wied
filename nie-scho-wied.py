import time

print("-----------------")
print("|  Willkommen!  |")
print("-----------------\n\n")
time.sleep(1)

print("-----------------------------")
print("| Nicht schon wieder! V.0.1 |")
print("-----------------------------\n\n")
time.sleep(1)

verschlüsseln=input("[1] zum verschlüsseln, [2] zum entschlüsseln ->  ")
print("\n")

while verschlüsseln=="1":
 
 print("-----------------")
 print("| VERSCHLÜSSELN |")
 print("-----------------\n\n")
 
 #variablen zur Verschlüsselung
 bcode = ("4536")
 ccode = ("8746")
 dcode = ("7921")
 fcode = ("5543")
 gcode = ("7741")
 hcode = ("9752")
 jcode = ("1123")
 kcode = ("5421")
 lcode = ("3000")
 mcode = ("6150")
 ncode = ("7810")
 pcode = ("4512")
 qcode = ("9851")
 rcode = ("4652")
 scode = ("3312")
 tcode = ("8523")
 vcode = ("7741")
 wcode = ("1142")
 xcode = ("3267")
 ycode = ("9463")
 zcode = ("2245")
 leercode=("0011")
 punkt=("1100")
 frage=("1325")
 ausrufe=("6654")
 komma=("9998")

 text1 = input("Satz zum verschlüsseln eingeben:\n")

 print("\n")

 text1=text1.replace("b", bcode)
 text1=text1.replace("c", ccode)
 text1=text1.replace("d", dcode)
 text1=text1.replace("f", fcode)
 text1=text1.replace("g", gcode)
 text1=text1.replace("h", hcode)
 text1=text1.replace("j", jcode)
 text1=text1.replace("k", kcode)
 text1=text1.replace("l", lcode)
 text1=text1.replace("m", mcode)
 text1=text1.replace("n", ncode)
 text1=text1.replace("p", pcode)
 text1=text1.replace("q", qcode)
 text1=text1.replace("r", rcode)
 text1=text1.replace("s", scode)
 text1=text1.replace("t", tcode)
 text1=text1.replace("v", vcode)
 text1=text1.replace("w", wcode)
 text1=text1.replace("x", xcode)
 text1=text1.replace("y", ycode)
 text1=text1.replace("z", zcode)
 text1=text1.replace(" ", leercode)
 text1=text1.replace("?", frage)
 text1=text1.replace("!", ausrufe)
 text1=text1.replace(".", punkt)
 text1=text1.replace(",", komma)

 text1=text1.replace("B", bcode)
 text1=text1.replace("B", ccode)
 text1=text1.replace("D", dcode)
 text1=text1.replace("F", fcode)
 text1=text1.replace("G", gcode)
 text1=text1.replace("H", hcode)
 text1=text1.replace("J", jcode)
 text1=text1.replace("K", kcode)
 text1=text1.replace("L", lcode)
 text1=text1.replace("M", mcode)
 text1=text1.replace("N", ncode)
 text1=text1.replace("P", pcode)
 text1=text1.replace("Q", qcode)
 text1=text1.replace("R", rcode)
 text1=text1.replace("S", scode)
 text1=text1.replace("T", tcode)
 text1=text1.replace("V", vcode)
 text1=text1.replace("W", wcode)
 text1=text1.replace("X", xcode)
 text1=text1.replace("X", ycode)
 text1=text1.replace("Z", zcode)



 print("\nText vollständig verschlüsselt!\n")

 ausgabe=input("Achtung! verschlüsselter Text wird nach bestätigung angezeigt! [Y] ")
 print("\n")

 if ausgabe=="y":
  print(text1)
  verschlüsseln=6

 else: print("Programm beendet.")

if verschlüsseln=="2":

 #Entschlüssselung

 print("-----------------")
 print("| ENTSCHLÜSSELN |")
 print("-----------------\n\n")
 
 text3=input("Text zum entschlüsseln eingeben:\n")

 #Decodierung
 #Evtl. Großbuchstaben hinzufügen...
 
 
 
 #Variablen für Buchstaben
 bb = "b"
 cc = "c"
 dd = "d"
 ff = "f"
 gg = "g"
 hh = "h"
 jj = "j"
 kk = "k"
 ll = "l"
 mm = "m"
 nn = "n"
 pp = "p"
 qq = "q"
 rr = "r"
 ss = "s"
 tt = "t"
 vv = "v"
 ww = "w"
 xx = "x"
 yy = "y"
 zz = "z"
 
 leercode2 = " "
 punkt2 = "."
 frage2 = "?"
 ausrufe2 = "!"
 komma2 = ","


 text3=text3.replace("4536", bb)
 text3=text3.replace("8746", cc)
 text3=text3.replace("7921", dd)
 text3=text3.replace("5543", ff)
 text3=text3.replace("7741", gg)
 text3=text3.replace("9752", hh)
 text3=text3.replace("1123", jj)
 text3=text3.replace("5421", kk)
 text3=text3.replace("3000", ll)
 text3=text3.replace("6150", mm)
 text3=text3.replace("7810", nn)
 text3=text3.replace("4512", pp)
 text3=text3.replace("9851", qq)
 text3=text3.replace("4652", rr)
 text3=text3.replace("3312", ss)
 text3=text3.replace("8523", tt)
 text3=text3.replace("7741", vv)
 text3=text3.replace("1142", ww)
 text3=text3.replace("3267", xx)
 text3=text3.replace("9463", yy)
 text3=text3.replace("2245", zz)
 text3=text3.replace("0011", leercode2)
 text3=text3.replace("1325", frage2)
 text3=text3.replace("6654", ausrufe2)
 text3=text3.replace("1100", punkt2)
 text3=text3.replace("9998", komma2)

 print("\n\n")
 text3show=input("Text vollständig entschlüsselt. Nun anzeigen? [Y] ")
 print("\n\n")

 if text3show=="y":
   print(text3)
 else: print("Programm beendet.")
 
 
 





