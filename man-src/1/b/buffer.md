---
title: "buffer(1)"
name: "buffer"
section: "1"
letter: "b"
url: "/docs/linux/man/1-buffer/"
description: "buffer – very fast reblocking program"
---

<h2>NAME</h2>
<p> buffer &#8211; very fast reblocking program</p>
<h2>SYNTAX</h2>
<p> <code>buffer</code> [<code>-S size</code>] [<code>-b blocks</code>] [<code>-s size</code>] [<code>-m size</code>] [<code>-p percentage</code>] [<code>-u microseconds</code>] [<code>-B</code>] [<code>-t</code>] [<code>-Z</code>] [<code>-i filename</code>] [<code>-o filename</code>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i filename</code></p>
<dd> Use the given file as the input file. The default is stdin.</p>
<dt><code>-o filename</code></p>
<dd> Use the given file as the output file. The default is stdout.</p>
<dt><code>-S size</code></p>
<dd> After every chunk of this size has been written, print out how much has been written so far. Also prints the total througput. By default this is not set.</p>
<dt><code>-s size</code></p>
<dd> Size in bytes of each block. The default blocksize is 10k to match the normal output of the <i><a href="/docs/linux/man/1-tar/">tar</a>(1)</i> program.</p>
<dt><code>-z size</code></p>
<dd> Combines the <code>-S</code> and <code>-s</code> flags.</p>
<dt><code>-b blocks</code></p>
<dd> Number of blocks to allocate to shared memory circular buffer. Defaults to the number required to fill up the shared memory requested.</p>
<dt><code>-m size</code></p>
<dd> Maximum size of the shared memory chunk to allocate for the circular queue. Defaults to one megabyte.</p>
<dt><code>-p percentage</code></p>
<dd> Only start a write when the given percentage of the internal queue is full. A percentage around 75 often proves best. Defaults to zero.</p>
<dt><code>-u microseconds</code></p>
<dd> After every write pause for this many microseconds. Defaults to zero. (Suprisingly a small sleep, 100 usecs, after each write can greatly enhance throughput on some drives.)</p>
<dt><code>-B</code></p>
<dd> Force each block written to be padded out to the blocksize. This is needed by some tape and cartridge drives. Defaults to unpadded. This only affects the last block written.</p>
<dt><code>-t</code></p>
<dd> On exiting print to stderr a brief message showing the total number of bytes written.</p>
<dt><code>-Z</code></p>
<dd> If reading/writing directly to a character device (like a tape drive) then after each gigabyte perform an lseek to the start of the file. Use this flag with extreme care. It can only be used on devices where an lseek does not rewind the tape but does reset the kernels position flags. It is used to allow more than 2 gigabytes to be written.</dl>
<p> Sizes are a number with an optional trailing character. A &#8216;b&#8217; multiplies the size by 512, a &#8216;k&#8217; by 1024 and an &#8216;m&#8217; by a meg.</p>
<h2>DESCRIPTION</h2>
<p> <i>Buffer</i> reads from standard input reblocking to the given blocksize and writes each block to standard output. </p>
<p> Internally <i>buffer</i> is a pair of processes communicating via a large circular queue held in shared memory. The reader process only has to block when the queue is full and the writer process when the queue is empty. <i>Buffer</i> is designed to try and keep the writer side continuously busy so that it can stream when writing to tape drives. When used to write tapes with an intervening network <i>buffer</i> can result in a considerable increase in throughput. </p>
<p> The default settings for <i>buffer</i> are normally good enough. If you are a heavy tape user then it is worth your while trying out various different combinations of options. In particular running a <i>buffer</i> at both ends of the pipe can provide a substantial increase (see last example below).</p>
<h2>EXAMPLES</h2>
<p> $ <code>buffer &lt; /etc/termcap &gt; /dev/rst8</code> </p>
<p> $ <code>tar cf &#8211; . | rsh somehost &#8216;buffer &gt; /dev/rst8&#8217;</code> </p>
<p> $ <code>dump fu &#8211; | rsh somehost &#8216;buffer -s 16k &gt; /dev/nrst8&#8217;</code><br />
 $ <code>tar cf &#8211; . | buffer |<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rsh somehost &#8216;buffer -S 500K -p 75 &gt; /dev/rst0&#8217;</code></p>
<h2>BUGS</h2>
<p> Internally, for printing purposes, buffer counts in terms of the number of kilobytes output. If the blocksize you use is not a whole number of kilobytes then the numbers printed will be inaccurate. </p>
<h2>THANKS</h2>
<p> Thanks to Kevin Twidle &lt;kpt [at] doc.ic.ac.uk&gt; for a lot of early suggestions and patches to make it work with non-tar/dump tapes to exabyte drives. </p>
<p> Thanks to Andi Karrer &lt;karrer [at] bernina.ethz.ch&gt;, Rumi Zahir &lt;rumi [at] iis.ethz.ch&gt; and Christoph Wicki &lt;wicki [at] iis.ethz.ch&gt; for patches to make buffer work when trying to write single tape files of greater than 2 gigabytes. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1990, 1991 by Lee McLoughlin.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dd/">dd</a>(1), <a href="/docs/linux/man/1-tar/">tar</a>(1), <a href="/docs/linux/man/1-rsh/">rsh</a>(1) </p>
<h2>Index</h2>
