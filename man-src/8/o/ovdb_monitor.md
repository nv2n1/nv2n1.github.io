---
title: "ovdb_monitor(8)"
name: "ovdb_monitor"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovdb_monitor/"
---

ovdb_monitor - Database maintenance

<h2>Synopsis</h2>

Use <tt>&quot;ovdb_init&quot;</tt> to start ovdb_monitor

<h2>Description</h2>

When started (by <tt>&quot;ovdb_init&quot;</tt>), <tt>&quot;ovdb_monitor&quot;</tt> forks three processes that perform routine database maintenance tasks. These are: transaction checkpointing, deadlock detection, and transaction log removal. The process <font SIZE="-1">ID</font> of the parent is written to <i>pathrun/ovdb_monitor.pid</i>. This <font SIZE="-1">PID</font> is used by other <font SIZE="-1">INN</font> commands to verify that ovdb_monitor is running. 

 To shut down ovdb_monitor, send a <font SIZE="-1">TERM</font> signal to the process <font SIZE="-1">ID</font> in <i>pathrun/ovdb_monitor.pid</i> . The parent process will shut down the three children and wait for their exit before exiting itself.

<h2>History</h2>

Written by Heath Kehoe &lt;hakehoe [at] avalon.net&gt; for InterNetNews. 

 <tt>$Id:</tt> ovdb_monitor.pod 9766 2014-12-07 21:08:08Z iulius $

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-ovdb/">ovdb</a></i>(5), <i><a HREF="/docs/linux/man/8-ovdb_init/">ovdb_init</a></i>(8) 
