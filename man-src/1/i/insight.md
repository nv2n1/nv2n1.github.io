---
title: "insight(1)"
name: "insight"
section: "1"
letter: "i"
url: "/docs/linux/man/1-insight/"
description: "insight – GDB/Insight graphical debugger"
---

<h2>NAME</h2>
<p> insight &#8211; GDB/Insight graphical debugger</p>
<h2>DESCRIPTION</h2>
<p> This is the GNU debugger. Usage:</p>
<dl>
<dt>
<dd> insight [options] [executable-file [core-file or process-id]] insight [options] <code>&#8211;args</code> executable-file [inferior-arguments &#8230;]</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;args</code></p>
<dd> Arguments after executable-file are passed to inferior</p>
<dt><code>-b</code> BAUDRATE</p>
<dd> Set serial port baud rate used for remote debugging.</p>
<dt><code>&#8211;batch</code></p>
<dd> Exit after processing options.</p>
<dt><code>&#8211;batch-silent</code></p>
<dd> As for <code>&#8211;batch</code>, but suppress all insight stdout output.</p>
<dt><code>&#8211;return-child-result</code></p>
<dd> INSIGHT exit code will be the child&#8217;s exit code.</p>
<dt><code>&#8211;cd</code>=<i>DIR</i></p>
<dd> Change current directory to DIR.</p>
<dt> <code>&#8211;command</code>=<i>FILE</i>, <code>-x</code> Execute INSIGHT commands from FILE.</p>
<dt><code>&#8211;eval-command</code>=<i>COMMAND</i>, <code>-ex</code></p>
<dd>
<dd>Execute a single INSIGHT command. May be used multiple times and in conjunction with <code>&#8211;command</code>.</p>
<dt><code>&#8211;core</code>=<i>COREFILE</i></p>
<dd> Analyze the core dump COREFILE.</p>
<dt><code>&#8211;pid</code>=<i>PID</i></p>
<dd> Attach to running process PID.</p>
<dt><code>&#8211;dbx</code></p>
<dd> DBX compatibility mode.</p>
<dt><code>&#8211;directory</code>=<i>DIR</i></p>
<dd> Search for source files in DIR.</p>
<dt><code>&#8211;epoch</code></p>
<dd> Output information used by epoch emacs-GDB interface.</p>
<dt><code>&#8211;exec</code>=<i>EXECFILE</i></p>
<dd> Use EXECFILE as the executable.</p>
<dt><code>&#8211;fullname</code></p>
<dd> Output information used by emacs-GDB interface.</p>
<dt><code>&#8211;help</code></p>
<dd> Print this message.</p>
<dt><code>&#8211;interpreter</code>=<i>INTERP</i></p>
<dd> Select a specific interpreter / user interface</p>
<dt><code>-l</code> TIMEOUT</p>
<dd> Set timeout in seconds for remote debugging.</p>
<dt><code>&#8211;nw</code></p>
<dd> Do not use a window interface.</p>
<dt><code>&#8211;nx</code></p>
<dd> Do not read .gdbinit file.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Do not print version number on startup.</p>
<dt><code>&#8211;readnow</code></p>
<dd> Fully read symbol files on first access.</p>
<dt><code>&#8211;se</code>=<i>FILE</i></p>
<dd> Use FILE as symbol file and executable file.</p>
<dt><code>&#8211;symbols</code>=<i>SYMFILE</i></p>
<dd> Read symbols from SYMFILE.</p>
<dt><code>&#8211;tty</code>=<i>TTY</i></p>
<dd> Use TTY for input/output by the program being debugged.</p>
<dt><code>&#8211;tui</code></p>
<dd> Use a terminal user interface.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and then exit.</p>
<dt><code>-w</code></p>
<dd> Use a window interface.</p>
<dt><code>&#8211;write</code></p>
<dd> Set writing into executable and core files.</p>
<dt><code>&#8211;xdb</code></p>
<dd> XDB compatibility mode.</dl>
<p> For more information, type &quot;help&quot; from within GDB, or consult the GDB manual (available as on-line info or a printed manual).</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &quot;bug-gdb [at] gnu.org&quot;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. Type &quot;show copying&quot; and &quot;show warranty&quot; for details. This GDB was configured as &quot;i386-linux-gnu&quot;.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gdb</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gdb</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gdb</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
