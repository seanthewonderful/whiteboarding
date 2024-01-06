// Write a function that takes in a string and returns a string with all vowels replaced with *

function replaceVowels(str) {
    let returnStr = ""
    let vowels = ["a", "e", "i", "o", "u"]

    for (i = 0; i < str.length; i++) {
        if (vowels.includes(str[i].toLowerCase())) {
            returnStr += "*"
        } else {
            returnStr += str[i]
        }
    }

    return returnStr
}

