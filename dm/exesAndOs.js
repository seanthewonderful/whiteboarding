// DESCRIPTION:
// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

// https://www.codewars.com/kata/55908aad6620c066bc00002a 

const xo = (str) => {
    let count = 0

    for (const letter in str) {
        if (letter.toLowerCase() === "x") {
            count += 1
        } 
        if (letter.toLowerCase() === "o") {
            count -= 1
        }
    }

    return count === 0
}

const arr1 = [1, 2, 3] 
const arr2 = ["Lea", "Kyle", "Scott"]

let newArr = []

for (let element of arr2) {
    newArr.push(element + " is great")
}

console.log(arr2)
console.log(newArr)




//  start val ; stop condition ; step
for (let i = arr2.length - 1; i >= 0; i --) {
    console.log(arr2[i])
}

