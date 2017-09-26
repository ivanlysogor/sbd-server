#!/usr/bin/env python

from distutils.core import setup

setup(name="sbdIOT",
      version="0.1",
      description="Iridium Short Burst Data DirectIP handling with compressing and parsing MQTT Messages. Based on Gadomsky code",
      author="Ivan Lysogor",
      author_email="ilysogor@gmail.com",
      url="https://github.com/ivanlysogor/sbdIOT",
      packages=["sbd"],
      scripts=["bin/iridiumd"],
      install_requires=[
          "python-daemon",
          ]
      )
