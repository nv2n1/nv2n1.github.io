---
title: "ne_has_support(3)"
name: "ne_has_support"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_has_support/"
description: "ne_has_support – determine feature support status"
---

<p>ne_has_support &#8211; determine feature support status</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_utils.h&gt;

int ne_has_support(int feature);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_has_support</code> function can be used to determine whether a particular optional feature, given by the feature code <i>feature</i>, is supported. The following feature codes are available: </p>
<p> <code>NE_FEATURE_SSL</code></p>
<dl>
<dd>Indicates support for SSL/TLS</dl>
<p> <code>NE_FEATURE_ZLIB</code></p>
<dl>
<dd>Indicates support for compressed responses</dl>
<p> <code>NE_FEATURE_IPV6</code></p>
<dl>
<dd>Indicates support for IPv6</dl>
<p> <code>NE_FEATURE_LFS</code></p>
<dl>
<dd>Indicates support for large files</dl>
<p> <code>NE_FEATURE_SOCKS</code></p>
<dl>
<dd>Indicates support for SOCKSv5</dl>
<p> <code>NE_FEATURE_TS_SSL</code></p>
<dl>
<dd>Indicates support for thread-safe SSL initialization &#8212; see ne_sock_init</dl>
<h2>Return Value</h2>
<p><code>ne_has_support</code> returns non-zero if the given feature is supported, or zero otherwise.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-ne_version_match/">ne_version_match</a>(3), <a href="/docs/linux/man/3-ne_sock_init/">ne_sock_init</a>(3)</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
