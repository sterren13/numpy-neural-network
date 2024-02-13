from data import dataConvert
def convert():
    convert("data/train-images-idx3-ubyte", "data/train-labels-idx1-ubyte",
            "mnist_train.csv", 60000)
    convert("data/t10k-images-idx3-ubyte", "data/t10k-labels-idx1-ubyte",
            "mnist_test.csv", 10000)

def main():
    print("Hello World!")


if __name__ == '__main__':
    main()