def rotate_word(s, i):
## Iterate each character in string "s"
  for ch in s:
## Rotating each ch by given value i
    r_ch = ord(ch) + i
## Priting the output
    print(f"{ch} = {chr(r_ch)}, ({i})")
