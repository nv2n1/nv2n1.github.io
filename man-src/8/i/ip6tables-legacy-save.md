---
title: "ip6tables-legacy-save(8)"
name: "ip6tables-legacy-save"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip6tables-legacy-save/"
description: "xtables-legacy — iptables using old getsockopt/setsockopt-based kernel api"
---

<p>xtables-legacy &#8212; iptables using old getsockopt/setsockopt-based kernel api</p>
<h2>Description</h2>
<p><code>xtables-legacy</code> are the original versions of iptables that use old getsockopt/setsockopt-based kernel interface. This kernel interface has some limitations, therefore iptables can also be used with the newer nf_tables based API. See <code><a href="/docs/linux/man/8-xtables-nft/">xtables-nft</a>(8)</code> for information about the xtables-nft variants of iptables. </p>
<h2>Usage</h2>
<p>The xtables-legacy-multi binary can be linked to the traditional names: </p>
<pre> /sbin/iptables -&gt; /sbin/iptables-legacy-multi
 /sbin/ip6tables -&gt; /sbin/ip6tables-legacy-multi
 /sbin/iptables-save -&gt; /sbin/ip6tables-legacy-multi
 /sbin/iptables-restore -&gt; /sbin/ip6tables-legacy-multi</pre>
<p>The iptables version string will indicate whether the legacy API (get/setsockopt) or the new nf_tables API is used: </p>
<pre> iptables -V
 iptables v1.7 (legacy)</pre>
<h2>Limitations</h2>
<p>When inserting a rule using iptables -A or iptables -I, iptables first needs to retrieve the current active ruleset, change it to include the new rule, and then commit back the result. This means that if two instances of iptables are running concurrently, one of the updates might be lost. This can be worked around partially with the &#8211;wait option. </p>
<p> There is also no method to monitor changes to the ruleset, except periodically calling iptables-legacy-save and checking for any differences in output. </p>
<p> <code><a href="/docs/linux/man/8-xtables-monitor/">xtables-monitor</a>(8)</code> will need the <code><a href="/docs/linux/man/8-xtables-nft/">xtables-nft</a>(8)</code> versions to work, it cannot display changes made using the <code>iptables-legacy</code> tools.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xtables-nft/">xtables-nft</a>(8)</code>, <code><a href="/docs/linux/man/8-xtables-translate/">xtables-translate</a>(8)</code> </p>
<h2>Authors</h2>
<p>Rusty Russell originally wrote iptables, in early consultation with Michael Neuling.</p>
