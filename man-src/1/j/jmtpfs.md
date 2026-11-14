---
title: "jmtpfs(1)"
name: "jmtpfs"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jmtpfs/"
description: "jmtpfs – FUSE based MTP filesystem"
---

<h2>NAME</h2>
<p> jmtpfs &#8211; FUSE based MTP filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>jmtpfs</code> [OPTIONS] &lt;mountpoint&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>jmtpfs</code> is a FUSE and libmtp based filesystem for accessing MTP (Media Transfer Protocol) devices. It was specifically designed for exchanging files between Linux systems and newer Android devices that support MTP but not USB Mass Storage. </p>
<p> This manual page documents briefly the <code>jmtpfs</code> commands. </p>
<h2>OPTIONS</h2>
<h3>FUSE Options:</h3>
<dl>
<dt><code>-h</code></p>
<dd> Show fuse help options.</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-l</code> or <code>&#8211;listDevices</code></p>
<dd> list available mtp devices (busLocation, devNum, productId, vendorId, product, vendor) and then exit.</p>
<dt><code>-device=&lt;busnum&gt;,&lt;devnum&gt;</code></p>
<dd> Device to mount. If not specified the first device found is used.</p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd> Show jmtpfs and FUSE version information. </p>
</dl>
<h2>UNMOUNT DEVICE</h2>
<p> Use <code>fusermount -u &lt;mountpoint&gt;</code> to umount the device. </p>
<h2>EXAMPLE</h2>
<p> jmtpfs -o allow_other ~/transformer </p>
<p> fusermount -u ~/transformer </p>
<h2>UDEV RULES</h2>
<p> You will need to identify the device (via dmesg) and add a new rule to; /lib/udev/rules.d/51-android.rules to identify the ATTRS{idVendor} and ATTRS{idProduct} for the device. </p>
<p> Current rules are for the ASUS Transformer TF101 and Samsung GT. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2012 Jason &quot;J&quot; Ferrara <a rel="nofollow" href="http://research.jacquette.com/">http://research.jacquette.com/</a> </p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Malcolm J Lewis &lt;malcolmlewis [at] opensuse.org&gt; for the openSUSE project. </p>
<h2>Index</h2>
