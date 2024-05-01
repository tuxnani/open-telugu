class NumberToWords:
  """
  This class converts an integer number to its word representation in English.
  """

  def __init__(self):
    self.number_words = {
      1: "ఒకటి",
      2: "రెండు",
      3: "మూడు",
      4: "నాలుగు",
      5: "ఐదు",
      6: "ఆరు",
      7: "ఏడు",
      8: "ఎనిమిది",
      9: "తొమ్మిది",
      10: "పది",
      11: "పదకొండు",
      12: "పన్నెండు",
      13: "పదమూడు",
      14: "పద్నాలుగు",
      15: "పదిహేను",
      16: "పదహారు",
      17: "పదిహేడు",
      18: "పద్దెనిమిది",
      19: "పంతొమ్మిది",
      20: "ఇరవై",
      30: "ముప్ఫై",
      40: "నలభై",
      50: "యాభై",
      60: "అరవై",
      70: "డెబ్బై",
      80: "ఎనభై",
      90: "తొంభై",
      100: "నూట",
    }

  def convert(self, number):
    """
    Converts an integer number to its word representation.

    Args:
      number: The integer number to be converted (between 0 and 999).

    Returns:
      A string representing the number in words.
    """

    if not 0 <= number <= 999:
      return "ప్రస్తుతం 0 నుండి 999 వరకే ఈ అనువర్తనం పని చేస్తుంది."

    # Handle single digits and teens
    if number < 20:
      return self.number_words[number]
    if number == 100:
      return "నూరు/వంద"

    # Handle tens and hundreds
    tens_digit = number // 10 * 10
    ones_digit = number % 10
    word = self.number_words.get(tens_digit, "")

    if ones_digit > 0:
      word += " " + self.number_words[ones_digit]

    if number >= 100:
      if number < 200:
        word = "నూట" + (" " if word else "") + word
      else: 
        word = self.number_words[number // 100] + " వందల" + (" " if word else "") + word

    return word.strip()

# Example usage
converter = NumberToWords()

numbers = [123, 45, 789, 100]
for number in numbers:
  word_representation = converter.convert(number)
  print(f"{number} అంకె పదాల్లో: {word_representation}")
