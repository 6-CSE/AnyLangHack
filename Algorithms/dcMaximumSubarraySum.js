/**
 * @param {Number[]} inputArray
 * @return {Number[]}
 */
export default function dcMaximumSubarraySum(inputArray) {
  /**
   * @param {number} elementIndex - the index of the element we're deciding to pick or not
   * @param {boolean} mustPick - to pick or not to pick the element
   * @returns {number} - maximum subarray sum that we'll get
   */
  function solveRecursively(elementIndex, mustPick) {
    if (elementIndex >= inputArray.length) {
      return mustPick ? 0 : -Infinity;
    }
    return Math.max(
      // Option #1: Pick the current element, and continue picking next one.
      inputArray[elementIndex] + solveRecursively(elementIndex + 1, true),
      // Option #2: Don't pick the current element.
      mustPick ? 0 : solveRecursively(elementIndex + 1, false),
    );
  }
  return solveRecursively(0, false);
}
