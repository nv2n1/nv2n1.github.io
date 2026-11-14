---
title: "grub-probe(8)"
name: "grub-probe"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grub-probe/"
description: "grub-probe – probe device information for GRUB"
---

<p>grub-probe &#8211; probe device information for GRUB</p>
<h2>Synopsis</h2>
<p><code>grub-probe</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTION/</i>]&#8230; [<i>,PATH|DEVICE/</i>]</p>
<h2>Description</h2>
<p>Probe device information for a given path (or device, if the <code>-d</code> option is given).</p>
<dl>
<dt><code>-0</code></p>
<dd>separate items in output using ASCII NUL characters</p>
<dt><code>-d</code>, <code>&#8211;device</code></p>
<dd>given argument is a system device, not a path</p>
<dt><code>-m</code>, <code>&#8211;device-map</code>=<i>,FILE/</i></p>
<dd>use FILE as the device map [default=/boot/grub/device.map]</p>
<dt><code>-t</code>, <code>&#8211;target</code>=<i>,TARGET/</i></p>
<dd>print TARGET available targets: abstraction, arc_hints, baremetal_hints, bios_hints, compatibility_hint, cryptodisk_uuid, device, disk, drive, efi_hints, fs, fs_label, fs_uuid, gpt_parttype, hints_string, ieee1275_hints, msdos_parttype, partmap, partuuid, zero_check [default=fs]</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>print verbose messages.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd>give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd>give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-grub [at] gnu.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-grub-fstest/">grub-fstest</a></code>(1) The full documentation for <code>grub-probe</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-probe</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info grub-probe</code></dl>
<p> should give you access to the complete manual. </p>
