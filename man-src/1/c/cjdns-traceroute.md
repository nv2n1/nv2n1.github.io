---
title: "cjdns-traceroute(1)"
name: "cjdns-traceroute"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cjdns-traceroute/"
description: "cjdns-traceroute — trace cjdns packet routing"
---

<h2>NAME</h2>
<p> <code>cjdns-traceroute</code> &#8212; trace cjdns packet routing</p>
<h2>SYNOPSIS</h2>
<p> <code>cjdns-traceroute</code> &lt;host<i>or</i>ip&gt;</p>
<h2>DESCRIPTION</h2>
<p> Because cjdns is end to end encrypted, the standard traceroute always shows a direct connection. Cjdns-traceroute queries cjdroute to discover what route would be used to send a packet to the destination IP. Note that just as with the standard traceroute, there is no guarantee that that precise route will actually be used with the next packet. </p>
<p> Cjdns-traceroute requires admin privilege. The cjdnsadmin lib will try to read <code>/etc/cjdroute.conf</code> for the admin password. This will normally succeed only for root. Otherwise, it tries <code>~/.cjdnsadmin</code></p>
<h2>USAGE</h2>
<h2>FILES</h2>
<p> <code>~/.cjdnsadmin</code> <code>/etc/cjdroute.conf</code></p>
<h2>BUGS</h2>
<p> Cjdns-traceroute throws an ugly exception if you forget to pass an IP or have the wrong admin password.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1) <a href="/docs/linux/man/1-cjdns-traceroute/">cjdns-traceroute</a>(1) &#8212; trace cjdns packet routing =============================================</p>
<h2>SYNOPSIS</h2>
<p> <code>cjdns-traceroute</code> &lt;host<i>or</i>ip&gt;</p>
<h2>DESCRIPTION</h2>
<p> Because cjdns is end to end encrypted, the standard traceroute always shows a direct connection. Cjdns-traceroute queries cjdroute to discover what route would be used to send a packet to the destination IP. Note that just as with the standard traceroute, there is no guarantee that that precise route will actually be used with the next packet. </p>
<p> Cjdns-traceroute requires admin privilege. The cjdnsadmin lib will try to read <code>/etc/cjdroute.conf</code> for the admin password. This will normally succeed only for root. Otherwise, it tries <code>~/.cjdnsadmin</code></p>
<h2>USAGE</h2>
<h2>FILES</h2>
<p> <code>~/.cjdnsadmin</code> <code>/etc/cjdroute.conf</code></p>
<h2>BUGS</h2>
<p> Cjdns-traceroute throws an ugly exception if you forget to pass an IP or have the wrong admin password.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1) </p>
<h2>Index</h2>
