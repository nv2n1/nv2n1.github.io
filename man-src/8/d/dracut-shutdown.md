---
title: "dracut-shutdown(8)"
name: "dracut-shutdown"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dracut-shutdown/"
description: "dracut-shutdown.service – unpack the initramfs to /run/initramfs"
---

<p>dracut-shutdown.service &#8211; unpack the initramfs to /run/initramfs</p>
<h2>Synopsis</h2>
<p>dracut-shutdown.service</p>
<h2>Description</h2>
<p>This service unpacks the initramfs image to /run/initramfs. systemd pivots into /run/initramfs at shutdown, so the root filesytem can be safely unmounted. </p>
<p> The following steps are executed during a shutdown: </p>
<dl>
<dd>&bull; systemd switches to the shutdown.target</dl>
<dl>
<dd>&bull; systemd starts /lib/systemd/system/shutdown.target.wants/dracut-shutdown.service</dl>
<dl>
<dd>&bull; dracut-shutdown.service executes /usr/lib/dracut/dracut-initramfs-restore which unpacks the initramfs to /run/initramfs</dl>
<dl>
<dd>&bull; systemd finishes shutdown.target</dl>
<dl>
<dd>&bull; systemd kills all processes</dl>
<dl>
<dd>&bull; systemd tries to unmount everything and mounts the remaining read-only</dl>
<dl>
<dd>&bull; systemd checks, if there is a /run/initramfs/shutdown executable</dl>
<dl>
<dd>&bull; if yes, it does a pivot_root to /run/initramfs and executes ./shutdown. The old root is then mounted on /oldroot. /usr/lib/dracut/modules.d/99shutdown/shutdown.sh is the shutdown executable.</dl>
<dl>
<dd>&bull; shutdown will try to umount every /oldroot mount and calls the various shutdown hooks from the dracut modules</dl>
<p> This ensures, that all devices are disassembled and unmounted cleanly. </p>
<p> To debug the shutdown process, you can get a shell in the shutdown procedure by injecting &quot;rd.break=pre-shutdown rd.shell&quot; or &quot;rd.break=shutdown rd.shell&quot;. </p>
<dl>
<dd>
<pre># mkdir -p /run/initramfs/etc/cmdline.d
# echo &quot;rd.break=pre-shutdown rd.shell&quot; &gt; /run/initramfs/etc/cmdline.d/debug.conf
# touch /run/initramfs/.need_shutdown</pre>
</dl>
<h2>Authors</h2>
<p>Harald Hoyer</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>
