from setuptools import setup 

setup( 
    name='travel_update', 
    version='0.1', 
    description='Generate travel and weather updates for office excursions', 
    author='Miles Bailey-Braendgaard', 
    author_email='milesbb101@gmail.com', 
    packages=['travel_update', 'travel_update.utils', 'travel_update.api'], 
    install_requires=[ 
        'requests', 
        'python-dotenv',
    ], 
) 