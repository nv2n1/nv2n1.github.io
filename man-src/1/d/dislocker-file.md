---
title: "dislocker-file(1)"
name: "dislocker-file"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dislocker-file/"
description: "Dislocker file – Read BitLocker encrypted volumes under Linux, OSX and FreeBSD."
---

<h2>NAME</h2>
<p> Dislocker file &#8211; Read BitLocker encrypted volumes under Linux, OSX and FreeBSD.</p>
<h2>SYNOPSIS</h2>
<p> dislocker-file [-hqrsv] [-l <i>LOG_FILE</i>] [-O <i>OFFSET</i>] [-V <i>VOLUME</i> <i>DECRYPTMETHOD</i> -F[<i>N</i>]] [&#8211;] <i>NTFS_FILE</i> </p>
<p> Where DECRYPTMETHOD = {-p[<i>RECOVERY_PASSWORD</i>] | -f <i>BEK_FILE</i> | -u[<i>USER_PASSWORD</i>] | -k <i>FVEK_FILE</i> | -c}</p>
<h2>DESCRIPTION</h2>
<p> Given a decryption mean, the program is used to decrypt BitLocker encrypted volumes. </p>
<p> This process may take a very long time, depending on the initial volume size, as the program will decrypt the encrypted partition linearly. About this size, note that the created NTFS file will be of the same size as the BitLocker encrypted partition, so you may want to check that you have enough free space on the volume where you put the NTFS file. </p>
<p> This NTFS file won&#8217;t have any link with the original BitLocker encrypted partition, so you may modify it to suit your needs.</p>
<h2>OPTIONS</h2>
<p> For program&#8217;s options description, see <a href="/docs/linux/man/1-dislocker-fuse/">dislocker-fuse</a>(1). The only change in the command line is the last argument, which in this case is the <i>NTFS_FILE</i> argument: </p>
<p> <code>NTFS_FILE</code> the newly created file where NTFS data will be put to, once decrypted from the BitLocker encrypted volume.</p>
<h2>EXAMPLES</h2>
<p> These are examples you can run directly. </p>
<p> Dislock the BitLocker encrypted volume:</p>
<dl>
<dt>
<dd> <code>% dislocker -V /dev/sda2 -p563200-557084-108284-218900-019151-415437-694144-239976 &#8212; decrypted.ntfs</code></p>
<dt>
<dd> This will decrypt <code>/dev/sda2</code> into <code>decrypted.ntfs</code> using the recovery password method.</p>
<dt>To mount the partition once decrypted, use this sort of line:</p>
<dd> <code>% mount -o loop decrypted.ntfs /mnt/clear</code></dl>
<p> &#8212;</p>
<dl>
<dt>You may have to unmount the NTFS partition before halting the system. In order to do so, you may run this command (replacing your mount point):</p>
<dd> <code>% umount /mnt/clear</code></dl>
<p> &#8212; </p>
<p> Note that these are <code>examples</code> and, as such, you may need to modify the given command lines. For example, you may want to change the decryption method used in them.</p>
<h2>AUTHOR</h2>
<p> This tool is developed by Romain Coltel on behalf of HSC (<code><a rel="nofollow" href="http://www.hsc.fr/">http://www.hsc.fr/</a></code>) </p>
<p> Feel free to send bugs report to &lt;dislocker __AT__ hsc __DOT__ fr&gt; </p>
<h2>Index</h2>
