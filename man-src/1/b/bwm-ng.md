---
title: "bwm-ng(1)"
name: "bwm-ng"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bwm-ng/"
description: "bwm-ng – Bandwidth Monitor NG (Next Generation), a live bandwidth monitor for network and disk io."
---

<h2 class="name">NAME</h2>
<p> bwm-ng &#8211; Bandwidth Monitor NG (Next Generation), a live bandwidth monitor for network and disk io. </p>
<h2>SYNOPSIS</h2>
<p> <code>bwm-ng [options]</code><i> &#8230; [configfile]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bwm-ng</code> can be used to monitor the current bandwidth of all or some specific network interfaces or disks (or partitions). It shows total of in and out as well as total of all interfaces/devices. Several different output methods are supported (curses, curses2, plain, csv and html). </p>
<p> <code>bwm-ng</code> is not limited in the number of interfaces or disks and can handle new ones dynamically while its running or hide those which are not up. </p>
<h2>INPUT METHODS</h2>
<p> The input methods used pretty much depends on your OS and system. You can choose the preferred method either at start or in curses during run-time. Each method can only be used if <code>bwm-ng </code> was compiled with support for it. </p>
<p> Currently supported <code>network input methods:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>proc</code>:</p>
<dd> This is the default for <i>Linux</i> based systems. It parses the special procfs file <code>/proc/net/dev</code>. This should be used if in doubt in <i>Linux</i>.</p>
<dt><code>getifaddrs</code>:</p>
<dd> This is the default on <i>BSD</i> systems like <i>FreeBSD</i>, <i>NetBSD</i>, <i>OpenBSD</i> and recent <i>Mac OS X</i> (&gt;=10.3). This should be used if in doubt on those systems. It uses the getifaddrs systemcall.</p>
<dt><code>kstat</code>:</p>
<dd> This is the default for <i>Solaris</i>. It uses the kstat systemcall.</p>
<dt><code>sysctl</code>:</p>
<dd> This is the default on Systems like <i>IRIX</i> and other <i>UNIX</i>. It can be used on many other systems like early <i>Mac OS X</i> as well. It uses the sysctl systemcall.</p>
<dt><code>netstat</code>:</p>
<dd> This is a Backup for systems without the above, or other problems.</p>
<dt><code>libstatgrab</code>:</p>
<dd> <code>bwm-ng</code> can use the external library libstatgrab to gather the data. please refer to <i><a rel="nofollow" href="http://www.i-scream.org/libstatgrab">http://www.i-scream.org/libstatgrab</a></i> for more info about this.</dl>
</dl>
<p> Currently supported <code>disk input methods:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>disk</code>:</p>
<dd> Shows the diskio on Linux 2.6+ systems using /proc/diskstats. Instead of packets the number of read/writes will be shown.</p>
<dt><code>kstatdisk</code>:</p>
<dd> same as <code>kstat</code> network input but for disk io. It uses the kstat systemcall from Solaris.</p>
<dt><code>sysctl</code>:</p>
<dd> Written for <i>NetBSD</i> and <i>OpenBSD</i>, but maybe working on other Platforms aswell.</p>
<dt><code>devstat</code>:</p>
<dd> devstat library based input. You can find this on FreeBSD based systems.</p>
<dt><code>ioservice</code>:</p>
<dd> framework IOKit based input. You can find this on Darwin systems like MacOSX.</p>
<dt><code>libstatdisk</code>:</p>
<dd> same as <code>libstatgrab</code> but for disk io (<i><a rel="nofollow" href="http://www.i-scream.org/libstatgrab/">http://www.i-scream.org/libstatgrab/</a></i>). </p>
</dl>
</dl>
<h2>OUTPUT METHODS</h2>
<p> You can select several different ways to output the data gathered by <code>bwm-ng</code>. </p>
<p> You can use one of: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>curses</code>:</p>
<dd> This is the default output method. Usually this fits you the most. In <i>curses</i> mode you can control <code>bwm-ng</code> with several keys. Press &#8216;h&#8217; for a online help. To quit using this mode either press &#8216;q&#8217; or ctrl-c.</p>
<dt><code>curses2</code>:</p>
<dd> Shows bar charts of the current IO, using curses output.</p>
<dt><code>plain</code>:</p>
<dd> <i>Plain</i> or <i>ASCII</i> is mostly a backup if curses is not available. You cannot control <code>bwm-ng</code> at all in this mode. To quit press ctrl-c. But for one single single output using this is the mode that fits the best.</p>
<dt><code>csv</code>:</p>
<dd> <i>CSV</i> is designed to use with scripts for easy parsing. </p>
<p> <code>Type rate</code>: </p>
<pre><code>
unix timestamp;
iface_name;
bytes_out / s;
bytes_in / s;
bytes_total / s;
bytes_in;
bytes_out;
packets_out / s;
packets_in / s;
packets_total / s;
packets_in;
packets_out;
errors_out / s;
errors_in / s;
errors_in;
errors_out

</code></pre>
<p> <code>Type svg, sum, max</code>: </p>
<pre><code>
unix timestamp;
iface_name;
bytes_out;
bytes_in;
bytes_total;
packets_out;
packets_in;
packets_total;
errors_out;
errors_in

</code></pre>
<p> To skip the first output with only zeros use: </p>
<pre>
bwm-ng -o csv -c 0
</pre>
<dt><code>html</code>:</p>
<dd> This is designed for use in the WWW. It uses the CSS file bwm-ng.css in current working dir. &quot;&#8211;htmlrefresh&quot; only affects the refresh of the page by the browser. For best results use the same value for &#8211;timeout and &#8211;htmlrefresh.</dl>
</dl>
<h2>OPTIONS</h2>
<p> The options that are recognized by <code>bwm-ng</code> can be divided into 3 different groups. The long versions can only be used if bwm-ng was compiled with getopt_long. </p>
<h3>INPUT</h3>
<p> These options specify the method to gather the data as well as different options for them.</p>
<dl>
<dt><code>-i, &#8211;input </code><i>method</i></p>
<dd> selects which method to use. It can be one of the above (see <code>INPUT METHODS</code>) if support for it was compiled in.</p>
<dt><code>-f, &#8211;procfile </code><i>filename</i></p>
<dd> selects the file to parse in <code>proc input method</code>. This is usually <i>/proc/net/dev</i>.</p>
<dt><code> &#8211;diskstatsfile </code><i>filename</i></p>
<dd> selects the file to parse in <code>disk input method</code>. This is usually <i>/proc/diskstats</i>.</p>
<dt><code> &#8211;partitionsfile </code><i>filename</i></p>
<dd> selects the file to parse in <code>disk input method</code> on older Kernel. This is usually <i>/proc/partitions</i>.</p>
<dt><code>-n, &#8211;netstat </code><i>path</i></p>
<dd> specifies the binary to execute for <code>netstat input method</code>. Because this may be a security flaw support for this option is <i>not</i> compiled in <code>bwm-ng </code> by default. </p>
</dl>
<h3>OUTPUT</h3>
<p> These options select the way to output the data and several options for the output.</p>
<dl>
<dt><code>-o, &#8211;output </code><i>method</i></p>
<dd> selects which method to use for output. It can be one of the above (see <code>OUTPUT METHODS</code>) if support for it was compiled in.</p>
<dt><code>-u, &#8211;unit </code><i>value</i></p>
<dd> selects which unit to show. It can be one of <i>bytes</i>, <i>bits</i>, <i>packets</i> or <i>errors</i>.</p>
<dt><code>-T, &#8211;type </code><i>value</i></p>
<dd> specifies the type of stats to show. Use one of <i>rate</i> for the current rate/s, <i>max</i> for the maximal value achieved since startup of <code>bwm-ng</code>, <i>sum</i> for the total sum counted since startup of <code>bwm-ng</code> or <i>avg</i> for the average over the last 30 seconds.</p>
<dt><code>-c, &#8211;count </code><i>number</i></p>
<dd> number of outputs for <i>Plain</i> and <i>CSV</i> output mode. Use &#8216;1&#8217; for once single output. Using &#8216;0&#8217; in <i>CSV</i> mode will skip first output that always consists of zero values.</p>
<dt><code>-C, &#8211;csvchar </code><i>char</i></p>
<dd> specifies the delimiter char for <i>CSV</i> mode. The default is &#8216;;&#8217;.</p>
<dt><code>-F, &#8211;outfile </code><i>filename</i></p>
<dd> specifies the use of a <i>outfile</i> instead of <i>stdout</i>. This option only affects <i>CSV</i> and <i>HTML</i> mode.</p>
<dt><code>-R, &#8211;htmlrefresh </code><i>seconds</i></p>
<dd> sets the <i>HTML</i> Meta refresh field to seconds in <i>HTML</i> mode. This will result in a reload of the page every <i>n</i> seconds by the browser. If this is set you want to use <i>&#8211;htmlheader</i> as well.</p>
<dt><code>-H, &#8211;htmlheader </code><i>[value]</i></p>
<dd> if this option is used, <code>bwm-ng</code> will print the correct <i>HTML</i> header (&lt;html&gt;&lt;/html&gt;) including Meta fields before and after data. This is only useful in <i>HTML</i> mode. <i>value</i> can be 0 (off) or 1 (on), if the value is not given &#8216;1&#8217; is used.</p>
<dt><code>-N, &#8211;ansiout </code></p>
<dd> disable ANSI Codes for Plain output.</p>
<dt><code> &#8211;longdisknames </code></p>
<dd> show long realnames of disks in Darwin (ioservice input) </p>
</dl>
<h3>OTHER</h3>
<p> These options specify the general behavior of <code>bwm-ng</code>.</p>
<dl>
<dt><code>-t, &#8211;timeout </code><i>msec</i></p>
<dd> displays and gathers stats every <i>n</i> msec (1msec = 1/1000sec). The default is 500msec.</p>
<dt><code>-d, &#8211;dynamic </code><i>[value]</i></p>
<dd> shows bytes and bits with dynamic unit like K, M or G (Kilo, Mega, Giga). <i>value</i> can be 0 (off) or 1 (on), without a value &#8216;1&#8217; is used.</p>
<dt><code>-a, &#8211;allif </code><i>[mode]</i></p>
<dd> specifies whether only up and selected interfaces (<i>mode</i>=0), all which are up but maybe not selected (<i>mode</i>=1) or all, even down and not selected interfaces (<i>mode</i>=2). If no interface list given (<i>&#8211;interfaces</i>) <i>mode</i>=1 and <i>mode</i>=2 are the same.</p>
<dt><code>-I, &#8211;interfaces </code><i>list</i></p>
<dd> show only interfaces which are in this comma separated list (<code>whitelist</code>). If the list is prefixed by a &#8216;%&#8217; its meaning is negated and interfaces in this list are hidden from output (<code>blacklist</code>). (Example: %eth0,tun0)</p>
<dt><code>-S, &#8211;sumhidden </code><i>[value]</i></p>
<dd> if given and the optional value is not 0, count also hidden and not shown interfaces for total value.</p>
<dt><code>-A, &#8211;avglength </code><i>seconds</i></p>
<dd> sets the span in which the stats for average mode are collected. Default is 30 seconds or 2*<i>timeout</i>.</p>
<dt><code>-D, &#8211;daemon </code><i>[value]</i></p>
<dd> fork into background and daemonize if given and the optional value is not 0. This only affects <i>HTML</i> and <i>CSV</i> mode and <i>&#8211;outfile</i> is required.</p>
<dt><code>-h, &#8211;help </code><i></i></p>
<dd> show a help of command line options.</p>
<dt><code>-V, &#8211;version </code><i></i></p>
<dd> print version info </p>
</dl>
<h2>CONFIGFILE</h2>
<p> The behavior of <code>bwm-ng</code> can be also controlled by a <i>configfile</i>. By default <code>bwm-ng</code> first reads /etc/bwm-ng.conf and then ~/.bwm-ng.conf. If specified on command line <code>bwm-ng</code> skips those. It consists of the same long-options as used for command line as keys followed by a &#8216;=&#8217; and the value. Lines starting with a # or unknown key will be ignored. </p>
<p> For example: </p>
<pre>
DYNAMIC=1
UNIT=bits
PROCFILE=/proc/net/dev
OUTPUT=plain
</pre>
<h2>OTHER FILES</h2>
<p> <code>bwm-ng.css</code> the CSS file used for html output. </p>
<h2>SEE ALSO</h2>
<p> bwm-ng.conf-example for an example of the configfile, README for other comments and hints about bwm-ng.<br />
 <i><a rel="nofollow" href="http://www.gropp.org/">http://www.gropp.org/</a></i> for new version or further help and links.</p>
<h2>AUTHORS</h2>
<p> Volker Gropp &lt;bwmng [at] gropp.org&gt; wrote bwm-ng and is current maintainer.<br />
 For further Authors please refer to AUTHORS file which should come with <code>bwm-ng</code>. </p>
<h2>Index</h2>
