---
title: "iperf(1)"
name: "iperf"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iperf/"
description: "iperf – perform network throughput tests"
---

<h2>NAME</h2>
<p> iperf &#8211; perform network throughput tests</p>
<h2>SYNOPSIS</h2>
<p> <code>iperf -s [</code> <i>options</i> <code>]</code> </p>
<p> <code>iperf -c </code> <i>server</i> <code>[</code> <i>options</i> <code>]</code> </p>
<p> <code>iperf -u -s [</code> <i>options</i> <code>]</code> </p>
<p> <code>iperf -u -c </code> <i>server</i> <code>[</code> <i>options</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> iperf is a tool for performing network throughput measurements. It can test either TCP or UDP throughput. To perform an iperf test the user must establish both a server (to discard traffic) and a client (to generate traffic).</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-e</code>, <code>&#8211;enhanced</code></p>
<dd> Display enhanced output in reports</p>
<dt><code>-f</code>, <code>&#8211;format</code></p>
<dd> [kmKM] format to report: Kbits, Mbits, KBytes, MBytes</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print a help synopsis</p>
<dt><code>-i</code>, <code>&#8211;interval</code> <i>n</i></p>
<dd> pause <i>n</i> seconds between periodic bandwidth reports</p>
<dt><code>-l</code>, <code>&#8211;len</code> <i>n</i>[KM]</p>
<dd> set length read/write buffer to <i>n</i> (default 8 KB)</p>
<dt><code>-m</code>, <code>&#8211;print_mss</code></p>
<dd> print TCP maximum segment size (MTU &#8211; TCP/IP header)</p>
<dt><code>-o</code>, <code>&#8211;output</code> <i>filename</i></p>
<dd> output the report or error message to this specified file</p>
<dt><code>-p</code>, <code>&#8211;port</code> <i>n</i></p>
<dd> set server port to listen on/connect to to <i>n</i> (default 5001)</p>
<dt><code>-u</code>, <code>&#8211;udp</code></p>
<dd> use UDP rather than TCP</p>
<dt><code>-w</code>, <code>&#8211;window</code> <i>n</i>[KM]</p>
<dd> TCP window size (socket buffer size)</p>
<dt><code>-z</code>, <code>&#8211;realtime</code></p>
<dd> Request realtime scheduler, if supported.</p>
<dt><code>-B</code>, <code>&#8211;bind</code> <i>host</i></p>
<dd> bind to <i>host</i>, an interface or multicast address</p>
<dt><code>-C</code>, <code>&#8211;compatibility</code></p>
<dd> for use with older versions does not sent extra msgs</p>
<dt><code>-M</code>, <code>&#8211;mss</code> <i>n</i></p>
<dd> set TCP maximum segment size (MTU &#8211; 40 bytes)</p>
<dt><code>-N</code>, <code>&#8211;nodelay</code></p>
<dd> set TCP no delay, disabling Nagle&#8217;s Algorithm</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information and quit</p>
<dt><code>-V</code>, <code>&#8211;IPv6Version</code></p>
<dd> Set the domain to IPv6</p>
<dt><code>-x</code>, <code>&#8211;reportexclude</code> [CDMSV]</p>
<dd> exclude C(connection) D(data) M(multicast) S(settings) V(server) reports</p>
<dt><code>-y</code>, <code>&#8211;reportstyle</code> C|c</p>
<dd> if set to C or c report results as CSV (comma separated values)</dl>
<h2>SERVER SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;server</code></p>
<dd> run in server mode</p>
<dt><code>-U</code>, <code>&#8211;single_udp</code></p>
<dd> run in single threaded UDP mode</p>
<dt><code>-D</code>, <code>&#8211;daemon</code></p>
<dd> run the server as a daemon. On Windows this will also install the IPerfService.</p>
<dt><code>-R</code>, <code>&#8211;remove</code></p>
<dd> remove the IPerfService (Windows only).</dl>
<h2>CLIENT SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;bandwidth</code> <i>n</i>[KMG] | <i>n</i>pps</p>
<dd> set target bandwidth to <i>n</i> bits/sec (default 1 Mbit/sec) or <i>n</i> packets per sec. This may be used with TCP or UDP.</p>
<dt><code>-c</code>, <code>&#8211;client</code> <i>host</i></p>
<dd> run in client mode, connecting to <i>host</i></p>
<dt><code>-d</code>, <code>&#8211;dualtest</code></p>
<dd> Do a bidirectional test simultaneously</p>
<dt><code>-n</code>, <code>&#8211;num</code> <i>n</i>[KM]</p>
<dd> number of bytes to transmit (instead of -t)</p>
<dt><code>-r</code>, <code>&#8211;tradeoff</code></p>
<dd> Do a bidirectional test individually</p>
<dt><code>-t</code>, <code>&#8211;time</code> <i>n</i></p>
<dd> time in seconds to transmit for (default 10 secs)</p>
<dt><code>-B</code>, <code>&#8211;bind</code> <i>ip</i> | <i>ip</i>:<i>port</i></p>
<dd> bind src addr(s) from which to originate traffic</p>
<dt><code>-F</code>, <code>&#8211;fileinput</code> <i>name</i></p>
<dd> input the data to be transmitted from a file</p>
<dt><code>-I</code>, <code>&#8211;stdin</code></p>
<dd> input the data to be transmitted from stdin</p>
<dt><code>-L</code>, <code>&#8211;listenport</code> <i>n</i></p>
<dd> port to recieve bidirectional tests back on</p>
<dt><code>-P</code>, <code>&#8211;parallel</code> <i>n</i></p>
<dd> number of parallel client threads to run</p>
<dt><code>-T</code>, <code>&#8211;ttl</code> <i>n</i></p>
<dd> time-to-live, for multicast (default 1)</p>
<dt><code>-Z</code>, <code>&#8211;linux-congestion</code> <i>algo</i></p>
<dd> set TCP congestion control algorithm (Linux only)</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TCP_WINDOW_SIZE</code></p>
<dd> Controls the size of TCP buffers.</dl>
<h2>DIAGNOSTICS</h2>
<p> This section needs to be filled in.</p>
<h2>BUGS</h2>
<p> Exit statuses are inconsistent. The threading implementation is rather heinous.</p>
<h2>AUTHORS</h2>
<p> Iperf was originally written by Mark Gates and Alex Warshavsky. Man page and maintence by Jon Dugan &lt;jdugan at x1024 dot net&gt;. Other contributions from Ajay Tirumala, Jim Ferguson, Feng Qin, Kevin Gibbs, John Estabrook &lt;jestabro at ncsa.uiuc.edu&gt;, Andrew Gallatin &lt;gallatin at gmail.com&gt;, Stephen Hemminger &lt;shemminger at linux-foundation.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://iperf.sourceforge.net/">http://iperf.sourceforge.net/</a> </p>
<h2>Index</h2>
