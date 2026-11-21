---

title: "dstat(1)"
name: "dstat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dstat/"
description: "dstat – versatile tool for generating system resource statistics"
---

<p> dstat [-afv] [options..] [delay [count]] </p>
<p> Dstat is a versatile replacement for vmstat, iostat and ifstat. Dstat overcomes some of the limitations and adds some extra features. </p>
<p> Dstat allows you to view all of your system resources instantly, you can eg. compare disk usage in combination with interrupts from your IDE controller, or compare the network bandwidth numbers directly with the disk throughput (in the same interval). </p>
<p> Dstat also cleverly gives you the most detailed information in columns and clearly indicates in what magnitude and unit the output is displayed. Less confusion, less mistakes, more efficient. </p>
<p> Dstat is unique in letting you aggregate block device throughput for a certain diskset or network bandwidth for a group of interfaces, ie. you can see the throughput for all the block devices that make up a single filesystem or storage system. </p>
<p> Dstat allows its data to be directly written to a CSV file to be imported and used by OpenOffice, Gnumeric or Excel to create graphs. </p>
<p> <code>Note</code> Users of Sleuthkit might find Sleuthkit&#8217;s dstat being renamed to datastat to avoid a name conflict. See Debian bug #283709 for more information. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-c, &#8211;cpu</dt>
<dd> enable cpu stats (system, user, idle, wait, hardware interrupt, software interrupt)</dd>
<dt>-C 0,3,total</dt>
<dd> include cpu0, cpu3 and total (when using -c/&#8211;cpu)</dd>
<dt>-d, &#8211;disk</dt>
<dd> enable disk stats (read, write)</dd>
<dt>-D total,hda</dt>
<dd> include total and hda (when using -d/&#8211;disk)</dd>
<dt>-g, &#8211;page</dt>
<dd> enable page stats (page in, page out)</dd>
<dt>-i, &#8211;int</dt>
<dd> enable interrupt stats</dd>
<dt>-I 5,10</dt>
<dd> include interrupt 5 and 10 (when using -i/&#8211;int)</dd>
<dt>-l, &#8211;load</dt>
<dd> enable load average stats (1 min, 5 mins, 15mins)</dd>
<dt>-m, &#8211;mem</dt>
<dd> enable memory stats (used, buffers, cache, free)</dd>
<dt>-n, &#8211;net</dt>
<dd> enable network stats (receive, send)</dd>
<dt>-N eth1,total</dt>
<dd> include eth1 and total (when using -n/&#8211;net)</dd>
<dt>-p, &#8211;proc</dt>
<dd> enable process stats (runnable, uninterruptible, new)</dd>
<dt>-r, &#8211;io</dt>
<dd> enable I/O request stats (read, write requests)</dd>
<dt>-s, &#8211;swap</dt>
<dd> enable swap stats (used, free)</dd>
<dt>-S swap1,total</dt>
<dd> include swap1 and total (when using -s/&#8211;swap)</dd>
<dt>-t, &#8211;time</dt>
<dd> enable time/date output</dd>
<dt>-T, &#8211;epoch</dt>
<dd> enable time counter (seconds since epoch)</dd>
<dt>-y, &#8211;sys</dt>
<dd> enable system stats (interrupts, context switches)</dd>
<dt>&#8211;aio</dt>
<dd> enable aio stats (asynchronous I/O)</dd>
<dt>&#8211;fs, &#8211;filesystem</dt>
<dd> enable filesystem stats (open files, inodes)</dd>
<dt>&#8211;ipc</dt>
<dd> enable ipc stats (message queue, semaphores, shared memory)</dd>
<dt>&#8211;lock</dt>
<dd> enable file lock stats (posix, flock, read, write)</dd>
<dt>&#8211;raw</dt>
<dd> enable raw stats (raw sockets)</dd>
<dt>&#8211;socket</dt>
<dd> enable socket stats (total, tcp, udp, raw, ip-fragments)</dd>
<dt>&#8211;tcp</dt>
<dd> enable tcp stats (listen, established, syn, time_wait, close)</dd>
<dt>&#8211;udp</dt>
<dd> enable udp stats (listen, active)</dd>
<dt>&#8211;unix</dt>
<dd> enable unix stats (datagram, stream, listen, active)</dd>
<dt>&#8211;vm</dt>
<dd> enable vm stats (hard pagefaults, soft pagefaults, allocated, free)</dd>
<dt>&#8211;plugin-name</dt>
<dd> enable (external) plugins by plugin name, see <code>PLUGINS</code> for options</dd>
<dt>Possible internal stats are</dt>
<dd> aio, cpu, cpu24, disk, disk24, disk24old, epoch, fs, int, int24, io, ipc, load, lock, mem, net, page, page24, proc, raw, socket, swap, swapold, sys, tcp, time, udp, unix, vm</dd>
<dt>&#8211;list</dt>
<dd> list the internal and external plugin names</dd>
<dt>-a, &#8211;all</dt>
<dd> equals -cdngy (default)</dd>
<dt>-f, &#8211;full</dt>
<dd> expand -C, -D, -I, -N and -S discovery lists</dd>
<dt>-v, &#8211;vmstat</dt>
<dd> equals -pmgdsc -D total</dd>
<dt>&#8211;bits</dt>
<dd> force bits for values expressed in bytes</dd>
<dt>&#8211;float</dt>
<dd> force float values on screen (mutual exclusive with <code>&#8211;integer</code>)</dd>
<dt>&#8211;integer</dt>
<dd> force integer values on screen (mutual exclusive with <code>&#8211;float</code>)</dd>
<dt>&#8211;bw, &#8211;blackonwhite</dt>
<dd> change colors for white background terminal</dd>
<dt>&#8211;nocolor</dt>
<dd> disable colors (implies <code>&#8211;noupdate</code>)</dd>
<dt>&#8211;noheaders</dt>
<dd> disable repetitive headers</dd>
<dt>&#8211;noupdate</dt>
<dd> disable intermediate updates when delay &gt; 1</dd>
<dt>&#8211;output file</dt>
<dd> write CSV output to file</dd>
<dt>&#8211;profile</dt>
<dd> show profiling statistics when exiting dstat</dd></dl>
<h2>PLUGINS</h2>
<p> While anyone can create their own dstat plugins (and contribute them) dstat ships with a number of plugins already that extend its capabilities greatly. Here is an overview of the plugins dstat ships with: </p>
<dl>
<dt>&#8211;battery</dt>
<dd> battery in percentage (needs ACPI)</dd>
<dt>&#8211;battery-remain</dt>
<dd> battery remaining in hours, minutes (needs ACPI)</dd>
<dt>&#8211;cpufreq</dt>
<dd> CPU frequency in percentage (needs ACPI)</dd>
<dt>&#8211;dbus</dt>
<dd> number of dbus connections (needs python-dbus)</dd>
<dt>&#8211;disk-tps</dt>
<dd> per disk transactions per second (tps) stats</dd>
<dt>&#8211;disk-util</dt>
<dd> per disk utilization in percentage</dd>
<dt>&#8211;dstat</dt>
<dd> show dstat cputime consumption and latency</dd>
<dt>&#8211;dstat-cpu</dt>
<dd> show dstat advanced cpu usage</dd>
<dt>&#8211;dstat-ctxt</dt>
<dd> show dstat context switches</dd>
<dt>&#8211;dstat-mem</dt>
<dd> show dstat advanced memory usage</dd>
<dt>&#8211;fan</dt>
<dd> fan speed (needs ACPI)</dd>
<dt>&#8211;freespace</dt>
<dd> per filesystem disk usage</dd>
<dt>&#8211;gpfs</dt>
<dd> GPFS read/write I/O (needs mmpmon)</dd>
<dt>&#8211;gpfs-ops</dt>
<dd> GPFS filesystem operations (needs mmpmon)</dd>
<dt>&#8211;helloworld</dt>
<dd> Hello world example dstat plugin</dd>
<dt>&#8211;innodb-buffer</dt>
<dd> show innodb buffer stats</dd>
<dt>&#8211;innodb-io</dt>
<dd> show innodb I/O stats</dd>
<dt>&#8211;innodb-ops</dt>
<dd> show innodb operations counters</dd>
<dt>&#8211;lustre</dt>
<dd> show lustre I/O throughput</dd>
<dt>&#8211;memcache-hits</dt>
<dd> show the number of hits and misses from memcache</dd>
<dt>&#8211;mysql5-cmds</dt>
<dd> show the MySQL5 command stats</dd>
<dt>&#8211;mysql5-conn</dt>
<dd> show the MySQL5 connection stats</dd>
<dt>&#8211;mysql5-io</dt>
<dd> show the MySQL5 I/O stats</dd>
<dt>&#8211;mysql5-keys</dt>
<dd> show the MySQL5 keys stats</dd>
<dt>&#8211;mysql-io</dt>
<dd> show the MySQL I/O stats</dd>
<dt>&#8211;mysql-keys</dt>
<dd> show the MySQL keys stats</dd>
<dt>&#8211;net-packets</dt>
<dd> show the number of packets received and transmitted</dd>
<dt>&#8211;nfs3</dt>
<dd> show NFS v3 client operations</dd>
<dt>&#8211;nfs3-ops</dt>
<dd> show extended NFS v3 client operations</dd>
<dt>&#8211;nfsd3</dt>
<dd> show NFS v3 server operations</dd>
<dt>&#8211;nfsd3-ops</dt>
<dd> show extended NFS v3 server operations</dd>
<dt>&#8211;ntp</dt>
<dd> show NTP time from an NTP server</dd>
<dt>&#8211;postfix</dt>
<dd> show postfix queue sizes (needs postfix)</dd>
<dt>&#8211;power</dt>
<dd> show power usage</dd>
<dt>&#8211;proc-count</dt>
<dd> show total number of processes</dd>
<dt>&#8211;qmail</dt>
<dd> show qmail queue sizes (needs qmail)</dd>
<dt>&#8211;rpc</dt>
<dd> show RPC client calls stats</dd>
<dt>&#8211;rpcd</dt>
<dd> show RPC server calls stats</dd>
<dt>&#8211;sendmail</dt>
<dd> show sendmail queue size (needs sendmail)</dd>
<dt>&#8211;snooze</dt>
<dd> show number of ticks per second</dd>
<dt>&#8211;squid</dt>
<dd> show squid usage statistics</dd>
<dt>&#8211;test</dt>
<dd> show test plugin output</dd>
<dt>&#8211;thermal</dt>
<dd> system temperature sensors</dd>
<dt>&#8211;top-bio</dt>
<dd> show most expensive block I/O process</dd>
<dt>&#8211;top-bio-adv</dt>
<dd> show most expensive block I/O process (incl. pid and other stats)</dd>
<dt>&#8211;top-childwait</dt>
<dd> show process waiting for child the most</dd>
<dt>&#8211;top-cpu</dt>
<dd> show most expensive CPU process</dd>
<dt>&#8211;top-cpu-adv</dt>
<dd> show most expensive CPU process (incl. pid and other stats)</dd>
<dt>&#8211;top-cputime</dt>
<dd> show process using the most CPU time (in ms)</dd>
<dt>&#8211;top-cputime-avg</dt>
<dd> show process with the highest average timeslice (in ms)</dd>
<dt>&#8211;top-int</dt>
<dd> show most frequent interrupt</dd>
<dt>&#8211;top-io</dt>
<dd> show most expensive I/O process</dd>
<dt>&#8211;top-io-adv</dt>
<dd> show most expensive I/O process (incl. pid and other stats)</dd>
<dt>&#8211;top-latency</dt>
<dd> show process with highest total latency (in ms)</dd>
<dt>&#8211;top-latency-avg</dt>
<dd> show process with the highest average latency (in ms)</dd>
<dt>&#8211;top-mem</dt>
<dd> show process using the most memory</dd>
<dt>&#8211;top-oom</dt>
<dd> show process that will be killed by OOM the first</dd>
<dt>&#8211;utmp</dt>
<dd> show number of utmp connections (needs python-utmp)</dd>
<dt>&#8211;vmk-hba</dt>
<dd> show VMware ESX kernel vmhba stats</dd>
<dt>&#8211;vmk-int</dt>
<dd> show VMware ESX kernel interrupt stats</dd>
<dt>&#8211;vmk-nic</dt>
<dd> show VMware ESX kernel port stats</dd>
<dt>&#8211;vm-memctl</dt>
<dd> show ballooning status inside VMware guests</dd>
<dt>&#8211;vz-cpu</dt>
<dd> show CPU usage per OpenVZ guest</dd>
<dt>&#8211;vz-io</dt>
<dd> show I/O usage per OpenVZ guest</dd>
<dt>&#8211;vz-ubc</dt>
<dd> show OpenVZ user beancounters</dd>
<dt>&#8211;wifi</dt>
<dd> wireless link quality and signal to noise ratio</dd></dl>
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
<a href="//www.systutorials.com/docs/linux/man/1-ifstat/">ifstat</a>(1), <a href="//www.systutorials.com/docs/linux/man/8-iftop/">iftop</a>(8), <a href="//www.systutorials.com/docs/linux/man/1-iostat/">iostat</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-mpstat/">mpstat</a>(1), netstat(1), nfsstat(1), nstat, vmstat(1), xosview(1)
</pre>
<h3>Debugging tools</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-htop/">htop</a>(1), lslk(1), <a href="//www.systutorials.com/docs/linux/man/8-lsof/">lsof</a>(8), <a href="//www.systutorials.com/docs/linux/man/1-top/">top</a>(1)
</pre>
<h3>Process tracing</h3>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-ltrace/">ltrace</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-pmap/">pmap</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-ps/">ps</a>(1), pstack(1), <a href="//www.systutorials.com/docs/linux/man/1-strace/">strace</a>(1)
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
dmidecode, ifinfo(1), lsdev(1), <a href="//www.systutorials.com/docs/linux/man/1-lshal/">lshal</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-lshw/">lshw</a>(1), <a href="//www.systutorials.com/docs/linux/man/8-lsmod/">lsmod</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-lspci/">lspci</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-lsusb/">lsusb</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-smartctl/">smartctl</a>(8), x86info(1)
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
<a href="//www.systutorials.com/docs/linux/man/1-collectl/">collectl</a>(1), <a href="//www.systutorials.com/docs/linux/man/5-proc/">proc</a>(5), procinfo(8)
</pre>
<h2>AUTHOR</h2>
<p> Written by Dag Wieers [1]<i>dag [at] wieers.com</i> </p>
<p> Homepage at [2]<i><a rel="nofollow" href="http://dag.wieers.com/home-made/dstat/">http://dag.wieers.com/home-made/dstat/</a></i> </p>
<p> This manpage was initially written by Andrew Pollock [3]<i>apollock [at] debian.org</i> for the Debian GNU/Linux system. </p>
<h2>REFERENCES</h2>
<dl>
<dt>1. dag [at] wieers.com</dt>
<dd> mailto:dag [at] wieers.com</dd>
<dt>2.&nbsp;<wbr><a rel="nofollow" href="http://dag.wieers.com/home-made/dstat/">http://dag.wieers.com/home-made/dstat/</a></dt>
<dd> <a rel="nofollow" href="http://dag.wieers.com/home-made/dstat/">http://dag.wieers.com/home-made/dstat/</a></dd>
<dt>3. apollock [at] debian.org</dt>
<dd> mailto:apollock [at] debian.org </dd>
</dl>
