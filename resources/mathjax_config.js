window.MathJax = {
  startup: {
    pageReady: function () {
      return MathJax.startup.defaultPageReady();
    }
  },
  tex: {
    inlineMath: [['$', '$'], ["\\(", "\\)"]],
    displayMath: [['$$', '$$'], ["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

var script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
script.setAttribute('id', 'MathJax-script');
document.head.appendChild(script);