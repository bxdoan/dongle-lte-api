from setuptools import setup, find_packages


def read_readme() -> str:
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='dongle-lte-api',
    version='0.0.2',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'dongle_lte_api': ['py.typed']},
    install_requires=[
        'requests',
    ],
    tests_require=[
        'tox'
    ],
    url='https://github.com/bxdoan/dongle-lte-api',
    license='LGPL-3.0 ',
    author='Doan Bui',
    author_email='hi@bxdoan.com',
    description='API For dongle LAN/WAN LTE USB Modems',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
    ],
    python_requires='>=3.10',
    project_urls={
        'Release notes': 'https://github.com/bxdoan/dongle-lte-api/releases',
    },
)
