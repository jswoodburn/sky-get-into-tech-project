function togglePicture() {
  var img = document.getElementById("breathing");
  if (img.style.display === "none") {
  img.style.display = "block";
  } else {
  img.style.display = "none";
  }
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
