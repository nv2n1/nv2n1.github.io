---
title: "usb_modeswitch_dispatcher(1)"
name: "usb_modeswitch_dispatcher"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usb_modeswitch_dispatcher/"
description: "usb_modeswitch_dispatcher – Linux wrapper for usb_modeswitch (not intended for direct invocation)"
---

<h2 class="name">NAME</h2>
<p> usb_modeswitch_dispatcher &#8211; Linux wrapper for usb_modeswitch (not intended for direct invocation) </p>
<h2>SYNOPSIS</h2>
<p> <code>usb_modeswitch_dispatcher</code></p>
<h2>DESCRIPTION</h2>
<p> usb_modeswitch_dispatcher will do detailed device checking and will subsequently use the Linux-independent usb_modeswitch binary together with the selected device config file to switch the mode of certain USB devices. </p>
<p> If no drivers are taking care of the device after the mode switch, the dispatcher will try to load and bind the &quot;option&quot; serial driver to any USB interfaces with class 0xff, in order to make the device useable in case it is not recognized by that driver yet. This may or may not work. </p>
<p> This program is called by udev and is not supposed to be called directly by the user.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-usb_modeswitch/">usb_modeswitch</a>(1).</code> </p>
<h2>Index</h2>
