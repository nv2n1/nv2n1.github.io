---
title: "vboxservice(8)"
name: "vboxservice"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vboxservice/"
description: "VBoxService – x86 virtualization solution"
---

<p>VBoxService &#8211; x86 virtualization solution</p>
<h2>Description</h2>
<h3>Usage:</h3>
<dl>
<dt>VBoxService</p>
<dd>[-f|&#8211;foreground] [-v|&#8211;verbose] [-l|&#8211;logfile &lt;file&gt;] [-i|&#8211;interval &lt;seconds&gt;] [&#8211;disable-&lt;service&gt;] [&#8211;enable-&lt;service&gt;] [&#8211;only-&lt;service&gt;] [-h|-?|&#8211;help] [&#8211;control-interval &lt;ms&gt;] [&#8211;control-procs-max-kept &lt;x&gt;] [&#8211;control-procs-mem-std[in|out|err] &lt;KB&gt;] [&#8211;timesync-interval &lt;ms&gt;] [&#8211;timesync-min-adjust &lt;ms&gt;] [&#8211;timesync-latency-factor &lt;x&gt;] [&#8211;timesync-max-latency &lt;ms&gt;] [&#8211;timesync-set-threshold &lt;ms&gt;] [&#8211;timesync-set-start] [&#8211;timesync-set-on-restore 0|1] [&#8211;vminfo-interval &lt;ms&gt;]</dl>
<h2>Options</h2>
<dl>
<dt><code>-i</code> | <code>&#8211;interval</code></p>
<dd>The default interval.</p>
<dt><code>-f</code> | <code>&#8211;foreground</code></p>
<dd>Don&#8217;t daemonize the program. For debugging.</p>
<dt><code>-l</code> | <code>&#8211;logfile</code> &lt;file&gt;</p>
<dd>Enables logging to a file.</p>
<dt><code>-v</code> | <code>&#8211;verbose</code></p>
<dd>Increment the verbosity level. For debugging.</p>
<dt><code>-V</code> | <code>&#8211;version</code></p>
<dd>Show version information.</p>
<dt><code>-h</code> | -? | <code>&#8211;help</code></p>
<dd>Show this message and exit with status 1.</dl>
<h3>Service-specific options:</h3>
<dl>
<dt><code>&#8211;enable-control</code></p>
<dd>Enables the control service. (default)</p>
<dt><code>&#8211;disable-control</code></p>
<dd>Disables the control service.</p>
<dt><code>&#8211;only-control</code></p>
<dd>Only enables the control service.</p>
<dt><code>&#8211;control-interval</code></p>
<dd>Specifies the interval at which to check for new control commands. The default is 1000 ms.</p>
<dt><code>&#8211;control-procs-max-kept</code></p>
<dd>Specifies how many started guest processes are kept into memory to work with. Default is 256.</p>
<dt><code>&#8211;enable-timesync</code></p>
<dd>Enables the timesync service. (default)</p>
<dt><code>&#8211;disable-timesync</code></p>
<dd>Disables the timesync service.</p>
<dt><code>&#8211;only-timesync</code></p>
<dd>Only enables the timesync service.</p>
<dt><code>&#8211;timesync-interval</code></p>
<dd>Specifies the interval at which to synchronize the time with the host. The default is 10000 ms.</p>
<dt><code>&#8211;timesync-min-adjust</code></p>
<dd>The minimum absolute drift value measured in milliseconds to make adjustments for. The default is 1000 ms on OS/2 and 100 ms elsewhere.</p>
<dt><code>&#8211;timesync-latency-factor</code></p>
<dd>The factor to multiply the time query latency with to calculate the dynamic minimum adjust time. The default is 8 times.</p>
<dt><code>&#8211;timesync-max-latency</code></p>
<dd>The max host timer query latency to accept. The default is 250 ms.</p>
<dt><code>&#8211;timesync-set-threshold</code></p>
<dd>The absolute drift threshold, given as milliseconds, where to start setting the time instead of trying to adjust it. The default is 20 min.</p>
<dt><code>&#8211;timesync-set-start</code></p>
<dd>Set the time when starting the time sync service.</p>
<dt><code>&#8211;timesync-set-on-restore</code> 0|1</p>
<dd>Immediately set the time when the VM was restored. 1 = set (default), 0 = don&#8217;t set.</p>
<dt><code>&#8211;enable-vminfo</code></p>
<dd>Enables the vminfo service. (default)</p>
<dt><code>&#8211;disable-vminfo</code></p>
<dd>Disables the vminfo service.</p>
<dt><code>&#8211;only-vminfo</code></p>
<dd>Only enables the vminfo service.</p>
<dt><code>&#8211;vminfo-interval</code></p>
<dd>Specifies the interval at which to retrieve the VM information. The default is 10000 ms.</p>
<dt><code>&#8211;enable-cpuhotplug</code></p>
<dd>Enables the cpuhotplug service. (default)</p>
<dt><code>&#8211;disable-cpuhotplug</code></p>
<dd>Disables the cpuhotplug service.</p>
<dt><code>&#8211;only-cpuhotplug</code></p>
<dd>Only enables the cpuhotplug service.</p>
<dt><code>&#8211;enable-memballoon</code></p>
<dd>Enables the memballoon service. (default)</p>
<dt><code>&#8211;disable-memballoon</code></p>
<dd>Disables the memballoon service.</p>
<dt><code>&#8211;only-memballoon</code></p>
<dd>Only enables the memballoon service.</p>
<dt><code>&#8211;enable-vmstats</code></p>
<dd>Enables the vmstats service. (default)</p>
<dt><code>&#8211;disable-vmstats</code></p>
<dd>Disables the vmstats service.</p>
<dt><code>&#8211;only-vmstats</code></p>
<dd>Only enables the vmstats service.</p>
<dt><code>&#8211;enable-automount</code></p>
<dd>Enables the automount service. (default)</p>
<dt><code>&#8211;disable-automount</code></p>
<dd>Disables the automount service.</p>
<dt><code>&#8211;only-automount</code></p>
<dd>Only enables the automount service.</p>
<dd>Copyright (C) 2009-2013 Oracle Corporation </p>
</dl>
