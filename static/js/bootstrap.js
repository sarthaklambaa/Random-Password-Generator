function copyPass() {
    const cb = navigator.clipboard;
    const password = document.querySelector('h2');
    cb.writeText(password.innerText).then(() => alert('Text copied'));
  }