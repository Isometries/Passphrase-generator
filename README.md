# Passphrase Generator

  - A super simple passphrase generator in python. Uses the `secrets` module to produce a passphrase of random words chosen from a list of ~100k English words, taken from `/usr/share/dict/words` in Ubuntu.
  
  - You can generate a `wordss.txt` file from your own distro's dictionary by doing the following in the cloned project
  
    creating a blank `words.txt`
    
    - `rm words.txt`
    
    - `touch words.txt`
    
    Piping the `/usr/share/dict/words` directory into the new file
    
    - `cat /usr/share/dict/words > words.txt`1

  Only compatible with `python3.6`

# Example Usage

  - Sample input

  `python3 password_gen.py 20 25`

 - Sample output
   `welder
    bark's
    investitures`
