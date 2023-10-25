notes = {
    "Benjamin": 19,
    "Nikki": 11,
    "Zébulon": 6,
    "Isabel": 20
}

meilleurEleve = max(notes, key=notes.get)
print("L'élève avec la meilleure note est", meilleurEleve, "avec une note de", notes[meilleurEleve])