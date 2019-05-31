import shutil
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

shutil.copy("transmart/transproxy.service", "/etc/systemd/system/")

setuptools.setup(
    name='transmart',
    version='0.2',
    author='zhaohui',
    author_email='zhaohui-sol@gfoxmail.com',
    description='Transfer file over LAN or Internet via terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/izhaohui/transmart',
    packages=['transmart'],
    scripts=['transmart/transmart', 'transmart/transproxy'],
    install_requires=['qrcode==6.1', 'Flask==1.0.2', 'requests==2.21.0']
)