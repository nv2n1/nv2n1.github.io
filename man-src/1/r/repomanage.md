---

title: "repomanage(1)"
name: "repomanage"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repomanage/"
description: "repomanage – list the newest or oldest RPM packages in a directory"
---

<p> repomanage &#8211; list the newest or oldest RPM packages in a directory</p>
<h2>SYNOPSIS</h2>
<p> <code>repomanage</code> [options] directory</p>
<h2>DESCRIPTION</h2>
<p> <code>repomanage</code> is a program to manage a directory of RPM packages. It displays a list of the newest or oldest packages in a directory for easy piping to xargs or similar programs. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help message, and then quit.</dd>
<dt><code>-o, &#8211;old</code></dt>
<dd> Print the oldest packages.</dd>
<dt><code>-n, &#8211;new</code></dt>
<dd> Print the newest packages.</dd>
<dt><code>-s, &#8211;space</code></dt>
<dd> Space-separated instead of newline-separated output.</dd>
<dt><code>-k KEEP, &#8211;keep=KEEP</code></dt>
<dd> Newest N packages to keep &#8211; defaults to 1.</dd>
<dt><code>-c, &#8211;nocheck</code></dt>
<dd> Do not check package payload signatures/digests. </dd>
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
