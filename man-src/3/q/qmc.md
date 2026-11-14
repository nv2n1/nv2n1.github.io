---
title: "qmc(3)"
name: "qmc"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qmc/"
description: "QMC – library for managing groups of Performance Co-Pilot metrics"
---

<p><code>QMC</code> &#8211; library for managing groups of Performance Co-Pilot metrics</p>
<h2>C++ Synopsis</h2>
<p><code> #include &lt;QMC.h&gt; </p>
<p> CC &#8230; -lqmc -lpcp </code></p>
<h2>Description</h2>
<p>The Qt-based Performance Metrics Class (<code>QMC</code>) class library is a collection of C++ classes for managing a large set of performance metrics from a variety of sources. This library is built over <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-qmccontext/">QmcContext</a></code>(3), <code><a href="/docs/linux/man/3-qmcdesc/">QmcDesc</a></code>(3), <code><a href="/docs/linux/man/3-qmcgroup/">QmcGroup</a></code>(3), <code><a href="/docs/linux/man/3-qmcindom/">QmcIndom</a></code>(3), <code><a href="/docs/linux/man/3-qmcmetric/">QmcMetric</a></code>(3), <code><a href="/docs/linux/man/3-qmcsource/">QmcSource</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) and <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>Error messages are generated using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) but are not flushed. It is the responsibility of the user to call <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) to output any messages. </p>
<p> Additional diagnostics may be activated by adding <code>DBG_TRACE_PMC</code> to the global <i>pmDebug</i>.</p>
