//coding Interview Question #1

const nums = [2, 7, 11, 15];
const target = 9;

function solution(nums, target) {
  let map = new Map();

  for (let i = 0; i < nums.length; i++) {
    let compliment = target - nums[i];

    if (map.has(compliment)) {
      return [i, map.get(compliment)];
    } else {
      map.set(nums[i], i);
    }
  }
}

console.log("numbers: ", nums, " and the target is: ", target);
console.log("indeces of the numbers: ", solution(nums, target));
