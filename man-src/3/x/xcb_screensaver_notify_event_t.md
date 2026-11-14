---
title: "xcb_screensaver_notify_event_t(3)"
name: "xcb_screensaver_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_screensaver_notify_event_t/"
description: "xcb_screensaver_notify_event_t –"
---

<p>xcb_screensaver_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/screensaver.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_screensaver_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>state</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 xcb_window_t <i>root</i>;
 xcb_window_t <i>window</i>;
 uint8_t <i>kind</i>;
 uint8_t <i>forced</i>;
 uint8_t <i>pad0</i>[14];
} <code>xcb_screensaver_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_SCREENSAVER_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>state</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>root</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>window</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>kind</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>forced</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from screensaver.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
