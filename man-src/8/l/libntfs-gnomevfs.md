---
title: "libntfs-gnomevfs(8)"
name: "libntfs-gnomevfs"
section: "8"
letter: "l"
url: "/docs/linux/man/8-libntfs-gnomevfs/"
description: "libntfs-gnomevfs – Module for GNOME VFS that allows access to NTFS filesystems."
---

<p>libntfs-gnomevfs &#8211; Module for GNOME VFS that allows access to NTFS filesystems.</p>
<h2>Overview</h2>
<p>The GNOME virtual filesystem (VFS) provides universal access to different filesystems. The <code>libntfs-gnomevfs</code> module enables GNOME VFS aware clients to seamlessly utilize the NTFS library <code>libntfs</code>. </p>
<p> So you can access an NTFS filesystem without needing to use the NTFS utilities themselves (at least in theory anyway). In practice this is probably more useful for programs and programmers to make using <code>libntfs</code> easier, more generic, and to allow easier debugging of <code>libntfs</code>.</p>
<h2>Examples</h2>
<h3>Prerequisites</h3>
<p>To be able to follow these examples you will need to have installed the test utilities from the gnome-vfs-2.4.x package. The easiest way to do this is to download and compile the gnome-vfs-2 package, e.g. download from: <a rel="nofollow" href="http://ftp.gnome.org/pub/GNOME/desktop/2.4/2.4.0/sources/gnome-vfs-2.4.0.tar.gz">http://ftp.gnome.org/pub/GNOME/desktop/2.4/2.4.0/sources/gnome-vfs-2.4.0.tar.gz</a> Then run ./configure followed by make and make install (as root). This will install it into /usr/local so it should not conflict with your existing installation from rpm or deb packages which will be in /usr. Note you may also need to add /usr/local/lib to /etc/ld.so.conf and then run ldconfig (as root) to let your system see the installed gnome-vfs-2.4.x libraries. Then run ./configure followed by make and make install (as root) in the main <code>ntfsprogs</code> directory to build and install the <code>libntfs-gnomevfs</code> module and <code>libntfs</code> library which is used by the module.</p>
<h3>Copying a file from an NTFS partition</h3>
<p>To copy the file autoexec.bat from the main directory of an NTFS partition (/dev/hda1) to the /tmp directory on your system you could run: /path/to/gnome-vfs-2.4.x/test/test-xfer file:///dev/hda1#libntfs:/autoexec.bat /tmp/autoexec.bat To copy a file from a directory inside the NTFS partition you would just specify the full path. So for example to copy the file win.ini from the Windows directory you would run: /path/to/gnome-vfs-2.4.x/test/test-xfer file:///dev/hda1#libntfs:/Windows/win.ini /tmp/win.ini</p>
<h3>Shell access to an NTFS partition</h3>
<p>For debugging it is most useful to be able to do various things to the NTFS partition while it is being operated upon by <code>libntfs</code>. This is achieved using the test-shell utility (from the gnome-vfs-2.4.x package) by running: /path/to/gnome-vfs-2.4.x/test/test-shell This drops you into the GNOME VFS shell from where you can now cd into the NTFS partition (/dev/hda1) by typing: cd file:///dev/hda1#libntfs:/ You are now in the root directory of the NTFS partition. The first thing you will probably want to do is to type &quot;ls&quot; to display the directory contents. You could then change directories using the &quot;cd&quot; command, e.g. to enter the Windows directory you would type: cd Windows You can then open files, seek inside files, read from files (write is not enabled at present), etc thus exercising large portions of the NTFS library. Use the &quot;help&quot; command while in the shell to see the available commands. </p>
<h2>Bugs</h2>
<p>No bugs are known but there are several limitations at the moment: You cannot get information about files other than what the &quot;ls&quot; command in the test-shell can give you, i.e. the &quot;info&quot; command in the test-shell does not work. Further access to the partition is read-only and hence you cannot write to files. This will be changed in the future once the module has had more wide testing. There may be other limitations and possibly bugs. Please report any problems to the NTFS mailing list: linux-ntfs-dev [at] lists.sourceforge.net </p>
<h2>Authors</h2>
<p>The <code>libntfs-gnomevfs</code> module was written by Jan Kratochvil. This man page was written by Anton Altaparmakov.</p>
<h2>Availability</h2>
<p>The <code>ntfsprogs</code> package which contains the <code>libntfs-gnomevfs</code> module can be downloaded from <a rel="nofollow" href="http://www.linux-ntfs.org/content/view/19/37/">http://www.linux-ntfs.org/content/view/19/37/</a> <code>These</code>manual<code>pages</code>can<code>be</code>viewed<code>online</code>at<code><a rel="nofollow" href="http://man.linux-ntfs.org/ntfsprogs.8.html">http://man.linux-ntfs.org/ntfsprogs.8.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
