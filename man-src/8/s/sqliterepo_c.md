---
title: "sqliterepo_c(8)"
name: "sqliterepo_c"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sqliterepo_c/"
---

sqliterepo_c - Generate sqlite db files for a repository in rpm-md format

<h2>Synopsis</h2>

sqliterepo_c [options] &lt;repo_directory&gt;

<h2>Options</h2>

<h3>-V --version</h3>

Show program's version number and exit.

<h3>-q --quiet</h3>

Run quietly.

<h3>-v --verbose</h3>

Run verbosely.

<h3>-f --force</h3>

Overwirte existing DBs.

<h3>--keep-old</h3>

Do not remove old DBs. Use only with combination with --force.

<h3>--xz</h3>

Use xz for repodata compression.

<h3>--compress-type &lt;compress_type&gt;</h3>

Which compression type to use.

<h3>--checksum &lt;checksum_type&gt;</h3>

Which checksum type to use in repomd.xml for sqlite DBs.

<h3>--local-sqlite</h3>

Gen sqlite DBs locally (into a directory for temporary files). Sometimes, sqlite has a trouble to gen DBs on a NFS mount, use this option in such cases. This option could lead to a higher memory consumption if TMPDIR is set to /tmp or not set at all, because then the /tmp is used and /tmp dir is often a ramdisk.
