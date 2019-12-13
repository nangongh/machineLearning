from data.SIXray import SIXrayDetection
train_sets = "/Users/xuzhang/PycharmProjects/UnbalancedSamples/coreless_5000.txt"
val_sets = "val"
test_sets = "test"

sd = SIXrayDetection(image_sets=train_sets)

tp201, target, height, width, og_img = sd.pull_item(2)
print(tp201, target, height, width)
