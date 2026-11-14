---
title: "atmdiag(8)"
name: "atmdiag"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmdiag/"
description: "atmdiag – show ATM device driver diagnostics"
---

<p>atmdiag &#8211; show ATM device driver diagnostics</p>
<h2>Synopsis</h2>
<p><code>atmdiag</code> [<code>-z</code>] [<i>interface</i>&#8230;<code>]</code></p>
<h2>Description</h2>
<p><code>atmdiag</code> shows statistic counters maintained by ATM device drivers. If one or more interface numbers are specified, the statistics of only these interfaces are shown. Otherwise, statistics of all interfaces are displayed. </p>
<p> The following counters are shown for each AAL:</p>
<dl>
<dd>
<dl>
<dt><code>TX_okay</code></p>
<dd>number of successfully sent PDUs.</p>
<dt><code>TX_err</code></p>
<dd>number of PDUs not sent because of errors.</p>
<dt><code>RX_okay</code></p>
<dd>number of successfully received PDUs.</p>
<dt><code>RX_err</code></p>
<dd>number of PDUs discarded because of errors.</p>
<dt><code>RX_drop</code></p>
<dd>number of PDUs dropped because of lack of memory.</dl>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-z</code></p>
<dd>zero all counters after showing them.</dl>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmdump/">atmdump</a>(8), <a href="/docs/linux/man/8-sonetdiag/">sonetdiag</a>(8) </p>
