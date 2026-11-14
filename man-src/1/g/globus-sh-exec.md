---
title: "globus-sh-exec(1)"
name: "globus-sh-exec"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-sh-exec/"
description: "globus-sh-exec – Run a shell script"
---

<h2 class="name">NAME</h2>
<p> globus-sh-exec &#8211; Run a shell script </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-sh-exec</code> [ -help | -usage | -version ] </p>
<p> <code>globus-sh-exec</code> <i>COMMAND</i> [<i>ARGS</i>&#8230;] </p>
<p> <code>globus-sh-exec</code> -e <i>EXEC</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>globus-sh-exec</code> command executes a shell script, setting the GLOBUS_SH_PERL and GLOBUS_SH environment variables to the perl and posix shell interpreters respectively. The <i>COMMAND</i> script can be a local file or a GASS url, in which case it is downloaded by <code>globus-url-copy</code> before execution. The <i>ARGS</i> parameters, if any, are passed as the command-line options to <i>COMMAND</i>. </p>
<p> The full set of options to <code>globus-sh-exec</code> are </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Print usage information and exit.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>-list, -l</code></p>
<dl>
<dt>
<dd> Lists the defined <i>GLOBUS_SH_</i> variables and exits.</dl>
<p> <code>-exec </code><i>EXEC</i><code>, -e </code><i>EXEC</i></p>
<dl>
<dt>
<dd> Run the command <i>EXEC</i> instead of executing a separate script.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2016 University of Chicago </p>
<h2>Index</h2>
