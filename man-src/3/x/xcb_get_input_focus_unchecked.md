---
title: "xcb_get_input_focus_unchecked(3)"
name: "xcb_get_input_focus_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_get_input_focus_unchecked/"
description: "xcb_get_input_focus –"
---

<p>xcb_get_input_focus &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_get_input_focus_cookie_t xcb_get_input_focus(xcb_connection_t *conn,</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_get_input_focus_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>revert_to</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_window_t <i>focus</i>;
} <code>xcb_get_input_focus_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_get_input_focus_reply_t *<code>xcb_get_input_focus_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_get_input_focus_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_GET_INPUT_FOCUS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>revert_to</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_INPUT_FOCUS_NONE</i></dt>
<dd>The focus reverts to <i>XCB_NONE</i>, so no window will have the input focus.</dd>
<dt><i>XCB_INPUT_FOCUS_POINTER_ROOT</i></dt>
<dd>The focus reverts to <i>XCB_POINTER_ROOT</i> respectively. When the focus reverts, FocusIn and FocusOut events are generated, but the last-focus-change time is not changed.</dd>
<dt><i>XCB_INPUT_FOCUS_PARENT</i></dt>
<dd>The focus reverts to the parent (or closest viewable ancestor) and the new revert_to value is <i>XCB_INPUT_FOCUS_NONE</i>.</dd>
<dt><i>XCB_INPUT_FOCUS_FOLLOW_KEYBOARD</i></dt>
<dd>NOT YET DOCUMENTED. Only relevant for the xinput extension.</dd></dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<dt><i>focus</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_get_input_focus_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_get_input_focus_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_get_input_focus_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
