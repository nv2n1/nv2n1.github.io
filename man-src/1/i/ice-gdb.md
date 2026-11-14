---
title: "ice-gdb(1)"
name: "ice-gdb"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ice-gdb/"
description: "ice-gdb – JTAG ICE frontend for avr-gdb ice-insight – JTAG ICE frontend for avr-insight"
---

<h2 class="name">NAME</h2>
<p> ice-gdb &#8211; JTAG ICE frontend for avr-gdb<br />
 ice-insight &#8211; JTAG ICE frontend for avr-insight </p>
<h2>SYNOPSIS</h2>
<p> <code>ice-gdb/ice-insight</code> [<code>&#8211;debugger</code> <i>debugger</i>] [<code>&#8211;capture</code>] [<code>&#8211;ignore-intr</code>] [<code>&#8211;external</code>] [<i>gdb_arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ice-gdb</code> (respectively <code>ice-insight</code>) starts <code>avr-gdb</code> (respectively <code>avr-insight</code>) and <code>avarice</code> to do on-chip debugging on Atmel AVR processors using their JTAG-based on-chip debug facilities, via the Atmel JTAG ICE pod. </p>
<p> The executable for the program being debugged is downloaded to the processor unless the <code>&#8211;capture</code> option is specified. A number of extra commands are available within gdb when started, see their description in NEW GDB COMMANDS below. Restrictions on debugging with the JTAG ICE pod are discussed in more detail in DEBUGGING WITH JTAG ICE below. </p>
<p> The arguments passed to <code>avarice</code> include the value of the <code>AVARICE_ARGS</code> environment variable. This is typically used to specify the serial port to which the JTAG ICE pod is connected by setting <code>AVARICE_ARGS</code> to &quot;-j &lt;serial port name&gt;&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debugger debugger_command</code></p>
<dd> Specify a different debugger than avr-gdb (or avr-insight). This other debugger should behave similarly to gdb.</p>
<dt><code>&#8211;capture</code></p>
<dd> Don&#8217;t download the executable being debugged to the mote, just interrupt the current program and assume that it matches the executable passed to <code>ice-gdb</code>. This is similar to &quot;attaching&quot; to a running program within gdb.</p>
<dt><code>&#8211;ignore-intr</code></p>
<dd> Pass the <code>&#8211;ignore-intr</code> option to <code>avarice</code>. The single-step commands in gdb (s, n) will then &quot;step over&quot; interrupt handlers (i.e., if an interrupt occurs, execution will resume for the duration of the interrupt).</p>
<dt><code>&#8211;external</code></p>
<dd> Do not start <code>avarice</code>. Instead, <code>avr-gdb</code> will attempt to connect to an already running <code>avarice</code> on port localhost:6423.</dl>
<h2>NEW GDB COMMANDS</h2>
<dl>
<dt><code>ice-restart</code></p>
<dd> Restart avarice.</p>
<dt><code>ice-load filename</code></p>
<dd> Download executable filename to the Atmel processor and start debugging it (this replaces the gdb <code>load</code> command).</p>
<dt><code>target-ice</code></p>
<dd> Connect to a copy of <code>avarice</code> running on port localhost:6423.</dl>
<h2>DEBUGGING WITH JTAG ICE</h2>
<p> The JTAG ICE debugging environment has a few restrictions and changes:</p>
<dl>
<dt>*</p>
<dd> No &quot;soft&quot; breakpoints, and only three hardware breakpoints. The break command sets hardware breakpoints. The easiest way to deal with this restriction is to enable and disable breakpoints as needed.</p>
<dt>*</p>
<dd> Two 1-byte hardware watchpoints (but each hardware watchpoint takes away one hardware breakpoint). If you set a watchpoint on a variable which takes more than one byte, execution will be abysmally slow. Instead it is better to do the following: </p>
<dl>
<dt>
<dd> watch *(char *)&amp;myvariable</dl>
<dt>
<dd> which watches the least significant byte of <code>myvariable</code>.</p>
<dt>*</p>
<dd> The Atmel AVR processors have a Harvard architecture (separate code and data buses). To distinguish data address 0 from code address 0, <code>avr-gdb</code> adds 0x800000 to all data addresses. Bear this in mind when examining printed pointers, or when passing absolute addresses to gdb commands.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>AVARICE_ARGS</code></p>
<dd> Extra arguments to pass to <code>avarice</code> at startup.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gdb/">gdb</a>(1), <a href="/docs/linux/man/1-insight/">insight</a>(1).</p>
<h2>BUGS</h2>
<p> On Windows, the <code>ice-gdb</code> and <code>ice-insight</code> commands only work in the <code>cygwin</code> environment. They do not work with the <code>mingw</code> environment. </p>
<h2>Index</h2>
