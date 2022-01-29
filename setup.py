from setuptools import setup

setup(
    name='obsidian-html',
    version='0.2',
    description='Converts an Obsidian vault into HTML',
    url='https://github.com/pankaz/obsidian-html',
    author='pankaz',
    author_email='pankaj.lagu@gmail.com',
    license='MIT',
    packages=['obsidian_html'],
    install_requires=[
      'markdown2',
      'regex'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'obsidian-html=obsidian_html:main'
        ]
    }
)
