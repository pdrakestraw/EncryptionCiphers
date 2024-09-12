from ciphers.utilities.characters import alphabet


def caesar_cipher_translate(prompt, shift, phase):
    new_message = ''
    n_chars = len(alphabet)

    new_char_index = None
    for character in prompt:
        char_index = alphabet.index(character)
        if phase:
            new_char_index = (char_index + shift) % n_chars
        elif not phase:
            new_char_index = (char_index - shit) % n_chars
        new_message += alphabet[new_char_index]
    return new_message
