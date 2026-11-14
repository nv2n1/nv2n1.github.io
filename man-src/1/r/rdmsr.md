---
title: "rdmsr(1)"
name: "rdmsr"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdmsr/"
description: "rdmsr – tool for reading CPU machine specific registers (MSR)"
---

<h2 class="name">NAME</h2>
<p> rdmsr &#8211; tool for reading CPU machine specific registers (MSR) </p>
<h2>SYNOPSIS</h2>
<p> <code>rdmsr [options] regno</code></p>
<h2>DESCRIPTION</h2>
<p> <code>rdmsr </code> is a tool used for reading a CPU&#8217;s machine specific registers (MSR).<br />
 Note: if you&#8217;re running a Debian kernel, be sure that the msr.ko kernel module is loaded. &#8216;modprobe msr&#8217; should do the trick. Otherwise, you&#8217;ll get an error about <code>rdmsr</code> not being able to open files in /dev/cpu/&#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a list of available options</p>
<dt><code>&#8211;version, -V</code></p>
<dd> Print current version</p>
<dt><code>&#8211;hexadecimal, -x</code></p>
<dd> Display output in hexadecimal (lower case)</p>
<dt><code>&#8211;capital-hex, -X</code></p>
<dd> Display output in hexadecimal (upper case)</p>
<dt><code>&#8211;decimal, -d</code></p>
<dd> Display output in signed decimal</p>
<dt><code>&#8211;unsigned, -u</code></p>
<dd> Display output in unsigned decimal</p>
<dt><code>&#8211;octal, -o</code></p>
<dd> Display output in octal</p>
<dt><code>&#8211;c-language, -c</code></p>
<dd> Format output as a C language constant</p>
<dt><code>&#8211;zero-pad, -0</code></p>
<dd> Output leading zeroes</p>
<dt><code>&#8211;zero-pad, -0</code></p>
<dd> Output leading zeroes</p>
<dt><code>&#8211;raw, -r</code></p>
<dd> Output raw binary</p>
<dt><code>&#8211;all, -a</code></p>
<dd> All processors</p>
<dt><code>&#8211;processor &lt;#&gt;, -p</code></p>
<dd> Select processor number (default: 0)</p>
<dt><code>&#8211;bitfield h:l, -f</code></p>
<dd> Output bits [h:l] only</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wrmsr/">wrmsr</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> <code>rdmsr </code> was written by Transmeta Corporation </p>
<p> This man page was contributed by Andres Salomon &lt;dilinger [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
