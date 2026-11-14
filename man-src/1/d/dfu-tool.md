---
title: "dfu-tool(1)"
name: "dfu-tool"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dfu-tool/"
description: "dfu-tool – write firmware to DFU devices"
---

<h2 class="name">NAME</h2>
<p> dfu-tool &#8211; write firmware to DFU devices </p>
<h2>SYNOPSIS</h2>
<p> dfu-tool [CMD]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>dfu-tool</code> command. </p>
<p> <code>dfu-tool</code> allows a user to write various kinds of firmware onto devices supporting the USB Device Firmware Upgrade protocol. This tool can be used to switch the device from the normal runtime mode to `DFU mode&#8217; which allows the user to read and write firmware. Either the whole device can be written in one operation, or individual `targets&#8217; can be specified with the alternative name or number. </p>
<p> All synchronous actions can be safely cancelled and on failure will return errors with both a type and a full textual description. libdfu supports DFU 1.0, DFU 1.1 and the ST DfuSe vendor extension, and handles many device `quirks&#8217; necessary for the real-world implementations of DFU.</p>
<h2>OPTIONS</h2>
<p> The dfu-tool command takes various options depending on the action. Run <code>dfu-tool &#8211;help</code> for the full list.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fwupdtool/">fwupdtool</a>(1), <a href="/docs/linux/man/1-fwupdmgr/">fwupdmgr</a>(1)</p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Richard Hughes (richard [at] hughsie.com) </p>
<h2>Index</h2>
