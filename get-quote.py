def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    for j in range (0,len(quotes)):
        quotes[j]=quotes[j].replace("\n","")
    f.close()
    print(quotes[14:18])
        
    mi_path = "fichero.txt"
    g = open(mi_path, 'a+')
    for i in quotes:
        g.write(i)
        g.write("\n")
    g.close()

if __name__== "__main__":
    primary()
