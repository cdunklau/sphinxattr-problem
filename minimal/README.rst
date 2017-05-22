This is a minimal reproduction of the issue. It seems that 'attribute'
directives are handled differently than class or method directives.

If you add ``.. module:: mypkg.models`` before the
``.. class:: SomeClass(config)`` directive in docs/index.rst, the links to the
attributes get created properly. However, the links to the class and method get
created regardless of whether the module is explicitly specified in this way or
not.

Setup::

    # In the minimal/ dir
    python3 -m venv venv
    venv/bin/pip install sphinx
    # Remove the build dir, otherwise the ref warnings don't get issued
    # after the first run (because cached build env?)
    rm docs/_build/ -rf && \
        SPHINXBUILD=`pwd`/venv/bin/sphinx-build make -e -C docs html


End of output (without explicit ``.. module`` directive)::

    docnames to write: index
    preparing documents... done
    writing output... [100%] index
    [app] emitting event: 'doctree-resolved'(<document: <comment...><section "welcome to attrissue's documentati ...>, 'index')

    /home/cdunklau/Development/sphinxattrissue/minimal/docs/index.rst:18: WARNING: py:attr reference target not found: mypkg.models.SomeClass.id
    /home/cdunklau/Development/sphinxattrissue/minimal/docs/index.rst:19: WARNING: py:attr reference target not found: mypkg.models.SomeClass.workflow_state
    /home/cdunklau/Development/sphinxattrissue/minimal/docs/index.rst:20: WARNING: py:attr reference target not found: mypkg.models.SomeClass.age
    /home/cdunklau/Development/sphinxattrissue/minimal/docs/index.rst:22: WARNING: py:attr reference target not found: mypkg.models.SomeClass.name
    /home/cdunklau/Development/sphinxattrissue/minimal/docs/index.rst:23: WARNING: py:attr reference target not found: mypkg.models.SomeClass.host
    generating indices... genindex
    [app] emitting event: 'html-collect-pages'()
    writing additional pages... search
    copying static files... done
    copying extra files... done
    dumping search index in English (code: en) ... done
    dumping object inventory... done
    build succeeded, 5 warnings.
    [app] emitting event: 'build-finished'(None,)

    Build finished. The HTML pages are in _build/html.
    make: Leaving directory '/home/cdunklau/Development/sphinxattrissue/minimal/docs'
