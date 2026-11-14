---
title: "dislocker-fuse(1)"
name: "dislocker-fuse"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dislocker-fuse/"
description: "Dislocker fuse – Read/write BitLocker encrypted volumes under Linux, OSX and FreeBSD."
---

<h2>NAME</h2>
<p> Dislocker fuse &#8211; Read/write BitLocker encrypted volumes under Linux, OSX and FreeBSD.</p>
<h2>SYNOPSIS</h2>
<p> dislocker-fuse [-hqrsv] [-l <i>LOG_FILE</i>] [-O <i>OFFSET</i>] [-V <i>VOLUME</i> <i>DECRYPTMETHOD</i> -F[<i>N</i>]] [&#8211; <i>ARGS</i>&#8230;] </p>
<p> Where DECRYPTMETHOD = {-p[<i>RECOVERY_PASSWORD</i>] | -f <i>BEK_FILE</i> | -u[<i>USER_PASSWORD</i>] | -k <i>FVEK_FILE</i> | -c}</p>
<h2>DESCRIPTION</h2>
<p> Given a decryption mean, the program is used to read or write BitLocker encrypted volumes. Technically, the program will create a virtual NTFS partition that you can mount as any other NTFS partition. </p>
<p> The virtual partition is linked to the underlying BitLocker volume, so any write to this volume is put on the BitLocker volume as well. However, you can use <a href="/docs/linux/man/1-dd/">dd</a>(1) to get rid of this limitation &#8212; if it&#8217;s a limitation for you. An example is provided in the EXAMPLES section of this man page.</p>
<h2>OPTIONS</h2>
<p> Program&#8217;s options are described below: </p>
<dl>
<dt><code>-c, &#8211;clearkey</code></p>
<dd> decrypt volume using a clear key which is searched on the volume (default)</p>
<dt><code>-f, &#8211;bekfile </code><i>BEK_FILE</i></p>
<dd> decrypt volume using the bek file (present on a USB key)</p>
<dt><code>-F, &#8211;force-block=[</code><i>N</i><code>]</code></p>
<dd> force use of metadata block number <i>N</i> (1, 2 or 3). Without <i>N</i>, the first block is forced. Without this option, the program will try each block until a valid one is found</p>
<dt><code>-h</code></p>
<dd> print the help and exit</p>
<dt><code>-k, &#8211;fvek </code><i>FVEK_FILE</i></p>
<dd> decrypt volume using the FVEK directly. See the FVEK FILE section below to understand what is to be put into this <i>FVEK_FILE</i></p>
<dt><code>-l, &#8211;logfile </code><i>LOG_FILE</i></p>
<dd> put messages into this file (stdout by default)</p>
<dt><code>-O, &#8211;offset </code><i>OFFSET</i></p>
<dd> BitLocker partition offset, in bytes, in base 10 (default is 0). Protip: in your shell, you probably can pass <code>-O $((</code><i>0xdeadbeef</i><code>))</code> if you have a 16-based number and are too lazy to convert it in another way.</p>
<dt><code>-p, &#8211;recovery-password=[</code><i>RECOVERY_PASSWORD</i><code>]</code></p>
<dd> decrypt volume using the recovery password method. If no recovery-password is provided, it will be asked afterward; this has the advantage that the program will validate each block one by one, on the fly, as you type it and not to leak the password on the commandline</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> do NOT display any information. This option has priority on any previous `<code>-v</code>&#8216;. One probably wants to check the return value of the program when using this option</p>
<dt><code>-r, &#8211;readonly</code></p>
<dd> do not allow to write on the BitLocker volume (read only mode)</p>
<dt><code>-s, &#8211;stateok</code></p>
<dd> do not check the volume&#8217;s state, assume it&#8217;s ok to mount it. Do not use this if you don&#8217;t know what you&#8217;re doing</p>
<dt><code>-u, &#8211;user-password=[</code><i>USER_PASSWORD</i><code>]</code></p>
<dd> decrypt the volume using the user password method. If no user-password is provided, it will be asked afterward; this has the advantage not to leak the password on the commandline</p>
<dt><code>-v, &#8211;verbosity</code></p>
<dd> increase verbosity (CRITICAL level by default), see also `<code>-q</code>&#8216;</p>
<dt><code>-V, &#8211;volume </code><i>VOLUME</i></p>
<dd> volume to get metadata and encrypted keys from</p>
<dt><code>&#8212;</code></p>
<dd> mark the end of program&#8217;s options and the beginning of FUSE&#8217;s ones (useful if you want to pass something like -d to FUSE)</dl>
<p> <code>ARGS</code> are any arguments you want to pass to FUSE. Note that you need to pass at least the mount-point.</p>
<h2>FVEK FILE</h2>
<dl>
<dt>The FVEK file option expects a specific format from the file. The file is split into two major parts:</p>
<dd> &#8211; 2 bytes describing the encryption in use, from 0x8000 to 0x8003 for AES 128 or 256 bits, with or without diffuser. </p>
<p> &#8211; 64 bytes (512 bits) which are the FVEK as in the FVEK key protector once decrypted.</dl>
<p> The file is therefore 66 bytes long, not more nor less. Note that you may have to deal with endianness.</p>
<h2>EXAMPLES</h2>
<p> These are examples you can run directly. First, you may want to copy the BitLocker volume:</p>
<dl>
<dt>
<dd> <code>% dd if=/dev/sda2 of=encrypted.bitlocker</code></p>
<dt>
<dd> This will copy the entire volume located into <code>/dev/sda2</code> to <code>encrypted.bitlocker</code>. You&#8217;re not forced to do this step, but this will ensure no write whatsoever is performed on the BitLocker volume.</dl>
<p> Then dislock it:</p>
<dl>
<dt>
<dd> <code>% dislocker -V encrypted.bitlocker -f /path/to/usb/file.BEK &#8212; /mnt/ntfs</code></p>
<dt>
<dd> This will create a file into <code>/mnt/ntfs</code> named dislocker-file.</p>
<dt>To mount partitions once decrypted, use this sort of line:</p>
<dd> <code>% mount -o loop /mnt/ntfs/dislocker-file /mnt/clear</code></dl>
<p> &#8212;</p>
<dl>
<dt>It seems that you have to unmount the NTFS partition and the dislocker one before halting the system, or you will run into unexpected behaviour. In order to do so, you may run these commands (replacing your mount points):</p>
<dd> <code>% umount /mnt/clear &amp;&amp; umount /mnt/ntfs/dislocker-file</code></dl>
<p> &#8212; </p>
<p> Note that these are <code>examples</code> and, as such, may need to be modified. For instance, you may want to change the decryption method used in them.</p>
<h2>AUTHOR</h2>
<p> This tool is developed by Romain Coltel on behalf of HSC (<code><a rel="nofollow" href="http://www.hsc.fr/">http://www.hsc.fr/</a></code>) </p>
<p> Feel free to send bugs report to &lt;dislocker __AT__ hsc __DOT__ fr&gt; </p>
<h2>Index</h2>
