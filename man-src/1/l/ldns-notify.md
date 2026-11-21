---

title: "ldns-notify(1)"
name: "ldns-notify"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-notify/"
description: "ldns-notify – notify DNS servers that updates are available"
---

<p> ldns-notify &#8211; notify DNS servers that updates are available</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-notify</code> [options] -z zone <i>servers</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-notify</code> sends a NOTIFY message to DNS servers. This tells them that an updated zone is available at the master servers. It can perform TSIG signatures and it can add a SOA serial number of the updated zone. If a server already has that serial number it will disregard the message. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-z zone</code></dt>
<dd> The zone that is updated. </dd>
<dt><code>-h</code></dt>
<dd> Show usage and exit </dd>
<dt><code>-v</code></dt>
<dd> Show the version and exit </dd>
<dt><code>-s serial</code></dt>
<dd> Append a SOA record indicating the serial number of the updated zone. </dd>
<dt><code>-p port</code></dt>
<dd> Use port as destination port (default the DNS port 53) for the UDP packets. </dd>
<dt><code>-y key:data</code></dt>
<dd> Use the given TSIG key and base64-data to sign the NOTIFY. Uses the hmac-md5 algorithm. </dd>
<dt><code>-d</code></dt>
<dd> Print verbose debug information. The query that is sent and the query that is received. </dd>
<dt><code>-r num</code></dt>
<dd> Specify the maximum number of retries before notify gives up trying to send the UDP packet. </dd>
</dl>
<h2>EXIT CODE</h2>
<p> The program exits with a 0 exit code if all servers replied an acknowledgement to the notify message, and a failure exit code otherwise. </p>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
