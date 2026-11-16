---
title: "xcb_xkb_names_notify_event_t(3)"
name: "xcb_xkb_names_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_names_notify_event_t/"
description: "xcb_xkb_names_notify_event_t –"
---

<p>xcb_xkb_names_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_xkb_names_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>xkbType</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>deviceID</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>changed</i>;
 uint8_t <i>firstType</i>;
 uint8_t <i>nTypes</i>;
 uint8_t <i>firstLevelName</i>;
 uint8_t <i>nLevelNames</i>;
 uint8_t <i>pad1</i>;
 uint8_t <i>nRadioGroups</i>;
 uint8_t <i>nKeyAliases</i>;
 uint8_t <i>changedGroupNames</i>;
 uint16_t <i>changedVirtualMods</i>;
 xcb_keycode_t <i>firstKey</i>;
 uint8_t <i>nKeys</i>;
 uint32_t <i>changedIndicators</i>;
 uint8_t <i>pad2</i>[4];
} <code>xcb_xkb_names_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_XKB_NAMES_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>xkbType</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>time</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>deviceID</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>changed</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstType</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nTypes</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstLevelName</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nLevelNames</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nRadioGroups</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nKeyAliases</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>changedGroupNames</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>changedVirtualMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstKey</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nKeys</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>changedIndicators</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
