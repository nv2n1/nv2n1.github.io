---
title: "fstab-decode(8)"
name: "fstab-decode"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fstab-decode/"
description: "fstab-decode – run a command with fstab-encoded arguments"
---

<p>fstab-decode &#8211; run a command with fstab-encoded arguments</p>
<h2>Synopsis</h2>
<p><code>fstab-decode</code> <i>COMMAND</i> [,<i>ARGUMENT</i> &#8230;] </p>
<h2>Description</h2>
<p><code>fstab-decode</code> decodes escapes (such as newline characters and other whitespace) in the specified <i>ARGUMENT/</i>s and uses them to run <i>COMMAND</i>. The argument escaping uses the same rules as path escaping in <code>/etc/fstab</code>, <code>/etc/mtab</code> and <code>/proc/mtab</code>. </p>
<p> In essence fstab-decode can be used anytime we want to pass multiple parameters to a command as a list of command line arguments. It turns output like this: </p>
<pre>/root
/mnt/remote-disk
/home
Into one long list of parameters, &quot;/root /mnt/remote-disk /home&quot;. This
can be useful when trying to work with multiple filesystems at once. For
instance, we can use it to unmount multiple NFS shares. This program also
removes whitespace and other characters which might cause programs such
as mount or umount to fail.</pre>
<h2>Exit Status</h2>
<p><code>fstab-decode</code> exits with status 127 if <i>COMMAND</i> can&#8217;t be run. Otherwise it exits with the status returned by <i>COMMAND</i>.</p>
<h2>Examples</h2>
<pre>The following example reads fstab, finds all instances of VFAT filesystems and
prints their mount points (argument 2 in the fstab file). fstab-decode then runs 
the specified program, umount, and passes it the list of VFAT mountpoints. 
This unmounts all VFAT partitions.
<code>fstab-decode umount $(awk '$3 == &quot;vfat&quot; { print $2 }' /etc/fstab)</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) </p>
