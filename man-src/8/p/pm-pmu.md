---
title: "pm-pmu(8)"
name: "pm-pmu"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pm-pmu/"
description: "pm-pmu – suspend the computer on machines using a Macintosh-style PMU"
---

<p>pm-pmu &#8211; suspend the computer on machines using a Macintosh-style PMU</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pm-pmu</code></dl>
<h2>Description</h2>
<dd>This manual page documents briefly the <code>pm-pmu</code> command. </p>
<p> <code>pm-pmu</code> is a command line program to suspend a computer on machines using a Macintosh-style PMU</p>
<h2>Exit Codes</h2>
<p>The command succeeds (status 0) if the machine uses a Macintosh-style PMU, and suspended successfully. The command fails (status other than 0) otherwise. It is designed to be easy to use in shell scripts. </p>
<p> <code>0 (true)</code></p>
<dl>
<dd>System was suspended using PMU.</dl>
<p> <code>1 (false)</code></p>
<dl>
<dd>System could not be suspended using PMU.</dl>
<h2>Options</h2>
<p>This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>&#8211;suspend</code></p>
<dl>
<dd>Suspend the computer.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show help message.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pm-suspend/">pm-suspend</a></code>(8)</p>
<h2>Author</h2>
<p>This manual page was written by Richard Hughes richard [at] hughsie.com.</p>
<h2>Author</h2>
<p><code>Richard Hughes</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Richard Hughes</p>
