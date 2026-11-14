---
title: "wrmsr(1)"
name: "wrmsr"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wrmsr/"
description: "wrmsr – tool for writing CPU machine specific registers (MSR)"
---

<h2 class="name">NAME</h2>
<p> wrmsr &#8211; tool for writing CPU machine specific registers (MSR) </p>
<h2>SYNOPSIS</h2>
<p> <code>wrmsr [options] regno value</code></p>
<h2>DESCRIPTION</h2>
<p> <code>wrmsr </code> is a tool used for writing values to a CPU&#8217;s machine specific registers (MSR).<br />
 Note: if you&#8217;re running a Debian kernel, be sure that the msr.ko kernel module is loaded. &#8216;modprobe msr&#8217; should do the trick. Otherwise, you&#8217;ll get an error about <code>wrmsr</code> not being able to open files in /dev/cpu/&#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a list of available options</p>
<dt><code>&#8211;version, -V</code></p>
<dd> Print current version</p>
<dt><code>&#8211;all, -a</code></p>
<dd> All processors</p>
<dt><code>&#8211;processor &lt;#&gt;, -p</code></p>
<dd> Select processor number (default: 0)</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rdmsr/">rdmsr</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> <code>wrmsr </code> was written by Transmeta Corporation </p>
<p> This man page was contributed by Andres Salomon &lt;dilinger [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
