---
title: "hid-replay(1)"
name: "hid-replay"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hid-replay/"
description: "hid-replay – HID Input device replay through uhid."
---

<h2 class="name">NAME</h2>
<p> hid-replay &#8211; HID Input device replay through uhid. </p>
<h2>SYNOPSIS</h2>
<p> <code>hid-replay</code> [OPTIONS] [FILENAME]</p>
<h2>OPTIONS</h2>
<p> <code>-i, &#8211;interactive</code></p>
<dl>
<dt>
<dd> <i>interactive</i> mode: This is the default mode. The device is created and the program wait for the user to hit <i>enter</i>. Once the <i>enter</i> key is pressed the whole events sequence in FILENAME is played in real time. Once it is done, the program loops back to the wait of the user keypress on the <i>enter</i> key. </p>
<dl>
<dt>
<dd>
<pre>
Hit *Ctrl-C* to stop the replay.
</pre>
</dl>
</dl>
<p> <code>-1, &#8211;one</code></p>
<dl>
<dt>
<dd> <i>one shot</i> mode: the device is created and then the events are replayed once in real time. The process exists at the end of the replay.</dl>
<p> <code>-s, &#8211;sleep X</code>: <i>sleep</i> X seconds once the device is created before next step. Useful in conjunction with <code>&#8211;one</code>.</p>
<h2>DESCRIPTION</h2>
<p> <code>hid-replay</code> requires the module uhid to be loaded (present in kernels 3.6+). </p>
<p> If this kernel module is loaded, <code>hid-replay</code> allows the user to create virtual HID devices as if they were physically plugged to the system. Then, the user has the possibility to replay the previously recorded HID events that are therefore handled by the right HID kernel module. </p>
<p> <code>hid-replay</code> needs to be able to write to /dev/uhid; in most cases this means it must be run as root. </p>
<p> <code>hid-recorder</code> and <code>hid-replay</code> are used to debug kernel issues with HID input devices.</p>
<h2>INPUT FILE</h2>
<p> The input file of <code>hid-replay</code> has the following syntax: </p>
<dl>
<dt>
<dd> &bull; <code>#</code> comments</dl>
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
<p> Any other starting characters are just ignored.</p>
<h2>CAUTION</h2>
<p> <code>hid-replay</code> is a very low level events injector. To have the virtual device handled by the right HID kernel module, <code>hid-replay</code> fakes that the device is on the original bus (USB, I2C or BT). Thus, if the kernel module in use has to write <i>back</i> to the device the kernel may oops if the module is trying to direclty talk to the physical layer. </p>
<p> Be sure to use this program with friendly HID modules that rely only on the generic hid callbacks.</p>
<h2>EXIT CODE</h2>
<p> <code>hid-replay</code> returns EXIT_FAILURE on error.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-hid-recorder/">hid-recorder</a>(1)</p>
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
