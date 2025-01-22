# InfoPlus

## Overview

InfoPlus is a Python-based utility designed to assist developers in compiling and running scripts efficiently on Windows platforms. The tool aims to enhance developer productivity by automating the compilation and execution process for different script types.

## Features

- **Platform Check**: Ensures that the program is running on a Windows platform.
- **Script Detection**: Identifies the type of script (Python, C, or Java) and performs necessary actions.
- **Compilation**: Automatically compiles C and Java scripts.
- **Execution**: Runs Python scripts, compiled C executables, and Java class files.
- **Error Handling**: Provides feedback on any errors encountered during compilation or execution.

## Requirements

- Windows OS
- Python 3.x
- GCC compiler for C scripts (MinGW recommended)
- Java JDK for Java scripts

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/infoplus.git
   ```
2. Navigate to the project directory:
   ```bash
   cd infoplus
   ```

## Usage

1. Run the program:
   ```bash
   python InfoPlus.py
   ```
2. Enter the path to your script when prompted.

## Supported Script Types

- **Python**: `.py`
- **C**: `.c` (requires GCC)
- **Java**: `.java` (requires Java JDK)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request.

## Contact

For any questions, please contact [your-email@example.com](mailto:your-email@example.com).