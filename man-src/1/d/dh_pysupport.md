---
title: "dh_pysupport(1)"
name: "dh_pysupport"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_pysupport/"
description: "dh_pysupport – use the python-support framework to handle Python modules"
---

<h2 class="name">NAME</h2>
<p> dh_pysupport &#8211; use the python-support framework to handle Python modules </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_pysupport</code> [<i>debhelper options</i>] [-V <i>X.Y</i>] [-X <i>item</i> [&#8230;]] [-n] [<i>module dirs &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_pysupport is a debhelper program that will scan your package, detect public modules in <i>/usr/lib/pythonX.Y/site-packages</i>, and move them to the shared Python modules location. It will generate appropriate postinst/prerm scripts to byte-compile modules installed there for all available python versions. </p>
<p> It will also look for private Python modules and will byte-compile them with the current Python version. You may have to list the directories containing private Python modules. </p>
<p> If a file named <i>debian/pyversions</i> exists, it is used to determine the python versions with which the package can work. </p>
<p> Appropriate dependencies on python-support, python and python<i>X.Y</i> are put in ${python:Depends}. The ${python:Versions} and ${python:Provides} optional substitution variables are made available as well.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>module dirs</i></p>
<dd> If your package installs private python modules in non-standard directories, you can make dh_pysupport check those directories by passing their names on the command line. By default, it will check /usr/lib/$PACKAGE, /usr/share/$PACKAGE, /usr/lib/games/$PACKAGE and /usr/share/games/$PACKAGE</p>
<dt><code>-n</code>, <code>&#8211;noscripts</code></p>
<dd> Do not modify postinst/postrm scripts.</p>
<dt><code>-d</code></p>
<dd> This option is deprecated.</p>
<dt><code>-V</code> <i>X.Y</i></p>
<dd> Force private modules to be bytecompiled with the specific <i>X.Y</i> python version, regardless of the default python version on the system.</p>
<dt><code>-X</code> <i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain &#8220;item&#8221; anywhere in their filename from being taken into account to generate the python dependency. It also excludes them from byte-compilation. You may use this option multiple times to build up a list of things to exclude.</dl>
<h2>CONFORMS TO</h2>
<p> Python policy as of 2006-08-10</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of python-support but is made to work with debhelper.</p>
<h2>AUTHORS</h2>
<p> Josselin Mouette &lt;joss [at] debian.org&gt;, Raphael Hertzog &lt;hertzog [at] debian.org&gt; </p>
<h2>Index</h2>
