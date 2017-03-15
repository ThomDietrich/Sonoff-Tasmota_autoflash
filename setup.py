from distutils.core import setup
setup(
  name = 'sonoff_autoflash',
  packages = ['sonoff_autoflash'],
  install_requires=[
          'esptool',
      ],
  version = 'v0.1.2',
  description = 'little python script to flash sonoff devices',
  author = 'Yann Doersam',
  author_email = 'yann.doersam@gmail.com',
  url = 'https://github.com/yann25/Sonoff-Tasmota_autoflash', # use the URL to the github repo
  download_url = 'https://github.com/yann25/Sonoff-Tasmota_autoflash/archive/v0.1.2.tar.gz', # I'll explain this in a second
  keywords = ['ESP8266', 'flashing', 'sonoff', 'itead'], # arbitrary keywords
  classifiers = [],
  zip_safe=False
)
