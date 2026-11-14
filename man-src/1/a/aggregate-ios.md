---
title: "aggregate-ios(1)"
name: "aggregate-ios"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aggregate-ios/"
description: "aggregate-ios – optimise a concatenated set of cisco/IOS prefix filters to help make them nice and short."
---

<h2>NAME</h2>
<p> <code>aggregate-ios</code> &#8211; optimise a concatenated set of cisco/IOS prefix filters to help make them nice and short. </p>
<h2>SYNOPSIS</h2>
<p> <code>aggregate-ios &lt;source_config &gt;optimised_config</code> </p>
<h2>DESCRIPTION</h2>
<p> Takes cisco IOS configuration on stdin, and optimises any prefix filters found using <code><a href="/docs/linux/man/1-aggregate/">aggregate</a>(1).</code> Optimised filters are produced on stdout. </p>
<h2>OPTIONS</h2>
<p> None. </p>
<h2>DIAGNOSTICS</h2>
<p> Any diagnostics produced by <code><a href="/docs/linux/man/1-aggregate/">aggregate</a>(1)</code> are passed through on stderr. </p>
<h2>EXAMPLES</h2>
<p> The following configuration fragment: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65530 description Foo, Inc<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65530 permit 10.1.0.0/16<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65530 permit 10.2.0.0/16<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65530 permit 10.2.1.0/24<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65530 permit 10.3.0.0/16<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65531 description Bar.Com<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65531 seq 5 permit 192.168.1.0/24<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65531 seq 10 permit 192.168.2.0/24<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65531 seq 15 permit 192.168.0.0/19 </code> </p>
<p> is optimised as follows: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65530 permit 10.1.0.0/16 le 24<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65530 permit 10.2.0.0/15 le 24<br />
&nbsp;<wbr>&nbsp;<wbr>ip prefix-list AS65531 permit 192.168.0.0/19 le 24 </code> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-aggregate/">aggregate</a>(1) </p>
<h2>HISTORY</h2>
<p> <code>Aggregate-ios</code> was written by Joe Abley &lt;jabley [at] mfnx.net&gt;. </p>
<h2>BUGS</h2>
<p> All those in <code><a href="/docs/linux/man/1-aggregate/">aggregate</a>(1)</code> and then some :) </p>
<h2>Index</h2>
