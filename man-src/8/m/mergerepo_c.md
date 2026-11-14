---
title: "mergerepo_c(8)"
name: "mergerepo_c"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mergerepo_c/"
---

mergerepo_c - Merge multiple rpm-md format repositories together

<h2>Synopsis</h2>

mergerepo_c [options] --repo repo1 --repo repo2

<h2>Options</h2>

<h3>--version</h3>

Show program's version number and exit

<h3>-r --repo REPOS</h3>

Repo url

<h3>-a --archlist ARCHLIST</h3>

Defaults to all arches - otherwise specify arches

<h3>-d --database</h3>

<h3>--no-database</h3>

<h3>-v --verbose</h3>

<h3>-o --outputdir OUTPUTDIR</h3>

Location to create the repository

<h3>--nogroups</h3>

Do not merge group (comps) metadata

<h3>--noupdateinfo</h3>

Do not merge updateinfo metadata

<h3>--compress-type COMPRESS_TYPE</h3>

Which compression type to use

<h3>--method MERGE_METHOD</h3>

Specify merge method for packages with the same name and arch (available merge methods: repo (default), ts, nvr)

<h3>--all</h3>

Include all packages with the same name and arch if version or release is different. If used --method argument is ignored!

<h3>--noarch-repo URL</h3>

Packages with noarch architecture will be replaced by package from this repo if exists in it.

<h3>--unique-md-filenames</h3>

Include the file's checksum in the metadata filename, helps HTTP caching (default).

<h3>--simple-md-filenames</h3>

Do not include the file's checksum in the metadata filename.

<h3>--omit-baseurl</h3>

Don't add a baseurl to packages that don't have one before.

<h3>-k --koji</h3>

Enable koji mergerepos behaviour.

<h3>-g --groupfile GROUPFILE</h3>

Path to groupfile to include in metadata.

<h3>-b --blocked FILE</h3>

A file containing a list of srpm names to exclude from the merged repo. Only works with combination with --koji/-k.
