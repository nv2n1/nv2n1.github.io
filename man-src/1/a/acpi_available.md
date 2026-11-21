---

title: "acpi_available(1)"
name: "acpi_available"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpi_available/"
description: "acpi_available – test whether ACPI subsystem is available"
---

<p> <code>acpi_available</code> </p>
<p> <code>acpi_available</code> checks whether the ACPI (&quot;Advanced Configuration and Power Interface&quot;) subsystem is available, as evidenced by the presence of the /proc/acpi directory. </p>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>EXIT STATUS</h2>
<pre>
<code>0</code> (true)        ACPI subsystem is available
<code>1</code> (false)       ACPI subsystem is not available
<code>2</code>                       usage error (arguments supplied)
</pre>
<h2>FILES</h2>
<pre>
<i>/proc/acpi</i>        ACPI status information file
</pre>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Hood &lt;jdthood [at] yahoo.co.uk&gt;. </p>
