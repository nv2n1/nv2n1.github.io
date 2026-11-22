---
title: "tc-simple(8)"
name: "tc-simple"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-simple/"
description: "simple – basic example action"
---

<p>simple &#8211; basic example action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action simple</code> [ <code>sdata</code><i> STRING</i> ] [ <code>index</code><i> INDEX</i> ] [ <i>CONTROL</i> ] </p>
<pre><code>CONTROL := {
    reclassify | pipe | drop | continue | ok }
</code></pre>
<h2>Description</h2>
<p>This is a pedagogical example rather than an actually useful action. Upon every access, it prints the given <i>STRING</i> which may be of arbitrary length.</p>
<h2>Options</h2>
<dl>
<dt><code>sdata</code><i> STRING</i></dt>
<dd>The actual string to print.</dd>
<dt><code>index</code><i> INDEX</i></dt>
<dd>Optional action index value.</dd>
<dt><i>CONTROL</i></dt>
<dd>Indicate how <code>tc</code> should proceed after executing the action. For a description of the possible <i>CONTROL</i> values, see <code><a href="/docs/linux/man/8-tc-actions/">tc-actions</a></code>(8).</dd></dl>
<h2>Examples</h2>
<p>The following example makes the kernel yell &quot;Incoming ICMP!&quot; every time it sees an incoming ICMP on eth0. Steps are:</p>
<dl>
<dt>1)</dt>
<dd>Add an ingress qdisc point to eth0</dd>
<dt>2)</dt>
<dd>Start a chain on ingress of eth0 that first matches ICMP then invokes the simple action to shout.</dd>
<dt>3)</dt>
<dd>display stats and show that no packet has been seen by the action</dd>
<dt>4)</dt>
<dd>Send one ping packet to google (expect to receive a response back)</dd>
<dt>5)</dt>
<dd>grep the logs to see the logged message</dd>
<dt>6)</dt>
<dd>display stats again and observe increment by 1 hadi [at] noma1$ ping -c 1 www.google.ca</dd>
<p>PING www.google.ca (74.125.225.120) 56(84) bytes of data.</p>
<p>64 bytes from ord08s08-in-f24.1e100.net (74.125.225.120): icmp_req=1 ttl=53 time=31.3 ms<br/>
&#8212; www.google.ca ping statistics &#8212;</p>
<p>1 packets transmitted, 1 received, 0% packet loss, time 0ms</p>
<p>rtt min/avg/max/mdev = 31.316/31.316/31.316/0.000 ms<br/>
&nbsp;<wbr>&nbsp;hadi [at] noma1:$&nbsp;sudo tc -s filter ls&nbsp;<wbr>&nbsp;dev eth0 parent ffff:<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;filter protocol ip pref 5 u32<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;filter protocol ip pref 5 u32 fh 800: ht divisor 1<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;filter protocol ip pref 5 u32 fh 800::800 order 2048 key ht 800 bkt 0 flowid 1:1<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match 00010000/00ff0000 at 8 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action order 1: Simple &lt;Incoming ICMP&gt;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> index 4 ref 1 bind 1 installed 29 sec used 29 sec<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> Action statistics:<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Sent 0 bytes 0 pkt (dropped 0, overlimits 0 requeues 0)<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>backlog 0b 0p requeues 0</p>
<pre><code>hadi [at] noma1$ ping -c 1 www.google.ca
PING www.google.ca (74.125.225.120) 56(84) bytes of data.
64 bytes from ord08s08-in-f24.1e100.net (74.125.225.120): icmp_req=1 ttl=53 time=31.3 ms
--- www.google.ca ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 31.316/31.316/31.316/0.000 ms</code></pre>
<p>&nbsp;<wbr>&nbsp;hadi [at] noma1$&nbsp;dmesg | grep simple<br/>
&nbsp;<wbr>&nbsp;[135354.473951]&nbsp;simple: Incoming ICMP_1<br/>
&nbsp;<wbr>&nbsp;hadi [at] noma1$&nbsp;sudo tc/tc -s filter ls&nbsp;<wbr>&nbsp;dev eth0 parent ffff:<br/>
&nbsp;<wbr>&nbsp;filter protocol ip pref 5 u32<br/>
&nbsp;<wbr>&nbsp;filter protocol ip pref 5 u32 fh 800: ht divisor 1<br/>
&nbsp;<wbr>&nbsp;filter protocol ip pref 5 u32 fh 800::800 order 2048 key ht 800 bkt 0 flowid 1:1<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match 00010000/00ff0000 at 8 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action order 1: Simple &lt;Incoming ICMP&gt;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> index 4 ref 1 bind 1 installed 206 sec used 67 sec<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Action statistics:<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Sent 84 bytes 1 pkt (dropped 0, overlimits 0 requeues 0)<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>backlog 0b 0p requeues 0
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) <code><a href="/docs/linux/man/8-tc-actions/">tc-actions</a></code>(8) </p>
</p>