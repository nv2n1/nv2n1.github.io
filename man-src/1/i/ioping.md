---
title: "ioping(1)"
name: "ioping"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ioping/"
description: "ioping – simple disk I/O latency monitoring tool"
---

<h2>NAME</h2>
<p> ioping &#8211; simple disk I/O latency monitoring tool</p>
<h2>SYNOPSYS</h2>
<p> [ <code>-ABCDLRWGYykq</code> ] [ <code>-c </code><i>count</i> ] [ <code>-i </code><i>interval</i> ] [ <code>-l </code><i>speed</i> ] [ <code>-t </code><i>time</i> ] [ <code>-T </code><i>time</i> ] [ <code>-s </code><i>size</i> ] [ <code>-S </code><i>wsize</i> ] [ <code>-o </code><i>offset</i> ] [ <code>-w </code><i>deadline</i> ] [ <code>-p </code><i>period</i> ] [ <code>-P </code><i>period</i> ] <i>directory</i>|<i>file</i>|<i>device</i><br />
 <code>-h</code> | <code>-v</code> </p>
<h2>DESCRIPTION</h2>
<p> This tool generates various I/O patterns and lets you monitor I/O speed and latency in real time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i>&nbsp;<wbr>count</i></p>
<dd> Stop after <i>count</i> requests.</p>
<dt><code>-i</code><i>&nbsp;<wbr>interval</i></p>
<dd> Set time between requests to <i>interval</i> (<code>1s</code>).</p>
<dt><code>-l</code><i>&nbsp;<wbr>speed</i></p>
<dd> Set <i>speed</i> limit in bytes per second. Set interval to request-size / speed.</p>
<dt><code>-t</code><i>&nbsp;<wbr>time</i></p>
<dd> Minimal valid request time (<code>0us</code>). Too fast requests are ignored in statistics.</p>
<dt><code>-T</code><i>&nbsp;<wbr>time</i></p>
<dd> Maximum valid request time. Too slow requests are ignored in statistics.</p>
<dt><code>-s</code><i>&nbsp;<wbr>size</i></p>
<dd> Request size (<code>4k</code>).</p>
<dt><code>-S</code><i>&nbsp;<wbr>wsize</i></p>
<dd> Working set size (<code>1m</code> for directory, whole size for file or device).</p>
<dt><code>-o</code><i>&nbsp;<wbr>offset</i></p>
<dd> Starting offset in the file/device (0).</p>
<dt><code>-w</code><i>&nbsp;<wbr>deadline</i></p>
<dd> Stop after <i>deadline</i> time passed.</p>
<dt><code>-p</code><i>&nbsp;<wbr>period</i></p>
<dd> Print raw statistics for every <i>period</i> requests (see format below).</p>
<dt><code>-P</code><i>&nbsp;<wbr>period</i></p>
<dd> Print raw statistics for every <i>period</i> in time.</p>
<dt><code>-A</code></p>
<dd> Use asynchronous I/O (syscalls <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), etc).</p>
<dt><code>-B</code></p>
<dd> Batch mode. Be quiet and print final statistics in raw format.</p>
<dt><code>-C</code></p>
<dd> Use cached I/O. Suppress cache invalidation via <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2)) before read and <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) after each write.</p>
<dt><code>-D</code></p>
<dd> Use direct I/O (see <code>O_DIRECT</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2)).</p>
<dt><code>-L</code></p>
<dd> Use sequential operations rather than random. This also sets default request size to <code>256k</code> (as in <code>-s 256k</code>).</p>
<dt><code>-R</code></p>
<dd> Disk seek rate test. This option suppress human-readable output for each request (as <code>-q</code>), sets default interval to zero (<code>-i 0</code>), stops measurement after 3 seconds (<code>-w 3</code>) and increases default working set size to 64m (<code>-S 64m</code>). Working set (<code>-S</code>) should be increased accordingly if disk has huge cache.</p>
<dt><code>-W</code></p>
<dd> Use writes rather than reads. Safe for directory target. Write I/O gives more reliable results for systems where non-cached reads are not supported or cached at some level. Might be <code>*DANGEROUS*</code> for file/device: it will shred your data. In this case should be repeated tree times (<code>-WWW</code>).</p>
<dt><code>-G</code></p>
<dd> Alternate read and write requests.</p>
<dt><code>-Y</code></p>
<dd> Use sync I/O (see <code>O_SYNC</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2)).</p>
<dt><code>-y</code></p>
<dd> Use data sync I/O (see <code>O_DSYNC</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2)).</p>
<dt><code>-k</code></p>
<dd> Keep and reuse temporary working file &quot;ioping.tmp&quot; (only for directory target).</p>
<dt><code>-q</code></p>
<dd> Suppress periodical human-readable output.</p>
<dt><code>-h</code></p>
<dd> Display help message and exit.</p>
<dt><code>-v</code></p>
<dd> Display version and exit.</dl>
<h3>Argument suffixes</h3>
<p> For options that expect time argument (<code>-i</code>, <code>-P</code> and <code>-w</code>), default is seconds, unless you specify one of the following suffixes (case-insensitive):</p>
<dl>
<dt><code>us</code>,&nbsp;<wbr><code>usec</code></p>
<dd> microseconds (a millionth of a second, 1 / 1 000 000)</p>
<dt><code>ms</code>,&nbsp;<wbr><code>msec</code></p>
<dd> milliseconds (a thousandth of a second, 1 / 1 000)</p>
<dt><code>s</code>,&nbsp;<wbr><code>sec</code></p>
<dd> seconds</p>
<dt><code>m</code>,&nbsp;<wbr><code>min</code></p>
<dd> minutes</p>
<dt><code>h</code>,&nbsp;<wbr><code>hour</code></p>
<dd> hours</dl>
<p> For options that expect &quot;size&quot; argument (<code>-s</code>, <code>-S</code> and <code>-o</code>), default is bytes, unless you specify one of the following suffixes (case-insensitive):</p>
<dl>
<dt><code>sector</code></p>
<dd> disk sectors (a sector is always 512).</p>
<dt><code>KiB</code>,&nbsp;<wbr><code>k</code>,&nbsp;<wbr><code>kb</code></p>
<dd> kilobytes (1 024 bytes)</p>
<dt><code>page</code></p>
<dd> memory pages (a page is always 4KiB).</p>
<dt><code>MiB</code>,&nbsp;<wbr><code>m</code>,&nbsp;<wbr><code>mb</code></p>
<dd> megabytes (1 048 576 bytes)</p>
<dt><code>GiB</code>,&nbsp;<wbr><code>g</code>,&nbsp;<wbr><code>gb</code></p>
<dd> gigabytes (1 073 741 824 bytes)</p>
<dt><code>TiB</code>,&nbsp;<wbr><code>t</code>,&nbsp;<wbr><code>tb</code></p>
<dd> terabytes (1 099 511 627 776 bytes)</dl>
<p> For options that expect &quot;number&quot; argument (<code>-p</code> and <code>-c</code>) you can optionally specify one of the following suffixes (case-insensitive):</p>
<dl>
<dt><code>k</code></p>
<dd> kilo (thousands, 1 000)</p>
<dt><code>m</code></p>
<dd> mega (millions, 1 000 000)</p>
<dt><code>g</code></p>
<dd> giga (billions, 1 000 000 000)</p>
<dt><code>t</code></p>
<dd> tera (trillions, 1 000 000 000 000)</dl>
<h2>EXIT STATUS</h2>
<p> Returns <code>0</code> upon success. The following error codes are defined:</p>
<dl>
<dt><code>1</code></p>
<dd> Invalid usage (error in arguments).</p>
<dt><code>2</code></p>
<dd> Error during preparation stage.</p>
<dt><code>3</code></p>
<dd> Error during runtime.</dl>
<h2>RAW STATISTICS</h2>
<p> <code>ioping -p 100 -c 200 -i 0 -q .</code><br />
 <tt>100 26694 3746 15344272 188 267 1923 228 100 26694<br />
 100 24165 4138 16950134 190 242 2348 214 100 24165<br />
 (1) (2) (3) (4) (5) (6) (7) (8) (9) (10) </p>
<p> (1) count of requests in statistics<br />
 (2) running time (usec)<br />
 (3) requests per second (iops)<br />
 (4) transfer speed (bytes/sec)<br />
 (5) minimal request time (usec)<br />
 (6) average request time (usec)<br />
 (7) maximum request time (usec)<br />
 (8) request time standard deviation (usec)<br />
 (9) total requests (including too slow and too fast)<br />
 (10) total running time (usec) </tt></p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>ioping .</code></p>
<dd> Show disk I/O latency using the default values and the current directory, until interrupted. This command prepares temporary (unlinked/hidden) working file and reads random chunks from it using non-cached read requests.</p>
<dt><code>ioping -c 10 -s 1M /tmp</code></p>
<dd> Measure latency on <code>/tmp</code> using 10 requests of 1 megabyte each.</p>
<dt><code>ioping -R /dev/sda</code></p>
<dd> Measure disk seek rate.</p>
<dt><code>ioping -RL /dev/sda</code></p>
<dd> Measure disk sequential speed.</p>
<dt><code>ioping -RLB . | awk &#8216;{print $4}&#8217;</code></p>
<dd> Get disk sequential speed in bytes per second.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1), <code><a href="/docs/linux/man/1-fio/">fio</a></code>(1), <code><a href="/docs/linux/man/1-dbench/">dbench</a></code>(1), <code>fsstress,</code> <code>xfstests,</code> <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8), <code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8),</p>
<h2>HOMEPAGE</h2>
<h2>AUTHORS</h2>
<p> This program was written by Konstantin Khlebnikov<br />
 Man-page was written by Kir Kolyshkin </p>
<h2>Index</h2>
