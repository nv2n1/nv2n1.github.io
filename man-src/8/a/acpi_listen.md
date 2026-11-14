---
title: "acpi_listen(8)"
name: "acpi_listen"
section: "8"
letter: "a"
url: "/docs/linux/man/8-acpi_listen/"
description: "acpi_listen – ACPI event listener"
---

<p>acpi_listen &#8211; ACPI event listener</p>
<h2>Synopsis</h2>
<p><code>acpi_listen</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>acpid</code> is the system-wide ACPI event catcher. <code>acpi_listen</code> is a simple shell-friendly tool which connects to acpid and listens for events. When an event occurs, acpi_listen will print it on stdout. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i></i>, <code>&#8211;count</code><i> events</i></p>
<dd>Receive up to a maximum number of ACPI events, then exit.</p>
<dt><code>-s</code><i></i>, <code>&#8211;socketfile</code><i> filename</i></p>
<dd>This option changes the name of the UNIX domain socket which <code>acpid</code> opens. Default is <i>/var/run/acpid.socket</i>.</p>
<dt><code>-t</code><i></i>, <code>&#8211;time</code><i> seconds</i></p>
<dd>Listen for the specified time in seconds, before exiting.</p>
<dt><code>-v</code><i></i>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-h</code><i></i>, <code>&#8211;help</code></p>
<dd>Show help and exit. </p>
</dl>
<h2>Files</h2>
<p><code>/var/run/acpid.socket</code></p>
<h2>Bugs</h2>
<p>There are no known bugs. To file bug reports, see <code>AUTHORS</code> below.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-acpid/">acpid</a>(8)</p>
<h2>Authors</h2>
<p>Ted Felix (<a rel="nofollow" href="http://www.tedfelix.com">www.tedfelix.com</a>)<br />
 Tim Hockin &lt;thockin [at] hockin.org&gt;<br />
 Luca Capello &lt;luca [at] pca.it&gt;</p>
