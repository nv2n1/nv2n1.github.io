---
title: "kannel(8)"
name: "kannel"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kannel/"
description: "bearerbox, wapbox, smsbox – Parts of Kannel, the WAP and SMS gateway"
---

<p>bearerbox, wapbox, smsbox &#8211; Parts of Kannel, the WAP and SMS gateway</p>
<h2>Synopsis</h2>
<p><code>bearerbox</code> <i></i>[<i>options</i>&#8230;<i>] [</i>conffile<i>]</i> </p>
<p> <code>wapbox</code> <i></i>[<i>options</i>&#8230;<i>] [</i>conffile<i>]</i> </p>
<p> <code>smsbox</code> <i></i>[<i>options</i>&#8230;<i>] [</i>conffile<i>]</i></p>
<h2>Description</h2>
<p><i>Kannel</i> is an WAP and SMS gateway. WAP is short for Wireless Application Protocol, and is used to implement hypertext based services on mobile phones. SMS is short for Short Message Service, and is used to send and recive short (up to 160 characters) text messages with mobile phones. SMS can also be used to implement simple text based services on mobile phones. </p>
<p> Kannel consists of three programs, usually run as daemons: <code>bearerbox</code>, <code>wapbox</code>, and <code>smsbox</code>. They implement the connection to the phone (SMS or UDP), the WAP protocol stack, and the SMS based services, respectively. </p>
<p> For more information, see <code><a rel="nofollow" href="http://www.kannel.org">http://www.kannel.org</a></code> or <code>file://usr/doc/kannel/</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-run_kannel_box/">run_kannel_box</a></code>(8), <code><a href="/docs/linux/man/1-seewbmp/">seewbmp</a></code>(1). </p>
