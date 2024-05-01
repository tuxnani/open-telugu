# Telugu language has removed some old letters of alphabet with simpler replacements.
# This program would parse through text and replace such occurences.
#
#
#
#	Incident character - Replacement
#	ఱ - ర
#	ఁ - ం / ""
#	౧ - 1 
#	౨ - 2
#	౩ - 3
#	౪ - 4
#	౫ - 5
#	౬ - 6
#	౭ - 7
#	౮ - 8
#	౯ - 9
#	౦ - 0

class TeluguNormalizer:
  """
  This class provides functionality to replace old type letters with new letters in a given string.
  """

  def __init__(self, old_letters_map):
    """
    Initializes the converter with a dictionary mapping old letters to new letters.

    Args:
      old_letters_map: A dictionary where keys are old letters and values are corresponding new letters.
    """
    self.old_letters_map = old_letters_map

  def normalize(self, text):
    """
    Replaces old type letters in the provided text with their corresponding new letters.

    Args:
      text: The string containing text to be converted.

    Returns:
      A new string with old letters replaced by new letters.
    """
    new_text = ""
    for char in text:
      if char in self.old_letters_map:
        new_text += self.old_letters_map[char]
      else:
        new_text += char
    return new_text

# Example usage
normalizer = TeluguNormalizer({
  'ఱ': 'ర',  # Replace 'ఱ' with 'ర'
  'ఁ': '',  # Replace అరసున్నా with పూర్తి సున్నా
  '౦': '0',
  '౧': '1',
  '౨': '2',
  '౩': '3',
  '౪': '4',
  '౫': '5',
  '౬': '6',
  '౭': '7',
  '౮': '8',
  '౯': '9'
                    
  # Add more mappings as needed
})

original_text = "గుఱ్ఱము, కఱ్ఱ, జాఱుడుబల్ల, అతఁడు, మాఁడు"
converted_text = normalizer.normalize(original_text)

print(f"Original text: {original_text}")
print(f"Converted text: {converted_text}")
