# dash-table Fork

## Motivation

The upstream dash-table had a buggy CSS variable support check in v4.7, rendering
the activeEdge immutable in CSS: hardcoded hotpink rather than var(--accent).

More generally, the only correct way to build the entire dash stack is via the
dash project's circleci build, but that config pulls dash components
from github indiscriminately, making builds of earlier builds impossible
without some fragile config hackery.

Instead, the dash, dash-table, dash-html-components, and dash-core-components
projects have been forked. The default `noisy` branch of all the projects points
to mutually-compatible versions, and the dash project's circleci config has
been modified to pull in the forks.


## Build Instructions

Build only using the top-level dash project's circleci method, otherwise
there is no guarantee that the build is reproducible.

## Fixing Javascript Dependencies

Fixing Javascript dependencies is painful, because it requires a local
node environment to be created, versioned correctly, and activated.

First, determine which node version the circleci Docker image specified
in `.circleci/config.yml` uses. For example, if the image specification
is `circleci/python:3.7-stretch-node-browsers`, go to
<https://hub.docker.com/r/circleci/python/tags> and enter the tag into
the search bar, which in this case is `3.7-stretch-node-browsers`. Click
on the appropriate image tag, and search the next screen for `NODE_VERSION`.
In this example, the version is `12.18.0`.

Next, use nodeenv to generate a python + node virtual environment one
directory level above the repo:

    ```
    python -m venv venv
    source venv/bin/activate
    pip install -U pip; pip install nodeenv
    nodeenv --node=12.18.0 -p
    ```

Make the necessary changes to `package.json`, then delete `package-lock.json`
and, if it exists, `node-modules/`. Run `npm install` to generate a new
`package-lock.json`. If it worked, delete `node-modules/`, and git add+commit.

## Branch Policy

The branch `noisy` always points to the commit that should be built. All the
noisycomputation forks of dash project need to have their `noisy` branches set
to a compatible set of commits.

To find a compatible set of commits for a dash version, first set the `dash`
fork's `noisy` branch to the appropriate commit. For example, to build `dash`
at tag v1.11.0, create a new branch from that release:

    git checkout -b noisy-v1.11.0 v1.11.0

Make any desired changes, commit as many times as you like. When ready to build,
point the `noisy` branch to the desired commit and forcibly point `noisy` to
the appropriate commit:

    git branch -vv (note the commit ID of the branch noisy should point to)
    git checkout noisy
    git reset --hard {commit ID}
    git push origin --force

When committing changes, make sure to omit lint verification, since there is
a husky commit hook defined, but it requires a full development environment:

    git commit --no-verify

#### Changelog

* v4.6.2

   core/environment/index.ts:

    * changed `ACTIVE_EDGE` to `var(--active_edge)` in _core/environment/index.ts_
