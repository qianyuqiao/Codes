from setuptools import setup, find_packages
setup(
name='ImagePlugins',
version='1.0',
description='Image plugins for jpg and png',
author='qian yu qiao',
packages=find_packages(),
include_package_data=True,
entry_points="""
[cms.plugin]
jpg_plugin=image_plugin:make_jpg_image_plugin
png_plugin=image_plugin:make_png_image_plugin

""",

)
