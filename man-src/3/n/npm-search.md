---
title: "npm-search(3)"
name: "npm-search"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-search/"
description: "npm-search — Search for packages"
---

<p><code>npm-search</code> &#8212; Search for packages</p>
<h2>Synopsis</h2>
<pre>npm.commands.search(searchTerms, [silent,] [staleness,] callback)</pre>
<h2>Description</h2>
<p>Search the registry for packages matching the search terms. The available parameters are:</p>
<dl>
<dt>&bull;</p>
<dd>searchTerms: Array of search terms. These terms are case-insensitive.</p>
<dt>&bull;</p>
<dd>silent: If true, npm will not log anything to the console.</p>
<dt>&bull;</p>
<dd>staleness: This is the threshold for stale packages. &quot;Fresh&quot; packages are not refreshed from the registry. This value is measured in seconds.</p>
<dt>&bull;</p>
<dd>callback: Returns an object where each key is the name of a package, and the value is information about that package along with a &#8216;words&#8217; property, which is a space-delimited string of all of the interesting words in that package. The only properties included are those that are searched, which generally include:</p>
<dt>&bull;</p>
<dd>name</p>
<dt>&bull;</p>
<dd>description</p>
<dt>&bull;</p>
<dd>maintainers</p>
<dt>&bull;</p>
<dd>url</p>
<dt>&bull;</p>
<dd>keywords</p>
<dd> A search on the registry excludes any result that does not match all of the search terms. It also removes any items from the results that contain an excluded term (the &quot;searchexclude&quot; config). The search is case insensitive and doesn&#8217;t try to read your mind (it doesn&#8217;t do any verb tense matching or the like). </p>
