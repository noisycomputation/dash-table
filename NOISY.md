# dash-table Fork

## Motivation

The upstream dash-table had a buggy CSS variable support check in v4.7, rendering
the activeEdge immutable in CSS: hardcoded hotpink rather than var(--accent).

## Build Instructions

First, set up the environment correctly.

* Create an outer directory, called something like dash-env, and move
  the cloned dash-table directory into it.
* In the outer directory, create a python + node virtualenv:
    
    ```
    python -m venv venv
    source venv/bin/activate
    pip install -U pip; pip install nodeenv
    nodeenv -p
    ```

Make sure you have the correct branch checked out and build:

* npm install
* npm run private::build:js
* python setup.py sdist

If the javascript build results in errors, often these are caused by incorrect version
pinning in package.json. @babel/core and @babel/preset-env are frequent culprits, try
pinning to 7-9-0 and 7-9-5, respectively, and re-run `npm install`.

The output package will be in the `dist` directory. This is ready to be installed with
pip.

## Changes to Upstream

The workflow is to create a new branch from the release that is to be modified:

    git checkout -b noisy_v4.6.2 v4.6.2

The default `noisy` branch merely tracks whichever of the versioned `noisy` branches
is currently in use by noisycomputing. To avoid cluttering the log, point `noisy` to
the appropriate commit as needed and `git push origin --force` without mercy or
concern for the integrity of this repo:

    git branch -vv (note the commit ID of the noisy branch you want to point to)
    git reset --hard {commit ID}
    git push origin --force

When committing changes, make sure to omit lint verification:

    git commit --no-verify

#### Changelog

* v4.6.2

   core/environment/index.ts:

    * changed `ACTIVE_EDGE` to `var(--active_edge)` in _core/environment/index.ts_
