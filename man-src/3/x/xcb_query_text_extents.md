---
title: "xcb_query_text_extents(3)"
name: "xcb_query_text_extents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_query_text_extents/"
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
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>font</i></p>
<dd>The <i>font</i> to calculate text extents in. You can also pass a graphics context.</p>
<dt><i>string_len</i></p>
<dd>The number of characters in <i>string</i>.</p>
<dt><i>string</i></p>
<dd>The text to get text extents for.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_QUERY_TEXT_EXTENTS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
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
<dd>TODO: NOT YET DOCUMENTED.</dl>
<dt><i>font_ascent</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>font_descent</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>overall_ascent</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>overall_descent</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>overall_width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>overall_left</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>overall_right</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
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
<dt><i>xcb_font_error_t</i></p>
<dd>The specified <i>font</i> does not exist.</p>
<dt><i>xcb_g_context_error_t</i></p>
<dd>The specified graphics context does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
