---
title: "estmaster(1)"
name: "estmaster"
section: "1"
letter: "e"
url: "/docs/linux/man/1-estmaster/"
description: "estmaster – master process of node servers"
---

<h2 class="name">NAME</h2>
<p> estmaster &#8211; master process of node servers</p>
<h2>SYNOPSIS</h2>
<p> <code>estmaster init [-ex] rootdir</code> </p>
<p> <code>estmaster start [-bg] [-ro] [-st] rootdir</code> </p>
<p> <code>estmaster stop rootdir</code> </p>
<p> <code>estmaster unittest rootdir</code> </p>
<p> <code>estmaster crypt key [hash]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>estmaster</code> is an aggregation of sub commands. The name of a sub command is specified by the first argument. Other arguments are parsed according to each sub command. The argument <i>rootdir</i> specifies the server root directory which contains configuration file and so on.</p>
<dl>
<dt><code>estmaster init [-ex] rootdir</code></p>
<dd> Create the server root directory.<br />
 If <code>-ex</code> is specified, some users and some nodes are set for example. By default, only a super user whose name and password are both &quot;admin&quot; is set.</p>
<dt><code>estmaster start [-bg] [-ro] [-st] rootdir</code></p>
<dd> Start the node master.<br />
 If <code>-bg</code> is specified, the server runs in background as a daemon process.<br />
 If <code>-ro</code> is specified, the server runs in read-only mode regardless of the configuration.<br />
 If <code>-st</code> is specified, the server runs in single thread mode.</p>
<dt><code>estmaster stop rootdir</code></p>
<dd> Stop the running node master.</p>
<dt><code>estmaster unittest rootdir</code></p>
<dd> Perform unit tests.</p>
<dt><code>estmaster crypt key [hash]</code></p>
<dd> Output an encrypted string of a string.<br />
 <i>key</i> specifies a target string.<br />
 If <i>hash</i> is specified, it checks whether the key and the hash matches.</dl>
<p> All sub commands return 0 if the operation is success, else return 1. A running node master finishes with closing the database when it catches the signal 1 (SIGHUP), 2 (SIGINT), 3 (SIGQUIT), or 15 (SIGTERM). Moreover, when a node master running as a daemon catches the signal 1 (SIGHUP), the process is re-start and re-read the configuration files. </p>
<p> A running node server should be finished by valid means by command line or via network. Otherwise, the index may be broken. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-estconfig/">estconfig</a></code>(1), <code><a href="/docs/linux/man/1-estcmd/">estcmd</a></code>(1), <code><a href="/docs/linux/man/1-estcall/">estcall</a></code>(1), <code><a href="/docs/linux/man/1-estwaver/">estwaver</a></code>(1), <code><a href="/docs/linux/man/3-estraier/">estraier</a></code>(3), <code><a href="/docs/linux/man/3-estnode/">estnode</a></code>(3) </p>
<p> Please see <code><a rel="nofollow" href="http://hyperestraier.sourceforge.net/nguide-en.html">http://hyperestraier.sourceforge.net/nguide-en.html</a></code> for detail. </p>
<h2>Index</h2>
