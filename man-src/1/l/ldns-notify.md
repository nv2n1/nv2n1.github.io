---
title: "ldns-notify(1)"
name: "ldns-notify"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-notify/"
description: "ldns-notify – notify DNS servers that updates are available"
---

<h2>NAME</h2>
<p> ldns-notify &#8211; notify DNS servers that updates are available</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-notify</code> [options] -z zone <i>servers</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-notify</code> sends a NOTIFY message to DNS servers. This tells them that an updated zone is available at the master servers. It can perform TSIG signatures and it can add a SOA serial number of the updated zone. If a server already has that serial number it will disregard the message. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-z zone</code></p>
<dd> The zone that is updated. </p>
<dt><code>-h</code></p>
<dd> Show usage and exit </p>
<dt><code>-v</code></p>
<dd> Show the version and exit </p>
<dt><code>-s serial</code></p>
<dd> Append a SOA record indicating the serial number of the updated zone. </p>
<dt><code>-p port</code></p>
<dd> Use port as destination port (default the DNS port 53) for the UDP packets. </p>
<dt><code>-y key:data</code></p>
<dd> Use the given TSIG key and base64-data to sign the NOTIFY. Uses the hmac-md5 algorithm. </p>
<dt><code>-d</code></p>
<dd> Print verbose debug information. The query that is sent and the query that is received. </p>
<dt><code>-r num</code></p>
<dd> Specify the maximum number of retries before notify gives up trying to send the UDP packet. </p>
</dl>
<h2>EXIT CODE</h2>
<p> The program exits with a 0 exit code if all servers replied an acknowledgement to the notify message, and a failure exit code otherwise. </p>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
