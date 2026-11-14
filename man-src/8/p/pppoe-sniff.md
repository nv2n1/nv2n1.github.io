---
title: "pppoe-sniff(8)"
name: "pppoe-sniff"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoe-sniff/"
description: "pppoe-sniff – examine network for non-standard PPPoE frames"
---

<p>pppoe-sniff &#8211; examine network for non-standard PPPoE frames</p>
<h2>Synopsis</h2>
<p><code>pppoe-sniff </code>[<i>options</i>] </p>
<h2>Description</h2>
<p><code>pppoe-sniff</code> listens for likely-looking PPPoE PADR and session frames and deduces extra options required for <code><a href="/docs/linux/man/8-pppoe/">pppoe</a>(8)</code> to work. Some DSL providers seem to use non-standard frame types for PPPoE frames, and/or require a certain value in the Service-Name field. It is often easier to sniff those values from a machine which can successfully connect rather than try to pry them out of the DSL provider. To use <code>pppoe-sniff</code>, you need two computers, a DSL modem and an Ethernet hub (<i>not</i> an Ethernet switch.) If the DSL modem normally connects directly to your computer&#8217;s Ethernet card, connect it to the &quot;uplink&quot; port on the Ethernet hub. Plug two computers into normal ports on the hub. On one computer, run whatever software the DSL provider gave you on whatever operating system the DSL provider supports. On the other computer, run Linux and log in as root. On the Linux machine, put the Ethernet interface into promiscuous mode and start <code>pppoe-sniff</code>. If the ethernet interface is <i>eth0</i>, for example, type these commands: </p>
<pre> ifconfig eth0 promisc
 pppoe-sniff -I eth0</pre>
<p>On the other machine, start your DSL connection as usual. After a short time, <code>pppoe-sniff</code> should print recommendations for the value of <code>PPPOE_EXTRA</code>. Set this value in <code>/etc/ppp/pppoe.conf</code>. If <code>pppoe-sniff</code> indicates that something special is required in <code>PPPOE_EXTRA</code>, please e-mail this to <code>pppoe [at] roaringpenguin.com</code> along with the name of your ISP and the manufacturer and model number of your DSL modem. This information will be collated and provided on the PPPoE web page for users who do not have two computers. After <code>pppoe-sniff</code> finishes (or you stop it if it seems hung), remember to turn off promiscuous mode: </p>
<pre> ifconfig eth0 -promisc</pre>
<h2>Options</h2>
<dl>
<dt><code>-I </code><i>interface</i></p>
<dd>The <code>-I</code> option specifies the Ethernet interface to use. Under Linux, it is typically <i>eth0</i> or <i>eth1</i>. The interface should be &quot;up&quot; and in promiscuous mode before you start <code>pppoe-sniff</code>. </p>
<dt><code>-V</code></p>
<dd>The <code>-V</code> option causes <code>pppoe-sniff</code> to print its version number and exit. </p>
</dl>
<h2>Bugs</h2>
<p><code>pppoe-sniff</code> only works on Linux. </p>
<h2>Authors</h2>
<p><code>pppoe-sniff</code> was written by David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;. </p>
<p> The <code>pppoe</code> home page is <i><a rel="nofollow" href="http://www.roaringpenguin.com/pppoe/">http://www.roaringpenguin.com/pppoe/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe-start/">pppoe-start</a>(8), <a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a>(8), <a href="/docs/linux/man/8-pppoe-connect/">pppoe-connect</a>(8), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/5-pppoe-conf/">pppoe.conf</a>(5), <a href="/docs/linux/man/8-pppoe/">pppoe</a>(8), <a href="/docs/linux/man/8-pppoe-setup/">pppoe-setup</a>(8), <a href="/docs/linux/man/8-pppoe-status/">pppoe-status</a>(8), <a href="/docs/linux/man/8-pppoe-server/">pppoe-server</a>(8), <a href="/docs/linux/man/8-pppoe-relay/">pppoe-relay</a>(8) </p>
