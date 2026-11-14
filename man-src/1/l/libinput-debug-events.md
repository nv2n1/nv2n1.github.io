---
title: "libinput-debug-events(1)"
name: "libinput-debug-events"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-debug-events/"
description: "libinput-debug-events – debug helper for libinput"
---

<h2 class="name">NAME</h2>
<p> libinput-debug-events &#8211; debug helper for libinput </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput debug-events </code><i>[options]</i> </p>
<p> <code>libinput debug-events </code><i>[options]</i><code> &#8211;udev </code><i>&lt;seat&gt;</i> </p>
<p> <code>libinput debug-events </code><i>[options]</i><code> [&#8211;device] </code><i>/dev/input/event0</i><code> [</code><i>/dev/input/event1</i><code>&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput debug-events</code> tool creates a libinput context and prints all events from these devices. </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;device </code><i>/dev/input/event0</i></p>
<dd> Use the given device(s) with the path backend. The <code>&#8211;device</code> argument may be omitted.</p>
<dt><code>&#8211;grab</code></p>
<dd> Exclusively grab all opened devices. This will prevent events from being delivered to the host system.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help</p>
<dt><code>&#8211;quiet</code></p>
<dd> Only print libinput messages, don&#8217;t print anything from this tool. This is useful in combination with &#8211;verbose for internal state debugging.</p>
<dt><code>&#8211;show-keycodes</code></p>
<dd> Key events shown by this tool are partially obfuscated to avoid passwords and other sensitive information showing up in the output. Use the <code>&#8211;show-keycodes</code> argument to make all keycodes visible.</p>
<dt><code>&#8211;udev </code><i>&lt;seat&gt;</i></p>
<dd> Use the udev backend to listen for device notifications on the given seat. The default behavior is equivalent to &#8211;udev &quot;seat0&quot;.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Use verbose output</dl>
<h3>libinput configuration options</h3>
<dl>
<dt><code>&#8211;apply-to=pattern</code></p>
<dd> Configuration options are only applied where the device name matches the pattern. This pattern has no effect on the <code>&#8211;disable-sendevents</code> option.</p>
<dt><code>&#8211;disable-sendevents=pattern</code></p>
<dd> Set the send-events option to disabled for the devices matching patterns. This option is not affected by the <code>&#8211;apply-to=&quot;pattern&quot;</code> option.</p>
<dt><code>&#8211;enable-tap|&#8211;disable-tap</code></p>
<dd> Enable or disable tap-to-click</p>
<dt><code>&#8211;enable-drag|&#8211;disable-drag</code></p>
<dd> Enable or disable tap-and-drag</p>
<dt><code>&#8211;enable-drag-lock|&#8211;disable-drag-lock</code></p>
<dd> Enable or disable drag-lock</p>
<dt><code>&#8211;enable-natural-scrolling|&#8211;disable-natural-scrolling</code></p>
<dd> Enable or disable natural scrolling</p>
<dt><code>&#8211;enable-left-handed|&#8211;disable-left-handed</code></p>
<dd> Enable or disable left handed button configuration</p>
<dt><code>&#8211;enable-middlebutton|&#8211;disable-middlebutton</code></p>
<dd> Enable or disable middle button emulation</p>
<dt><code>&#8211;enable-dwt|&#8211;disable-dwt</code></p>
<dd> Enable or disable disable-while-typing</p>
<dt><code>&#8211;enable-scroll-button-lock|&#8211;disable-scroll-button-lock</code></p>
<dd> Enable or disable the scroll button lock</p>
<dt><code>&#8211;set-click-method=[none|clickfinger|buttonareas]</code></p>
<dd> Set the desired click method</p>
<dt><code>&#8211;set-scroll-method=[none|twofinger|edge|button]</code></p>
<dd> Set the desired scroll method</p>
<dt><code>&#8211;set-scroll-button=BTN_MIDDLE</code></p>
<dd> Set the button to the given button code</p>
<dt><code>&#8211;set-profile=[adaptive|flat]</code></p>
<dd> Set pointer acceleration profile</p>
<dt><code>&#8211;set-speed=&lt;value&gt;</code></p>
<dd> Set pointer acceleration speed. The allowed range is [-1, 1].</p>
<dt><code>&#8211;set-tap-map=[lrm|lmr]</code></p>
<dd> Set button mapping for tapping</dl>
<h2>NOTES</h2>
<p> Events shown by this tool may not correspond to the events seen by a different user of libinput. This tool initializes a separate context.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
