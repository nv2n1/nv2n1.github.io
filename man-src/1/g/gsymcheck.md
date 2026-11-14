---
title: "gsymcheck(1)"
name: "gsymcheck"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsymcheck/"
description: "gsymcheck – gEDA/gaf Symbol Checker"
---

<h2>NAME</h2>
<p> gsymcheck &#8211; gEDA/gaf Symbol Checker</p>
<h2>SYNOPSIS</h2>
<p> <code>gsymcheck</code> [-h] [-v] [-q] symbol1 [&#8230; symbolN]</p>
<h2>DESCRIPTION</h2>
<p> <i>gsymcheck</i> is a symbol checker for gEDA/gaf. Here is a list of checks that <i>gsymcheck</i> performs: </p>
<dl>
<dt>[bu]</p>
<dd> Checks for graphical= attribute (if present does varied tests)</p>
<dt>[bu]</p>
<dd> Checks for the device= attribute</p>
<dt>[bu]</p>
<dd> Checks for various other missing attributes (pinlabel, pintype, pinseq, footprint, refdes)</p>
<dt>[bu]</p>
<dd> Checks to make sure that the active pin end is on the 100 unit grid.</p>
<dt>[bu]</p>
<dd> Checks the uses of the various attributes (duplicates, incorrect syntax, invalid values, etc&#8230;)</p>
<dt>[bu]</p>
<dd> Checks for obsolete, old, and forbidden attributes</p>
<dt>[bu]</p>
<dd> Checks for any nets or buses within a symbol</p>
<dt>[bu]</p>
<dd> Checks for any other connections within a symbol</p>
<dt>[bu]</p>
<dd> Checks to make sure the number of pins is the correct number </p>
</dl>
<h2>OPTIONS</h2>
<p> <i>gsymcheck</i> accepts the following options:</p>
<dl>
<dt><code>-q</code></p>
<dd> Quiet mode on. This mode turns off all warnings/notes/messages. (optional)</p>
<dt><code>-v </code></p>
<dd> Verbose mode 1. This mode will show all error messages (optional)</p>
<dt><code>-vv </code></p>
<dd> Verbose mode 2. This mode will show all error and warning messages (optional)</p>
<dt><code>-vvv </code></p>
<dd> Verbose mode 2. This mode will show all error, warning, and info messages (optional)</p>
<dt><code>-h </code></p>
<dd> Usage summary / gsymcheck help</p>
<dt>symbol1 [&#8230; symbolN]</p>
<dd> At least one symbol file must be specified. If multiple symbols are specified then they are sequentially read in and checked. It is important that the schematic(s) follow all the options (ie last). </p>
</dl>
<h2>EXAMPLES</h2>
<p> Here are some examples on how to run <i>gsymcheck</i>: </p>
<p> To get usage information just run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> gsymcheck</p>
<p> To actually check a symbol with just error counts, run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gsymcheck symbolfilename.sym</p>
<p> To get the actuall error messages, run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gsymcheck -v symbolfilename.sym</p>
<p> To see all the error messages and warnings, run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gsymcheck -vv symbolfilename.sym</p>
<p> To see all the error messages, warnings, and parse info, run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gsymcheck -vvv symbolfilename.sym</p>
<h2>ENVIRONMENT</h2>
<p> <i>gsymcheck</i> respects the following environment variable: </p>
<dl>
<dt><code>GEDADATA </code></p>
<dd> specifies where the various required scheme and rc files are located (the default is ${prefix}/share/gEDA). This environment variables does not need to be set by the end user unless they are moving the executables to a new install ${prefix}. </p>
</dl>
<h2>AUTHOR</h2>
<p> Ales Hvezda and many others </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gschem/">gschem</a></code>(1), <code><a href="/docs/linux/man/1-gnetlist/">gnetlist</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1999-2008 Ales Hvezda </p>
<p> This document can be freely redistributed according to the terms of the GNU General Public License version 2.0 </p>
<h2>Index</h2>
