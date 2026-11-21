---

title: "vboxsdl(1)"
name: "vboxsdl"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxsdl/"
description: "VBoxSDL – x86 virtualization solution"
---

<p> VBoxSDL &#8211; x86 virtualization solution </p>
<h2>DESCRIPTION</h2>
<p> Oracle VM VirtualBox SDL GUI version (C) 2005-2019 Oracle Corporation All rights reserved.</p>
<h3>Usage:</h3>
<dl>
<dt><code>&#8211;startvm</code> &lt;uuid|name&gt;</dt>
<dd> Virtual machine to start, either UUID or name</dd>
<dt><code>&#8211;separate</code></dt>
<dd> Run a separate VM process or attach to a running VM</dd>
<dt><code>&#8211;hda</code> &lt;file&gt;</dt>
<dd> Set temporary first hard disk to file</dd>
<dt><code>&#8211;fda</code> &lt;file&gt;</dt>
<dd> Set temporary first floppy disk to file</dd>
<dt><code>&#8211;cdrom</code> &lt;file&gt;</dt>
<dd> Set temporary CDROM/DVD to file/device (&#8216;none&#8217; to unmount)</dd>
<dt><code>&#8211;boot</code> &lt;a|c|d|n&gt;</dt>
<dd> Set temporary boot device (a = floppy, c = 1st HD, d = DVD, n = network)</dd>
<dt><code>&#8211;memory</code> &lt;size&gt;</dt>
<dd> Set temporary memory size in megabytes</dd>
<dt><code>&#8211;vram</code> &lt;size&gt;</dt>
<dd> Set temporary size of video memory in megabytes</dd>
<dt><code>&#8211;fullscreen</code></dt>
<dd> Start VM in fullscreen mode</dd>
<dt><code>&#8211;fullscreenresize</code></dt>
<dd> Resize the guest on fullscreen</dd>
<dt> <code>&#8211;fixedmode</code> &lt;w&gt; &lt;h&gt; &lt;bpp&gt; Use a fixed SDL video mode with given width, height and bits per pixel</dt>
<dt><code>&#8211;nofstoggle</code></dt>
<dd>
</dd><dd>Forbid switching to/from fullscreen mode</dd>
<dt><code>&#8211;noresize</code></dt>
<dd> Make the SDL frame non resizable</dd>
<dt><code>&#8211;nohostkey</code></dt>
<dd> Disable all hostkey combinations</dd>
<dt><code>&#8211;nohostkeys</code> &#8230;</dt>
<dd> Disable specific hostkey combinations, see below for valid keys</dd>
<dt><code>&#8211;nograbonclick</code></dt>
<dd> Disable mouse/keyboard grabbing on mouse click w/o additions</dd>
<dt><code>&#8211;detecthostkey</code></dt>
<dd> Get the hostkey identifier and modifier state</dd>
<dt> <code>&#8211;hostkey</code> &lt;key&gt; {&lt;key2&gt;} &lt;mod&gt; Set the host key to the values obtained using <code>&#8211;detecthostkey</code></dt>
<dt><code>&#8211;termacpi</code></dt>
<dd>
</dd><dd>Send an ACPI power button event when closing the window</dd>
<dt><code>&#8211;vrdp</code> &lt;ports&gt;</dt>
<dd> Listen for VRDP connections on one of specified ports (default if not specified)</dd>
<dt><code>&#8211;discardstate</code></dt>
<dd> Discard saved state (if present) and revert to last snapshot (if present)</dd>
<dt><code>&#8211;settingspw</code> &lt;pw&gt;</dt>
<dd> Specify the settings password</dd>
<dt><code>&#8211;settingspwfile</code> &lt;file&gt;</dt>
<dd> Specify a file containing the settings password</dd>
<dt><code>&#8211;[no]rawr0</code></dt>
<dd> Enable or disable raw ring 3</dd>
<dt><code>&#8211;[no]rawr3</code></dt>
<dd> Enable or disable raw ring 0</dd>
<dt><code>&#8211;[no]patm</code></dt>
<dd> Enable or disable PATM</dd>
<dt><code>&#8211;[no]csam</code></dt>
<dd> Enable or disable CSAM</dd>
<dt><code>&#8211;[no]hwvirtex</code></dt>
<dd> Permit or deny the usage of VT-x/AMD-V</dd></dl>
<h3>Key bindings:</h3>
<dl>
<dt>&lt;hostkey&gt; +</dt>
<dd> f Switch to full screen / restore to previous view h Press ACPI power button n Take a snapshot and continue execution p Pause / resume execution q Power off r VM reset s Save state and power off</dd>
<dt>&lt;del&gt;</dt>
<dd> Send &lt;ctrl&gt;&lt;alt&gt;&lt;del&gt;</dd>
<dt>&lt;F1&gt;&#8230;&lt;F12&gt;</dt>
<dd> Send &lt;ctrl&gt;&lt;alt&gt;&lt;Fx&gt; </dd>
</dl>
