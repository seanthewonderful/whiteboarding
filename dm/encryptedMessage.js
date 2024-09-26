/*
Write a function that prints an encrypted message.

Using this method, the message HOT SAUCE would look like this:

HTAC
OSUE
It’s a pretty simplistic method of encryption. All you do is split the letters of the initial message and alternate them over two rows of text, skipping any spaces. For example, the first letter goes in the first row, the second letter goes in the second row, the third letter goes in the first row, and so on…

Write a function that takes in a phrase and prints an encrypted version of that phrase using the method described above.

The phrase is guaranteed to only contain uppercase, alphabetic characters and spaces.
*/

const encryptedMessage = (phrase) => {
  let topLine = ""
  let botLine = ""

  phrase = phrase.split(' ').join()

  for (let i = 0; i < phrase.length; i++) {
    if (i % 2 === 0) {
      topLine
    }
  }
}

// mention your changes -> const arr = 
// 