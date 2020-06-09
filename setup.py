from setuptools import setup
import io
import json

with open("package.json") as f:
    package = json.load(f)

package_name = str(package["name"].replace(" ", "_").replace("-", "_"))

setup(
    name=package_name,
    version=package["version"],
    author=package["author"],
    packages=[package_name.replace("_noisycomputation", "")],
    url='https://github.com/noisycomputation/dash-table',
    include_package_data=True,
    license=package["license"],
    description=package.get("description", package_name),
    long_description=io.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
)
