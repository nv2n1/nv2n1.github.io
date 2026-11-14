---
title: "ttylinkd(8)"
name: "ttylinkd"
section: "8"
letter: "t"
url: "/docs/linux/man/8-ttylinkd/"
description: "ttylinkd – TTYlink daemon for AX.25, NET/ROM, ROSE and IP."
---

<p>ttylinkd &#8211; TTYlink daemon for AX.25, NET/ROM, ROSE and IP.</p>
<h2>Synopsis</h2>
<p><code>ttylinkd [-hv] [-c callsign] [-f file]</code></p>
<h2>Description</h2>
<p><code>ttylinkd</code> is a simple daemon that allows incoming ttylink calls to be routed through to Linux&#8217;s normal <a href="/docs/linux/man/8-talkd/">talkd</a>(8) system and provides a pipe between the two. </p>
<p> <code>ttylinkd </code> is usually setup to be spawned from <a href="/docs/linux/man/8-ax25d/">ax25d</a>(8) or <a href="/docs/linux/man/8-inetd/">inetd</a>(8) but can, since version 0.03, be used on the command line, although <a href="/docs/linux/man/1-talk/">talk</a>(1) is a much better idea for interactive users. </p>
<p> Use <a href="/docs/linux/man/1-splitscreen/">splitscreen</a>(1) for outgoing ttylink sessions.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></p>
<dd>Display the version.</p>
<dt><code>-h</code></p>
<dd>Display some help and information on it.</p>
<dt><code>-c callsign</code></p>
<dd>Disable callsign checking and use the given callsign for a name for this end of the link.</p>
<dt><code>-f file</code></p>
<dd>Use &lt;file&gt; for the configuration file, instead of the default /etc/ax25/ttylinkd.conf</dl>
<h2>Files</h2>
<p>/etc/ax25/ttylinkd.conf the configuration file for ttylinkd</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-talk/">talk</a></code>(1), <code><a href="/docs/linux/man/1-splitscreen/">splitscreen</a></code>(1), <code><a href="/docs/linux/man/5-ttylinkd-conf/">ttylinkd.conf</a></code>(5), <code><a href="/docs/linux/man/8-ax25d/">ax25d</a></code>(8), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-talkd/">talkd</a></code>(8).</p>
<h2>Bugs</h2>
<p>There is still some need for some checking of who is still logged on. </p>
<p> The daemon may hang if you disconnect from it strangely. </p>
<p> There is no real way of working out what is going on with talkd. </p>
<p> If you do not have a talk daemon going on the specified host then the program will tend to sit there and do nothing.</p>
<h2>Author</h2>
<p>Craig Small VK2XLZ &lt;csmall [at] small.dropbear.id.au&gt;</p>
