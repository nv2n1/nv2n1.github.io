---
title: "grub2-fstest(1)"
name: "grub2-fstest"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-fstest/"
description: "grub-fstest — Debug tool for GRUB’s filesystem driver."
---

<h2>NAME</h2>
<p> <code>grub-fstest</code> — Debug tool for GRUB&#8217;s filesystem driver. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-fstest</code> [-c | &#8211;diskcount=<i>NUM</i>] [-C | &#8211;crypto]</p>
<dl>
<dt>
<dd> [-d | &#8211;debug=<i>STRING</i>] [-K | &#8211;zfs-key=<i>FILE</i>|<i>prompt</i>]</dl>
<dl>
<dt>
<dd> [-n | &#8211;length=<i>NUM</i>] [-r | &#8211;root=<i>DEVICE_NAME</i>]</dl>
<dl>
<dt>
<dd> [-s | &#8211;skip=<i>NUM</i>] [-u | &#8211;uncompress] [-v | &#8211;verbose]</dl>
<dl>
<dt>
<dd> <i>IMAGE_PATH</i> &lt;blocklist <i>FILE</i> | cat <i>FILE</i> |</dl>
<dl>
<dt>
<dd> cmp <i>FILE</i> <i>LOCAL</i> | cp <i>FILE</i> <i>LOCAL</i> | crc <i>FILE</i> |</dl>
<dl>
<dt>
<dd> hex <i>FILE</i> | ls <i>PATH</i> | xnu_uuid <i>DEVICE</i>&gt; </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-fstest</code> is a tool for testing GRUB&#8217;s filesystem drivers. You should not normally need to run this program. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;diskcount</code>=<i>NUM</i></p>
<dd> Specify the number of input files. </p>
<dt><code>&#8211;crypto</code></p>
<dd> Mount cryptographic devices. </p>
<dt><code>&#8211;debug</code>=<i>STRING</i></p>
<dd> Set debug environment variable. </p>
<dt><code>&#8211;zfs-key</code>=<i>FILE</i>|<i>prompt</i></p>
<dd> Load ZFS cryptographic key. </p>
<dt><code>&#8211;length</code>=<i>NUM</i></p>
<dd> Handle NUM bytes in output file. </p>
<dt><code>&#8211;root</code>=<i>DEVICE_NAME</i></p>
<dd> Set root device. </p>
<dt><code>&#8211;skip</code>=<i>NUM</i></p>
<dd> Skip NUM bytes from output file. </p>
<dt><code>&#8211;uncompress</code></p>
<dd> Uncompress data. </p>
<dt><code>&#8211;verbose</code></p>
<dd> Print verbose messages. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>blocklist</code> <i>FILE</i></p>
<dd> Display block list of <i>FILE</i>. </p>
<dt><code>cat</code> <i>FILE</i></p>
<dd> Display <i>FILE</i> on standard output. </p>
<dt><code>cmp</code> <i>FILE</i> <i>LOCAL</i></p>
<dd> Compare <i>FILE</i> with local file <i>LOCAL</i>. </p>
<dt><code>cp</code> <i>FILE</i> <i>LOCAL</i></p>
<dd> Copy <i>FILE</i> to local file <i>LOCAL</i>. </p>
<dt><code>crc</code> <i>FILE</i></p>
<dd> Display the CRC-32 checksum of <i>FILE</i>. </p>
<dt><code>hex</code> <i>FILE</i></p>
<dd> Display contents of <i>FILE</i> in hexidecimal. </p>
<dt><code>ls</code> <i>PATH</i></p>
<dd> List files at <i>PATH</i>. </p>
<dt><code>xnu_uuid</code> <i>DEVICE</i></p>
<dd> Display the XNU UUID of <i>DEVICE</i>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>
