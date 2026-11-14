---
title: "xvfreeadaptorinfo(3)"
name: "xvfreeadaptorinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvfreeadaptorinfo/"
description: "XvFreeAdaptorInfo – free adaptor information"
---

<p>XvFreeAdaptorInfo &#8211; free adaptor information</p>
<h2>Synopsis</h2>
<p><code>void XvFreeAdaptorInfo(XvAdaptorInfo *</code><i>p_adaptor_info</i><code>);</code></p>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>p_adaptor_info</i></p>
<dd>Pointer to where the adaptor information is located.</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvfreeadaptorinfo/">XvFreeAdaptorInfo</a></code>(3) frees adaptor information that was returned by <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3). The data structure used for adaptor information is defined in the reference page for <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3), <code><a href="/docs/linux/man/3-xvfreeencodinginfo/">XvFreeEncodingInfo</a></code>(3)</p>
