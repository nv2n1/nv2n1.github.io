---
title: "lcp_crtpconf(8)"
name: "lcp_crtpconf"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lcp_crtpconf/"
description: "lcp_crtpconf – create a platform configuration measurement for v1 policies"
---

<p>lcp_crtpconf &#8211; create a platform configuration measurement for v1 policies</p>
<h2>Synopsis</h2>
<p><code>lcp_crtpconf</code> <code>-p</code> <i>PCR-index1,PCR-index2,&#8230;,PCR-indexN</i> [<code>-f</code> <i>file-name</i>] [<code>-h</code>]</p>
<h2>Description</h2>
<p><code>lcp_crtpconf</code> is used to create a platform configuration measurement. The produced platform configuration measurement will be appended to the input file in binary mode.</p>
<h2>Options</h2>
<dl>
<dt><code>-p&nbsp;<wbr></code><i>PCR-index1,PCR-index2,&#8230;,PCR-indexN</i></p>
<dd>Index values can be 0-23.</p>
<dt><code>-f&nbsp;<wbr></code><i>file-name</i></p>
<dd>File name to which the measurement is appended.</p>
<dt><code>-h</code></p>
<dd>Print out the help message</dl>
<h2>Examples</h2>
<p><code>lcp_crtpconf -p </code><i>0,1,2,3 </i><code> -f </code><i>pconf-file </i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_writepol/">lcp_writepol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpol/">lcp_crtpol</a></code>(8). </p>
