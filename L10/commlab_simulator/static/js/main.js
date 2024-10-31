const output = document.getElementById("output");
const code = document.getElementById("code");
const cons = document.getElementById("console");
const header = "import sys, asyncio\nsys.path.insert(2,'.')\n";

function addToOutput(s) {
    cons.value += s + "\n";
    cons.focus();
}

addToOutput("Initializing...");
if (window.location.protocol == 'file:') {
    alert("You need to run a web server to use this tool.\n" +
          "Run this command from this folder in a terminal:\n" +
          "python -m http.server --bind localhost \n" +
          "Then open http://localhost:8000/ in your browser.")
}

function saveFile() {
    window.open('data:text/x-python;charset=utf-8,' +
        encodeURIComponent(code.value)
    );
}

function flagNoise() {
    if (document.getElementById("flag1").innerHTML == "NOISE") {
        document.getElementById("flag1").innerHTML = "";
    } else {
        document.getElementById("flag1").innerHTML = "NOISE";
    }
    if (document.getElementById("flag1").innerHTML == "NOISE") {
        document.getElementById("noise").innerHTML = "Noise Off";
    } else {
        document.getElementById("noise").innerHTML = "Noise On";
    }
}

async function main() {
    let pyodide = await loadPyodide({
        stdout: addToOutput
    });

    output.value += "Ready!\n";
    return pyodide;
}
let pyodideReadyPromise = main().then(value => {
    ubit_ui.init();
    return value;
});

document.getElementById("halt").disabled = true;
function flagHalt() {
    document.getElementById("flag").innerHTML = "STOP";
}

function handleFileSelect(evt) {
    var files = evt.target.files;
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
        fparts = f.name.split('.');
        ext = fparts[fparts.length - 1];
        if (!ext.match('py')) {
            continue;
        }
        var reader = new FileReader();
        reader.onload = (function(theFile) {
            return function(e) {
                code.value = e.target.result;
            };
        })(f);
        reader.readAsText(f);
    }
}
document.getElementById('files').addEventListener('change', handleFileSelect, false);

async function evaluatePython() {
    document.getElementById("run").disabled = true;
    document.getElementById("halt").disabled = false;
    let imports = ["lib/microbit.py", "lib/machine.py", "lib/radio.py", "lib/utime.py"];
    let pyodide = await pyodideReadyPromise;
    for (let z of imports) {
        q = z.split('/');
        x = q[q.length - 1];
        await pyodide.runPythonAsync(`
            from pyodide.http import pyfetch
            response = await pyfetch("${z}", cache="no-store")
            if response.status == 200:
                with open("${x}", "wb") as f:
                    f.write(await response.bytes())
        `)
    }
    try {
        addToOutput("");
        let result = await pyodide.runPythonAsync(header + code.value);
        if (typeof result !== 'undefined') {
            addToOutput(">>>"+result);
        }
    } catch (err) {
        addToOutput(err);
    }
    document.getElementById("run").disabled = false;
    document.getElementById("halt").disabled = true;
    document.getElementById("flag").innerHTML = "";
    
}