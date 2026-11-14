---
title: "grub-fstest(1)"
name: "grub-fstest"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-fstest/"
description: "grub-fstest – debug tool for GRUB filesystem drivers"
---

<h2 class="name">NAME</h2>
<p> grub-fstest &#8211; debug tool for GRUB filesystem drivers </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-fstest</code> [<i>,OPTION/</i>&#8230;] <i>,IMAGE_PATH COMMANDS/</i></p>
<h2>DESCRIPTION</h2>
<p> Debug tool for filesystem driver.</p>
<dl>
<dt>
<dd> Commands:</p>
<dt>blocklist FILE</p>
<dd> Display blocklist of FILE.</p>
<dt>cat FILE</p>
<dd> Copy FILE to standard output.</p>
<dt>cmp FILE LOCAL</p>
<dd> Compare FILE with local file LOCAL.</p>
<dt>cp FILE LOCAL</p>
<dd> Copy FILE to local file LOCAL.</p>
<dt>crc FILE</p>
<dd> Get crc32 checksum of FILE.</p>
<dt>hex FILE</p>
<dd> Show contents of FILE in hex.</p>
<dt>ls PATH</p>
<dd> List files in PATH.</p>
<dt>xnu_uuid DEVICE</p>
<dd> Compute XNU UUID of the device.</p>
<dt><code>-c</code>, <code>&#8211;diskcount</code>=<i>,NUM/</i></p>
<dd> Specify the number of input files.</p>
<dt><code>-C</code>, <code>&#8211;crypto</code></p>
<dd> Mount crypto devices.</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>,STRING/</i></p>
<dd> Set debug environment variable.</p>
<dt><code>-K</code>, <code>&#8211;zfs-key</code>=<i>,FILE/</i>|prompt</p>
<dd> Load zfs crypto key.</p>
<dt><code>-n</code>, <code>&#8211;length</code>=<i>,NUM/</i></p>
<dd> Handle N bytes in output file.</p>
<dt><code>-r</code>, <code>&#8211;root</code>=<i>,DEVICE_NAME/</i></p>
<dd> Set root device.</p>
<dt><code>-s</code>, <code>&#8211;skip</code>=<i>,NUM/</i></p>
<dd> Skip N bytes from output file.</p>
<dt><code>-u</code>, <code>&#8211;uncompress</code></p>
<dd> Uncompress data.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print verbose messages.</p>
<dt>-?, <code>&#8211;help</code></p>
<dd> give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd> give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-grub-probe/">grub-probe</a></code>(8) </p>
<p> The full documentation for <code>grub-fstest</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-fstest</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info grub-fstest</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
