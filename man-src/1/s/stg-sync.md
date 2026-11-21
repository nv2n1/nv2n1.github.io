---

title: "stg-sync(1)"
name: "stg-sync"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-sync/"
description: "stg-sync – Synchronise patches with a branch or a series"
---

<pre><code>
stg sync[options][--][&lt;patch1&gt;][&lt;patch2&gt;][&lt;patch3&gt;..&lt;patch4&gt;]
</code></pre>
<p> For each of the specified patches perform a three-way merge with the same patch in the specified branch or series. The command can be used for keeping patches on several branches in sync. Note that the operation may fail for some patches because of conflicts. The patches in the series must apply cleanly.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
</dt><dd> Synchronise all the applied patches.</dd></dl>
<p> -B REF-BRANCH, &#8211;ref-branch REF-BRANCH</p>
<dl>
<dt>
</dt><dd> Syncronise patches with BRANCH.</dd></dl>
<p> -s SERIES, &#8211;series SERIES</p>
<dl>
<dt>
</dt><dd> Syncronise patches with SERIES.</dd></dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
