kuha = float(input("Kuika pitkä kuha on?: "))
liian_pieni = 37
if kuha<37:
    puuttuva_pituus = liian_pieni - kuha
    print(f"Palauta kuha järveen. Se on {puuttuva_pituus:.0f} cm alle sallitun pyyntimitan.")
