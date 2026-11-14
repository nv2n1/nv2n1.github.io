---
title: "rwho(1)"
name: "rwho"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rwho/"
description: "rwho – who is logged in on local machines"
---

<h2 class="name">NAME</h2>
<p> <code>rwho</code> &#8211; who is logged in on local machines </p>
<h2>SYNOPSIS</h2>
<p> <code>rwho</code> [-<code>a</code> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>rwho</code> command produces output similar to who, but for all machines on the local network. If no report has been received from a machine for 11 minutes then <code>rwho</code> assumes the machine is down, and does not report users last known to be logged into that machine. </p>
<p> If a users hasn&#8217;t typed to the system for a minute or more, then <code>rwho</code> reports this idle time. If a user hasn&#8217;t typed to the system for an hour or more, then the user will be omitted from the output of <code>rwho</code> unless the &#8211;<code>a</code> flag is given.</p>
<h2>FILES</h2>
<dl>
<dt><code>/var/spool/rwho/whod.* </code></p>
<dd> information about other machines</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-finger/">finger</a>(1), <a href="/docs/linux/man/1-rup/">rup</a>(1), <a href="/docs/linux/man/1-ruptime/">ruptime</a>(1), <a href="/docs/linux/man/1-rusers/">rusers</a>(1), <a href="/docs/linux/man/1-who/">who</a>(1), <a href="/docs/linux/man/8-rwhod/">rwhod</a>(8)</p>
<h2>HISTORY</h2>
<p> The <code>rwho</code> command appeared in BSD 4.3</p>
<h2>BUGS</h2>
<p> This is unwieldy when the number of machines on the local net is large. </p>
<h2>Index</h2>
