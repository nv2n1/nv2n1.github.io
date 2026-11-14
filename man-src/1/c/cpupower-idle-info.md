---
title: "cpupower-idle-info(1)"
name: "cpupower-idle-info"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpupower-idle-info/"
description: "cpupower idle-info – Utility to retrieve cpu idle kernel information"
---

<h2>NAME</h2>
<p> cpupower idle-info &#8211; Utility to retrieve cpu idle kernel information</p>
<h2>SYNTAX</h2>
<p> cpupower [ -c cpulist ] idle-info [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> A tool which prints out per cpu idle information helpful to developers and interested users.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> <code>&#8211;silent</code></p>
<dd> Only print a summary of all available C-states in the system.</p>
<dt><code>-e</code> <code>&#8211;proc</code></p>
<dd> deprecated. Prints out idle information in old /proc/acpi/processor/*/power format. This interface has been removed from the kernel for quite some time, do not let further code depend on this option, best do not use it. </p>
</dl>
<h2>IDLE-INFO DESCRIPTIONS</h2>
<p> CPU sleep state statistics and descriptions are retrieved from sysfs files, exported by the cpuidle kernel subsystem. The kernel only updates these statistics when it enters or leaves an idle state, therefore on a very idle or a very busy system, these statistics may not be accurate. They still provide a good overview about the usage and availability of processor sleep states on the platform. </p>
<p> Be aware that the sleep states as exported by the hardware or BIOS and used by the Linux kernel may not exactly reflect the capabilities of the processor. This often is the case on the X86 architecture when the acpi_idle driver is used. It is also possible that the hardware overrules the kernel requests, due to internal activity monitors or other reasons. On recent X86 platforms it is often possible to read out hardware registers which monitor the duration of sleep states the processor resided in. The cpupower monitor tool (<a href="/docs/linux/man/1-cpupower-monitor/">cpupower-monitor</a>(1)) can be used to show real sleep state residencies. Please refer to the architecture specific description section below. </p>
<h2>IDLE-INFO ARCHITECTURE SPECIFIC DESCRIPTIONS</h2>
<h3>X86</h3>
<p> POLL idle state </p>
<p> If cpuidle is active, X86 platforms have one special idle state. The POLL idle state is not a real idle state, it does not save any power. Instead, a busy-loop is executed doing nothing for a short period of time. This state is used if the kernel knows that work has to be processed very soon and entering any real hardware idle state may result in a slight performance penalty. </p>
<p> There exist two different cpuidle drivers on the X86 architecture platform: </p>
<p> &quot;acpi_idle&quot; cpuidle driver </p>
<p> The acpi_idle cpuidle driver retrieves available sleep states (C-states) from the ACPI BIOS tables (from the _CST ACPI function on recent platforms or from the FADT BIOS table on older ones). The C1 state is not retrieved from ACPI tables. If the C1 state is entered, the kernel will call the hlt instruction (or mwait on Intel). </p>
<p> &quot;intel_idle&quot; cpuidle driver </p>
<p> In kernel 2.6.36 the intel_idle driver was introduced. It only serves recent Intel CPUs (Nehalem, Westmere, Sandybridge, Atoms or newer). On older Intel CPUs the acpi_idle driver is still used (if the BIOS provides C-state ACPI tables). The intel_idle driver knows the sleep state capabilities of the processor and ignores ACPI BIOS exported processor sleep states tables. </p>
<h2>REMARKS</h2>
<p> By default only values of core zero are displayed. How to display settings of other cores is described in the <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1) manpage in the &#8211;cpu option section.</p>
<h2>REFERENCES</h2>
<p> <a rel="nofollow" href="http://www.acpi.info/spec.htm">http://www.acpi.info/spec.htm</a></p>
<h2>FILES</h2>
<pre>
<i>/sys/devices/system/cpu/cpu*/cpuidle/state*</i>
<i>/sys/devices/system/cpu/cpuidle/*</i>
</pre>
<h2>AUTHORS</h2>
<pre>
Thomas Renninger &lt;trenn [at] suse.de&gt;
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1), <a href="/docs/linux/man/1-cpupower-monitor/">cpupower-monitor</a>(1), <a href="/docs/linux/man/1-cpupower-info/">cpupower-info</a>(1), <a href="/docs/linux/man/1-cpupower-set/">cpupower-set</a>(1), <a href="/docs/linux/man/1-cpupower-idle-set/">cpupower-idle-set</a>(1) </p>
<h2>Index</h2>
