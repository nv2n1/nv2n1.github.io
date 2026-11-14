---
title: "cpu_model(3)"
name: "cpu_model"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpu_model/"
description: "cpu_model – Contains the Intel CPU submodel. Allegro game programming library."
---

<h2>NAME</h2>
<p> cpu_model &#8211; Contains the Intel CPU submodel. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int cpu_model;</code></p>
<h2>DESCRIPTION</h2>
<p> Contains the CPU submodel, where applicable. Allegro defines at least the following CPU family types (see include/allegro/system.h for a more complete list): </p>
<pre>
   CPU_FAMILY_I586:
      CPU_MODEL_PENTIUM, CPU_MODEL_K5, CPU_MODEL_K6
   
   CPU_FAMILY_I686:
      CPU_MODEL_PENTIUMPRO, CPU_MODEL_PENTIUMII,
      CPU_MODEL_PENTIUMIIIKATMAI, CPU_MODEL_PENTIUMIIICOPPERMINE,
      CPU_MODEL_ATHLON, CPU_MODEL_DURON
   
   CPU_FAMILY_EXTENDED:
      CPU_MODEL_PENTIUMIV, CPU_MODEL_XEON,
      CPU_MODEL_ATHLON64, CPU_MODEL_OPTERON
   
   CPU_FAMILY_POWERPC:
      CPU_MODEL_POWERPC_x, for x=601-604, 620, 750, 7400, 7450
   
</pre>
<p> You can read this variable after you have called check_cpu() (which is automatically called by allegro_init()). Make sure you check the cpu_family and cpu_vendor so you know which models make sense to check. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-check_cpu/">check_cpu</a></code>(3), <code><a href="/docs/linux/man/3-cpu_vendor/">cpu_vendor</a></code>(3), <code><a href="/docs/linux/man/3-cpu_family/">cpu_family</a></code>(3), <code><a href="/docs/linux/man/3-cpu_capabilities/">cpu_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3) </p>
<h2>Index</h2>
