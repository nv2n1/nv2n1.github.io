---
title: "outsw(2)"
name: "outsw"
section: "2"
letter: "o"
url: "/docs/linux/man/2-outsw/"
description: "outb, outw, outl, outsb, outsw, outsl, inb, inw, inl, insb, insw, insl, outb_p, outw_p, outl_p, inb_p, inw_p, inl_p – port I/O"
---

<h2 class="name">NAME</h2>
<p> outb, outw, outl, outsb, outsw, outsl, inb, inw, inl, insb, insw, insl, outb_p, outw_p, outl_p, inb_p, inw_p, inl_p &#8211; port I/O </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/io.h&gt;
unsigned char inb(unsigned short port);
unsigned char inb_p(unsigned short port);
unsigned short inw(unsigned short port);
unsigned short inw_p(unsigned short port);
unsigned int inl(unsigned short port);
unsigned int inl_p(unsigned short port);
void outb(unsigned char value, unsigned short port);
void outb_p(unsigned char value, unsigned short port);
void outw(unsigned short value, unsigned short port);
void outw_p(unsigned short value, unsigned short port);
void outl(unsigned int value, unsigned short port);
void outl_p(unsigned int value, unsigned short port);
void insb(unsigned short port, void *addr,
          unsigned long count);
void insw(unsigned short port, void *addr,
          unsigned long count);
void insl(unsigned short port, void *addr,
          unsigned long count);
void outsb(unsigned short port, const void *addr,
           unsigned long count);
void outsw(unsigned short port, const void *addr,
           unsigned long count);
void outsl(unsigned short port, const void *addr,
           unsigned long count);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This family of functions is used to do low-level port input and output. The out* functions do port output, the in* functions do port input; the b-suffix functions are byte-width and the w-suffix functions word-width; the _p-suffix functions pause until the I/O completes. </p>
<p> They are primarily designed for internal kernel use, but can be used from user space. </p>
<p> You must compile with <code>-O</code> or <code>-O2</code> or similar. The functions are defined as inline macros, and will not be substituted in without optimization enabled, causing unresolved references at link time. </p>
<p> You use <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2) or alternatively <code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2) to tell the kernel to allow the user space application to access the I/O ports in question. Failure to do this will cause the application to receive a segmentation fault.</p>
<h2>CONFORMING TO</h2>
<p> <code>outb</code>() and friends are hardware-specific. The <i>value</i> argument is passed first and the <i>port</i> argument is passed second, which is the opposite order from most DOS implementations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2), <code><a href="/docs/linux/man/2-iopl/">iopl</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
