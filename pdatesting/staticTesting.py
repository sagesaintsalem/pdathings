class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # Should be == here
      return True
    else # Missing a colon
      return False
   

  dif highest_card(self, card1 card2): # def is misspelled, missing a comma between card1 and card2
  if card1.value > card2.value: # if statement should be indented
    return card # card has not been declared, I assume it's supposed to be card1
  else:
    return card2
  


def cards_total(self, cards): # this should be indented
  total # improperly declared variable, no value given
  for card in cards:
    total += card.value 
    return "You have a total of" + total # return needs to be aligned with initial for statement or it won't loop properly, also need a space at the end of the string for readability
    # Also, integers cannot be concatenated, total needs to be converted to string