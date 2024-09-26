const largestSmaller = (nums, num) => {
    let max = null
    let min = nums[0]
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < min) {
            min = nums[i]
        }
    }

    console.log("min: ", min)

    if (min < num) {
        max = min
    } else {
        return null
    }
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > max && nums[i] < num) {
            max = nums[i]
        }
    }

    return max
}

console.log(largestSmaller([300, 3, 5, 70], 100))