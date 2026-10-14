const fs = require('fs');
const path = require('path');
const vm = require('vm');

const htmlFiles = [
  { file: 'DISM_Examen/test_dam_tema2.html', tema: 2 },
  { file: 'DISM_Examen/quiz_tema3.1.html', tema: 3 },
  { file: 'DISM_Examen/quiz_tema3.2_infraestructura_telefonia.html', tema: 3 },
  { file: 'DISM_Examen/quiz_tema3.3_arquitectura_procesadores.html', tema: 3 },
  { file: 'DISM_Examen/quiz_iot_tema4.html', tema: 4 }
];

const allExtracted = [];

for (const { file, tema } of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');
  const m = content.match(/(?:const|let|var)\s+(questions|QUESTIONS)\s*=\s*(\[[\s\S]*?\]);\s*(?:\r?\n|let|const|var|function)/);
  if (!m) {
    console.error('Not found in', file);
    continue;
  }
  const sandbox = {};
  vm.createContext(sandbox);
  vm.runInContext('result = ' + m[2], sandbox);
  const arr = sandbox.result;
  console.log(`${file}: found ${arr.length} questions`);

  for (const item of arr) {
    // Standardize keys: q, options, correct, explanation
    let q = item.q || item.question;
    let options = item.options || item.opts || item.o;
    let correct = item.correct !== undefined ? item.correct : item.a;
    let exp = item.explanation || item.exp || '';

    allExtracted.push({
      tema: tema,
      source: path.basename(file),
      q: q.trim(),
      options: options.map(o => String(o).trim()),
      correct: correct,
      explanation: exp
    });
  }
}

console.log(`Total extracted from HTMLs: ${allExtracted.length}`);
fs.writeFileSync('DISM_Examen/html_questions.json', JSON.stringify(allExtracted, null, 2), 'utf8');
