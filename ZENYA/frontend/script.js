document.addEventListener("DOMContentLoaded", () => {
  const startBtn = document.getElementById("start-btn");
  const bgMusic = document.getElementById("bg-music");
  const botImage = document.getElementById("bot");

  // 🎵 Start background music on button click
  startBtn.addEventListener("click", () => {
    bgMusic.volume = 0.3; // soft background
    bgMusic.play();
    speak("Hello, I’m Zenya. How are you feeling today?");
  });

  // 🗣️ Text-to-Speech with soothing female voice
  function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.voice = speechSynthesis
      .getVoices()
      .find(v => v.name.toLowerCase().includes("female") || v.lang === "en-US");
    utterance.pitch = 1;
    utterance.rate = 0.9;
    utterance.volume = 1;

    botImage.src = "assets/bot_talk.gif";

    utterance.onend = () => {
      botImage.src = "assets/bot_idle.gif";
    };

    speechSynthesis.speak(utterance);
  }
});

