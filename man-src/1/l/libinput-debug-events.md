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
<dt><code>&#8211;device </code><i>/dev/input/event0</i></dt>
<dd> Use the given device(s) with the path backend. The <code>&#8211;device</code> argument may be omitted.</dd>
<dt><code>&#8211;grab</code></dt>
<dd> Exclusively grab all opened devices. This will prevent events from being delivered to the host system.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print help</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Only print libinput messages, don&#8217;t print anything from this tool. This is useful in combination with &#8211;verbose for internal state debugging.</dd>
<dt><code>&#8211;show-keycodes</code></dt>
<dd> Key events shown by this tool are partially obfuscated to avoid passwords and other sensitive information showing up in the output. Use the <code>&#8211;show-keycodes</code> argument to make all keycodes visible.</dd>
<dt><code>&#8211;udev </code><i>&lt;seat&gt;</i></dt>
<dd> Use the udev backend to listen for device notifications on the given seat. The default behavior is equivalent to &#8211;udev &quot;seat0&quot;.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Use verbose output</dd></dl>
<h3>libinput configuration options</h3>
<dl>
<dt><code>&#8211;apply-to=pattern</code></dt>
<dd> Configuration options are only applied where the device name matches the pattern. This pattern has no effect on the <code>&#8211;disable-sendevents</code> option.</dd>
<dt><code>&#8211;disable-sendevents=pattern</code></dt>
<dd> Set the send-events option to disabled for the devices matching patterns. This option is not affected by the <code>&#8211;apply-to=&quot;pattern&quot;</code> option.</dd>
<dt><code>&#8211;enable-tap|&#8211;disable-tap</code></dt>
<dd> Enable or disable tap-to-click</dd>
<dt><code>&#8211;enable-drag|&#8211;disable-drag</code></dt>
<dd> Enable or disable tap-and-drag</dd>
<dt><code>&#8211;enable-drag-lock|&#8211;disable-drag-lock</code></dt>
<dd> Enable or disable drag-lock</dd>
<dt><code>&#8211;enable-natural-scrolling|&#8211;disable-natural-scrolling</code></dt>
<dd> Enable or disable natural scrolling</dd>
<dt><code>&#8211;enable-left-handed|&#8211;disable-left-handed</code></dt>
<dd> Enable or disable left handed button configuration</dd>
<dt><code>&#8211;enable-middlebutton|&#8211;disable-middlebutton</code></dt>
<dd> Enable or disable middle button emulation</dd>
<dt><code>&#8211;enable-dwt|&#8211;disable-dwt</code></dt>
<dd> Enable or disable disable-while-typing</dd>
<dt><code>&#8211;enable-scroll-button-lock|&#8211;disable-scroll-button-lock</code></dt>
<dd> Enable or disable the scroll button lock</dd>
<dt><code>&#8211;set-click-method=[none|clickfinger|buttonareas]</code></dt>
<dd> Set the desired click method</dd>
<dt><code>&#8211;set-scroll-method=[none|twofinger|edge|button]</code></dt>
<dd> Set the desired scroll method</dd>
<dt><code>&#8211;set-scroll-button=BTN_MIDDLE</code></dt>
<dd> Set the button to the given button code</dd>
<dt><code>&#8211;set-profile=[adaptive|flat]</code></dt>
<dd> Set pointer acceleration profile</dd>
<dt><code>&#8211;set-speed=&lt;value&gt;</code></dt>
<dd> Set pointer acceleration speed. The allowed range is [-1, 1].</dd>
<dt><code>&#8211;set-tap-map=[lrm|lmr]</code></dt>
<dd> Set button mapping for tapping</dd></dl>
<h2>NOTES</h2>
<p> Events shown by this tool may not correspond to the events seen by a different user of libinput. This tool initializes a separate context.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
