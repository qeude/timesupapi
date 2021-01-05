import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timesup",  # Replace with your own username
    version="0.0.1",
    author="Quentin Eude",
    author_email="quentineude@gmail.com",
    description="TimesUp api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qeude/timesupapi.git",
    packages=setuptools.find_packages(),
)
