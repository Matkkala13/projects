
function cleanInputString(str) {
  const regex = /[^a-zA-Z0-9]/g;
  const new_word = str.replace(regex, '');
  return new_word.toLowerCase()
}
let test = cleanInputString("1 eye for of 1 eye.")
console.log(test)
