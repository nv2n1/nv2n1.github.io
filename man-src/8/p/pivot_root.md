---
title: "pivot_root(8)"
name: "pivot_root"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pivot_root/"
description: "pivot_root – change the root filesystem"
---

<p>pivot_root &#8211; change the root filesystem</p>
<h2>Synopsis</h2>
<p><code>pivot_root</code> <i>new_root</i> <i>put_old</i></p>
<h2>Description</h2>
<p><code>pivot_root</code> moves the root file system of the current process to the directory <i>put_old</i> and makes <i>new_root</i> the new root file system. Since <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8) simply calls <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2), we refer to the man page of the latter for further details. </p>
<p> Note that, depending on the implementation of <code>pivot_root</code>, root and current working directory of the caller may or may not change. The following is a sequence for invoking <code>pivot_root</code> that works in either case, assuming that <code>pivot_root</code> and <code>chroot</code> are in the current <code>PATH</code>: </p>
<dl>
<dd>
<pre>cd new_root
pivot_root . put_old
exec chroot . command</pre>
</dl>
<p> Note that <code>chroot</code> must be available under the old root and under the new root, because <code>pivot_root</code> may or may not have implicitly changed the root directory of the shell. </p>
<p> Note that <code>exec chroot</code> changes the running executable, which is necessary if the old root directory should be unmounted afterwards. Also note that standard input, output, and error may still point to a device on the old root file system, keeping it busy. They can easily be changed when invoking <code>chroot</code> (see below; note the absence of leading slashes to make it work whether <code>pivot_root</code> has changed the shell&#8217;s root or not).</p>
<h2>Options</h2>
<p><code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Example</h2>
<p>Change the root file system to <i>/dev/hda1</i> from an interactive shell: </p>
<dl>
<dd>
<pre>mount /dev/hda1 /new-root
cd /new-root
pivot_root . old-root
exec chroot . sh &lt;dev/console &gt;dev/console 2&gt;&amp;1
umount /old-root</pre>
</dl>
<p> Mount the new root file system over NFS from 10.0.0.1:/my_root and run <code>init</code>: </p>
<dl>
<dd>
<pre>ifconfig lo 127.0.0.1 up # for portmap
# configure Ethernet or such
portmap # for lockd (implicitly started by mount)
mount -o ro 10.0.0.1:/my_root /mnt
killall portmap # portmap keeps old root busy
cd /mnt
pivot_root . old_root
exec chroot . sh -c 'umount /old_root; exec /sbin/init' \
 &lt;dev/console &gt;dev/console 2&gt;&amp;1</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1), <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-switch_root/">switch_root</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>pivot_root</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
