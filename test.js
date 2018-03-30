const one = ['a', 'b', 'c']
const two = ['d', 'e', 'f']
const three = ['g', 'h', 'i']
// Old way #1
// const result = one.concat(two, three)
// Old way #2
// const result = [].concat(one, two, three)
// New
const result = [...one, ...two, ...three]



console.log(result)