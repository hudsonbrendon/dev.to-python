from setuptools import setup


setup(name='dev.to-python',
      version='0.1',
      description='Access DEV articles, comments and other resources via API',
      url='https://github.com/hudsonbrendon/dev.to-python',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['dev'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)