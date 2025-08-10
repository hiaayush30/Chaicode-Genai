class Tokenizer {
   encode = (text) => {
     const arr = text.split("")
     const tokens = []
     arr.map(char=>{
       tokens.push(char)
     })
     return tokens
   }
}


const tokenizer = new Tokenizer();

console.log(tokenizer.encode("Hello"))