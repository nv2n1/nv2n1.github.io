---
title: "foomatic-compiledb(1)"
name: "foomatic-compiledb"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-compiledb/"
description: "foomatic-compiledb – Compile the Foomatic printer/driver database"
---

<h2>NAME</h2>
<p> foomatic-compiledb &#8211; Compile the Foomatic printer/driver database</p>
<h2>SYNOPSIS</h2>
<p> <code>foomatic-compiledb</code><i>&nbsp;<wbr></i><code>[&nbsp;<wbr>-t</code><i>&nbsp;<wbr>type</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr></i><code>[&nbsp;<wbr>-f</code><i>&nbsp;<wbr></i><code>]&nbsp;<wbr>[&nbsp;<wbr>-j</code><i>&nbsp;<wbr>n</i><code>&nbsp;<wbr>]</code><i>&nbsp;<wbr></i><code>[&nbsp;<wbr>&nbsp;<wbr></code><i>driver</i><code>&nbsp;<wbr>&#8230;&nbsp;<wbr>&nbsp;<wbr>]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>foomatic-compiledb</code> generates all PPD files or Foomatic combo XML files for all possible printer/driver combos, or only for a selected range of drivers. It generally should not be necessary except for people who want to generate a set of Foomatic data files for distribution. For configuring single printers <code><a href="/docs/linux/man/1-foomatic-ppdfile/">foomatic-ppdfile</a>(1)</code> and especially <code><a href="/docs/linux/man/1-foomatic-configure/">foomatic-configure</a>(1)</code> will automagically compute just what they need. </p>
<h3>Options</h3>
<dl>
<dt><code>-t</code><i>&nbsp;<wbr>type</i></p>
<dd> Output file type, either ppd or xml. </p>
<dt><code>-f</code></p>
<dd> Force: Write into the destination directory even if it already exists. </p>
<dt><code>-j</code><i>&nbsp;<wbr>n</i></p>
<dd> n = number of work processes to run </p>
<dt><i>driver &#8230; </i></p>
<dd> only generate data files for these driver(s) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-foomatic-ppdfile/">foomatic-ppdfile</a></i>(1),<i><a href="/docs/linux/man/1-foomatic-configure/">foomatic-configure</a></i>(1) </p>
<h2>EXIT STATUS</h2>
<p> <code>foomatic-compiledb</code> returns 0 unless something unexpected happens. </p>
<h2>AUTHORS</h2>
<p> Manfred Wassmann &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; and Till Kamppeter &lt;<i>till.kamppeter [at] gmx.net</i>&gt; for the foomatic project using output from the associated binary. </p>
<h2>BUGS</h2>
<p> Existing files are always conserved instead of older files being overwritten. So deleting the destination directory (rm -rf dir) and calling foomatic-compiledb without the -f option is recommended. </p>
<p> Please post bug reports on </p>
<p> <a rel="nofollow" href="http://lists.freestandards.org/mailman/listinfo/printing-foomatic">http://lists.freestandards.org/mailman/listinfo/printing-foomatic</a> </p>
<h2>Index</h2>
