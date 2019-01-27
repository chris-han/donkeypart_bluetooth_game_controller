from setuptools import setup, find_packages

setup(name='donkeypart_xbox_one_s_controller',
      version='0.1',
      description='xbox one s controller part for donkeycar.',
      long_description='none',
      long_description_content_type="text/markdown",
      url='https://github.com/chris-han/donkeypart_xbox_one_s_controller',
      author='Chris Han',
      license='MIT',
      install_requires=['evdev', 'pyyaml'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars',

      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
