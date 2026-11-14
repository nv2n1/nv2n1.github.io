---
title: "zcav(8)"
name: "zcav"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zcav/"
description: "zcav – program to test raw hard drive throughput."
---

<p>zcav &#8211; program to test raw hard drive throughput. </p>
<h2>Synopsis</h2>
<p><code>zcav</code> <i>[-b block-size[:chunk-size]] [-c count] [-r [first-block]:last-block]</i> <i>[-w] [-s skip-rate] [-u uid-to-use:gid-to-use] [-g gid-to-use]</i> <i>[-l log-file] [-f] file-name</i> <i>[-l log-file [-f] file-name]&#8230;</i> </p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>zcav</code>, program. Modern hard drives have a constant rotational speed but have varying numbers of sectors per track (outside tracks are longer and have more sectors). This is referred to as Zoned Constant Angular Velocity (or ZCAV). The outer tracks will have a higher data transfer rate due to having more sectors per track, these tracks generally have the lower track/sector numbers. This program tests the ZCAV performance of a hard drive, by reading the entire data on it a specified number of times. The file name given as the first parameter, it can be specified as <code>&#8211;</code>, for standard input. This file will be opened as read-only and in usual operation it will be <code>/dev/hdX</code> or <code>/dev/ide/host0/busX/targetY/lun0/disc</code> depending on whether you use devfs or not (NB operating systems other than Linux will have different device names). The output should be able to be easily graphed with <code>gnuplot</code> which is what I use to view the results. </p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>the size (in Meg) of the blocks to read/write (default 512M), optionally followed by a &#8216;:&#8217; and the chunk size for read/write operations (default 1M). Note that the chunk size must be less than or equal to the block size and must also be significantly less than the size of the RAM in the machine. Also note that for the write test there will be a fsync() after writing every chunk. </p>
<dt><code>-c</code></p>
<dd>the number of times to read/write the entire disk. </p>
<dt><code>-r</code></p>
<dd>the range of data (in Meg) to read/write on each pass (default the entire device). Useful if you want to quickly test part of a large drive. If a single number is given then that is the last block to read, if two numbers then it&#8217;s the start and end of a range. Values are in megs, but they are rounded down to the block size. </p>
<dt><code>-s</code></p>
<dd>skip rate. The option -s 10 will cause it to read every 10th block and skip the rest. Accepts values from 2 to 20. </p>
<dt><code>-f</code></p>
<dd>the file-name for the input data. This isn&#8217;t needed on well configured systems that have a recent Glibc where you can specify the file name without the -f flag. </p>
<dt><code>-u</code></p>
<dd>user-id to use. When running as root specify the UID to run the tests as, it is not recommended to use root, so if you want to run as root use <code>-u root.</code> Also if you want to specify the group to run as then use the <code>user:group</code> format. If you specify a user by name but no group then the primary group of that user will be chosen. If you specify a user by number and no group then the group will be <code>nogroup.</code><br />
&nbsp;<wbr></p>
<dt><code>-g</code></p>
<dd>group-id to use. Same as using <code>:group</code> for the <code>-u</code> parameter, just a different way to specify it for compatibility with other programs. </p>
<dt><code>-w</code></p>
<dd>write zero blocks to the disk instead of reading from the disk &#8211; will destroy data! </p>
</dl>
<h2>Author</h2>
<p>This program, it&#8217;s manual page, and the Debian package were written by Russell Coker &lt;russell [at] coker.com.au&gt;.</p>
<h2>Availability</h2>
<p>The source is available from <a rel="nofollow" href="http://www.coker.com.au/bonnie++">http://www.coker.com.au/bonnie++</a> . </p>
<p> See <a rel="nofollow" href="http://etbe.coker.com.au/category/benchmark">http://etbe.coker.com.au/category/benchmark</a> for further information.</p>
