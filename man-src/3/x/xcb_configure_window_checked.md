---
title: "xcb_configure_window_checked(3)"
name: "xcb_configure_window_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_configure_window_checked/"
description: "xcb_configure_window – Configures window attributes"
---

<p>xcb_configure_window &#8211; Configures window attributes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_configure_window(xcb_connection_t *conn, xcb_window_t window, uint16_t value_mask, const void *value_list);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The window to configure.</p>
<dt><i>value_mask</i></p>
<dd>Bitmask of attributes to change.</p>
<dt><i>value_list</i></p>
<dd>New values, corresponding to the attributes in value_mask. The order has to correspond to the order of possible <i>value_mask</i> bits. See the example.</dl>
<h2>Description</h2>
<p>Configures a window&#8217;s size, position, border width and stacking order.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_configure_window_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_match_error_t</i></p>
<dd>You specified a Sibling without also specifying StackMode or the window is not actually a Sibling.</p>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified window does not exist. TODO: any other reason?</dl>
<h2>Example</h2>
<pre><code>/*
 * Configures the given window to the left upper corner
 * with a size of 1024x768 pixels.
 *
 */
void my_example(xcb_connection_t *c, xcb_window_t window)
{
    uint16_t mask = 0;

    mask |= XCB_CONFIG_WINDOW_X;
    mask |= XCB_CONFIG_WINDOW_Y;
    mask |= XCB_CONFIG_WINDOW_WIDTH;
    mask |= XCB_CONFIG_WINDOW_HEIGHT;

    const uint32_t values[] = {
        0,    /* x */
        0,    /* y */
        1024, /* width */
        768   /* height */
    };

    xcb_configure_window(c, window, mask, values);
    xcb_flush(c);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3), <code><a href="/docs/linux/man/3-xcb_expose_event_t/">xcb_expose_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_map_notify_event_t/">xcb_map_notify_event_t</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
