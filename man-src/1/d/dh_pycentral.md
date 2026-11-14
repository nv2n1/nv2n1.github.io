---
title: "dh_pycentral(1)"
name: "dh_pycentral"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_pycentral/"
description: "dh_pycentral – use the python-central framework to handle Python modules and extensions"
---

<h2 class="name">NAME</h2>
<p> dh_pycentral &#8211; use the python-central framework to handle Python modules and extensions </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_pycentral</code> [<i>debhelper options</i>] [<code>-n</code>] [<code>-X</code><i>item</i>] [<code>-V</code> <i>version</i>] [<i>module dirs &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_pycentral is a debhelper program that will scan your package, detect public Python modules and move them in /usr/share/pycentral so that python-central can byte-compile those for all supported Python versions. Extensions are kept into the original installation location. </p>
<p> Moving the files to the pycentral location and adding symbolic links to /usr/lib/pythonX.Y/*-packages can be done by setting the environment varibale <font SIZE="-1">DH_PYCENTRAL</font> to a string containing the string <code>include-links</code>. </p>
<p> Moving the files to the pycentral location can be disabled by setting the environment varibale <font SIZE="-1">DH_PYCENTRAL</font> to a string containing the string <code>nomove</code>. </p>
<p> The functionality to shorten the time of unavailabilty of files during unpack and configure has been removed (symlinking files in the preinst and not removing the symlinked files on upgrade) in version 0.6.9. </p>
<p> You must have filled the XS-Python-Version header to indicate the set of python versions that are going to be supported. dh_pycentral expects the XB-Python-Version for each binary package it is supposed to work on. </p>
<p> dh_pycentral will also generate substitution variables: the ${python:Provides} variable will contain versioned provides of the package (if the package&#8217;s name starts with &#8220;python-&#8221;). A python-foo package could provide &#8220;python2.3-foo&#8221; and &#8220;python2.4-foo&#8221; at the same time. Python extensions have to provide those whereas it&#8217;s only option for pure python modules. </p>
<p> The ${python:Versions} variable should be used to provide the required XB-Python-Version field listing the python versions supported by the package.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>module dirs</i></p>
<dd> If your package installs python modules in non-standard directories, you can make dh_pycentral check those directories by passing their names on the command line. By default, it will check /usr/lib/$PACKAGE, /usr/share/$PACKAGE, /usr/lib/games/$PACKAGE, /usr/share/games/$PACKAGE, /usr/lib/python?.?/site-packages and /usr/lib/python?.?/dist-packages. </p>
<p> Note: only /usr/lib/python?.?/site-packages and the extra names on the command line are searched for binary (.so) modules.</p>
<dt><code>-V</code> <i>version</i></p>
<dd> If the .py files your package ships are meant to be used by a specific pythonX.Y version, you can use this option to specify the desired version, such as 2.3. Do not use if you ship modules in /usr/lib/site-python. </p>
<p> With the new policy, this option is mostly deprecated. Use the XS-Python-Field to indicate that you&#8217;re using a specific python version.</p>
<dt><code>-n</code>, <code>&#8211;noscripts</code></p>
<dd> Do not modify postinst/postrm scripts.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain &#8220;item&#8221; anywhere in their filename from being taken into account to generate the python dependency. You may use this option multiple times to build up a list of things to exclude.</dl>
<h2>CONFORMS TO</h2>
<p> Python policy, version 0.4.1 (2006-06-20)</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of python-central but is made to work with debhelper.</p>
<h2>AUTHORS</h2>
<p> Raphael Hertzog &lt;hertzog [at] debian.org&gt; </p>
<p> Also includes bits of the old dh_python written by Josselin Mouette &lt;joss [at] debian.org&gt; who used many ideas from Brendan O&#8217;Dea &lt;bod [at] debian.org&gt;. </p>
<h2>Index</h2>
