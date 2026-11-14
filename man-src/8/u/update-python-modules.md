---
title: "update-python-modules(8)"
name: "update-python-modules"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-python-modules/"
description: "update-python-modules – byte-compile python modules"
---

<p>update-python-modules &#8211; byte-compile python modules</p>
<h2>Synopsis</h2>
<p><code>update-python-modules</code> [<i>options</i>] [<i>package.public</i> [&#8230;]]</p>
<h2>Description</h2>
<p>The <code>update-python-modules</code> command is part of the <code>python-support</code> bundle. </p>
<p> <code>update-python-modules</code> is responsible for the byte-compilation of python modules. When used in byte-compilation mode, it will byte-compile modules references in the files given on the command line. When used in installation mode, it will byte-compile them once for each installed python version, and will make them available for all of them. </p>
<p> At each invocation, with or without arguments, <code>update-python-modules</code> will check for installed python versions, and will build or remove modules according to new or removed versions since the last time it was run.</p>
<h2>Arguments</h2>
<p>Arguments must be files or directories located in the <i>/usr/share/python-support</i> directory. Depending on their extension, they are treated differently.</p>
<dl>
<dt><i>package</i>.public</p>
<dd>A file listing public modules to install for each version. These modules must lie in <i>/usr/share/pyshared</i> or <i>/usr/lib/pyshared</i>.</p>
<dt><i>package</i>.private</p>
<dd>A file listing private modules to byte-compile for one Python version.</p>
<dt><i>package</i>/</p>
<dd>A legacy directory hierarchy of public modules. The C extensions and portions that change with the Python version are to be found in <i>/usr/lib/python-support/python</i>X.Y<i>/</i>package<i>/</i>.</p>
<dt><i>package.dirs</i></p>
<dd>A legacy file listing directories where to find private modules.</dl>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Detail all actions while they are performed.</p>
<dt><code>-b, &#8211;bytecompile</code></p>
<dd>Only accept to work on private modules. When given this option, <code>update-python-modules</code> will fail if passed references to public modules.</p>
<dt><code>-i, &#8211;install</code></p>
<dd>Only accept to work on public modules. When given this option, <code>update-python-modules</code> will fail if passed references to public modules.</p>
<dt><code>-c, &#8211;clean</code></p>
<dd>Clean modules instead of installing them.</p>
<dt><code>-a, &#8211;rebuild-all</code></p>
<dd>Rebuild all private modules. This is necessary when the default python version was changed, for example. .TP <code>-f, &#8211;force-rebuild-all</code> Clean all modules (public and private), and rebuild them.</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/pymodules/python</i>X.Y<i>/</i></p>
<dd>These directories contain the byte-compiled modules for version python<i>X.Y</i>.</dl>
<h2>See Also</h2>
<p>/usr/share/doc/python-support/README.gz</p>
<h2>Author</h2>
<p>Josselin Mouette &lt;joss [at] debian.org&gt;.</p>
