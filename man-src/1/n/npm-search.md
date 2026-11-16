---
title: "npm-search(1)"
name: "npm-search"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-search/"
description: "npm-search – Search for packages"
---

<h2 class="name">NAME</h2>
<p> <code>npm-search</code> &#8211; Search for packages </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre><code>
npm search[-l | --long][--json][--parseable][--no - description][search terms...] aliases : s, se, find
</code></pre>
</dd></dl>
<h3>Description</h3>
<p> Search the registry for packages matching the search terms. <code>npm search</code> performs a linear, incremental, lexically-ordered search through package metadata for all files in the registry. If color is enabled, it will further highlight the matches in the results. </p>
<p> Additionally, using the <code>&#8211;searchopts</code> and <code>&#8211;searchexclude</code> options paired with more search terms will respectively include and exclude further patterns. The main difference between <code>&#8211;searchopts</code> and the standard search terms is that the former does not highlight results in the output and can be used for more fine-grained filtering. Additionally, both of these can be added to <code>.npmrc</code> for default search filtering behavior. </p>
<p> Search also allows targeting of maintainers in search results, by prefixing their npm username with <code>=</code>. </p>
<p> If a term starts with <code>/</code>, then it&#8217;s interpreted as a regular expression and supports standard JavaScript RegExp syntax. A trailing <code>/</code> will be ignored in this case. (Note that many regular expression characters must be escaped or quoted in most shells.)</p>
<h3>A Note on caching</h3>
<h3>Configuration</h3>
<h3>description</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: true</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Used as <code>&#8211;no-description</code>, disables search matching in package descriptions and suppresses display of that field in results.</p>
<h3>json</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: false</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Output search results as a JSON array.</p>
<h3>parseable</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: false</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Output search results as lines with tab-separated columns.</p>
<h3>long</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: false</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Display full package descriptions and other long text across multiple lines. When disabled (default) search results are truncated to fit neatly on a single line. Modules with extremely long names will fall on multiple lines.</p>
<h3>searchopts</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: &quot;&quot;</dd>
<dt>&bull;</dt>
<dd> Type: String </dd>
</dl>
</dl>
<p> Space-separated options that are always passed to search.</p>
<h3>searchexclude</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: &quot;&quot;</dd>
<dt>&bull;</dt>
<dd> Type: String </dd>
</dl>
</dl>
<p> Space-separated options that limit the results from search.</p>
<h3>searchstaleness</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: 900 (15 minutes)</dd>
<dt>&bull;</dt>
<dd> Type: Number </dd>
</dl>
</dl>
<p> The age of the cache, in seconds, before another registry request is made.</p>
<h3>registry</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: <a rel="nofollow" href="https://registry.npmjs.org/">https://registry.npmjs.org/</a></dd>
<dt>&bull;</dt>
<dd> Type: url </dd>
</dl>
</dl>
<p> Search the specified registry for modules. If you have configured npm to point to a different default registry, such as your internal private module repository, <code>npm search</code> will default to that registry when searching. Pass a different registry url such as the default above in order to override this setting.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help registry</dd>
<dt>&bull;</dt>
<dd> npm help config</dd>
<dt>&bull;</dt>
<dd> npm help npmrc</dd>
<dt>&bull;</dt>
<dd> npm help view </dd>
</dl>
</dl>
<h2>Index</h2>
