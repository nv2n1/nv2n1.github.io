---
title: "xtables-nft(8)"
name: "xtables-nft"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xtables-nft/"
description: "xtables-nft — iptables using nftables kernel api"
---

<p>xtables-nft &#8212; iptables using nftables kernel api</p>
<h2>Description</h2>
<p><code>xtables-nft</code> are versions of iptables that use the nftables API. This is a set of tools to help the system administrator migrate the ruleset from <code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code>, <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a>(8)</code>, <code><a href="/docs/linux/man/8-arptables/">arptables</a>(8)</code>, and <code><a href="/docs/linux/man/8-ebtables/">ebtables</a>(8)</code> to <code><a href="/docs/linux/man/8-nftables/">nftables</a>(8)</code>. The <code>xtables-nft</code> set is composed of several commands:</p>
<dl>
<dt>&bull;</p>
<dd>iptables-nft</p>
<dt>&bull;</p>
<dd>iptables-nft-save</p>
<dt>&bull;</p>
<dd>iptables-nft-restore</p>
<dt>&bull;</p>
<dd>ip6tables-nft</p>
<dt>&bull;</p>
<dd>ip6tables-nft-save</p>
<dt>&bull;</p>
<dd>ip6tables-nft-restore</p>
<dt>&bull;</p>
<dd>arptables-nft</p>
<dt>&bull;</p>
<dd>ebtables-nft These tools use the libxtables framework extensions and hook to the nf_tables kernel subsystem using the <code>nft_compat</code> module. </p>
<h2>Usage</h2>
<p>The xtables-nft tools allow you to manage the nf_tables backend using the native syntax of <code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code>, <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a>(8)</code>, <code><a href="/docs/linux/man/8-arptables/">arptables</a>(8)</code>, and <code><a href="/docs/linux/man/8-ebtables/">ebtables</a>(8)</code>. </p>
<p> You should use the xtables-nft tools exactly the same way as you would use the corresponding original tools. </p>
<p> Adding a rule will result in that rule being added to the nf_tables kernel subsystem instead. Listing the ruleset will use the nf_tables backend as well. </p>
<p> When these tools were designed, the main idea was to replace each legacy binary with a symlink to the xtables-nft program, for example: </p>
<pre> /sbin/iptables -&gt; /usr/sbin/iptables-nft-multi
 /sbin/ip6tables -&gt; /usr/sbin/ip6tables-nft-multi
 /sbin/arptables -&gt; /usr/sbin/arptables-nft-multi
 /sbin/ebtables -&gt; /usr/sbin/ebtables-nft-multi</pre>
<p>The iptables version string will indicate whether the legacy API (get/setsockopt) or the new nf_tables api is used: </p>
<pre> iptables -V
 iptables v1.7 (nf_tables)</pre>
<h2>Differences To Legacy Iptables</h2>
<p>Because the xtables-nft tools use the nf_tables kernel API, rule additions and deletions are always atomic. Unlike iptables-legacy, iptables-nft -A .. will NOT need to retrieve the current ruleset from the kernel, change it, and re-load the altered ruleset. Instead, iptables-nft will tell the kernel to add one rule. For this reason, the iptables-legacy &#8211;wait option is a no-op in iptables-nft. </p>
<p> Use of the xtables-nft tools allow monitoring ruleset changes using the <code><a href="/docs/linux/man/8-xtables-monitor/">xtables-monitor</a>(8)</code> command. </p>
<p> When using -j TRACE to debug packet traversal to the ruleset, note that you will need to use <code><a href="/docs/linux/man/8-xtables-monitor/">xtables-monitor</a>(8)</code> in &#8211;trace mode to obtain monitoring trace events.</p>
<h2>Examples</h2>
<p>One basic example is creating the skeleton ruleset in nf_tables from the xtables-nft tools, in a fresh machine: </p>
<pre> root [at] machine:~# iptables-nft -L
 [...]
 root [at] machine:~# ip6tables-nft -L
 [...]
 root [at] machine:~# arptables-nft -L
 [...]
 root [at] machine:~# ebtables-nft -L
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
<pre> root [at] machine:~# iptables-legacy-save &gt; myruleset # reads from x_tables
 root [at] machine:~# iptables-nft-restore myruleset # writes to nf_tables</pre>
<p>or </p>
<pre> root [at] machine:~# iptables-legacy-save | iptables-translate-restore | less</pre>
<p>to see how rules would look like in the nft <code><a href="/docs/linux/man/8-nft/">nft</a>(8)</code> syntax. </p>
<h2>Limitations</h2>
<p>You should use <code>Linux kernel &gt;= 4.17</code>. </p>
<p> The CLUSTERIP target is not supported. </p>
<p> To get up-to-date information about this, please head to <code><a rel="nofollow" href="http://wiki.nftables.org/">http://wiki.nftables.org/</a></code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nft/">nft</a>(8)</code>, <code><a href="/docs/linux/man/8-xtables-translate/">xtables-translate</a>(8)</code>, <code><a href="/docs/linux/man/8-xtables-monitor/">xtables-monitor</a>(8)</code> </p>
<h2>Authors</h2>
<p>The nftables framework is written by the Netfilter project (<a rel="nofollow" href="https://www.netfilter.org">https://www.netfilter.org</a>). </p>
<p> This manual page was written by Arturo Borrero Gonzalez &lt;arturo [at] debian.org&gt; for the Debian project, but may be used by others. </p>
<p> This documentation is free/libre under the terms of the GPLv2+.</p>
