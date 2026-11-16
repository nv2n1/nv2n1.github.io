---
title: "lshw(1)"
name: "lshw"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lshw/"
description: "lshw – list hardware"
---

<h2 class="name">NAME</h2>
<p> lshw &#8211; list hardware </p>
<h2>SYNOPSIS</h2>
<p> <code>lshw</code> [ <code>-version</code> ] </p>
<p> <code>lshw</code> [ <code>-help</code> ] </p>
<p> <code>lshw</code> [ <code>-X</code> ] </p>
<p> <code>lshw</code> [ <code> [ -html ] [ -short ] [ -xml ] [ -json ] [ -businfo ] </code> ] [ <code>-dump </code><i>filename</i> ] [ <code>-class </code><i>class</i><i>&#8230;</i> ] [ <code>-disable </code><i>test</i><i>&#8230;</i> ] [ <code>-enable </code><i>test</i><i>&#8230;</i> ] [ <code>-sanitize</code> ] [ <code>-numeric</code> ] [ <code>-quiet</code> ] [ <code>-notime</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lshw</code> is a small tool to extract detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc. on DMI-capable x86 or IA-64 systems and on some PowerPC machines (PowerMac G4 is known to work). </p>
<p> It currently supports DMI (x86 and IA-64 only), OpenFirmware device tree (PowerPC only), PCI/AGP, CPUID (x86), IDE/ATA/ATAPI, PCMCIA (only tested on x86), SCSI and USB. </p>
<dl>
<dt><code>-version</code></dt>
<dd> Displays the version of <code>lshw</code> and exits.</dd>
<dt><code>-help</code></dt>
<dd> Displays the available command line options and quits.</dd>
<dt><code>-X</code></dt>
<dd> Launch the X11 GUI (if available).</dd>
<dt><code>-html</code></dt>
<dd> Outputs the device tree as an HTML page.</dd>
<dt><code>-xml</code></dt>
<dd> Outputs the device tree as an XML tree.</dd>
<dt><code>-json</code></dt>
<dd> Outputs the device tree as a JSON object (JavaScript Object Notation).</dd>
<dt><code>-short</code></dt>
<dd> Outputs the device tree showing hardware paths, very much like the output of HP-UX&#8217;s <code>ioscan</code>.</dd>
<dt><code>-businfo</code></dt>
<dd> Outputs the device list showing bus information, detailing SCSI, USB, IDE and PCI addresses.</dd>
<dt><code>-dump </code><i>filename</i></dt>
<dd> Display output and dump collected information into a file (SQLite database).</dd>
<dt><code>-class </code><i>class</i></dt>
<dd> Only show the given class of hardware. <i>class</i> can be found using <code>lshw -short</code> or <code>lshw -businfo</code>.</dd>
<dt><code>-C </code><i>class</i></dt>
<dd> Alias for <code>-class</code> <i>class</i>.</dd>
<dt><code>-enable </code><i>test</i></dt>
<dd>
</dd><dt><code>-disable </code><i>test</i></dt>
<dd> Enables or disables a test. <i>test</i> can be <code>dmi</code> (for DMI/SMBIOS extensions), <code>device-tree</code> (for OpenFirmware device tree), <code>spd</code> (for memory Serial Presence Detect), <code>memory</code> (for memory-size guessing heuristics), <code>cpuinfo</code> (for kernel-reported CPU detection), <code>cpuid</code> (for CPU detection), <code>pci</code> (for PCI/AGP access), <code>isapnp</code> (for ISA PnP extensions), <code>pcmcia</code> (for PCMCIA/PCCARD), <code>ide</code> (for IDE/ATAPI), <code>usb</code> (for USB devices),<code>scsi</code> (for SCSI) or <code>network</code> (for network interfaces detection).</dd>
<dt><code>-quiet</code></dt>
<dd> Don&#8217;t display status.</dd>
<dt><code>-sanitize</code></dt>
<dd> Remove potentially sensitive information from output (IP addresses, serial numbers, etc.).</dd>
<dt><code>-numeric</code></dt>
<dd> Also display numeric IDs (for PCI and USB devices).</dd>
<dt><code>-notime</code></dt>
<dd> Exclude volatile attributes (timestamps) from output.</dd></dl>
<h2>BUGS</h2>
<p> <code>lshw</code> currently does not detect Firewire(IEEE1394) devices. </p>
<p> Not all architectures supported by GNU/Linux are fully supported (e.g. CPU detection). </p>
<p> &quot;Virtual&quot; SCSI interfaces used for SCSI emulation over IDE are not reported correctly yet.</p>
<h2>NOTES</h2>
<p> <code>lshw</code> must be run as super user or it will only report partial information.</p>
<h2>FILES</h2>
<dl>
<dt><code>/usr/local/share/pci.ids</code></dt>
<dd>
</dd><dt><code>/usr/share/pci.ids</code></dt>
<dd>
</dd><dt><code>/etc/pci.ids</code></dt>
<dd>
</dd><dt><code>/usr/share/hwdata/pci.ids</code></dt>
<dd> A list of all known PCI ID&#8217;s (vendors, devices, classes and subclasses). If compiled with zlib support, lshw will look for <i>pci.ids.gz</i> first, then for <i>pci.ids</i>.</dd>
<dt><code>/proc/bus/pci/*</code></dt>
<dd> Used to access the configuration of installed PCI buses and devices.</dd>
<dt><code>/proc/ide/*</code></dt>
<dd> Used to access the configuration of installed IDE buses and devices.</dd>
<dt><code>/proc/scsi/*, /dev/sg*</code></dt>
<dd> Used to access the configuration of installed SCSI devices.</dd>
<dt><code>/dev/cpu/*/cpuid</code></dt>
<dd> Used on x86 platforms to access CPU-specific configuration.</dd>
<dt><code>/proc/device-tree/*</code></dt>
<dd> Used on PowerPC platforms to access OpenFirmware configuration.</dd>
<dt><code>/proc/bus/usb/*</code></dt>
<dd> Used to access the configuration of installed USB buses and devices.</dd>
<dt><code>/sys/*</code></dt>
<dd> Used on 2.6 kernels to access hardware/driver configuration information.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>lshw -short</code></dt>
<dd> Lists hardware in a compact format.</dd>
<dt><code>lshw -class disk -class storage</code></dt>
<dd> Lists all disks and storage controllers in the system.</dd>
<dt><code>lshw -html -class network</code></dt>
<dd> Lists all network interfaces in HTML.</dd>
<dt><code>lshw -disable dmi</code></dt>
<dd> Don&#8217;t use DMI to detect hardware.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>/proc/*</i>, <code>linuxinfo</code>(1), <code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/8-lsusb/">lsusb</a></code>(8)</p>
<h2>COPYING</h2>
<p> <code>lshw</code> is distributed under the GNU GENERAL PUBLIC LICENSE (GPL) version 2.</p>
<h2>AUTHOR</h2>
<p> <code>lshw</code> is maintained by Lyonel Vincent &lt;lyonel [at] ezix.org&gt;.</p>
<h2>OTHER INFO</h2>
<p> The webpage for <code>lshw</code> is at<br />
&nbsp;&lt;URL:<a rel="nofollow" href="http://lshw.ezix.org/">http://lshw.ezix.org/</a>&gt; </p>
<h2>Index</h2>
