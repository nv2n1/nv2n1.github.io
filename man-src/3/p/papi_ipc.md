---
title: "papi_ipc(3)"
name: "papi_ipc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_ipc/"
description: "PAPI_ipc –"
---

<p>PAPI_ipc &#8211; </p>
<p> Simplified call to get instructions per cycle, real and processor time.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface: </code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt;<br />
 int <code>PAPI_ipc( float *rtime, float *ptime, long long *ins, float *ipc )</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*rtime</i> total realtime since the first call<br />
 <i>*ptime</i> total process time since the first call<br />
 <i>*ins</i> total instructions since the first call<br />
 <i>*ipc</i> incremental instructions per cycle since the last call</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> The counters were already started by something other than <code>PAPI_ipc()</code>.<br />
 <i>PAPI_ENOEVNT</i> The floating point operations event does not exist.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.</dl>
<p> The first call to <code>PAPI_ipc()</code> will initialize the PAPI High Level interface, set up the counters to monitor PAPI_TOT_INS and PAPI_TOT_CYC events and start the counters. </p>
<p> Subsequent calls will read the counters and return total real time, total process time, total instructions since the start of the measurement and the IPC rate since the latest call to <code>PAPI_ipc()</code>. </p>
<p> A call to <code>PAPI_stop_counters()</code> will stop the counters from running and then calls such as <code>PAPI_start_counters()</code> or other rate calls can safely be used. </p>
<p> <code>PAPI_ipc</code> should return a ratio greater than 1.0, indicating instruction level parallelism within the chip. The larger this ratio the more effeciently the program is running. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_flips()</code> </p>
<p> <code>PAPI_flops()</code> </p>
<p> <code>PAPI_epc()</code> </p>
<p> <code>PAPI_stop_counters()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
