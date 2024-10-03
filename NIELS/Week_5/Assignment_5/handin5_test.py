import numpy as np
import matplotlib.pyplot as plt
import handin5 as h5

mnist_data = h5.read_mnist_csv('mnist_test_200.csv')
print(mnist_data.shape)

digital_image_groups = h5.group_by_label(mnist_data)
if len(digital_image_groups) != 10:
    print("Error: Expected 10 groups, got", len(digital_image_groups))
    exit(1)
else:
    print(f"Success: Found {len(digital_image_groups)} groups")

random_digit = np.random.randint(0, 10)
digit_image = h5.get_image(digital_image_groups, random_digit)

plt.imshow(digit_image, cmap='gray')
plt.axis('off')
plt.show()

plt.savefig('random_image.png')

