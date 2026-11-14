---
title: "deweb(1)"
name: "deweb"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deweb/"
description: "deweb – strips away C & CWEB commands from CWEB sources"
---

<h2 class="name">NAME</h2>
<p> deweb &#8211; strips away C &amp; CWEB commands from CWEB sources </p>
<h2>SYNOPSIS</h2>
<p> <code>deweb</code> [ <code>file1 file2 &#8230;</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>deweb</i> filters away all C &amp; CWEB commands from a CWEB source code. This leaves only the <i>LaTeX</i> code. This stripped code, in turn, may then be passed to a suitable syntax checker for LaTeX, like <i>ChkTeX</i> and <i>lacheck,</i> or spell-checkers like <i>ispell.</i> </p>
<p> The <i>chkweb</i> tool, included in the <i>ChkTeX</i> distribution will do just this; writing similar scripts should be trivial. </p>
<p> When <i>deweb</i> strips away the C code from your CWEB source, it tries to preserve line breaks. This means that the error reports from <i>&lt;your favorite tool&gt;</i> will be correct regarding to line numbers. In most cases, the column position will also be correct. This significantly simplifies finding the errors in the <i>LaTeX</i> source (in contrast to the output from <i>cweave,</i> which output is truly difficult to figure anything out from). </p>
<p> <i>deweb</i> accepts a list of filenames on the argument line, and will send its output to <i>stdout.</i> If no filenames are given, it will read from stdin, acting as a filter. No options are currently accepted. </p>
<p> Macho users may try to pipe the output from <i>deweb</i> directly into <i>LaTeX,</i> theoretically, this should work. This would ease the debugging of the <i>LaTeX</i> code significantly, as when <i>LaTeX</i> complains about wrong syntax, you&#8217;ll be able to find the erroneous line much more easily. Don&#8217;t expect that the output looks very much like the final one, though. </p>
<p> <i>deweb</i> should now understand all correct <i>CWEB</i> opcodes. If it complains about not understanding a correct opcode, please inform the author.</p>
<h2>DISTRIBUTION</h2>
<p> Copyright (C) 1996 Jens T. Berger Thielemann </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <i>GNU General Public License </i> as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <code>WITHOUT ANY WARRANTY;</code> without even the implied warranty of <code>MERCHANTABILITY</code> or <code>FITNESS FOR A PARTICULAR PURPOSE.</code> See the <i>GNU General Public License</i> for more details. </p>
<p> You should have received a copy of the <code>GNU General Public License</code> along with this program; if not, write to the <i>Free Software Foundation, Inc.,</i> 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.</p>
<h2>ENVIRONMENT</h2>
<p> No environment variables are used.</p>
<h2>FILES</h2>
<p> None.</p>
<h2>AUTHOR</h2>
<p> Jens T. Berger Thielemann, <i>&lt;jensthi [at] ifi.uio.no&gt;</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cweave/">cweave</a>(1), <a href="/docs/linux/man/1-perl/">perl</a>(1), chktex, <a href="/docs/linux/man/1-lacheck/">lacheck</a>(1), <a href="/docs/linux/man/1-ispell/">ispell</a>(1)</code></p>
<h2>BUGS</h2>
<p> Doesn&#8217;t even <code>compile</code> under <i>Perl</i> versions before perl v5. Unfortunately, this means that we can&#8217;t even tell the user why we failed;</p>
