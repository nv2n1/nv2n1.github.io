---
title: "xcb_query_tree_children_end(3)"
name: "xcb_query_tree_children_end"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_query_tree_children_end/"
description: "xcb_query_tree – query the window tree"
---

<p>xcb_query_tree &#8211; query the window tree</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_query_tree_cookie_t xcb_query_tree(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_query_tree_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_window_t <i>root</i>;
 xcb_window_t <i>parent</i>;
 uint16_t <i>children_len</i>;
 uint8_t <i>pad1</i>[14];
} <code>xcb_query_tree_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_query_tree_reply_t *<code>xcb_query_tree_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_query_tree_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_window_t *<code>xcb_query_tree_children</code>(const xcb_query_tree_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_query_tree_children_length</code>(const xcb_query_tree_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_query_tree_children_end</code>(const xcb_query_tree_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The <i>window</i> to query.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_QUERY_TREE</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>root</i></p>
<dd>The root window of <i>window</i>.</p>
<dt><i>parent</i></p>
<dd>The parent window of <i>window</i>.</p>
<dt><i>children_len</i></p>
<dd>The number of child windows.</dl>
<h2>Description</h2>
<p>Gets the root window ID, parent window ID and list of children windows for the specified <i>window</i>. The children are listed in bottom-to-top stacking order.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_query_tree_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_query_tree_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_query_tree_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>Example</h2>
<pre><code>/*
 * Displays the root, parent and children of the specified window.
 *
 */
void my_example(xcb_connection_t *conn, xcb_window_t window)
{
    xcb_query_tree_cookie_t cookie;
    xcb_query_tree_reply_t *reply;

    cookie = xcb_query_tree(conn, window);
    if ((reply = xcb_query_tree_reply(conn, cookie, NULL))) {
        printf(&quot;root = 0x%08x
&quot;, reply-&gt;root);
        printf(&quot;parent = 0x%08x
&quot;, reply-&gt;parent);

        xcb_window_t *children = xcb_query_tree_children(reply);
        for (int i = 0; i &lt; xcb_query_tree_children_length(reply); i++)
            printf(&quot;child window = 0x%08x
&quot;, children[i]);

        free(reply);
    }
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3), <code><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
