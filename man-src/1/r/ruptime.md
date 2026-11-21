---

title: "ruptime(1)"
name: "ruptime"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ruptime/"
description: "ruptime – show host status of local machines"
---

<p> <code>ruptime</code> &#8211; show host status of local machines </p>
<h2>SYNOPSIS</h2>
<p> <code>ruptime</code> [-<code>alrtu</code> ] [-<code>n=length</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ruptime</code> gives a status line like <i>uptime</i> for each machine on the local network; these are formed from packets broadcast by each host on the network once a minute. </p>
<p> Machines for which no status report has been received for 11 minutes are shown as being down. </p>
<p> Options:</p>
<dl>
<dt><code>-a</code></dt>
<dd> Users idle an hour or more are not counted unless the &#8211;<code>a</code> flag is given.</dd>
<dt><code>-l</code></dt>
<dd> Sort by load average.</dd>
<dt><code>-r</code></dt>
<dd> Reverses the sort order.</dd>
<dt><code>-t</code></dt>
<dd> Sort by uptime.</dd>
<dt><code>-u</code></dt>
<dd> Sort by number of users.</dd>
<dt><code>-n=length</code></dt>
<dd> Specify hostname length in output.</dd></dl>
<p> The default listing is sorted by host name.</p>
<h2>FILES</h2>
<dl>
<dt><code>/var/spool/rwho/whod.* </code></dt>
<dd> data files</dd></dl>
<h2>SEE ALSO</h2>
<p> rup(1), <a href="/docs/linux/man/1-rwho/">rwho</a>(1), <a href="/docs/linux/man/1-uptime/">uptime</a>(1), <a href="/docs/linux/man/8-rwhod/">rwhod</a>(8)</p>
<h2>HISTORY</h2>
<p> <code>Ruptime</code> appeared in BSD 4.2 </p>
