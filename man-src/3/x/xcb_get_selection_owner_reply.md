---
title: "xcb_get_selection_owner_reply(3)"
name: "xcb_get_selection_owner_reply"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_get_selection_owner_reply/"
description: "xcb_get_selection_owner – Gets the owner of a selection"
---

<p>xcb_get_selection_owner &#8211; Gets the owner of a selection</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_get_selection_owner_cookie_t xcb_get_selection_owner(xcb_connection_t *conn, xcb_atom_t selection);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_get_selection_owner_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_window_t <i>owner</i>;
} <code>xcb_get_selection_owner_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_get_selection_owner_reply_t *<code>xcb_get_selection_owner_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_get_selection_owner_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>selection</i></p>
<dd>The selection.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_GET_SELECTION_OWNER</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>owner</i></p>
<dd>The current selection owner window.</dl>
<h2>Description</h2>
<p>Gets the owner of the specified selection. </p>
<p> TODO: briefly explain what a selection is.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_get_selection_owner_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_get_selection_owner_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_get_selection_owner_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_atom_error_t</i></p>
<dd><i>selection</i> does not refer to a valid atom.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_set_selection_owner/">xcb_set_selection_owner</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
