
function sum (args) { 
   let res = 0.0;
   for (let i of args) {
     res += i;
   }
   return res;
}

xs = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]

console.log("sum: %d", sum(xs))

