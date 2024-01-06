// Given a positive integer, write a function that will return the sum of each digit of the integer.
// ex: sumDigits(9119) -> 9 + 1 + 1 + 9 -> 20

function sumDigits(num) {
    let digitArr = String(num).split('')
    let sum = 0
    for (digit of digitArr) {
        sum += +digit
    }
    return sum
}

console.log(sumDigits(9119))
