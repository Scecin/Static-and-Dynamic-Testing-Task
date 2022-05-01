### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):
    # We need to use the equality operator (==) to compare if the two values are equal, and in this line we have an assigment operator.
    if card.value = 1:
      return True
      # we have to end any loop with a colon (:)
    else
      return False
   
  # There are two syntax errors. First, every method must start with the word def, not dif.
  # and the second one, we need to use a comma to separate any attributes in the method. (self, card1, card2)
  dif highest_card(self, card1 card2):
  # There is an indentation error, the if cannot be at the same level as the def, as it is contained by it
  if card1.value > card2.value:
    # The name is wrong, there is no attribute only with the name card, it should be card1.
    return card
  else:
    return card2
  

 # There is an indentation error, the method is included inside the class, so it must have indentation.
def cards_total(self, cards):
  #  Total must have an initial value (total = 0)
  total
  for card in cards:
    total += card.value
    # I can only concatenate str to str, not  int (str(total))
    return "You have a total of" + total
  
```
