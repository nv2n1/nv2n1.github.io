---
title: "pmtime(1)"
name: "pmtime"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmtime/"
description: "pmtime – time control server for Performance Co-Pilot"
---

<h2>NAME</h2>
<p> <code>pmtime</code> &#8211; time control server for Performance Co-Pilot</p>
<h2>SYNOPSIS</h2>
<p> <code>pmtime</code> [<code>-p</code> <i>port</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmtime</code> is a graphical user interface for performance monitoring applications using the PCP infrastructure and requiring interactive time control. </p>
<p> <code>pmtime</code> is not normally invoked directly by users. Rather, it is more typical for it to be started by client applications (e.g. <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1) and <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1)). </p>
<p> There are two modes of interacting with a <code>pmtime</code> process &#8211; live host mode, and historical archive mode. In archive mode the window presents time controls suitable for manipulating the archive position, allowing full VCR control to move forwards and backwards in time at configurable rates and intervals. In live mode the <code>pmtime</code> window contains the simpler time controls suitable for live monitoring. </p>
<p> The arguments to <code>pmtime</code> are as follows:</p>
<dl>
<dt><code>-p</code></p>
<dd> <i>port</i> is the port number which <code>pmtime</code> will use for communication with its clients (monitoring applications).</dl>
<p> Note that the <code>pmtime</code> window is only made visible when explicitly requested. Multiple client applications can be connected to a single <code>pmtime</code> server &#8211; when the final client application exits, <code>pmtime</code> will also exit.</p>
<h2>ENVIRONMENT</h2>
<p> When a port number is not explicitly requested on the command line via the <code>-p</code> option, the environment variable <i>PMTIME_PORT</i> can be set to specify the port number from which available-port probing will commence when <code>pmtime</code> is searching for a port number to use. </p>
<p> The default starting port number is 43334.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), and <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1). </p>
<h2>Index</h2>
