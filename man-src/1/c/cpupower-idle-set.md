---
title: "cpupower-idle-set(1)"
name: "cpupower-idle-set"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpupower-idle-set/"
description: "cpupower idle-set – Utility to set cpu idle state specific kernel options"
---

<h2>NAME</h2>
<p> cpupower idle-set &#8211; Utility to set cpu idle state specific kernel options</p>
<h2>SYNTAX</h2>
<p> cpupower [ -c cpulist ] idle-info [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The cpupower idle-set subcommand allows to set cpu idle, also called cpu sleep state, specific options offered by the kernel. One example is disabling sleep states. This can be handy for power vs performance tuning.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> <code>&#8211;disable</code> &lt;STATE_NO&gt;</p>
<dd> Disable a specific processor sleep state.</p>
<dt><code>-e</code> <code>&#8211;enable</code> &lt;STATE_NO&gt;</p>
<dd> Enable a specific processor sleep state.</p>
<dt><code>-D</code> <code>&#8211;disable-by-latency</code> &lt;LATENCY&gt;</p>
<dd> Disable all idle states with a equal or higher latency than &lt;LATENCY&gt;. </p>
<p> Enable all idle states with a latency lower than &lt;LATENCY&gt;.</p>
<dt><code>-E</code> <code>&#8211;enable-all</code></p>
<dd> Enable all idle states if not enabled already. </p>
</dl>
<h2>REMARKS</h2>
<p> Cpuidle Governors Policy on Disabling Sleep States </p>
<dl>
<dt>
<dd> Depending on the used cpuidle governor, implementing the kernel policy how to choose sleep states, subsequent sleep states on this core, might get disabled as well. </p>
<p> There are two cpuidle governors ladder and menu. While the ladder governor is always available, if CONFIG_CPU_IDLE is selected, the menu governor additionally requires CONFIG_NO_HZ. </p>
<p> The behavior and the effect of the disable variable depends on the implementation of a particular governor. In the ladder governor, for example, it is not coherent, i.e. if one is disabling a light state, then all deeper states are disabled as well. Likewise, if one enables a deep state but a lighter state still is disabled, then this has no effect.</dl>
<p> Disabling the Lightest Sleep State may not have any Affect </p>
<dl>
<dt>
<dd> If criteria are not met to enter deeper sleep states and the lightest sleep state is chosen when idle, the kernel may still enter this sleep state, irrespective of whether it is disabled or not. This is also reflected in the usage count of the disabled sleep state when using the cpupower idle-info command.</dl>
<p> Selecting specific CPU Cores </p>
<dl>
<dt>
<dd> By default processor sleep states of all CPU cores are set. Please refer to the <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1) manpage in the &#8211;cpu option section how to disable C-states of specific cores.</dl>
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
<p> <a href="/docs/linux/man/1-cpupower/">cpupower</a>(1), <a href="/docs/linux/man/1-cpupower-monitor/">cpupower-monitor</a>(1), <a href="/docs/linux/man/1-cpupower-info/">cpupower-info</a>(1), <a href="/docs/linux/man/1-cpupower-set/">cpupower-set</a>(1), <a href="/docs/linux/man/1-cpupower-idle-info/">cpupower-idle-info</a>(1) </p>
<h2>Index</h2>
