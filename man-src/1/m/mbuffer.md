---
title: "mbuffer(1)"
name: "mbuffer"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mbuffer/"
description: "mbuffer – measuring buffer"
---

<h2>NAME</h2>
<p> mbuffer &#8211; measuring buffer</p>
<h2>SYNTAX</h2>
<p> mbuffer [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> mbuffer buffers I/O operations and displays the throughput rate. It is multi-threaded, supports network connections, and offers more options than the standard buffer.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> &lt;<i>filename</i>&gt;</p>
<dd> Use <i>filename</i> as input instead of the standard input (needs to be given for multi volume support). If <i>filename</i> is -, input is read from standard input.</p>
<dt><code>-I</code> &lt;<i>port</i>&gt;</p>
<dd> Use network port <i>port</i> as input instead of the standard input. If given a hostname and a port in the form hostname:port, the first interface with the IP of hostname will be used.</p>
<dt><code>-o</code> &lt;<i>filename</i>&gt;</p>
<dd> Use <i>filename</i> as output instead of the standard output (needs to be given for multi volume support, will enable use of sendfile if available). If <i>filename</i> is -, output is written to standard output. The option -o can be passed multiple times to specify multiple outputs.</p>
<dt><code>-O</code> &lt;<i>hostname:port</i>&gt;</p>
<dd> Write output to <i>hostname:port</i> instead of the standard output (will enable use of sendfile if available). This option can be used multiple times to send data to multiple machines.</p>
<dt><code>-b</code> &lt;<i>num</i>&gt;</p>
<dd> Use <i>num</i> blocks for buffer (default 256).</p>
<dt><code>-s</code> &lt;<i>size</i>&gt;</p>
<dd> Use blocks of <i>size</i> bytes for buffer (default pagesize of system).</p>
<dt><code>-m</code> &lt;<i>size</i>&gt;</p>
<dd> Use a total of <i>size</i> bytes for buffer (default 2MB) &#8211; size can be set with a trailing character (b and B for Byte, k for kByte, M for MByte, G for Gigabyte, and with % for a percentage of total physical memory).</p>
<dt><code>-L</code></p>
<dd> Lock buffer in memory &#8211; this option is not available for file-based buffers and requires mbuffer to be set-UID root (use with care).</p>
<dt><code>-n</code> &lt;<i>num</i>&gt;</p>
<dd> <i>num</i> volumes in input device (requires use of option -i for input device specification, pass 0 as argument if mbuffer should prompt for every new volume)</p>
<dt><code>-t</code></p>
<dd> use a memory-mapped temporary file as buffer (use with huge buffers)</p>
<dt><code>-T</code> &lt;<i>file</i>&gt;</p>
<dd> as -t but use <i>file</i> instead</p>
<dt><code>-d</code></p>
<dd> use block-size of device for output (needed for some devices, slows output down)</p>
<dt><code>-D</code> &lt;<i>size</i>&gt;</p>
<dd> assume an output volume of <i>size</i> bytes (default infinite) after which a volume change will be initiated. Small values are useful for the timely testing of multi-volume runs; accurate values if your device doesn&#8217;t properly signal end of media. Size can be set with a trailing character (b and B for Byte, k for kByte, M for MByte, or G for Gigabyte)</p>
<dt><code>-P</code> &lt;<i>num</i>&gt;</p>
<dd> start writing after the buffer has been filled to <i>num</i>% (default 0 &#8211; start at once)</p>
<dt><code>-p</code> &lt;<i>num</i>&gt;</p>
<dd> start reading after the buffer has dropped below fill-ratio of <i>num</i>% (default 100 &#8211; start at once)</p>
<dt><code>-l</code> &lt;<i>file</i>&gt;</p>
<dd> log messages to <i>file</i> instead of standard error output</p>
<dt><code>-u</code> &lt;<i>num</i>&gt;</p>
<dd> pause <i>num</i> microseconds after each write &#8211; might increase performance on some drives with very low performance (&lt; 1 MB/sec)</p>
<dt><code>-r</code> &lt;<i>rate</i>&gt;</p>
<dd> Set the maximum read rate to &lt;<i>rate</i>&gt;. &lt;<i>rate</i>&gt; can be given in either Bytes, kBytes, MBytes, or GBytes per second. To do so, use an appropriate suffix (i.e. k,M,G). This option is useful if you have a tape that is capable of transferring data faster than the host can handle it. In this case you can use this option to limit the transfer rate and keep the tape running. Be aware that this is both good for your tape drive, and enhances overall performance, by avoiding tape screwing.</p>
<dt><code>-R</code> &lt;<i>rate</i>&gt;</p>
<dd> Same as above only for setting the transfer limit for the writer.</p>
<dt><code>-A</code> &lt;<i>cmd</i>&gt;</p>
<dd> the device used is an autoloader which uses <i>cmd</i> to load the next volume. Pass &lt;<i>/bin/false</i>&gt; as an autoload command to suppress the warning message that appears when run without controlling terminal (e.g. via cron). Like this the autoload will fail and mbuffer will terminate with an error message when reaching the end of the tape.</p>
<dt><code>-a</code> &lt;<i>time</i>&gt;</p>
<dd> the device used is an autoloader which takes <i>time</i> seconds to load a new tape</p>
<dt><code>-f</code></p>
<dd> overwrite output file if it exists already</p>
<dt><code>-c</code></p>
<dd> write with synchronous data integrity support &#8211; This option forces all writes to complete before continuing. This enables errors to be reported earlier and more precisely, but might decrease performance. Especially systems with high level of data integrity support suffer a huge performance hit. Others might seem to be unaffected, but just neglect support for full synchronous data integrity.</p>
<dt><code>-v</code> &lt;<i>num</i>&gt;</p>
<dd> set verbose level to <i>num</i>. Valid values are 0..6 (0 = none, 1 = errors, 2 = warnings, 4 = information messages, 5 = debugging messages, 6 = I/O debugging). Higher values include lower values messages.</p>
<dt><code>-q</code></p>
<dd> quiet &#8211; do not display the status on the standard error output</p>
<dt><code>-Q</code></p>
<dd> quiet &#8211; do not log the status in the log file</p>
<dt><code>&#8211;direct</code></p>
<dd> Use O_DIRECT to open file descriptors. This option is not available on all systems. It tells the OS to bypass the page cache to improve performance when reading and writing. On Solaris this is an auto-magic option that is enabled if it is supported for the relevant file. Be aware that this option might lead to read/write failures, if the buffer isn&#8217;t properly aligned for direct I/O. Additionally, open might fail with EINVAL (i.e. invalid argument) if the named file does not support O_DIRECT.</p>
<dt><code>&#8211;append</code></p>
<dd> Open next output file given via option -o in append mode.</p>
<dt><code>&#8211;truncate</code></p>
<dd> Truncate next output file given via option -o when opening it.</p>
<dt><code>-6</code></p>
<dd> Force IPv6 mode for the following network I/O options on command line. <code>-4</code> Force IPv4 mode for the following network I/O options on command line. <code>-0</code> Choose IPv4/IPv6 mode on demand.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Output help information and exit.</p>
<dt><code>-H, &#8211;md5</code></p>
<dd> Generate a MD5 hash of transferred data.</p>
<dt><code>-H, &#8211;pid</code></p>
<dd> Print PID of current process. This option can help you to figure out which instance of mbuffer to kill, if multiple are running and one is hanging due to a network issue. Printing of the PID can also be triggered by adding &quot;printpid = 1&quot; to your .mbuffer.rc file.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>-W</code> &lt;<i>timeout</i>&gt;</p>
<dd> Activates a watchdog that gets triggered every <i>timeout</i> seconds and checks weather I/O activity has stalled. If either channel has stalled for a complete period, the watchdog writes an error message and terminates mbuffer via SIGINT. Be aware that the watchdog is unaware of tape-change activities. So choose the watchdog timeout greater that the worst-case tape-change time.</dl>
<h2>DEFAULT VALUES</h2>
<p> The default values for following options can be set as <i>key = value</i> pairs in the ~/.mbuffer.rc file:<br />
 <i>blocksize</i>: block size (option -s)<br />
 <i>timeout</i>: watchdog timeout (option -W)<br />
 <i>totalmem</i>: total buffer size (option -m)<br />
 <i>maxreadspeed</i>: maximum read speed (option -r)<br />
 <i>maxwritespeed</i>: maximum write speed (option -R)<br />
 <i>startwrite</i>: threshold for start writing (option -P)<br />
 <i>startread</i>: threshold for start reading (option -p)<br />
 <i>pause</i>: pause after writing a block (option -u)<br />
 <i>numblocks</i>: number of blocks in buffer (option -b)<br />
 <i>memlock</i>: lock buffer in memory (option -L)<br />
 <i>showstatus</i>: print transfer status on console (option -q)<br />
 <i>logstatus</i>: write transfer status to logfile (option -Q)<br />
 <i>tcpbuffer</i>: TCP buffer size (option &#8211;tcpbuffer) </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> If TMPDIR is set, mbuffer allocates storage for file-based buffers in this directory. If TMPDIR is unset, <i>/var/tmp</i> will be used.</p>
<h2>FILES</h2>
<p> <i>/usr/bin/mbuffer</i><br />
 <i>/var/tmp/mbuffer-*</i><br />
 <i>~/.mbuffer.rc</i></p>
<h2>EXAMPLES</h2>
<p> To run this program with the default options just type: </p>
<p> mbuffer </p>
<p> Using mbuffer to do a backup with tar to the default tape device. Options for this example: memory-mapped temporary file with a size of 10 Megabytes, start after 80% of the buffer have been filled. </p>
<p> tar cf &#8211; mydirectory | gzip | mbuffer -t -m 10M -P 80 -f -o $TAPE </p>
<p> Using mbuffer with 3 tapes for input and extracting the contents in the current work directory: </p>
<p> mbuffer -n 3 -i $TAPE | gzip -dc | tar xf &#8211; </p>
<p> Using mbuffer to write to multiple tape volumes: </p>
<p> tar cf &#8211; /usr | mbuffer -f -o $TAPE </p>
<p> Write to multiple tapes and erase every tape before writing: </p>
<p> tar cf &#8211; /usr | mbuffer -A &quot;echo next tape; read a &lt; /dev/tty; mt erase $TAPE&quot; -f -o $TAPE </p>
<p> Making a backup via network: </p>
<p> <i>tape server: </i>mbuffer -I 8000 -f -o $TAPE </p>
<p> <i>backup client: </i>tar zcf &#8211; /home | mbuffer -O tapeserver:8000 </p>
<p> Distributing a directory tree to multiple machines: </p>
<p> <i>master: </i>tar cf &#8211; /tree_to_clone | mbuffer -O clone0:8000 -O clone1:8000 </p>
<p> <i>clones: </i>mbuffer -I master:8000 | tar xf &#8211;</p>
<h2>EXITCODE</h2>
<p> mbuffer return 0 upon success. Any kind of failure will yield a non-zero exit code.</p>
<h2>AUTHORS</h2>
<p> Thomas Maier-Komor &lt;thomas [at] maier-komor.de&gt;</p>
<h2>DONATIONS</h2>
<p> If you like this software, and use it for production purposes in your company, please consider making a donation to support this work. You can donate directly via PayPal to the author&#8217;s e-mail address (thomas [at] maier-komor.de).</p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="http://www.maier-komor.de/mbuffer.html">http://www.maier-komor.de/mbuffer.html</a></p>
<h2>LICENSE</h2>
<p> This software is published under GNU General Public License V3. See file LICENSE for details.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-buffer/">buffer</a>(1) </p>
<h2>Index</h2>
