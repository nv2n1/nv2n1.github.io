---
title: "xkbfindoverlayforkey(3)"
name: "xkbfindoverlayforkey"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfindoverlayforkey/"
description: "XkbFindOverlayForKey – Find the alternate name by using the primary name for a key that is part of an overlay"
---

<p>XkbFindOverlayForKey &#8211; Find the alternate name by using the primary name for a key that is part of an overlay </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>char * XkbFindOverlayForKey</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>XkbSectionPtr </code><i>section</i><code>,</code> <code>char *</code><i>under</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry that contains the section</p>
<dt><i>&#8211; section</i></p>
<dd>section to be searched for matching keys</p>
<dt><i>&#8211; under</i></p>
<dd>primary name of the key to be considered</dl>
<h2>Description</h2>
<p>Keys that can generate multiple keycodes may be associated with multiple names. Such keys have a primary name and an alternate name. </p>
<p> <i>XkbFindOverlayForKey </i> uses the primary name of the key, <i>under,</i> to look up the alternate name, which it returns.</p>
