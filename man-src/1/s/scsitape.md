---
title: "scsitape(1)"
name: "scsitape"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scsitape/"
description: "scsitape – control SCSI tape devices"
---

<h2>NAME</h2>
<p> scsitape &#8211; control SCSI tape devices</p>
<h2>SYNOPSIS</h2>
<p> scsitape [-f &lt;scsi-generic-device&gt;] commands</p>
<h2>DESCRIPTION</h2>
<p> The <code>scsitape</code> command controls SCSI tape drives in a platform-independent manner. As long as &#8216;mtx&#8217; works on the platform, so does &#8216;scsitape&#8217;. </p>
<p> Note that &#8216;scsitape&#8217; and your OS&#8217;s native tape driver may stomp on each other. In particular, if you use &#8216;setblk&#8217; and your OS&#8217;s native tape driver has a different notion of the block size, you may get evil results. It is recommended to use &#8216;scsitape&#8217; only for software where you&#8217;ve written your own low-level READ and WRITE routines that use the SCSI command set to directly talk to tape drives (i.e., you do not use the OS&#8217;s native tape driver at all).</p>
<h2>OPTIONS</h2>
<p> The first argument, given following <code>-f</code> , is the SCSI generic device corresponding to your tape drive. Consult your operating system&#8217;s documentation for more information (for example, under Linux these are generally /dev/sg0 through /dev/sg15, under FreeBSD these are /dev/pass0 through /dev/passX. Under Solaris this is usually the same as your tape drive (Solaris has a SCSI passthrough ioctl). You can set the STAPE or TAPE environment variable rather than use -f. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>setblk &lt;n&gt;</code></p>
<dd> Set the tape drive&#8217;s SCSI block size to &lt;n&gt; bytes. (NOTE: if you are using your OS&#8217;s native tape driver, THIS IS EVIL!). </p>
<dt><code>fsf &lt;n&gt;</code></p>
<dd> Go forward by &lt;n&gt; tapemarks.</p>
<dt><code>bsf &lt;n&gt;</code></p>
<dd> Go to immediately previous the &lt;n&gt;th previous tapemark. (WARNING: This probably doesn&#8217;t do what you expect &#8212; e.g. if you are immediately after a tapemark and type &#8216;bfs 1&#8217;, it moves to immediately *before* that tape mark, for a sum total of zero effective movement!).</p>
<dt><code>eod</code></p>
<dd> Go to end of data.</p>
<dt><code>rewind</code></p>
<dd> Rewind the tape drive.</p>
<dt><code>eject</code></p>
<dd> Eject the tape currently in the drive.</p>
<dt><code>erase</code></p>
<dd> Does a *short* erase (warning: does NOT work on all drives!).</p>
<dt><code>mark &lt;n&gt;</code></p>
<dd>
&nbsp;<wbr>write&nbsp;<wbr>&lt;n&gt;&nbsp;<wbr>filemarks&nbsp;<wbr>(&nbsp;<wbr>&#8216;mark 0&#8217;&nbsp;<wbr>flushes the drive&#8217;s buffers&nbsp;<wbr>).&nbsp;<wbr></p>
<dt><code>seek &lt;n&gt;</code></p>
<dd> Seek to a logical position &lt;n&gt; that was reported by a previous &#8216;tapeinfo&#8217; command.</p>
<dt><code>write &lt;blocksize&gt; </code></p>
<dd> write blocks from stdin to the tape. Chunk the data into &lt;blocksize&gt;-sized chunks. *DOES NOT WRITE OUT A TAPEMARK!* (you will need to use a subsequent <code>mark 1</code> command to write out a tape mark).</p>
<dt><code>read [&lt;blocksize&gt;] [ &lt;#blocks/#bytes&gt; ]</code></p>
<dd> read blocks from the tape, write them to stdout. If we are in variable block mode, &lt;blocksize&gt; should be zero (note: The maximum block size we currently support in variable block mode is 128K, MAX_READ_SIZE will need to be turned into a settable variable to allow bigger reads). If &lt;blocksize&gt; is ommitted, we assume that we&#8217;re in variable block mode, and that we are going to read from tape until we hit a tapemark or end of partition or end of tape. </p>
</dl>
<h2>AUTHORS</h2>
<p> This program was written by Eric Lee Green &lt;eric [at] badtux.org&gt;. Major portions of the &#8216;mtxl.c&#8217; library used herein were written by Leonard Zubkoff. </p>
<p> The SCSI read and write routines are based upon those that Richard Fish wrote for Enhanced Software Technology&#8217;s BRU 16.1 product, substantially modified to work in our particular environment (in particular, all the variable block stuff is new since BRU only does fixed block reads and writes, and the BRU code uses bitmasks rather than bitfields for the various flags and such in return values, as well as the BRU code having a different SCSI API and having variable names considerably shorter than the rather sesquipedalian &#8216;mtx&#8217; identifiers). As required by &#8216;mtxl.c&#8217;, these routines are licensed under the GNU General Public License. </p>
<h2>HINTS</h2>
<p> Under Linux, <code>cat /proc/scsi/scsi</code> will tell you what SCSI devices you have. You can then refer to them as <code>/dev/sga,</code> <code>/dev/sgb, </code> etc. by the order they are reported. </p>
<p> Under FreeBSD, <code>camcontrol devlist</code> will tell you what SCSI devices you have, along with which <code>pass</code> device controls them. </p>
<p> Under Solaris 7 and 8, <code>/usr/sbin/devfsadm -C</code> will clean up your /devices directory. Then <code>find /devices -name &#8216;st@*&#8217; -print </code> will return a list of all tape drives. /dev on Solaris is apparently only of historical interest. </p>
<h2>BUGS AND LIMITATIONS</h2>
<p> for <code>scsitape read 0 &lt;n&gt;</code> where you are doing variable-block-size reads and wish for &lt;n&gt; bytes, it instead reads one and exactly one block from tape and prints that (no matter what its size). Use &#8216;dd&#8217; on the output of scsitape if you want finer control. </p>
<p> <code>scsitape read 0</code> attempts reads of MAX_READ_SIZE, which is currently 128K. If blocks on tape are larger than 128K, only the first 128K will be read &#8212; the remainder will be silently dumped in the toilet. </p>
<p> This program does not interact well (or at all :-) with your OS&#8217;s native tape driver. You will likely see weird things happen if you attempt to intermingle scsitape commands with native tape driver operations. Note that BRU 16.1 for Solaris (and possibly others, but Solaris I know about) will have a &#8216;scsi&#8217; keyword to bypass the native tape driver and write via direct uscsi commands, so if you use &#8216;scsitape&#8217; to bypass the flaws of the native Solaris driver, you can use BRU 16.1 to write your actual tape archives. (Assuming that BRU 16.1 has been released at the time that you read this). </p>
<h2>AVAILABILITY</h2>
<p> This version of <code>scsitape</code> is currently being maintained by Robert Nelson &lt;robertnelson [at] users.sourceforge.net&gt; as part of the &#8216;mtx&#8217; suite of programs. The &#8216;mtx&#8217; home page is <a rel="nofollow" href="http://mtx.sourceforge.net">http://mtx.sourceforge.net</a> and the actual code is currently available there and via SVN from <a rel="nofollow" href="http://sourceforge.net/projects/mtx.">http://sourceforge.net/projects/mtx.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-loaderinfo/">loaderinfo</a></code>(1),<code><a href="/docs/linux/man/1-tapeinfo/">tapeinfo</a></code>(1),<code><a href="/docs/linux/man/1-mtx/">mtx</a></code>(1) </p>
<h2>Index</h2>
