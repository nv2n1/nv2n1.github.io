---
title: "cpuspeed(8)"
name: "cpuspeed"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cpuspeed/"
description: "cpuspeed – user-space cpu frequency scaling program, v1.5.1"
---

<p>cpuspeed &#8211; user-space cpu frequency scaling program, v1.5.1</p>
<h2>Synopsis</h2>
<p><code>cpuspeed</code> [<i>Options</i>]</p>
<h2>Description</h2>
<p>cpuspeed v1.5.1 </p>
<p> This program monitors the system&#8217;s idle percentage and reduces or raises the CPUs&#8217; clock speeds and voltages accordingly to minimize power consumption when idle and maximize performance when needed. This is the default. </p>
<p> The program may also optionally be configured to reduce the CPUs&#8217; clock speeds if the temperature gets too high, NOT minimize their speeds if the computer&#8217;s AC adapter is disconnected or maximize their speeds when the AC adapter is connected. </p>
<p> By default this program will manage every CPU found in the system.</p>
<dl>
<dd>Options:</p>
<dt> <code>-d</code></p>
<dd>
<dd>Tells the process to daemonize itself (run in background).</p>
<dt> <code>-i</code> &lt;interval&gt;</p>
<dd>
<dd>Sets the interval between idle percentage tests and possible speed changes in tenths of a second (default is 20).</p>
<dt> <code>-p</code> &lt;fast up&gt; &lt;threshold&gt;</p>
<dd>
<dd>Sets the CPU core idle percentage thresholds. &lt;fast up&gt; is the idle percentage below which a CPU core will be set to the highest possible speed. &lt;threshold&gt; is the idle percentage above which a CPU core&#8217;s speed will be decreased and below which a CPU core&#8217;s speed will be increased (defaults are 10 and 25).</p>
<dt> <code>-m</code> &lt;minimum speed&gt;</p>
<dd>
<dd>Sets the minimum speed in KHz below which a CPU core will not be set.</p>
<dt> <code>-M</code> &lt;maximum speed&gt;</p>
<dd>
<dd>Sets the maximum speed in KHz above which a CPU core will not be set.</p>
<dt> <code>-n</code></p>
<dd>
<dd>Do not treat niced programs as idle time.</p>
<dt> <code>-w</code></p>
<dd>
<dd>Do not treat time waiting for IO as idle time.</p>
<dt> <code>-t</code> &lt;temp file&gt; &lt;maxtemp&gt;</p>
<dd>
<dd>Sets the ACPI temperature file and the temperature at which CPUs will be set to minimum speed.</p>
<dt> <code>-T</code> &lt;interval&gt;</p>
<dd>
<dd>Sets the interval at which the temperature will be polled in tenths of a second (default is 10). (Requires the &#8216;-t&#8217; option above.)</p>
<dt> <code>-a</code> &lt;AC file&gt;</p>
<dd>
<dd>Sets the ACPI AC adapter state file and tells the program to set the CPUs to minimum speed when the AC adapter is disconnected. (This is the default but is changeable by the &#8216;-D&#8217; option below).</p>
<dt> <code>-A</code> &lt;interval&gt;</p>
<dd>
<dd>Sets the interval at which the AC adapter state will be polled in tenths of a second (default is 50). (Requires the &#8216;-a&#8217; option above.)</p>
<dt> <code>-C</code></p>
<dd>
<dd>Run at maximum speed when AC adapter is connected. (Requires the &#8216;-a&#8217; option above.)</p>
<dt> <code>-D</code></p>
<dd>
<dd>Do NOT force minimum speed when AC adapter is disconnected. (Requires the &#8216;-a&#8217; option above.)</p>
<dt> <code>-r</code></p>
<dd>
<dd>Restores previous speed on program exit.</p>
<dt> <code>-S</code> &lt;CPU core 1&gt; [[&lt;CPU core 2&gt;] &#8230;]</p>
<dd>
<dd>Manage only a single group of CPU cores. All of the specified cores will controlled as a single group (locked to the same speed) and are in the range 0 to n-1 where &#8216;n&#8217; is the total number of CPU cores in the system. Note that when specifying multiple cores the list must be enclosed in quotes. Without this option the program creates copies of itself to manage every core of every CPU in the system and automatically determines core groups. If you are running on an old kernel and get an error message about not being able to open an &quot;affected_cpus&quot; file then you must run this program separately for each group of cores that must be controlled together (which probably means for each physical CPU) and use this option.</dl>
<h3>Notes:</h3>
<p>To have a CPU core stay at the highest clock speed to maximize performance send the process controlling that CPU core the SIGUSR1 signal. </p>
<p> To have a CPU core stay at the lowest clock speed to maximize battery life send the process controlling that CPU core the SIGUSR2 signal. </p>
<p> To resume having a CPU core&#8217;s clock speed dynamically scaled send the process controlling that CPU core the SIGHUP signal. </p>
<p> Many modern Linux systems support in-kernel cpu frequency scaling. The cpuspeed daemon only works in conjunction with the &#8216;userspace&#8217; frequency scaling governor. Other governors, such as &#8216;ondemand&#8217; and &#8216;conservative&#8217;, rely on the Linux kernel to adjust cpu frequencies on the fly without the need of any user-space assistance, such as that provided by cpuspeed. </p>
<p> Red Hat and Fedora distributions employ a unified configuration file for both scenarios, as well as a cpuspeed init script that will configure either cpuspeed or in-kernel cpu frequency scaling, as appropriate.</p>
<h2>Files</h2>
<pre>/etc/sysconfig/cpuspeed, configuration file
/etc/init.d/cpuspeed, initialzation script
/usr/sbin/cpuspeed, cpuspeed program</pre>
<h2>See Also</h2>
<p>The CPUSpeed web page:<br />
&nbsp;<wbr>&nbsp;<wbr><code>&nbsp;<wbr><a rel="nofollow" href="http://carlthompson.net/Software/CPUSpeed">http://carlthompson.net/Software/CPUSpeed</a></code></p>
<h2>License</h2>
<p>CPUSpeed is released under the GNU General Public License version 2 (or if you wish any later version). This license allows you to use, copy, distribute and modify the software with very few restrictions. The full text of the license may be found here:<br />
&nbsp;<wbr>&nbsp;<wbr><code><a rel="nofollow" href="http://carlthompson.net/Software/CPUSpeed/License">http://carlthompson.net/Software/CPUSpeed/License</a></code></p>
<h2>Author(S):</h2>
<dl>
<dt>CPUSpeed daemon, original init script and configuration file:</p>
<dd>
<pre>Carl Thompson - cet [at] carlthompson.net
 (copyright 2002 - 2008)
<dt>Modernized init script, configuration file and man page:<dd>Dave Jones - davej [at] redhat.com
Michal Jaegermann - michal [at] harddata.com
Jarod Wilson - jwilson [at] redhat.com
</dl></pre>
