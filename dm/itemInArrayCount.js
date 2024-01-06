// Write a function that takes in an item and an array. Return the number of times the given item appears in the array.

function itemInArrayCount(arr, item) {
    let count = 0
    for (element of arr) {
        if (element === item) {
            count ++
        }
    }
    return count
}


let arr1 = [1,2,3,4,4,5,4,7,1,3,5]

// console.log(itemInArrayCount(arr1, 5))

let o1 = { one: 1, two: 2 }
let o2 = { one: 1, two: 2 }
let o3 = o1

console.log(o1 === o2)
console.log(o1 == o2)
console.log(o3 === o1)
console.log(o3 == o1)
console.log(o3 === o2)
console.log(o3 == o2)

