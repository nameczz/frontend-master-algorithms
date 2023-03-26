const binarySearch = (arr, target) => {
  let low = 0
  let high = arr.length
  while (low < high) {
    const mid = Math.floor(low + (high - low) / 2);
    const midVal = arr[mid]
    if (midVal === target) {
      return true
    }
    if (midVal < target) {
      low = mid + 1
    }
    if (midVal > target) {
      high = mid
    }
  }
  return false

}

module.exports = { binarySearch };