const fs = require('fs');
const path = require('path');
const vm = require('vm');

const htmlFiles = [
  'DISM_Examen/quiz_iot_tema4.html',
  'DISM_Examen/quiz_tema3.1.html',
  'DISM_Examen/quiz_tema3.2_infraestructura_telefonia.html',
  'DISM_Examen/quiz_tema3.3_arquitectura_procesadores.html',
  'DISM_Examen/test_dam_tema2.html'
];

for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');
  // Match the array assignment
  // e.g. const questions = [...]; or const QUESTIONS = [...];
  const m = content.match(/(?:const|let|var)\s+(questions|QUESTIONS)\s*=\s*(\[[\s\S]*?\]);\s*(?:\r?\n|let|const|var|function)/);
  if (m) {
    const sandbox = {};
    vm.createContext(sandbox);
    vm.runInContext('result = ' + m[2], sandbox);
    console.log(`File: ${file} => Count: ${sandbox.result.length}`);
    if (sandbox.result.length > 0) {
      console.log('Sample keys:', Object.keys(sandbox.result[0]));
      console.log('Sample question:', sandbox.result[0]);
    }
  } else {
    console.log(`Could not find array in ${file}`);
  }
}
