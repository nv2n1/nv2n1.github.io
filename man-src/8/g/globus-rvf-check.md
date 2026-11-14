---
title: "globus-rvf-check(8)"
name: "globus-rvf-check"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-rvf-check/"
description: "globus-rvf-check – Edit a GRAM5 RSL validation file"
---

<p>globus-rvf-check &#8211; Edit a GRAM5 RSL validation file</p>
<h2>Synopsis</h2>
<p><code>globus-rvf-check</code> <i>-h</i> <i>-help</i></p>
<h2>Description</h2>
<p>The <code>globus-rvf-check</code> command is a utility which checks the syntax of a RSL validation file, and prints out parse errors when encountered. It can also parse the RVF file contents and then dump file&#8217;s contents to stdout, after canonicalizing values and quoting. The exit code of command is a utility which checks the syntax of a RSL validation file, and prints out parse errors when encountered. It can also parse the RVF file contents and then dump file&#8217;s contents to stdout, after canonicalizing values and quoting. The exit code of <code>globus-rvf-check</code> is 0 if all files specified on the command line exist and have no parse errors. is 0 if all files specified on the command line exist and have no parse errors. </p>
<p> The full set of command-line options to <code>globus-rvf-check</code> consists of: consists of: </p>
<p> <i>-h</i><code>,</code><i>-help</i><code>,</code><i>&#8211;help</i></p>
<dl>
<dd>Print command-line option summary and exit</dl>
<p> <i>-d</i></p>
<dl>
<dd>Dump the RVF contents to stdout. In the output, Each file which is parsed will be prefixed by an RVF comment which contains the input filename. If not specified, <code>globus-rvf-check</code> just prints a diagnostic message to standard output indicating whether the file could be parsed. just prints a diagnostic message to standard output indicating whether the file could be parsed.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-globus-rvf-edit/">globus-rvf-edit</a>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
