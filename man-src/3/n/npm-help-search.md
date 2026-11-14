---
title: "npm-help-search(3)"
name: "npm-help-search"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-help-search/"
description: "npm-help-search — Search the help pages"
---

<p><code>npm-help-search</code> &#8212; Search the help pages</p>
<h2>Synopsis</h2>
<pre>npm.commands.helpSearch(args, [silent,] callback)</pre>
<h2>Description</h2>
<p>This command is rarely useful, but it exists in the rare case that it is. This command takes an array of search terms and returns the help pages that match in order of best match. If there is only one match, then npm displays that help section. If there are multiple results, the results are printed to the screen formatted and the array of results is returned. Each result is an object with these properties:</p>
<dl>
<dt>&bull;</p>
<dd>hits: A map of args to number of hits on that arg. For example, {&quot;npm&quot;: 3}</p>
<dt>&bull;</p>
<dd>found: Total number of unique args that matched.</p>
<dt>&bull;</p>
<dd>totalHits: Total number of hits.</p>
<dt>&bull;</p>
<dd>lines: An array of all matching lines (and some adjacent lines).</p>
<dt>&bull;</p>
<dd>file: Name of the file that matched</p>
<dd></dl>
<p> The silent parameter is not neccessary not used, but it may in the future. </p>
