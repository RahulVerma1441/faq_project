from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Fallback to original text