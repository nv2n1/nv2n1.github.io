---
title: "xcb_sync_counter_notify_event_t(3)"
name: "xcb_sync_counter_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_sync_counter_notify_event_t/"
description: "xcb_sync_counter_notify_event_t –"
---

<p>xcb_sync_counter_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/sync.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_sync_counter_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>kind</i>;
 uint16_t <i>sequence</i>;
 xcb_sync_counter_t <i>counter</i>;
 xcb_sync_int64_t <i>wait_value</i>;
 xcb_sync_int64_t <i>counter_value</i>;
 xcb_timestamp_t <i>timestamp</i>;
 uint16_t <i>count</i>;
 uint8_t <i>destroyed</i>;
 uint8_t <i>pad0</i>;
} <code>xcb_sync_counter_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_SYNC_COUNTER_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>kind</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>counter</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>wait_value</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>counter_value</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>timestamp</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>count</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>destroyed</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from sync.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
