---
title: "gpt-deps(8)"
name: "gpt-deps"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-deps/"
description: "gpt-deps – Reports on an installation’s package dependencies"
---

<p><code>gpt-deps</code> &#8211; Reports on an installation&#8217;s package dependencies</p>
<h2>Synopsis</h2>
<p>gpt-deps [ -help -man -version ] DependencyTypes</p>
<h2>Description</h2>
<p><code>gpt-deps</code> is an experimental script which prints out an html file that contains a hyperlinked report of dependencies for packages installed at <tt>$GLOBUS_LOCATION</tt>. The output file is called ./deptable.html. One or more of the following dependency types can be reported: </p>
<pre> Runtime - Packages needed at runtime
 Setup - Packages needed to set up localization data such as 
 configuration files.
 Build - Packages needed to build other packages.</pre>
<p>If you are confused by the dependency types, simply run &#8216;gpt-deps Runtime Setup Build&#8217; and view ./deptree.html with your favorite browser. Be sure to set <tt>$GLOBUS_LOCATION</tt>.</p>
<h2>Options</h2>
<dl>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</p>
<dt><code>-version</code></p>
<dd>Prints the version of <font SIZE="-1">GPT</font> and exits.</dl>
<h2>Bugs</h2>
<p>Future versions will provide more flexibility in inputs, and output formats.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-gpt-install/">gpt-install</a></i>(8) <i><a href="/docs/linux/man/8-gpt-verify/">gpt-verify</a></i>(8) <i><a href="/docs/linux/man/8-gpt-query/">gpt-query</a></i>(8) <i><a href="/docs/linux/man/8-gpt-postinstall/">gpt-postinstall</a></i>(8)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt;</p>
