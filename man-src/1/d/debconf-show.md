---
title: "debconf-show(1)"
name: "debconf-show"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-show/"
description: "debconf-show – query the debconf database"
---

<h2 class="name">NAME</h2>
<p> debconf-show &#8211; query the debconf database </p>
<h2>SYNOPSIS</h2>
<pre><code>
debconf - show packagename[...][--db = dbname] debconf - show-- listowners[--db = dbname] debconf - show-- listdbs
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>debconf-show</code> lets you query the debconf database in different ways. </p>
<p> The most common use is &#8220;debconf-show packagename&#8221;, which displays all items in the debconf database owned by a given package, and their current values. Questions that have been asked already are prefixed with an &#8216;*&#8217;. </p>
<p> This can be useful as a debugging aid, and especially handy in bug reports involving a package&#8217;s use of debconf.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;db=</code><i>dbname</i></p>
<dd> Specify the database to query. By default, debconf-show queries the main database.</p>
<dt><code>&#8211;listowners</code></p>
<dd> Lists all owners of questions in the database. Generally an owner is equivalent to a debian package name.</p>
<dt><code>&#8211;listdbs</code></p>
<dd> Lists all available databases.</dl>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; and Sylvain Ferriol </p>
<h2>Index</h2>
