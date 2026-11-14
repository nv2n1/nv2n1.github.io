---
title: "mkdumprd(8)"
name: "mkdumprd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkdumprd/"
description: "mkdumprd – creates initial ramdisk images for kdump crash recovery"
---

<p>mkdumprd &#8211; creates initial ramdisk images for kdump crash recovery</p>
<h2>Synopsis</h2>
<p><code>mkdumprd</code> [OPTION] </p>
<h2>Description</h2>
<p><code>mkdumprd</code> creates an initial ram file system for use in conjunction with the booting of a kernel within the kdump framework for crash recovery. <code>mkdumprds</code> purpose is to create an initial ram filesystem capable of copying the crashed systems vmcore image to a location specified in <i>/etc/kdump.conf </i><code>mkdumprd</code> interrogates the running system to understand what modules need to be loaded in the initramfs (based on configuration retrieved from <i>/etc/kdump.conf)</i> <code>mkdumprd</code> add a new <code>dracut</code> module 99kdumpbase and use <code>dracut</code> utility to generate the initramfs. <code>mkdumprd</code> was not intended for casual use outside of the service initialization script for the kdump utility, and should not be run manually. If you require a custom kdump initramfs image, it is suggested that you use the kdump service infrastructure to create one, and then manually unpack, modify and repack the image. </p>
<h2>Options</h2>
<dl>
<dt>All options here are passed to dracut directly, please refer <code>dracut</code> docs</p>
<dd>for the info. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>
