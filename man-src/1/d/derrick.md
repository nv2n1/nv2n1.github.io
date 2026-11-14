---
title: "derrick(1)"
name: "derrick"
section: "1"
letter: "d"
url: "/docs/linux/man/1-derrick/"
description: "derrick — a simple network stream recorder"
---

<h2 class="name">NAME</h2>
<p> derrick &#8212; a simple network stream recorder </p>
<h2>SYNOPSIS</h2>
<p> <code>derrick</code> [<code>-mvVh</code>] [<code>-i</code> <i>interface</i>] [<code>-r</code> <i>file</i>] [<code>-f</code> <i>expression</i>] [<code>-l</code> <i>file</i>] [<code>-b</code> <i>bytes</i>] [<code>-t</code> <i>lines</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>derrick</code> is a simple tool for recording data streams of <font SIZE="-1">TCP</font> and <font SIZE="-1">UDP</font> traffic. It shares similarities with other network recorders, such as tcpflow and wireshark, where it is more advanced than the first and clearly inferior to the latter. </p>
<p> <code>derrick</code> has been specifically designed to monitor application-layer communication. In contrast to other tools the application data is logged in a line-based text format. Common <font SIZE="-1">UNIX</font> tools, such as grep, sed &amp; awk, can be directly applied. Even replay of recorded communication is straight forward using netcat. </p>
<p> <code>derrick</code> supports on-the-fly compression and rotation of log files. Payloads of <font SIZE="-1">TCP</font> sessions are re-assembled using libnids and can be merged or truncated. <font SIZE="-1">UDP</font> payloads are logged as-is. Details of lower network layers are omitted.</p>
<h2>OUTPUT FORMAT</h2>
<p> <code>derrick</code> outputs the monitored network traffic in a line-based text format, where each line corresponds to one recorded <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> payload. Note that <font SIZE="-1">TCP</font> payloads are re-assembled and thus not necessary match the corresponding <font SIZE="-1">TCP</font> datagrams. </p>
<p> Each line of the output has the following format: </p>
<pre>
   &lt;TIME&gt; &lt;FLAG&gt; &lt;SRC&gt; &lt;DST&gt; &lt;PAYLOAD&gt;
</pre>
<p> The different fields of the output are defined as follows</p>
<dl>
<dt>&lt;<font SIZE="-1">TIME</font>&gt;</p>
<dd> This field specifies the time at which the payload has been monitored. The time is given as standard <font SIZE="-1">UNIX</font> time and encoded as a floating-point number of seconds.</p>
<dt>&lt;<font SIZE="-1">FLAG</font>&gt;</p>
<dd> This field indicates the type of payload that has been recorded. <code>U</code> refers to a <font SIZE="-1">UDP</font> payload and <code>T</code> refers to a <font SIZE="-1">TCP</font> payload. Additionally, the beginning and end of <font SIZE="-1">TCP</font> streams are marked by <code>T+</code> and <code>T-</code>, respectively.</p>
<dt>&lt;<font SIZE="-1">SRC</font>&gt;</p>
<dd> This field specifies the source of the payload. It is a tuple of an <font SIZE="-1">IP</font> address and a port number in form of <font SIZE="-1"><code>IP:PORT</code></font>.</p>
<dt>&lt;<font SIZE="-1">DST</font>&gt;</p>
<dd> This field specifies the destination of the payload. It is a tuple of an <font SIZE="-1">IP</font> address and a port number in form of <font SIZE="-1"><code>IP:PORT</code></font>.</p>
<dt>&lt;<font SIZE="-1">PAYLOAD</font>&gt;</p>
<dd> The last field is the monitored payload. Non-printable characters are escaped using standard <font SIZE="-1">URI</font> encoding. Each non-printable characters is replaced by <tt>%XX</tt> where <font SIZE="-1">XX</font> is the character&#8217;s hexadecimal <font SIZE="-1">ASCII</font> number.</dl>
<p> An example output of <code>derrick</code> looks as follows </p>
<pre>
  05.80 T 10.100.163.103:58445 91.198.174.233:80 GET /index.html ...
</pre>
<p> The line shows a <font SIZE="-1">TCP</font> payload recorded at time 05.80, that is, 5.8 seconds after new year&#8217;s eve of 1970 ;). The payload is directed to port 80 (<font SIZE="-1">HTTP</font>) and shows the beginning of a typical <font SIZE="-1">HTTP GET</font> request. Note that whitespaces are not escaped in the payload and thus each line may seemingly have more than 5 fields. However, starting from the 5th field all following white-spaces are part of the payload.</p>
<h2>OPTIONS</h2>
<p> <code>derrick</code> supports the following command-line <i>options</i> which can be used to control the recording of network traffic.</p>
<dl>
<dt><code>-i</code> <i>interface</i></p>
<dd> Record network traffic from this <i>interface</i>. On Linux systems with 2.2 or later kernels, an interface argument of &#8220;any&#8221; can be used to capture packets from all interfaces.</p>
<dt><code>-r</code> <i>file</i></p>
<dd> Read network traffic from a dump <i>file</i> in pcap format. Dump files can be created using <code>tcpdump</code>.</p>
<dt><code>-f</code> <i>expression</i></p>
<dd> Filter network traffic using a filter <i>expression</i>. Only packets that match the expression will be recorded. Consult the man page of <code>tcpdump</code> for a description of filter expressions.</p>
<dt><code>-l</code> <i>file</i></p>
<dd> Write output to a compressed log <i>file</i> instead of stdout. This option can be used when <code>derrick</code> runs in the background. The log file will be rotated if a certain number of lines have been logged, see <code>-t</code>.</p>
<dt><code>-b</code> <i>bytes</i></p>
<dd> Record only the first <i>bytes</i> of each <font SIZE="-1">TCP</font> stream. The number of bytes is computed from incoming and outgoing <font SIZE="-1">TCP</font> payloads.</p>
<dt><code>-m</code></p>
<dd> Merge consecutive <font SIZE="-1">TCP</font> payloads in the same direction. This options comes handy if protocol messages are split over multiple <font SIZE="-1">TCP</font> payloads.</p>
<dt><code>-t</code> <i>lines</i></p>
<dd> Rotate the log file after the given number of <i>lines</i>.</p>
<dt><code>-v</code></p>
<dd> Increase the verbosity of <code>derrick</code> during recording.</p>
<dt><code>-h</code></p>
<dd> Print a brief help screen.</p>
<dt><code>-V</code></p>
<dd> Print a version and copyright string.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2011-2012 Konrad Rieck (konrad [at] mlsec.org) </p>
<p> Derrick is licensed under the new <font SIZE="-1">BSD</font> License. See the file <i></i><font SIZE="-1"><i>COPYING</i></font><i></i> in the source distribution for more information. </p>
<h2>Index</h2>
