---
title: "pmie2col(1)"
name: "pmie2col"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmie2col/"
description: "pmie2col – convert pmie output to multi-column format"
---

<h2>NAME</h2>
<p> <code>pmie2col</code> &#8211; convert pmie output to multi-column format</p>
<h2>SYNOPSIS</h2>
<p> <code>pmie2col</code> [<code>-d</code> <i>delimiter</i>] [<code>-p</code> <i>precision</i>] [<code>-w</code> <i>width</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmie2col</code> is a simple tool that converts output from <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) into regular column format. Each column is 7 characters wide (by default, may be changed with the <code>-w</code> option) with a single space between columns. That single space can be substituted with an alternate delimiter using the <code>-d</code> option (this is useful for importing the data into a spreadsheet, for example). </p>
<p> The precision of the tabulated values from <code>pmie</code> can be specified with the <code>-p</code> option (default is 2 decimal places). This option can and will override any width setting in order to present the requested precision. </p>
<p> The <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) configuration must follow these rules:</p>
<dl>
<dt>(1)</p>
<dd> Each <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) expression is of the form &#8220;NAME = expr;&#8221;. NAME will be used as the column heading, and must contain no white space, although special characters can be escaped by enclosing NAME in single quotes.</p>
<dt>(2)</p>
<dd> The &#8220;expr&#8221; must be a valid <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) expression that produces a singular value.</dl>
<p> In addition, <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) must be run with the <code>-v</code> command line option. </p>
<p> It is also possible to use the <code>-e</code> command line to <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) and output lines will be prefixed by a timestamp.</p>
<h2>EXAMPLE</h2>
<p> Given this <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) configuration file <i>(config)</i>: <code> </p>
<p> </code></p>
<pre><code>
loadav = kernel.all.load #'1 minute';
'%usr' = kernel.all.cpu.user;
'%sys' = kernel.all.cpu.sys;
'%wio' = kernel.all.cpu.wait.total;
'%idle' = kernel.all.cpu.idle;
'max-iops' = max_inst(disk.dev.total);
</code></pre>
<p> Then this command pipeline: <code> </p>
<p> </code></p>
<pre>
$ pmie -v -t 5 &lt;config | pmie2col -w 8
</pre>
<p> Produces output like this: <code> </p>
<p> </code></p>
<pre>
   loadav     %usr     %sys     %wio    %idle max-iops
     0.21        ?        ?        ?        ?        ?
     0.36     0.49     0.03     0.18     0.29    25.40
     0.49     0.41     0.10     0.36     0.13    51.00
     0.69     0.49     0.10     0.05     0.37    43.20
     0.71     0.39     0.08     0.04     0.49    14.00
     0.83     0.63     0.15     0.00     0.21    32.30
     1.09     0.60     0.02     0.10     0.27    47.00
     0.92     0.01     0.00     0.00     0.99     2.40
</pre>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1). </p>
<h2>Index</h2>
