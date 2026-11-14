---
title: "virt-top(1)"
name: "virt-top"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-top/"
description: "virt-top – ‘top’-like utility for virtualization stats"
---

<h2 class="name">NAME</h2>
<p> virt-top &#8211; &#8216;top&#8217;-like utility for virtualization stats </p>
<h2>SUMMARY</h2>
<p> virt-top [-options]</p>
<h2>DESCRIPTION</h2>
<p> virt-top is a <i><a href="/docs/linux/man/1-top/">top</a></i>(1)-like utility for showing stats of virtualized domains. Many keys and command line options are the same as for ordinary <i>top</i>. </p>
<p> It uses libvirt so it is capable of showing stats across a variety of different virtualization systems.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> Display physical CPUs by default (instead of domains). </p>
<p> Under each domain column, two numbers are shown. The first is the percentage of the physical <font SIZE="-1">CPU</font> used by the domain and the hypervisor together. The second is the percentage used by just the domain. </p>
<p> When virt-top is running, use the <i>1</i> key to toggle between physical CPUs and domains display.</p>
<dt><code>-2</code></p>
<dd> Display network interfaces by default (instead of domains). When virt-top is running, use the <i>2</i> key to toggle between network interfaces and domains display.</p>
<dt><code>-3</code></p>
<dd> Display block devices (virtual disks) by default (instead of domains). When virt-top is running, use the <i>3</i> key to toggle between block devices and domains display.</p>
<dt><code>-b</code></p>
<dd> Batch mode. In this mode keypresses are ignored.</p>
<dt><code>-c uri</code> or <code>&#8211;connect uri</code></p>
<dd> Connect to the libvirt <font SIZE="-1">URI</font> given. </p>
<p> To connect to <font SIZE="-1">QEMU/KVM</font> you would normally do <i>-c <a href="qemu:///system">qemu:///system</a></i> </p>
<p> To connect to Xen on the same host, do <i>-c <a href="xen:///">xen:///</a></i> </p>
<p> To connect to libvirtd on a remote machine you would normally do <i>-c <a href="qemu://host/system">qemu://host/system</a></i> </p>
<p> If this option is not given then virt-top connects by default to whatever is the default hypervisor for libvirt, although this can be overridden by setting environment variables. </p>
<p> See the libvirt documentation at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; for further information.</p>
<dt><code>-d delay</code></p>
<dd> Set the delay between screen updates in seconds. The default is 3.0 seconds. You can change this while virt-top is running by pressing either <i>s</i> or <i>d</i> key.</p>
<dt><code>-n iterations</code></p>
<dd> Set the number of iterations to run. The default is to run continuously.</p>
<dt><code>-o sort</code></p>
<dd> Set the sort order to one of: <code>cpu</code> (sort by <tt>%CPU</tt> used), <code>mem</code> (sort by total memory), <code>time</code> (sort by total time), <code>id</code> (sort by domain <font SIZE="-1">ID</font>), <code>name</code> (sort by domain name), <code>netrx</code> (sort by network received bytes), <code>nettx</code> (sort by network transmitted bytes), <code>blockrdrq</code> (sort by block device [disk] read requests), <code>blockwrrq</code> (sort by block device [disk] write requests). </p>
<p> While virt-top is running you can change the sort order using keys <i>P</i> (cpu), <i>M</i> (memory), <i>T</i> (total time), <i>N</i> (domain <font SIZE="-1">ID</font>), <i>F</i> (interactively select the sort field).</p>
<dt><code>-s</code></p>
<dd> Secure mode. Currently this does nothing.</p>
<dt><code>&#8211;hist-cpu secs</code></p>
<dd> Set the time in seconds between updates of the historical <tt>%CPU</tt> at the top right of the display.</p>
<dt><code>&#8211;csv file.csv</code></p>
<dd> Write the statistics to file <i>file.csv</i>. First a header is written showing the statistics being recorded in each column, then one line is written for each screen update. The <font SIZE="-1">CSV</font> file can be loaded directly by most spreadsheet programs. </p>
<p> Currently the statistics which this records vary between releases of virt-top (but the column headers will stay the same, so you can use those to process the <font SIZE="-1">CSV</font> file). </p>
<p> Not every version of virt-top supports <font SIZE="-1">CSV</font> output &#8211; it depends how the program was compiled (see <i></i><font SIZE="-1"><i>README</i></font><i></i> file in the source distribution for details). </p>
<p> To save space you can compress your <font SIZE="-1">CSV</font> files (if your shell supports this feature, eg. <i>bash</i>): </p>
<pre>
 virt-top --csv &gt;(gzip -9 &gt; output.csv.gz)
</pre>
<p> You can use a similar trick to split the <font SIZE="-1">CSV</font> file up. In this example the <font SIZE="-1">CSV</font> file is split every 1000 lines into files called <i>output.csv.00</i>, <i>output.csv.01</i> etc. </p>
<pre>
 virt-top --csv &gt;(split -d -l 1000 - output.csv.)
</pre>
<p> <font SIZE="-1">RHEL</font> provides a short Python script called <tt>&quot;processcsv.py&quot;</tt> which can be used to post-process the <font SIZE="-1">CSV</font> output. Run it like this: </p>
<pre>
 virt-top --csv data.csv
 processcsv.py &lt; data.csv
</pre>
<p> This creates or <i>overwrites</i> the following files in the current directory: </p>
<pre>
 global.csv
 domain&lt;NNN&gt;.csv
</pre>
<p> <tt>&quot;global.csv&quot;</tt> will contain the global data. One <tt>&quot;domain&lt;NNN&gt;.csv&quot;</tt> file will also be created for each domain with <font SIZE="-1">ID </font><tt>&quot;NNN&quot;</tt>, containing the per-domain data.</p>
<dt><code>&#8211;no-csv-cpu</code></p>
<dd> Disable domain <font SIZE="-1">CPU</font> stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>&#8211;no-csv-mem</code></p>
<dd> Disable domain memory stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>&#8211;no-csv-block</code></p>
<dd> Disable domain block device stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>&#8211;no-csv-net</code></p>
<dd> Disable domain network interface stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>&#8211;debug filename</code></p>
<dd> Send debug and error messages to <i>filename</i>. To send error messages to syslog you can do: </p>
<pre>
 virt-top --debug &gt;(logger -t virt-top)
</pre>
<p> See also <font SIZE="-1">REPORTING BUGS</font> below.</p>
<dt><code>&#8211;init-file filename</code></p>
<dd> Read <i>filename</i> as the init file instead of the default which is <i></i>$HOME<i>/.virt-toprc</i>. See also <font SIZE="-1">INIT FILE</font> below.</p>
<dt><code>&#8211;no-init-file</code></p>
<dd> Do not read any init file.</p>
<dt><code>&#8211;script</code></p>
<dd> Script mode. There will be no user interface. This is most useful when used together with the <i>&#8211;csv</i> and <i>-n</i> options.</p>
<dt><code>&#8211;stream</code></p>
<dd> Stream mode. All output is sent to stdout. This can be used from shell scripts etc. There is no user interface.</p>
<dt><code>&#8211;block-in-bytes</code></p>
<dd> Show I/O statistics in Bytes. Default is shown in the number of Requests.</p>
<dt><code>&#8211;end-time time</code></p>
<dd> The program will exit at the <i>time</i> given. </p>
<p> The time may be given in one of the following formats:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>YYYY-MM-DD </i><font SIZE="-1"><i>HH:MM:SS</i></font><i></i></p>
<dd> End time is the date and time given.</p>
<dt><i></i><font SIZE="-1"><i>HH:MM:SS</i></font><i></i></p>
<dd> End time is the time given, today.</p>
<dt><i>+HH:MM:SS</i></p>
<dd> End time is <font SIZE="-1">HH</font> hours, <font SIZE="-1">MM</font> minutes, <font SIZE="-1">SS</font> seconds in the future (counted from the moment that program starts).</p>
<dt><i>+secs</i></p>
<dd> End time is <i>secs</i> seconds in the future.</dl>
</dl>
<dl>
<dt>
<dd>
<p> For example to run the program for 3 minutes you could do: </p>
<pre>
 virt-top --end-time +00:03:00
</pre>
<p> or: </p>
<pre>
 virt-top --end-time +180
</pre>
<p> Not every version of virt-top supports this option &#8211; it depends how the program was compiled (see <i></i><font SIZE="-1"><i>README</i></font><i></i> file in the source distribution for details).</dl>
<dt><code>&#8211;help</code></p>
<dd> Display usage summary.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</dl>
<h2>KEYS</h2>
<p> Note that keys are case sensitive. For example use upper-case <i>P</i> (shift P) to sort by <tt>%CPU</tt>. <i>^</i> before a key means a Ctrl key, so <i>^L</i> is Ctrl L.</p>
<dl>
<dt><i>space</i> or <i>^L</i></p>
<dd> Updates the display.</p>
<dt><i>q</i></p>
<dd> Quits the program.</p>
<dt><i>h</i></p>
<dd> Displays help.</p>
<dt><i>s</i> or <i>d</i></p>
<dd> Change the delay between screen updates.</p>
<dt><i>B</i></p>
<dd> Toggle Block I/O statistics so they are shown in either bytes or requests.</p>
<dt><i>0</i> (number 0)</p>
<dd> Show the normal list of domains display.</p>
<dt><i>1</i> (number 1)</p>
<dd> Toggle into showing physical CPUs. If pressed again toggles back to showing domains (the normal display).</p>
<dt><i>2</i></p>
<dd> Toggle into showing network interfaces. If pressed again toggles back to showing domains.</p>
<dt><i>3</i></p>
<dd> Toggle into showing block devices (virtual disks). If pressed again toggles back to showing domains.</p>
<dt><i>P</i></p>
<dd> Sort by <tt>%CPU</tt>.</p>
<dt><i>M</i></p>
<dd> Sort by total memory. Note that this shows the total memory allocated to the guest, not the memory being used.</p>
<dt><i>T</i></p>
<dd> Sort by total time.</p>
<dt><i>N</i></p>
<dd> Sort by domain <font SIZE="-1">ID.</font></p>
<dt><i>F</i></p>
<dd> Select the sort field interactively (there are other sort fields you can choose using this key).</p>
<dt><i>W</i></p>
<dd> This creates or overwrites the init file with the current settings. </p>
<p> This key is disabled if <i>&#8211;no-init-file</i> was specified on the command line or if <i>overwrite-init-file false</i> is given in the init file.</dl>
<h2>INIT FILE</h2>
<p> When virt-top starts up, it reads initial settings from the file <i>.virt-toprc</i> in the user&#8217;s home directory. </p>
<p> The name of this file may be overridden using the <i>&#8211;init-file filename</i> command line option or may be disabled entirely using <i>&#8211;no-init-file</i>. </p>
<p> The init file has a simple format. Blank lines and comments beginning with <i>#</i> are ignored. Everything else is a set of <i>key value</i> pairs, described below.</p>
<dl>
<dt><code>display</code> <i>task|pcpu|block|net</i></p>
<dd> Sets the major display mode to one of <i>task</i> (tasks, the default), <i>pcpu</i> (physical CPUs), <i>block</i> (block devices), or <i>net</i> (network interfaces).</p>
<dt><code>delay</code> <i>secs</i></p>
<dd> Sets the delay between display updates in seconds.</p>
<dt><code>hist-cpu</code> <i>secs</i></p>
<dd> Sets the historical <font SIZE="-1">CPU</font> delay in seconds.</p>
<dt><code>iterations</code> <i>n</i></p>
<dd> Sets the number of iterations to run before we exit. Setting this to <i>-1</i> means to run continuously.</p>
<dt><code>sort</code> <i>cpu|mem|time|id|name|&#8230;</i></p>
<dd> Sets the sort order. The option names are the same as for the command line <i>-o</i> option.</p>
<dt><code>connect</code> <i>uri</i></p>
<dd> Sets the default connection <font SIZE="-1">URI.</font></p>
<dt><code>debug</code> <i>filename</i></p>
<dd> Sets the default filename to use for debug and error messages.</p>
<dt><code>csv</code> <i>filename</i></p>
<dd> Enables <font SIZE="-1">CSV</font> output to the named file.</p>
<dt><code>csv-cpu</code> <i>true|false</i></p>
<dd> Enable or disable domain <font SIZE="-1">CPU</font> stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>csv-mem</code> <i>true|false</i></p>
<dd> Enable or disable domain memory stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>csv-block</code> <i>true|false</i></p>
<dd> Enable or disable domain block device stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>csv-net</code> <i>true|false</i></p>
<dd> Enable or disable domain network interface stats in <font SIZE="-1">CSV</font> output.</p>
<dt><code>batch</code> <i>true|false</i></p>
<dd> Sets batch mode.</p>
<dt><code>secure</code> <i>true|false</i></p>
<dd> Sets secure mode.</p>
<dt><code>script</code> <i>true|false</i></p>
<dd> Sets script mode.</p>
<dt><code>stream</code> <i>true|false</i></p>
<dd> Sets stream mode.</p>
<dt><code>block-in-bytes</code> <i>true|false</i></p>
<dd> Show block device statistics in bytes.</p>
<dt><code>end-time</code> <i>time</i></p>
<dd> Set the time at which the program exits. See above for the time formats supported.</p>
<dt><code>overwrite-init-file</code> <i>false</i></p>
<dd> If set to <i>false</i> then the <i>W</i> key will not overwrite the init file.</dl>
<p> Note that in the current implementation, options specified in the init file override options specified on the command line. This is a bug and this behaviour may change in the future.</p>
<h2>COLUMN HEADINGS</h2>
<dl>
<dt><code>%CPU</code></p>
<dd> Percentage of <font SIZE="-1">CPU</font> used. As with <i><a href="/docs/linux/man/1-top/">top</a></i>(1), 100% means that all physical CPUs are being fully used.</p>
<dt><font SIZE="-1"><code>DEVICE</code></font></p>
<dd> The block device name.</p>
<dt><font SIZE="-1"><code>DOMAIN</code></font></p>
<dd>
<dt><font SIZE="-1"><code>NAME</code></font></p>
<dd> The name of the libvirt domain.</p>
<dt><font SIZE="-1"><code>ID</code></font></p>
<dd> The libvirt domain <font SIZE="-1">ID.</font></p>
<dt><font SIZE="-1"><code>INTERFACE</code></font></p>
<dd> The network interface name.</p>
<dt><code>%MEM</code></p>
<dd> The percentage of host memory assigned to the guest.</p>
<dt><font SIZE="-1"><code>PHYCPU</code></font></p>
<dd> The physical <font SIZE="-1">CPU.</font></p>
<dt><font SIZE="-1"><code>RDBY</code></font></p>
<dd> Disk bytes read since last displayed.</p>
<dt><font SIZE="-1"><code>RDRQ</code></font></p>
<dd> Disk read requests since last displayed.</p>
<dt><font SIZE="-1"><code>RXBY</code></font></p>
<dd> Network bytes received since last displayed.</p>
<dt><font SIZE="-1"><code>RXPK</code></font></p>
<dd> Network packets received since last displayed.</p>
<dt><code>S</code></p>
<dd> The state of the domain, one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>?</code></p>
<dd> Unknown.</p>
<dt><code>R</code></p>
<dd> Running.</p>
<dt><code>S</code></p>
<dd> Blocked.</p>
<dt><code>P</code></p>
<dd> Paused.</p>
<dt><code>D</code></p>
<dd>
<dt><code>O</code></p>
<dd> Shutdown.</p>
<dt><code>X</code></p>
<dd> Crashed.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><font SIZE="-1"><code>TIME</code></font></p>
<dd> Total <font SIZE="-1">CPU</font> time used.</p>
<dt><font SIZE="-1"><code>TXBY</code></font></p>
<dd> Network bytes transmitted since last displayed.</p>
<dt><font SIZE="-1"><code>TXPK</code></font></p>
<dd> Network packets transmitted since last displayed.</p>
<dt><font SIZE="-1"><code>WRBY</code></font></p>
<dd> Disk bytes written since last displayed.</p>
<dt><font SIZE="-1"><code>WRRQ</code></font></p>
<dd> Disk write requests since last displayed.</dl>
<h2>NOTES</h2>
<h3>Block I/O statistics</h3>
<p> This I/O value is the amount of I/O since the previous iteration of virt-top. To calculate speed of I/O, you should divide the number by delay secs.</p>
<h3><font SIZE="-1">NETWORK RX BYTES AND PACKETS</font></h3>
<p> Libvirt/virt-top has no way to know that a packet transmitted to a guest was received (eg. if the guest is not listening). In the network <font SIZE="-1">RX</font> stats, virt-top reports the packets transmitted to the guest, on the basis that the guest might receive them. </p>
<p> In particular this includes broadcast packets. Because of the way that Linux bridges work, if the guest is connected to a bridge, it will probably see a steady &#8220;background noise&#8221; of <font SIZE="-1">RX</font> packets even when the network interface is idle or down. These are caused by <font SIZE="-1">STP</font> packets generated by the bridge.</p>
<h3><font SIZE="-1">DEBUGGING LIBVIRT ISSUES</font></h3>
<p> virt-top tries to turn libvirt errors into informative messages. However if libvirt initialization fails then this is not possible. Instead you will get an obscure error like: </p>
<pre>
 libvir: error : Unknown failure
 Fatal error: exception Libvirt.Virterror(...)
</pre>
<p> To see the cause of libvirt errors in more detail, enable libvirt debugging by setting this environment variable: </p>
<pre>
 export LIBVIRT_DEBUG=1
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-top/">top</a></i>(1), <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), &lt;<a rel="nofollow" href="http://www.libvirt.org/ocaml/">http://www.libvirt.org/ocaml/</a>&gt;, &lt;<a rel="nofollow" href="http://www.libvirt.org/">http://www.libvirt.org/</a>&gt;, &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>&gt;, &lt;<a rel="nofollow" href="http://caml.inria.fr/">http://caml.inria.fr/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>COPYRIGHT</h2>
<p> (C) Copyright 2007-2012 Red Hat Inc., Richard W.M. Jones <a rel="nofollow" href="http://libvirt.org/">http://libvirt.org/</a> </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>REPORTING BUGS</h2>
<p> Bugs can be viewed on the Red Hat Bugzilla page: &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt;. </p>
<p> If you find a bug in virt-top, please follow these steps to report it:</p>
<dl>
<dt>1. Check for existing bug reports</p>
<dd> Go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt; and search for similar bugs. Someone may already have reported the same bug, and they may even have fixed it.</p>
<dt>2. Capture debug and error messages</p>
<dd> Run </p>
<pre>
 virt-top --debug virt-top.log
</pre>
<p> and keep <i>virt-top.log</i>. It contains error messages which you should submit with your bug report.</p>
<dt>3. Get version of virt-top and version of libvirt.</p>
<dd> Use: </p>
<pre>
 virt-top --version
</pre>
<p> If you can get the precise version of libvirt you are using then that too is helpful.</p>
<dt>4. Submit a bug report.</p>
<dd> Go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt; and enter a new bug. Please describe the problem in as much detail as possible. </p>
<p> Remember to include the version numbers (step 3) and the debug messages file (step 2).</p>
<dt>5. Assign the bug to rjones @ redhat.com</p>
<dd> Assign or reassign the bug to <code>rjones @ redhat.com</code> (without the spaces). You can also send me an email with the bug number if you want a faster response. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAM">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAN">AUTHORS</a></p>
<dd>
<dt><a href="#lbAO">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAP">REPORTING BUGS</a></p>
<dd></dl>
