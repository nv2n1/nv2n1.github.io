---
title: "pppoe(5)"
name: "pppoe"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pppoe/"
description: "ifcfg-ppp0 – Configuration file used by"
---

<p>ifcfg-ppp0 &#8211; Configuration file used by <code></p>
<p><a href="/docs/linux/man/8-pppoe-start/">pppoe-start</a></code>(8), <code><a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a></code>(8), <code><a href="/docs/linux/man/8-pppoe-status/">pppoe-status</a>(8)</code> and <code><a href="/docs/linux/man/8-pppoe-connect/">pppoe-connect</a></code>(8). </p>
<h2>Description</h2>
<p><code>/etc/sysconfig/network-scripts/ifcfg-ppp0</code> is a shell script which contains configuration information for Roaring Penguin&#8217;s PPPoE scripts. Note that <code>pppoe.conf</code> is used only by the various pppoe-* shell scripts, not by <code>pppoe</code> itself. <code>ifcfg-ppp0</code> consists of a sequence of shell variable assignments. The variables and their meanings are:</p>
<dl>
<dt><code>ETH</code></p>
<dd>The Ethernet interface connected to the DSL modem (for example, eth0).</p>
<dt><code>USER</code></p>
<dd>The PPPoE user-id (for example, b1xxnxnx [at] sympatico.ca).</p>
<dt><code>SERVICENAME</code></p>
<dd>If this is not blank, then it is passed with the <code>-S</code> option to <code>pppoe</code>. It specifies a service name to ask for. Usually, you should leave it blank.</p>
<dt><code>ACNAME</code></p>
<dd>If this is not blank, then it is passed with the <code>-C</code> option to <code>pppoe</code>. It specifies the name of the access concentrator to connect to. Usually, you should leave it blank.</p>
<dt><code>DEMAND</code></p>
<dd>If set to a number, the link is activated on demand and brought down after after <code>DEMAND</code> seconds. If set to <code>no</code>, the link is kept up all the time rather than being activated on demand.</p>
<dt><code>DNSTYPE</code></p>
<dd>One of <code>NOCHANGE</code>, <code>SPECIFY</code> or <code>SERVER</code>. If set to NOCHANGE, <code>pppoe-connect</code> will not adjust the DNS setup in any way. If set to SPECIFY, it will re-write /etc/resolv.conf with the values of DNS1 and DNS2. If set to <code>SERVER</code>, it will supply the <i>usepeerdns</i> option to <code>pppd</code>, and make a symlink from /etc/resolv.conf to /etc/ppp/resolv.conf.</p>
<dt><code>DNS1, DNS2</code></p>
<dd>IP addresses of DNS servers if you use DNSTYPE=SPECIFY.</p>
<dt><code>USERCTL</code></p>
<dd>If the line <code>USERCTL=yes</code> (exactly like that; no whitespace or comments) appears in the configuration file, then <code>/sbin/ifup</code> will allow non-root users to bring the conneciton up or down.</p>
<dt><code>USEPEERDNS</code></p>
<dd>If set to &quot;yes&quot;, then <code>pppoe-connect</code> will supply the <i>usepeerdns</i> option to <code>pppd</code>, which causes it to obtain DNS server addresses from the peer and create a new <code>/etc/resolv.conf</code> file. Otherwise, <code>pppoe-connect</code> will not supply this option, and <code>pppd</code> will not modify <code>/etc/resolv.conf</code>.</p>
<dt><code>CONNECT_POLL</code></p>
<dd>How often (in seconds) <code>pppoe-start</code> should check to see if a new PPP interface has come up. If this is set to 0, the <code>pppoe-start</code> simply initiates the PPP session, but does not wait to see if it comes up successfully.</p>
<dt><code>CONNECT_TIMEOUT</code></p>
<dd>How long (in seconds) <code>pppoe-start</code> should wait for a new PPP interface to come up before concluding that <code>pppoe-connect</code> has failed and killing the session.</p>
<dt><code>PING</code></p>
<dd>A character which is echoed every <code>CONNECT_POLL</code> seconds while <code>pppoe-start</code> is waiting for the PPP interface to come up.</p>
<dt><code>FORCEPING</code></p>
<dd>A character which is echoed every <code>CONNECT_POLL</code> seconds while <code>pppoe-start</code> is waiting for the PPP interface to come up. Similar to <code>PING</code>, but the character is echoed even if <code>pppoe-start</code>&#8216;s standard output is not a tty.</p>
<dt><code>PIDFILE</code></p>
<dd>A file in which to write the process-ID of the pppoe-connect process (for example, <code>/var/run/pppoe.pid</code>). Two additional files ($PIDFILE.pppd and $PIDFILE.pppoe) hold the process-ID&#8217;s of the <code>pppd</code> and <code>pppoe</code> processes, respectively.</p>
<dt><code>SYNCHRONOUS</code></p>
<dd>An indication of whether or not to use synchronous PPP (<code>yes</code> or <code>no</code>). Synchronous PPP is safe on Linux machines with the n_hdlc line discipline. (If you have a file called &quot;n_hdlc.o&quot; in your modules directory, you have the line discipline.) It is <i>not recommended</i> on other machines or on Linux machines without the n_hdlc line discipline due to some known and unsolveable race conditions in a user-mode client.</p>
<dt><code>CLAMPMSS</code></p>
<dd>The value at which to &quot;clamp&quot; the advertised MSS for TCP sessions. The default of 1412 should be fine.</p>
<dt><code>LCP_INTERVAL</code></p>
<dd>How often (in seconds) <code>pppd</code> sends out LCP echo-request packets.</p>
<dt><code>LCP_FAILURE</code></p>
<dd>How many unanswered LCP echo-requests must occur before <code>pppd</code> concludes the link is dead.</p>
<dt><code>PPPOE_TIMEOUT</code></p>
<dd>If this many seconds elapse without any activity seen by <code>pppoe</code>, then <code>pppoe</code> exits.</p>
<dt><code>FIREWALL</code></p>
<dd>One of NONE, STANDALONE or MASQUERADE. If NONE, then <code>pppoe-connect</code> does not add any firewall rules. If STANDALONE, then it clears existing firewall rules and sets up basic rules for a standalone machine. If MASQUERADE, then it clears existing firewall rules and sets up basic rules for an Internet gateway. If you run services on your machine, these simple firewall scripts are inadequate; you&#8217;ll have to make your own firewall rules and set FIREWALL to NONE.</p>
<dt><code>PPPOE_EXTRA</code></p>
<dd>Any extra arguments to pass to <code>pppoe</code></p>
<dt><code>PPPD_EXTRA</code></p>
<dd>Any extra arguments to pass to <code>pppd</code></p>
<dt><code>LINUX_PLUGIN</code></p>
<dd>If non-blank, the full path of the Linux kernel-mode PPPoE plugin (typically <code>/etc/ppp/plugins/rp-pppoe.so</code>.) This forces <code>pppoe-connect</code> to use kernel-mode PPPoE on Linux 2.4.x systems. This code is experimental and unsupported. Use of the plugin causes <code>pppoe-connect</code> to ignore CLAMPMSS, PPPOE_EXTRA, SYNCHRONOUS and PPPOE_TIMEOUT.  By using different configuration files with different PIDFILE settings, you can manage multiple PPPoE connections. Just specify the configuration file as an argument to <code>pppoe-start</code> and <code>pppoe-stop</code>. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe/">pppoe</a>(8), <a href="/docs/linux/man/8-pppoe-connect/">pppoe-connect</a>(8), <a href="/docs/linux/man/8-pppoe-start/">pppoe-start</a>(8), <a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a>(8), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/8-pppoe-setup/">pppoe-setup</a>(8), <a href="/docs/linux/man/8-pppoe-wrapper/">pppoe-wrapper</a>(8) </p>
