---
title: "xkbfreecomponentlist(3)"
name: "xkbfreecomponentlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreecomponentlist/"
description: "XkbFreeComponentList – Free the structure returned by XkbListComponents"
---

<p>XkbFreeComponentList &#8211; Free the structure returned by <i>XkbListComponents</i> </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeComponentList</code> <code>(XkbComponentListPtr </code><i>list</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; list</i></p>
<dd>
<dd>pointer to XkbComponentListRec to free</dl>
<h2>Description</h2>
<p>When you are done using the structure returned by <i>XkbListComponents, </i> free it using <i>XkbFreeComponentList.</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkblistcomponents/">XkbListComponents</a></code>(3)</p>
