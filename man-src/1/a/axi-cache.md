---
title: "axi-cache(1)"
name: "axi-cache"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axi-cache/"
description: "axi-cache – query the Apt Xapian Index"
---

<h2 class="name">NAME</h2>
<p> axi-cache &#8211; query the Apt Xapian Index </p>
<h2>SYNOPSIS</h2>
<p> <code>axi-cache</code> [<i>options</i>] <i>command </i>[<i>args</i>]</p>
<h2>DESCRIPTION</h2>
<p> Query the Apt Xapian index.</p>
<h3>Commands:</h3>
<dl>
<dt>
<dd> search commands:</p>
<dt>axi-cache again [query]</p>
<dd> repeat the last search, possibly adding query terms</p>
<dt>axi-cache help</p>
<dd> show a summary of commands</p>
<dt>axi-cache info</p>
<dd> print information about the apt-xapian-index environment</p>
<dt>axi-cache last [count]</p>
<dd> show the last results again</p>
<dt>axi-cache more [count]</p>
<dd> show more terms from the last search</p>
<dt>axi-cache rdetails pkgname[s]</p>
<dd> show details of reverse relationships for the given packages</p>
<dt>axi-cache search [terms]</p>
<dd> start a new search</p>
<dt>
<dd> apt-cache front-ends:</p>
<dt>axi-cache depends pkgname[s]</p>
<dd> run apt-cache depends pkgname[s]</p>
<dt>axi-cache madison pkgname[s]</p>
<dd> run apt-cache madison pkgname[s]</p>
<dt>axi-cache policy pkgname[s]</p>
<dd> run apt-cache policy pkgname[s]</p>
<dt>axi-cache rdepends pkgname[s]</p>
<dd> run apt-cache rdepends pkgname[s]</p>
<dt>axi-cache show pkgname[s]</p>
<dd> run apt-cache show pkgname[s]</p>
<dt>axi-cache showpkg pkgname[s]</p>
<dd> run apt-cache showpkg pkgname[s]</p>
<dt>axi-cache showsrc pkgname[s]</p>
<dd> run apt-cache showsrc pkgname[s]</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-s</code> SORT, <code>&#8211;sort</code>=<i>SORT</i></p>
<dd> sort by the given value, as listed in <i>/var/lib/apt-xapian-index/values</i>. Add a &#8216;-&#8216; to reverse sort order</p>
<dt><code>&#8211;tags</code></p>
<dd> show matching tags, rather than packages</p>
<dt><code>&#8211;tabcomplete</code>=<i>TYPE</i></p>
<dd> suggest words for tab completion of the current command line (type is &#8216;plain&#8217; or &#8216;partial&#8217;)</p>
<dt><code>&#8211;last</code></p>
<dd> use &#8216;show <code>&#8211;last</code>&#8216; to limit tab completion to only the packages from the last search results</p>
<dt><code>&#8211;all</code></p>
<dd> disable pagination and always show all results. Note that search results are normally sorted by relevance, so you may find meaningless results at the end of the output </p>
</dl>
<h2>Index</h2>
