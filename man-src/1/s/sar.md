---
title: "sar(1)"
name: "sar"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sar/"
description: "sar – Collect, report, or save system activity information."
---

<h2 class="name">NAME</h2>
<p> sar &#8211; Collect, report, or save system activity information.</p>
<h2>SYNOPSIS</h2>
<p> <code>sar [ -A ] [ -B ] [ -b ] [ -C ] [ -D ] [ -d ] [ -F [ MOUNT ] ] [ -H ] [ -h ] [ -p ]</code> <code>[ -r [ ALL ] ] [ -S ] [ -t ] [ -u [ ALL ] ] [ -V ] [ -v ] [ -W ] [ -w ] [ -y ] [ -z ]</code> <code>[ &#8211;dec={ 0 | 1 | 2 } ]</code> <code>[ &#8211;dev=</code><i>dev_list </i><code>] [ &#8211;fs=</code><i>fs_list </i><code>] [ &#8211;help ] [ &#8211;human ] [ &#8211;iface=</code><i>iface_list</i> <code>] [ &#8211;pretty ] [ &#8211;sadc ] [ -I { </code><i>int_list </i><code>| SUM | ALL } ] [ -P { </code><i>cpu_list</i> <code>| ALL } ] [ -m {</code> <i>keyword</i><code>[,&#8230;] | ALL } ] [ -n { </code><i>keyword</i><code>[,&#8230;] | ALL } ] [ -q [ </code><i>keyword</i><code>[,&#8230;] | ALL ] ]</code> <code>[ -j { SID | ID | LABEL | PATH | UUID | &#8230; } ]</code> <code>[ -f [ </code><i>filename </i><code>] | -o [ </code><i>filename </i><code>] | -[0-9]+ ]</code> <code>[ -i </code><i>interval </i><code>] [ -s [ </code><i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>]</code> <code>] ] [ -e [ </code><i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>] ] ] [ </code><i>interval </i><code>[ </code><i>count </i><code>] ]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>sar</code> command writes to standard output the contents of selected cumulative activity counters in the operating system. The accounting system, based on the values in the <i>count </i>and <i>interval</i> parameters, writes information the specified number of times spaced at the specified intervals in seconds. If the <i>interval </i>parameter is set to zero, the <code>sar</code> command displays the average statistics for the time since the system was started. If the <i>interval </i>parameter is specified without the <i>count</i> parameter, then reports are generated continuously. The collected data can also be saved in the file specified by the <code>-o </code><i>filename</i> flag, in addition to being displayed onto the screen. If <i>filename </i>is omitted, <code>sar</code> uses the standard system activity daily data file (see below). By default all the data available from the kernel are saved in the data file. </p>
<p> The <code>sar</code> command extracts and writes to standard output records previously saved in a file. This file can be either the one specified by the <code>-f</code> flag or, by default, the standard system activity daily data file. It is also possible to enter <code>-1</code>, <code>-2 </code>etc. as an argument to <code>sar</code> to display data of that days ago. For example, <code>-1 </code>will point at the standard system activity file of yesterday. </p>
<p> Standard system activity daily data files are named <i>saDD </i>or <i>saYYYYMMDD</i>, where <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day. They are the default files used by <code>sar</code> only when no filename has been explicitly specified. When used to write data to files (with its option <code>-o</code>), <code>sar</code> will use <i>saYYYYMMDD</i> if option <code>-D</code> has also been specified, else it will use <i>saDD</i>. When used to display the records previously saved in a file, <code>sar</code> will look for the most recent of <i>saDD </i>and <i>saYYYYMMDD</i>, and use it. </p>
<p> Standard system activity daily data files are located in the <i>/var/log/sysstat</i> directory by default. Yet it is possible to specify an alternate location for them: If a directory (instead of a plain file) is used with options <code>-f </code>or <code>-o</code> then it will be considered as the directory containing the data files. </p>
<p> Without the <code>-P </code>flag, the <code>sar</code> command reports system-wide (global among all processors) statistics, which are calculated as averages for values expressed as percentages, and as sums otherwise. If the <code>-P </code>flag is given, the <code>sar</code> command reports activity which relates to the specified processor or processors. If <code>-P ALL </code>is given, the <code>sar</code> command reports statistics for each individual processor and global statistics among all processors. Offline processors are not displayed. </p>
<p> You can select information about specific system activities using flags. Not specifying any flags selects only CPU activity. Specifying the <code>-A</code> flag selects all possible activities. </p>
<p> The default version of the <code>sar</code> command (CPU utilization report) might be one of the first facilities the user runs to begin system activity investigation, because it monitors major system resources. If CPU utilization is near 100 percent (user + nice + system), the workload sampled is CPU-bound. </p>
<p> If multiple samples and multiple reports are desired, it is convenient to specify an output file for the <code>sar </code>command. Run the <code>sar</code> command as a background process. The syntax for this is: </p>
<p> <code>sar -o </code><i>datafile interval count </i><code>&gt;/dev/null 2&gt;&amp;1 &amp;</code> </p>
<p> All data are captured in binary form and saved to a file (<i>datafile</i>). The data can then be selectively displayed with the <code>sar </code>command using the <code>-f </code>option. Set the <i>interval </i>and <i>count </i>parameters to select <i>count </i>records at <i>interval</i> second intervals. If the <i>count</i> parameter is not set, all the records saved in the file will be selected. Collection of data in this manner is useful to characterize system usage over a period of time and determine peak usage hours. </p>
<p> Note: The <code>sar</code> command only reports on local activities. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> This is equivalent to specifying <code>-bBdFHSvwWy -I SUM -m ALL -n ALL -q ALL -r ALL -u ALL</code>. This option also implies specifying <code>-I ALL -P ALL</code> unless these options are explicitly set on the command line.</p>
<dt><code>-B</code></p>
<dd> Report paging statistics. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>pgpgin/s</p>
<dd> Total number of kilobytes the system paged in from disk per second.</p>
<dt>pgpgout/s</p>
<dd> Total number of kilobytes the system paged out to disk per second.</p>
<dt>fault/s</p>
<dd> Number of page faults (major + minor) made by the system per second. This is not a count of page faults that generate I/O, because some page faults can be resolved without I/O.</p>
<dt>majflt/s</p>
<dd> Number of major faults the system has made per second, those which have required loading a memory page from disk.</p>
<dt>pgfree/s</p>
<dd> Number of pages placed on the free list by the system per second.</p>
<dt>pgscank/s</p>
<dd> Number of pages scanned by the kswapd daemon per second.</p>
<dt>pgscand/s</p>
<dd> Number of pages scanned directly per second.</p>
<dt>pgsteal/s</p>
<dd> Number of pages the system has reclaimed from cache (pagecache and swapcache) per second to satisfy its memory demands.</p>
<dt>%vmeff</p>
<dd> Calculated as pgsteal / pgscan, this is a metric of the efficiency of page reclaim. If it is near 100% then almost every page coming off the tail of the inactive list is being reaped. If it gets too low (e.g. less than 30%) then the virtual memory is having some difficulty. This field is displayed as zero if no pages have been scanned during the interval of time.</dl>
</dl>
<dt><code>-b</code></p>
<dd> Report I/O and transfer rate statistics. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>tps</p>
<dd> Total number of transfers per second that were issued to physical devices. A transfer is an I/O request to a physical device. Multiple logical requests can be combined into a single I/O request to the device. A transfer is of indeterminate size.</p>
<dt>rtps</p>
<dd> Total number of read requests per second issued to physical devices.</p>
<dt>wtps</p>
<dd> Total number of write requests per second issued to physical devices.</p>
<dt>dtps</p>
<dd> Total number of discard requests per second issued to physical devices.</p>
<dt>bread/s</p>
<dd> Total amount of data read from the devices in blocks per second. Blocks are equivalent to sectors and therefore have a size of 512 bytes.</p>
<dt>bwrtn/s</p>
<dd> Total amount of data written to devices in blocks per second.</p>
<dt>bdscd/s</p>
<dd> Total amount of data discarded for devices in blocks per second.</dl>
</dl>
<dt><code>-C</code></p>
<dd> When reading data from a file, tell <code>sar </code>to display comments that have been inserted by <code>sadc</code>.</p>
<dt><code>-D</code></p>
<dd> Use <i>saYYYYMMDD </i>instead of <i>saDD</i> as the standard system activity daily data file name. This option works only when used in conjunction with option <code>-o </code>to save data to file.</p>
<dt><code>-d</code></p>
<dd> Report activity for each block device. When data are displayed, the device name is displayed as it (should) appear in <i>/dev</i>. <code>sar </code>uses data in <i>/sys </i>to determine the device name based on its major and minor numbers. If this name resolution fails, <code>sar </code>will use name mapping controlled by <i>/etc/sysstat/sysstat.ioconf </i>file. Persistent device names can also be printed if option <code>-j</code> is used (see below). Statistics for all devices are displayed unless a restricted list is specified using option <code>&#8211;dev=</code> (see corresponding option entry). Note that disk activity depends on <code>sadc</code>&#8216;s options <code>-S DISK </code>and <code>-S XDISK</code> to be collected. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>tps</p>
<dd> Total number of transfers per second that were issued to physical devices. A transfer is an I/O request to a physical device. Multiple logical requests can be combined into a single I/O request to the device. A transfer is of indeterminate size.</p>
<dt>rkB/s</p>
<dd> Number of kilobytes read from the device per second.</p>
<dt>wkB/s</p>
<dd> Number of kilobytes written to the device per second.</p>
<dt>dkB/s</p>
<dd> Number of kilobytes discarded for the device per second.</p>
<dt>areq-sz</p>
<dd> The average size (in kilobytes) of the I/O requests that were issued to the device.<br />
 Note: In previous versions, this field was known as avgrq-sz and was expressed in sectors.</p>
<dt>aqu-sz</p>
<dd> The average queue length of the requests that were issued to the device.<br />
 Note: In previous versions, this field was known as avgqu-sz.</p>
<dt>await</p>
<dd> The average time (in milliseconds) for I/O requests issued to the device to be served. This includes the time spent by the requests in queue and the time spent servicing them.</p>
<dt>%util</p>
<dd> Percentage of elapsed time during which I/O requests were issued to the device (bandwidth utilization for the device). Device saturation occurs when this value is close to 100% for devices serving requests serially. But for devices serving requests in parallel, such as RAID arrays and modern SSDs, this number does not reflect their performance limits.</dl>
</dl>
<dt><code>&#8211;dec={ 0 | 1 | 2 }</code></p>
<dd> Specify the number of decimal places to use (0 to 2, default value is 2).</p>
<dt><code>&#8211;dev=</code><i>dev_list</i></p>
<dd> Specify the block devices for which statistics are to be displayed by <code>sar</code>. <i>dev_list </i>is a list of comma-separated device names.</p>
<dt><code>-e [ </code><i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>] ]</code></p>
<dd> Set the ending time of the report. The default ending time is 18:00:00. Hours must be given in 24-hour format. This option can be used when data are read from or written to a file (options <code>-f </code>or <code>-o</code>).</p>
<dt><code>-F [ MOUNT ]</code></p>
<dd> Display statistics for currently mounted filesystems. Pseudo-filesystems are ignored. At the end of the report, <code>sar</code> will display a summary of all those filesystems. Use of the <code>MOUNT</code> parameter keyword indicates that mountpoint will be reported instead of filesystem device. Statistics for all filesystems are displayed unless a restricted list is specified using option <code>&#8211;fs=</code> (see corresponding option entry). Note that filesystems statistics depend on <code>sadc</code>&#8216;s option <code>-S XDISK </code> to be collected. </p>
<p> The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>MBfsfree</p>
<dd> Total amount of free space in megabytes (including space available only to privileged user).</p>
<dt>MBfsused</p>
<dd> Total amount of space used in megabytes.</p>
<dt>%fsused</p>
<dd> Percentage of filesystem space used, as seen by a privileged user.</p>
<dt>%ufsused</p>
<dd> Percentage of filesystem space used, as seen by an unprivileged user.</p>
<dt>Ifree</p>
<dd> Total number of free file nodes in filesystem.</p>
<dt>Iused</p>
<dd> Total number of file nodes used in filesystem.</p>
<dt>%Iused</p>
<dd> Percentage of file nodes used in filesystem.</dl>
</dl>
<dt><code>-f [ </code><i>filename </i><code>]</code></p>
<dd> Extract records from <i>filename </i>(created by the <code>-o </code><i>filename</i> flag). The default value of the <i>filename</i> parameter is the current standard system activity daily data file. If <i>filename</i> is a directory instead of a plain file then it is considered as the directory where the standard system activity daily data files are located. Option <code>-f </code>is exclusive of option <code>-o</code>.</p>
<dt><code>&#8211;fs=</code><i>fs_list</i></p>
<dd> Specify the filesystems for which statistics are to be displayed by <code>sar</code>. <i>fs_list</i> is a list of comma-separated filesystem names or mountpoints.</p>
<dt><code>-H</code></p>
<dd> Report hugepages utilization statistics. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>kbhugfree</p>
<dd> Amount of hugepages memory in kilobytes that is not yet allocated.</p>
<dt>kbhugused</p>
<dd> Amount of hugepages memory in kilobytes that has been allocated.</p>
<dt>%hugused</p>
<dd> Percentage of total hugepages memory that has been allocated.</p>
<dt>kbhugrsvd</p>
<dd> Amount of reserved hugepages memory in kilobytes.</p>
<dt>kbhugsurp</p>
<dd> Amount of surplus hugepages memory in kilobytes.</dl>
</dl>
<dt><code>-h</code></p>
<dd> This option is equivalent to specifying <code>&#8211;pretty &#8211;human</code>.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a short help message then exit.</p>
<dt><code>&#8211;human</code></p>
<dd> Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g. kilobytes, sectors&#8230;) associated with the metrics.</p>
<dt><code>-I { </code><i>int_list </i><code>| SUM | ALL }</code></p>
<dd> Report statistics for interrupts. <i>int_list</i> is a list of comma-separated values or range of values (e.g., <code>0-16,35,400-</code>). The <code>SUM</code> keyword indicates that the total number of interrupts received per second is to be displayed. The <code>ALL</code> keyword indicates that statistics from all interrupts, including potential APIC interrupt sources, are to be reported. Note that interrupt statistics depend on <code>sadc</code>&#8216;s option <code>-S INT</code> to be collected.</p>
<dt><code>-i </code><i>interval</i></p>
<dd> Select data records at seconds as close as possible to the number specified by the <i>interval </i>parameter.</p>
<dt><code>&#8211;iface=</code><i>iface_list</i></p>
<dd> Specify the network interfaces for which statistics are to be displayed by <code>sar</code>. <i>iface_list</i> is a list of comma-separated interface names.</p>
<dt><code>-j { SID | ID | LABEL | PATH | UUID | &#8230; }</code></p>
<dd> Display persistent device names. Use this option in conjunction with option <code>-d</code>. Keywords <code>ID</code>, <code>LABEL</code>, etc. specify the type of the persistent name. These keywords are not limited, only prerequisite is that directory with required persistent names is present in <i>/dev/disk</i>. Keyword <code>SID</code> tries to get a stable identifier to use as the device name. A stable identifier won&#8217;t change across reboots for the same physical device. If it exists, this identifier is normally the WWN (World Wide Name) of the device, as read from the <i>/dev/disk/by-id </i>directory.</p>
<dt><code>-m { </code><i>keyword</i><code>[,&#8230;] | ALL }</code></p>
<dd> Report power management statistics. Note that these statistics depend on <code>sadc</code>&#8216;s option <code>-S POWER </code>to be collected. </p>
<p> Possible keywords are <code>CPU</code>, <code>FAN</code>, <code>FREQ</code>, <code>IN</code>, <code>TEMP </code>and <code>USB</code>. </p>
<p> With the <code>CPU</code> keyword, statistics about CPU are reported. The following value is displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>MHz</p>
<dd> Instantaneous CPU clock frequency in MHz.</dl>
</dl>
<dt>
<dd> With the <code>FAN</code> keyword, statistics about fans speed are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>rpm</p>
<dd> Fan speed expressed in revolutions per minute.</p>
<dt>drpm</p>
<dd> This field is calculated as the difference between current fan speed (rpm) and its low limit (fan_min).</p>
<dt>DEVICE</p>
<dd> Sensor device name.</dl>
</dl>
<dt>
<dd> With the <code>FREQ</code> keyword, statistics about CPU clock frequency are reported. The following value is displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>wghMHz</p>
<dd> Weighted average CPU clock frequency in MHz. Note that the cpufreq-stats driver must be compiled in the kernel for this option to work.</dl>
</dl>
<dt>
<dd> With the <code>IN</code> keyword, statistics about voltage inputs are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>inV</p>
<dd> Voltage input expressed in Volts.</p>
<dt>%in</p>
<dd> Relative input value. A value of 100% means that voltage input has reached its high limit (in_max) whereas a value of 0% means that it has reached its low limit (in_min).</p>
<dt>DEVICE</p>
<dd> Sensor device name.</dl>
</dl>
<dt>
<dd> With the <code>TEMP</code> keyword, statistics about devices temperature are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>degC</p>
<dd> Device temperature expressed in degrees Celsius.</p>
<dt>%temp</p>
<dd> Relative device temperature. A value of 100% means that temperature has reached its high limit (temp_max).</p>
<dt>DEVICE</p>
<dd> Sensor device name.</dl>
</dl>
<dt>
<dd> With the <code>USB </code>keyword, the <code>sar</code> command takes a snapshot of all the USB devices currently plugged into the system. At the end of the report, <code>sar</code> will display a summary of all those USB devices. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>BUS</p>
<dd> Root hub number of the USB device.</p>
<dt>idvendor</p>
<dd> Vendor ID number (assigned by USB organization).</p>
<dt>idprod</p>
<dd> Product ID number (assigned by Manufacturer).</p>
<dt>maxpower</p>
<dd> Maximum power consumption of the device (expressed in mA).</p>
<dt>manufact</p>
<dd> Manufacturer name.</p>
<dt>product</p>
<dd> Product name.</dl>
</dl>
<dt>
<dd> The <code>ALL</code> keyword is equivalent to specifying all the keywords above and therefore all the power management statistics are reported.</p>
<dt><code>-n { </code><i>keyword</i><code>[,&#8230;] | ALL }</code></p>
<dd> Report network statistics. </p>
<p> Possible keywords are <code>DEV</code>, <code>EDEV</code>, <code>FC</code>, <code>ICMP</code>, <code>EICMP</code>, <code>ICMP6</code>, <code>EICMP6</code>, <code>IP</code>, <code>EIP</code>, <code>IP6</code>, <code>EIP6</code>, <code>NFS</code>, <code>NFSD</code>, <code>SOCK</code>, <code>SOCK6</code>, <code>SOFT</code>, <code>TCP</code>, <code>ETCP</code>, <code>UDP </code>and <code>UDP6</code>. </p>
<p> With the <code>DEV</code> keyword, statistics from the network devices are reported. Statistics for all network interfaces are displayed unless a restricted list is specified using option <code>&#8211;iface=</code> (see corresponding option entry). The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>IFACE</p>
<dd> Name of the network interface for which statistics are reported.</p>
<dt>rxpck/s</p>
<dd> Total number of packets received per second.</p>
<dt>txpck/s</p>
<dd> Total number of packets transmitted per second.</p>
<dt>rxkB/s</p>
<dd> Total number of kilobytes received per second.</p>
<dt>txkB/s</p>
<dd> Total number of kilobytes transmitted per second.</p>
<dt>rxcmp/s</p>
<dd> Number of compressed packets received per second (for cslip etc.).</p>
<dt>txcmp/s</p>
<dd> Number of compressed packets transmitted per second.</p>
<dt>rxmcst/s</p>
<dd> Number of multicast packets received per second.</p>
<dt>%ifutil</p>
<dd> Utilization percentage of the network interface. For half-duplex interfaces, utilization is calculated using the sum of rxkB/s and txkB/s as a percentage of the interface speed. For full-duplex, this is the greater of rxkB/S or txkB/s.</dl>
</dl>
<dt>
<dd> With the <code>EDEV</code> keyword, statistics on failures (errors) from the network devices are reported. Statistics for all network interfaces are displayed unless a restricted list is specified using option <code>&#8211;iface=</code> (see corresponding option entry). The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>IFACE</p>
<dd> Name of the network interface for which statistics are reported.</p>
<dt>rxerr/s</p>
<dd> Total number of bad packets received per second.</p>
<dt>txerr/s</p>
<dd> Total number of errors that happened per second while transmitting packets.</p>
<dt>coll/s</p>
<dd> Number of collisions that happened per second while transmitting packets.</p>
<dt>rxdrop/s</p>
<dd> Number of received packets dropped per second because of a lack of space in linux buffers.</p>
<dt>txdrop/s</p>
<dd> Number of transmitted packets dropped per second because of a lack of space in linux buffers.</p>
<dt>txcarr/s</p>
<dd> Number of carrier-errors that happened per second while transmitting packets.</p>
<dt>rxfram/s</p>
<dd> Number of frame alignment errors that happened per second on received packets.</p>
<dt>rxfifo/s</p>
<dd> Number of FIFO overrun errors that happened per second on received packets.</p>
<dt>txfifo/s</p>
<dd> Number of FIFO overrun errors that happened per second on transmitted packets.</dl>
</dl>
<dt>
<dd> With the <code>FC</code> keyword, statistics about fibre channel traffic are reported. Note that fibre channel statistics depend on <code>sadc</code>&#8216;s option <code>-S DISK</code> to be collected. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>FCHOST</p>
<dd> Name of the fibre channel host bus adapter (HBA) interface for which statistics are reported.</p>
<dt>fch_rxf/s</p>
<dd> The total number of frames received per second.</p>
<dt>fch_txf/s</p>
<dd> The total number of frames transmitted per second.</p>
<dt>fch_rxw/s</p>
<dd> The total number of transmission words received per second.</p>
<dt>fch_txw/s</p>
<dd> The total number of transmission words transmitted per second.</dl>
</dl>
<dt>
<dd> With the <code>ICMP</code> keyword, statistics about ICMPv4 network traffic are reported. Note that ICMPv4 statistics depend on <code>sadc</code>&#8216;s option <code>-S SNMP</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>imsg/s</p>
<dd> The total number of ICMP messages which the entity received per second [icmpInMsgs]. Note that this counter includes all those counted by ierr/s.</p>
<dt>omsg/s</p>
<dd> The total number of ICMP messages which this entity attempted to send per second [icmpOutMsgs]. Note that this counter includes all those counted by oerr/s.</p>
<dt>iech/s</p>
<dd> The number of ICMP Echo (request) messages received per second [icmpInEchos].</p>
<dt>iechr/s</p>
<dd> The number of ICMP Echo Reply messages received per second [icmpInEchoReps].</p>
<dt>oech/s</p>
<dd> The number of ICMP Echo (request) messages sent per second [icmpOutEchos].</p>
<dt>oechr/s</p>
<dd> The number of ICMP Echo Reply messages sent per second [icmpOutEchoReps].</p>
<dt>itm/s</p>
<dd> The number of ICMP Timestamp (request) messages received per second [icmpInTimestamps].</p>
<dt>itmr/s</p>
<dd> The number of ICMP Timestamp Reply messages received per second [icmpInTimestampReps].</p>
<dt>otm/s</p>
<dd> The number of ICMP Timestamp (request) messages sent per second [icmpOutTimestamps].</p>
<dt>otmr/s</p>
<dd> The number of ICMP Timestamp Reply messages sent per second [icmpOutTimestampReps].</p>
<dt>iadrmk/s</p>
<dd> The number of ICMP Address Mask Request messages received per second [icmpInAddrMasks].</p>
<dt>iadrmkr/s</p>
<dd> The number of ICMP Address Mask Reply messages received per second [icmpInAddrMaskReps].</p>
<dt>oadrmk/s</p>
<dd> The number of ICMP Address Mask Request messages sent per second [icmpOutAddrMasks].</p>
<dt>oadrmkr/s</p>
<dd> The number of ICMP Address Mask Reply messages sent per second [icmpOutAddrMaskReps].</dl>
</dl>
<dt>
<dd> With the <code>EICMP</code> keyword, statistics about ICMPv4 error messages are reported. Note that ICMPv4 statistics depend on <code>sadc</code>&#8216;s option <code>-S SNMP</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>ierr/s</p>
<dd> The number of ICMP messages per second which the entity received but determined as having ICMP-specific errors (bad ICMP checksums, bad length, etc.) [icmpInErrors].</p>
<dt>oerr/s</p>
<dd> The number of ICMP messages per second which this entity did not send due to problems discovered within ICMP such as a lack of buffers [icmpOutErrors].</p>
<dt>idstunr/s</p>
<dd> The number of ICMP Destination Unreachable messages received per second [icmpInDestUnreachs].</p>
<dt>odstunr/s</p>
<dd> The number of ICMP Destination Unreachable messages sent per second [icmpOutDestUnreachs].</p>
<dt>itmex/s</p>
<dd> The number of ICMP Time Exceeded messages received per second [icmpInTimeExcds].</p>
<dt>otmex/s</p>
<dd> The number of ICMP Time Exceeded messages sent per second [icmpOutTimeExcds].</p>
<dt>iparmpb/s</p>
<dd> The number of ICMP Parameter Problem messages received per second [icmpInParmProbs].</p>
<dt>oparmpb/s</p>
<dd> The number of ICMP Parameter Problem messages sent per second [icmpOutParmProbs].</p>
<dt>isrcq/s</p>
<dd> The number of ICMP Source Quench messages received per second [icmpInSrcQuenchs].</p>
<dt>osrcq/s</p>
<dd> The number of ICMP Source Quench messages sent per second [icmpOutSrcQuenchs].</p>
<dt>iredir/s</p>
<dd> The number of ICMP Redirect messages received per second [icmpInRedirects].</p>
<dt>oredir/s</p>
<dd> The number of ICMP Redirect messages sent per second [icmpOutRedirects].</dl>
</dl>
<dt>
<dd> With the <code>ICMP6</code> keyword, statistics about ICMPv6 network traffic are reported. Note that ICMPv6 statistics depend on <code>sadc</code>&#8216;s option <code>-S IPV6</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>imsg6/s</p>
<dd> The total number of ICMP messages received by the interface per second which includes all those counted by ierr6/s [ipv6IfIcmpInMsgs].</p>
<dt>omsg6/s</p>
<dd> The total number of ICMP messages which this interface attempted to send per second [ipv6IfIcmpOutMsgs].</p>
<dt>iech6/s</p>
<dd> The number of ICMP Echo (request) messages received by the interface per second [ipv6IfIcmpInEchos].</p>
<dt>iechr6/s</p>
<dd> The number of ICMP Echo Reply messages received by the interface per second [ipv6IfIcmpInEchoReplies].</p>
<dt>oechr6/s</p>
<dd> The number of ICMP Echo Reply messages sent by the interface per second [ipv6IfIcmpOutEchoReplies].</p>
<dt>igmbq6/s</p>
<dd> The number of ICMPv6 Group Membership Query messages received by the interface per second [ipv6IfIcmpInGroupMembQueries].</p>
<dt>igmbr6/s</p>
<dd> The number of ICMPv6 Group Membership Response messages received by the interface per second [ipv6IfIcmpInGroupMembResponses].</p>
<dt>ogmbr6/s</p>
<dd> The number of ICMPv6 Group Membership Response messages sent per second [ipv6IfIcmpOutGroupMembResponses].</p>
<dt>igmbrd6/s</p>
<dd> The number of ICMPv6 Group Membership Reduction messages received by the interface per second [ipv6IfIcmpInGroupMembReductions].</p>
<dt>ogmbrd6/s</p>
<dd> The number of ICMPv6 Group Membership Reduction messages sent per second [ipv6IfIcmpOutGroupMembReductions].</p>
<dt>irtsol6/s</p>
<dd> The number of ICMP Router Solicit messages received by the interface per second [ipv6IfIcmpInRouterSolicits].</p>
<dt>ortsol6/s</p>
<dd> The number of ICMP Router Solicitation messages sent by the interface per second [ipv6IfIcmpOutRouterSolicits].</p>
<dt>irtad6/s</p>
<dd> The number of ICMP Router Advertisement messages received by the interface per second [ipv6IfIcmpInRouterAdvertisements].</p>
<dt>inbsol6/s</p>
<dd> The number of ICMP Neighbor Solicit messages received by the interface per second [ipv6IfIcmpInNeighborSolicits].</p>
<dt>onbsol6/s</p>
<dd> The number of ICMP Neighbor Solicitation messages sent by the interface per second [ipv6IfIcmpOutNeighborSolicits].</p>
<dt>inbad6/s</p>
<dd> The number of ICMP Neighbor Advertisement messages received by the interface per second [ipv6IfIcmpInNeighborAdvertisements].</p>
<dt>onbad6/s</p>
<dd> The number of ICMP Neighbor Advertisement messages sent by the interface per second [ipv6IfIcmpOutNeighborAdvertisements].</dl>
</dl>
<dt>
<dd> With the <code>EICMP6</code> keyword, statistics about ICMPv6 error messages are reported. Note that ICMPv6 statistics depend on <code>sadc</code>&#8216;s option <code>-S IPV6</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>ierr6/s</p>
<dd> The number of ICMP messages per second which the interface received but determined as having ICMP-specific errors (bad ICMP checksums, bad length, etc.) [ipv6IfIcmpInErrors]</p>
<dt>idtunr6/s</p>
<dd> The number of ICMP Destination Unreachable messages received by the interface per second [ipv6IfIcmpInDestUnreachs].</p>
<dt>odtunr6/s</p>
<dd> The number of ICMP Destination Unreachable messages sent by the interface per second [ipv6IfIcmpOutDestUnreachs].</p>
<dt>itmex6/s</p>
<dd> The number of ICMP Time Exceeded messages received by the interface per second [ipv6IfIcmpInTimeExcds].</p>
<dt>otmex6/s</p>
<dd> The number of ICMP Time Exceeded messages sent by the interface per second [ipv6IfIcmpOutTimeExcds].</p>
<dt>iprmpb6/s</p>
<dd> The number of ICMP Parameter Problem messages received by the interface per second [ipv6IfIcmpInParmProblems].</p>
<dt>oprmpb6/s</p>
<dd> The number of ICMP Parameter Problem messages sent by the interface per second [ipv6IfIcmpOutParmProblems].</p>
<dt>iredir6/s</p>
<dd> The number of Redirect messages received by the interface per second [ipv6IfIcmpInRedirects].</p>
<dt>oredir6/s</p>
<dd> The number of Redirect messages sent by the interface by second [ipv6IfIcmpOutRedirects].</p>
<dt>ipck2b6/s</p>
<dd> The number of ICMP Packet Too Big messages received by the interface per second [ipv6IfIcmpInPktTooBigs].</p>
<dt>opck2b6/s</p>
<dd> The number of ICMP Packet Too Big messages sent by the interface per second [ipv6IfIcmpOutPktTooBigs].</dl>
</dl>
<dt>
<dd> With the <code>IP</code> keyword, statistics about IPv4 network traffic are reported. Note that IPv4 statistics depend on <code>sadc</code>&#8216;s option <code>-S SNMP</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>irec/s</p>
<dd> The total number of input datagrams received from interfaces per second, including those received in error [ipInReceives].</p>
<dt>fwddgm/s</p>
<dd> The number of input datagrams per second, for which this entity was not their final IP destination, as a result of which an attempt was made to find a route to forward them to that final destination [ipForwDatagrams].</p>
<dt>idel/s</p>
<dd> The total number of input datagrams successfully delivered per second to IP user-protocols (including ICMP) [ipInDelivers].</p>
<dt>orq/s</p>
<dd> The total number of IP datagrams which local IP user-protocols (including ICMP) supplied per second to IP in requests for transmission [ipOutRequests]. Note that this counter does not include any datagrams counted in fwddgm/s.</p>
<dt>asmrq/s</p>
<dd> The number of IP fragments received per second which needed to be reassembled at this entity [ipReasmReqds].</p>
<dt>asmok/s</p>
<dd> The number of IP datagrams successfully re-assembled per second [ipReasmOKs].</p>
<dt>fragok/s</p>
<dd> The number of IP datagrams that have been successfully fragmented at this entity per second [ipFragOKs].</p>
<dt>fragcrt/s</p>
<dd> The number of IP datagram fragments that have been generated per second as a result of fragmentation at this entity [ipFragCreates].</dl>
</dl>
<dt>
<dd> With the <code>EIP</code> keyword, statistics about IPv4 network errors are reported. Note that IPv4 statistics depend on <code>sadc</code>&#8216;s option <code>-S SNMP</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>ihdrerr/s</p>
<dd> The number of input datagrams discarded per second due to errors in their IP headers, including bad checksums, version number mismatch, other format errors, time-to-live exceeded, errors discovered in processing their IP options, etc. [ipInHdrErrors]</p>
<dt>iadrerr/s</p>
<dd> The number of input datagrams discarded per second because the IP address in their IP header&#8217;s destination field was not a valid address to be received at this entity. This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E). For entities which are not IP routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address [ipInAddrErrors].</p>
<dt>iukwnpr/s</p>
<dd> The number of locally-addressed datagrams received successfully but discarded per second because of an unknown or unsupported protocol [ipInUnknownProtos].</p>
<dt>idisc/s</p>
<dd> The number of input IP datagrams per second for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space) [ipInDiscards]. Note that this counter does not include any datagrams discarded while awaiting re-assembly.</p>
<dt>odisc/s</p>
<dd> The number of output IP datagrams per second for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space) [ipOutDiscards]. Note that this counter would include datagrams counted in fwddgm/s if any such packets met this (discretionary) discard criterion.</p>
<dt>onort/s</p>
<dd> The number of IP datagrams discarded per second because no route could be found to transmit them to their destination [ipOutNoRoutes]. Note that this counter includes any packets counted in fwddgm/s which meet this &#8216;no-route&#8217; criterion. Note that this includes any datagrams which a host cannot route because all of its default routers are down.</p>
<dt>asmf/s</p>
<dd> The number of failures detected per second by the IP re-assembly algorithm (for whatever reason: timed out, errors, etc) [ipReasmFails]. Note that this is not necessarily a count of discarded IP fragments since some algorithms can lose track of the number of fragments by combining them as they are received.</p>
<dt>fragf/s</p>
<dd> The number of IP datagrams that have been discarded per second because they needed to be fragmented at this entity but could not be, e.g., because their Don&#8217;t Fragment flag was set [ipFragFails].</dl>
</dl>
<dt>
<dd> With the <code>IP6</code> keyword, statistics about IPv6 network traffic are reported. Note that IPv6 statistics depend on <code>sadc</code>&#8216;s option <code>-S IPV6</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>irec6/s</p>
<dd> The total number of input datagrams received from interfaces per second, including those received in error [ipv6IfStatsInReceives].</p>
<dt>fwddgm6/s</p>
<dd> The number of output datagrams per second which this entity received and forwarded to their final destinations [ipv6IfStatsOutForwDatagrams].</p>
<dt>idel6/s</p>
<dd> The total number of datagrams successfully delivered per second to IPv6 user-protocols (including ICMP) [ipv6IfStatsInDelivers].</p>
<dt>orq6/s</p>
<dd> The total number of IPv6 datagrams which local IPv6 user-protocols (including ICMP) supplied per second to IPv6 in requests for transmission [ipv6IfStatsOutRequests]. Note that this counter does not include any datagrams counted in fwddgm6/s.</p>
<dt>asmrq6/s</p>
<dd> The number of IPv6 fragments received per second which needed to be reassembled at this interface [ipv6IfStatsReasmReqds].</p>
<dt>asmok6/s</p>
<dd> The number of IPv6 datagrams successfully reassembled per second [ipv6IfStatsReasmOKs].</p>
<dt>imcpck6/s</p>
<dd> The number of multicast packets received per second by the interface [ipv6IfStatsInMcastPkts].</p>
<dt>omcpck6/s</p>
<dd> The number of multicast packets transmitted per second by the interface [ipv6IfStatsOutMcastPkts].</p>
<dt>fragok6/s</p>
<dd> The number of IPv6 datagrams that have been successfully fragmented at this output interface per second [ipv6IfStatsOutFragOKs].</p>
<dt>fragcr6/s</p>
<dd> The number of output datagram fragments that have been generated per second as a result of fragmentation at this output interface [ipv6IfStatsOutFragCreates].</dl>
</dl>
<dt>
<dd> With the <code>EIP6</code> keyword, statistics about IPv6 network errors are reported. Note that IPv6 statistics depend on <code>sadc</code>&#8216;s option <code>-S IPV6</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>ihdrer6/s</p>
<dd> The number of input datagrams discarded per second due to errors in their IPv6 headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IPv6 options, etc. [ipv6IfStatsInHdrErrors]</p>
<dt>iadrer6/s</p>
<dd> The number of input datagrams discarded per second because the IPv6 address in their IPv6 header&#8217;s destination field was not a valid address to be received at this entity. This count includes invalid addresses (e.g., ::0) and unsupported addresses (e.g., addresses with unallocated prefixes). For entities which are not IPv6 routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address [ipv6IfStatsInAddrErrors].</p>
<dt>iukwnp6/s</p>
<dd> The number of locally-addressed datagrams received successfully but discarded per second because of an unknown or unsupported protocol [ipv6IfStatsInUnknownProtos].</p>
<dt>i2big6/s</p>
<dd> The number of input datagrams that could not be forwarded per second because their size exceeded the link MTU of outgoing interface [ipv6IfStatsInTooBigErrors].</p>
<dt>idisc6/s</p>
<dd> The number of input IPv6 datagrams per second for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space) [ipv6IfStatsInDiscards]. Note that this counter does not include any datagrams discarded while awaiting re-assembly.</p>
<dt>odisc6/s</p>
<dd> The number of output IPv6 datagrams per second for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space) [ipv6IfStatsOutDiscards]. Note that this counter would include datagrams counted in fwddgm6/s if any such packets met this (discretionary) discard criterion.</p>
<dt>inort6/s</p>
<dd> The number of input datagrams discarded per second because no route could be found to transmit them to their destination [ipv6IfStatsInNoRoutes].</p>
<dt>onort6/s</p>
<dd> The number of locally generated IP datagrams discarded per second because no route could be found to transmit them to their destination [unknown formal SNMP name].</p>
<dt>asmf6/s</p>
<dd> The number of failures detected per second by the IPv6 re-assembly algorithm (for whatever reason: timed out, errors, etc.) [ipv6IfStatsReasmFails]. Note that this is not necessarily a count of discarded IPv6 fragments since some algorithms can lose track of the number of fragments by combining them as they are received.</p>
<dt>fragf6/s</p>
<dd> The number of IPv6 datagrams that have been discarded per second because they needed to be fragmented at this output interface but could not be [ipv6IfStatsOutFragFails].</p>
<dt>itrpck6/s</p>
<dd> The number of input datagrams discarded per second because datagram frame didn&#8217;t carry enough data [ipv6IfStatsInTruncatedPkts].</dl>
</dl>
<dt>
<dd> With the <code>NFS</code> keyword, statistics about NFS client activity are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>call/s</p>
<dd> Number of RPC requests made per second.</p>
<dt>retrans/s</p>
<dd> Number of RPC requests per second, those which needed to be retransmitted (for example because of a server timeout).</p>
<dt>read/s</p>
<dd> Number of &#8216;read&#8217; RPC calls made per second.</p>
<dt>write/s</p>
<dd> Number of &#8216;write&#8217; RPC calls made per second.</p>
<dt>access/s</p>
<dd> Number of &#8216;access&#8217; RPC calls made per second.</p>
<dt>getatt/s</p>
<dd> Number of &#8216;getattr&#8217; RPC calls made per second.</dl>
</dl>
<dt>
<dd> With the <code>NFSD</code> keyword, statistics about NFS server activity are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>scall/s</p>
<dd> Number of RPC requests received per second.</p>
<dt>badcall/s</p>
<dd> Number of bad RPC requests received per second, those whose processing generated an error.</p>
<dt>packet/s</p>
<dd> Number of network packets received per second.</p>
<dt>udp/s</p>
<dd> Number of UDP packets received per second.</p>
<dt>tcp/s</p>
<dd> Number of TCP packets received per second.</p>
<dt>hit/s</p>
<dd> Number of reply cache hits per second.</p>
<dt>miss/s</p>
<dd> Number of reply cache misses per second.</p>
<dt>sread/s</p>
<dd> Number of &#8216;read&#8217; RPC calls received per second.</p>
<dt>swrite/s</p>
<dd> Number of &#8216;write&#8217; RPC calls received per second.</p>
<dt>saccess/s</p>
<dd> Number of &#8216;access&#8217; RPC calls received per second.</p>
<dt>sgetatt/s</p>
<dd> Number of &#8216;getattr&#8217; RPC calls received per second.</dl>
</dl>
<dt>
<dd> With the <code>SOCK</code> keyword, statistics on sockets in use are reported (IPv4). The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>totsck</p>
<dd> Total number of sockets used by the system.</p>
<dt>tcpsck</p>
<dd> Number of TCP sockets currently in use.</p>
<dt>udpsck</p>
<dd> Number of UDP sockets currently in use.</p>
<dt>rawsck</p>
<dd> Number of RAW sockets currently in use.</p>
<dt>ip-frag</p>
<dd> Number of IP fragments currently in queue.</p>
<dt>tcp-tw</p>
<dd> Number of TCP sockets in TIME_WAIT state.</dl>
</dl>
<dt>
<dd> With the <code>SOCK6</code> keyword, statistics on sockets in use are reported (IPv6). Note that IPv6 statistics depend on <code>sadc</code>&#8216;s option <code>-S IPV6</code> to be collected. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>tcp6sck</p>
<dd> Number of TCPv6 sockets currently in use.</p>
<dt>udp6sck</p>
<dd> Number of UDPv6 sockets currently in use.</p>
<dt>raw6sck</p>
<dd> Number of RAWv6 sockets currently in use.</p>
<dt>ip6-frag</p>
<dd> Number of IPv6 fragments currently in use.</dl>
</dl>
<dt>
<dd> With the <code>SOFT</code> keyword, statistics about software-based network processing are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>total/s</p>
<dd> The total number of network frames processed per second.</p>
<dt>dropd/s</p>
<dd> The total number of network frames dropped per second because there was no room on the processing queue.</p>
<dt>squeezd/s</p>
<dd> The number of times the softirq handler function terminated per second because its budget was consumed or the time limit was reached, but more work could have been done.</p>
<dt>rx_rps/s</p>
<dd> The number of times the CPU has been woken up per second to process packets via an inter-processor interrupt.</p>
<dt>flw_lim/s</p>
<dd> The number of times the flow limit has been reached per second. Flow limiting is an optional RPS feature that can be used to limit the number of packets queued to the backlog for each flow to a certain amount. This can help ensure that smaller flows are processed even though much larger flows are pushing packets in.</dl>
</dl>
<dt>
<dd> With the <code>TCP</code> keyword, statistics about TCPv4 network traffic are reported. Note that TCPv4 statistics depend on <code>sadc</code>&#8216;s option <code>-S SNMP</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>active/s</p>
<dd> The number of times TCP connections have made a direct transition to the SYN-SENT state from the CLOSED state per second [tcpActiveOpens].</p>
<dt>passive/s</p>
<dd> The number of times TCP connections have made a direct transition to the SYN-RCVD state from the LISTEN state per second [tcpPassiveOpens].</p>
<dt>iseg/s</p>
<dd> The total number of segments received per second, including those received in error [tcpInSegs]. This count includes segments received on currently established connections.</p>
<dt>oseg/s</p>
<dd> The total number of segments sent per second, including those on current connections but excluding those containing only retransmitted octets [tcpOutSegs].</dl>
</dl>
<dt>
<dd> With the <code>ETCP</code> keyword, statistics about TCPv4 network errors are reported. Note that TCPv4 statistics depend on <code>sadc</code>&#8216;s option <code>-S SNMP</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>atmptf/s</p>
<dd> The number of times per second TCP connections have made a direct transition to the CLOSED state from either the SYN-SENT state or the SYN-RCVD state, plus the number of times per second TCP connections have made a direct transition to the LISTEN state from the SYN-RCVD state [tcpAttemptFails].</p>
<dt>estres/s</p>
<dd> The number of times per second TCP connections have made a direct transition to the CLOSED state from either the ESTABLISHED state or the CLOSE-WAIT state [tcpEstabResets].</p>
<dt>retrans/s</p>
<dd> The total number of segments retransmitted per second &#8211; that is, the number of TCP segments transmitted containing one or more previously transmitted octets [tcpRetransSegs].</p>
<dt>isegerr/s</p>
<dd> The total number of segments received in error (e.g., bad TCP checksums) per second [tcpInErrs].</p>
<dt>orsts/s</p>
<dd> The number of TCP segments sent per second containing the RST flag [tcpOutRsts].</dl>
</dl>
<dt>
<dd> With the <code>UDP</code> keyword, statistics about UDPv4 network traffic are reported. Note that UDPv4 statistics depend on <code>sadc</code>&#8216;s option <code>-S SNMP</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>idgm/s</p>
<dd> The total number of UDP datagrams delivered per second to UDP users [udpInDatagrams].</p>
<dt>odgm/s</p>
<dd> The total number of UDP datagrams sent per second from this entity [udpOutDatagrams].</p>
<dt>noport/s</p>
<dd> The total number of received UDP datagrams per second for which there was no application at the destination port [udpNoPorts].</p>
<dt>idgmerr/s</p>
<dd> The number of received UDP datagrams per second that could not be delivered for reasons other than the lack of an application at the destination port [udpInErrors].</dl>
</dl>
<dt>
<dd> With the <code>UDP6</code> keyword, statistics about UDPv6 network traffic are reported. Note that UDPv6 statistics depend on <code>sadc</code>&#8216;s option <code>-S IPV6</code> to be collected. The following values are displayed (formal SNMP names between square brackets):</p>
<dl>
<dt>
<dd>
<dl>
<dt>idgm6/s</p>
<dd> The total number of UDP datagrams delivered per second to UDP users [udpInDatagrams].</p>
<dt>odgm6/s</p>
<dd> The total number of UDP datagrams sent per second from this entity [udpOutDatagrams].</p>
<dt>noport6/s</p>
<dd> The total number of received UDP datagrams per second for which there was no application at the destination port [udpNoPorts].</p>
<dt>idgmer6/s</p>
<dd> The number of received UDP datagrams per second that could not be delivered for reasons other than the lack of an application at the destination port [udpInErrors].</dl>
</dl>
<dt>
<dd> The <code>ALL</code> keyword is equivalent to specifying all the keywords above and therefore all the network activities are reported.</p>
<dt><code>-o [ </code><i>filename </i><code>]</code></p>
<dd> Save the readings in the file in binary form. Each reading is in a separate record. The default value of the <i>filename</i> parameter is the current standard system activity daily data file. If <i>filename</i> is a directory instead of a plain file then it is considered as the directory where the standard system activity daily data files are located. Option <code>-o </code>is exclusive of option <code>-f</code>. All the data available from the kernel are saved in the file (in fact, <code>sar </code>calls its data collector <code>sadc </code>with the option <code>-S ALL</code>. See <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8) manual page).</p>
<dt><code>-P { </code><i>cpu_list </i><code>| ALL }</code></p>
<dd> Report per-processor statistics for the specified processor or processors. <i>cpu_list</i> is a list of comma-separated values or range of values (e.g., <code>0,2,4-7,12-</code>). Note that processor 0 is the first processor, and processor <code>all</code> is the global average among all processors. Specifying the <code>ALL</code> keyword reports statistics for each individual processor, and globally for all processors. Offline processors are not displayed.</p>
<dt><code>-p</code>, <code>&#8211;pretty</code></p>
<dd> Make reports easier to read by a human. This option may be especially useful when displaying e.g., network interfaces or block devices statistics.</p>
<dt><code>-q [ </code><i>keyword</i><code>[,&#8230;] | ALL ]</code></p>
<dd> Report system load and pressure-stall statistics. </p>
<p> Possible keywords are <code>CPU</code>, <code>IO</code>, <code>LOAD</code>, <code>MEM </code>and PSI . </p>
<p> With the <code>CPU</code> keyword, CPU pressure statistics are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%scpu-10</p>
<dd> Percentage of the time that at least some runnable tasks were delayed because the CPU was unavailable to them, over the last 10 second window.</p>
<dt>%scpu-60</p>
<dd> Percentage of the time that at least some runnable tasks were delayed because the CPU was unavailable to them, over the last 60 second window.</p>
<dt>%scpu-300</p>
<dd> Percentage of the time that at least some runnable tasks were delayed because the CPU was unavailable to them, over the last 300 second window.</p>
<dt>%scpu</p>
<dd> Percentage of the time that at least some runnable tasks were delayed because the CPU was unavailable to them, over the last time interval.</dl>
</dl>
<dt>
<dd> With the <code>IO</code> keyword, I/O pressure statistics are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%sio-10</p>
<dd> Percentage of the time that at least some tasks lost waiting for I/O, over the last 10 second window.</p>
<dt>%sio-60</p>
<dd> Percentage of the time that at least some tasks lost waiting for I/O, over the last 60 second window.</p>
<dt>%sio-300</p>
<dd> Percentage of the time that at least some tasks lost waiting for I/O, over the last 300 second window.</p>
<dt>%sio</p>
<dd> Percentage of the time that at least some tasks lost waiting for I/O, over the last time interval.</p>
<dt>%fio-10</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for I/O, over the last 10 second window.</p>
<dt>%fio-60</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for I/O, over the last 60 second window.</p>
<dt>%fio-300</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for I/O, over the last 300 second window.</p>
<dt>%fio</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for I/O, over the last time interval.</dl>
</dl>
<dt>
<dd> With the <code>LOAD</code> keyword, queue length and load averages statistics are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>runq-sz</p>
<dd> Run queue length (number of tasks running or waiting for run time).</p>
<dt>plist-sz</p>
<dd> Number of tasks in the task list.</p>
<dt>ldavg-1</p>
<dd> System load average for the last minute. The load average is calculated as the average number of runnable or running tasks (R state), and the number of tasks in uninterruptible sleep (D state) over the specified interval.</p>
<dt>ldavg-5</p>
<dd> System load average for the past 5 minutes.</p>
<dt>ldavg-15</p>
<dd> System load average for the past 15 minutes.</p>
<dt>blocked</p>
<dd> Number of tasks currently blocked, waiting for I/O to complete.</dl>
</dl>
<dt>
<dd> With the <code>MEM</code> keyword, memory pressure statistics are reported. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%smem-10</p>
<dd> Percentage of the time during which at least some tasks were waiting for memory resources, over the last 10 second window.</p>
<dt>%smem-60</p>
<dd> Percentage of the time during which at least some tasks were waiting for memory resources, over the last 60 second window.</p>
<dt>%smem-300</p>
<dd> Percentage of the time during which at least some tasks were waiting for memory resources, over the last 300 second window.</p>
<dt>%smem</p>
<dd> Percentage of the time during which at least some tasks were waiting for memory resources, over the last time interval.</p>
<dt>%fmem-10</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for memory resources, over the last 10 second window.</p>
<dt>%fmem-60</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for memory resources, over the last 60 second window.</p>
<dt>%fmem-300</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for memory resources, over the last 300 second window.</p>
<dt>%fmem</p>
<dd> Percentage of the time during which all non-idle tasks were stalled waiting for memory resources, over the last time interval.</dl>
</dl>
<dt>
<dd> The <code>PSI</code> keyword is equivalent to specifying CPU, IO and MEM keywords together and therefore all the pressure-stall statistics are reported. </p>
<p> The <code>ALL</code> keyword is equivalent to specifying all the keywords above and therefore all the statistics are reported.</p>
<dt><code>-r [ ALL ]</code></p>
<dd> Report memory utilization statistics. The <code>ALL</code> keyword indicates that all the memory fields should be displayed. The following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>kbmemfree</p>
<dd> Amount of free memory available in kilobytes.</p>
<dt>kbavail</p>
<dd> Estimate of how much memory in kilobytes is available for starting new applications, without swapping. The estimate takes into account that the system needs some page cache to function well, and that not all reclaimable slab will be reclaimable, due to items being in use. The impact of those factors will vary from system to system.</p>
<dt>kbmemused</p>
<dd> Amount of used memory in kilobytes (calculated as total installed memory &#8211; kbmemfree &#8211; kbbuffers &#8211; kbcached &#8211; kbslab).</p>
<dt>%memused</p>
<dd> Percentage of used memory.</p>
<dt>kbbuffers</p>
<dd> Amount of memory used as buffers by the kernel in kilobytes.</p>
<dt>kbcached</p>
<dd> Amount of memory used to cache data by the kernel in kilobytes.</p>
<dt>kbcommit</p>
<dd> Amount of memory in kilobytes needed for current workload. This is an estimate of how much RAM/swap is needed to guarantee that there never is out of memory.</p>
<dt>%commit</p>
<dd> Percentage of memory needed for current workload in relation to the total amount of memory (RAM+swap). This number may be greater than 100% because the kernel usually overcommits memory.</p>
<dt>kbactive</p>
<dd> Amount of active memory in kilobytes (memory that has been used more recently and usually not reclaimed unless absolutely necessary).</p>
<dt>kbinact</p>
<dd> Amount of inactive memory in kilobytes (memory which has been less recently used. It is more eligible to be reclaimed for other purposes).</p>
<dt>kbdirty</p>
<dd> Amount of memory in kilobytes waiting to get written back to the disk.</p>
<dt>kbanonpg</p>
<dd> Amount of non-file backed pages in kilobytes mapped into userspace page tables.</p>
<dt>kbslab</p>
<dd> Amount of memory in kilobytes used by the kernel to cache data structures for its own use.</p>
<dt>kbkstack</p>
<dd> Amount of memory in kilobytes used for kernel stack space.</p>
<dt>kbpgtbl</p>
<dd> Amount of memory in kilobytes dedicated to the lowest level of page tables.</p>
<dt>kbvmused</p>
<dd> Amount of memory in kilobytes of used virtual address space.</dl>
</dl>
<dt><code>-S</code></p>
<dd> Report swap space utilization statistics. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>kbswpfree</p>
<dd> Amount of free swap space in kilobytes.</p>
<dt>kbswpused</p>
<dd> Amount of used swap space in kilobytes.</p>
<dt>%swpused</p>
<dd> Percentage of used swap space.</p>
<dt>kbswpcad</p>
<dd> Amount of cached swap memory in kilobytes. This is memory that once was swapped out, is swapped back in but still also is in the swap area (if memory is needed it doesn&#8217;t need to be swapped out again because it is already in the swap area. This saves I/O).</p>
<dt>%swpcad</p>
<dd> Percentage of cached swap memory in relation to the amount of used swap space.</dl>
</dl>
<dt><code>-s [ </code><i>hh</i><code>:</code><i>mm</i><code>[:</code><i>ss</i><code>] ]</code></p>
<dd> Set the starting time of the data, causing the <code>sar</code> command to extract records time-tagged at, or following, the time specified. The default starting time is 08:00:00. Hours must be given in 24-hour format. This option can be used only when data are read from a file (option <code>-f</code>).</p>
<dt><code>&#8211;sadc</code></p>
<dd> Indicate which data collector is called by <code>sar</code>. If the data collector is sought in <code>PATH</code> then enter &quot;which sadc&quot; to know where it is located.</p>
<dt><code>-t</code></p>
<dd> When reading data from a daily data file, indicate that <code>sar</code> should display the timestamps in the original local time of the data file creator. Without this option, the <code>sar</code> command displays the timestamps in the user&#8217;s locale time.</p>
<dt><code>-u [ ALL ]</code></p>
<dd> Report CPU utilization. The <code>ALL</code> keyword indicates that all the CPU fields should be displayed. The report may show the following fields:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%user</p>
<dd> Percentage of CPU utilization that occurred while executing at the user level (application). Note that this field includes time spent running virtual processors.</p>
<dt>%usr</p>
<dd> Percentage of CPU utilization that occurred while executing at the user level (application). Note that this field does NOT include time spent running virtual processors.</p>
<dt>%nice</p>
<dd> Percentage of CPU utilization that occurred while executing at the user level with nice priority.</p>
<dt>%system</p>
<dd> Percentage of CPU utilization that occurred while executing at the system level (kernel). Note that this field includes time spent servicing hardware and software interrupts.</p>
<dt>%sys</p>
<dd> Percentage of CPU utilization that occurred while executing at the system level (kernel). Note that this field does NOT include time spent servicing hardware or software interrupts.</p>
<dt>%iowait</p>
<dd> Percentage of time that the CPU or CPUs were idle during which the system had an outstanding disk I/O request.</p>
<dt>%steal</p>
<dd> Percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor.</p>
<dt>%irq</p>
<dd> Percentage of time spent by the CPU or CPUs to service hardware interrupts.</p>
<dt>%soft</p>
<dd> Percentage of time spent by the CPU or CPUs to service software interrupts.</p>
<dt>%guest</p>
<dd> Percentage of time spent by the CPU or CPUs to run a virtual processor.</p>
<dt>%gnice</p>
<dd> Percentage of time spent by the CPU or CPUs to run a niced guest.</p>
<dt>%idle</p>
<dd> Percentage of time that the CPU or CPUs were idle and the system did not have an outstanding disk I/O request.</dl>
</dl>
<dt><code>-V</code></p>
<dd> Print version number then exit.</p>
<dt><code>-v</code></p>
<dd> Report status of inode, file and other kernel tables. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>dentunusd</p>
<dd> Number of unused cache entries in the directory cache.</p>
<dt>file-nr</p>
<dd> Number of file handles used by the system.</p>
<dt>inode-nr</p>
<dd> Number of inode handlers used by the system.</p>
<dt>pty-nr</p>
<dd> Number of pseudo-terminals used by the system.</dl>
</dl>
<dt><code>-W</code></p>
<dd> Report swapping statistics. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>pswpin/s</p>
<dd> Total number of swap pages the system brought in per second.</p>
<dt>pswpout/s</p>
<dd> Total number of swap pages the system brought out per second.</dl>
</dl>
<dt><code>-w</code></p>
<dd> Report task creation and system switching activity. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>proc/s</p>
<dd> Total number of tasks created per second.</p>
<dt>cswch/s</p>
<dd> Total number of context switches per second.</dl>
</dl>
<dt><code>-y</code></p>
<dd> Report TTY devices activity. The following values are displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>rcvin/s</p>
<dd> Number of receive interrupts per second for current serial line. Serial line number is given in the TTY column.</p>
<dt>xmtin/s</p>
<dd> Number of transmit interrupts per second for current serial line.</p>
<dt>framerr/s</p>
<dd> Number of frame errors per second for current serial line.</p>
<dt>prtyerr/s</p>
<dd> Number of parity errors per second for current serial line.</p>
<dt>brk/s</p>
<dd> Number of breaks per second for current serial line.</p>
<dt>ovrun/s</p>
<dd> Number of overrun errors per second for current serial line.</dl>
</dl>
<dt><code>-z</code></p>
<dd> Tell <code>sar</code> to omit output for any devices for which there was no activity during the sample period. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>sar</code> command takes into account the following environment variables:</p>
<dl>
<dt><code>S_COLORS</code></p>
<dd> By default statistics are displayed in color when the output is connected to a terminal. Use this variable to change the settings. Possible values for this variable are <i>never</i>, <i>always </i>or <i>auto</i> (the latter is equivalent to the default settings).<br />
 Please note that the color (being red, yellow, or some other color) used to display a value is not indicative of any kind of issue simply because of the color. It only indicates different ranges of values.</p>
<dt><code>S_COLORS_SGR</code></p>
<dd> Specify the colors and other attributes used to display statistics on the terminal. Its value is a colon-separated list of capabilities that defaults to <code>C=33;22:H=31;1:I=32;22:M=35;1:N=34;1:R=31;22:Z=34;22</code>. Supported capabilities are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>C=</code></p>
<dd> SGR (Select Graphic Rendition) substring for comments inserted in the binary daily data files.</p>
<dt><code>H=</code></p>
<dd> SGR substring for percentage values greater than or equal to 75%.</p>
<dt><code>I=</code></p>
<dd> SGR substring for item names or values (eg. network interfaces, CPU number&#8230;)</p>
<dt><code>M=</code></p>
<dd> SGR substring for percentage values in the range from 50% to 75%.</p>
<dt><code>N=</code></p>
<dd> SGR substring for non-zero statistics values.</p>
<dt><code>R=</code></p>
<dd> SGR substring for restart messages.</p>
<dt><code>Z=</code></p>
<dd> SGR substring for zero values.</dl>
</dl>
<dt><code>S_TIME_DEF_TIME</code></p>
<dd> If this variable exists and its value is <code>UTC </code>then <code>sar</code> will save its data in UTC time (data will still be displayed in local time). <code>sar</code> will also use UTC time instead of local time to determine the current daily data file located in the <i>/var/log/sysstat</i> directory. This variable may be useful for servers with users located across several timezones.</p>
<dt><code>S_TIME_FORMAT</code></p>
<dd> If this variable exists and its value is <code>ISO</code> then the current locale will be ignored when printing the date in the report header. The <code>sar</code> command will use the ISO 8601 format (YYYY-MM-DD) instead. The timestamp will also be compliant with ISO 8601 format. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>sar -u 2 5</code></p>
<dd> Report CPU utilization for each 2 seconds. 5 lines are displayed.</p>
<dt><code>sar -I 14 -o int14.file 2 10</code></p>
<dd> Report statistics on IRQ 14 for each 2 seconds. 10 lines are displayed. Data are stored in a file called <i>int14.file</i>.</p>
<dt><code>sar -r -n DEV -f /var/log/sysstat/sa16</code></p>
<dd> Display memory and network statistics saved in daily data file <i>sa16</i>.</p>
<dt><code>sar -A</code></p>
<dd> Display all the statistics saved in current daily data file. </p>
</dl>
<h2>BUGS</h2>
<p> <i>/proc </i>filesystem must be mounted for the <code>sar </code>command to work. </p>
<p> All the statistics are not necessarily available, depending on the kernel version used. <code>sar</code> assumes that you are using at least a 2.6 kernel. </p>
<p> Although <code>sar</code> speaks of kilobytes (kB), megabytes (MB)&#8230;, it actually uses kibibytes (kiB), mebibytes (MiB)&#8230; A kibibyte is equal to 1024 bytes, and a mebibyte is equal to 1024 kibibytes. </p>
<h2>FILES</h2>
<p> <i>/var/log/sysstat/saDD</i><br />
 <i>/var/log/sysstat/saYYYYMMDD</i></p>
<dl>
<dt>
<dd> The standard system activity daily data files and their default location. <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day.</dl>
<p> <i>/proc </i>and <i>/sys </i>contain various files with system statistics. </p>
<h2>AUTHOR</h2>
<p> Sebastien Godard (sysstat &lt;at&gt; orange.fr) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-sadc/">sadc</a></code>(8), <code><a href="/docs/linux/man/8-sa1/">sa1</a></code>(8), <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8), <code><a href="/docs/linux/man/1-sadf/">sadf</a></code>(1), <code><a href="/docs/linux/man/5-sysstat/">sysstat</a></code>(5), <code><a href="/docs/linux/man/1-pidstat/">pidstat</a></code>(1), <code><a href="/docs/linux/man/1-mpstat/">mpstat</a></code>(1), <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8) </p>
<p> <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
<h2>Index</h2>
