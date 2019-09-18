from setuptools import setup, find_packages

setup(
  name="icub-model-pybullet",
  version="0.1",
  author="Diego Ferigo",
  author_email="diego.ferigo@iit.it",
  description="SDF iCub model for PyBullet",
  license="LGPL",
  platforms='any',
  python_requires='>=3.6',
  keywords="sdf icub models robot robotics humanoid simulation pybullet",
  packages=find_packages(),
  package_data={'': ['meshes/**/*', 'icub_model.sdf']},
  url="https://github.com/diegoferigo/icub-model-pybullet",
)
