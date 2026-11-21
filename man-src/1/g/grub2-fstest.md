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
</dt><dd> [-d | &#8211;debug=<i>STRING</i>] [-K | &#8211;zfs-key=<i>FILE</i>|<i>prompt</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [-n | &#8211;length=<i>NUM</i>] [-r | &#8211;root=<i>DEVICE_NAME</i>]</dd></dl>
<dl>
<dt>
</dt><dd> [-s | &#8211;skip=<i>NUM</i>] [-u | &#8211;uncompress] [-v | &#8211;verbose]</dd></dl>
<dl>
<dt>
</dt><dd> <i>IMAGE_PATH</i> &lt;blocklist <i>FILE</i> | cat <i>FILE</i> |</dd></dl>
<dl>
<dt>
</dt><dd> cmp <i>FILE</i> <i>LOCAL</i> | cp <i>FILE</i> <i>LOCAL</i> | crc <i>FILE</i> |</dd></dl>
<dl>
<dt>
</dt><dd> hex <i>FILE</i> | ls <i>PATH</i> | xnu_uuid <i>DEVICE</i>&gt; </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-fstest</code> is a tool for testing GRUB&#8217;s filesystem drivers. You should not normally need to run this program. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;diskcount</code>=<i>NUM</i></dt>
<dd> Specify the number of input files. </dd>
<dt><code>&#8211;crypto</code></dt>
<dd> Mount cryptographic devices. </dd>
<dt><code>&#8211;debug</code>=<i>STRING</i></dt>
<dd> Set debug environment variable. </dd>
<dt><code>&#8211;zfs-key</code>=<i>FILE</i>|<i>prompt</i></dt>
<dd> Load ZFS cryptographic key. </dd>
<dt><code>&#8211;length</code>=<i>NUM</i></dt>
<dd> Handle NUM bytes in output file. </dd>
<dt><code>&#8211;root</code>=<i>DEVICE_NAME</i></dt>
<dd> Set root device. </dd>
<dt><code>&#8211;skip</code>=<i>NUM</i></dt>
<dd> Skip NUM bytes from output file. </dd>
<dt><code>&#8211;uncompress</code></dt>
<dd> Uncompress data. </dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Print verbose messages. </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>blocklist</code> <i>FILE</i></dt>
<dd> Display block list of <i>FILE</i>. </dd>
<dt><code>cat</code> <i>FILE</i></dt>
<dd> Display <i>FILE</i> on standard output. </dd>
<dt><code>cmp</code> <i>FILE</i> <i>LOCAL</i></dt>
<dd> Compare <i>FILE</i> with local file <i>LOCAL</i>. </dd>
<dt><code>cp</code> <i>FILE</i> <i>LOCAL</i></dt>
<dd> Copy <i>FILE</i> to local file <i>LOCAL</i>. </dd>
<dt><code>crc</code> <i>FILE</i></dt>
<dd> Display the CRC-32 checksum of <i>FILE</i>. </dd>
<dt><code>hex</code> <i>FILE</i></dt>
<dd> Display contents of <i>FILE</i> in hexidecimal. </dd>
<dt><code>ls</code> <i>PATH</i></dt>
<dd> List files at <i>PATH</i>. </dd>
<dt><code>xnu_uuid</code> <i>DEVICE</i></dt>
<dd> Display the XNU UUID of <i>DEVICE</i>. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
