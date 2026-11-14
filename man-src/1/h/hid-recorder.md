---
title: "hid-recorder(1)"
name: "hid-recorder"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hid-recorder/"
description: "hid-recorder – HID Input device recorder."
---

<h2 class="name">NAME</h2>
<p> hid-recorder &#8211; HID Input device recorder. </p>
<h2>SYNOPSIS</h2>
<p> <code>hid-recorder</code> </p>
<p> <code>hid-recorder</code> [OPTIONS] [/dev/hidrawX] [[/dev/hidrawY] &#8230; ]</p>
<h2>OPTIONS</h2>
<p> <code>-d, &#8211;debugfs</code></p>
<dl>
<dt>
<dd> use HID debugfs node. Some devices (like &quot;Logitech USB Receiver&quot; or &quot;Apple Magic Mouse&quot;) grabs the hidraw output leading to an empty output. Fortunately, relying on HID debugfs can help us most of the time. However, if hte device does report two many events at once (multitouch panles for example), the HID debugfs node is missing a lot of events, preventing us to make this the default behaviour.</dl>
<h2>DESCRIPTION</h2>
<p> <code>hid-recorder</code> is a tool that allow users to capture hidraw description and events in order to replay them through the uhid kernel module. </p>
<p> The first invocation type displayed above (without arguments) causes hid-recorder to let the user choose which hidraw she will use, including the name the device. </p>
<p> Several hidraw nodes can be given to <code>hid-recorder</code>. In this case, the recording of each node are multiplexed thanks to the tag <code>D:</code> as seen below. </p>
<p> <code>hid-recorder</code> needs to be able to read from the hidraw device; in most cases this means it must be run as root. </p>
<p> <code>hid-recorder</code> and <code>hid-replay</code> are used to debug kernel issues with HID input devices. The output of <code>hid-recorder</code> has the following syntax: </p>
<dl>
<dt>
<dd> &bull; <code>#</code> lines comments</dl>
<dl>
<dt>
<dd> &bull; <code>D:</code> tell which device we are currently working with</dl>
<dl>
<dt>
<dd> &bull; <code>R:</code> size dump_of_report_descriptor_in_hexadecimal</dl>
<dl>
<dt>
<dd> &bull; <code>N:</code> common_name_of_the_device</dl>
<dl>
<dt>
<dd> &bull; <code>P:</code> physical_path</dl>
<dl>
<dt>
<dd> &bull; <code>I:</code> bus vendor_id product_id</dl>
<dl>
<dt>
<dd> &bull; <code>E:</code> timestamp size report_in_hexadecimal</dl>
<h2>EXIT CODE</h2>
<p> <code>hid-recorder</code> returns EXIT_FAILURE on error.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-hid-replay/">hid-replay</a>(1)</p>
<h2>COPYRIGHT</h2>
<dl>
<dt>
<dd>
<pre>
Copyright 2012, Benjamin Tissoires.
Copyright 2012, Red Hat, Inc.
</pre>
</dl>
<h2>AUTHOR</h2>
<dl>
<dt>
<dd>
<pre>
Benjamin Tissoires &lt;benjamin.tissoires [at] redhat.com&gt;
</pre>
</dl>
<h2>Index</h2>
