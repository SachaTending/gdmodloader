import re
import pathlib
from setuptools import setup

root = pathlib.Path(__file__).parent

requirements = (root / "requirements.txt").read_text("utf-8").splitlines()

txt = (root / "gdmodloader" / "__init__.py").read_text("utf-8")

try:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', txt, re.MULTILINE).group(1)

except AttributeError:
    raise RuntimeError("Failed to find version.") from None

readme = (root / "README.rst").read_text("utf-8")

extras_require = {
    "docs": ["sphinx", "sphinx_rtd_theme", "sphinxcontrib_trio", "sphinxcontrib-websupport"],
}


setup(
    name="gdmodloader",
    author="SpookyBear0",
    author_email="collinmcarroll@gmail.com",
    url="https://github.com/SpookyBear0/gdmodloader",
    project_urls={
        "Documentation": "https://gdmodloader.readthedocs.io/en/latest",
        "Issue tracker": "https://github.com/SpookyBear0/gdmodloader/issues",
    },
    version=version,
    packages=["gdmodloader", "gdmodloader.sdk"],
    license="MIT",
    description="ModLoader for Geometry Dash, written in Python",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={"console_scripts": ["modloader = modloader.__main__:main"]},
)
