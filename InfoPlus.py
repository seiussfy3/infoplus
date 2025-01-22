import os
import subprocess
import platform

class InfoPlus:
    def __init__(self, script_path):
        self.script_path = script_path
        self.check_platform()

    def check_platform(self):
        if platform.system() != 'Windows':
            raise EnvironmentError("InfoPlus is designed to run on Windows platforms only.")
        print("Platform check passed: Running on Windows.")

    def compile_script(self):
        if self.script_path.endswith('.py'):
            print("Python script detected, no compilation required.")
            return True
        elif self.script_path.endswith('.c'):
            print("C script detected, compiling...")
            compile_command = f"gcc {self.script_path} -o {self.script_path[:-2]}.exe"
            return self.run_command(compile_command)
        elif self.script_path.endswith('.java'):
            print("Java script detected, compiling...")
            compile_command = f"javac {self.script_path}"
            return self.run_command(compile_command)
        else:
            print("Unsupported script type for compilation.")
            return False

    def run_script(self):
        if self.script_path.endswith('.py'):
            print("Running Python script...")
            run_command = f"python {self.script_path}"
        elif self.script_path.endswith('.exe'):
            print("Running executable...")
            run_command = self.script_path
        elif self.script_path.endswith('.class'):
            print("Running Java class...")
            script_name = os.path.splitext(os.path.basename(self.script_path))[0]
            run_command = f"java {script_name}"
        else:
            print("Unsupported script type for execution.")
            return False

        return self.run_command(run_command)

    def run_command(self, command):
        try:
            subprocess.run(command, check=True, shell=True)
            print(f"Command executed successfully: {command}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {command}")
            print(e)
            return False

    def assist(self):
        if self.compile_script():
            self.run_script()

if __name__ == "__main__":
    script_path = input("Enter the path to your script: ")
    infoplus = InfoPlus(script_path)
    infoplus.assist()