---
title: "ip-ntable(8)"
name: "ip-ntable"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-ntable/"
description: "ip-ntable – neighbour table configuration"
---

<p>ip-ntable &#8211; neighbour table configuration</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

ntable

{ COMMAND |

    help }
</code></pre>
<p> <code>ip ntable change name</code> <i>NAME</i> [ <code>dev</code> <i>DEV</i> ] [ <code>thresh1</code> <i>VAL</i> ] [ <code>thresh2</code> <i>VAL</i> ] [ <code>thresh3</code> <i>VAL</i> ] [ <code>gc_int</code> <i>MSEC</i> ] [ <code>base_reachable</code> <i>MSEC</i> ] [ <code>retrans</code> <i>MSEC</i> ] [ <code>gc_stale</code> <i>MSEC</i> ] [ <code>delay_probe</code> <i>MSEC</i> ] [ <code>queue</code> <i>LEN</i> ] [ <code>app_probs</code> <i>VAL</i> ] [ <code>ucast_probes</code> <i>VAL</i> ] [ <code>mcast_probes</code> <i>VAL</i> ] [ <code>anycast_delay</code> <i>MSEC</i> ] [ <code>proxy_delay</code> <i>MSEC</i> ] [ <code>proxy_queue</code> <i>LEN</i> ] [ <code>locktime</code> <i>MSEC</i> ]<br />
 <code>ip ntable show</code> [ <code>dev</code> <i>DEV</i> ] [ <code>name</code> <i>NAME</i> ] </p>
<h2>Description</h2>
<p><i>ip ntable</i> controls the parameters for the neighbour tables.</p>
<h3>ip ntable show &#8211; list the ip neighbour tables</h3>
<p>This commands displays neighbour table parameters and statistics.</p>
<dl>
<dt><code>dev</code><i> DEV</i></p>
<dd>only list the table attached to this device.</p>
<dt><code>name</code><i> NAME</i></p>
<dd>only lists the table with the given name.</dl>
<h3>ip ntable change &#8211; modify table parameter</h3>
<p>This command allows modifying table parameters such as timers and queue lengths.</p>
<dl>
<dt><code>name</code><i> NAME</i></p>
<dd>the name of the table to modify.</p>
<dt><code>dev</code><i> DEV</i></p>
<dd>the name of the device to modify the table values. </p>
<h2>Examples</h2>
<p>ip ntable show dev eth0</p>
<dl>
<dd>Shows the neighbour table (IPv4 ARP and IPv6 ndisc) parameters on device eth0.</dl>
<p> ip ntable change name arp_cache queue 8 dev eth0</p>
<dl>
<dd>Changes the number of packets queued while address is being resolved from the default value (3) to 8 packets.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Manpage by Stephen Hemminger</p>
