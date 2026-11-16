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
<dt><i>package</i>.public</dt>
<dd>A file listing public modules to install for each version. These modules must lie in <i>/usr/share/pyshared</i> or <i>/usr/lib/pyshared</i>.</dd>
<dt><i>package</i>.private</dt>
<dd>A file listing private modules to byte-compile for one Python version.</dd>
<dt><i>package</i>/</dt>
<dd>A legacy directory hierarchy of public modules. The C extensions and portions that change with the Python version are to be found in <i>/usr/lib/python-support/python</i>X.Y<i>/</i>package<i>/</i>.</dd>
<dt><i>package.dirs</i></dt>
<dd>A legacy file listing directories where to find private modules.</dd></dl>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Show summary of options.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Detail all actions while they are performed.</dd>
<dt><code>-b, &#8211;bytecompile</code></dt>
<dd>Only accept to work on private modules. When given this option, <code>update-python-modules</code> will fail if passed references to public modules.</dd>
<dt><code>-i, &#8211;install</code></dt>
<dd>Only accept to work on public modules. When given this option, <code>update-python-modules</code> will fail if passed references to public modules.</dd>
<dt><code>-c, &#8211;clean</code></dt>
<dd>Clean modules instead of installing them.</dd>
<dt><code>-a, &#8211;rebuild-all</code></dt>
<dd>Rebuild all private modules. This is necessary when the default python version was changed, for example. .TP <code>-f, &#8211;force-rebuild-all</code> Clean all modules (public and private), and rebuild them.</dd></dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/pymodules/python</i>X.Y<i>/</i></dt>
<dd>These directories contain the byte-compiled modules for version python<i>X.Y</i>.</dd></dl>
<h2>See Also</h2>
<p>/usr/share/doc/python-support/README.gz</p>
<h2>Author</h2>
<p>Josselin Mouette &lt;joss [at] debian.org&gt;.</p>
