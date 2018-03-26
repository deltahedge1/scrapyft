# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = ft_scraper.settings']},
    package_data = {'ft_scraper': ['spiders/*.txt','spiders/*.py']},
    zip_safe=False,
)
