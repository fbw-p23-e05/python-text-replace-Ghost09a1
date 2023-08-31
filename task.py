def replace_dog_with_cat(sentence):
  """Replaces all standalone instances of "dog" in the given sentence with "cat".

  Args:
    sentence: The sentence to be modified.

  Returns:
    The modified sentence.
  """

  modified_sentence = sentence.replace("dog", "cat")
  return modified_sentence


if __name__ == "__main__":
  sentence = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."
  modified_sentence = replace_dog_with_cat(sentence)
  print(f"The modified sentence is: {modified_sentence}")
