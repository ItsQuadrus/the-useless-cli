# Commands
Here are all the commands that the CLI has. If you don't want to read this, just try `useless` in your terminal.

## Basic
### `useless`
Shows the help message. Pretty useful for a useless CLI.

### `useless about` or `useless info` or `useless version`
Shows information about the CLI and its author.


---

These are boring commands, right? Well, there are some more interesting ones.

---
## Random number generator
### `useless number`
Prints a random number between 0 and 100.

### `useless number <num>`
Prints a random number between 0 and the number you specified.

### `useless num <num1> <num2>`
Prints a random number between the two numbers you specified.

---

## Random word generator
### `useless word`
Prints a random word from a US dictionnary (requires an Internet connection)

### `useless word <number>`
Prints a random word with the length you specified.

---

## Random color generator
### `useless color (type)`
Types available:
- `useless color hex`
    -  Prints a random color in hexadecimal format.
- `useless color rgb`
    -  Prints a random color in RGB format.
- `useless color hsl`
    -  Prints a random color in HSL format.
- `useless color hsv`
    -  Prints a random color in HSV format.
- `useless color cmyk`
    -  Prints a random color in CMYK format.

## Random password generator
### `useless password`
Prints a random password with 16 characters (uses secrets module for security)

### `useless password <number>`
Prints a random password with the length you specified (MAX: 32)

---