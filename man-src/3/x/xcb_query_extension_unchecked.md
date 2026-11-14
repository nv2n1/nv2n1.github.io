---
title: "xcb_query_extension_unchecked(3)"
name: "xcb_query_extension_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_query_extension_unchecked/"
description: "xcb_query_extension – check if extension is present"
---

<p>xcb_query_extension &#8211; check if extension is present</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_query_extension_cookie_t
    xcb_query_extension(xcb_connection_t *conn, uint16_t name_len, const char *name);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_query_extension_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint8_t <i>present</i>;
 uint8_t <i>major_opcode</i>;
 uint8_t <i>first_event</i>;
 uint8_t <i>first_error</i>;
} <code>xcb_query_extension_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_query_extension_reply_t *<code>xcb_query_extension_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_query_extension_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>name_len</i></p>
<dd>The length of <i>name</i> in bytes.</p>
<dt><i>name</i></p>
<dd>The name of the extension to query, for example &quot;RANDR&quot;. This is case sensitive!</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_QUERY_EXTENSION</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>present</i></p>
<dd>Whether the extension is present on this X11 server.</p>
<dt><i>major_opcode</i></p>
<dd>The major opcode for requests.</p>
<dt><i>first_event</i></p>
<dd>The first event code, if any.</p>
<dt><i>first_error</i></p>
<dd>The first error code, if any.</dl>
<h2>Description</h2>
<p>Determines if the specified extension is present on this X11 server. </p>
<p> Every extension has a unique <i>major_opcode</i> to identify requests, the minor opcodes and request formats are extension-specific. If the extension provides events and errors, the <i>first_event</i> and <i>first_error</i> fields in the reply are set accordingly. </p>
<p> There should rarely be a need to use this request directly, XCB provides the <i>xcb_get_extension_data</i> function instead.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_query_extension_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_query_extension_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_query_extension_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_get_extension_data/">xcb_get_extension_data</a></code>(3), <code><a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
