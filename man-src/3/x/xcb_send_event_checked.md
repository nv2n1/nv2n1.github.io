---
title: "xcb_send_event_checked(3)"
name: "xcb_send_event_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_send_event_checked/"
description: "xcb_send_event – send an event"
---

<p>xcb_send_event &#8211; send an event</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_send_event(xcb_connection_t *conn, uint8_t propagate, xcb_window_t destination, uint32_t event_mask, const char *event);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>propagate</i></p>
<dd>If <i>propagate</i> is true and no clients have selected any event on <i>destination</i>, the destination is replaced with the closest ancestor of <i>destination</i> for which some client has selected a type in <i>event_mask</i> and for which no intervening window has that type in its do-not-propagate-mask. If no such window exists or if the window is an ancestor of the focus window and <i>InputFocus</i> was originally specified as the destination, the event is not sent to any clients. Otherwise, the event is reported to every client selecting on the final destination any of the types specified in <i>event_mask</i>.</p>
<dt><i>destination</i></p>
<dd>The window to send this event to. Every client which selects any event within <i>event_mask</i> on <i>destination</i> will get the event. </p>
<p> The special value <i>XCB_SEND_EVENT_DEST_POINTER_WINDOW</i> refers to the window that contains the mouse pointer. </p>
<p> The special value <i>XCB_SEND_EVENT_DEST_ITEM_FOCUS</i> refers to the window which has the keyboard focus.</p>
<dt><i>event_mask</i></p>
<dd>Event_mask for determining which clients should receive the specified event. See <i>destination</i> and <i>propagate</i>.</p>
<dt><i>event</i></p>
<dd>The event to send to the specified <i>destination</i>.</dl>
<h2>Description</h2>
<p>Identifies the <i>destination</i> window, determines which clients should receive the specified event and ignores any active grabs. </p>
<p> The <i>event</i> must be one of the core events or an event defined by an extension, so that the X server can correctly byte-swap the contents as necessary. The contents of <i>event</i> are otherwise unaltered and unchecked except for the <i>send_event</i> field which is forced to &#8216;true&#8217;.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_send_event_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_value_error_t</i></p>
<dd>The given <i>event</i> is neither a core event nor an event defined by an extension.</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>destination</i> window does not exist.</dl>
<h2>Example</h2>
<pre><code>/*
 * Tell the given window that it was configured to a size of 800x600 pixels.
 *
 */
void my_example(xcb_connection_t *conn, xcb_window_t window)
{
    /* Every X11 event is 32 bytes long. Therefore, XCB will copy 32 bytes.
     * In order to properly initialize these bytes, we allocate 32 bytes even
     * though we only need less for an xcb_configure_notify_event_t */
    xcb_configure_notify_event_t *event = calloc(32, 1);

    event-&gt;event = window;
    event-&gt;window = window;
    event-&gt;response_type = XCB_CONFIGURE_NOTIFY;

    event-&gt;x = 0;
    event-&gt;y = 0;
    event-&gt;width = 800;
    event-&gt;height = 600;

    event-&gt;border_width = 0;
    event-&gt;above_sibling = XCB_NONE;
    event-&gt;override_redirect = false;

    xcb_send_event(conn, false, window, XCB_EVENT_MASK_STRUCTURE_NOTIFY,
                   (char *)event);
    xcb_flush(conn);
    free(event);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3), <code><a href="/docs/linux/man/3-xcb_configure_notify_event_t/">xcb_configure_notify_event_t</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
