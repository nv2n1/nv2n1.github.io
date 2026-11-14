---
title: "qdrouterd(8)"
name: "qdrouterd"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qdrouterd/"
description: "qdrouterd – dispatch router"
---

<p>qdrouterd &#8211; dispatch router</p>
<h2>Synopsis</h2>
<p>qdrouterd [<i>options</i>]</p>
<h2>Description</h2>
<p>The Qpid Dispatch router (qdrouterd) is a network daemon that directs AMQP 1.0 messages between endpoints, such as messaging clients and servers.</p>
<h2>Options</h2>
<p>-c, &#8211;config=PATH (/etc/qpid-dispatch/qdrouterd.conf) : Load configuration from file at PATH </p>
<p> -I, &#8211;include=PATH (/usr/lib/qpid-dispatch/python) : Location of Dispatch&#8217;s Python library </p>
<p> -d, &#8211;daemon : Run process as a SysV-style daemon </p>
<p> -P, &#8211;pidfile : If daemon, the file for the stored daemon pid </p>
<p> -U, &#8211;user : If daemon, the username to run as </p>
<p> -h, &#8211;help : Print this help</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/qdrouterd.conf</code></p>
<dd>Configuration flie.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-qdrouterd-conf/">qdrouterd.conf</a>(5)</i>, <i><a href="/docs/linux/man/8-qdstat/">qdstat</a>(8)</i>, <i><a href="/docs/linux/man/8-qdmanage/">qdmanage</a>(8)</i> </p>
<p> <i><a rel="nofollow" href="http://qpid.apache.org/components/dispatch-router">http://qpid.apache.org/components/dispatch-router</a></i></p>
<h2>Copyright</h2>
<p>2013, Apache Qpid &lt;<a rel="nofollow" href="http://qpid.apache.org/">http://qpid.apache.org/</a>&gt;</p>
