num1 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12];

num2 = [11, 22, 33, 44, 55, 66, 88, 99];

num3 = [6, 7, 8, 9, 11, 12, 15, 16, 17];
num4 = [3, 6, 2, 9, 11, 4, 7, 12, 15];

function findMissing(numbers) {
  //using total sum formula of arthimetic sequences
  //for any sorted first n natural numbers
  let last = numbers[numbers.length - 1];
  sum = (last * (last + 1)) / 2;
  let total = 0;
  for (let i = 0; i < numbers.length; i++) {
    total += numbers[i];
  }
  console.log(sum - total);
}

function findMissing2(numbers) {
  //using the general formula of arthimetic sequence
  //for any sorted arthimetic sequence
  let first = numbers[0],
    diff = numbers[1] - numbers[0];
  for (let i = 0; i < numbers.length; i++) {
    let num = first + diff * i;
    if (numbers[i] !== num) return num;
  }
}

function findMissing3(numbers) {
  //use the difference between the index and the numbers
  //can be used for arthimetic sequences and is able to detect multiple missing numbers
  let diff = numbers[0] - 0;
  let missing = [];
  for (let i = 1; i < numbers.length; i++) {
    if (diff !== numbers[i] - i) {
      while (diff < numbers[i] - i) {
        missing.push(diff + i);
        diff++;
      }
    }
  }
  return missing;
}

function findMissing4(numbers) {
  // for unsorted first n natural numbers
  // has O(n) space complexity
  let bitmap = [],
    missing = [];
  for (let i = 0; i < numbers.length; i++) {
    bitmap[numbers[i]] = 1;
  }

  for (let i = 1; i < bitmap.length; i++) {
    if (bitmap[i] !== 1) missing.push(i);
  }
  return missing;
}

// findMissing(num3);

// console.log(findMissing2(num3));

// console.log(findMissing3(num3));

// console.log(findMissing4(num4));

arr1 = [3, 6, 2, 2, 2, 5, 4, 1, 7, 7];

function findDuplicate(numbers) {
  for (let i = 0; i < numbers.length - 1; i++) {
    if (numbers[i] == numbers[i + 1]) {
      console.log(numbers[i] + " is duplicated");
    }
  }
}

function findDuplicate2(numbers) {
  for (let i = 0; i < numbers.length - 1; i++) {
    if (numbers[i] == numbers[i + 1]) {
      let j = i + 1;
      while++++ (numbers[j] == numbers[i]) j++;
      console.log(numbers[i] + " appeared " + (j - i) + " times");
      i = j - 1;
    }
  }
}

function findDuplicate3(numbers) {
  //for unsorted array we can use nested for loops with a counter to search for duplicates
}
// findDuplicate2(arr1);

//finding equilibrum

function findEquilibrum(numbers) {
  //this doesn't work come up with another solution
  let left = 0,
    right = numbers.length - 1;
  let leftTotal = numbers[left],
    rightTotal = numbers[right];
  while (left < right) {
    if (leftTotal == rightTotal) {
      return right - left + 1;
    }
    if (leftTotal < rightTotal) {
      leftTotal += numbers[++left];
    } else {
      rightTotal += numbers[--right];
    }
    console.log(leftTotal + " " + rightTotal);
  }
  return -1;
}

//console.log(findEquilibrum([1, 5, 3, 1, 1, 1, 1, 1, 1]));

const findSum = (arr, value) => {
  //to avoid redundence result we can use bitmaps or hashtables but they donot work for negative numbers
  let ans = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] == value) {
        ans.push([arr[i], arr[j]]);
      }
    }
  }
  return ans;
};

const findSum2 = (arr, value) => {
  //we can use two pointers for sorted array which is more efficient
  let low = 0,
    high = arr.length - 1,
    ans = [];
  while (low < high) {
    if (arr[low] + arr[high] == value) {
      ans.push([arr[low++], arr[high--]]);
    } else if (arr[low] + arr[high] < value) {
      low++;
    } else high--;
  }
  return ans;
};

//console.log(findSum2([1, 3, 4, 6, 7, 8, 9, 10], 10));

function signFilter(arr) {
  let front = 0,
    back = arr.length - 1;
  while (front < back) {
    if (arr[front] < 0) front++;
    if (arr[back] > 0) back--;
    else if (arr[front] > 0 && arr[back] < 0) {
      let temp = arr[front];
      arr[front] = arr[back];
      arr[back] = temp;
      front++;
      back--;
    }
  }
  return arr;
}

let array = [3, -1, 5, 8, -22, 4, 7, -1, -4, -7, 6];

//console.log(signFilter(array));

//leaders in array GFG

const leaders = (array) => {
  let leader = array[array.length - 1],
    arr = [leader];
  for (let i = array.length - 1; i >= 0; i--) {
    if (array[i] >= leader) {
      leader = array[i];
      arr.push(leader);
    }
  }
  return arr.reverse();
};

//console.log(leaders([16, 17, 4, 3, 5, 2]));

//count morethan n/k occurence GFG

const countOccur = (arr, k) => {
  let n = arr.length,
    m = n / k,
    counted = 0;
  for (let i = 0; i < n; i++) {
    let occur = 0;
    for (let j = 0; j < n; j++) {
      if (arr[j] == arr[i]) occur++;
    }
    console.log(occur);
    if (occur > m) {
      counted++;
    }
  }
  return counted;
};

//learn the moose algorithm  and do it for the second time
console.log(countOccur([3, 1, 2, 2, 1, 2, 3, 3], 4));
