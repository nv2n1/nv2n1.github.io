---
title: "ffado-dice-firmware(1)"
name: "ffado-dice-firmware"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffado-dice-firmware/"
description: "ffado-dice-firmware – firmware download application for DICE-based devices"
---

<h2>NAME</h2>
<p> ffado-dice-firmware &#8211; firmware download application for DICE-based devices</p>
<h2>SYNOPSIS</h2>
<p> <code>ffado-dice-firmware [OPTION&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ffado-dice-firmware</code> permits firmware updates to be made to DICE-based devices under Linux. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display brief usage information and exit</dd>
<dt><code>-p, &#8211;port=NUM</code></dt>
<dd> Specify use of IEEE1394 port <i>NUM</i></dd>
<dt><code>-v, &#8211;verbose=LEVEL</code></dt>
<dd> Produce verbose output. The higher the <i>LEVEL</i> the more verbose the messages. The some verbose messages may only be available of FFADO was compiled with debugging enabled.</dd>
<dt><code>-d, &#8211;delete=IMAGENAME</code></dt>
<dd> Delete image by name.</dd>
<dt><code>-e, &#8211;dump=FILENAME</code></dt>
<dd> Extract current DICE device flash contents into file <i>FILENAME</i></dd>
<dt><code>-f, &#8211;flash=FILENAME</code></dt>
<dd> Write firmware file <i>FILENAME</i> to DICE device.</dd>
<dt><code>-i, &#8211;image-info</code></dt>
<dd> Show detailed information about each image within the firmware on the device.</dd>
<dt><code>-m, &#8211;flash-info</code></dt>
<dd> Show information about the flash memory on the device.</dd>
<dt><code>-s, &#8211;dice-info</code></dt>
<dd> Show DICE image vendor and product information.</dd>
<dt><code>-t, &#8211;test OPERATION</code></dt>
<dd> Invoke a test/debug operation. Possible <i>OPERATIONs</i> are 1 (POKE, write to address) and 2 (PEEK, read from address). Refer to the source code for further information.</dd>
<dt><code>-n, &#8211;node NODE</code></dt>
<dd> Specify the node to operate on. </dd>
</dl>
<h2>NOTES</h2>
<p> Manipulating firmware can cause your device to stop working. The FFADO project accepts no responsibility if this occurs as a result of using this tool. </p>
<h2>Index</h2>
