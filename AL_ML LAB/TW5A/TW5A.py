# Inputs
inputs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
# Target / Actual outputs
outputs = [1, -1, -1, -1]

w1 = w2 = b = 0


def hebbian():
    global w1, w2, b
    print("dw1\tdw2\ty\ttw1\ttw2\tb")
    for i in range(0, len(inputs)):
        x1, x2 = inputs[i]
        y = outputs[i]
        w1 += y*x1
        w2 += y*x2
        b += y
        print(x1, x2, y, w1, w2, b, sep="\t")


hebbian()
print("Learning complete")

print("Output using predicted bias")
print("x1\tx2\ty")
for i in range(0, len(inputs)):
    x1, x2 = inputs[i]
    y = outputs[i]
    pred = 1 if (x1*w1)+(x2*w2) + b > 0 else -1
    print(x1, x2, pred, sep="\t")
