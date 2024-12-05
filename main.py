def result(txt, slvd):
  # I forgot how I made this. Best of luck
  result = ''
  for i in range(len(txt)):
    letter = txt[i]
    if letter in alphabet:
      for index in range(len(slvd)):
        if letter == slvd[index][0]:
            result = result + slvd[index][1]
        else:
          continue
    else:
      result = result + letter
  return result

def caesar_decode(txt, shift):
  bclst = txt.split()
  slvd = []
  found = ''
  for item in bclst:
  # Breaks bclst into individual items

    for letter in item:
    # Breaks the items into their letters

      if letter in alphabet:
      # Checks to make sure that letter isn't a symbol
        
        # Finds the index to the letter then shifts it by the shift value
        x = alphabet.index(letter)
        x += shift
        if x > 25:
        # Cycles the alphabet if the shift value is over 25
          x -= 26
        if letter in found:
        # Skips letter that have already been found
          continue
        else:
        # Adds letters that haven't been found
          slvd.append([letter, alphabet[x]])
          found = found + letter

  # Returns the answer using the Result function to return a string
  return result(txt, slvd)

def caesar_encode(txt, shift):
  bclst = txt.split()
  slvd = []
  found = ''
  for item in bclst:
    # Takes item in bclst to solve
    for letter in item:
      # Splits each letter in the word up to solve
      if letter in alphabet:
        # Checks to make sure that the letter isn't a symbol or space
        # Else clause not needed since I'm just solving for the letters
        # in the words and not maintaining the txt.
        # The Result function takes care of that for me
        x = alphabet.index(letter)
        x -= shift
        if x > 25:
          # Shifts the alphabet if it goes over
          x -= 26
        if letter in found:
          # Skips what has already been solved for
          continue
        else:
          # Adds new valve
          slvd.append([letter, alphabet[x]])
          found = found + letter

  # Returns the answer using Result function to give a string
  return result(txt, slvd)

def manual_brute_force(txt):
  # A simple way to solve the problem
  shift = 1
  while True:
    result = caesar_decode(txt, shift)
    print(result)
    user_input = input('Decoded? (y or n): ')
    if user_input == 'y':
      return result, shift
    else:
      shift += 1
      continue

def vig_decode(txt, keyword):
  # Start - Replace txt letter values with keyword values
  de_vals = ''
  keyword_index = 0
  for letter in txt:
    if letter in alphabet:
      if keyword_index < len(keyword):
        de_vals = de_vals + keyword[keyword_index]
        keyword_index += 1
      else:
        keyword_index = 0
        de_vals = de_vals + keyword[keyword_index]
        keyword_index += 1
    else:
      de_vals = de_vals + letter
  # End
  # Start - Decript values
  decoded = ''
  lst_de_vals = [x for x in de_vals]
  index = 0
  for letter in txt:
    if letter in alphabet:
      shift = alphabet.index(lst_de_vals[index])
      decoded = decoded + caesar_decode(letter, shift)
    else:
      decoded = decoded + letter
    index += 1
  return decoded

def vig_encode(txt, keyword):
  # Start - Replace txt letter values with keyword values
  en_vals = ''
  keyword_index = 0
  for letter in txt:
    if letter in alphabet:
      if keyword_index < len(keyword):
        en_vals = en_vals + keyword[keyword_index]
        keyword_index += 1
      else:
        keyword_index = 0
        en_vals = en_vals + keyword[keyword_index]
        keyword_index += 1
    else:
      en_vals = en_vals + letter
  # End
  # Start - Encript keyword values
  encoded = ''
  lst_en_vals = [x for x in en_vals]
  index = 0
  for letter in txt:
    if letter in alphabet:
      shift = alphabet.index(lst_en_vals[index])
      encoded = encoded + caesar_encode(letter, shift)
    else:
      encoded = encoded + letter
    index += 1
  # End
  return encoded

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


first_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
first_message_decoded = caesar_decode(first_message, 10)
second_message_encoded = caesar_encode('I did it and I\'m happy about it.', 10)

third_messaage = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
third_messaage_decoded = caesar_decode(third_messaage, 10)
print(third_messaage_decoded)

fourth_message = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'
fourth_message_decoded = caesar_decode(fourth_message, 14)
print(fourth_message_decoded)

fifth_message = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
fifth_message_decoded, shift = manual_brute_force(fifth_message)
print(fifth_message_decoded)

sixth_message_encoded = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!'
answer = vig_decode(sixth_message_encoded, 'friends')
print(answer)