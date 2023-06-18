const greeting = ["Good Morning", "Good Afternoon", "Good Evining"];

const currentHour = new Date().getHours();

function getIndex(hour) {
  if (hour >= 12 && hour < 17) {
    return 1;
  } else if (hour > 17 && hour < 24) {
    return 2;
  } else return 0;
}

const index = getIndex(currentHour);

console.log(greeting[index]);
