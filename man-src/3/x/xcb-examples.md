---
title: "xcb-examples(3)"
name: "xcb-examples"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb-examples/"
description: "xcb-examples – manpage examples"
---

<p>xcb-examples &#8211; manpage examples</p>
<h2>Description</h2>
<p>Many of the XCB manpages contain example code. These examples intend to explain how to use one particular part of XCB. They almost never represent a standalone (or even useful) program &#8211; X11 programs are relatively involved and thus beyond the scope of a manpage example. </p>
<h2>Environment</h2>
<p>Every example assumes you have an <i>xcb_connection</i> and possibly other variables at hand. For illustrating how <i>xcb_get_property</i> works, you need the window of which you want to get the property, for example. To make it clear that these variables are your responsibility, these examples consist of a single function which takes the necessary variables as parameters.</p>
<h2>Flushing</h2>
<p>Flushing means calling <i>xcb_flush</i> to clear the XCB-internal write buffer and send all pending requests to the X11 server. You don&#8217;t explicitly need to flush before using a reply function (like <i>xcb_query_pointer_reply</i>), but you do need to flush before entering the event loop of your program. </p>
<p> There are only two cases when XCB flushes by itself. The first case is when its write buffer becomes full, the second case is when you are asking for the reply of a request which wasn&#8217;t flushed out yet (like <i>xcb_query_pointer_reply</i>). This last point also includes xcb_request_check(). Please note that waiting for an event does <code>NOT</code> flush. </p>
<p> Examples generally include the <i>xcb_flush</i> call where appropriate (for example after setting a property). Therefore, including these functions and calling them in your application should just work. However, you might get better results when flushing outside of the function, depending on the architecture of your program.</p>
<h2>Compilation</h2>
<p>If an example does not compile (without warnings) when using <i>-std=c99</i>, that is considered a documentation bug. Similarly, not handling errors or leaking memory is also considered a documentation bug. Please inform us about it on xcb [at] lists.freedesktop.org.</p>
<h2>Coding Style</h2>
<p>Every example uses 4 spaces for indentation. </p>
<p> Comments are in asterisks, like /* this */. </p>
<p> No line is longer than 80 characters (including indentation).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_connect/">xcb_connect</a></code>(3), <code><a href="/docs/linux/man/3-xcb_get_property/">xcb_get_property</a></code>(3), <code><a href="/docs/linux/man/3-xcb_flush/">xcb_flush</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Stapelberg &lt;michael+xcb at stapelberg dot de&gt;</p>
