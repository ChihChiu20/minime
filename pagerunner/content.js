var

var INTERNAL_SEC = 3;

function runUntil(fn, intervalSec, untilSec) {
  const intervalId = setInterval(() => {
    console.log('Running periodic function...');
    fn();
    console.log('Periodic function completed');
  }, intervalSec * 1000);
  setTimeout(function () {
    clearInterval(intervalId);
    console.log('Periodic function removed');
  }, untilSec * 1000);
}

function contains(str, subStr) {
  return str.indexOf(subStr) >= 0;
}

function isRoot() {
  return window.location.pathname === '/';
}

function runNextTask() {

}

function executeActionMain() {
  console.log('hello');
}

function main() {
  setInterval(executeActionMain, INTERNAL_SEC * 1000);
}

main();