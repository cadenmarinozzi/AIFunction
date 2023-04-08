from modules.web.OpenAI.OpenAI import createCompletion
import subprocess, os, re

def runCode(codePath):
    try:
        output = subprocess.check_output(['python3', codePath], stderr=subprocess.STDOUT).decode('utf-8');

        return (output, False);
    except subprocess.CalledProcessError as e:
        err = e.output.decode('utf-8');

        return (err, True);

def installModule(module):
    try:
        subprocess.run(['python3', '-m', 'pip', 'install', module], stderr=subprocess.STDOUT);

        return True;
    except subprocess.CalledProcessError as e:
        return False;

def aiFunction(function, description, installPackages):
    if (not os.path.exists('functions')):
        os.mkdir('functions');

    functionPath = f'functions/{function}.py';

    if (not os.path.exists(functionPath)):
        code = createCompletion([
            {
                'content': 'You are an AI code generator. Generate ONLY the python code for the given function description, nothing else. The code should include just the function body, without the def statement, and should print just the output, without any other text. The code should take no user input, and should only have a single print statement.',
                'role': 'system'
            },
            {
                'content': 'Here is an example:\nFunction: time\nDescription: Returns the current time.\n\nfrom datetime import datetime\nnow = datetime.now();\ntime = now.strftime("%I:%M %p");\nprint(time);',
                'role': 'system'
            },
            {
                'content': f'Function: {function}\nDescription: {description}',
                'role': 'user'
            }
        ]);

        with open(functionPath, 'w') as functionFile:
            functionFile.write(code);

    # Run the code from the path. If there are errors, print them. Return the output
    (output, err) = runCode(functionPath);

    while (err):
        if ('ModuleNotFoundError' in output and installPackages):
            # Install the missing module
            module = re.search(r"ModuleNotFoundError: No module named '(.*)'", output).group(1);

            if (module == ''):
                break;

            print(f'Installing module: {module}');
            installed = installModule(module);

            if (not installed):
                return f'Error: Could not install module: {module}';

            (output, err) = runCode(functionPath);
        else:
            return '';

    return output;

print(aiFunction('time', 'Returns the current time.'));
