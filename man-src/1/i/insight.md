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
</dt><dd> insight [options] [executable-file [core-file or process-id]] insight [options] <code>&#8211;args</code> executable-file [inferior-arguments &#8230;]</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;args</code></dt>
<dd> Arguments after executable-file are passed to inferior</dd>
<dt><code>-b</code> BAUDRATE</dt>
<dd> Set serial port baud rate used for remote debugging.</dd>
<dt><code>&#8211;batch</code></dt>
<dd> Exit after processing options.</dd>
<dt><code>&#8211;batch-silent</code></dt>
<dd> As for <code>&#8211;batch</code>, but suppress all insight stdout output.</dd>
<dt><code>&#8211;return-child-result</code></dt>
<dd> INSIGHT exit code will be the child&#8217;s exit code.</dd>
<dt><code>&#8211;cd</code>=<i>DIR</i></dt>
<dd> Change current directory to DIR.</dd>
<dt> <code>&#8211;command</code>=<i>FILE</i>, <code>-x</code> Execute INSIGHT commands from FILE.</dt>
<dt><code>&#8211;eval-command</code>=<i>COMMAND</i>, <code>-ex</code></dt>
<dd>
</dd><dd>Execute a single INSIGHT command. May be used multiple times and in conjunction with <code>&#8211;command</code>.</dd>
<dt><code>&#8211;core</code>=<i>COREFILE</i></dt>
<dd> Analyze the core dump COREFILE.</dd>
<dt><code>&#8211;pid</code>=<i>PID</i></dt>
<dd> Attach to running process PID.</dd>
<dt><code>&#8211;dbx</code></dt>
<dd> DBX compatibility mode.</dd>
<dt><code>&#8211;directory</code>=<i>DIR</i></dt>
<dd> Search for source files in DIR.</dd>
<dt><code>&#8211;epoch</code></dt>
<dd> Output information used by epoch emacs-GDB interface.</dd>
<dt><code>&#8211;exec</code>=<i>EXECFILE</i></dt>
<dd> Use EXECFILE as the executable.</dd>
<dt><code>&#8211;fullname</code></dt>
<dd> Output information used by emacs-GDB interface.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print this message.</dd>
<dt><code>&#8211;interpreter</code>=<i>INTERP</i></dt>
<dd> Select a specific interpreter / user interface</dd>
<dt><code>-l</code> TIMEOUT</dt>
<dd> Set timeout in seconds for remote debugging.</dd>
<dt><code>&#8211;nw</code></dt>
<dd> Do not use a window interface.</dd>
<dt><code>&#8211;nx</code></dt>
<dd> Do not read .gdbinit file.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Do not print version number on startup.</dd>
<dt><code>&#8211;readnow</code></dt>
<dd> Fully read symbol files on first access.</dd>
<dt><code>&#8211;se</code>=<i>FILE</i></dt>
<dd> Use FILE as symbol file and executable file.</dd>
<dt><code>&#8211;symbols</code>=<i>SYMFILE</i></dt>
<dd> Read symbols from SYMFILE.</dd>
<dt><code>&#8211;tty</code>=<i>TTY</i></dt>
<dd> Use TTY for input/output by the program being debugged.</dd>
<dt><code>&#8211;tui</code></dt>
<dd> Use a terminal user interface.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and then exit.</dd>
<dt><code>-w</code></dt>
<dd> Use a window interface.</dd>
<dt><code>&#8211;write</code></dt>
<dd> Set writing into executable and core files.</dd>
<dt><code>&#8211;xdb</code></dt>
<dd> XDB compatibility mode.</dd></dl>
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
</dt><dd> <code>info gdb</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
