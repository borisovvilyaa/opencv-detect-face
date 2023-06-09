import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facedetectorapp",
    version="0.1.3",
    author="Illia Borusov",
    author_email="",
    description="Python application for real-time face detection using OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/borisovvilyaa/opencv-detect-face",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.19.3',
        'opencv-python>=4.5.3.56',
    ],
)
