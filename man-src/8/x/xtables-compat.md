---
title: "xtables-compat(8)"
name: "xtables-compat"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xtables-compat/"
description: "xtables-compat – compat tools to migrate from iptables to nftables"
---

<p>xtables-compat &#8211; compat tools to migrate from iptables to nftables</p>
<h2>Description</h2>
<p><code>xtables-compat</code> is set of tools to help the system administrator migrate the ruleset from <code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code>, <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a>(8)</code>, <code><a href="/docs/linux/man/8-arptables/">arptables</a>(8)</code>, and <code><a href="/docs/linux/man/8-ebtables/">ebtables</a>(8)</code> to <code><a href="/docs/linux/man/8-nftables/">nftables</a>(8)</code>. The <code>xtables-compat</code> set is composed of several commands:</p>
<dl>
<dt>&bull;</p>
<dd>iptables-compat</p>
<dt>&bull;</p>
<dd>iptables-compat-save</p>
<dt>&bull;</p>
<dd>iptables-compat-restore</p>
<dt>&bull;</p>
<dd>ip6tables-compat</p>
<dt>&bull;</p>
<dd>ip6tables-compat-save</p>
<dt>&bull;</p>
<dd>ip6tables-compat-restore</p>
<dt>&bull;</p>
<dd>arptables-compat</p>
<dt>&bull;</p>
<dd>ebtables-compat These tools use the libxtables framework extensions and hook to the nf_tables kernel subsystem using the <code>nft_compat</code> module. </p>
<h2>Usage</h2>
<p>The compat tools set allows you to manage the nf_tables backend using the native syntax of <code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code>, <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a>(8)</code>, <code><a href="/docs/linux/man/8-arptables/">arptables</a>(8)</code>, and <code><a href="/docs/linux/man/8-ebtables/">ebtables</a>(8)</code>. </p>
<p> You should use the compat tools exactly the same way as you would use the corresponding original tool. </p>
<p> Adding a rule will result in that rule being added to the nf_tables kernel subsystem instead. Listing the ruleset will use the nf_tables backend as well. </p>
<p> When these tools were designed, the main idea was to replace each legacy binary with a symlink to the corresponding compat tool, for example: </p>
<pre> /sbin/iptables --&gt; /usr/sbin/iptables-compat
 /sbin/ip6tables --&gt; /usr/sbin/ip6tables-compat
 /sbin/arptables --&gt; /usr/sbin/arptables-compat
 /sbin/ebtables --&gt; /usr/sbin/ebtables-compat</pre>
<h2>Examples</h2>
<p>One basic example is creating the skeleton ruleset in nf_tables from the compat tools, in a fresh machine: </p>
<pre> root [at] machine:~# iptables-compat -L
 [...]
 root [at] machine:~# ip6tables-compat -L
 [...]
 root [at] machine:~# arptables-compat -L
 [...]
 root [at] machine:~# ebtables-compat -L
 [...]
 root [at] machine:~# nft list ruleset
 table ip filter {
 chain INPUT {
 type filter hook input priority 0; policy accept;
 }
 chain FORWARD {
 type filter hook forward priority 0; policy accept;
 }
 chain OUTPUT {
 type filter hook output priority 0; policy accept;
 }
 }
 table ip6 filter {
 chain INPUT {
 type filter hook input priority 0; policy accept;
 }
 chain FORWARD {
 type filter hook forward priority 0; policy accept;
 }
 chain OUTPUT {
 type filter hook output priority 0; policy accept;
 }
 }
 table bridge filter {
 chain INPUT {
 type filter hook input priority -200; policy accept;
 }
 chain FORWARD {
 type filter hook forward priority -200; policy accept;
 }
 chain OUTPUT {
 type filter hook output priority -200; policy accept;
 }
 }
 table arp filter {
 chain INPUT {
 type filter hook input priority 0; policy accept;
 }
 chain FORWARD {
 type filter hook forward priority 0; policy accept;
 }
 chain OUTPUT {
 type filter hook output priority 0; policy accept;
 }
 }</pre>
<p>(please note that in fresh machines, listing the ruleset for the first time results in all tables an chain being created). To migrate your complete filter ruleset, in the case of <code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code>, you would use: </p>
<pre> root [at] machine:~# iptables-save &gt; myruleset # reads from x_tables
 root [at] machine:~# iptables-compat-restore myruleset # writes to nf_tables</pre>
<h2>Limitations</h2>
<p>You should use <code>Linux kernel &gt;= 4.2</code>. </p>
<p> Some (few) extensions may be not supported (or fully-supported) for whatever reason (for example, they were considered obsolete). </p>
<p> To get up-to-date information about this, please head to <code><a rel="nofollow" href="http://wiki.nftables.org/">http://wiki.nftables.org/</a></code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nft/">nft</a>(8)</code>, <code><a href="/docs/linux/man/8-xtables-translate/">xtables-translate</a>(8)</code> </p>
<h2>Authors</h2>
<p>The nftables framework is written by the Netfilter project (<a rel="nofollow" href="https://www.netfilter.org">https://www.netfilter.org</a>). </p>
<p> This manual page was written by Arturo Borrero Gonzalez &lt;arturo [at] debian.org&gt; for the Debian project, but may be used by others. </p>
<p> This documentation is free/libre under the terms of the GPLv2+.</p>
