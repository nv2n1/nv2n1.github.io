---
title: "cpupower-set(1)"
name: "cpupower-set"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpupower-set/"
description: "cpupower-set – Set processor power related kernel or hardware configurations"
---

<h2>NAME</h2>
<p> cpupower-set &#8211; Set processor power related kernel or hardware configurations</p>
<h2>SYNOPSIS</h2>
<p> <code> cpupower set [ -b VAL ]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>cpupower set </code> sets kernel configurations or directly accesses hardware registers affecting processor power saving policies. </p>
<p> Some options are platform wide, some affect single cores. By default values are applied on all cores. How to modify single core configurations is described in the <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1) manpage in the &#8211;cpu option section. Whether an option affects the whole system or can be applied to individual cores is described in the Options sections. </p>
<p> Use <code>cpupower info </code> to read out current settings and whether they are supported on the system at all. </p>
<h2>Options</h2>
<p> &#8211;perf-bias, -b</p>
<dl>
<dt>
<dd> Sets a register on supported Intel processore which allows software to convey its policy for the relative importance of performance versus energy savings to the processor. </p>
<p> The range of valid numbers is 0-15, where 0 is maximum performance and 15 is maximum energy efficiency. </p>
<p> The processor uses this information in model-specific ways when it must select trade-offs between performance and energy efficiency. </p>
<p> This policy hint does not supersede Processor Performance states (P-states) or CPU Idle power states (C-states), but allows software to have influence where it would otherwise be unable to express a preference. </p>
<p> For example, this setting may tell the hardware how aggressively or conservatively to control frequency in the &quot;turbo range&quot; above the explicitly OS-controlled P-state frequency range. It may also tell the hardware how aggressively it should enter the OS requested C-states. </p>
<p> This option can be applied to individual cores only via the &#8211;cpu option, <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1). </p>
<p> Setting the performance bias value on one CPU can modify the setting on related CPUs as well (for example all CPUs on one socket), because of hardware restrictions. Use <code>cpupower -c all info -b</code> to verify. </p>
<p> This options needs the msr kernel driver (CONFIG_X86_MSR) loaded.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cpupower-info/">cpupower-info</a>(1), <a href="/docs/linux/man/1-cpupower-monitor/">cpupower-monitor</a>(1), <a href="/docs/linux/man/1-powertop/">powertop</a>(1) </p>
<h2>AUTHORS</h2>
<pre><code>
--perf - bias parts written by Len Brown&lt;len.brown[at] intel.com&gt;
             Thomas Renninger&lt;trenn[at] suse.de&gt;
</code></pre>
<h2>Index</h2>
