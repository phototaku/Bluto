from setuptools import setup, find_packages

setup(
    name='Bluto',
    version='3.0b',
    author='Darryl lane',
    author_email='DarrylLane101@gmail.com',
    url='https://github.com/darryllane/Bluto',
    packages=['Bluto'],
    include_package_data=True,
    license='LICENSE.txt',
    description='''
    DNS Recon | Brute Forcer | DNS Zone Transfer | DNS Wild Card Checks
    DNS Wild Card Brute Forcer | Email Enumeration | Staff Enumeration
    Compromised Account Checking''',
    long_description=open('README.md').read(),
    scripts=['Bluto/bluto'],
    install_requires=[
        "bs4",
		"certifi",
		"chardet",
		"EasyProcess",
		"idna",
		"lxml",
		"progressbar",
		"pythonwhois",
		"PyVirtualDisplay",
		"requests",
		"selenium",
		"tqdm",
		"urllib3",
		"dnspython",
		"termcolor",
		"BeautifulSoup4",
		"requests[security]",
		"oletools",
		"pdfminer"
    ],
)

