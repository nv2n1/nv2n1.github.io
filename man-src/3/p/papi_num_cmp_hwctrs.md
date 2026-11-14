---
title: "papi_num_cmp_hwctrs(3)"
name: "papi_num_cmp_hwctrs"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_num_cmp_hwctrs/"
description: "PAPI_num_cmp_hwctrs –"
---

<p>PAPI_num_cmp_hwctrs &#8211; </p>
<p> Return the number of hardware counters for the specified component.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>PAPI_num_cmp_hwctrs()</code> returns the number of counters present in the specified component. By convention, component 0 is always the cpu. </p>
<p> On some components, especially for CPUs, the value returned is a theoretical maximum for estimation purposes only. It might not be possible to easily create an EventSet that contains the full number of events. This can be due to a variety of reasons: 1). Some CPUs (especially Intel and POWER) have the notion of fixed counters that can only measure one thing, usually cycles. 2). Some CPUs have very explicit rules about which event can run in which counter. In this case it might not be possible to add a wanted event even if counters are free. 3). Some CPUs halve the number of counters available when running with SMT (multiple CPU threads) enabled. 4). Some operating systems &#8216;steal&#8217; a counter to use for things such as NMI Watchdog timers. The only sure way to see if events will fit is to attempt adding events to an EventSet, and doing something sensible if an error is generated. </p>
<p> <code>PAPI_library_init()</code> must be called in order for this function to return anything greater than 0. </p>
<p> <code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_num_cmp_hwctrs(int&nbsp;<wbr>&nbsp;<wbr>cidx&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cidx</i> &#8212; An integer identifier for a component. By convention, component 0 is always the cpu component.</dl>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>
<pre>* // Query the cpu component for the number of counters.
* printf(* </pre>
</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>On success, this function returns a value greater than zero. </p>
<p>&nbsp;<wbr>A zero result usually means the library has not been initialized.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
