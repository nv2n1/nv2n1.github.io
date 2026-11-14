---
title: "ifpps(8)"
name: "ifpps"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifpps/"
description: "ifpps – top-like networking and system statistics"
---

<p>ifpps &#8211; top-like networking and system statistics </p>
<h2>Synopsis</h2>
<p><code>ifpps</code> { [<i>options</i>] | [<i>device</i>] } </p>
<h2>Description</h2>
<p>ifpps is a small utility which periodically provides top-like networking and system statistics from the kernel. ifpps gathers its data directly from procfs files and does not make use of any user space monitoring libraries which would falsify statistics under high load. For instance, consider the following scenario: two directly connected Linux machines with Intel Core 2 Quad Q6600 2.40GHz CPUs, 4 GB RAM, and an Intel 82566DC-2 Gigabit Ethernet NIC are used for performance evaluation. One machine generates 64 byte network packets by using the kernel space packet generator pktgen with a maximum possible packet rate. The other machine displays statistics about incoming network packets by using i) <a href="/docs/linux/man/8-iptraf/">iptraf</a>(8) and ii) ifpps. iptraf which incorporates <a href="/docs/linux/man/3-pcap/">pcap</a>(3) shows an average packet rate of 246,000 pps while on the other hand ifpps shows an average packet rate of 1,378,000 pps. Hence, due to packet copies and deferring statistics creation into user space, a measurement error of approximately 460 percent occurs. Tools like iptraf might display much more information such as TCP per flow statistics (hence the use of the pcap library). This is not possible with ifpps, because overall networking statistics are its focus; statistics, which are also fairly reliable under high packet load. ifpps also periodically displays CPU load, interrupt, software interrupt data per sample interval as well as total interrupts, all per CPU. In case the number of CPUs exceeds 5 or the number specified by the user with the &#8220;-n&#8221; command line option, ifpps will only display this number top heavy hitters. The topmost heavy hitter CPU will be marked with &#8220;+&#8221;. The least heavy hitter will always be displayed and is marked with &#8220;-&#8220;. In addition, the average for all the above per-CPU data is shown. Optionally the median values can be displayed using the &#8220;-m&#8221; command line option. ifpps also supports directly the <a href="/docs/linux/man/1-gnuplot/">gnuplot</a>(1) data sample format. This facilitates creation of gnuplot figures from ifpps time series. </p>
<h2>Options</h2>
<h3>-d &lt;netdev&gt;, &#8211;dev &lt;netdev&gt;</h3>
<p>Networking device to fetch statistics from, for example eth0, wlan0.</p>
<h3>-n, &#8211;num-cpus</h3>
<p>Set maximum number of top hitter CPUs (in terms of time spent in system/user mode) to display in ncurses mode, default is 10.</p>
<h3>-t &lt;time&gt;, &#8211;interval &lt;time&gt;</h3>
<p>Statistics refresh interval in milliseconds, default is 1000ms.</p>
<h3>-c, &#8211;csv</h3>
<p>Output (once) the ncurses data to the terminal as <a href="/docs/linux/man/1-gnuplot/">gnuplot</a>(1)-ready data.</p>
<h3>-l, &#8211;loop</h3>
<p>Continuously output the terminal data after a refresh interval. This option is only available, if option &#8220;-c&#8221; is given. For &#8220;-l&#8221; it is usually recommended to redirect the output into a file that is to be be processed later with <a href="/docs/linux/man/1-gnuplot/">gnuplot</a>(1).</p>
<h3>-m, &#8211;median</h3>
<p>Show median values across all CPUs for CPU load, interrupts (per interval and absolute) and software interrupts.</p>
<h3>-p, &#8211;promisc</h3>
<p>Turn on promiscuous mode for the given networking device.</p>
<h3>-W, &#8211;no-warn</h3>
<p>Suppress possible warnings in the ncurses output, e.g. about a too low sampling interval that could cause performance regression.</p>
<h3>-v, &#8211;version</h3>
<p>Show version information.</p>
<h3>-h, &#8211;help</h3>
<p>Show user help.</p>
<h2>Usage Example</h2>
<h3>ifpps eth0</h3>
<p>Default ncurses output for the eth0 device.</p>
<h3>ifpps -pd eth0</h3>
<p>Ncurses output for the eth0 device in promiscuous mode.</p>
<h3>ifpps -lpcd wlan0 &gt; plot.dat</h3>
<p>Continuous terminal output for the wlan0 device in promiscuous mode.</p>
<h2>Note</h2>
<p>On 10Gbit/s cards or higher, receive and transmit statistics are usually accumulated at a higher duration interval than 1 second. Thus, it might be advisable to alter the timing to a higher accumulation interval for such cards.</p>
<h2>Legal</h2>
<p>ifpps is licensed under the GNU GPL version 2.0.</p>
<h2>History</h2>
<p><code>ifpps</code> was originally written for the netsniff-ng toolkit by Daniel Borkmann. It is currently maintained by Tobias Klauser &lt;tklauser [at] distanz.ch&gt; and Daniel Borkmann &lt;dborkma [at] tik.ee.ethz.ch&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-netsniff-ng/">netsniff-ng</a></code>(8), <code><a href="/docs/linux/man/8-trafgen/">trafgen</a></code>(8), <code><a href="/docs/linux/man/8-mausezahn/">mausezahn</a></code>(8), <code><a href="/docs/linux/man/8-bpfc/">bpfc</a></code>(8), <code><a href="/docs/linux/man/8-flowtop/">flowtop</a></code>(8), <code><a href="/docs/linux/man/8-astraceroute/">astraceroute</a></code>(8), <code><a href="/docs/linux/man/8-curvetun/">curvetun</a></code>(8) </p>
<h2>Author</h2>
<p>Manpage was written by Daniel Borkmann.</p>
<h2>Colophon</h2>
<p>This page is part of the Linux netsniff-ng toolkit project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://netsniff-ng.org/.">http://netsniff-ng.org/.</a> </p>
