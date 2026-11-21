---

title: "axi-cache(1)"
name: "axi-cache"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axi-cache/"
description: "axi-cache – query the Apt Xapian Index"
---

<p> <code>axi-cache</code> [<i>options</i>] <i>command </i>[<i>args</i>]</p>
<p> Query the Apt Xapian index.</p>
<h3>Commands:</h3>
<dl>
<dt>
</dt><dd> search commands:</dd>
<dt>axi-cache again [query]</dt>
<dd> repeat the last search, possibly adding query terms</dd>
<dt>axi-cache help</dt>
<dd> show a summary of commands</dd>
<dt>axi-cache info</dt>
<dd> print information about the apt-xapian-index environment</dd>
<dt>axi-cache last [count]</dt>
<dd> show the last results again</dd>
<dt>axi-cache more [count]</dt>
<dd> show more terms from the last search</dd>
<dt>axi-cache rdetails pkgname[s]</dt>
<dd> show details of reverse relationships for the given packages</dd>
<dt>axi-cache search [terms]</dt>
<dd> start a new search</dd>
<dt>
</dt><dd> apt-cache front-ends:</dd>
<dt>axi-cache depends pkgname[s]</dt>
<dd> run apt-cache depends pkgname[s]</dd>
<dt>axi-cache madison pkgname[s]</dt>
<dd> run apt-cache madison pkgname[s]</dd>
<dt>axi-cache policy pkgname[s]</dt>
<dd> run apt-cache policy pkgname[s]</dd>
<dt>axi-cache rdepends pkgname[s]</dt>
<dd> run apt-cache rdepends pkgname[s]</dd>
<dt>axi-cache show pkgname[s]</dt>
<dd> run apt-cache show pkgname[s]</dd>
<dt>axi-cache showpkg pkgname[s]</dt>
<dd> run apt-cache showpkg pkgname[s]</dd>
<dt>axi-cache showsrc pkgname[s]</dt>
<dd> run apt-cache showsrc pkgname[s]</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-s</code> SORT, <code>&#8211;sort</code>=<i>SORT</i></dt>
<dd> sort by the given value, as listed in <i>/var/lib/apt-xapian-index/values</i>. Add a &#8216;-&#8216; to reverse sort order</dd>
<dt><code>&#8211;tags</code></dt>
<dd> show matching tags, rather than packages</dd>
<dt><code>&#8211;tabcomplete</code>=<i>TYPE</i></dt>
<dd> suggest words for tab completion of the current command line (type is &#8216;plain&#8217; or &#8216;partial&#8217;)</dd>
<dt><code>&#8211;last</code></dt>
<dd> use &#8216;show <code>&#8211;last</code>&#8216; to limit tab completion to only the packages from the last search results</dd>
<dt><code>&#8211;all</code></dt>
<dd> disable pagination and always show all results. Note that search results are normally sorted by relevance, so you may find meaningless results at the end of the output </dd>
</dl>
