---
title: "filebench(1)"
name: "filebench"
section: "1"
letter: "f"
url: "/docs/linux/man/1-filebench/"
description: "filebench – interprets WML script and generates appropriate filesystem workload"
---

<h2>NAME</h2>
<p> filebench &#8211; interprets WML script and generates appropriate filesystem workload</p>
<h2>SYNOPSIS</h2>
<p> <code>filebench [-f &lt;filename&gt;] [-h]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Filebench</code> is a file system and storage benchmark that allows to generate a large variety of workloads. Unlike typical benchmarks it is very flexible and allows to minutely specify (any) applications&#8217; behaviour using extensive Workload Model Language (WML). Filebench uses loadable workload personalities to allow easy emulation of complex applications (e.g., mail, web, file, and database servers). Filebench is quick to set up and easy to use compared to deploying real applications. It is also a handy tool for micro-benchmarking. </p>
<p> <code>Filebench</code> includes many features to facilitate file system benchmarking:</p>
<dl>
<dt>&bull;</p>
<dd> Multiple workload types support via loadable personalities</p>
<dt>&bull;</p>
<dd> Ships with more than 40 pre-defined personalities, including the one that describe mail, web, file, and database servers behaviour</p>
<dt>&bull;</p>
<dd> Easy to add new personalities using reach Workload Model Language (WML)</p>
<dt>&bull;</p>
<dd> Multi-process and multi-thread workload support</p>
<dt>&bull;</p>
<dd> Configurable directory hierarchies with depth, width, and file sizes set to given statistical distributions</p>
<dt>&bull;</p>
<dd> Support of asynchronous I/O and process synchronization primitives</p>
<dt>&bull;</p>
<dd> Integrated statistics for throughput, latency, and CPU cycle counts per system call </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-f &lt;filename&gt;</p>
<dd> use specified file as an input instead of stdin</p>
<dt>-h</p>
<dd> Display verbose help</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Run filebench interactively:</p>
<dd>
<dt><code>$ filebench</code></p>
<dd> Start filebench interactive shell, filebench prompt will appear after that.</p>
<dt><code>filebench&gt; load fileserver</code></p>
<dd> Load fileserver personality using load command.</p>
<dt><code>filebench&gt; set $dir=/mnt</code></p>
<dd> After personality is loaded, tunables of the workload personality can be set. Here we change the benchmark directory to /mnt where the file system we want to benchmark is presumably mounted.</p>
<dt><code>filebench&gt; run 60</code></p>
<dd> Start workload for 60 seconds. After 60 seconds of the run the statistics is printed and Filebench exits.</p>
<dt>Run filebench non-interactively:</p>
<dd>
<dt><code>filebench -f /usr/share/filebench/workloads/fileserver.f</code></p>
<dd> Run filebench non-interactively, however, you need to add &#8216;run &lt;time&gt;&#8217; to the end of the workload personality file before calling filebench.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>0 if OK,</p>
<dd>
<dt>1 if workload file is not found.</p>
<dd></dl>
<h2>REPORTING BUGS</h2>
<p> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=133644">http://sourceforge.net/tracker/?group_id=133644</a>&amp;atid=727883 </p>
<h2>Index</h2>
