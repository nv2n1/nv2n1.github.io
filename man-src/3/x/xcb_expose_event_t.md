---
title: "xcb_expose_event_t(3)"
name: "xcb_expose_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_expose_event_t/"
description: "xcb_expose_event_t – NOT YET DOCUMENTED"
---

<p>xcb_expose_event_t &#8211; NOT YET DOCUMENTED</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_expose_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>window</i>;
 uint16_t <i>x</i>;
 uint16_t <i>y</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 uint16_t <i>count</i>;
 uint8_t <i>pad1</i>[2];
} <code>xcb_expose_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_EXPOSE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>window</i></dt>
<dd>The exposed (damaged) window.</dd>
<dt><i>x</i></dt>
<dd>The X coordinate of the left-upper corner of the exposed rectangle, relative to the <i>window</i>&#8216;s origin.</dd>
<dt><i>y</i></dt>
<dd>The Y coordinate of the left-upper corner of the exposed rectangle, relative to the <i>window</i>&#8216;s origin.</dd>
<dt><i>width</i></dt>
<dd>The width of the exposed rectangle.</dd>
<dt><i>height</i></dt>
<dd>The height of the exposed rectangle.</dd>
<dt><i>count</i></dt>
<dd>The amount of <i>Expose</i> events following this one. Simple applications that do not want to optimize redisplay by distinguishing between subareas of its window can just ignore all Expose events with nonzero counts and perform full redisplays on events with zero counts.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code>xcb_generic_event_t</code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
