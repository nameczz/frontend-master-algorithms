const twoCrystalBalls = (breaks) => {
  let low = 0;
  let high = breaks.length

  while (low < high) {
    const mid = Math.floor(low + Math.sqrt(high - low))
    const midVal = breaks[mid]
    if (midVal === true) {
      // first ball is broken, use the second one to find target
      for (let i = low; i < mid; i++) {
        if (breaks[i]) {
          return i
        }
      }
    }
    low = mid + 1
  }
  return -1
}

module.exports = { twoCrystalBalls };
