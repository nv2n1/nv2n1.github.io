---
title: "ustr-import(1)"
name: "ustr-import"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ustr-import/"
description: "ustr-import – ustr string library import tool"
---

<h2>NAME</h2>
<p> ustr-import &#8211; ustr string library import tool</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ustr-import</code> [&#8211;32|&#8211;64] [-d][d] [-c] [-b x] [-e 1|0] [-s 1|0] section </p>
<dl>
<dt>&#8211;32</p>
<dd>
<dd>If you installed with multilib, this runs the 32 bit varient (and installs the variable multilib build code as ustr-conf.h). </p>
<dt>&#8211;64</p>
<dd> If you installed with multilib, this runs the 64 bit varient (and installs the variable multilib build code as ustr-conf.h). </p>
<dt>-d</p>
<dd> Turn debugging on, USTR_ASSERT() now runs code etc. </p>
<dt>-d</p>
<dd> Turn extra debugging on, including End of String (EOS) markers that takeup space. Note that you can do -dd to add both at once. </p>
<dt>-c</p>
<dd> Use C files, this requires that you alter the build system to compile the C files and link them into your application. The default is to just provide headers that you can just include. </p>
<dt>-b</p>
<dd> Specify the default reference count byte size: 0, 1, 2 or 4 (or 8 on 64 bit platforms). Note that 2 bytes is the minimum if you have explicit size storage. </p>
<dt>-e</p>
<dd> Specify the default exact sized allocations flag, without this flag allocations are rounded up to the neared half power of two. </p>
<dt>-s</p>
<dd> Specify the default explicit size storage flag, without this flag allocations have an implicit size based on their length with it a size value is stored with the string (thus taking significantly larger space for small strings, but this doesn&#8217;t require reallocating the string when growing and shrinking the string). Note that turning this on also increases the minimum sizes for length and reference count storage. </p>
</dl>
<h2>SECTIONS</h2>
<dl>
<dt>all</p>
<dd> All of the following sections are included. </p>
<dt>b</p>
<dd> Working with binary numbers in NBO format. </p>
<dt>cmp</p>
<dd> Comparing, strcmp() for Ustr&#8217;s, although the Ustr versions are safer and much faster. </p>
<dt>cntl</p>
<dd> Control options dynamically. </p>
<dt>fmt</p>
<dd> Formatted output, sprintf() for Ustr&#8217;s. </p>
<dt>gdb</p>
<dd> Copy just the .gdbinit file to the local dir. </p>
<dt>io</p>
<dd> Input Output. </p>
<dt>ins</p>
<dd> Inserting data. </p>
<dt>main</p>
<dd> The core functions, including strcat(), strdup() and delete for Ustr&#8217;s. Always safer and often much faster. </p>
<dt>parse</p>
<dd> Parsing integers, Ie. Nice versions of strtol(). </p>
<dt>pool</p>
<dd> A bundled memory pool API, to use with the ustrp functions. </p>
<dt>replace</p>
<dd> Replacing all occurances of data. </p>
<dt>sc</p>
<dd> Shortcut functions for Ustr&#8217;s. </p>
<dt>set</p>
<dd> Setting data, strcpy() for Ustr&#8217;s. </p>
<dt>split</p>
<dd> Slit the data, strtok() / strsep() for Ustr&#8217;s. </p>
<dt>spn</p>
<dd> Spanning, strspn() / strcspn() for Ustr&#8217;s. </p>
<dt>srch</p>
<dd> Searching, strchr() / strrchr() / strstr() for Ustr&#8217;s, although the Ustr versions are safer and much faster. </p>
<dt>sub</p>
<dd> Substituting data. </p>
<dt>utf8</p>
<dd> Working with UTF8. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/ustr/include/ustr-conf.h</i> <i>/ustr/include/ustr-conf-debug.h</i></p>
<dd> In multilib. this is the header to choose the correct conf.h header based on the byte size. </p>
<dt><i>/ustr/include/ustr*.h</i></p>
<dd> The default &quot;extern&quot; header files. </p>
<dt><i>/usr/share/ustr-*/ustr-*-internal.h</i></p>
<dd> Internal functions, used the implement the public interfaces. </p>
<dt><i>/usr/share/ustr-*/ustr-*-code.h</i></p>
<dd> The code behind the public interfaces. </p>
<dt><i>/usr/share/ustr-*/ustr-*-code.c</i></p>
<dd> The C files, which use the code header files to create objects. </p>
<dt><i>/usr/share/ustr-*/.gdbinit</i></p>
<dd> The GDB init file containing macros to help inspect Ustr&#8217;s in the debugger. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ustr/">ustr</a></code>(3),<code><a href="/docs/linux/man/3-ustr_const/">ustr_const</a></code>(3) </p>
<h2>Index</h2>
