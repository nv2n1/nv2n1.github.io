---
title: "x86_energy_perf_policy(8)"
name: "x86_energy_perf_policy"
section: "8"
letter: "x"
url: "/docs/linux/man/8-x86_energy_perf_policy/"
description: "x86_energy_perf_policy – read or write MSR_IA32_ENERGY_PERF_BIAS"
---

<p>x86_energy_perf_policy &#8211; read or write MSR_IA32_ENERGY_PERF_BIAS</p>
<h2>Synopsis</h2>
<p><code> x86_energy_perf_policy</code> [<code>-c cpu</code>] [<code>-v</code>] -r<br />
 <code>x86_energy_perf_policy</code> [<code>-c cpu</code>] [<code>-v</code>] &#8216;performance&#8217;<br />
 <code>x86_energy_perf_policy</code> [<code>-c cpu</code>] [<code>-v</code>] &#8216;normal&#8217;<br />
 <code>x86_energy_perf_policy</code> [<code>-c cpu</code>] [<code>-v</code>] &#8216;powersave&#8217;<br />
 <code>x86_energy_perf_policy</code> [<code>-c cpu</code>] [<code>-v</code>] n</p>
<h2>Description</h2>
<p><code>x86_energy_perf_policy</code> allows software to convey its policy for the relative importance of performance versus energy savings to the processor. The processor uses this information in model-specific ways when it must select trade-offs between performance and energy efficiency. This policy hint does not supersede Processor Performance states (P-states) or CPU Idle power states (C-states), but allows software to have influence where it would otherwise be unable to express a preference. For example, this setting may tell the hardware how aggressively or conservatively to control frequency in the &quot;turbo range&quot; above the explicitly OS-controlled P-state frequency range. It may also tell the hardware how aggressively is should enter the OS requested C-states. Support for this feature is indicated by CPUID.06H.ECX.bit3 per the Intel Architectures Software Developer&#8217;s Manual.</p>
<h3>Options</h3>
<p><code>-c</code> limits operation to a single CPU. The default is to operate on all CPUs. Note that MSR_IA32_ENERGY_PERF_BIAS is defined per logical processor, but that the initial implementations of the MSR were shared among all processors in each package. <code>-v</code> increases verbosity. By default x86_energy_perf_policy is silent. <code>-r</code> is for &quot;read-only&quot; mode &#8211; the unchanged state is read and displayed. <i>performance</i> Set a policy where performance is paramount. The processor will be unwilling to sacrifice any performance for the sake of energy saving. This is the hardware default. <i>normal</i> Set a policy with a normal balance between performance and energy efficiency. The processor will tolerate minor performance compromise for potentially significant energy savings. This reasonable default for most desktops and servers. <i>powersave</i> Set a policy where the processor can accept a measurable performance hit to maximize energy efficiency. <i>n</i> Set MSR_IA32_ENERGY_PERF_BIAS to the specified number. The range of valid numbers is 0-15, where 0 is maximum performance and 15 is maximum energy efficiency. </p>
<h2>Notes</h2>
<p><code>x86_energy_perf_policy </code> runs only as root.</p>
<h2>Files</h2>
<pre>/dev/cpu/*/msr</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/4-msr/">msr</a>(4) </p>
<h2>Authors</h2>
<pre>Written by Len Brown &lt;len.brown [at] intel.com&gt;</pre>
