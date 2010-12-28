import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup

tests_require = ['pytest', 'webtest']

setup(
    name = "pecanraw",
    version = "0.0.2",
    packages = ['pecanraw'],
    include_package_data=True,
    package_data = {
        '': ['distribute_setup.py'],
        },

    # metadata 
    author = "Alfredo Deza",
    author_email = "alfredodeza [at] gmail [dot] com",
    description = "A Pecan Hook to display per request information.",
    long_description = """\
 An easy hook for the Pecan Web Framework that provides some information 
 in a per request basis for development purposes.

 Currently supported:

 * Request Method 
 * Request Response Status 
 * Request URL
 * Controller Method Hit
 * Pecan Context information 
 * Pecan Hooks enabled
 * Parameters
 
 It is not yet configurable since it only displays a small amount of data, but
 feature releases should include a way to properly configure the verbosity of the 
 output.

 Once installed, the proper way of adding it to your Pecan application is::

    from pecanraw import RawHook

    app = make_app(RootController(), hooks=[RawHook()]


 """,
   zip_safe = False,
   classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
      ],

    license = "MIT",
    keywords = "WSGI stats requests context development",
    url = "http://github.com/alfredodeza/pecanraw",   

)

