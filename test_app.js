const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('DISM_Examen/index.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);

const elements = {};
function getEl(id) {
  if (!elements[id]) {
    elements[id] = {
      classList: { add: () => {}, remove: () => {}, toggle: () => {} },
      style: {},
      textContent: '',
      innerHTML: '',
      appendChild: () => {}
    };
  }
  return elements[id];
}

const context = {
  document: {
    addEventListener: () => {},
    body: { classList: { add: () => {}, remove: () => {}, toggle: () => {}, contains: () => false } },
    getElementById: getEl,
    querySelectorAll: () => [],
    createElement: (tag) => ({
      classList: { add: () => {}, remove: () => {} },
      style: {},
      innerHTML: '',
      appendChild: () => {},
      textContent: ''
    })
  },
  localStorage: { getItem: () => null, setItem: () => {} },
  window: { scrollTo: () => {} },
  Set: Set,
  setInterval: () => 1,
  clearInterval: () => {},
  console: console
};

vm.createContext(context);
vm.runInContext(scriptMatch[1], context);

vm.runInContext(`
  app.init();
  console.log('Total bank questions:', app.questions.length);
  app.startExam('global');
  console.log('Global exam questions:', app.currentExam.questions.length);
  app.startExam(1);
  console.log('Tema 1 exam questions:', app.currentExam.questions.length);
  app.startExam(2);
  console.log('Tema 2 exam questions:', app.currentExam.questions.length);
  app.startExam(3);
  console.log('Tema 3 exam questions:', app.currentExam.questions.length);
  app.startExam(4);
  console.log('Tema 4 exam questions:', app.currentExam.questions.length);
  app.startCalculationsOnly();
  console.log('Calculations mode questions:', app.currentExam.questions.length);
`, context);
