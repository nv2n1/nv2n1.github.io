---
title: "xcb_query_font_char_infos_iterator(3)"
name: "xcb_query_font_char_infos_iterator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_query_font_char_infos_iterator/"
description: "xcb_query_font – query font metrics"
---

<p>xcb_query_font &#8211; query font metrics</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_query_font_cookie_t xcb_query_font(xcb_connection_t *conn, xcb_fontable_t font);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_query_font_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_charinfo_t <i>min_bounds</i>;
 uint8_t <i>pad1</i>[4];
 xcb_charinfo_t <i>max_bounds</i>;
 uint8_t <i>pad2</i>[4];
 uint16_t <i>min_char_or_byte2</i>;
 uint16_t <i>max_char_or_byte2</i>;
 uint16_t <i>default_char</i>;
 uint16_t <i>properties_len</i>;
 uint8_t <i>draw_direction</i>;
 uint8_t <i>min_byte1</i>;
 uint8_t <i>max_byte1</i>;
 uint8_t <i>all_chars_exist</i>;
 int16_t <i>font_ascent</i>;
 int16_t <i>font_descent</i>;
 uint32_t <i>char_infos_len</i>;
} <code>xcb_query_font_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_query_font_reply_t *<code>xcb_query_font_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_query_font_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_fontprop_t *<code>xcb_query_font_properties</code>(const xcb_query_font_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_query_font_properties_length</code>(const xcb_query_font_reply_t *<i>reply</i>);</p>
<dd>xcb_fontprop_iterator_t <code>xcb_query_font_properties_iterator</code>(const xcb_query_font_reply_t *<i>reply</i>);</p>
<dd>xcb_charinfo_t *<code>xcb_query_font_char_infos</code>(const xcb_query_font_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_query_font_char_infos_length</code>(const xcb_query_font_reply_t *<i>reply</i>);</p>
<dd>xcb_charinfo_iterator_t <code>xcb_query_font_char_infos_iterator</code>(const xcb_query_font_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>font</i></p>
<dd>The fontable (Font or Graphics Context) to query.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_QUERY_FONT</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>min_bounds</i></p>
<dd>minimum bounds over all existing char</p>
<dt><i>max_bounds</i></p>
<dd>maximum bounds over all existing char</p>
<dt><i>min_char_or_byte2</i></p>
<dd>first character</p>
<dt><i>max_char_or_byte2</i></p>
<dd>last character</p>
<dt><i>default_char</i></p>
<dd>char to print for undefined character</p>
<dt><i>properties_len</i></p>
<dd>how many properties there are</p>
<dt><i>draw_direction</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_FONT_DRAW_LEFT_TO_RIGHT</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_FONT_DRAW_RIGHT_TO_LEFT</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>min_byte1</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>max_byte1</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>all_chars_exist</i></p>
<dd>flag if all characters have nonzero size</p>
<dt><i>font_ascent</i></p>
<dd>baseline to top edge of raster</p>
<dt><i>font_descent</i></p>
<dd>baseline to bottom edge of raster</p>
<dt><i>char_infos_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<p>Queries information associated with the font.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_query_font_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_query_font_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_query_font_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
