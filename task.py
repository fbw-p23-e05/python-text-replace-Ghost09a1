def replace_word(sentence, target_word, replacement_word):
    words = sentence.split()
    for i in range(len(words)):
        if words[i] == target_word:
            words[i] = replacement_word
    new_sentence = ' '.join(words)
    return new_sentence

input_sentence = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."
target_word = "dog"
replacement_word = "cat"

output_sentence = replace_word(input_sentence, target_word, replacement_word)
print(f"Output: {output_sentence}")
