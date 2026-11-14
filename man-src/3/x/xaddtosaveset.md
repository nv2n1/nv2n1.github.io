---
title: "xaddtosaveset(3)"
name: "xaddtosaveset"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xaddtosaveset/"
description: "XChangeSaveSet, XAddToSaveSet, XRemoveFromSaveSet – change a client’s save set"
---

<p>XChangeSaveSet, XAddToSaveSet, XRemoveFromSaveSet &#8211; change a client&#8217;s save set </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XChangeSaveSet(Display *<i>display</i>, Window <i>w</i>, int <i>change_mode</i>);</p>
<dd>int XAddToSaveSet(Display *<i>display</i>, Window <i>w</i>);</p>
<dd>int XRemoveFromSaveSet(Display *<i>display</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>change_mode</i></p>
<dd>Specifies the mode. You can pass <code>SetModeInsert</code> or <code>SetModeDelete</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>w</i></p>
<dd>Specifies the window that you want to add or delete from the client&#8217;s save-set.</dl>
<h2>Description</h2>
<p>Depending on the specified mode, <code>XChangeSaveSet</code> either inserts or deletes the specified window from the client&#8217;s save-set. The specified window must have been created by some other client, or a <code>BadMatch</code> error results. </p>
<p> <code>XChangeSaveSet</code> can generate <code>BadMatch</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XAddToSaveSet</code> function adds the specified window to the client&#8217;s save-set. The specified window must have been created by some other client, or a <code>BadMatch</code> error results. </p>
<p> <code>XAddToSaveSet</code> can generate <code>BadMatch</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XRemoveFromSaveSet</code> function removes the specified window from the client&#8217;s save-set. The specified window must have been created by some other client, or a <code>BadMatch</code> error results. </p>
<p> <code>XRemoveFromSaveSet</code> can generate <code>BadMatch</code> and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xreparentwindow/">XReparentWindow</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
