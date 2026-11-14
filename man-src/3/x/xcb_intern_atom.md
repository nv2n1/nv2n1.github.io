---
title: "xcb_intern_atom(3)"
name: "xcb_intern_atom"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_intern_atom/"
description: "xcb_intern_atom – Get atom identifier by name"
---

<p>xcb_intern_atom &#8211; Get atom identifier by name</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_intern_atom_cookie_t
    xcb_intern_atom(xcb_connection_t *conn, uint8_t only_if_exists, uint16_t name_len, const char *name);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_intern_atom_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_atom_t <i>atom</i>;
} <code>xcb_intern_atom_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_intern_atom_reply_t *<code>xcb_intern_atom_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_intern_atom_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>only_if_exists</i></p>
<dd>Return a valid atom id only if the atom already exists.</p>
<dt><i>name_len</i></p>
<dd>The length of the following <i>name</i>.</p>
<dt><i>name</i></p>
<dd>The name of the atom.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_INTERN_ATOM</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>atom</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<p>Retrieves the identifier (xcb_atom_t TODO) for the atom with the specified name. Atoms are used in protocols like EWMH, for example to store window titles (<i>_NET_WM_NAME</i> atom) as property of a window. </p>
<p> If <i>only_if_exists</i> is 0, the atom will be created if it does not already exist. If <i>only_if_exists</i> is 1, <i>XCB_ATOM_NONE</i> will be returned if the atom does not yet exist.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_intern_atom_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_intern_atom_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_intern_atom_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_alloc_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_value_error_t</i></p>
<dd>A value other than 0 or 1 was specified for <i>only_if_exists</i>.</dl>
<h2>Example</h2>
<pre><code>/*
 * Resolves the _NET_WM_NAME atom.
 *
 */
void my_example(xcb_connection_t *c)
{
    xcb_intern_atom_cookie_t cookie;
    xcb_intern_atom_reply_t *reply;

    cookie = xcb_intern_atom(c, 0, strlen(&quot;_NET_WM_NAME&quot;), &quot;_NET_WM_NAME&quot;);
    /* ... do other work here if possible ... */
    if ((reply = xcb_intern_atom_reply(c, cookie, NULL))) {
        printf(&quot;The _NET_WM_NAME atom has ID %u, reply-&gt;atom);
        free(reply);
    }
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3), <code><a href="/docs/linux/man/3-xcb_get_atom_name/">xcb_get_atom_name</a></code>(3), <code><a href="/docs/linux/man/1-xlsatoms/">xlsatoms</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
