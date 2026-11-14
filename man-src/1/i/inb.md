---
title: "inb(1)"
name: "inb"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inb/"
---

<h2 class="name">NAME</h2>
 

 inb, outb, inw, outw, inl, outl - access I/O ports 

<h2>SYNOPSIS</h2>

 <pre>
 inb ADDRESS
 inw ADDRESS
 inl ADDRESS
 outb ADDRESS DATA
 outw ADDRESS DATA
 outl ADDRESS DATA
</pre>

<h2>EXAMPLES</h2>

 <pre>
 inb 0x278
 outw 0x440 0xffff
</pre>

<h2>DESCRIPTION</h2>

 These commands enable command line and script access directly to I/O ports on <font SIZE="-1">PC</font> hardware. 

 The <tt>&quot;inb&quot;</tt>, <tt>&quot;inw&quot;</tt> and <tt>&quot;inl&quot;</tt> commands perform an input (read) operation on the given I/O port, and print the result. 

 The <tt>&quot;outb&quot;</tt>, <tt>&quot;outw&quot;</tt> and <tt>&quot;outl&quot;</tt> commands perform an output (write) operation to the given I/O port, sending the given data. Note that the order of the parameters is <font SIZE="-1">ADDRESS</font> <font SIZE="-1">DATA</font>. 

 The size of the operation is selected according to the suffix, with <tt>&quot;b&quot;</tt> meaning byte, <tt>&quot;w&quot;</tt> meaning word (16 bits) and <tt>&quot;l&quot;</tt> meaning long (32 bits). 

 Port numbers are in the range 0-0xffff. We don't support access to memory mapped devices. 

 Hexadecimal numbers (prefixed by <tt>&quot;0x&quot;</tt>), decimal numbers, and octal numbers (prefixed by <tt>0</tt>), are allowed as parameters.

<h2>RETURN FROM IN OPERATIONS</h2>

 The value read from the port by an ``in'' operation is normally printed in decimal. 

 Use the <tt>&quot;--hex&quot;</tt> option to print the result as hexadecimal (<tt>&quot;0x&quot;</tt> prefix is <font SIZE="-1">NOT</font> printed). 

 Use the <tt>&quot;--code&quot;</tt> option to turn the result into an exit status. Note that Unix/shell can only reliably return exit status in the range 0-0x7f, so this is not particularly useful in practice.

<h2>TYPE AND SIZE OF OPERATION</h2>

 The type and size of the operation is normally determined by the name of the command, eg. <tt>&quot;inb&quot;</tt> is a read operation of 1 byte. 

 You can override this by using the <tt>&quot;--read&quot;</tt>, <tt>&quot;--write&quot;</tt> and/or <tt>&quot;--size N&quot;</tt> options. For <tt>&quot;--size N&quot;</tt>, <tt>&quot;N&quot;</tt> should be <tt>1</tt>, <tt>2</tt> or <tt>4</tt> meaning byte, word and long respectively.

<h2>PERMISSIONS</h2>

 You would normally need to be root or have the <tt>&quot;CAP_SYS_RAWIO&quot;</tt> capability in order to run these commands.

<h2>WARNING</h2>

 Using these commands can cause Bad Things to happen to your hardware.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/2-iopl/">iopl</a></i>(2), <i><a HREF="/docs/linux/man/4-mem/">mem</a></i>(4), &lt;<a rel="nofollow" HREF="http://et.redhat.com/~rjones/ioport">http://et.redhat.com/~rjones/ioport</a>&gt;, &lt;<a rel="nofollow" HREF="http://www.faqs.org/docs/Linux-mini/IO-Port-Programming.html">http://www.faqs.org/docs/Linux-mini/IO-Port-Programming.html</a>&gt;.

<h2>AUTHORS</h2>

 Richard W.M. Jones &lt;rjones @ redhat . com&gt;

<h2>COPYRIGHT</h2>

 (C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" HREF="http://et.redhat.com/~rjones/ioport">http://et.redhat.com/~rjones/ioport</a>&gt;. 

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>. 

<h2>Index</h2>


