---
title: "semodule_deps(8)"
name: "semodule_deps"
section: "8"
letter: "s"
url: "/docs/linux/man/8-semodule_deps/"
description: "semodule_deps – show the dependencies between SELinux policy packages."
---

<p>semodule_deps &#8211; show the dependencies between SELinux policy packages. </p>
<h2>Synopsis</h2>
<p><code>semodule_deps [-v -g -b] basemodpkg modpkg1 [modpkg2 &#8230; ]</code></p>
<h2>Description</h2>
<p>semodule_deps is a developer tool for showing the dependencies between policy packages. For each module it prints a list of modules that must be present for a module&#8217;s requirements to be satisfied. It only deals with requirements, not optional dependencies. In order for semodule_deps to give useful information the list of packages passed in cannot have unsatisfied dependencies. In general this means that the list of modules will usually be quite long. By default options to the base module are excluded as almost every module has this dependency. The -b option will include these dependencies. In addition to human readable output, semodule_deps can output the dependencies in the Graphviz dot format (<a rel="nofollow" href="http://www.graphviz.org/)">http://www.graphviz.org/)</a> using the -g option. This is useful for producing a picture of the dependencies. </p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></p>
<dd>verbose mode</p>
<dt><code>-g</code></p>
<dd>output dependency information in Graphviz dot format</p>
<dt><code>-b</code></p>
<dd>include dependencies to the base module &#8211; by default these are excluded </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-checkmodule/">checkmodule</a>(8), <a href="/docs/linux/man/8-semodule_package/">semodule_package</a>(8), <a href="/docs/linux/man/8-semodule/">semodule</a>(8), <a href="/docs/linux/man/8-semodule_link/">semodule_link</a>(8)</code></p>
<h2>Authors</h2>
<pre>This manual page was written by Karl MacMillan &lt;kmacmillan [at] mentalrootkit.com&gt;.
The program was written by Karl MacMillan &lt;kmacmillan [at] mentalrootkit.com&gt;.</pre>
