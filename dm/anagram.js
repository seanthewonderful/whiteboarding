function isAnagram(str1, str2) {
  if (str1.length !== str2.length) {
    return false
  }
  // return str1.toLowerCase().split('').sort().join('') === str2.toLowerCase().split('').sort().join('')

  let obj1 = {}
  let obj2 = {}
  str1 = str1.toLowerCase()
  str2 = str2.toLowerCase()

  for (let i = 0; i < str1.length; i++) {
    obj1[str1[i]] = (obj1[str1[i]] || 0) + 1
    obj2[str2[i]] = (obj2[str2[i]] || 0) + 1
  }

  // return Object.keys(obj1).every(key => obj1[key] === obj2[key])

  for (let key in obj1) {
    if (obj1[key] !== obj2[key]) {
      return false
    }
  }
  return true

}

console.log(isAnagram('listen', 'Silent'))
console.log(isAnagram('moon', 'noom'))
console.log(isAnagram('bat', 'batt'))
