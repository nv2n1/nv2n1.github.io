---
title: "foomatic-ppdfile(1)"
name: "foomatic-ppdfile"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-ppdfile/"
description: "foomatic-ppdfile – Generate a PPD file for a given printer/driver combo"
---

<h2>NAME</h2>
<p> foomatic-ppdfile &#8211; Generate a PPD file for a given printer/driver combo</p>
<h2>SYNOPSIS</h2>
<p> <code>foomatic-ppdfile [-w] [-d &lt;driver&gt;] -p &lt;printerid&gt;</code><br />
 <code>foomatic-ppdfile [-A] [-P pattern]</code><br />
 <code>foomatic-ppdfile -h</code> </p>
<h2>DESCRIPTION</h2>
<p> The first form of the <code>foomatic-ppdfile</code> to compute the spooler-independent Foomatic PPD file for any valid printer/driver combo available in the Foomatic database, both for printing with <code><a href="/docs/linux/man/1-foomatic-rip/">foomatic-rip</a>(1)</code> and for applications/clients being able to access the printer&#8217;s options. The PPD file is returned on standard ouput. If the driver is not specified, the default driver is used. </p>
<p> The second form of the <code>foomatic-ppdfile</code> program will search the printer database and return either all printer entries or those whose name and/or model information match a regular expression. </p>
<p> The last form prints a help message and exits. </p>
<h3>Options</h3>
<dl>
<dt><code>-d</code><i> drivername</i></p>
<dd> The (optional) driver name to use. If the driver name is not supplied, the default or first driver in the printers compatible driver list is used. </p>
<dt><code>-p</code></p>
<dd> printer id The printer id. </p>
<dt><code>-w</code></p>
<dd> Return a PPD file that conforms to the Microsoft Windows format limitations. </p>
<dt><code>-A</code></p>
<dd> Return all printer entries in the database. </p>
<dt><code>-P</code><i>pattern</i></p>
<dd> Return all printer entries in the database which match the regular expression. </p>
<dt></dl>
<h2>SEE ALSO</h2>
<dd> <i><a href="/docs/linux/man/1-foomatic-rip/">foomatic-rip</a></i>(1) </p>
<h2>EXIT STATUS</h2>
<p> <code>foomatic-ppdfile</code> returns 0 on success, 1 otherwise. </p>
<h2>AUTHOR</h2>
<p> Manfred Wassmann &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; for the foomatic project using output from the associated binary. </p>
<p> Modified and updated by Patrick Powell &lt;<i>papowell at astart.com</i>&gt;. </p>
<h2>BUGS</h2>
<p> None so far. </p>
<p> Please post bug reports on </p>
<p> <a rel="nofollow" href="http://lists.freestandards.org/mailman/listinfo/printing-foomatic">http://lists.freestandards.org/mailman/listinfo/printing-foomatic</a> </p>
<h2>Index</h2>
