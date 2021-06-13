piwigo
======

Piwigo is a famous open-source online photo gallery. 

piwigo is a module python to communicate with Piwigo API.


Installation
------------

::

    pip install piwigo
        
Or

::

    git clone https://github.com/fraoustin/piwigo.git
    cd piwigo
    python setup.py install

Usage
-----

::

    from piwigo import Piwigo
    mysite = Piwigo('http://mysite.com')
    print(mysite.pwg.getVersion())

Piwigo object has an attribute name of webservice.

List of webservices at http://mysite.com/tools/ws.htm

Example of uploading a file into category with id=1

::

    from piwigo import Piwigo
    mysite = Piwigo('http://mysite.com')
    mysite.pwg.session.login(username="test", password="test")
    mysite.pwg.images.addSimple(image="myphoto.jpg", category=1)
    mysite.pwg.session.logout()
