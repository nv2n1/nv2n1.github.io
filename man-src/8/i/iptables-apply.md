---
title: "iptables-apply(8)"
name: "iptables-apply"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iptables-apply/"
description: "iptables-apply – a safer way to update iptables remotely"
---

<p>iptables-apply &#8211; a safer way to update iptables remotely</p>
<h2>Synopsis</h2>
<p><code>iptables-apply</code> [-<code>hV</code>] [<code>-t</code> <i>timeout</i>] [<code>-w</code> <i>savefile</i>] {[<i>rulesfile]|-c [runcmd]}</i></p>
<h2>Description</h2>
<p>iptables-apply will try to apply a new rulesfile (as output by iptables-save, read by iptables-restore) or run a command to configure iptables and then prompt the user whether the changes are okay. If the new iptables rules cut the existing connection, the user will not be able to answer affirmatively. In this case, the script rolls back to the previous working iptables rules after the timeout expires. </p>
<p> Successfully applied rules can also be written to savefile and later used to roll back to this state. This can be used to implement a store last good configuration mechanism when experimenting with an iptables setup script: iptables-apply -w /etc/network/iptables.up.rules -c /etc/network/iptables.up.run </p>
<p> When called as ip6tables-apply, the script will use ip6tables-save/-restore and IPv6 default values instead. Default value for rulesfile is &#8216;/etc/network/iptables.up.rules&#8217;.</p>
<h2>Options</h2>
<dl>
<dt><code>-t</code> <i>seconds</i>, <code>&#8211;timeout</code> <i>seconds</i></p>
<dd>Sets the timeout in seconds after which the script will roll back to the previous ruleset (default: 10).</p>
<dt><code>-w</code> <i>savefile</i>, <code>&#8211;write</code> <i>savefile</i></p>
<dd>Specify the savefile where successfully applied rules will be written to (default if empty string is given: /etc/network/iptables.up.rules).</p>
<dt><code>-c</code> <i>runcmd</i>, <code>&#8211;command</code> <i>runcmd</i></p>
<dd>Run command runcmd to configure iptables instead of applying a rulesfile (default: /etc/network/iptables.up.run).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage information.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version information.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></code>(8), <code><a href="/docs/linux/man/8-iptables-save/">iptables-save</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8).</p>
<h2>Legalese</h2>
<p>Original iptables-apply &#8211; Copyright 2006 Martin F. Krafft &lt;madduck [at] madduck.net&gt;. Version 1.1 &#8211; Copyright 2010 GW &lt;gw.2010 [at] tnode.com or <a rel="nofollow" href="http://gw.tnode.com/">http://gw.tnode.com/</a>&gt;. </p>
<p> This manual page was written by Martin F. Krafft &lt;madduck [at] madduck.net&gt; and extended by GW &lt;gw.2010 [at] tnode.com or <a rel="nofollow" href="http://gw.tnode.com/">http://gw.tnode.com/</a>&gt;. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the Artistic License 2.0.</p>
