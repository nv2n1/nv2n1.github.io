---
title: "atopsar(1)"
name: "atopsar"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atopsar/"
description: "atopsar – Advanced System Activity Report (atop related)"
---

<h2>NAME</h2>
<p> <code>atopsar</code> &#8211; Advanced System Activity Report (atop related)</p>
<h2>SYNOPSIS</h2>
<p> <code>atopsar</code> [-flags&#8230;] [-r <i>file|date</i> ] [-R <i>cnt</i> ] [-b <i>hh:mm</i> ] [-e <i>hh:mm</i> ]<br />
 <code>atopsar</code> [-flags&#8230;] <i>interval</i> [ <i>samples</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The program <i>atopsar</i> can be used to report statistics on system level. </p>
<p> In the first synopsis line (no sampling interval specified), <i>atopsar</i> extracts data from a raw logfile that has been recorded previously by the program <i>atop</i> (option <code>-w </code> of the <i>atop</i> program).<br />
 You can specify the name of the logfile with the <code>-r</code> option of the <i>atopsar</i> program. When a daily logfile of <i>atop</i> is used, named <code>/var/log/atop/atop_YYYYMMDD</code> (where YYYYMMDD reflects the date), the required date of the form YYYYMMDD can be specified with the <code>-r</code> option instead of the filename, or the symbolic name &#8216;y&#8217; can be used for yesterday&#8217;s daily logfile (this can be repeated so &#8216;yyyy&#8217; indicates the logfile of four days ago). If the <code>-r</code> option is not specified at all, today&#8217;s daily logfile is used by default.<br />
 The starting and ending times of the report can be defined using the options <code>-b</code> and <code>-e</code> followed by a time argument of the form hh:mm. </p>
<p> In the second synopsis line, <code>atopsar</code> reads actual activity counters from the kernel with the specified <i>interval</i> (in seconds) and the specified number of <i>samples</i> (optionally). When <code>atopsar</code> is activated in this way it immediately sends the output for every requested report to standard output. If only one type of report is requested, the header is printed once and after every <i>interval</i> seconds the statistical counters are shown for that period. If several reports are requested, a header is printed per sample followed by the statistical counters for that period. </p>
<p> Some generic flags can be specified to influence the behaviour of the <code>atopsar</code> program: </p>
<dl>
<dt><code>-S</code></p>
<dd> By default the timestamp at the beginning of a line is suppressed if more lines are shown for one interval. With this flag a timestamp is given for every output-line (easier for post-processing).</dl>
<dl>
<dt><code>-a</code></p>
<dd> By default certain resources as disks and network interfaces are only shown when they were active during the interval. With this flag all resources of a given type are shown, even if they were inactive during the interval.</dl>
<dl>
<dt><code>-x</code></p>
<dd> By default <code>atopsar</code> only uses colors if output is directed to a terminal (window). These colors might indicate that a critical occupation percentage has been reached (red) or has been almost reached (cyan) for a particular resource. See the man-page of <code>atop</code> for a detailed description of this feature (section COLORS).<br />
 With the flag <code>-x</code> the use of colors is suppressed unconditionally.</dl>
<dl>
<dt><code>-C</code></p>
<dd> By default <code>atopsar</code> only uses colors if output is directed to a terminal (window). These colors might indicate that a critical occupation percentage has been reached (red) or has been almost reached (cyan) for a particular resource. See the man-page of <code>atop</code> for a detailed description of this feature (section COLORS).<br />
 With the flag <code>-C</code> colors will always be used, even if output is not directed to a terminal.</dl>
<dl>
<dt><code>-M</code></p>
<dd> Use markers at the end of a line to indicate that a critical occupation percentage has been reached (&#8216;*&#8217;) or has been almost reached (&#8216;+&#8217;) for particular resources. The marker &#8216;*&#8217; is similar to the color red and the marker &#8216;+&#8217; to the color cyan. See the man-page of <code>atop</code> for a detailed description of these colors (section COLORS).</dl>
<dl>
<dt><code>-H</code></p>
<dd> Repeat the header line within a report for every <i>N</i> detail lines. The value of <i>N </i> is determined dynamically in case of output to a tty/window (depending on the number of lines); for output to a file or pipe this value is 23.</dl>
<dl>
<dt><code>-R</code></p>
<dd> Summarize <i>cnt</i> samples into one sample. When the logfile contains e.g. samples of 10 minutes, the use of the flag &#8216;-R 6&#8217; shows a report with one sample for every hour.</dl>
<p> Other flags are used to define which reports are required: </p>
<dl>
<dt><code>-A</code></p>
<dd> Show all possible reports.</dl>
<dl>
<dt><code>-c</code></p>
<dd> Report about CPU utilization (in total and per cpu).</dl>
<dl>
<dt><code>-p</code></p>
<dd> Report about processor-related matters, like load-averages and hardware interrupts.</dl>
<dl>
<dt><code>-P</code></p>
<dd> Report about processes.</dl>
<dl>
<dt><code>-m</code></p>
<dd> Current memory- and swap-occupation.</dl>
<dl>
<dt><code>-s</code></p>
<dd> Report about paging- and swapping-activity, and overcommitment.</dl>
<dl>
<dt><code>-l</code></p>
<dd> Report about utilization of logical volumes.</dl>
<dl>
<dt><code>-f</code></p>
<dd> Report about utilization of multiple devices.</dl>
<dl>
<dt><code>-d</code></p>
<dd> Report about utilization of disks.</dl>
<dl>
<dt><code>-i</code></p>
<dd> Report about the network interfaces.</dl>
<dl>
<dt><code>-I</code></p>
<dd> Report about errors for network-interfaces.</dl>
<dl>
<dt><code>-w</code></p>
<dd> Report about IP version 4 network traffic.</dl>
<dl>
<dt><code>-W</code></p>
<dd> Report about errors for IP version 4 traffic.</dl>
<dl>
<dt><code>-y</code></p>
<dd> General report about ICMP version 4 layer activity.</dl>
<dl>
<dt><code>-Y</code></p>
<dd> Per-type report about ICMP version 4 layer activity.</dl>
<dl>
<dt><code>-u</code></p>
<dd> Report about UDP version 4 network traffic.</dl>
<dl>
<dt><code>-z</code></p>
<dd> Report about IP version 6 network traffic.</dl>
<dl>
<dt><code>-Z</code></p>
<dd> Report about errors for IP version 6 traffic.</dl>
<dl>
<dt><code>-k</code></p>
<dd> General report about ICMP version 6 layer activity.</dl>
<dl>
<dt><code>-K</code></p>
<dd> Per-type report about ICMP version 6 layer activity.</dl>
<dl>
<dt><code>-U</code></p>
<dd> Report about UDP version 6 network traffic.</dl>
<dl>
<dt><code>-t</code></p>
<dd> Report about TCP network traffic.</dl>
<dl>
<dt><code>-T</code></p>
<dd> Report about errors for TCP-traffic.</dl>
<dl>
<dt><code>-O</code></p>
<dd> Report about top-3 processes consuming most processor capacity. This report is only available when using a log file (not when specifying an interval).</dl>
<dl>
<dt><code>-G</code></p>
<dd> Report about top-3 processes consuming most resident memory. This report is only available when using a log file (not when specifying an interval).</dl>
<dl>
<dt><code>-D</code></p>
<dd> Report about top-3 processes issueing most disk transfers. This report is only available when using a log file (not when specifying an interval).</dl>
<dl>
<dt><code>-N</code></p>
<dd> Report about top-3 processes issueing most IPv4/IPv6 socket transfers. This report is only available when using a log file (not when specifying an interval).</dl>
<h2>OUTPUT DESCRIPTION</h2>
<p> Depending on the requested report, a number of columns with output values are produced. The values are mostly presented as a number of events per second. </p>
<p> The output for the flag <code>-c</code> contains the following columns per cpu:</p>
<dl>
<dt><code>usr%</code></p>
<dd> Percentage of cpu-time consumed in user mode (program text) for all active processes running with a nice value of zero (default) or a negative nice value (which means a higher priority than usual). The cpu consumption in user mode of processes with a nice value larger than zero (lower priority) is indicated in the nice%-column.</p>
<dt><code>nice%</code></p>
<dd> Percentage of cpu time consumed in user mode (i.e. program text) for all processes running witn a nice value larger than zero (which means with a lower priority than average).</p>
<dt><code>sys%</code></p>
<dd> Percentage of cpu time consumed in system mode (kernel text) for all active processes. A high percentage usually indicates a lot of system calls being issued.</p>
<dt><code>irq%</code></p>
<dd> Percentage of cpu time consumed for handling of device interrupts.</p>
<dt><code>softirq%</code></p>
<dd> Percentage of cpu time consumed for soft interrupt handling.</p>
<dt><code>steal%</code></p>
<dd> Percentage of cpu time stolen by other virtual machines running on the same hardware.</p>
<dt><code>guest%</code></p>
<dd> Percentage of cpu time used by other virtual machines running on the same hardware (overlaps with usr%/nice%).</p>
<dt><code>wait%</code></p>
<dd> Percentage of unused cpu time while at least one of the processes in wait-state awaits completion of disk I/O.</p>
<dt><code>idle%</code></p>
<dd> Percentage of unused cpu time because all processes are in a wait-state but not waiting for disk-I/O.</dl>
<p> The output for the flag <code>-p</code> contains the following values:</p>
<dl>
<dt><code>pswch/s</code></p>
<dd> Number of process switches (also called context switches) per second on this cpu. A process switch occurs at the moment that an active thread (i.e. the thread using a cpu) enters a wait state or has used its time slice completely; another thread will then be chosen to use the cpu.</p>
<dt><code>devintr/s</code></p>
<dd> Number of hardware interrupts handled per second on this cpu.</p>
<dt><code>clones/s</code></p>
<dd> The number of new threads started per second.</p>
<dt><code>loadavg1</code></p>
<dd> Load average reflecting the average number of threads in the runqueue or in non-interruptible wait state (usually waiting for disk or tape I/O) during the last minute.</p>
<dt><code>loadavg5</code></p>
<dd> Load average reflecting the average number of threads in the runqueue or in non-interruptible wait state (usually waiting for disk or tape I/O) during the last 5 minutes.</p>
<dt><code>loadavg15</code></p>
<dd> Load average reflecting the average number of threads in the runqueue or in non-interruptible wait state (usually waiting for disk or tape I/O) during the last 15 minutes.</dl>
<p> The output for the flag <code>-P</code> contains information about the processes and threads:</p>
<dl>
<dt><code>clones/s</code></p>
<dd> The number of new threads started per second.</p>
<dt><code>pexit/s</code></p>
<dd>
<dt><code>curproc</code></p>
<dd> Total number of processes present in the system.</p>
<dt><code>curzomb</code></p>
<dd> Number of zombie processes present in the system.</p>
<dt><code>thrrun</code></p>
<dd> Total number of threads present in the system in state &#8216;running&#8217;.</p>
<dt><code>thrslpi</code></p>
<dd> Total number of threads present in the system in state &#8216;interruptible sleeping&#8217;.</p>
<dt><code>thrslpu</code></p>
<dd> Total number of threads present in the system in state &#8216;uninterruptible sleeping&#8217;.</dl>
<p> The output for the flag <code>-m</code> contains information about the memory- and swap-utilization:</p>
<dl>
<dt><code>memtotal</code></p>
<dd> Total usable main memory size.</p>
<dt><code>memfree</code></p>
<dd> Available main memory size at this moment (snapshot).</p>
<dt><code>buffers</code></p>
<dd> Main memory used at this moment to cache metadata-blocks (snapshot).</p>
<dt><code>cached</code></p>
<dd> Main memory used at this moment to cache data-blocks (snapshot).</p>
<dt><code>dirty</code></p>
<dd> Amount of memory in the page cache that still has to be flushed to disk at this moment (snapshot).</p>
<dt><code>slabmem</code></p>
<dd> Main memory used at this moment for dynamically allocated memory by the kernel (snapshot).</p>
<dt><code>swptotal</code></p>
<dd> Total swap space size at this moment (snapshot).</p>
<dt><code>swpfree</code></p>
<dd> Available swap space at this moment (snapshot).</dl>
<p> The output for the flag <code>-s</code> contains information about the frequency of swapping:</p>
<dl>
<dt><code>pagescan/s</code></p>
<dd> Number of scanned pages per second due to the fact that free memory drops below a particular threshold.</p>
<dt><code>swapin/s</code></p>
<dd> The number of memory-pages the system read from the swap-device per second.</p>
<dt><code>swapout/s</code></p>
<dd> The number of memory-pages the system wrote to the swap-device per second.</p>
<dt><code>commitspc</code></p>
<dd> The committed virtual memory space i.e. the reserved virtual space for all allocations of private memory space for processes.</p>
<dt><code>commitlim</code></p>
<dd> The maximum limit for the committed space, which is by default swap size plus 50% of memory size. The kernel only verifies whether the committed space exceeds the limit if strict overcommit handling is configured (vm.overcommit_memory is 2).</dl>
<p> The output for the flags <code>-l</code> (LVM), <code>-f</code> (MD), and <code>-d </code> (hard disk) contains the following columns per active unit:</p>
<dl>
<dt><code>disk</code></p>
<dd> Name.</p>
<dt><code>busy</code></p>
<dd> Busy-percentage of the unit (i.e. the portion of time that the device was busy handling requests).</p>
<dt><code>read/s</code></p>
<dd> Number of read-requests issued per second on this unit.</p>
<dt><code>KB/read</code></p>
<dd> Average number of Kbytes transferred per read-request for this unit.</p>
<dt><code>writ/s</code></p>
<dd> Number of write-requests issued per second on this unit.</p>
<dt><code>KB/writ</code></p>
<dd> Average number of Kbytes transferred per write-request for this unit.</p>
<dt><code>avque</code></p>
<dd> Average number of requests outstanding in the queue during the time that the unit is busy.</p>
<dt><code>avserv</code></p>
<dd> Average number of milliseconds needed by a request on this unit (seek, latency and data-transfer).</dl>
<p> The output for the flag <code>-i</code> provides information about utilization of network interfaces:</p>
<dl>
<dt><code>interf</code></p>
<dd> Name of interface.</p>
<dt><code>busy</code></p>
<dd> Busy percentage for this interface. If the linespeed of this interface could not be determined (for virtual interfaces or in case that <code>atop</code> or <code>atopsar</code> had no root-privileges), a question mark is shown.</p>
<dt><code>ipack/s</code></p>
<dd> Number of packets received from this interface per second.</p>
<dt><code>opack/s</code></p>
<dd> Number of packets transmitted to this interface per second.</p>
<dt><code>iKbyte/s</code></p>
<dd> Number of Kbytes received from this interface per second.</p>
<dt><code>oKbyte/s</code></p>
<dd> Number of Kbytes transmitted via this interface per second.</p>
<dt><code>imbps/s</code></p>
<dd> Effective number of megabits received per second.</p>
<dt><code>ombps/s</code></p>
<dd> Effective number of megabits transmitted per second.</p>
<dt><code>maxmbps/s</code></p>
<dd> Linespeed as number of megabits per second. If the linespeed could not be determined (for virtual interfaces or in case that <code>atop</code> or <code>atopsar</code> had no root-privileges), value 0 is shown.<br />
 The linespeed is followed by the indication &#8216;f&#8217; (full duplex) or &#8216;h&#8217; (half duplex).</dl>
<p> The output for the flag <code>-I</code> provides information about the failures that were detected for network interfaces:</p>
<dl>
<dt><code>interf</code></p>
<dd> Name of interface.</p>
<dt><code>ierr/s</code></p>
<dd> Number of bad packets received from this interface per second.</p>
<dt><code>oerr/s</code></p>
<dd> Number of times that packet transmission to this interface failed per second.</p>
<dt><code>coll/s</code></p>
<dd> Number of collisions encountered per second while transmitting packets.</p>
<dt><code>idrop/s</code></p>
<dd> Number of received packets dropped per second due to lack of buffer-space in the local system.</p>
<dt><code>odrop/s</code></p>
<dd> Number of transmitted packets dropped per second due to lack of buffer-space in the local system.</p>
<dt><code>iframe/s</code></p>
<dd> Number of frame alignment-errors encountered per second on received packets.</p>
<dt><code>ocarrier/s</code></p>
<dd> Number of carrier-errors encountered per second on transmitted packets.</dl>
<p> The output for the flag <code>-w</code> provides information about the utilization of the IPv4-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>inrecv/s</code></p>
<dd> Number of IP datagrams received from interfaces per second, including those received in error (ipInReceives).</p>
<dt><code>outreq/s</code></p>
<dd> Number of IP datagrams that local higher-layer protocols supplied to IP in requests for transmission per second (ipOutRequests).</p>
<dt><code>indeliver/s</code></p>
<dd> Number of received IP datagrams that have been successfully delivered to higher protocol-layers per second (ipInDelivers).</p>
<dt><code>forward/s</code></p>
<dd> Number of received IP datagrams per second for which this entity was not their final IP destination, as a result of which an attempt was made to forward (ipForwDatagrams).</p>
<dt><code>reasmok/s</code></p>
<dd> Number of IP datagrams successfully reassembled per second (ipReasmOKs).</p>
<dt><code>fragcreat/s</code></p>
<dd> Number of IP datagram fragments generated per second at this entity (ipFragCreates).</dl>
<p> The output for the flag <code>-W</code> provides information about the failures that were detected in the IPv4-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>in: dsc/s</code></p>
<dd> Number of input IP datagrams per second for which no problems were encountered to prevent their continued processing but that were discarded, e.g. for lack of buffer space (ipInDiscards).</p>
<dt><code>in: hder/s</code></p>
<dd> Number of input IP datagrams per second discarded due to errors in the IP header (ipInHdrErrors).</p>
<dt><code>in: ader/s</code></p>
<dd> Number of input IP datagrams per second discarded because the IP address in the destination field was not valid to be received by this entity (ipInAddrErrors).</p>
<dt><code>in: unkp/s</code></p>
<dd> Number of inbound packets per second that were discarded because of an unknown or unsupported protocol (ipInUnknownProtos).</p>
<dt><code>in: ratim/s</code></p>
<dd> Number of timeout-situations per second while other fragments were expected for successful reassembly (ipReasmTimeout).</p>
<dt><code>in: rfail/s</code></p>
<dd> Number of failures detected per second by the IP reassembly algorithm (ipReasmFails).</p>
<dt><code>out: dsc/s</code></p>
<dd> Number of output IP datagrams per second for which no problems were encountered to prevent their continued processing but that were discarded, e.g. for lack of buffer space (ipOutDiscards).</p>
<dt><code>out: nrt/s</code></p>
<dd> Number of IP datagrams per second discarded because no route could be found (ipOutNoRoutes).</dl>
<p> The output for the flag <code>-y</code> provides information about the general utilization of the ICMPv4-layer and some information per type of ICMP-message (formal SNMP-names between brackets):</p>
<dl>
<dt><code>intot/s</code></p>
<dd> Number of ICMP messages (any type) received per second at this entity (icmpInMsgs).</p>
<dt><code>outtot/s</code></p>
<dd> Number of ICMP messages (any type) transmitted per second from this entity (icmpOutMsgs).</p>
<dt><code>inecho/s</code></p>
<dd> Number of ICMP Echo (request) messages received per second (icmpInEchos).</p>
<dt><code>inerep/s</code></p>
<dd> Number of ICMP Echo-Reply messages received per second (icmpInEchoReps).</p>
<dt><code>otecho/s</code></p>
<dd> Number of ICMP Echo (request) messages transmitted per second (icmpOutEchos).</p>
<dt><code>oterep/s</code></p>
<dd> Number of ICMP Echo-Reply messages transmitted per second (icmpOutEchoReps).</dl>
<p> The output for the flag <code>-Y</code> provides information about other types of ICMPv4-messages (formal SNMP-names between brackets):</p>
<dl>
<dt><code>ierr/s</code></p>
<dd> Number of ICMP messages received per second but determined to have ICMP-specific errors (icmpInErrors).</p>
<dt><code>isq/s</code></p>
<dd> Number of ICMP Source Quench messages received per second (icmpInSrcQuenchs).</p>
<dt><code>ird/s</code></p>
<dd> Number of ICMP Redirect messages received per second (icmpInRedirects).</p>
<dt><code>idu/s</code></p>
<dd> Number of ICMP Destination Unreachable messages received per second (icmpInDestUnreachs).</p>
<dt><code>ite/s</code></p>
<dd> Number of ICMP Time Exceeded messages received per second (icmpOutTimeExcds).</p>
<dt><code>oerr/s</code></p>
<dd> Number of ICMP messages transmitted per second but determined to have ICMP-specific errors (icmpOutErrors).</p>
<dt><code>osq/s</code></p>
<dd> Number of ICMP Source Quench messages transmitted per second (icmpOutSrcQuenchs).</p>
<dt><code>ord/s</code></p>
<dd> Number of ICMP Redirect messages transmitted per second (icmpOutRedirects).</p>
<dt><code>odu/s</code></p>
<dd> Number of ICMP Destination Unreachable messages transmitted per second (icmpOutDestUnreachs).</p>
<dt><code>ote/s</code></p>
<dd> Number of ICMP Time Exceeded messages transmitted per second (icmpOutTimeExcds).</dl>
<p> The output for the flag <code>-u</code> provides information about the utilization of the UDPv4-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>indgram/s</code></p>
<dd> Number of UDP datagrams per second delivered to UDP users (udpInDatagrams).</p>
<dt><code>outdgram/s</code></p>
<dd> Number of UDP datagrams transmitted per second from this entity (udpOutDatagrams).</p>
<dt><code>inerr/s</code></p>
<dd> Number of received UDP datagrams per second that could not be delivered for reasons other than the lack of an application at the destination port (udpInErrors).</p>
<dt><code>noport/s</code></p>
<dd> Number of received UDP datagrams per second for which there was no application at the destination port (udpNoPorts).</dl>
<p> The output for the flag <code>-z</code> provides information about the utilization of the IPv6-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>inrecv/s</code></p>
<dd> Number of input IPv6-datagrams received from interfaces per second, including those received in error (ipv6IfStatsInReceives).</p>
<dt><code>outreq/s</code></p>
<dd> Number of IPv6-datagrams per second that local higher-layer protocols supplied to IP in requests for transmission (ipv6IfStatsOutRequests). This counter does not include any forwarded datagrams.</p>
<dt><code>inmc/s</code></p>
<dd> Number of multicast packets per second that have been received by the interface (ipv6IfStatsInMcastPkts).</p>
<dt><code>outmc/s</code></p>
<dd> Number of multicast packets per second that have been transmitted to the interface (ipv6IfStatsOutMcastPkts).</p>
<dt><code>indeliv/s</code></p>
<dd> Number of IP datagrams successfully delivered per second to IPv6 user-protocols, including ICMP (ipv6IfStatsInDelivers).</p>
<dt><code>reasmok/s</code></p>
<dd> Number of IPv6 datagrams successfully reassembled per second (ipv6IfStatsReasmOKs).</p>
<dt><code>fragcre/s</code></p>
<dd> Number of IPv6 datagram fragments generated per second at this entity (ipv6IfStatsOutFragCreates).</dl>
<p> The output for the flag <code>-Z</code> provides information about the failures that were detected in the IPv6-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>in: dsc/s</code></p>
<dd> Number of input IPv6 datagrams per second for which no problems were encountered to prevent their continued processing but that were discarded, e.g. for lack of buffer space (ipv6IfStatsInDiscards).</p>
<dt><code>in: hder/s</code></p>
<dd> Number of input datagrams per second discarded due to errors in the IPv6 header (ipv6IfStatsInHdrErrors).</p>
<dt><code>in: ader/s</code></p>
<dd> Number of input datagrams per second discarded because the IPv6 address in the destination field was not valid to be received by this entity (ipv6IfStatsInAddrErrors).</p>
<dt><code>in: unkp/s</code></p>
<dd> Number of locally-addressed datagrams per second that were discarded because of an unknown or unsupported protocol (ipv6IfStatsInUnknownProtos).</p>
<dt><code>in: ratim/s</code></p>
<dd> Number of timeout-situations per second while other IPv6 fragments were expected for successful reassembly (ipv6ReasmTimeout).</p>
<dt><code>in: rfail/s</code></p>
<dd> Number of failures detected per second by the IPv6 reassembly-algorithm (ipv6IfStatsReasmFails).</p>
<dt><code>out: dsc/s</code></p>
<dd> Number of output IPv6 datagrams per second for which no problems were encountered to prevent their continued processing but that were discarded, e.g. for lack of buffer space (ipv6IfStatsOutDiscards).</p>
<dt><code>out: nrt/s</code></p>
<dd> Number of IPv6 datagrams per second discarded because no route could be found (ipv6IfStatsInNoRoutes).</dl>
<p> The output for the flag <code>-k</code> provides information about the general utilization of the ICMPv6-layer and some information per type of ICMP-message (formal SNMP-names between brackets):</p>
<dl>
<dt><code>intot/s</code></p>
<dd> Number of ICMPv6 messages (any type) received per second at the interface (ipv6IfIcmpInMsgs).</p>
<dt><code>outtot/s</code></p>
<dd> Number of ICMPv6 messages (any type) transmitted per second from this entity (ipv6IfIcmpOutMsgs).</p>
<dt><code>inerr/s</code></p>
<dd> Number of ICMPv6 messages received per second that had ICMP-specific errors, such as bad ICMP checksums, bad length, etc (ipv6IfIcmpInErrors).</p>
<dt><code>innsol/s</code></p>
<dd> Number of ICMP Neighbor Solicit messages received per second (ipv6IfIcmpInNeighborSolicits).</p>
<dt><code>innadv/s</code></p>
<dd> Number of ICMP Neighbor Advertisement messages received per second (ipv6IfIcmpInNeighborAdvertisements).</p>
<dt><code>otnsol/s</code></p>
<dd> Number of ICMP Neighbor Solicit messages transmitted per second (ipv6IfIcmpOutNeighborSolicits).</p>
<dt><code>otnadv/s</code></p>
<dd> Number of ICMP Neighbor Advertisement messages transmitted per second (ipv6IfIcmpOutNeighborAdvertisements).</dl>
<p> The output for the flag <code>-K</code> provides information about other types of ICMPv6-messages (formal SNMP-names between brackets):</p>
<dl>
<dt><code>iecho/s</code></p>
<dd> Number of ICMP Echo (request) messages received per second (ipv6IfIcmpInEchos).</p>
<dt><code>ierep/s</code></p>
<dd> Number of ICMP Echo-Reply messages received per second (ipv6IfIcmpInEchoReplies).</p>
<dt><code>oerep/s</code></p>
<dd> Number of ICMP Echo-Reply messages transmitted per second (ipv6IfIcmpOutEchoReplies).</p>
<dt><code>idu/s</code></p>
<dd> Number of ICMP Destination Unreachable messages received per second (ipv6IfIcmpInDestUnreachs).</p>
<dt><code>odu/s</code></p>
<dd> Number of ICMP Destination Unreachable messages transmitted per second (ipv6IfIcmpOutDestUnreachs).</p>
<dt><code>ird/s</code></p>
<dd> Number of ICMP Redirect messages received per second (ipv6IfIcmpInRedirects).</p>
<dt><code>ord/s</code></p>
<dd> Number of ICMP Redirect messages transmitted per second (ipv6IfIcmpOutRedirect).</p>
<dt><code>ite/s</code></p>
<dd> Number of ICMP Time Exceeded messages received per second (ipv6IfIcmpInTimeExcds).</p>
<dt><code>ote/s</code></p>
<dd> Number of ICMP Time Exceeded messages transmitted per second (ipv6IfIcmpOutTimeExcds).</dl>
<p> The output for the flag <code>-U</code> provides information about the utilization of the UDPv6-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>indgram/s</code></p>
<dd> Number of UDPv6 datagrams per second delivered to UDP users (udpInDatagrams),</p>
<dt><code>outdgram/s</code></p>
<dd> Number of UDPv6 datagrams transmitted per second from this entity (udpOutDatagrams),</p>
<dt><code>inerr/s</code></p>
<dd> Number of received UDPv6 datagrams per second that could not be delivered for reasons other than the lack of an application at the destination port (udpInErrors).</p>
<dt><code>noport/s</code></p>
<dd> Number of received UDPv6 datagrams per second for which there was no application at the destination port (udpNoPorts).</dl>
<p> The output for the flag <code>-t</code> provides information about the utilization of the TCP-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>insegs/s</code></p>
<dd> Number of received segments per second, including those received in error (tcpInSegs).</p>
<dt><code>outsegs/s</code></p>
<dd> Number of transmitted segments per second, excluding those containing only retransmitted octets (tcpOutSegs).</p>
<dt><code>actopen/s</code></p>
<dd> Number of active opens per second that have been supported by this entity (tcpActiveOpens).</p>
<dt><code>pasopen/s</code></p>
<dd> Number of passive opens per second that have been supported by this entity (tcpPassiveOpens).</p>
<dt><code>nowopen</code></p>
<dd> Number of connections currently open (snapshot), for which the state is either ESTABLISHED or CLOSE-WAIT (tcpCurrEstab).</dl>
<p> The output for the flag <code>-T</code> provides information about the failures that were detected in the TCP-layer (formal SNMP-names between brackets):</p>
<dl>
<dt><code>inerr/s</code></p>
<dd> Number of received segments per second received in error (tcpInErrs).</p>
<dt><code>retrans/s</code></p>
<dd> Number of retransmitted segments per second (tcpRetransSegs).</p>
<dt><code>attfail/s</code></p>
<dd> Number of failed connection attempts per second that have occurred at this entity (tcpAttemptFails).</p>
<dt><code>estabreset/s</code></p>
<dd> Number of resets per second that have occurred at this entity (tcpEstabResets).</p>
<dt><code>outreset/s</code></p>
<dd> Number of transmitted segments per second containing the RST flag (tcpOutRsts).</dl>
<p> The output for the flag <code>-O</code> provides information about the top-3 of processes with the highest processor consumption:</p>
<dl>
<dt><code>pid</code></p>
<dd> Process-id (if zero, the process has exited while the pid could not be determined).</p>
<dt><code>command</code></p>
<dd> The name of the process.</p>
<dt><code>cpu%</code></p>
<dd> The percentage of cpu-capacity being consumed. This value can exceed 100% for a multithreaded process running on a multiprocessor machine.</dl>
<p> The output for the flag <code>-G</code> provides information about the top-3 of processes with the highest memory consumption:</p>
<dl>
<dt><code>pid</code></p>
<dd> Process-id (if zero, the process has exited while the pid could not be determined).</p>
<dt><code>command</code></p>
<dd> The name of the process.</p>
<dt><code>mem%</code></p>
<dd> The percentage of resident memory-utilization by this process.</dl>
<p> The output for the flag <code>-D</code> provides information about the top-3 of processes that issue the most read and write accesses to disk:</p>
<dl>
<dt><code>pid</code></p>
<dd> Process-id (if zero, the process has exited while the pid could not be determined).</p>
<dt><code>command</code></p>
<dd> The name of the process.</p>
<dt><code>dsk%</code></p>
<dd> The percentage of read and write accesses related to the total number of read and write accesses issued on disk by all processes, so a high percentage does not imply a high disk load on system level.</dl>
<p> The output for the flag <code>-N</code> provides information about the top-3 of processes that issue the most socket transfers for IPv4/IPv6:</p>
<dl>
<dt><code>pid</code></p>
<dd> Process-id (if zero, the process has exited while the pid could not be determined).</p>
<dt><code>command</code></p>
<dd> The name of the process.</p>
<dt><code>net%</code></p>
<dd> The percentage of socket transfers related to the total number of transfers issued by all processes, so a high percentage does not imply a high network load on system level.</dl>
<h2>EXAMPLES</h2>
<p> To see today&#8217;s cpu-activity so far (supposed that <code>atop</code> is logging in the background): </p>
<dl>
<dt><code>&nbsp;<wbr> atopsar</code></p>
<dd></dl>
<p> To see the memory occupation for June 5, 2012 between 10:00 and 12:30 (supposed that <code>atop</code> has been logging daily in the background): </p>
<dl>
<dt><code>&nbsp;<wbr> atopsar -m -r /var/log/atop_20120605 -b 10:00 -e 12:30</code></p>
<dd>
 &nbsp;<wbr> </p>
<p>&nbsp;<wbr>or</p>
<dt><code>&nbsp;<wbr> atopsar -m -r 20120605 -b 10:00 -e 12:30</code></p>
<dd>
 &nbsp;<wbr> </p>
<p>&nbsp;<wbr>or, suppose it is June 8, 2012 at this moment</p>
<dt><code>&nbsp;<wbr> atopsar -m -r yyy -b 10:00 -e 12:30</code></p>
<dd></dl>
<p> Write a logfile with <code>atop</code> to record the system behaviour for 30 minutes (30 samples of one minute) and produce all available reports afterwards: </p>
<dl>
<dt><code>&nbsp;<wbr> atop -w /tmp/atoplog 60 30</code></p>
<dd>
<dt><code>&nbsp;<wbr> atopsar -A -r /tmp/atoplog</code></p>
<dd></dl>
<p> To watch TCP activity evolve for ten minutes (10 samples with sixty seconds interval): </p>
<dl>
<dt><code>&nbsp;<wbr> atopsar -t 60 10</code></p>
<dd></dl>
<p> To watch the header-lines (&#8216;_&#8217; as last character) of all reports with only the detail-lines showing critical resource consumption (marker &#8216;*&#8217; or &#8216;+&#8217; as last character): </p>
<dl>
<dt><code>&nbsp;<wbr> atopsar -AM | grep &#8216;[_*+]$&#8217;</code></p>
<dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/atoprc</code></p>
<dd> Configuration file containing system-wide default values (mainly flags). See related man-page.</dl>
<dl>
<dt><code>~/.atoprc</code></p>
<dd> Configuration file containing personal default values (mainly flags). See related man-page.</dl>
<dl>
<dt><code>/var/log/atop/atop_</code><i>YYYYMMDD</i></p>
<dd> Daily data file, where <i>YYYYMMDD</i> are digits representing the date.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-atop/">atop</a>(1),</code> <code><a href="/docs/linux/man/5-atoprc/">atoprc</a>(5),</code> <code><a href="/docs/linux/man/8-atopacctd/">atopacctd</a>(8),</code> <code><a href="/docs/linux/man/4-netatop/">netatop</a>(4),</code> <code><a href="/docs/linux/man/8-netatopd/">netatopd</a>(8)</code><br />
 <code><a rel="nofollow" href="http://www.atoptool.nl">http://www.atoptool.nl</a></code></p>
<h2>AUTHOR</h2>
<p> Gerlof Langeveld (gerlof.langeveld [at] atoptool.nl) </p>
<h2>Index</h2>
