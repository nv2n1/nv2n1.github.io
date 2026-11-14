---
title: "ne_version_match(3)"
name: "ne_version_match"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_version_match/"
description: "ne_version_match, ne_version_string – library versioning"
---

<p>ne_version_match, ne_version_string &#8211; library versioning</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_utils.h&gt;

int ne_version_match(int major, int minor);

const char *ne_version_string(void);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_version_match</code> function returns non-zero if the library version is not of major version <i>major</i>, or the minor version is less than <i>minor</i>. For neon versions 0.x, every minor version is assumed to be incompatible with every other minor version. </p>
<p> The <code>ne_version_string</code> function returns a string giving the library version.</p>
<h2>Examples</h2>
<p>To require neon 1.x, version 1.2 or later: </p>
<pre><code>if (ne_version_match(1, 2)) {
    printf(&quot;Library version out of date: 1.2 required, found %s.&quot;,
           ne_version_string());
    exit(1);
}</code></pre>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
