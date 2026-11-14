---
title: "fping(8)"
name: "fping"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fping/"
description: "fping – send ICMP ECHO_REQUEST packets to network hosts"
---

<p>fping &#8211; send ICMP ECHO_REQUEST packets to network hosts</p>
<h2>Synopsis</h2>
<p><code>fping</code> [ <i>options</i> ] [ <i>systems&#8230;</i> ] <code>fping6</code> [ <i>options</i> ] [ <i>systems&#8230;</i> ]</p>
<h2>Description</h2>
<p><code>fping</code> is a program like <code>ping</code> which uses the Internet Control Message Protocol (<font SIZE="-1">ICMP</font>) echo request to determine if a target host is responding. <code>fping</code> differs from <code>ping</code> in that you can specify any number of targets on the command line, or specify a file containing the lists of targets to ping. Instead of sending to one target until it times out or replies, <code>fping</code> will send out a ping packet and move on to the next target in a round-robin fashion. In the default mode, if a target replies, it is noted and removed from the list of targets to check; if a target does not respond within a certain time limit and/or retry limit it is designated as unreachable. <code>fping</code> also supports sending a specified number of pings to a target, or looping indefinitely (as in <code>ping</code> ). Unlike <code>ping</code>, <code>fping</code> is meant to be used in scripts, so its output is designed to be easy to parse. </p>
<p> The binary named <code>fping6</code> is the same as <code>fping</code>, except that it uses IPv6 addresses instead of IPv4.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Show systems that are alive.</p>
<dt><code>-A</code></p>
<dd>Display targets by address rather than <font SIZE="-1">DNS</font> name.</p>
<dt><code>-b</code> <i>n</i></p>
<dd>Number of bytes of ping data to send. The minimum size (normally 12) allows room for the data that <code>fping</code> needs to do its work (sequence number, timestamp). The reported received data size includes the <font SIZE="-1">IP</font> header (normally 20 bytes) and <font SIZE="-1">ICMP</font> header (8 bytes), so the minimum total size is 40 bytes. Default is 56, as in <code>ping</code>. Maximum is the theoretical maximum <font SIZE="-1">IP</font> datagram size (64K), though most systems limit this to a smaller, system-dependent number.</p>
<dt><code>-B</code> <i>n</i></p>
<dd>Backoff factor. In the default mode, <code>fping</code> sends several requests to a target before giving up, waiting longer for a reply on each successive request. This parameter is the value by which the wait time (<code>-t</code>) is multiplied on each successive request; it must be entered as a floating-point number (x.y). The default is 1.5.</p>
<dt><code>-c</code> <i>n</i></p>
<dd>Number of request packets to send to each target. In this mode, a line is displayed for each received response (this can suppressed with <code>-q</code> or <code>-Q</code>). Also, statistics about responses for each target are displayed when all requests have been sent (or when interrupted).</p>
<dt><code>-C</code> <i>n</i></p>
<dd>Similar to <code>-c</code>, but the per-target statistics are displayed in a format designed for automated response-time statistics gathering. For example: </p>
<pre> % fping -C 5 -q somehost 
 somehost : 91.7 37.0 29.2 - 36.8</pre>
<p>shows the response time in milliseconds for each of the five requests, with the <tt>&quot;-&quot;</tt> indicating that no response was received to the fourth request.</p>
<dt><code>-d</code></p>
<dd>Use <font SIZE="-1">DNS</font> to lookup address of return ping packet. This allows you to give fping a list of <font SIZE="-1">IP</font> addresses as input and print hostnames in the output.</p>
<dt><code>-D</code></p>
<dd>Add Unix timestamps in front of output lines generated with in looping or counting modes (<code>-l</code>, <code>-c</code>, or <code>-C</code>).</p>
<dt><code>-e</code></p>
<dd>Show elapsed (round-trip) time of packets.</p>
<dt><code>-f</code></p>
<dd>Read list of targets from a file. This option can only be used by the root user. Regular users should pipe in the file via stdin: </p>
<pre> % fping &lt; targets_file</pre>
<dt><code>-g</code> <i>addr/mask</i></p>
<dd>Generate a target list from a supplied <font SIZE="-1">IP</font> netmask, or a starting and ending <font SIZE="-1">IP</font>. Specify the netmask or start/end in the targets portion of the command line. If a network with netmask is given, the network and broadcast addresses will be excluded. ex. To ping the network 192.168.1.0/24, the specified command line could look like either: </p>
<pre> fping -g 192.168.1.0/24</pre>
<p>or </p>
<pre> fping -g 192.168.1.1 192.168.1.254</pre>
<dt><code>-h</code></p>
<dd>Print usage message.</p>
<dt><code>-i</code> <i>n</i></p>
<dd>The minimum amount of time (in milliseconds) between sending a ping packet to any target (default is 25).</p>
<dt><code>-l</code></p>
<dd>Loop sending packets to each target indefinitely. Can be interrupted with Ctrl-C; statistics about responses for each target are then displayed.</p>
<dt><code>-m</code></p>
<dd>Send pings to each of a target host&#8217;s multiple interfaces.</p>
<dt><code>-n</code></p>
<dd>Same as -d.</p>
<dt><code>-p</code> &lt;n&gt;</p>
<dd>In looping or counting modes (<code>-l</code>, <code>-c</code>, or <code>-C</code>), this parameter sets the time in milliseconds that <code>fping</code> waits between successive packets to an individual target. Default is 1000.</p>
<dt><code>-q</code></p>
<dd>Quiet. Don&#8217;t show per-probe results, but only the final summary. Also don&#8217;t show <font SIZE="-1">ICMP</font> error messages.</p>
<dt><code>-Q</code> <i>n</i></p>
<dd>Like <code>-q</code>, but show summary results every n seconds.</p>
<dt><code>-r</code> <i>n</i></p>
<dd>Retry limit (default 3). This is the number of times an attempt at pinging a target will be made, not including the first try.</p>
<dt><code>-s</code></p>
<dd>Print cumulative statistics upon exit.</p>
<dt><code>-S</code> <i>addr</i></p>
<dd>Set source address.</p>
<dt><code>-I</code> <i>if</i></p>
<dd>Set the interface (requires <font SIZE="-1">SO_BINDTODEVICE</font> support)</p>
<dt><code>-t</code> <i>n</i></p>
<dd>Initial target timeout in milliseconds (default 500). In the default mode, this is the amount of time that <code>fping</code> waits for a response to its first request. Successive timeouts are multiplied by the backoff factor specified with <code>-B</code>. Note that this option has no effect looping or counting modes (<code>-l</code>, <code>-c</code>, or <code>-C</code>).</p>
<dt><code>-T</code> <i>n</i></p>
<dd>Ignored (for compatibility with fping 2.4).</p>
<dt><code>-u</code></p>
<dd>Show targets that are unreachable.</p>
<dt><code>-O</code> <i>n</i></p>
<dd>Set the typ of service flag (<font SIZE="-1">TOS</font>). <i>n</i> can be either decimal or hexadecimal (0xh) format.</p>
<dt><code>-v</code></p>
<dd>Print <code>fping</code> version information.</p>
<dt><code>-H</code> <i>n</i></p>
<dd>Set the <font SIZE="-1">IP</font> <font SIZE="-1">TTL</font> field (time to live hops).</dl>
<h2>Authors</h2>
<dl>
<dt>&bull;</p>
<dd>Roland J. Schemers <font SIZE="-1">III</font>, Stanford University, concept and versions 1.x</p>
<dt>&bull;</p>
<dd><font SIZE="-1">RL</font> &#8220;Bob&#8221; Morgan, Stanford University, versions 2.x</p>
<dt>&bull;</p>
<dd>David Papp, versions 2.3x and up</p>
<dt>&bull;</p>
<dd>David Schweikert, versions 3.0 and up</dl>
<p> <code>fping website: &lt;<a rel="nofollow" href="http://www.fping.org">http://www.fping.org</a>&gt;</code></p>
<h2>Diagnostics</h2>
<p>Exit status is 0 if all the hosts are reachable, 1 if some hosts were unreachable, 2 if any <font SIZE="-1">IP</font> addresses were not found, 3 for invalid command line arguments, and 4 for a system call failure.</p>
<h2>Restrictions</h2>
<p>If certain options are used (i.e, a low value for <code>-i</code> and <code>-t</code>, and a high value for <code>-r</code>) it is possible to flood the network. This program must be installed as setuid root in order to open up a raw socket, or must be run by root. In order to stop mere mortals from hosing the network, normal users can&#8217;t specify the following:</p>
<dl>
<dt>&bull;</p>
<dd><code>-i</code> <i>n</i>, where <i>n</i> &lt; 10 msec</p>
<dt>&bull;</p>
<dd><code>-r</code> <i>n</i>, where <i>n</i> &gt; 20</p>
<dt>&bull;</p>
<dd><code>-t</code> <i>n</i>, where n &lt; 250 msec</dl>
<h2>See Also</h2>
<p><tt><a href="/docs/linux/man/8-ping/">ping</a>(8)</tt> </p>
