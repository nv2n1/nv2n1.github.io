---

title: "virt-top(1)"
name: "virt-top"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-top/"
description: "virt-top – ‘top’-like utility for virtualization stats"
---

<p> virt-top &#8211; &#8216;top&#8217;-like utility for virtualization stats </p>
<h2>SUMMARY</h2>
<p> virt-top [-options]</p>
<h2>DESCRIPTION</h2>
<p> virt-top is a <i><a href="/docs/linux/man/1-top/">top</a></i>(1)-like utility for showing stats of virtualized domains. Many keys and command line options are the same as for ordinary <i>top</i>. </p>
<p> It uses libvirt so it is capable of showing stats across a variety of different virtualization systems.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></dt>
<dd> Display physical CPUs by default (instead of domains). </dd>
<p> Under each domain column, two numbers are shown. The first is the percentage of the physical CPU used by the domain and the hypervisor together. The second is the percentage used by just the domain. </p>
<p> When virt-top is running, use the <i>1</i> key to toggle between physical CPUs and domains display.</p>
<dt><code>-2</code></dt>
<dd> Display network interfaces by default (instead of domains). When virt-top is running, use the <i>2</i> key to toggle between network interfaces and domains display.</dd>
<dt><code>-3</code></dt>
<dd> Display block devices (virtual disks) by default (instead of domains). When virt-top is running, use the <i>3</i> key to toggle between block devices and domains display.</dd>
<dt><code>-b</code></dt>
<dd> Batch mode. In this mode keypresses are ignored.</dd>
<dt><code>-c uri</code> or <code>&#8211;connect uri</code></dt>
<dd> Connect to the libvirt URI given. </dd>
<p> To connect to QEMU/KVM you would normally do <i>-c <a href="qemu:///system">qemu:///system</a></i> </p>
<p> To connect to Xen on the same host, do <i>-c <a href="xen:///">xen:///</a></i> </p>
<p> To connect to libvirtd on a remote machine you would normally do <i>-c <a href="qemu://host/system">qemu://host/system</a></i> </p>
<p> If this option is not given then virt-top connects by default to whatever is the default hypervisor for libvirt, although this can be overridden by setting environment variables. </p>
<p> See the libvirt documentation at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; for further information.</p>
<dt><code>-d delay</code></dt>
<dd> Set the delay between screen updates in seconds. The default is 3.0 seconds. You can change this while virt-top is running by pressing either <i>s</i> or <i>d</i> key.</dd>
<dt><code>-n iterations</code></dt>
<dd> Set the number of iterations to run. The default is to run continuously.</dd>
<dt><code>-o sort</code></dt>
<dd> Set the sort order to one of: <code>cpu</code> (sort by <tt>%CPU</tt> used), <code>mem</code> (sort by total memory), <code>time</code> (sort by total time), <code>id</code> (sort by domain ID), <code>name</code> (sort by domain name), <code>netrx</code> (sort by network received bytes), <code>nettx</code> (sort by network transmitted bytes), <code>blockrdrq</code> (sort by block device [disk] read requests), <code>blockwrrq</code> (sort by block device [disk] write requests). </dd>
<p> While virt-top is running you can change the sort order using keys <i>P</i> (cpu), <i>M</i> (memory), <i>T</i> (total time), <i>N</i> (domain ID), <i>F</i> (interactively select the sort field).</p>
<dt><code>-s</code></dt>
<dd> Secure mode. Currently this does nothing.</dd>
<dt><code>&#8211;hist-cpu secs</code></dt>
<dd> Set the time in seconds between updates of the historical <tt>%CPU</tt> at the top right of the display.</dd>
<dt><code>&#8211;csv file.csv</code></dt>
<dd> Write the statistics to file <i>file.csv</i>. First a header is written showing the statistics being recorded in each column, then one line is written for each screen update. The CSV file can be loaded directly by most spreadsheet programs. </dd>
<p> Currently the statistics which this records vary between releases of virt-top (but the column headers will stay the same, so you can use those to process the CSV file). </p>
<p> Not every version of virt-top supports CSV output &#8211; it depends how the program was compiled (see <i></i><i>README</i><i></i> file in the source distribution for details). </p>
<p> To save space you can compress your CSV files (if your shell supports this feature, eg. <i>bash</i>): </p>
<pre>
 virt-top --csv &gt;(gzip -9 &gt; output.csv.gz)
</pre>
<p> You can use a similar trick to split the CSV file up. In this example the CSV file is split every 1000 lines into files called <i>output.csv.00</i>, <i>output.csv.01</i> etc. </p>
<pre>
 virt-top --csv &gt;(split -d -l 1000 - output.csv.)
</pre>
<p> RHEL provides a short Python script called <tt>&quot;processcsv.py&quot;</tt> which can be used to post-process the CSV output. Run it like this: </p>
<pre>
 virt-top --csv data.csv
 processcsv.py &lt; data.csv
</pre>
<p> This creates or <i>overwrites</i> the following files in the current directory: </p>
<pre>
 global.csv
 domain&lt;NNN&gt;.csv
</pre>
<p> <tt>&quot;global.csv&quot;</tt> will contain the global data. One <tt>&quot;domain&lt;NNN&gt;.csv&quot;</tt> file will also be created for each domain with ID <tt>&quot;NNN&quot;</tt>, containing the per-domain data.</p>
<dt><code>&#8211;no-csv-cpu</code></dt>
<dd> Disable domain CPU stats in CSV output.</dd>
<dt><code>&#8211;no-csv-mem</code></dt>
<dd> Disable domain memory stats in CSV output.</dd>
<dt><code>&#8211;no-csv-block</code></dt>
<dd> Disable domain block device stats in CSV output.</dd>
<dt><code>&#8211;no-csv-net</code></dt>
<dd> Disable domain network interface stats in CSV output.</dd>
<dt><code>&#8211;debug filename</code></dt>
<dd> Send debug and error messages to <i>filename</i>. To send error messages to syslog you can do: </dd>
<pre>
 virt-top --debug &gt;(logger -t virt-top)
</pre>
<p> See also REPORTING BUGS below.</p>
<dt><code>&#8211;init-file filename</code></dt>
<dd> Read <i>filename</i> as the init file instead of the default which is <i></i>$HOME<i>/.virt-toprc</i>. See also INIT FILE below.</dd>
<dt><code>&#8211;no-init-file</code></dt>
<dd> Do not read any init file.</dd>
<dt><code>&#8211;script</code></dt>
<dd> Script mode. There will be no user interface. This is most useful when used together with the <i>&#8211;csv</i> and <i>-n</i> options.</dd>
<dt><code>&#8211;stream</code></dt>
<dd> Stream mode. All output is sent to stdout. This can be used from shell scripts etc. There is no user interface.</dd>
<dt><code>&#8211;block-in-bytes</code></dt>
<dd> Show I/O statistics in Bytes. Default is shown in the number of Requests.</dd>
<dt><code>&#8211;end-time time</code></dt>
<dd> The program will exit at the <i>time</i> given. </dd>
<p> The time may be given in one of the following formats:</p>
<dl>
<dl>
<dt><i>YYYY-MM-DD </i><i>HH:MM:SS</i><i></i></dt>
<dd> End time is the date and time given.</dd>
<dt><i></i><i>HH:MM:SS</i><i></i></dt>
<dd> End time is the time given, today.</dd>
<dt><i>+HH:MM:SS</i></dt>
<dd> End time is HH hours, MM minutes, SS seconds in the future (counted from the moment that program starts).</dd>
<dt><i>+secs</i></dt>
<dd> End time is <i>secs</i> seconds in the future.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> For example to run the program for 3 minutes you could do: </p>
<pre>
 virt-top --end-time +00:03:00
</pre>
<p> or: </p>
<pre>
 virt-top --end-time +180
</pre>
<p> Not every version of virt-top supports this option &#8211; it depends how the program was compiled (see <i></i><i>README</i><i></i> file in the source distribution for details).</dd></dl>
<dt><code>&#8211;help</code></dt>
<dd> Display usage summary.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd></dl>
<h2>KEYS</h2>
<p> Note that keys are case sensitive. For example use upper-case <i>P</i> (shift P) to sort by <tt>%CPU</tt>. <i>^</i> before a key means a Ctrl key, so <i>^L</i> is Ctrl L.</p>
<dl>
<dt><i>space</i> or <i>^L</i></dt>
<dd> Updates the display.</dd>
<dt><i>q</i></dt>
<dd> Quits the program.</dd>
<dt><i>h</i></dt>
<dd> Displays help.</dd>
<dt><i>s</i> or <i>d</i></dt>
<dd> Change the delay between screen updates.</dd>
<dt><i>B</i></dt>
<dd> Toggle Block I/O statistics so they are shown in either bytes or requests.</dd>
<dt><i>0</i> (number 0)</dt>
<dd> Show the normal list of domains display.</dd>
<dt><i>1</i> (number 1)</dt>
<dd> Toggle into showing physical CPUs. If pressed again toggles back to showing domains (the normal display).</dd>
<dt><i>2</i></dt>
<dd> Toggle into showing network interfaces. If pressed again toggles back to showing domains.</dd>
<dt><i>3</i></dt>
<dd> Toggle into showing block devices (virtual disks). If pressed again toggles back to showing domains.</dd>
<dt><i>P</i></dt>
<dd> Sort by <tt>%CPU</tt>.</dd>
<dt><i>M</i></dt>
<dd> Sort by total memory. Note that this shows the total memory allocated to the guest, not the memory being used.</dd>
<dt><i>T</i></dt>
<dd> Sort by total time.</dd>
<dt><i>N</i></dt>
<dd> Sort by domain ID.</dd>
<dt><i>F</i></dt>
<dd> Select the sort field interactively (there are other sort fields you can choose using this key).</dd>
<dt><i>W</i></dt>
<dd> This creates or overwrites the init file with the current settings. </dd>
<p> This key is disabled if <i>&#8211;no-init-file</i> was specified on the command line or if <i>overwrite-init-file false</i> is given in the init file.</dl>
<h2>INIT FILE</h2>
<p> When virt-top starts up, it reads initial settings from the file <i>.virt-toprc</i> in the user&#8217;s home directory. </p>
<p> The name of this file may be overridden using the <i>&#8211;init-file filename</i> command line option or may be disabled entirely using <i>&#8211;no-init-file</i>. </p>
<p> The init file has a simple format. Blank lines and comments beginning with <i>#</i> are ignored. Everything else is a set of <i>key value</i> pairs, described below.</p>
<dl>
<dt><code>display</code> <i>task|pcpu|block|net</i></dt>
<dd> Sets the major display mode to one of <i>task</i> (tasks, the default), <i>pcpu</i> (physical CPUs), <i>block</i> (block devices), or <i>net</i> (network interfaces).</dd>
<dt><code>delay</code> <i>secs</i></dt>
<dd> Sets the delay between display updates in seconds.</dd>
<dt><code>hist-cpu</code> <i>secs</i></dt>
<dd> Sets the historical CPU delay in seconds.</dd>
<dt><code>iterations</code> <i>n</i></dt>
<dd> Sets the number of iterations to run before we exit. Setting this to <i>-1</i> means to run continuously.</dd>
<dt><code>sort</code> <i>cpu|mem|time|id|name|&#8230;</i></dt>
<dd> Sets the sort order. The option names are the same as for the command line <i>-o</i> option.</dd>
<dt><code>connect</code> <i>uri</i></dt>
<dd> Sets the default connection URI.</dd>
<dt><code>debug</code> <i>filename</i></dt>
<dd> Sets the default filename to use for debug and error messages.</dd>
<dt><code>csv</code> <i>filename</i></dt>
<dd> Enables CSV output to the named file.</dd>
<dt><code>csv-cpu</code> <i>true|false</i></dt>
<dd> Enable or disable domain CPU stats in CSV output.</dd>
<dt><code>csv-mem</code> <i>true|false</i></dt>
<dd> Enable or disable domain memory stats in CSV output.</dd>
<dt><code>csv-block</code> <i>true|false</i></dt>
<dd> Enable or disable domain block device stats in CSV output.</dd>
<dt><code>csv-net</code> <i>true|false</i></dt>
<dd> Enable or disable domain network interface stats in CSV output.</dd>
<dt><code>batch</code> <i>true|false</i></dt>
<dd> Sets batch mode.</dd>
<dt><code>secure</code> <i>true|false</i></dt>
<dd> Sets secure mode.</dd>
<dt><code>script</code> <i>true|false</i></dt>
<dd> Sets script mode.</dd>
<dt><code>stream</code> <i>true|false</i></dt>
<dd> Sets stream mode.</dd>
<dt><code>block-in-bytes</code> <i>true|false</i></dt>
<dd> Show block device statistics in bytes.</dd>
<dt><code>end-time</code> <i>time</i></dt>
<dd> Set the time at which the program exits. See above for the time formats supported.</dd>
<dt><code>overwrite-init-file</code> <i>false</i></dt>
<dd> If set to <i>false</i> then the <i>W</i> key will not overwrite the init file.</dd></dl>
<p> Note that in the current implementation, options specified in the init file override options specified on the command line. This is a bug and this behaviour may change in the future.</p>
<h2>COLUMN HEADINGS</h2>
<dl>
<dt><code>%CPU</code></dt>
<dd> Percentage of CPU used. As with <i><a href="/docs/linux/man/1-top/">top</a></i>(1), 100% means that all physical CPUs are being fully used.</dd>
<dt><code>DEVICE</code></dt>
<dd> The block device name.</dd>
<dt><code>DOMAIN</code></dt>
<dd>
</dd><dt><code>NAME</code></dt>
<dd> The name of the libvirt domain.</dd>
<dt><code>ID</code></dt>
<dd> The libvirt domain ID.</dd>
<dt><code>INTERFACE</code></dt>
<dd> The network interface name.</dd>
<dt><code>%MEM</code></dt>
<dd> The percentage of host memory assigned to the guest.</dd>
<dt><code>PHYCPU</code></dt>
<dd> The physical CPU.</dd>
<dt><code>RDBY</code></dt>
<dd> Disk bytes read since last displayed.</dd>
<dt><code>RDRQ</code></dt>
<dd> Disk read requests since last displayed.</dd>
<dt><code>RXBY</code></dt>
<dd> Network bytes received since last displayed.</dd>
<dt><code>RXPK</code></dt>
<dd> Network packets received since last displayed.</dd>
<dt><code>S</code></dt>
<dd> The state of the domain, one of:</dd>
<dl>
<dl>
<dt><code>?</code></dt>
<dd> Unknown.</dd>
<dt><code>R</code></dt>
<dd> Running.</dd>
<dt><code>S</code></dt>
<dd> Blocked.</dd>
<dt><code>P</code></dt>
<dd> Paused.</dd>
<dt><code>D</code></dt>
<dd>
</dd><dt><code>O</code></dt>
<dd> Shutdown.</dd>
<dt><code>X</code></dt>
<dd> Crashed.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>TIME</code></dt>
<dd> Total CPU time used.</dd>
<dt><code>TXBY</code></dt>
<dd> Network bytes transmitted since last displayed.</dd>
<dt><code>TXPK</code></dt>
<dd> Network packets transmitted since last displayed.</dd>
<dt><code>WRBY</code></dt>
<dd> Disk bytes written since last displayed.</dd>
<dt><code>WRRQ</code></dt>
<dd> Disk write requests since last displayed.</dd></dl>
<h2>NOTES</h2>
<h3>Block I/O statistics</h3>
<p> This I/O value is the amount of I/O since the previous iteration of virt-top. To calculate speed of I/O, you should divide the number by delay secs.</p>
<h3>NETWORK RX BYTES AND PACKETS</h3>
<p> Libvirt/virt-top has no way to know that a packet transmitted to a guest was received (eg. if the guest is not listening). In the network RX stats, virt-top reports the packets transmitted to the guest, on the basis that the guest might receive them. </p>
<p> In particular this includes broadcast packets. Because of the way that Linux bridges work, if the guest is connected to a bridge, it will probably see a steady &#8220;background noise&#8221; of RX packets even when the network interface is idle or down. These are caused by STP packets generated by the bridge.</p>
<h3>DEBUGGING LIBVIRT ISSUES</h3>
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
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>REPORTING BUGS</h2>
<p> Bugs can be viewed on the Red Hat Bugzilla page: &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt;. </p>
<p> If you find a bug in virt-top, please follow these steps to report it:</p>
<dl>
<dt>1. Check for existing bug reports</dt>
<dd> Go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt; and search for similar bugs. Someone may already have reported the same bug, and they may even have fixed it.</dd>
<dt>2. Capture debug and error messages</dt>
<dd> Run </dd>
<pre>
 virt-top --debug virt-top.log
</pre>
<p> and keep <i>virt-top.log</i>. It contains error messages which you should submit with your bug report.</p>
<dt>3. Get version of virt-top and version of libvirt.</dt>
<dd> Use: </dd>
<pre>
 virt-top --version
</pre>
<p> If you can get the precise version of libvirt you are using then that too is helpful.</p>
<dt>4. Submit a bug report.</dt>
<dd> Go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a>&gt; and enter a new bug. Please describe the problem in as much detail as possible. </dd>
<p> Remember to include the version numbers (step 3) and the debug messages file (step 2).</p>
<dt>5. Assign the bug to rjones @ redhat.com</dt>
<dd> Assign or reassign the bug to <code>rjones @ redhat.com</code> (without the spaces). You can also send me an email with the bug number if you want a faster response. </dd>
</dl>
