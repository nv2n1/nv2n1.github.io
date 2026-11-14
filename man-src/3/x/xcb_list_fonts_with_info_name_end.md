---
title: "xcb_list_fonts_with_info_name_end(3)"
name: "xcb_list_fonts_with_info_name_end"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_list_fonts_with_info_name_end/"
description: "xcb_list_fonts_with_info – get matching font names and information"
---

<p>xcb_list_fonts_with_info &#8211; get matching font names and information</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_list_fonts_with_info_cookie_t
    xcb_list_fonts_with_info(xcb_connection_t *conn, uint16_t max_names, uint16_t pattern_len, const char *pattern);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_list_fonts_with_info_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>name_len</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_charinfo_t <i>min_bounds</i>;
 uint8_t <i>pad0</i>[4];
 xcb_charinfo_t <i>max_bounds</i>;
 uint8_t <i>pad1</i>[4];
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
 uint32_t <i>replies_hint</i>;
} <code>xcb_list_fonts_with_info_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_list_fonts_with_info_reply_t *<code>xcb_list_fonts_with_info_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_list_fonts_with_info_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_fontprop_t *<code>xcb_list_fonts_with_info_properties</code>(const xcb_list_fonts_with_info_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_list_fonts_with_info_properties_length</code>(const xcb_list_fonts_with_info_reply_t *<i>reply</i>);</p>
<dd>xcb_fontprop_iterator_t <code>xcb_list_fonts_with_info_properties_iterator</code>(const xcb_list_fonts_with_info_reply_t *<i>reply</i>);</p>
<dd>char *<code>xcb_list_fonts_with_info_name</code>(const xcb_list_fonts_with_info_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_list_fonts_with_info_name_length</code>(const xcb_list_fonts_with_info_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_list_fonts_with_info_name_end</code>(const xcb_list_fonts_with_info_reply_t *<i>reply</i>);
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
<dd>The type of this reply, in this case <i>XCB_LIST_FONTS_WITH_INFO</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>name_len</i></p>
<dd>The number of matched font names.</p>
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
<dt><i>replies_hint</i></p>
<dd>An indication of how many more fonts will be returned. This is only a hint and may be larger or smaller than the number of fonts actually returned. A zero value does not guarantee that no more fonts will be returned.</dl>
<h2>Description</h2>
<p>Gets a list of available font names which match the given <i>pattern</i>.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_list_fonts_with_info_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_list_fonts_with_info_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_list_fonts_with_info_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
