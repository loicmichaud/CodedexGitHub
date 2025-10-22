def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }
    def translate_word(word):
        print("Looking for word:", word.lower())
        if language in translations:
            if word.lower() in translations[language]:
                print("In dictionary:", translations[language])
                return translations[language][word.lower()]
            else : return "translation not available"
        else : return "language not supported"

    return translate_word

lang = input("enter a language").lower().strip()
print("Language entered:", lang)
translate = translator(lang)

word = input("Enter a word to translate :").strip()

print(translate(word))

