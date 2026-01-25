# 📘 NumPy – Day 9  

## 📌 Topic: Meshgrids, Random Module, Image Processing & Histogram Visualization  

On Day 9, I learned advanced NumPy concepts related to **meshgrids, random number generation, basic image processing using NumPy, and data visualization using Matplotlib**. These concepts are widely used in simulations, computer vision, data analysis, and machine learning.

---

## 🔹 Meshgrid

`np.meshgrid()` is used to create coordinate matrices from coordinate vectors.  
It is commonly used in mathematical computations, surface plots, and grid-based operations.

```python
import numpy as np

x = np.arange(1, 4)
y = np.arange(5, 8)

X, Y = np.meshgrid(x, y)
```

---

## 🔹 Working with Random Numbers

### `np.random.randint()`
Generates random integers within a given range.

```python
np.random.randint(1, 10, size=5)
```

---

### `np.random.seed()`
Used to generate reproducible random results.

```python
np.random.seed(42)
np.random.randint(1, 10, 3)
```

---

### `np.random.shuffle()`
Shuffles elements of an array in-place.

```python
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
```

---

### `np.random.choice()`
Randomly selects elements from an array.

```python
np.random.choice([10, 20, 30, 40], size=2)
```

---

## 🔹 Working with Images using NumPy

Images can be treated as NumPy arrays where:
- Rows → height  
- Columns → width  
- Channels → color information  

---

### Reading an Image

```python
import matplotlib.pyplot as plt

img = plt.imread("image.jpg")
```

---

### Checking Image Array Shape

```python
img.shape
```

---

### Displaying the Image

```python
plt.imshow(img)
plt.axis("off")
plt.show()
```

---

## 🔹 Image Manipulation Operations

### Flip Image

```python
np.flip(img, axis=1)
```

---

### Clip (Fade Effect)

```python
np.clip(img, 50, 200)
```

---

### Negative Image

```python
negative_img = 255 - img
```

---

### Trim Image (Cropping)

```python
img[50:200, 50:200]
```

---

## 🔹 Plot Histogram using Matplotlib

Histogram helps to understand pixel intensity distribution.

```python
plt.hist(img.ravel(), bins=256)
plt.title("Image Pixel Intensity Distribution")
plt.show()
```

---

## 🧠 Key Learnings (Day 9)

- Created coordinate grids using meshgrid  
- Generated and controlled random numbers  
- Understood reproducibility using seed  
- Random shuffling and selection techniques  
- Treated images as NumPy arrays  
- Performed basic image processing operations  
- Visualized pixel distributions using histograms  

---

## 🎯 Outcome

Day 9 connected NumPy with **random simulations, image processing, and data visualization**, strengthening practical skills useful for data science, machine learning, and computer vision.

✅ **Day 9 Completed Successfully**

