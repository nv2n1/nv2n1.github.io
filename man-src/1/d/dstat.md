---
title: "dstat(1)"
name: "dstat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dstat/"
description: "dstat – versatile tool for generating system resource statistics"
---

<h2 class="name">NAME</h2>
<p> dstat &#8211; versatile tool for generating system resource statistics </p>
<h2>SYNOPSIS</h2>
<p> dstat [-afv] [options..] [delay [count]] </p>
<h2>DESCRIPTION</h2>
<p> Dstat is a versatile replacement for vmstat, iostat and ifstat. Dstat overcomes some of the limitations and adds some extra features. </p>
<p> Dstat allows you to view all of your system resources instantly, you can eg. compare disk usage in combination with interrupts from your IDE controller, or compare the network bandwidth numbers directly with the disk throughput (in the same interval). </p>
<p> Dstat also cleverly gives you the most detailed information in columns and clearly indicates in what magnitude and unit the output is displayed. Less confusion, less mistakes, more efficient. </p>
<p> Dstat is unique in letting you aggregate block device throughput for a certain diskset or network bandwidth for a group of interfaces, ie. you can see the throughput for all the block devices that make up a single filesystem or storage system. </p>
<p> Dstat allows its data to be directly written to a CSV file to be imported and used by OpenOffice, Gnumeric or Excel to create graphs. </p>
<p> <code>Note</code> Users of Sleuthkit might find Sleuthkit&#8217;s dstat being renamed to datastat to avoid a name conflict. See Debian bug #283709 for more information. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-c, &#8211;cpu</p>
<dd> enable cpu stats (system, user, idle, wait, hardware interrupt, software interrupt)</p>
<dt>-C 0,3,total</p>
<dd> include cpu0, cpu3 and total (when using -c/&#8211;cpu)</p>
<dt>-d, &#8211;disk</p>
<dd> enable disk stats (read, write)</p>
<dt>-D total,hda</p>
<dd> include total and hda (when using -d/&#8211;disk)</p>
<dt>-g, &#8211;page</p>
<dd> enable page stats (page in, page out)</p>
<dt>-i, &#8211;int</p>
<dd> enable interrupt stats</p>
<dt>-I 5,10</p>
<dd> include interrupt 5 and 10 (when using -i/&#8211;int)</p>
<dt>-l, &#8211;load</p>
<dd> enable load average stats (1 min, 5 mins, 15mins)</p>
<dt>-m, &#8211;mem</p>
<dd> enable memory stats (used, buffers, cache, free)</p>
<dt>-n, &#8211;net</p>
<dd> enable network stats (receive, send)</p>
<dt>-N eth1,total</p>
<dd> include eth1 and total (when using -n/&#8211;net)</p>
<dt>-p, &#8211;proc</p>
<dd> enable process stats (runnable, uninterruptible, new)</p>
<dt>-r, &#8211;io</p>
<dd> enable I/O request stats (read, write requests)</p>
<dt>-s, &#8211;swap</p>
<dd> enable swap stats (used, free)</p>
<dt>-S swap1,total</p>
<dd> include swap1 and total (when using -s/&#8211;swap)</p>
<dt>-t, &#8211;time</p>
<dd> enable time/date output</p>
<dt>-T, &#8211;epoch</p>
<dd> enable time counter (seconds since epoch)</p>
<dt>-y, &#8211;sys</p>
<dd> enable system stats (interrupts, context switches)</p>
<dt>&#8211;aio</p>
<dd> enable aio stats (asynchronous I/O)</p>
<dt>&#8211;fs, &#8211;filesystem</p>
<dd> enable filesystem stats (open files, inodes)</p>
<dt>&#8211;ipc</p>
<dd> enable ipc stats (message queue, semaphores, shared memory)</p>
<dt>&#8211;lock</p>
<dd> enable file lock stats (posix, flock, read, write)</p>
<dt>&#8211;raw</p>
<dd> enable raw stats (raw sockets)</p>
<dt>&#8211;socket</p>
<dd> enable socket stats (total, tcp, udp, raw, ip-fragments)</p>
<dt>&#8211;tcp</p>
<dd> enable tcp stats (listen, established, syn, time_wait, close)</p>
<dt>&#8211;udp</p>
<dd> enable udp stats (listen, active)</p>
<dt>&#8211;unix</p>
<dd> enable unix stats (datagram, stream, listen, active)</p>
<dt>&#8211;vm</p>
<dd> enable vm stats (hard pagefaults, soft pagefaults, allocated, free)</p>
<dt>&#8211;plugin-name</p>
<dd> enable (external) plugins by plugin name, see <code>PLUGINS</code> for options</p>
<dt>Possible internal stats are</p>
<dd> aio, cpu, cpu24, disk, disk24, disk24old, epoch, fs, int, int24, io, ipc, load, lock, mem, net, page, page24, proc, raw, socket, swap, swapold, sys, tcp, time, udp, unix, vm</p>
<dt>&#8211;list</p>
<dd> list the internal and external plugin names</p>
<dt>-a, &#8211;all</p>
<dd> equals -cdngy (default)</p>
<dt>-f, &#8211;full</p>
<dd> expand -C, -D, -I, -N and -S discovery lists</p>
<dt>-v, &#8211;vmstat</p>
<dd> equals -pmgdsc -D total</p>
<dt>&#8211;bits</p>
<dd> force bits for values expressed in bytes</p>
<dt>&#8211;float</p>
<dd> force float values on screen (mutual exclusive with <code>&#8211;integer</code>)</p>
<dt>&#8211;integer</p>
<dd> force integer values on screen (mutual exclusive with <code>&#8211;float</code>)</p>
<dt>&#8211;bw, &#8211;blackonwhite</p>
<dd> change colors for white background terminal</p>
<dt>&#8211;nocolor</p>
<dd> disable colors (implies <code>&#8211;noupdate</code>)</p>
<dt>&#8211;noheaders</p>
<dd> disable repetitive headers</p>
<dt>&#8211;noupdate</p>
<dd> disable intermediate updates when delay &gt; 1</p>
<dt>&#8211;output file</p>
<dd> write CSV output to file</p>
<dt>&#8211;profile</p>
<dd> show profiling statistics when exiting dstat</dl>
<h2>PLUGINS</h2>
<p> While anyone can create their own dstat plugins (and contribute them) dstat ships with a number of plugins already that extend its capabilities greatly. Here is an overview of the plugins dstat ships with: </p>
<dl>
<dt>&#8211;battery</p>
<dd> battery in percentage (needs ACPI)</p>
<dt>&#8211;battery-remain</p>
<dd> battery remaining in hours, minutes (needs ACPI)</p>
<dt>&#8211;cpufreq</p>
<dd> CPU frequency in percentage (needs ACPI)</p>
<dt>&#8211;dbus</p>
<dd> number of dbus connections (needs python-dbus)</p>
<dt>&#8211;disk-tps</p>
<dd> per disk transactions per second (tps) stats</p>
<dt>&#8211;disk-util</p>
<dd> per disk utilization in percentage</p>
<dt>&#8211;dstat</p>
<dd> show dstat cputime consumption and latency</p>
<dt>&#8211;dstat-cpu</p>
<dd> show dstat advanced cpu usage</p>
<dt>&#8211;dstat-ctxt</p>
<dd> show dstat context switches</p>
<dt>&#8211;dstat-mem</p>
<dd> show dstat advanced memory usage</p>
<dt>&#8211;fan</p>
<dd> fan speed (needs ACPI)</p>
<dt>&#8211;freespace</p>
<dd> per filesystem disk usage</p>
<dt>&#8211;gpfs</p>
<dd> GPFS read/write I/O (needs mmpmon)</p>
<dt>&#8211;gpfs-ops</p>
<dd> GPFS filesystem operations (needs mmpmon)</p>
<dt>&#8211;helloworld</p>
<dd> Hello world example dstat plugin</p>
<dt>&#8211;innodb-buffer</p>
<dd> show innodb buffer stats</p>
<dt>&#8211;innodb-io</p>
<dd> show innodb I/O stats</p>
<dt>&#8211;innodb-ops</p>
<dd> show innodb operations counters</p>
<dt>&#8211;lustre</p>
<dd> show lustre I/O throughput</p>
<dt>&#8211;memcache-hits</p>
<dd> show the number of hits and misses from memcache</p>
<dt>&#8211;mysql5-cmds</p>
<dd> show the MySQL5 command stats</p>
<dt>&#8211;mysql5-conn</p>
<dd> show the MySQL5 connection stats</p>
<dt>&#8211;mysql5-io</p>
<dd> show the MySQL5 I/O stats</p>
<dt>&#8211;mysql5-keys</p>
<dd> show the MySQL5 keys stats</p>
<dt>&#8211;mysql-io</p>
<dd> show the MySQL I/O stats</p>
<dt>&#8211;mysql-keys</p>
<dd> show the MySQL keys stats</p>
<dt>&#8211;net-packets</p>
<dd> show the number of packets received and transmitted</p>
<dt>&#8211;nfs3</p>
<dd> show NFS v3 client operations</p>
<dt>&#8211;nfs3-ops</p>
<dd> show extended NFS v3 client operations</p>
<dt>&#8211;nfsd3</p>
<dd> show NFS v3 server operations</p>
<dt>&#8211;nfsd3-ops</p>
<dd> show extended NFS v3 server operations</p>
<dt>&#8211;ntp</p>
<dd> show NTP time from an NTP server</p>
<dt>&#8211;postfix</p>
<dd> show postfix queue sizes (needs postfix)</p>
<dt>&#8211;power</p>
<dd> show power usage</p>
<dt>&#8211;proc-count</p>
<dd> show total number of processes</p>
<dt>&#8211;qmail</p>
<dd> show qmail queue sizes (needs qmail)</p>
<dt>&#8211;rpc</p>
<dd> show RPC client calls stats</p>
<dt>&#8211;rpcd</p>
<dd> show RPC server calls stats</p>
<dt>&#8211;sendmail</p>
<dd> show sendmail queue size (needs sendmail)</p>
<dt>&#8211;snooze</p>
<dd> show number of ticks per second</p>
<dt>&#8211;squid</p>
<dd> show squid usage statistics</p>
<dt>&#8211;test</p>
<dd> show test plugin output</p>
<dt>&#8211;thermal</p>
<dd> system temperature sensors</p>
<dt>&#8211;top-bio</p>
<dd> show most expensive block I/O process</p>
<dt>&#8211;top-bio-adv</p>
<dd> show most expensive block I/O process (incl. pid and other stats)</p>
<dt>&#8211;top-childwait</p>
<dd> show process waiting for child the most</p>
<dt>&#8211;top-cpu</p>
<dd> show most expensive CPU process</p>
<dt>&#8211;top-cpu-adv</p>
<dd> show most expensive CPU process (incl. pid and other stats)</p>
<dt>&#8211;top-cputime</p>
<dd> show process using the most CPU time (in ms)</p>
<dt>&#8211;top-cputime-avg</p>
<dd> show process with the highest average timeslice (in ms)</p>
<dt>&#8211;top-int</p>
<dd> show most frequent interrupt</p>
<dt>&#8211;top-io</p>
<dd> show most expensive I/O process</p>
<dt>&#8211;top-io-adv</p>
<dd> show most expensive I/O process (incl. pid and other stats)</p>
<dt>&#8211;top-latency</p>
<dd> show process with highest total latency (in ms)</p>
<dt>&#8211;top-latency-avg</p>
<dd> show process with the highest average latency (in ms)</p>
<dt>&#8211;top-mem</p>
<dd> show process using the most memory</p>
<dt>&#8211;top-oom</p>
<dd> show process that will be killed by OOM the first</p>
<dt>&#8211;utmp</p>
<dd> show number of utmp connections (needs python-utmp)</p>
<dt>&#8211;vmk-hba</p>
<dd> show VMware ESX kernel vmhba stats</p>
<dt>&#8211;vmk-int</p>
<dd> show VMware ESX kernel interrupt stats</p>
<dt>&#8211;vmk-nic</p>
<dd> show VMware ESX kernel port stats</p>
<dt>&#8211;vm-memctl</p>
<dd> show ballooning status inside VMware guests</p>
<dt>&#8211;vz-cpu</p>
<dd> show CPU usage per OpenVZ guest</p>
<dt>&#8211;vz-io</p>
<dd> show I/O usage per OpenVZ guest</p>
<dt>&#8211;vz-ubc</p>
<dd> show OpenVZ user beancounters</p>
<dt>&#8211;wifi</p>
<dd> wireless link quality and signal to noise ratio</dl>
<h2>ARGUMENTS</h2>
<p> <code>delay</code> is the delay in seconds between each update </p>
<p> <code>count</code> is the number of updates to display before exiting </p>
<p> The default delay is 1 and count is unspecified (unlimited) </p>
<h2>INTERMEDIATE UPDATES</h2>
<p> When invoking dstat with a <code>delay</code> greater than 1 and without the <code>&#8211;noupdate</code> option, it will show intermediate updates, ie. the first time a 1 sec average, the second update a 2 second average, etc. until the delay has been reached. </p>
<p> So in case you specified a delay of 10, <code>the 9 intermediate updates are NOT snapshots</code>, they are averages over the time that passed since the last final update. The end result is that you get a 10 second average on a new line, just like with vmstat. </p>
<h2>EXAMPLES</h2>
<p> Using dstat to relate disk-throughput with network-usage (eth0), total CPU-usage and system counters: </p>
<pre>
dstat -dnyc -N eth0 -C total -f 5
</pre>
<p> Checking dstat&#8217;s behaviour and the system impact of dstat: </p>
<pre>
dstat -taf --debug
</pre>
<p> Using the time plugin together with cpu, net, disk, system, load, proc and top_cpu plugins: </p>
<pre>
dstat -tcndylp --top-cpu
</pre>
<p> this is identical to </p>
<pre><code>
dstat-- time-- cpu-- net-- disk-- sys-- load-- proc-- top - cpu
</code></pre>
<p> Using dstat to relate cpu stats with interrupts per device: </p>
<pre>
dstat -tcyif
</pre>
<h2>BUGS</h2>
<p> Since it is practically impossible to test dstat on every possible permutation of kernel, python or distribution version, I need your help and your feedback to fix the remaining problems. If you have improvements or bugreports, please send them to: [1]<i>dag [at] wieers.com</i> </p>
<p> <code>Note</code> Please see the TODO file for known bugs and future plans. </p>
<h2>FILES</h2>
<p> Paths that may contain external dstat_*.py plugins: </p>
<pre>
~/.dstat/
(path of binary)/plugins/
/usr/share/dstat/
/usr/local/share/dstat/
</pre>
<h2>SEE ALSO</h2>
<h3>Performance tools</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-ifstat/">ifstat</a>(1), <a href="//www.systutorials.com/docs/linux/man/8-iftop/">iftop</a>(8), <a href="//www.systutorials.com/docs/linux/man/1-iostat/">iostat</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-mpstat/">mpstat</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-netstat/">netstat</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-nfsstat/">nfsstat</a>(1), nstat, <a href="//www.systutorials.com/docs/linux/man/1-vmstat/">vmstat</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-xosview/">xosview</a>(1)
</pre>
<h3>Debugging tools</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-htop/">htop</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-lslk/">lslk</a>(1), <a href="//www.systutorials.com/docs/linux/man/8-lsof/">lsof</a>(8), <a href="//www.systutorials.com/docs/linux/man/1-top/">top</a>(1)
</pre>
<h3>Process tracing</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-ltrace/">ltrace</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-pmap/">pmap</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-ps/">ps</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-pstack/">pstack</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-strace/">strace</a>(1)
</pre>
<h3>Binary debugging</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-ldd/">ldd</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-file/">file</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-nm/">nm</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-objdump/">objdump</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-readelf/">readelf</a>(1)
</pre>
<h3>Memory usage tools</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-free/">free</a>(1), memusage, memusagestat, <a href="//www.systutorials.com/docs/linux/man/1-slabtop/">slabtop</a>(1)
</pre>
<h3>Accounting tools</h3>
<pre>
dump-acct, dump-utmp, <a href="//www.systutorials.com/docs/linux/man/8-sa/">sa</a>(8)
</pre>
<h3>Hardware debugging tools</h3>
<pre>
dmidecode, <a href="//www.systutorials.com/docs/linux/man/1-ifinfo/">ifinfo</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-lsdev/">lsdev</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-lshal/">lshal</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-lshw/">lshw</a>(1), <a href="//www.systutorials.com/docs/linux/man/8-lsmod/">lsmod</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-lspci/">lspci</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-lsusb/">lsusb</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-smartctl/">smartctl</a>(8), <a href="//www.systutorials.com/docs/linux/man/1-x86info/">x86info</a>(1)
</pre>
<h3>Application debugging</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/8-mailstats/">mailstats</a>(8), <a href="//www.systutorials.com/docs/linux/man/1-qshape/">qshape</a>(1)
</pre>
<h3>Xorg related tools</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-xdpyinfo/">xdpyinfo</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-xrestop/">xrestop</a>(1)
</pre>
<h3>Other useful info</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-collectl/">collectl</a>(1), <a href="//www.systutorials.com/docs/linux/man/5-proc/">proc</a>(5), <a href="//www.systutorials.com/docs/linux/man/8-procinfo/">procinfo</a>(8)
</pre>
<h2>AUTHOR</h2>
<p> Written by Dag Wieers [1]<i>dag [at] wieers.com</i> </p>
<p> Homepage at [2]<i><a rel="nofollow" href="http://dag.wieers.com/home-made/dstat/">http://dag.wieers.com/home-made/dstat/</a></i> </p>
<p> This manpage was initially written by Andrew Pollock [3]<i>apollock [at] debian.org</i> for the Debian GNU/Linux system. </p>
<h2>REFERENCES</h2>
<dl>
<dt>1. dag [at] wieers.com</p>
<dd> mailto:dag [at] wieers.com</p>
<dt>2.&nbsp;<wbr><a rel="nofollow" href="http://dag.wieers.com/home-made/dstat/">http://dag.wieers.com/home-made/dstat/</a></p>
<dd> <a rel="nofollow" href="http://dag.wieers.com/home-made/dstat/">http://dag.wieers.com/home-made/dstat/</a></p>
<dt>3. apollock [at] debian.org</p>
<dd> mailto:apollock [at] debian.org </p>
</dl>
<h2>Index</h2>
