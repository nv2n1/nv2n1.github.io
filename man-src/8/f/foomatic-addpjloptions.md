---
title: "foomatic-addpjloptions(8)"
name: "foomatic-addpjloptions"
section: "8"
letter: "f"
url: "/docs/linux/man/8-foomatic-addpjloptions/"
description: "foomatic-addpjloptions – Format PJL option information the for foomatic database"
---

<p>foomatic-addpjloptions &#8211; Format PJL option information the for foomatic database</p>
<h2>Synopsis</h2>
<p><code>foomatic-addpjloptions [-dafis][-o dir] -p printer_ID [pjl_info_file]</code> <code>foomatic-addpjloptions [-dafq] [pjl_info_file]</code> <code>foomatic-addpjloptions -h</code> </p>
<h2>Description</h2>
<p><code>foomatic-addpjloptions</code> formats the PJL information file (or STDIN) into a format usable by the Foomatic database.</p>
<h3>Options</h3>
<dl>
<dt><code>-a</code></dt>
<dd>Convert all PJL options in the information file.</dd>
<dt><code>-d</code></dt>
<dd>Enable debugging information.</dd>
<dt><code>-f</code></dt>
<dd>Do not ask for permission, force conversion.</dd>
<dt><code>-h</code></dt>
<dd>Print a help message and exit.</dd>
<dt><code>-q</code></dt>
<dd>Print a summary of the PJL information. This output is not compatible with the foomatic database, and is useful for debugging.</dd>
<dt><code>-s</code></dt>
<dd>Produce a single option file containing all the option values.</dd>
<dt><code>-o</code><i> dir</i></dt>
<dd>The directory the option information files are written to.</dd>
<dt><code>-p</code><i> printer_ID</i></dt>
<dd>Name of the printer in the foomatic database. This is used to extract printer manufacturer and model information.</dd>
<dt><code>pjl_info_file</code></dt>
<dd>File with PJL information returned by the printer. If this filename is not provided, the PJL options are taken from standard input. </dd>
<h2>Files</h2>
<dl>
<dt><code>/usr/share/foomatic/templates/pjl*.xml</code></dt>
<dd>Template files for option information. </dd>
<dt><code>./foomatic-db/opts</code></dt>
<dd>Option information stored in this directory. </dd>
</dl>
<h2>Exit Status</h2>
<p><code>foomatic-addpjloptions</code> returns 0 on success, and a nonzero value on failure.</p>
<h2>Author</h2>
<p>Manfred Wassmann &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; for the foomatic project using output from the associated binary. </p>
<p> Modified by Patrick Powell (&lt;papowell at astart.com&gt;).</p>
<h2>Bugs</h2>
<p>Please post bug reports on <a rel="nofollow" href="http://lists.freestandards.org/mailman/listinfo/printing-foomatic">http://lists.freestandards.org/mailman/listinfo/printing-foomatic</a> </p>
</dl>