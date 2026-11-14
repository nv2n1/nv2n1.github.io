---
title: "cpu_family(3)"
name: "cpu_family"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpu_family/"
description: "cpu_family – Contains the CPU type. Allegro game programming library."
---

<h2>NAME</h2>
<p> cpu_family &#8211; Contains the CPU type. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int cpu_family;</code></p>
<h2>DESCRIPTION</h2>
<p> Contains the Intel type, where applicable. Allegro defines the following CPU family types: </p>
<pre>
   CPU_FAMILY_UNKNOWN  - The type of processor is unknown
   CPU_FAMILY_I386     - The processor is an Intel-compatible 386
   CPU_FAMILY_I486     - The processor is an Intel-compatible 486
   CPU_FAMILY_I586     - The processor is a Pentium or equivalent
   CPU_FAMILY_I686     - The processor is a Pentium Pro, II, III
                         or equivalent
   CPU_FAMILY_ITANIUM  - The processor is an Itanium processor
   CPU_FAMILY_POWERPC  - The processor is a PowerPC processor
   CPU_FAMILY_EXTENDED - The processor type needs to be read
                         from the cpu_model
   
</pre>
<p> You can read this variable after you have called check_cpu() (which is automatically called by allegro_init()). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-check_cpu/">check_cpu</a></code>(3), <code><a href="/docs/linux/man/3-cpu_vendor/">cpu_vendor</a></code>(3), <code><a href="/docs/linux/man/3-cpu_model/">cpu_model</a></code>(3), <code><a href="/docs/linux/man/3-cpu_capabilities/">cpu_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3) </p>
<h2>Index</h2>
