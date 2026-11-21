---

title: "verifytree(1)"
name: "verifytree"
section: "1"
letter: "v"
url: "/docs/linux/man/1-verifytree/"
description: "verifytree – verify that a local yum repository is consistent"
---

<p> verifytree &#8211; verify that a local yum repository is consistent</p>
<h2>SYNOPSIS</h2>
<p> <code>verifytree</code> [options] directory</p>
<h2>DESCRIPTION</h2>
<p> <code>verifytree</code> is a program that verifies whether a local yum repository is consistent. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help message, and then quit.</dd>
<dt><code>-a, &#8211;checkall</code></dt>
<dd> Check all packages in the repository.</dd>
<dt><code>-t TESTOPIA, &#8211;testopia=TESTOPIA</code></dt>
<dd> Report results to the given testopia run number.</dd>
<dt><code>-r, &#8211;treeinfo</code></dt>
<dd> Check the checksums of listed files in a .treeinfo file, if available. </dd>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
