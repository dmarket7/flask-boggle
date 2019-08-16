console.log('javascript loaded')
$(async function () {

  const $gameForm = $('#board');
  const $guess = $('#guess');
  const $guessResult = $('#guessResult')

  $gameForm.on("submit", async function(e){
    e.preventDefault();

    let userGuess = $guess.val()
    console.log(userGuess)
    let checkValidWord = await axios.post(`/guess`, {userGuess})
    console.log(checkValidWord)
    $guessResult.empty()
    $guessResult.append(checkValidWord.data.response)
  })

});