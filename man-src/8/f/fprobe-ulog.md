---
title: "fprobe-ulog(8)"
name: "fprobe-ulog"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fprobe-ulog/"
description: "fprobe-ulog – a NetFlow probe"
---

<p>fprobe-ulog &#8211; a NetFlow probe</p>
<h2>Synopsis</h2>
<p><code>fprobe-ulog</code> [<i>options</i>] <i>remote:port[/[local][/type]] &#8230;</i> </p>
<h2>Description</h2>
<p><code>fprobe-ulog</code> &#8211; libipulog-based tool that collect network traffic data and emit it as NetFlow flows towards the specified collector. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Display short help</p>
<dt><code>-U </code><i>&lt;mask&gt;</i></p>
<dd>ULOG group bitwise mask. [default=1]</p>
<dt><code>-s </code><i>&lt;seconds&gt;</i></p>
<dd>How often scan for expired flows. [default=5]</p>
<dt><code>-g </code><i>&lt;seconds&gt;</i></p>
<dd>Fragmented flow lifetime. [default=30]</p>
<dt><code>-d </code><i>&lt;seconds&gt;</i></p>
<dd>Idle flow lifetime (inactive timer). [default=60]</p>
<dt><code>-e </code><i>&lt;seconds&gt;</i></p>
<dd>Active flow lifetime (active timer). [default=300]</p>
<dt><code>-n </code><i>&lt;version&gt;</i></p>
<dd>NetFlow version for use (1, 5, 7). [default=5]</p>
<dt><code>-a </code><i>&lt;address&gt;</i></p>
<dd>Use <i>address</i> as source for NetFlow flow.</p>
<dt><code>-X </code><i>&lt;rule[,&#8230;]&gt;</i></p>
<dd>Comma separated list of interface name to SNMP-index conversion rules. Each <i>rule</i> consists of <i>interface base name</i> and <i>SNMP-index base</i> separated by colon (e.g. ppp:200). Final SNMP-index is sum of corresponding <i>SNMP-index base</i> and <i>interface number</i>.<br />
 In the above example SNMP-index of interface ppp11 is 211. </p>
<p> If interface name did not fit to any of conversion rules then SNMP-index will be taken from kernel.</p>
<dt><code>-M</code></p>
<dd>Use the netfilter mark as Type Of Service value.</p>
<dt><code>-b </code><i>&lt;flows&gt;</i></p>
<dd>Memory bulk size. [default=200 or 10000]<br />
 Note that maximum and default values depends on compiling options (<i>&#8211;with-membulk</i> parameter).</p>
<dt><code>-m </code><i>&lt;kilobytes&gt;</i></p>
<dd>Memory limit for flows cache (0=no limit). [default=0]</p>
<dt><code>-q </code><i>&lt;flows&gt;</i></p>
<dd>Pending queue length. [default=100]<br />
 Each captured packet at first puts into special buffer called `pending queue&#8217;. Purpose of this buffer is to separate most time-critical packet capture thread from other.</p>
<dt><code>-B </code><i>&lt;kilobytes&gt;</i></p>
<dd>Kernel capture buffer size (0=don&#8217;t change). [default=0]<br />
 Increase kernel capture buffer size is most adequate way to prevent packets loss.<br />
 Note that maximum allowed size of the buffer in Linux limited and generally relatively small, so it should need to change the maximum: sysctl -w net/core/rmem_max=4194304</p>
<dt><code>-r </code><i>&lt;priority&gt;</i></p>
<dd>Real-time priority (0=disabled). [default=0]<br />
 If parameter greater then zero <code>fprobe-ulog</code> will use real-time scheduling policy to prevent packets loss. Note that possible values for this option depends on operating system.</p>
<dt><code>-t </code><i>&lt;B:N&gt;</i></p>
<dd>Emitting rate limit (0:0=no limit). [default=0:0]<br />
 Produce <i>N</i> nanosecond delay after each <i>B</i> bytes sent. This option may be useful with slow interfaces and slow collectors. Note that the suspension time may be longer than requested because the argument value is rounded up to an integer multiple of the sleep resolution (it depends on operating system and hardware) or because of the scheduling of other activity by the system.<br />
 See BUGS section.</p>
<dt><code>-c </code><i>&lt;directory&gt;</i></p>
<dd>Directory to chroot to.</p>
<dt><code>-u </code><i>&lt;user&gt;</i></p>
<dd>User to run as.</p>
<dt><code>-v </code><i>&lt;level&gt;</i></p>
<dd>Maximum displayed log level. (0=EMERG, 1=ALERT, 2=CRIT, 3=ERR, 4=WARNING, 5=NOTICE, 6=INFO, 7=DEBUG) [default=6]</p>
<dt><code>-l </code><i>&lt;[dst][:id]&gt;</i></p>
<dd>Log destination (0=none, 1=syslog, 2=stdout, 3=both) and log/pidfile identifier. [default=1]<br />
 This option allows to select opportune log destination and process identifier. The identifier helps to distinguish pidfile and logs of one <code>fprobe-ulog</code> process from other.<br />
 Note that if log destination contains `<i>stdout</i>&#8216; (equal 2 or 3) <code>fprobe-ulog</code> will run in foreground.</p>
<dt><code>remote:port/local/type</code></p>
<dd>Parameters <i>remote</i> and <i>port</i> are respectively define address and port of the NetFlow collector.<br />
 The <i>local</i> parameter allows binding certain local IP address with specified collector. If the parameter is omitted the value (if any) of <i>-a</i> option will be used.<br />
 The <i>type</i> parameter determines emitting behavior. It may be `m&#8217; for mirroring (by default) and `r&#8217; for collectors round-robin rotating.<br />
 You may specify multiple collectors. </p>
</dl>
<h2>Examples</h2>
<p><code>fprobe-ulog -Xeth:100,ppp:200 localhost:2055</code> Reasonable configuration to run under heavy load:<br />
 <code>fprobe-ulog -B4096 -r2 -q10000 -t10000:10000000 localhost:2055</code> Send packets to collector at 10.1.1.1:2055 and distribute them between collectors at 10.1.1.2:2055 and at 10.1.1.3:2055 on a round-robin basis:<br />
 <code>fprobe-ulog 10.1.1.1:2055 10.1.1.2:2055//r 10.1.1.3:2055//r</code> </p>
<h2>Bugs</h2>
<p><code>Slow interfaces and slow collectors.</code><br />
 There are may be problems with slow interfaces and slow collectors. It effects as emitted packets loss. On the one hand silent non-blocking sendto() implementation can&#8217;t guarantee that packet was really sent to collector &#8211; it may be dropped by kernel due to outgoing buffer shortage (slow interface&#8217;s problem) and on the other hand packet may be dropped on collector&#8217;s machine due the similar reason &#8211; incoming buffer shortage (slow collector&#8217;s problem).<br />
 Use <i>-t</i> option as workaround for this issue. <code>Locally originated packets and their timestamps.</code><br />
 Locally originated packets does not contains valid timestamps. Therefore <code>fprobe-ulog</code> fill timestamp by itself on act of receive such packet. Unfortunately, between capturing packet by netfilter code and receiving it by <code>fprobe-ulog</code> may occur certain lags, thus timestamps of locally originated packets generally inexact.<br />
 It is possible to fix this problem entirely by trivial kernel patch (see contrib/ipt_ULOG.patch). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code><br />
 <code><a rel="nofollow" href="http://freshmeat.net/projects/ulogd">http://freshmeat.net/projects/ulogd</a></code><br />
 <code><a rel="nofollow" href="http://www.cisco.com/go/netflow">http://www.cisco.com/go/netflow</a></code> </p>
