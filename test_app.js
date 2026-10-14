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
    body: { classList: { add: () => {}, remove: () => {}, toggle: () => {} } },
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
  console.log('Questions in database:', app.questions.length);
  console.log('Flashcards in database:', app.flashcards.length);
  
  app.startExam('parcial1');
  console.log('Primer Parcial questions count:', app.currentExam.questions.length);
  
  app.selectOption(0);
  app.nextQuestion();
  console.log('Current question index after next:', app.currentIndex);
  
  app.finishAttemptSummary();
  app.submitAttempt();
  console.log('Attempt submitted successfully!');
  
  app.showFlashcards();
  console.log('Flashcard rendered title:', document.getElementById('cardTitle').textContent);
`, context);
