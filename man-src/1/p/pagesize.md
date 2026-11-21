---
title: "pagesize(1)"
name: "pagesize"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pagesize/"
description: "pagesize – Print supported system page sizes"
---

<h2>SYNOPSIS</h2>
<p> <code>pagesize [options]</code></p>
<h2>DESCRIPTION</h2>
<p> The pagesize utility prints the page sizes of a page of memory in bytes, as returned by getpagesizes(3). This is useful when creating portable shell scripts, configuring huge page pools with hugeadm or launching applications to use huge pages with hugectl. </p>
<p> If no parameters are specified, <code>pagesize</code> prints the system base page size as returned by <code>getpagesize()</code>. The following parameters affect what other pagesizes are displayed. </p>
<dl>
<dt><code>&#8211;huge-only, -H</code></dt>
<dd>
<p> Display all huge pages supported by the system as returned by <code>gethugepagesizes()</code>. </p>
</dd><dt><code>&#8211;all, -a</code></dt>
<dd>
<p> Display all page sizes supported by the system. </p>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1),</i> <i><a href="/docs/linux/man/2-getpagesize/">getpagesize</a>(2),</i> <i>getpagesizes(3),</i> <i>gethugepagesizes(3),</i> <i>hugectl(7),</i> <i>hugeadm(7),</i> <i><a href="/docs/linux/man/7-libhugetlbfs/">libhugetlbfs</a>(7)</i> </p>
<h2>AUTHORS</h2>
<p> libhugetlbfs was written by various people on the libhugetlbfs-devel mailing list. </p>
