// Given an array of numbers, return the sum of the 2 smallest numbers in the array
// ex: 
// [25, 5, 16, 7, 90] --> 12

function sumTwoSmallestNumbers(numbers){  
    numbers = numbers.sort((a, b) => a - b)
    return numbers[0] + numbers[1]
  };