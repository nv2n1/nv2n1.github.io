---
title: "vbetool(1)"
name: "vbetool"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vbetool/"
description: "vbetool – run real-mode video BIOS code to alter hardware state"
---

<h2>NAME</h2>
<p> vbetool &#8211; run real-mode video BIOS code to alter hardware state </p>
<h2>SYNOPSIS</h2>
<p> <code>vbetool [[vbestate save|restore]|[vbemode set|get]|[vgamode]|[dpms on|off|standby|suspend|reduced]|[post [romfile]]|[vgastate on|off]|[vbefp panelid|panelsize|getbrightness|setbrightness|invert]]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>vbetool</code> uses lrmi in order to run code from the video BIOS. Currently, it is able to alter DPMS states, save/restore video card state and attempt to initialize the video card from scratch. </p>
<h2>OPTIONS</h2>
<p> <code>vbetool</code> takes the following options:</p>
<dl>
<dt>vbestate</p>
<dd> <code>vbetool</code> will use the VESA 0x4f0f extensions to save or restore hardware state. This will be sent to or read from stdin. This information is highly hardware specific &#8211; do not attempt to restore state saved from a different machine. This command will not work unless you are at a text console, as it interferes badly with X. </p>
<dt>dpms</p>
<dd> <code>vbetool</code> will use the VESA 0x4f10 extensions to alter the power management state of your screen. &quot;On&quot;, &quot;off&quot;, &quot;standby&quot;, &quot;suspend&quot; and &quot;reduced&quot; are acceptable further options and determine which state will be activated. </p>
<dt>vbemode</p>
<dd> <code>vbetool</code> will get or set the current VESA mode. &quot;get&quot; will return the current mode number on stdout &#8211; &quot;set&quot; will set the mode to the next argument. </p>
<dt>vgamode</p>
<dd> <code>vbetool</code> will set the legacy VGA mode to the following numeric argument. </p>
<dt>post</p>
<dd> <code>vbetool</code> will attempt to run BIOS code located at c000:0003. This is the code run by the system BIOS at boot in order to intialise the video hardware. Note that on some machines (especially laptops), not all of this code is present after system boot &#8211; as a result, executing this command may result in undefined behaviour. This command must be run from a text console, as it will otherwise interfere with the operation of X. This command takes an optional argument which is the location of a file containing a ROM image. If provided, this image will be mapped to the c000 segment and used instead of the system&#8217;s video BIOS. </p>
<dt>vgastate</p>
<dd> <code>vbetool</code> will enable or disable the current video card. On most hardware, disabling will cause the hardware to stop responding until it is reenabled. You probably don&#8217;t want to do this if you&#8217;re using a framebuffer. </p>
<dt>vbefp</p>
<dd> <code>vbetool</code> will execute a VESA flat panel interface call.</p>
<dt>
<dd> panelid will provide information about the panel</p>
<dt>
<dd> panelsize will provide the size of the panel</p>
<dt>
<dd> getbrightness will provide the current screen brightness as an integer</p>
<dt>
<dd> setbrightness accepts an integer as an argument and will set the screen brightness to that</p>
<dt>
<dd> invert will invert the colours of the screen </p>
</dl>
<h2>BUGS</h2>
<p> Switching dpms modes may interact badly with X on some systems. </p>
<p> The vbestate command may behave in strange ways. </p>
<p> The post command may result in the execution of arbitrary code that happens to be lying around in the area where chunks of your video BIOS used to be. </p>
<p> The VESA specification does not require that &quot;vbemode get&quot; provides the correct mode if the current mode was set via some means other than the VESA BIOS extensions. </p>
<p> The VESA flat panel interface ceased development at the proposal stage. panelid and panelsize will work on many machines, but the other arguments are unlikely to be implemented on available hardware. </p>
<h2>AUTHOR</h2>
<p> vbetool was written by Matthew Garrett &lt;mjg59 [at] srcf.ucam.org&gt;, based on code from read-edid by John Fremlin &lt;john [at] fremlin.de&gt;, LRMI (<a rel="nofollow" href="http://sourceforge.net/projects/lrmi/)">http://sourceforge.net/projects/lrmi/)</a> and XFree (<a rel="nofollow" href="http://www.xfree86.org">http://www.xfree86.org</a>). It is released under the terms of the GNU General Public License. </p>
<h2>Index</h2>
