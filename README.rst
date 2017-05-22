Issue:

Something about this setup prevents the attr links in docs/prose.rst from being
generated properly.

Setup and result::

    cdunklau@krusty:~/Development/sphinxattrissue$ python3 -V
    Python 3.5.3

    cdunklau@krusty:~/Development/sphinxattrissue$ python3 -m venv venv

    cdunklau@krusty:~/Development/sphinxattrissue$ venv/bin/pip install sphinx sphinxcontrib-napoleon
    Collecting sphinx
      Using cached Sphinx-1.6.1-py2.py3-none-any.whl
    Collecting sphinxcontrib-napoleon
      Using cached sphinxcontrib_napoleon-0.6.1-py2.py3-none-any.whl
    Collecting Pygments>=2.0 (from sphinx)
      Using cached Pygments-2.2.0-py2.py3-none-any.whl
    Collecting six>=1.5 (from sphinx)
      Using cached six-1.10.0-py2.py3-none-any.whl
    Requirement already satisfied: setuptools in ./venv/lib/python3.5/site-packages (from sphinx)
    Collecting sphinxcontrib-websupport (from sphinx)
      Using cached sphinxcontrib_websupport-1.0.1-py2.py3-none-any.whl
    Collecting requests>=2.0.0 (from sphinx)
      Using cached requests-2.14.2-py2.py3-none-any.whl
    Collecting alabaster<0.8,>=0.7 (from sphinx)
      Using cached alabaster-0.7.10-py2.py3-none-any.whl
    Collecting babel!=2.0,>=1.3 (from sphinx)
      Using cached Babel-2.4.0-py2.py3-none-any.whl
    Collecting typing (from sphinx)
      Using cached typing-3.6.1.tar.gz
    Collecting docutils>=0.11 (from sphinx)
      Using cached docutils-0.13.1-py3-none-any.whl
    Collecting snowballstemmer>=1.1 (from sphinx)
      Using cached snowballstemmer-1.2.1-py2.py3-none-any.whl
    Collecting imagesize (from sphinx)
      Using cached imagesize-0.7.1-py2.py3-none-any.whl
    Collecting Jinja2>=2.3 (from sphinx)
      Using cached Jinja2-2.9.6-py2.py3-none-any.whl
    Collecting pockets>=0.3 (from sphinxcontrib-napoleon)
      Using cached pockets-0.5.1-py2.py3-none-any.whl
    Collecting pytz>=0a (from babel!=2.0,>=1.3->sphinx)
      Using cached pytz-2017.2-py2.py3-none-any.whl
    Collecting MarkupSafe>=0.23 (from Jinja2>=2.3->sphinx)
    Installing collected packages: Pygments, six, sphinxcontrib-websupport, requests, alabaster, pytz, babel, typing, docutils, snowballstemmer, imagesize, MarkupSafe, Jinja2, sphinx, pockets, sphinxcontrib-napoleon
      Running setup.py install for typing ... done
    Successfully installed Jinja2-2.9.6 MarkupSafe-1.0 Pygments-2.2.0 alabaster-0.7.10 babel-2.4.0 docutils-0.13.1 imagesize-0.7.1 pockets-0.5.1 pytz-2017.2 requests-2.14.2 six-1.10.0 snowballstemmer-1.2.1 sphinx-1.6.1 sphinxcontrib-napoleon-0.6.1 sphinxcontrib-websupport-1.0.1 typing-3.6.1

    cdunklau@krusty:~/Development/sphinxattrissue$ rm docs/_build/ -rf && SPHINXBUILD=`pwd`/venv/bin/sphinx-build make -e -C docs html > /dev/null 
    /home/cdunklau/Development/sphinxattrissue/docs/prose.rst:12: WARNING: py:attr reference target not found: mypkg.models.SomeClass.id
    /home/cdunklau/Development/sphinxattrissue/docs/prose.rst:13: WARNING: py:attr reference target not found: mypkg.models.SomeClass.workflow_state
    /home/cdunklau/Development/sphinxattrissue/docs/prose.rst:14: WARNING: py:attr reference target not found: mypkg.models.SomeClass.age
    /home/cdunklau/Development/sphinxattrissue/docs/prose.rst:16: WARNING: py:attr reference target not found: mypkg.models.SomeClass.name
    /home/cdunklau/Development/sphinxattrissue/docs/prose.rst:17: WARNING: py:attr reference target not found: mypkg.models.SomeClass.host
    WARNING: html_static_path entry '/home/cdunklau/Development/sphinxattrissue/docs/_static' does not exist
