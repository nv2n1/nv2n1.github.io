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
</dd><dl>
<dt><code>TX_okay</code></dt>
<dd>number of successfully sent PDUs.</dd>
<dt><code>TX_err</code></dt>
<dd>number of PDUs not sent because of errors.</dd>
<dt><code>RX_okay</code></dt>
<dd>number of successfully received PDUs.</dd>
<dt><code>RX_err</code></dt>
<dd>number of PDUs discarded because of errors.</dd>
<dt><code>RX_drop</code></dt>
<dd>number of PDUs dropped because of lack of memory.</dd></dl>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-z</code></dt>
<dd>zero all counters after showing them.</dd></dl>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmdump/">atmdump</a>(8), sonetdiag(8) </p>
