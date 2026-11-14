---
title: "ovdb_server(8)"
name: "ovdb_server"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovdb_server/"
---

ovdb_server - overview 'helper' server

<h2>Synopsis</h2>

Use <tt>&quot;ovdb_init&quot;</tt> to start ovdb_server

<h2>Description</h2>

If the <tt>&quot;readserver&quot;</tt> parameter in <i>ovdb.conf</i> is true, <tt>&quot;ovdb_init&quot;</tt> will start <tt>&quot;ovdb_server&quot;</tt>. 

 <tt>&quot;ovdb_server&quot;</tt> opens the overview database, and accesses it on behalf of the nnrpd reader processes. 

 To shut down ovdb_server, send a <font SIZE="-1">TERM</font> signal to the process <font SIZE="-1">ID</font> in <i>pathrun/ovdb_server.pid</i> . The parent process will shut down its children and wait for their exit before exiting itself.

<h2>History</h2>

Written by Heath Kehoe &lt;hakehoe [at] avalon.net&gt; for InterNetNews. 

 <tt>$Id:</tt> ovdb_server.pod 9766 2014-12-07 21:08:08Z iulius $

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-ovdb/">ovdb</a></i>(5), <i><a HREF="/docs/linux/man/8-ovdb_init/">ovdb_init</a></i>(8) 
