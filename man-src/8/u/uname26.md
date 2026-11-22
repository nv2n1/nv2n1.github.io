---
title: "uname26(8)"
name: "uname26"
section: "8"
letter: "u"
url: "/docs/linux/man/8-uname26/"
description: "setarch – change reported architecture in new program environment and set personality flags"
---

<p>setarch &#8211; change reported architecture in new program environment and set personality flags</p>
<h2>Synopsis</h2>
<p><code>setarch</code> <i>arch</i> [options] [<i>program</i> [<i>argument</i>&#8230;]] </p>
<p> <code>arch</code> [options] [<i>program</i> [<i>argument</i>&#8230;]] </p>
<p> <code>setarch</code> <code>&#8211;list</code>|<code>-h</code>|<code>-V</code></p>
<h2>Description</h2>
<p><code>setarch</code> currently only affects the output of <code>uname -m</code>. For example, on an AMD64 system, running <code>setarch i386 </code><i>program</i> will cause <i>program</i> to see i686 instead of x86_64 as the machine type. It also allows to set various personality options. The default <i>program</i> is <code>/bin/sh</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;list</code></dt>
<dd>List the architectures that <code>setarch</code> knows about. Whether <code>setarch</code> can actually set each of these architectures depends on the running kernel.</dd>
<dt><code>&#8211;uname-2.6</code></dt>
<dd>Causes the <i>program</i> to see a kernel version number beginning with 2.6.</dd>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd>Be verbose.</dd>
<dt><code>-3</code>, <code>&#8211;3gb</code></dt>
<dd>Specifies that processes should use a maximum of 3GB of address space on systems where it is supported (ADDR_LIMIT_3GB).</dd>
<dt><code>&#8211;4gb</code></dt>
<dd>Ignored (for backward compatibility only).</dd>
<dt><code>-B</code>, <code>&#8211;32bit</code></dt>
<dd>Turns on ADDR_LIMIT_32BIT.</dd>
<dt><code>-F</code>, <code>&#8211;fdpic-funcptrs</code></dt>
<dd>Userspace function pointers point to descriptors (turns on FDPIC_FUNCPTRS).</dd>
<dt><code>-I</code>, <code>&#8211;short-inode</code></dt>
<dd>Turns on SHORT_INODE.</dd>
<dt><code>-L</code>, <code>&#8211;addr-compat-layout</code></dt>
<dd>Changes the way virtual memory is allocated (turns on the ADDR_COMPAT_LAYOUT).</dd>
<dt><code>-R</code>, <code>&#8211;addr-no-randomize</code></dt>
<dd>Disables randomization of the virtual address space (turns on ADDR_NO_RANDOMIZE).</dd>
<dt><code>-S</code>, <code>&#8211;whole-seconds</code></dt>
<dd>Turns on WHOLE_SECONDS.</dd>
<dt><code>-T</code>, <code>&#8211;sticky-timeouts</code></dt>
<dd>Turns on STICKY_TIMEOUTS.</dd>
<dt><code>-X</code>, <code>&#8211;read-implies-exec</code></dt>
<dd>Turns on READ_IMPLIES_EXEC.</dd>
<dt><code>-Z</code>, <code>&#8211;mmap-page-zero</code></dt>
<dd>Turns on MMAP_PAGE_ZERO.</dd>
<dt><code>-V</code>,<code> &#8211;version</code></dt>
<dd>Display version information and exit.</dd>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd>Display help text and exit.</dd></dl>
<h2>Examples</h2>
<p>setarch ppc32 rpmbuild &#8211;target=ppc &#8211;rebuild foo.src.rpm<br/>
 setarch ppc32 -v -vL3 rpmbuild &#8211;target=ppc &#8211;rebuild bar.src.rpm<br/>
 setarch ppc32 &#8211;32bit rpmbuild &#8211;target=ppc &#8211;rebuild foo.src.rpm</p>
<h2>Author</h2>
<p>Elliot Lee<br/>
 Jindrich Novy</p>
<h2>Availability</h2>
<p>The setarch command is part of the util-linux package and is available from Linux Kernel Archive</p>
