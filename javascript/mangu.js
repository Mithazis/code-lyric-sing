// cara menjalankan 
// pastikan sudah install node
// buka terminal kemudian copas :

// node javascript/mangu.js



const lyrics = [
  { text: "", delayAfter: 100 },
  { text: "Jangan salahkan paham ku kini tertuju oh", delayAfter: 1100 },
  { text: "Siapa yang tau siapa yang mau", delayAfter: 1800 },
  { text: "Kau disana Aku diseberangmu", delayAfter: 1000 },
  { text: "", delayAfter: 100 },
  { text: "Cerita kita sulit di cerna", delayAfter: 1400 },
  { text: "Tak lagi sama cara berdoa", delayAfter: 1700 },
  { text: "Cerita kita sulit diterka", delayAfter: 1400 },
  { text: "Tak lagi sama arah kiblatnya oh", delayAfter: 950 },
  { text: "", delayAfter: 1 },
  { text: "Cerita kita sulit di cerna", delayAfter: 1300 },
  { text: "Tak lagi sama cara berdoa", delayAfter: 1700 },
  { text: "Cerita kita sulit diterka", delayAfter: 1300 },
  { text: "Tak lagi sama arah kiblatnya", delayAfter: 2000 }
];

// Default delay
const defaultLetterDelay = 60;
const slowWordLetterDelay = 120;

// Delay antar kata
const defaultWordPause = 80;

// Delay khusus per huruf (misal untuk frasa lebih lambat)
const slowWords = ["kini","tertuju","tau","mau","aku", "diseberangmu","kita","berdoa","arah", "kiblatnya"];

// Delay tambahan setelah kata (opsional, untuk tekanan musik)
const wordDelayOverride = {
  "salahkan": 500,
  "paham": 1000,
  "kini": 1500,
  "tertuju": 2150,
  "tau": 1300,
  "disana": 1250,
  "kita": 1500,
  "sama": 1500,
  "diterka": 500
};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Cek apakah kata termasuk slowWord
function getLetterDelay(word) {
  const clean = word.toLowerCase().replace(/[^a-z]/g, "");
  return slowWords.includes(clean) ? slowWordLetterDelay : defaultLetterDelay;
}

async function typewriter(text) {
  const words = text.split(" ");

  for (const word of words) {
    const letterDelay = getLetterDelay(word);
    const clean = word.toLowerCase().replace(/[^a-z]/g, "");

    for (const char of word) {
      process.stdout.write(char);
      await sleep(letterDelay);
    }

    process.stdout.write(" ");

    const wordDelay = wordDelayOverride[clean] || defaultWordPause;
    await sleep(wordDelay);
  }

  process.stdout.write("\n");
}

async function runLyrics() {
  for (const line of lyrics) {
    await typewriter(line.text);
    await sleep(line.delayAfter);
  }

  console.log("\n🎭 Boleh Request:)");
}

runLyrics();