// Javascript Built-in Higher order functions -> map, reduce and filter
// Using Higher Order Function - Map

const numberArray = [1, 2, 3, 4, 5];
const numberArrayTens = numberArray.map((x) => x * 10);

console.log("Array von Nummernd: ", numberArrayTens);

// let's create our own Higher Order Function
const namesArray = ["Aron", "Serin", "Mahmoud"];

function mapReplica(array, func) {
  const nameArrayList = [];

  for (let i = 0; i < array.length; i++) {
    nameArrayList.push(func(array[i]));
  }

  return nameArrayList;
}

const namesArrayDoubleLength = mapReplica(namesArray, function (item) {
  return item.length;
});

console.log("Laenge von Namen in Array: ", namesArrayDoubleLength);
