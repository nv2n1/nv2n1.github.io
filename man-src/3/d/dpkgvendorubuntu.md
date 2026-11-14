---
title: "dpkgvendorubuntu(3)"
name: "dpkgvendorubuntu"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgvendorubuntu/"
---

Dpkg::Vendor::Ubuntu - Ubuntu vendor object 

<h2>Description</h2>This vendor object customize the behaviour of dpkg-source to check that Maintainers have been modified if necessary.
<h2>Public Functions</h2><dl COMPACT><dt>$bugs = Dpkg::Vendor::Ubuntu::find_launchpad_closes($changes)
<dd>Takes one string as argument and finds ``<font SIZE="-1">LP:</font> #123456, #654321'' statements, which are references to bugs on Launchpad. Returns all closed bug numbers in an array reference.</dl><h2>Changes</h2><h3>Version 0.xx</h3>This is a semi-private module. Only documented functions are public.
