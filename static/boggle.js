console.log('javascript loaded')
$(async function () {

  const $gameForm = $('#board');
  const $guess = $('#guess');
  const $guessResult = $('#guessResult')
  const $scoreTracker = $('#scoreTracker')
  const $submitButton = $('#submitButton')
  const $highScoreTracker = $('#highScoreTracker')

  $gameForm.on("submit", async function(e){
    e.preventDefault();

    let userGuess = $guess.val()
    console.log(userGuess)
    let checkValidWord = await axios.post(`/guess`, {userGuess})
    console.log('here', checkValidWord.data.score)
    $guessResult.empty()
    $scoreTracker.empty()
    $guessResult.append(checkValidWord.data.response)
    $scoreTracker.append(checkValidWord.data.score)
    $highScoreTracker.append(checkValidWord.data.highscore)

    setTimeout(async function(){
      $submitButton.remove()
      $guess.remove()
      let highestScore = await axios.get(`/finished`)
      console.log(highestScore)
    }, 5000);
  })


});