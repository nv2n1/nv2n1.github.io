---
title: "xmtab(3)"
name: "xmtab"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtab/"
description: "XmTab — Data type for a tab stop"
---

<p><code>XmTab</code> &#8212; Data type for a tab stop</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
XmTab</pre>
<h2>Description</h2>
<p><code>XmTab</code> is a data structure that specifies a tab stop to be used in rendering an <code>XmString</code> containing tab components. An <code>XmTab</code> value contains a value, a unit type, an offset model (either <code>XmABSOLUTE</code> or <code>XmRELATIVE</code>), an alignment model (<code>XmALIGNMENT_BEGINNING</code>), and a decimal point character. The resource file syntax for <code>XmTab</code> is specified in the <code>XmTabList</code> reference page.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtabcreate/">XmTabCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmtabfree/">XmTabFree</a></code>(3), <code><a href="/docs/linux/man/3-xmtabgetvalues/">XmTabGetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3), and <code><a href="/docs/linux/man/3-xmtabsetvalue/">XmTabSetValue</a></code>(3).</p>
