---
title: "git-hash-object(1)"
name: "git-hash-object"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-hash-object/"
description: "git-hash-object – Compute object ID and optionally creates a blob from a file"
---

<h2 class="name">NAME</h2>
<p> git-hash-object &#8211; Compute object ID and optionally creates a blob from a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
git hash - object[-t&lt;type&gt;][-w][--path = &lt;file&gt; | --no - filters][--stdin[--literally]][--]&lt;file&gt;... git hash - object[-t&lt;type&gt;][-w]-- stdin - paths[--no - filters]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Computes the object ID value for an object with specified type with the contents of the named file (which can be outside of the work tree), and optionally writes the resulting object into the object database. Reports its object ID to its standard output. When &lt;type&gt; is not specified, it defaults to &quot;blob&quot;.</p>
<h2>OPTIONS</h2>
<p> -t &lt;type&gt;</p>
<dl>
<dt>
<dd> Specify the type (default: &quot;blob&quot;).</dl>
<p> -w</p>
<dl>
<dt>
<dd> Actually write the object into the object database.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Read the object from standard input instead of from a file.</dl>
<p> &#8211;stdin-paths</p>
<dl>
<dt>
<dd> Read file names from the standard input, one per line, instead of from the command-line.</dl>
<p> &#8211;path</p>
<dl>
<dt>
<dd> Hash object as it were located at the given path. The location of file does not directly influence on the hash value, but path is used to determine what Git filters should be applied to the object before it can be placed to the object database, and, as result of applying filters, the actual blob put into the object database may differ from the given file. This option is mainly useful for hashing temporary files located outside of the working directory or files read from stdin.</dl>
<p> &#8211;no-filters</p>
<dl>
<dt>
<dd> Hash the contents as is, ignoring any input filter that would have been chosen by the attributes mechanism, including the end-of-line conversion. If the file is read from standard input then this is always implied, unless the <code>&#8211;path</code> option is given.</dl>
<p> &#8211;literally</p>
<dl>
<dt>
<dd> Allow <code>&#8211;stdin</code> to hash any garbage into a loose object which might not otherwise pass standard object parsing or git-fsck checks. Useful for stress-testing Git itself or reproducing characteristics of corrupt or bogus objects encountered in the wild.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
