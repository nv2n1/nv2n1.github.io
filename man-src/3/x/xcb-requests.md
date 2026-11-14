---
title: "xcb-requests(3)"
name: "xcb-requests"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb-requests/"
description: "xcb-requests – about request manpages"
---

<p>xcb-requests &#8211; about request manpages</p>
<h2>Description</h2>
<p>Every request in X11, like <i>MapWindow</i>, corresponds to a number of functions and data structures in XCB. For <i>MapWindow</i>, XCB provides the function <i>xcb_map_window</i>, which fills the <i>xcb_map_window_request_t</i> data structure and writes that to the X11 connection. Since the <i>MapWindow</i> request does not have a reply, this is the most simple case. </p>
<h2>Replies</h2>
<p>Many requests have replies. For each reply, XCB provides at least a corresponding data structure and a function to return a pointer to a filled data structure. Let&#8217;s take the <i>InternAtom</i> request as an example: XCB provides the <i>xcb_intern_atom_reply_t</i> data structure and <i>xcb_intern_atom_reply</i> function. For replies which are more complex (for example lists, such as in <i>xcb_list_fonts</i>), accessor functions are provided.</p>
<h2>Cookies</h2>
<p>XCB returns a cookie for each request you send. This is an XCB-specific data structure containing the sequence number with which the request was sent to the X11 server. To get any reply, you have to provide that cookie (so that XCB knows which of the waiting replies you want). Here is an example to illustrate the use of cookies: </p>
<pre>void my_example(xcb_connection *conn) {
 xcb_intern_atom_cookie_t cookie;
 xcb_intern_atom_reply_t *reply;
 cookie = xcb_intern_atom(conn, 0, strlen(&quot;_NET_WM_NAME&quot;), &quot;_NET_WM_NAME&quot;);
 /* ... do other work here if possible ... */
 if ((reply = xcb_intern_atom_reply(conn, cookie, NULL))) {
 printf(&quot;The _NET_WM_NAME atom has ID %u
&quot;, reply-&gt;atom);
 }
 free(reply);
}</pre>
<h2>Checked Vs. Unchecked</h2>
<p>The checked and unchecked suffixes for functions determine which kind of error handling is used for this specific request. </p>
<p> For requests which have no reply (for example <i>xcb_map_window</i>), errors will be delivered to the event loop (you will receive an X11 event of type 0 when calling <i>xcb_poll_for_event</i>). If you want to explicitly check for errors in a blocking fashion, call the _checked version of the function (for example <i>xcb_map_window_checked</i>) and use <i>xcb_request_check</i>. </p>
<p> For requests which have a reply (for example <i>xcb_intern_atom</i>), errors will be checked when calling the reply function. To get errors in the event loop instead, use the _unchecked version of the function (for example <i>xcb_intern_atom_unchecked</i>). </p>
<p> Here is an example which illustrates the four different ways of handling errors: </p>
<pre>/*
 * Request without a reply, handling errors in the event loop (default)
 *
 */
void my_example(xcb_connection *conn, xcb_window_t window) {
 /* This is a request without a reply. Errors will be delivered to the event
 * loop. Getting an error to xcb_map_window most likely is a bug in our
 * program, so we don't need to check for that in a blocking way. */
 xcb_map_window(conn, window);
 /* ... of course your event loop would not be in the same function ... */
 while ((event = xcb_wait_for_event(conn)) != NULL) {
 if (event-&gt;response_type == 0) {
 fprintf(&quot;Received X11 error %d
&quot;, error-&gt;error_code);
 free(event);
 continue;
 }
 /* ... handle a normal event ... */
 }
}
/*
 * Request without a reply, handling errors directly
 *
 */
void my_example(xcb_connection *conn, xcb_window_t deco, xcb_window_t window) {
 /* A reparenting window manager wants to know whether a new window was
 * successfully reparented. If not (because the window got destroyed
 * already, for example), it does not make sense to map an empty window
 * decoration at all, so we need to know this right now. */
 xcb_void_cookie_t cookie = xcb_reparent_window_checked(conn, window,
 deco, 0, 0);
 xcb_generic_error_t *error;
 if ((error = xcb_request_check(conn, cookie))) {
 fprintf(stderr, &quot;Could not reparent the window
&quot;);
 free(error);
 return;
 }
 /* ... do window manager stuff here ... */
}
/*
 * Request with a reply, handling errors directly (default)
 *
 */
void my_example(xcb_connection *conn, xcb_window_t window) {
 xcb_intern_atom_cookie_t cookie;
 xcb_intern_atom_reply_t *reply;
 xcb_generic_error_t *error;
 cookie = xcb_intern_atom(c, 0, strlen(&quot;_NET_WM_NAME&quot;), &quot;_NET_WM_NAME&quot;);
 /* ... do other work here if possible ... */
 if ((reply = xcb_intern_atom_reply(c, cookie, &amp;error))) {
 printf(&quot;The _NET_WM_NAME atom has ID %u
&quot;, reply-&gt;atom);
 free(reply);
 } else {
 fprintf(stderr, &quot;X11 Error %d
&quot;, error-&gt;error_code);
 free(error);
 }
}
/*
 * Request with a reply, handling errors in the event loop
 *
 */
void my_example(xcb_connection *conn, xcb_window_t window) {
 xcb_intern_atom_cookie_t cookie;
 xcb_intern_atom_reply_t *reply;
 cookie = xcb_intern_atom_unchecked(c, 0, strlen(&quot;_NET_WM_NAME&quot;),
 &quot;_NET_WM_NAME&quot;);
 /* ... do other work here if possible ... */
 if ((reply = xcb_intern_atom_reply(c, cookie, NULL))) {
 printf(&quot;The _NET_WM_NAME atom has ID %u
&quot;, reply-&gt;atom);
 free(reply);
 }
 /* ... of course your event loop would not be in the same function ... */
 while ((event = xcb_wait_for_event(conn)) != NULL) {
 if (event-&gt;response_type == 0) {
 fprintf(&quot;Received X11 error %d
&quot;, error-&gt;error_code);
 free(event);
 continue;
 }
 /* ... handle a normal event ... */
 }
}</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_map_window/">xcb_map_window</a></code>(3), <code><a href="/docs/linux/man/3-xcb_intern_atom/">xcb_intern_atom</a></code>(3), <code><a href="/docs/linux/man/3-xcb_list_fonts/">xcb_list_fonts</a></code>(3), <code><a href="/docs/linux/man/3-xcb_poll_for_event/">xcb_poll_for_event</a></code>(3), <code><a href="/docs/linux/man/3-xcb_request_check/">xcb_request_check</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Stapelberg &lt;michael+xcb at stapelberg dot de&gt;</p>
