---
title: "cups-genppdupdate(8)"
name: "cups-genppdupdate"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cups-genppdupdate/"
description: "cups-genppdupdate – update CUPS+Gutenprint PPD files"
---

<p>cups-genppdupdate &#8211; update CUPS+Gutenprint PPD files</p>
<h2>Synopsis</h2>
<p><code>cups-genppdupdate</code> [<i>-h</i>] [<i>-n</i>] [<i>-N</i>] [<i>-q</i> | <i>-v</i>] [<i>-s ppd-directory</i>] [<i>-s output-directory</i>] [<i>PPD-FILES or QUEUES&#8230;</i>]</p>
<h2>Description</h2>
<p><code>cups-genppdupdate</code> regenerates the <i>Gutenprint</i> PPD files in use by CUPS, using the PPD files under <i>/usr/share/cups/model/gutenprint</i> as templates. The new PPD file replaces the old PPD file under <i>/etc/cups/ppd</i>, but all the options set in the old PPD will be merged into the new PPD, provided that they are still valid in the new file. </p>
<p> If no files or queue names are specified, <code>cups-genppdupdate</code> updates all Gutenprint PPD files in <i>/etc/cups/ppd</i>. Otherwise, <code>cups-genppdupdate</code> updates all files or queues listed on the command line. </p>
<p> <code>cups-genppdupdate</code> does not update PPD files from Gimp-Print 4.2 or earlier. </p>
<p> <code>cups-genppdupdate</code> does <code>not</code> restart cupsd. cupsd will need manually reloading (or send SIGHUP) once <code>cups-genppdupdate</code> has completed.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Show a help message.</p>
<dt><code>-n</code></p>
<dd>No action. The program will run, but the old PPD files will not be replaced.</p>
<dt><code>-q</code></p>
<dd>Quiet mode. No messages will be issued, apart from errors.</p>
<dt><code>-v</code></p>
<dd>Verbose mode. More informative messages will be issued. Note that extremely verbose output may be turned on by setting $debug=1 in the source, but this output will not be of use to the average user.</p>
<dt><code>-s </code><i>ppd-directory</i></p>
<dd>Use <i>ppd-directory</i> as the base directory to read PPD files from. By default, the base directory is /usr/share/cups/model/gutenprint. Under this directory, the PPD files are located in subdirectories according to language code and territory.</p>
<dt><code>-o </code><i>output-directory</i></p>
<dd>Place updated PPD files in <i>output-directory</i>. By default, this is the same as the input directory.</p>
<dt><code>-N</code></p>
<dd>Reset all options to their defaults (do not merge options from the current PPD file)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cups-genppd/">cups-genppd</a></code>(8), <code><a href="/docs/linux/man/8-cups-genppdconfig/">cups-genppdconfig</a></code>(8), CUPS Software Administrators Manual, <a rel="nofollow" href="http://localhost:631/documentation.html">http://localhost:631/documentation.html</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2006 Roger Leigh (rleigh [at] debian.org) and Robert Krawitz (rlk [at] alum.mit.edu) </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation. </p>
<p> This manual page was written by Roger Leigh (rleigh [at] debian.org).</p>
