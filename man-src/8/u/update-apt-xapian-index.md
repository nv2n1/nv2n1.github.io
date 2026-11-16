---
title: "update-apt-xapian-index(8)"
name: "update-apt-xapian-index"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-apt-xapian-index/"
description: "update-apt-xapian-index – rebuild the Apt Xapian Index"
---

<p>update-apt-xapian-index &#8211; rebuild the Apt Xapian Index</p>
<h2>Synopsis</h2>
<p><code>update-apt-xapian-index</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>Rebuild the Apt Xapian index</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd>show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>show this help message and exit</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd>quiet mode: only output fatal errors</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>verbose mode</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd>force database rebuild even if it&#8217;s already up to date</dd>
<dt><code>&#8211;pkgfile</code>=<i>PKGFILE</i></dt>
<dd>do not use the APT cache, but the given Package file</dd>
<dt><code>&#8211;batch-mode</code></dt>
<dd>use progress reporting suitable from programatic parsing.</dd>
<dt><code>-u</code>, <code>&#8211;update</code></dt>
<dd>incremental update, reindexing only those packages whose version has changed since the last run </dd>
</dl>
