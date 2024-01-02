from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."

def get_requirements(req_path: str) -> list[str]:
    '''Function to return the list of requirements for installing package.
    '''
    requirements = []
    with open(req_path, "r") as req_obj:
        requirements = req_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="e2emlproject",
    version="0.0.1",
    author="Swaraj Reddy Chada",
    author_email="swarajreddy10972@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"), # ["pandas", "numpy", "seaborn"],
)
