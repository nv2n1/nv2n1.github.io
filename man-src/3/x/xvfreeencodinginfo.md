---
title: "xvfreeencodinginfo(3)"
name: "xvfreeencodinginfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvfreeencodinginfo/"
description: "XvFreeEncodingInfo – free encoding information"
---

<p>XvFreeEncodingInfo &#8211; free encoding information</p>
<h2>Synopsis</h2>
<p><code>void XvFreeEncodingInfo(XvEncodingInfo *</code><i>p_encoding_info</i><code>);</code></p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>p_encoding_info</i></p>
<dd>Pointer to where the encoding information is located.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvfreeencodinginfo/">XvFreeEncodingInfo</a></code>(3) frees encoding information that was returned by <code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3). The data structure used for encoding information is defined in the reference page for <code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3)</p>
