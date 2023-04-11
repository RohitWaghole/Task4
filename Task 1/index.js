var i = 0;

function SimpleToAdvance() {
  i = 1;
  document.getElementById("container").style.display = "none";
  document.getElementById("container2").style.display = "inline-block";
}

function AdvanceToSimple() {
  i = 0;
  document.getElementById("container").style.display = "inline-block";
  document.getElementById("container2").style.display = "none";
}

var flag = 0;

let buttons = document.getElementsByClassName("button");
Array.from(buttons).forEach((button) => {
  button.addEventListener("click", function (e) {
    try {
      if (flag) {
        flag = 0;
        document.getElementsByClassName("simpleInput")[i].value = "";
      }
      let symbol = e.target.innerHTML;
      if (symbol == "=") {
        document.getElementsByClassName("simpleInput")[i].value = eval(
          document.getElementsByClassName("simpleInput")[i].value
        );
      } else if (symbol == "x") {
        symbol = "*";
        document.getElementsByClassName("simpleInput")[i].value += symbol;
      } else if (symbol == "C") {
        document.getElementsByClassName("simpleInput")[i].value = "";
      } else if (symbol == "√") {
        document.getElementsByClassName("simpleInput")[i].value += "Math.sqrt(";
      } else if (symbol == "ln") {
        document.getElementsByClassName("simpleInput")[i].value += "Math.log(";
      } else if (symbol == "log") {
        document.getElementsByClassName("simpleInput")[i].value +=
          "Math.log10(";
      } else if (symbol == "π") {
        document.getElementsByClassName("simpleInput")[i].value += "Math.PI";
      } else if (symbol == "x<sup>2</sup>") {
        document.getElementsByClassName("simpleInput")[i].value +=
          "Math.pow(,2)";
      } else if (symbol == "x<sup>y</sup>") {
        document.getElementsByClassName("simpleInput")[i].value +=
          "Math.pow(,)";
      } else if (symbol == "sin" || symbol == "cos" || symbol == "tan") {
        document.getElementsByClassName("simpleInput")[i].value +=
          "Math." + symbol + "(";
      } else if (symbol == "1/x") {
        document.getElementsByClassName("simpleInput")[i].value += "(1/";
      } else if (symbol == "e") {
        document.getElementsByClassName("simpleInput")[i].value += "Math.E";
      } else if (symbol == "|x|") {
        document.getElementsByClassName("simpleInput")[i].value += "Math.abs(";
      } else if (symbol == "") {
        let str = document.getElementsByClassName("simpleInput")[i].value;
        if (str.length == 1) {
          str = "";
        } else {
          str = str.slice(0, str.length - 1);
        }
        document.getElementsByClassName("simpleInput")[i].value = str;
      } else if (symbol == "e<sup>x</sup>") {
        document.getElementsByClassName("simpleInput")[i].value += "Math.exp(";
      } else {
        document.getElementsByClassName("simpleInput")[i].value += symbol;
      }
    } catch {
      flag = 1;
      document.getElementsByClassName("simpleInput")[i].value = "Syntax Error";
    }
  });
});
