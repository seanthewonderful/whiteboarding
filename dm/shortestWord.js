// Given a string of space-separated words, return the shortest word

function shortestWord(str) {
    let lengths = str.split(' ').map(word => word.length)
    return Math.min(...lengths)
}