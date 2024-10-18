import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI)

months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November','December']
years = [str(x) for x in range(1992,2022)] 

pages = []
for y in years:
    for m in months:
        page = f"Deaths_in_{m}_{y}"
        pages.append(page)

names = []
for page in pages:
    p_wiki = wiki_wiki.page(page)
    text = p_wiki.text.split("\n")
    deaths = text[6:]
    for death in deaths:
        try:
            int(death)
        except ValueError:
            if death != "":    
                name = death.split(",")
                names.append(name[0])
print(names)
