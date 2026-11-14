---
title: "sync-available(8)"
name: "sync-available"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sync-available/"
description: "sync-available – sync dpkg’s available database with apt’s database"
---

<p>sync-available &#8211; sync dpkg&#8217;s available database with apt&#8217;s database</p>
<h2>Synopsis</h2>
<p><code>sync-available</code> </p>
<p> <code>sync-available &#8211;version</code> </p>
<p> <code>sync-available &#8211;help</code></p>
<h2>Description</h2>
<p>This program updates the <code><a href="/docs/linux/man/8-dpkg/">dpkg</a></code>(8) <i>available</i> database with the data in the <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) package database. This is required for <code><a href="/docs/linux/man/1-grep-available/">grep-available</a></code>(1) and other similar programs to give up-to-date results. </p>
<p> The same functionality is available through <code><a href="/docs/linux/man/8-dselect/">dselect</a></code>(8), when it is configured to use <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8) as its acquisition method. However, this program does not require that <code><a href="/docs/linux/man/8-dselect/">dselect</a></code>(8) is installed.</p>
<h2>Exit Status</h2>
<p>The program exits with status code <code>0</code> if all went well, and a non-zero status code otherwise.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</p>
<dd>Output the name and version of the program onto standard output stream.</p>
<dt>&#8211;help</p>
<dd>Give a brief usage statement on the standard output stream.</dl>
<p> </code></p>
<h2>Environment</h2>
<dl>
<dt><code>TMPDIR</p>
<dd>The name of the directory where temporary files are created. Default is </code><i>/tmp</i>.</dl>
<h2>Author</h2>
<p>The program and this manual page were written by Antti-Juhani Kaijanaho &lt;ajk [at] debian.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-grep-available/">grep-available</a></code>(1), <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8), <code><a href="/docs/linux/man/8-dpkg/">dpkg</a></code>(8), <code><a href="/docs/linux/man/8-dselect/">dselect</a></code>(8) </p>
