---
title: "arch_phys_wc_add(9)"
name: "arch_phys_wc_add"
section: "9"
letter: "a"
url: "/docs/linux/man/9-arch_phys_wc_add/"
---

arch_phys_wc_add - add a WC MTRR and handle errors if PAT is unavailable

<h2>Synopsis</h2>

<pre><code>int arch_phys_wc_add(unsigned long base, unsigned long size);</code></pre>

<h2>Arguments</h2>

<i>base</i>
<dl><dd><dd>Physical base address</dl>
 

 <i>size</i>
<dl><dd>Size of region</dl>

<h2>Description</h2>

If PAT is available, this does nothing. If PAT is unavailable, it attempts to add a WC MTRR covering size bytes starting at base and logs an error if this fails. 

 The called should provide a power of two size on an equivalent power of two boundary. 

 Drivers must store the return value to pass to mtrr_del_wc_if_needed, but drivers should not try to interpret that return value.

<h2>Copyright</h2>


