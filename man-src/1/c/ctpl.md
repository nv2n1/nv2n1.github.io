---
title: "ctpl(1)"
name: "ctpl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctpl/"
description: "ctpl – CTPL command-line template parsing tool"
---

<h2>NAME</h2>
<p> <code>ctpl</code> &#8211; CTPL command-line template parsing tool </p>
<h2>SYNOPSIS</h2>
<p> <code>ctpl</code> [<i>OPTION</i>]&#8230; <i>INPUTFILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ctpl</code> parses one or more <i>INPUTFILE</i> template against the provided environment and outputs the result. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Prints the command line options. </p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> Write output to <i>FILE</i>. If not provided, defaults to stdout. </p>
<dt><code>-e</code>, <code>&#8211;env-file</code>=<i>ENVFILE</i></p>
<dd> Add environment from <i>ENVFILE</i>. This option may appear more than once. </p>
<dt><code>-c</code>, <code>&#8211;env-chunk</code>=<i>CHUNK</i></p>
<dd> Add environment chunk <i>CHUNK</i>. This option may appear more than once. </p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose. </p>
<dt><code>&#8211;version</code></p>
<dd> Print the version information and exit. </p>
<dt><code>&#8211;encoding</code>=<i>ENCODING</i></p>
<dd> Specify the encoding of the input and output files. The default encoding is the system&#8217;s one. </p>
</dl>
<h2>TEMPLATE AND ENVIRONMENT DESCRIPTION SYNTAX</h2>
<p> For the documentation about the syntax of templates and environment descriptions, see the CTPL library&#8217;s documentation. </p>
<h2>REPORTING BUGS</h2>
<p> Report CTPL bugs to ban [at] herbesfolles.org<br />
 CTPL home page: &lt;<a rel="nofollow" href="http://ctpl.tuxfamily.org">http://ctpl.tuxfamily.org</a>&gt; </p>
<h2>AUTHOR</h2>
<p> Colomban Wendling (ban [at] herbesfolles.org) </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2010 Colomban Wendling. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
