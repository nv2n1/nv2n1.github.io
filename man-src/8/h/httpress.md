---
title: "httpress(8)"
name: "httpress"
section: "8"
letter: "h"
url: "/docs/linux/man/8-httpress/"
description: "httpress – High performance HTTP server stress & benchmark utility."
---

<p>httpress &#8211; High performance HTTP server stress &amp; benchmark utility.</p>
<h2>Synopsis</h2>
<p><code>httpress </code> [-flag [value]]&#8230; [url] </p>
<h2>Description</h2>
<p>This is a high performance HTTP server stress &amp; benchmark utility; inspired by weighttp tool. Main features:</p>
<dl>
<dt><code>event driven</code> (low memory footprint, large number of connections)</p>
<dd>
<dt><code>multi-threaded</code> (uses all cores of your CPU)</p>
<dd>
<dt><code>SSL support</code> (via GNUTLS library) with cipher suite selection</p>
<dd>
<h2>Options</h2>
<dl>
<dt><code>-n</code> num</p>
<dd>number of requests (default: 1)</p>
<dt><code>-t</code> num</p>
<dd>number of threads (default: 1)</p>
<dt><code>-c</code> num</p>
<dd>concurrent connections (default: 1)</p>
<dt><code>-k</code></p>
<dd>keep alive (default: no)</p>
<dt><code>-q</code></p>
<dd>no progress indication (default: no)</p>
<dt><code>-z</code> pri</p>
<dd>GNUTLS cipher priority (default: NORMAL)</p>
<dt><code>-h</code></p>
<dd>show this help</dl>
<p> example: httpress <code>-n</code> 10000 <code>-c</code> 100 <code>-t</code> 4 <code>-k</code> <a rel="nofollow" href="http://localhost:8080/index.html">http://localhost:8080/index.html</a></p>
<h2>Authors</h2>
<p>Yaroslav Stavnichiy</p>
<h2>Bugs</h2>
<p>Please report issues reports to: <a rel="nofollow" href="https://bitbucket.org/yarosla/httpress/issues">https://bitbucket.org/yarosla/httpress/issues</a> </p>
