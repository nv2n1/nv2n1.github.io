---
title: "hwinfo(8)"
name: "hwinfo"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hwinfo/"
description: "hwinfo – probe for hardware"
---

<p>hwinfo &#8211; probe for hardware</p>
<h2>Synopsis</h2>
<p><code>hwinfo [</code> <i>OPTIONS</i> <code>]</code></p>
<h2>Description</h2>
<p><code>hwinfo</code> is used to probe for the hardware present in the system. It can be used to generate a system overview log which can be later used for support.</p>
<h2>Options</h2>
<p>Note that running <code>hwinfo</code> without any options is roughly equivalent to &#8216;hwinfo &#8211;all &#8211;log=-&#8216;.</p>
<dl>
<dt><code>&#8211;&lt;</code>HARDWARE_ITEM<code>&gt;</code></p>
<dd>This option can be given more than once. Probe for a particular <i>HARDWARE_ITEM</i>. Available hardware items are: </p>
<p> all, arch, bios, block, bluetooth, braille, bridge, camera, cdrom, chipcard, cpu, disk, dsl, dvb, fingerprint, floppy, framebuffer, gfxcard, hub, ide, isapnp, isdn, joystick, keyboard, memory, modem, monitor, mouse, netcard, network, partition, pci, pcmcia, pcmcia-ctrl, pppoe, printer, redasd, reallyall, scanner, scsi, smp, sound, storage-ctrl, sys, tape, tv, uml, usb, usb-ctrl, vbe, wlan, xen, zip</p>
<dt><code>&#8211;short</code></p>
<dd>Show only a summary. Use this option in addition to a hardware probing option.</p>
<dt><code>&#8211;listmd</code></p>
<dd>Normally hwinfo does not report RAID devices. Add this option to see them.</p>
<dt><code>&#8211;only </code><i>DEVNAME</i></p>
<dd>This option can be given more than once. If you add this option, only data about devices with <i>DEVNAME</i> will be shown.</p>
<dt><code>&#8211;save-config </code><i>SPEC</i></p>
<dd>Store config for a particular device below /var/lib/hardware. <i>SPEC</i> can be a device name, an UDI, or &#8216;all&#8217;. This option must be given in addition to a hardware probing option.</p>
<dt><code>&#8211;show-config </code><i>UDI</i></p>
<dd>Show saved config data for a particular device.</p>
<dt><code>&#8211;map</code></p>
<dd>If disk names have changed (e.g. after a kernel update) this prints a list of disk name mappings. Note that you must have used &#8211;save-config at some point before for this can work.</p>
<dt><code>&#8211;debug </code><i>N</i></p>
<dd>Set debug level to <i>N</i>. The debug info is shown only in the log file. If you specify a log file, the debug level is implicitly set to a reasonable value.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Increase verbosity. Only together with &#8211;map.</p>
<dt><code>&#8211;log </code><i>FILE</i></p>
<dd>Write log info to <i>FILE</i>.</p>
<dt><code>&#8211;dump-db </code><i>N</i></p>
<dd>Dump hardware data base. <i>N</i> is either 0 for the external data base in /var/lib/hardware, or 1 for the internal data base.</p>
<dt><code>&#8211;version</code></p>
<dd>Print libhd version.</p>
<dt><code>&#8211;help</code></p>
<dd>Print usage.</dl>
<h2>Environment</h2>
<p><code>hwprobe</code> can hold a comma-separated list of probing flags preceded by &#8216;+&#8217; or &#8216;-&#8216; to be turned on or off. To get a complete list of supported flags, run &#8216;hwinfo -all&#8217; (note: not &#8216;&#8211;all&#8217;) and look at the top of the output. </p>
<p> hwinfo also looks at /proc/cmdline for a <code>hwprobe</code> option.</p>
<h2>Examples</h2>
<dl>
<dt>&#8211; show all disks</p>
<dd>hwinfo &#8211;disk</p>
<dt>&#8211; just an overview</p>
<dd>hwinfo &#8211;short &#8211;block</p>
<dt>&#8211; show a particular disk</p>
<dd>hwinfo &#8211;disk &#8211;only /dev/sdb</p>
<dt>&#8211; save disk config state</p>
<dd>hwinfo &#8211;disk &#8211;save-config=all</p>
<dt>&#8211; try 4 graphics card ports for monitor data (default: 3)</p>
<dd>hwprobe=bios.ddc.ports=4 hwinfo &#8211;monitor</p>
<dt>&#8211; monitor detection runs the Video BIOS to get the monitor data; dump a complete BIOS code execution trace to the log</p>
<dd>hwprobe=bios.ddc.ports=1,x86emu=trace:dump:trace.only=0:dump.only=0 hwinfo &#8211;monitor &#8211;log=foo</dl>
<h2>Files</h2>
<dl>
<dt><code>/var/lib/hardware/hd.ids</code></p>
<dd>External hardware data base (in readable text form). Try the &#8211;dump-db option to see the format.</p>
<dt><code>/var/lib/hardware/udi</code></p>
<dd>Directory where persistent config data are stored (see &#8211;save-config option).</dl>
<h2>Bugs</h2>
<p>Not all hardware can be detected.</p>
<h2>See Also</h2>
<p>More documentation in /usr/share/doc/packages/hwinfo.<br />
 Source repository: <a href="git://git.opensuse.org/projects/hwinfo.git.">git://git.opensuse.org/projects/hwinfo.git.</a> </p>
