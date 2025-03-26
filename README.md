collective.pyplaywrightdemo
===========================

To run test you can use `pytest` or `tox`.

```sh
cd collective.pyplaywrightdemo
./venv/bin/pytest tests/
```

if yopu want to run all tests in parallel, this is the way:

```sh
./venv/bin/pytest -n auto tests/

```

or to only use 5 CPU cores:

```sh
./venv/bin/pytest -n 5 tests/

```

this can speed up the process if you have way less tests, then you have CPU threads.
With auto it will create the maximum amount of workers, for me 16 for example, even if i only have two tests.
This step take a bit time, so a call with `-n 2` would be a bit faster.


```sh
tox -e e2e
```

In `pytest.ini` you can change settings and enable to see the browser for example.
Make sure that you don't use the `--headed` option, when running the tests with tox!

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
