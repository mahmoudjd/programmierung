function sum (args) { 
   let summ = 0.0;
   for (let i of args) {
     summ += i;
   }
   return summ;
}

x = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]

console.log(sum(x))

