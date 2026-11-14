---
title: "runc-ps(8)"
name: "runc-ps"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-ps/"
description: "runc-ps – display the processes inside a container"
---

<p><code>runc-ps</code> &#8211; display the processes inside a container </p>
<h2>Synopsis</h2>
<p><code>runc ps</code> [<i>option</i> &#8230;] <i>container-id</i> [<i>ps-option</i> &#8230;] </p>
<h2>Description</h2>
<p>The command <code>ps</code> is a wrapper around the stock <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) utility, which filters its output to only contain processes belonging to a specified <i>container-id</i>. Therefore, the PIDs shown are the host PIDs. Any <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) options can be used, but some might break the filtering. In particular, if PID column is not available, an error is returned, and if there are columns with values containing spaces before the PID column, the result is undefined. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;format</code>|<code>-f</code> <code>table</code>|<code>json</code></p>
<dd>Output format. Default is <code>table</code>. The <code>json</code> format shows a mere array of PIDs belonging to a container; if used, all <code>ps</code> options are gnored. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc-list/">runc-list</a></code>(8), <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
