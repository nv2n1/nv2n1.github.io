---
title: "vboxsdl(1)"
name: "vboxsdl"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxsdl/"
description: "VBoxSDL – x86 virtualization solution"
---

<h2 class="name">NAME</h2>
<p> VBoxSDL &#8211; x86 virtualization solution </p>
<h2>DESCRIPTION</h2>
<p> Oracle VM VirtualBox SDL GUI version (C) 2005-2019 Oracle Corporation All rights reserved.</p>
<h3>Usage:</h3>
<dl>
<dt><code>&#8211;startvm</code> &lt;uuid|name&gt;</p>
<dd> Virtual machine to start, either UUID or name</p>
<dt><code>&#8211;separate</code></p>
<dd> Run a separate VM process or attach to a running VM</p>
<dt><code>&#8211;hda</code> &lt;file&gt;</p>
<dd> Set temporary first hard disk to file</p>
<dt><code>&#8211;fda</code> &lt;file&gt;</p>
<dd> Set temporary first floppy disk to file</p>
<dt><code>&#8211;cdrom</code> &lt;file&gt;</p>
<dd> Set temporary CDROM/DVD to file/device (&#8216;none&#8217; to unmount)</p>
<dt><code>&#8211;boot</code> &lt;a|c|d|n&gt;</p>
<dd> Set temporary boot device (a = floppy, c = 1st HD, d = DVD, n = network)</p>
<dt><code>&#8211;memory</code> &lt;size&gt;</p>
<dd> Set temporary memory size in megabytes</p>
<dt><code>&#8211;vram</code> &lt;size&gt;</p>
<dd> Set temporary size of video memory in megabytes</p>
<dt><code>&#8211;fullscreen</code></p>
<dd> Start VM in fullscreen mode</p>
<dt><code>&#8211;fullscreenresize</code></p>
<dd> Resize the guest on fullscreen</p>
<dt> <code>&#8211;fixedmode</code> &lt;w&gt; &lt;h&gt; &lt;bpp&gt; Use a fixed SDL video mode with given width, height and bits per pixel</p>
<dt><code>&#8211;nofstoggle</code></p>
<dd>
<dd>Forbid switching to/from fullscreen mode</p>
<dt><code>&#8211;noresize</code></p>
<dd> Make the SDL frame non resizable</p>
<dt><code>&#8211;nohostkey</code></p>
<dd> Disable all hostkey combinations</p>
<dt><code>&#8211;nohostkeys</code> &#8230;</p>
<dd> Disable specific hostkey combinations, see below for valid keys</p>
<dt><code>&#8211;nograbonclick</code></p>
<dd> Disable mouse/keyboard grabbing on mouse click w/o additions</p>
<dt><code>&#8211;detecthostkey</code></p>
<dd> Get the hostkey identifier and modifier state</p>
<dt> <code>&#8211;hostkey</code> &lt;key&gt; {&lt;key2&gt;} &lt;mod&gt; Set the host key to the values obtained using <code>&#8211;detecthostkey</code></p>
<dt><code>&#8211;termacpi</code></p>
<dd>
<dd>Send an ACPI power button event when closing the window</p>
<dt><code>&#8211;vrdp</code> &lt;ports&gt;</p>
<dd> Listen for VRDP connections on one of specified ports (default if not specified)</p>
<dt><code>&#8211;discardstate</code></p>
<dd> Discard saved state (if present) and revert to last snapshot (if present)</p>
<dt><code>&#8211;settingspw</code> &lt;pw&gt;</p>
<dd> Specify the settings password</p>
<dt><code>&#8211;settingspwfile</code> &lt;file&gt;</p>
<dd> Specify a file containing the settings password</p>
<dt><code>&#8211;[no]rawr0</code></p>
<dd> Enable or disable raw ring 3</p>
<dt><code>&#8211;[no]rawr3</code></p>
<dd> Enable or disable raw ring 0</p>
<dt><code>&#8211;[no]patm</code></p>
<dd> Enable or disable PATM</p>
<dt><code>&#8211;[no]csam</code></p>
<dd> Enable or disable CSAM</p>
<dt><code>&#8211;[no]hwvirtex</code></p>
<dd> Permit or deny the usage of VT-x/AMD-V</dl>
<h3>Key bindings:</h3>
<dl>
<dt>&lt;hostkey&gt; +</p>
<dd> f Switch to full screen / restore to previous view h Press ACPI power button n Take a snapshot and continue execution p Pause / resume execution q Power off r VM reset s Save state and power off</p>
<dt>&lt;del&gt;</p>
<dd> Send &lt;ctrl&gt;&lt;alt&gt;&lt;del&gt;</p>
<dt>&lt;F1&gt;&#8230;&lt;F12&gt;</p>
<dd> Send &lt;ctrl&gt;&lt;alt&gt;&lt;Fx&gt; </p>
</dl>
<h2>Index</h2>
