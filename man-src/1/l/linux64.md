---
title: "linux64(1)"
name: "linux64"
section: "1"
letter: "l"
url: "/docs/linux/man/1-linux64/"
description: "setarch – change reported architecture in new program environment and/or set personality flags"
---

<h2 class="name">NAME</h2>
<p> setarch &#8211; change reported architecture in new program environment and/or set personality flags </p>
<h2>SYNOPSIS</h2>
<p> <code>setarch</code> [<i>arch</i>] [options] [<i>program</i> [<i>argument</i>&#8230;]] </p>
<p> <code>setarch</code> <code>&#8211;list</code>|<code>-h</code>|<code>-V</code> </p>
<p> <code>arch</code> [options] [<i>program</i> [<i>argument</i>&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>setarch</code> modifies execution domains and process personality flags. </p>
<p> The execution domains currently only affects the output of <code>uname -m</code>. For example, on an AMD64 system, running <code>setarch i386 </code><i>program</i> will cause <i>program</i> to see i686 instead of x86_64 as the machine type. It also allows to set various personality options. The default <i>program</i> is <code>/bin/sh</code>. </p>
<p> Since version 2.33 the <i>arch</i> command line argument is optional and <code>setarch</code> may be used to change personality flags (ADDR_LIMIT_*, SHORT_INODE, etc) without modification of the execution domain.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;list</code></p>
<dd> List the architectures that <code>setarch</code> knows about. Whether <code>setarch</code> can actually set each of these architectures depends on the running kernel.</p>
<dt><code>&#8211;uname-2.6</code></p>
<dd> Causes the <i>program</i> to see a kernel version number beginning with 2.6. Turns on UNAME26.</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> Be verbose.</p>
<dt><code>-3</code>, <code>&#8211;3gb</code></p>
<dd> Specifies <i>program</i> should use a maximum of 3GB of address space. Supported on x86. Turns on ADDR_LIMIT_3GB.</p>
<dt><code>&#8211;4gb</code></p>
<dd> This option has no effect. It is retained for backward compatibility only, and may be removed in future releases.</p>
<dt><code>-B</code>, <code>&#8211;32bit</code></p>
<dd> Limit the address space to 32 bits to emulate hardware. Supported on ARM and Alpha. Turns on ADDR_LIMIT_32BIT.</p>
<dt><code>-F</code>, <code>&#8211;fdpic-funcptrs</code></p>
<dd> Treat user-space function pointers to signal handlers as pointers to address descriptors. This option has no effect on architectures that do not support FDPIC ELF binaries. In kernel v4.14 support is limited to ARM, Blackfin, Fujitsu FR-V, and SuperH CPU architectures.</p>
<dt><code>-I</code>, <code>&#8211;short-inode</code></p>
<dd> Obsolete bug emulation flag. Turns on SHORT_INODE.</p>
<dt><code>-L</code>, <code>&#8211;addr-compat-layout</code></p>
<dd> Provide legacy virtual address space layout. Use when the <i>program</i> binary does not have PT_GNU_STACK ELF header. Turns on ADDR_COMPAT_LAYOUT.</p>
<dt><code>-R</code>, <code>&#8211;addr-no-randomize</code></p>
<dd> Disables randomization of the virtual address space. Turns on ADDR_NO_RANDOMIZE.</p>
<dt><code>-S</code>, <code>&#8211;whole-seconds</code></p>
<dd> Obsolete bug emulation flag. Turns on WHOLE_SECONDS.</p>
<dt><code>-T</code>, <code>&#8211;sticky-timeouts</code></p>
<dd> This makes <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), and <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2) system calls preserve the timeout value instead of modifying it to reflect the amount of time not slept when interrupted by a signal handler. Use when <i>program</i> depends on this behavior. For more details see the timeout description in <code><a href="/docs/linux/man/2-select/">select</a></code>(2) manual page. Turns on STICKY_TIMEOUTS.</p>
<dt><code>-X</code>, <code>&#8211;read-implies-exec</code></p>
<dd> If this is set then <code><a href="/docs/linux/man/3-mmap/">mmap</a></code>(3) PROT_READ will also add the PROT_EXEC bit &#8211; as expected by legacy x86 binaries. Notice that the ELF loader will automatically set this bit when it encounters a legacy binary. Turns on READ_IMPLIES_EXEC.</p>
<dt><code>-Z</code>, <code>&#8211;mmap-page-zero</code></p>
<dd> SVr4 bug emulation that will set <code><a href="/docs/linux/man/3-mmap/">mmap</a></code>(3) page zero as read-only. Use when <i>program</i> depends on this behavior, and the source code is not available to be fixed. Turns on MMAP_PAGE_ZERO.</p>
<dt><code>-V</code>,<code> &#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help text and exit.</dl>
<h2>EXAMPLES</h2>
<p> setarch &#8211;addr-no-randomize mytestprog<br />
 setarch ppc32 rpmbuild &#8211;target=ppc &#8211;rebuild foo.src.rpm<br />
 setarch ppc32 -v -vL3 rpmbuild &#8211;target=ppc &#8211;rebuild bar.src.rpm<br />
 setarch ppc32 &#8211;32bit rpmbuild &#8211;target=ppc &#8211;rebuild foo.src.rpm</p>
<h2>AUTHOR</h2>
<p> Elliot Lee<br />
 Jindrich Novy<br />
 Karel Zak</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2)</p>
<h2>AVAILABILITY</h2>
<p> The setarch command is part of the util-linux package and is available from Linux Kernel Archive </p>
<h2>Index</h2>
