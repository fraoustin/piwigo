piwigo
======

Piwigo is a famous open-source online photo gallery. 

piwigo is a module python for communicate with API Piwigo.


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

    import piwigo
    mysite = Piwigo('http://mysite.com')
    print(mysite.pwg.getVersion())

Piwigo object has attribute name of webservice.

List of webservice at http://mysite.com/tools/ws.htm

Sample of uplad file in category with id=1

::

    import piwigo
    mysite = Piwigo('http://mysite.com')
    mysite.pwg.session.login(username="test", password="test")
    mysite.pwg.images.addSimple(image="myphoto.jpg", "category"=1)
    mysite.pwg.session.logout()
