---
title: "xkballockeyboard(3)"
name: "xkballockeyboard"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballockeyboard/"
description: "XkbAllocKeyboard – Creates a keyboard description from scratch"
---

<p>XkbAllocKeyboard &#8211; Creates a keyboard description from scratch </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbDescRec XkbAllocKeyboard</code> <code>(void);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Description</h2>
<dd>Applications seldom need to directly allocate a keyboard description; calling <i>XkbGetKeyboard </i> usually suffices. In the event you need to create a keyboard description from scratch, however, use <i>XkbAllocKeyboard </i> rather than directly calling <i>malloc.</i> </p>
<p> If <i>XkbAllocKeyboard </i> fails to allocate the keyboard description, it returns NULL. Otherwise, it returns a pointer to an empty keyboard description structure. The <i>device_spec </i> field will have been initialized to XkbUseCoreKbd. You may then either fill in the structure components or use Xkb functions to obtain values for the structure components from a keyboard device.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/3F-malloc/">malloc</a></code>(3F), <code><a href="/docs/linux/man/3-xkbusecorekbd/">XkbUseCoreKbd</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyboard/">XkbGetKeyboard</a></code>(3)</p>
