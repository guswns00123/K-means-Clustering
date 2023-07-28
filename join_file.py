file = open("./hw3/MNIST/train_label", "r")
# file = open("./hw3/MNIST/test_label", "r")


labels = []

for line in file:
    line = line.strip()
    label = line
    labels.append(label)



file = open("./hw4/pca_64", "r")

img_list = []
i = 0
for line in file:
    line = line.strip()
    img = [img_item for img_item in line.split(',')]
    img_list.append(img)
for i in range(60000):
    img = ' '.join(str(k) for k in img_list[i])
    
    print("%s\t%s" %(labels[i], img))
    

    