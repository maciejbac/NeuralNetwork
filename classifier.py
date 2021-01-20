import random
i = random.randint(0, 10000)
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()

print('Values:\n0. T-shirt/top\n1. Trouser\n2. Pullover\n3. Dress\n4. Coat\n5. Sandal\n6. Shirt\n7. Sneaker\n8. Bag\n9. Ankle boot')
