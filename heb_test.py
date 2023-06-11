import HebHTR

test = HebHTR('Screenshot(43).png')

test_text = test.imgToWord(iterations=5, decoder_type='word_beam')

print(test_text)