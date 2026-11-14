---
title: "git-http-fetch(1)"
name: "git-http-fetch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-http-fetch/"
description: "git-http-fetch – Download from a remote Git repository via HTTP"
---

<h2 class="name">NAME</h2>
<p> git-http-fetch &#8211; Download from a remote Git repository via HTTP </p>
<h2>SYNOPSIS</h2>
<pre><code>
git http - fetch[-c][-t][-a][-d][-v][-w filename][--recover][--stdin | --packfile = &lt;hash&gt; | &lt;commit&gt;]&lt;url&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Downloads a remote Git repository via HTTP. </p>
<p> This command always gets all objects. Historically, there were three options <code>-a</code>, <code>-c</code> and <code>-t</code> for choosing which objects to download. They are now silently ignored.</p>
<h2>OPTIONS</h2>
<p> commit-id</p>
<dl>
<dt>
<dd> Either the hash or the filename under [URL]/refs/ to pull.</dl>
<p> -a, -c, -t</p>
<dl>
<dt>
<dd> These options are ignored for historical reasons.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Report what is downloaded.</dl>
<p> -w &lt;filename&gt;</p>
<dl>
<dt>
<dd> Writes the commit-id into the filename under $GIT_DIR/refs/&lt;filename&gt; on the local end after the transfer is complete.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Instead of a commit id on the command line (which is not expected in this case), <i>git http-fetch</i> expects lines on stdin in the format </p>
<dl>
<dt>
<dd>
<pre>
&lt;commit-id&gt;['	'&lt;filename-as-in--w&gt;]
</pre>
</dl>
</dl>
<p> &#8211;packfile=&lt;hash&gt;</p>
<dl>
<dt>
<dd> For internal use only. Instead of a commit id on the command line (which is not expected in this case), <i>git http-fetch</i> fetches the packfile directly at the given URL and uses index-pack to generate corresponding .idx and .keep files. The hash is used to determine the name of the temporary file and is arbitrary. The output of index-pack is printed to stdout. Requires &#8211;index-pack-args.</dl>
<p> &#8211;index-pack-args=&lt;args&gt;</p>
<dl>
<dt>
<dd> For internal use only. The command to run on the contents of the downloaded pack. Arguments are URL-encoded separated by spaces.</dl>
<p> &#8211;recover</p>
<dl>
<dt>
<dd> Verify that everything reachable from target is fetched. Used after an earlier fetch is interrupted.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
