---
title: "perl-prov(1)"
name: "perl-prov"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl-prov/"
description: "perl.prov – list what Perl source files provide"
---

<p>perl.prov &#8211; list what Perl source files provide </p>
<h2>Synopsis</h2>
<p><code>perl.prov</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;]</p>
<h2>Description</h2>
<p>This script calculates conventional name for each Perl source <i>file</i> specified on a command line, based on its location relative to standard Perl library paths; alternatively, a list of files is obtained from standard input, one file per line. <i>*.pm</i>, <i>*.pl</i>, and <i>*.ph</i> files are processed (<i>*.pm</i> files also suffer version extraction). The output of perl.prov is suitable for automatic dependency tracking (e.g. for <font SIZE="-1">RPM</font> packaging). </p>
<p> For example, <i>/usr/lib/perl5/i386-linux/DB_File.pm</i> provides <tt>&quot;perl(DB_File.pm) = 1.810&quot;</tt> (as of perl-5.8.6). </p>
<p> perl.prov is a counterpart of perl.req.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase verbosity.</dl>
<p> The <font SIZE="-1">RPM_PERL_LIB_PATH</font> environment variable, if set, must contain the list of paths, separated by colons. These paths are considered as library paths used to determine relative names of provided perl files (in addition to paths from <tt>@INC</tt> variable).</p>
<h2>Author</h2>
<p>Written by Alexey Tourbin &lt;at [at] altlinux.org&gt;, based on an earlier version by Ken Estes &lt;kestes [at] staff.mail.com&gt;, with contributions from Mikhail Zabaluev &lt;mhz [at] altlinux.org&gt;.</p>
<h2>Copying</h2>
<p>Copyright (c) 2003, 2004, 2006, 2007, 2008 Alexey Tourbin, <font SIZE="-1">ALT</font> Linux Team. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Library General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p>perl.req</p>
