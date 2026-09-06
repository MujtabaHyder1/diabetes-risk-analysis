from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='diabetes-risk-analysis',
    version='1.0.0',
    author='Data Analysis Team',
    author_email='your-email@example.com',
    description='Comprehensive analysis of diabetes risk prediction dataset',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/diabetes-risk-analysis',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    python_requires='>=3.7',
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
    ],
)
