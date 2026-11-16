---
title: "free(1)"
name: "free"
section: "1"
letter: "f"
url: "/docs/linux/man/1-free/"
description: "free – Display amount of free and used memory in the system"
---

<h2 class="name">NAME</h2>
<p> free &#8211; Display amount of free and used memory in the system </p>
<h2>SYNOPSIS</h2>
<p> <code>free</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>free</code> displays the total amount of free and used physical and swap memory in the system, as well as the buffers and caches used by the kernel. The information is gathered by parsing /proc/meminfo. The displayed columns are:</p>
<dl>
<dt><code>total</code></dt>
<dd> Total installed memory (MemTotal and SwapTotal in /proc/meminfo)</dd>
<dt><code>used</code></dt>
<dd> Used memory (calculated as <code>total</code> &#8211; <code>free</code> &#8211; <code>buffers</code> &#8211; <code>cache</code>)</dd>
<dt><code>free</code></dt>
<dd> Unused memory (MemFree and SwapFree in /proc/meminfo)</dd>
<dt><code>shared</code></dt>
<dd> Memory used (mostly) by tmpfs (Shmem in /proc/meminfo)</dd>
<dt><code>buffers</code></dt>
<dd> Memory used by kernel buffers (Buffers in /proc/meminfo)</dd>
<dt><code>cache</code></dt>
<dd> Memory used by the page cache and slabs (Cached and SReclaimable in /proc/meminfo)</dd>
<dt><code>buff/cache</code></dt>
<dd> Sum of <code>buffers</code> and <code>cache</code></dd>
<dt><code>available</code></dt>
<dd> Estimation of how much memory is available for starting new applications, without swapping. Unlike the data provided by the <code>cache</code> or <code>free</code> fields, this field takes into account page cache and also that not all reclaimable memory slabs will be reclaimed due to items being in use (MemAvailable in /proc/meminfo, available on kernels 3.14, emulated on kernels 2.6.27+, otherwise the same as <code>free</code>)</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;bytes</code></dt>
<dd> Display the amount of memory in bytes.</dd>
<dt><code>-k</code>, <code>&#8211;kibi</code></dt>
<dd> Display the amount of memory in kibibytes. This is the default.</dd>
<dt><code>-m</code>, <code>&#8211;mebi</code></dt>
<dd> Display the amount of memory in mebibytes.</dd>
<dt><code>-g</code>, <code>&#8211;gibi</code></dt>
<dd> Display the amount of memory in gibibytes.</dd>
<dt><code>&#8211;tebi</code></dt>
<dd> Display the amount of memory in tebibytes.</dd>
<dt><code>&#8211;pebi</code></dt>
<dd> Display the amount of memory in pebibytes.</dd>
<dt><code>&#8211;kilo</code></dt>
<dd> Display the amount of memory in kilobytes. Implies &#8211;si.</dd>
<dt><code>&#8211;mega</code></dt>
<dd> Display the amount of memory in megabytes. Implies &#8211;si.</dd>
<dt><code>&#8211;giga</code></dt>
<dd> Display the amount of memory in gigabytes. Implies &#8211;si.</dd>
<dt><code>&#8211;tera</code></dt>
<dd> Display the amount of memory in terabytes. Implies &#8211;si.</dd>
<dt><code>&#8211;peta</code></dt>
<dd> Display the amount of memory in petabytes. Implies &#8211;si.</dd>
<dt><code>-h</code>, <code>&#8211;human</code></dt>
<dd> Show all output fields automatically scaled to shortest three digit unit and display the units of print out. Following units are used. </dd>
<pre>
  B = bytes
  Ki = kibibyte
  Mi = mebibyte
  Gi = gibibyte
  Ti = tebibyte
  Pi = pebibyte
</pre>
<p> If unit is missing, and you have exbibyte of RAM or swap, the number is in tebibytes and columns might not be aligned with header.</p>
<dt><code>-w</code>, <code>&#8211;wide</code></dt>
<dd> Switch to the wide mode. The wide mode produces lines longer than 80 characters. In this mode <code>buffers</code> and <code>cache</code> are reported in two separate columns.</dd>
<dt><code>-c</code>, <code>&#8211;count</code> <i>count</i></dt>
<dd> Display the result <i>count</i> times. Requires the <code>-s</code> option.</dd>
<dt><code>-l</code>, <code>&#8211;lohi</code></dt>
<dd> Show detailed low and high memory statistics.</dd>
<dt><code>-s</code>, <code>&#8211;seconds</code> <i>delay</i></dt>
<dd> Continuously display the result <i>delay</i> seconds apart. You may actually specify any floating point number for <i>delay</i> using either . or , for decimal point. <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3) is used for microsecond resolution delay times.</dd>
<dt><code>&#8211;si</code></dt>
<dd> Use kilo, mega, giga etc (power of 1000) instead of kibi, mebi, gibi (power of 1024).</dd>
<dt><code>-t</code>, <code>&#8211;total</code></dt>
<dd> Display a line showing the column totals.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print help.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version information.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>/proc/meminfo</dt>
<dd> memory information</dd></dl>
<h2>BUGS</h2>
<p> The value for the <code>shared</code> column is not available from kernels before 2.6.32 and is displayed as zero.</p>
<dl>
<dt>Please send bug reports to</dt>
<dd></dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-slabtop/">slabtop</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8). </p>
<h2>Index</h2>
