---
title: "usb_state_string(9)"
name: "usb_state_string"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_state_string/"
---

usb_state_string - Returns human readable name for the state.

<h2>Synopsis</h2>

<pre><code>const char *usb_state_string(enum usb_device_state state);</code></pre>

<h2>Arguments</h2>

<i>state</i>
<dl><dd><dd>The state to return a human-readable name for. If it's not any of the states devices in usb_device_state_string enum, the string UNKNOWN will be returned.</dl>

<h2>Copyright</h2>


