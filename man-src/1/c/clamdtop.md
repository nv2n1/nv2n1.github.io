---
title: "clamdtop(1)"
name: "clamdtop"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clamdtop/"
description: "clamdtop – monitor the Clam AntiVirus Daemon"
---

<h2>NAME</h2>
<p> clamdtop &#8211; monitor the Clam AntiVirus Daemon</p>
<h2>SYNOPSIS</h2>
<p> clamdtop [options] [clamdspec &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> clamdtop is a tool to monitor one or multiple clamd(s). It has a (color) ncurses interface, that shows the jobs in clamd&#8217;s queue, memory usage, and information about the loaded signature database. You can specify on the command-line to which clamd(s) it should connect to. By default it will attempt to connect to the local clamd as defined in clamd.conf. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version number and exit.</p>
<dt><code>&#8211;config-file=FILE</code></p>
<dd> Read clamd settings from FILE, to determine how to connect to it.</p>
<dt><code>clamdspec</code></p>
<dd> Specifies the clamd to connect to: either a path to the local (unix domain) socket of clamd, or an IP address and an port number (that defaults to 3310) to connect to a local or remote clamd using TCP/IP. </p>
</dl>
<h2>OVERVIEW</h2>
<h3>KEYS:</h3>
<dl>
<dt><code>H</code></p>
<dd>
<p> Displays a short helpscreen, describing the meaning of various elements on the display.</p>
<dt><code>Q</code></p>
<dd>
<p> Quits clamdtop</p>
<dt><code>R</code></p>
<dd>
<p> Resets the maximum values.</p>
<dt><code>up arrow, down arrow</code></p>
<dd>
<p> If you are monitoring multiple clamds then clamdtop will show an overview screen by default. You can use the <code>up arrow</code> and <code> down arrow</code> keys to cycle through each clamd individually, and the overview screen. A blue bar will highlight the clamd that is currently shown in detail. On the overview screen none of the clamds is selected (hence no blue bar), and you can see the items from the queue of all clamds. </p>
</dl>
<h3>The top bar</h3>
<p> Shows the version of clamdtop and the current time. Clamdtop updates the display once every 2 seconds. </p>
<h3>The list of clamds</h3>
<p> Shows the clamds that clamdtop is connected to, and statistics about them. </p>
<dl>
<dt><code>NO</code></p>
<dd> Unique clamd number</p>
<dt><code>CONNTIME</code></p>
<dd> How long clamdtop has been connected (reset upon a reconnect)</p>
<dt><code>LIV</code></p>
<dd> Total number of live threads</p>
<dt><code>IDL</code></p>
<dd> Total number of idle threads</p>
<dt><code>QUEUE</code></p>
<dd> Number of items in queue</p>
<dt><code>MAXQ</code></p>
<dd> Maximum number of items observed in the queue</p>
<dt><code>MEM</code></p>
<dd> Total memory usage (if available)</p>
<dt><code>HOST</code></p>
<dd> Which clamd, local means unix socket</p>
<dt><code>ENGINE</code></p>
<dd> Engine version</p>
<dt><code>DBVER</code></p>
<dd> Database version</p>
<dt><code>DBTIME</code></p>
<dd> Database publish time</dl>
<h3>Clamd detailed view</h3>
<dl>
<dt>Primary threads <code>live</code></p>
<dd> The number of threads that are executing commands or scanning.</p>
<dt>Primary threads <code>idle</code></p>
<dd> The number of threads that are idle, waiting for commands. They will exit after IdleTimeout (30 seconds).</p>
<dt>Primary threads <code>max</code></p>
<dd> The maximum number of threads configured.</p>
<dt>Queue items</p>
<dd> The number of items (scanjobs) in clamd&#8217;s queue that are waiting for a free thread to be processed.</p>
<dt>Queue max</p>
<dd> The maximum number of items observed in clamd&#8217;s queue.</dl>
<h3>The memory usage view</h3>
<p> If available, it will show details on clamd&#8217;s memory usage:</p>
<dl>
<dt><code>Mem heap</code></p>
<dd> The amount of memory used by libc from the heap in MegaBytes.</p>
<dt><code>Mem mmap</code></p>
<dd> The amount of memory used by libc from mmap-allocated memory in MegaBytes.</p>
<dt><code>Mem unused</code></p>
<dd> The amount of memory that can be reclaimed by libc.</p>
<dt><code>Libc used</code></p>
<dd> The amount of useful memory allocated by libc.</p>
<dt><code>Libc free</code></p>
<dd> The amount of memory allocated by libc, that can&#8217;t be freed due to fragmentation.</p>
<dt><code>Libc total</code></p>
<dd> The amount of memory allocated by libc from the system in total.</p>
<dt><code>Pool count</code></p>
<dd> The number of mmap regions allocated by clamd&#8217; memory pool allocator (for the signature database).</p>
<dt><code>Pool used</code></p>
<dd> The amount of memory used by clamd&#8217;s memory pool allocator (for the signature database).</p>
<dt><code>Total</code></p>
<dd> The total amount of memory allocated by clamd&#8217;s memory pool allocator.</dl>
<h3>The clamd job queue</h3>
<dl>
<dt><code>COMMAND</code></p>
<dd> Kind of command being executed, STATS is clamdtop, SCAN/CONTSCAN/FILDES/MULTISCAN is scan of a file/directory, MULTISCANFILE is scan of one item by a MULTISCAN job.</p>
<dt><code>QUEUEDSINCE</code></p>
<dd> The time since the command got queued, until now.</p>
<dt><code>FILE</code></p>
<dd> The name of the file being processed (if applicable).</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>(1) To connect to the clamd configured in the default clamd.conf:</p>
<dd>
<p> <code>clamdtop</code></p>
<dt>(2) To connect to the clamd configured in another clamd.conf:</p>
<dd>
<p> <code>clamdtop &#8211;config-file=/path/to/clamd.conf </p>
<dt>(3) To connect to a clamd running on another machine (192.168.0.3) on the LAN:</p>
<dd>
<p> clamdtop 192.168.0.3</code> </p>
<dt>(4) To connect to a clamd running on another machine (192.168.0.3) on a non-default port (3410):</p>
<dd>
<p> <code>clamdtop 192.168.0.3:3410</code></p>
<dt>(5) To monitor the local clamd and 2 other remote clamds over TCP/IP:</p>
<dd>
<p> <code>clamdtop localhost 192.168.0.3 192.168.0.4</code></dl>
<h2>NOTES</h2>
<p> clamdtop uses colors if the terminal is capable of colors. If you know your terminal is capable of colors, yet you aren&#8217;t seeing any, then check that your <code>TERM</code> environment variable is set correctly. For example try setting it to TERM=xterm-color if you are in an xterm-like environment. IPv6 support has been added. If specifying an IPv6 address, please use the normal IPv6 addressing rules. If specifying both an IPv6 address and a port combination, encapsulate the IPv6 address in square brakets (e.g. [::1]:3410).</p>
<h2>RETURN CODES</h2>
<p> 0 : Normal terminator</p>
<dl>
<dt>&gt;0: Error occured.</p>
<dd></dl>
<h2>CREDITS</h2>
<p> Please check the full documentation for credits.</p>
<h2>AUTHOR</h2>
<p> Török Edvin &lt;edwin [at] clamav.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5) </p>
<h2>Index</h2>
