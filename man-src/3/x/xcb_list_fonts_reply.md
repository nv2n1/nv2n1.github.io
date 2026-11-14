---
title: "xcb_list_fonts_reply(3)"
name: "xcb_list_fonts_reply"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_list_fonts_reply/"
description: "xcb_list_fonts – get matching font names"
---

<p>xcb_list_fonts &#8211; get matching font names</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_list_fonts_cookie_t
    xcb_list_fonts(xcb_connection_t *conn, uint16_t max_names, uint16_t pattern_len, const char *pattern);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_list_fonts_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>names_len</i>;
 uint8_t <i>pad1</i>[22];
} <code>xcb_list_fonts_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_list_fonts_reply_t *<code>xcb_list_fonts_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_list_fonts_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>int <code>xcb_list_fonts_names_length</code>(const xcb_list_fonts_reply_t *<i>reply</i>);</p>
<dd>xcb_str_iterator_t <code>xcb_list_fonts_names_iterator</code>(const xcb_list_fonts_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>max_names</i></p>
<dd>The maximum number of fonts to be returned.</p>
<dt><i>pattern_len</i></p>
<dd>The length (in bytes) of <i>pattern</i>.</p>
<dt><i>pattern</i></p>
<dd>A font pattern, for example &quot;-misc-fixed-*&quot;. </p>
<p> The asterisk (*) is a wildcard for any number of characters. The question mark (?) is a wildcard for a single character. Use of uppercase or lowercase does not matter.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_LIST_FONTS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>names_len</i></p>
<dd>The number of font names.</dl>
<h2>Description</h2>
<p>Gets a list of available font names which match the given <i>pattern</i>.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_list_fonts_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_list_fonts_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_list_fonts_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
