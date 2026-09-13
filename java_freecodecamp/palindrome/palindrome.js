const word = document.getElementById("text-input")
const button = document.getElementById("check-btn")
const result = document.getElementById("result")
result.style.display = "none"

function cleanInputString(str) {
  const regex = /[^a-zA-Z0-9]/g;
  const new_word = str.replace(regex, '');
  return new_word.toLowerCase()
}


function check_palindrome(word){

    let is_palindrome = false
    const clean = cleanInputString(word)
    clean.toLowerCase()
    const chars = clean.split("")
    chars.reverse()
    const inverse = chars.join("")

    if (clean === inverse){
        is_palindrome = true
    } else{
        is_palindrome = false
    }

    if (is_palindrome){
        result.innerText = word + " is a palindrome."
    
    } else {
        result.innerText = word + " is not a palindrome."
        
    }
    
    result.style.display = "block"
    return 
}

button.addEventListener("click", ()=>{
    if (word.value===""){
        alert("Please input a value")
    } else{
    check_palindrome(word.value)
    }
})

