---
title: "slv2_util(3)"
name: "slv2_util"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slv2_util/"
description: "Utility functions –"
---

<p>Utility functions &#8211;</p>
<h3>Functions</h3>
<pre><code>const char * slv2_uri_to_path (const char *uri)</code></pre>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>const char* slv2_uri_to_path (const char *uri)</h3>
<p>Convert a full URI (eg file://foo/bar/baz.ttl) to a local path (e.g. /foo/bar/baz.ttl). </p>
<p> Return value is shared and must not be deleted by caller. </p>
<p> <code>Returns:</code></p>
<dl>
<dd><i>uri</i> converted to a path, or NULL on failure (URI is not local).</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SLV2 from the source code.</p>
