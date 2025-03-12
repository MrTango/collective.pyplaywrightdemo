collective.pyplaywrightdemo
===========================

To run test you can use `pytest` or `tox`.

```sh
cd collective.pyplaywrightdemo
./venv/bin/pytest tests/
```

```sh
tox -e e2e
```

In `pytest.ini` you can change settings and enable to see the browser for example.

The following config will enable the chromium browser and slow down the steps, so one can follow them.

```ini
addopts = -v --browser chromium --headed --slowmo 900
```


Authors
-------

Maik Derstappen - MrTango


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.pyplaywrightdemo/issues
- Source Code: https://github.com/collective/collective.pyplaywrightdemo
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
