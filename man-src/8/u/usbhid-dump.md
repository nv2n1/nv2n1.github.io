---
title: "usbhid-dump(8)"
name: "usbhid-dump"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usbhid-dump/"
description: "usbhid-dump – dump USB HID device report descriptors and streams"
---

<p>usbhid-dump &#8211; dump USB HID device report descriptors and streams</p>
<h2>Synopsis</h2>
<p><code>usbhid-dump</code> [OPTION]&#8230;</p>
<h2>Description</h2>
<p><code>usbhid-dump</code> uses <code>libusb</code> to dump report descriptors and streams from HID (human interface device) interfaces of USB devices. By default, it dumps HID interfaces of all connected USB devices, but could be limited to a subset of them, or to a single interface, using options. </p>
<p> NOTE: usbhid-dump detaches kernel drivers from the interfaces it dumps and uses them exclusively, so no other program receives the input in the meantime. The report descriptor dumping is instantaneous, but the stream dumping continues until terminated with SIGINT (^C from the terminal) or a timeout expires. </p>
<p> If you accidentally start dumping a stream from the USB keyboard you use to control the terminal, the system will stop receiving the input and you won&#8217;t be able to terminate usbhid-dump. Just stop your input and wait until the timeout expires. The stream dumping will stop, the keyboard will be reattached to the kernel driver and you will regain control. </p>
<p> The default stream dumping timeout is 60 seconds and could be changed with the -t option.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Output a help message and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Output version information and exit.</p>
<dt><code>-s, -a, &#8211;address=bus[:dev]</code></p>
<dd>Limit interfaces by bus number and device address. Both 1-255, decimal. Zeroes match any bus or device.</p>
<dt><code>-d, -m, &#8211;model=vid[:pid]</code></p>
<dd>Limit interfaces by device vendor and product IDs. Both 1-FFFF, hexadecimal. Zeroes match any vendor or product.</p>
<dt><code>-i, &#8211;interface=NUMBER</code></p>
<dd>Limit interfaces by number (0-254), decimal. 255 matches any interface.</p>
<dt><code>-e, &#8211;entity=STRING</code></p>
<dd>The entity to dump: either &quot;descriptor&quot;, &quot;stream&quot; or &quot;all&quot;. The value can be abbreviated down to one letter. The default is &quot;descriptor&quot;.</p>
<dt><code>-t, &#8211;stream-timeout=NUMBER</code></p>
<dd>Stream interrupt transfer timeout, ms. Zero means infinity. The default is 60000 (60 seconds).</p>
<dt><code>-p, &#8211;stream-paused</code></p>
<dd>Start with the stream dump output paused.</p>
<dt><code>-f, &#8211;stream-feedback</code></p>
<dd>Enable stream dumping feedback: print a dot to stderr for every transfer dumped.</dl>
<h2>Signals</h2>
<dl>
<dt><code>USR1/USR2</code></p>
<dd>Pause/resume stream dump output.</dl>
<h2>Output Format</h2>
<p><code>usbhid-dump</code> outputs dumps in chunks. Each chunk is separated by an empty line and starts with the following header line: </p>
<p> BUS:DEVICE:INTERFACE:ENTITY TIMESTAMP </p>
<p> Here, BUS, DEVICE and INTERFACE are bus, device and interface numbers respectively. ENTITY is either &quot;DESCRIPTOR&quot; or &quot;STREAM&quot;. TIMESTAMP is timestamp in seconds since epoch. </p>
<p> After the header the actual dump data follows as hex bytes. A descriptor chunk includes the whole report descriptor. Every stream chunk includes a whole report, usually, but if a report is bigger than endpoint&#8217;s wMaxPacketSize, it will span several chunks.</p>
<h2>Examples</h2>
<dl>
<dt>Dump report descriptor for a device with address 3 on bus number 2:</p>
<dd><code>usbhid-dump -a 2:3</code></p>
<dt>Dump report stream for a device with vendor ID 0x5543 and product ID 0x0005:</p>
<dd><code>usbhid-dump -m 5543:0005 -es</code></p>
<dt>Dump report descriptor from interface 1 of a device with vendor ID 0x5543:</p>
<dd><code>usbhid-dump -m 5543 -i 1 -ed</code></p>
<dt>Dump report streams from all HID interfaces of all USB devices (caution: you will lose control over the terminal if you use USB keyboard):</p>
<dd><code>usbhid-dump -es</code> </p>
<h2>Author</h2>
<p>Nikolai Kondrashov &lt;spbnick [at] gmail.com&gt;</p>
