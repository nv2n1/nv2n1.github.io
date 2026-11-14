---
title: "hardening-check(1)"
name: "hardening-check"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hardening-check/"
description: "hardening-check – check binaries for security hardening features"
---

<h2 class="name">NAME</h2>
<p> hardening-check &#8211; check binaries for security hardening features </p>
<h2>SYNOPSIS</h2>
<p> hardening-check [options] [<font SIZE="-1">ELF &#8230;</font>] </p>
<p> Examine a given set of <font SIZE="-1">ELF</font> binaries and check for several security hardening features, failing if they are not all found.</p>
<h2>DESCRIPTION</h2>
<p> This utility checks a given list of <font SIZE="-1">ELF</font> binaries for several security hardening features that can be compiled into an executable. These features are:</p>
<dl>
<dt><code>Position Independent Executable</code></p>
<dd> This indicates that the executable was built in such a way (<font SIZE="-1">PIE</font>) that the &#8220;text&#8221; section of the program can be relocated in memory. To take full advantage of this feature, the executing kernel must support text Address Space Layout Randomization (<font SIZE="-1">ASLR</font>).</p>
<dt><code>Stack Protected</code></p>
<dd> This indicates that there is evidence that the <font SIZE="-1">ELF</font> was compiled with the <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1) option <code>-fstack-protector</code> (e.g. uses <code>__stack_chk_fail</code>). The program will be resistant to having its stack overflowed. </p>
<p> When an executable was built without any character arrays being allocated on the stack, this check will lead to false alarms (since there is no use of <code>__stack_chk_fail</code>), even though it was compiled with the correct options.</p>
<dt><code>Fortify Source functions</code></p>
<dd> This indicates that the executable was compiled with <code>-D_FORTIFY_SOURCE=2</code> and <code>-O1</code> or higher. This causes certain unsafe glibc functions with their safer counterparts (e.g. <code>strncpy</code> instead of <code>strcpy</code>), or replaces calls that are verifiable at runtime with the runtime-check version (e.g. <code>__memcpy_chk</code> insteade of <code>memcpy</code>). </p>
<p> When an executable was built such that the fortified versions of the glibc functions are not useful (e.g. use is verified as safe at compile time, or use cannot be verified at runtime), this check will lead to false alarms. In an effort to mitigate this, the check will pass if any fortified function is found, and will fail if only unfortified functions are found. Uncheckable conditions also pass (e.g. no functions that could be fortified are found, or not linked against glibc).</p>
<dt><code>Read-only relocations</code></p>
<dd> This indicates that the executable was build with <code>-Wl,-z,relro</code> to have <font SIZE="-1">ELF</font> markings (<font SIZE="-1">RELRO</font>) that ask the runtime linker to mark any regions of the relocation table as &#8220;read-only&#8221; if they were resolved before execution begins. This reduces the possible areas of memory in a program that can be used by an attacker that performs a successful memory corruption exploit.</p>
<dt><code>Immediate binding</code></p>
<dd> This indicates that the executable was built with <code>-Wl,-z,now</code> to have <font SIZE="-1">ELF</font> markings (<font SIZE="-1">BIND_NOW</font>) that ask the runtime linker to resolve all relocations before starting program execution. When combined with <font SIZE="-1">RELRO</font> above, this further reduces the regions of memory available to memory corruption attacks.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;nopie</code>, <code>-p</code></p>
<dd> No not require that the checked binaries be built as <font SIZE="-1">PIE.</font></p>
<dt><code>&#8211;nostackprotector</code>, <code>-s</code></p>
<dd> No not require that the checked binaries be built with the stack protector.</p>
<dt><code>&#8211;nofortify</code>, <code>-f</code></p>
<dd> No not require that the checked binaries be built with Fority Source.</p>
<dt><code>&#8211;norelro</code>, <code>-r</code></p>
<dd> No not require that the checked binaries be built with <font SIZE="-1">RELRO.</font></p>
<dt><code>&#8211;nobindnow</code>, <code>-b</code></p>
<dd> No not require that the checked binaries be built with <font SIZE="-1">BIND_NOW.</font></p>
<dt><code>&#8211;quiet</code>, <code>-q</code></p>
<dd> Only report failures.</p>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd> Report verbosely on failures.</p>
<dt><code>&#8211;report-functions</code>, <code>-R</code></p>
<dd> After the report, display all external functions needed by the <font SIZE="-1">ELF.</font></p>
<dt><code>&#8211;find-libc-functions</code>, <code>-F</code></p>
<dd> Instead of the regular report, locate the libc for the first <font SIZE="-1">ELF</font> on the command line and report all the known &#8220;fortified&#8221; functions exported by libc.</p>
<dt><code>&#8211;color</code>, <code>-c</code></p>
<dd> Enable colorized status output.</p>
<dt><code>&#8211;lintian</code>, <code>-l</code></p>
<dd> Switch reporting to lintian-check-parsable output.</p>
<dt><code>&#8211;debug</code></p>
<dd> Report some debugging during processing.</p>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></p>
<dd> Print a brief help message and exit.</p>
<dt><code>&#8211;man</code>, <code>-H</code></p>
<dd> Print the manual page and exit.</dl>
<h2>RETURN VALUE</h2>
<p> When all checked binaries have all checkable hardening features detected, this program will finish with an exit code of 0. If any check fails, the exit code with be 1. Individual checks can be disabled via command line options.</p>
<h2>AUTHOR</h2>
<p> Kees Cook &lt;kees [at] debian.org&gt;</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 2009-2013 Kees Cook &lt;kees [at] debian.org&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; version 2 or later.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-hardening-wrapper/">hardening-wrapper</a></i>(1) </p>
<h2>Index</h2>
