---
title: "debconf-loadtemplate(1)"
name: "debconf-loadtemplate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-loadtemplate/"
---

<h2 class="name">NAME</h2>
 

 debconf-loadtemplate - load template file into debconf database 

<h2>SYNOPSIS</h2>

 <pre>
 debconf-loadtemplate owner file [file ..]
</pre>

<h2>DESCRIPTION</h2>

 Loads one or more template files into the debconf database. The first parameter specifies the owner of the templates (typically, the owner is the name of a debian package). The remaining parameters are template files to load.

<h2>WARNING</h2>

 This program should never be used from a maintainer script of a package that uses debconf! It may however, be useful in debugging, or to seed the debconf database.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-debconf-communicate/">debconf-communicate</a></i>(1)

<h2>AUTHOR</h2>

 Joey Hess &lt;joeyh [at] debian.org&gt; 

<h2>Index</h2>


