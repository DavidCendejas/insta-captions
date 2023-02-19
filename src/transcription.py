import sys
# from deepspeech import Model, version

def main():
    if len(sys.argv) == 1:
        print('At least 1 file must be inputed.\n\nUsage: "./transcription.py filename1 filename2 ...')
    for audiofile in sys.argv:
        print('test') 

if __name__ == '__main__':
    main()