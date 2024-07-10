import subprocess
import os

def convert(input_file, output_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    c_executable = os.path.join(script_dir, 'c_src', 'camp2ascii')
    result = subprocess.run([c_executable, input_file, '-o', output_file], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Conversion failed: {result.stderr}")
    print(result.stdout)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convert Campbell Scientific binary files to ASCII.')
    parser.add_argument('input_file', help='The input binary file')
    parser.add_argument('output_file', help='The output ASCII file')
    args = parser.parse_args()
    convert(args.input_file, args.output_file)
