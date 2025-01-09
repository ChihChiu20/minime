var TASKMANAGER_ADDRESS = 'localhost:5000';

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

function httpGet(theUrl) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, false); // false for synchronous request
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

function runNextTask() {
  var task = JSON.parse(httpGet(`http://${TASKMANAGER_ADDRESS}/pop_next_task`));
  if (task.id === -1) {
    return;
  }

  console.log(task);
}

function executeActionMain() {
  console.log('hello');
}

function main() {
  console.log('WELCOME');
  setInterval(executeActionMain, INTERNAL_SEC * 1000);
}

main();
console.log('what going on?');