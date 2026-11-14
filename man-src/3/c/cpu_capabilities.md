---
title: "cpu_capabilities(3)"
name: "cpu_capabilities"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpu_capabilities/"
description: "cpu_capabilities – Contains the capability flags of the CPU. Allegro game programming library."
---

<h2>NAME</h2>
<p> cpu_capabilities &#8211; Contains the capability flags of the CPU. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int cpu_capabilities;</code></p>
<h2>DESCRIPTION</h2>
<p> Contains CPU flags indicating what features are available on the current CPU. The flags can be any combination of these: </p>
<pre>
   CPU_ID       - Indicates that the &quot;cpuid&quot; instruction is
                  available. If this is set, then all Allegro CPU
                  variables are 100% reliable, otherwise there
                  may be some mistakes.
   CPU_FPU      - An FPU is available.
   CPU_IA64     - Running on Intel 64 bit CPU
   CPU_AMD64    - Running on AMD 64 bit CPU
   CPU_MMX      - Intel MMX  instruction set is available.
   CPU_MMXPLUS  - Intel MMX+ instruction set is available.
   CPU_SSE      - Intel SSE  instruction set is available.
   CPU_SSE2     - Intel SSE2 instruction set is available.
   CPU_SSE3     - Intel SSE3 instruction set is available.
   CPU_3DNOW    - AMD 3DNow! instruction set is available.
   CPU_ENH3DNOW - AMD Enhanced 3DNow! instruction set is
                  available.
   CPU_CMOV     - Pentium Pro &quot;cmov&quot; instruction is available.
   
</pre>
<p> You can check for multiple features by OR-ing the flags together. For example, to check if the CPU has an FPU and MMX instructions available, you&#8217;d do: </p>
<pre><code>
if ((cpu_capabilities &amp; (CPU_FPU | CPU_MMX)) ==
    (CPU_FPU | CPU_MMX)) {
    printf("CPU has both an FPU and MMX instructions!
");
}
</code></pre>
<p> You can read this variable after you have called check_cpu() (which is automatically called by allegro_init()). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-check_cpu/">check_cpu</a></code>(3), <code><a href="/docs/linux/man/3-cpu_vendor/">cpu_vendor</a></code>(3), <code><a href="/docs/linux/man/3-cpu_family/">cpu_family</a></code>(3), <code><a href="/docs/linux/man/3-cpu_model/">cpu_model</a></code>(3), <code><a href="/docs/linux/man/3-cpu_capabilities/">cpu_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3) </p>
<h2>Index</h2>
