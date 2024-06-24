import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CrossDarkBiology",
    version="0.0.0",
    author="CrossDark",
    author_email="liuhanbo333@icloud.com",
    description="CrossDark's biology tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CrossDark/CellSpeedMeasure",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'moviepy',
        'av',
        'ultralytics',
        'pymysql'
    ],
    entry_points={
        'console_scripts': [
            'douyin_image=douyin_image:main'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
