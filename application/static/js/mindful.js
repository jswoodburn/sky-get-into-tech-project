function togglePicture() {
  var img = document.getElementById("breathing");
  if (img.style.display === "none") {
  img.style.display = "block";
  } else {
  img.style.display = "none";
  }
 }
function trackTime() {
    if (img.style.display === "block") {
    var start = new Date();
    } else {
    var elapsed_ms = end_time - start_time;
    var seconds = Math.round(elapsed_ms / 1000);
    var minutes = Math.round(seconds / 60);
    var hours = Math.round(minutes / 60);

    var sec = TrimSecondsMinutes(seconds);
    var min = TrimSecondsMinutes(minutes);
    console.log(min, sec);
    }

}
function trackClick(){

}
function toggleAudio() {
  var audio = document.getElementById('audio');
        if (audio.paused) {
            audio.play();
            $('#play').removeClass('glyphicon-play-circle')
            $('#play').addClass('glyphicon-pause')
        }else{
            audio.pause();
            audio.currentTime = 0
            $('#play').addClass('glyphicon-play-circle')
            $('#play').removeClass('glyphicon-pause')
        }
    }
