from setuptools import setup

setup(
    name='ghviztoggle',
    version='1.0.0',
    description='Quickly change github visibility for your repos',
    url='https://github.com/CakeCrusher/mimicbot/tree/master/mimicbot_cli/mimicbot_chat',
    author='Sebastian Sosa',
    author_email='1sebastian1sosa1@gmail.com',
    license='MIT License',
    packages=['ghviztoggle'],
    install_requires=[
        'requests',
        'typer',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)