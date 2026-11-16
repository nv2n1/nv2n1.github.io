---
title: "xcb_query_text_extents_unchecked(3)"
name: "xcb_query_text_extents_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_query_text_extents_unchecked/"
description: "xcb_query_text_extents – get text extents"
---

<p>xcb_query_text_extents &#8211; get text extents</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
    xcb_query_text_extents_cookie_t
    xcb_query_text_extents(xcb_connection_t *conn, xcb_fontable_t font, uint32_t string_len, const xcb_char2b_t *string);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_query_text_extents_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>draw_direction</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 int16_t <i>font_ascent</i>;
 int16_t <i>font_descent</i>;
 int16_t <i>overall_ascent</i>;
 int16_t <i>overall_descent</i>;
 int32_t <i>overall_width</i>;
 int32_t <i>overall_left</i>;
 int32_t <i>overall_right</i>;
} <code>xcb_query_text_extents_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_query_text_extents_reply_t *<code>xcb_query_text_extents_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_query_text_extents_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>font</i></dt>
<dd>The <i>font</i> to calculate text extents in. You can also pass a graphics context.</dd>
<dt><i>string_len</i></dt>
<dd>The number of characters in <i>string</i>.</dd>
<dt><i>string</i></dt>
<dd>The text to get text extents for.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_QUERY_TEXT_EXTENTS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>draw_direction</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_FONT_DRAW_LEFT_TO_RIGHT</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_FONT_DRAW_RIGHT_TO_LEFT</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<dt><i>font_ascent</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>font_descent</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>overall_ascent</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>overall_descent</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>overall_width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>overall_left</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>overall_right</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<p>Query text extents from the X11 server. This request returns the bounding box of the specified 16-bit character string in the specified <i>font</i> or the font contained in the specified graphics context. </p>
<p> <i>font_ascent</i> is set to the maximum of the ascent metrics of all characters in the string. <i>font_descent</i> is set to the maximum of the descent metrics. <i>overall_width</i> is set to the sum of the character-width metrics of all characters in the string. For each character in the string, let W be the sum of the character-width metrics of all characters preceding it in the string. Let L be the left-side-bearing metric of the character plus W. Let R be the right-side-bearing metric of the character plus W. The lbearing member is set to the minimum L of all characters in the string. The rbearing member is set to the maximum R. </p>
<p> For fonts defined with linear indexing rather than 2-byte matrix indexing, each <i>xcb_char2b_t</i> structure is interpreted as a 16-bit number with byte1 as the most significant byte. If the font has no defined default character, undefined characters in the string are taken to have all zero metrics. </p>
<p> Characters with all zero metrics are ignored. If the font has no defined default_char, the undefined characters in the string are also ignored.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_query_text_extents_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_query_text_extents_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_query_text_extents_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_font_error_t</i></dt>
<dd>The specified <i>font</i> does not exist.</dd>
<dt><i>xcb_g_context_error_t</i></dt>
<dd>The specified graphics context does not exist.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
