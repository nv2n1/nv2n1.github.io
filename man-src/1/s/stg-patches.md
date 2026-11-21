---

title: "stg-patches(1)"
name: "stg-patches"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-patches/"
description: "stg-patches – Show the applied patches modifying a file"
---

<pre><code>
stg patches[options][--][ &lt; files or dirs &gt; ]
</code></pre>
<p> Show the applied patches modifying the given files. Without arguments, it shows the patches affected by the local tree modifications. The <i>&#8211;diff</i> option also lists the patch log and the diff for the given files.</p>
<h2>OPTIONS</h2>
<p> -d, &#8211;diff</p>
<dl>
<dt>
</dt><dd> Show the diff for the given files.</dd></dl>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
</dt><dd> Use BRANCH instead of the default branch.</dd></dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
