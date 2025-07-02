// cara menjalankan 
// pastikan sudah install node
// buka terminal kemudian copas :

// node javascript/Die-with-a-smile.js



const lyrics = [
  {
    text: "",
    delayAfter: 1
  },
    {
    text: "Wherever you go, that's where I'll follow",
    delayAfter: 1700
  },
  {
    text: "Nobody 's promised tomorrow",
    delayAfter: 1500
  },
  {
    text: "So I'ma love you every night like it's the last night",
    delayAfter: 700
  },
  {
    text: "Like it's the last night",
    delayAfter: 900
  },
  {
    text: "",
    delayAfter: 100
  },
  {
    text: "If the world was ending I'd wanna be next to you",
    delayAfter: 3000
  },
  {
    text: "If the party was over and our time on Earth was through",
    delayAfter: 3150
  },
  {
    text: "I'd wanna hold you just for a while",
    delayAfter: 1900
  },
  {
    text: "And die with a smile",
    delayAfter: 1300
  },
  {
    text: "If the world was ending I'd wanna be next to you",
    delayAfter: 3000
  }
];

// Delay default antar huruf
const defaultLetterDelay = 60;

// Delay khusus per kata (opsional)
const wordDelayOverride = {
  "nobody": 400,
  "next": 1000,
  "party" : 500,
  "over" : 1100,
  "earth": 900,
  "hold you" : 1000,
  "die" : 1600,
  "world":400,
  "ending":500
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function typewriter(text) {
  const words = text.split(" ");

  for (const word of words) {
    for (const char of word) {
      process.stdout.write(char);
      await sleep(defaultLetterDelay);
    }
    process.stdout.write(" ");
    const delayAfterWord = wordDelayOverride[word.replace(/[^a-zA-Z]/g, "").toLowerCase()] || 100;
    await sleep(delayAfterWord);
  }
  process.stdout.write("\n");
}

// Menjalankan semua baris
async function runLyrics() {
  for (const line of lyrics) {
    await typewriter(line.text);
    await sleep(line.delayAfter);
  }

  console.log("\n🎭 Thank You:)");
}

runLyrics();
