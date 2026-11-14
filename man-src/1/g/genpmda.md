---
title: "genpmda(1)"
name: "genpmda"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genpmda/"
description: "genpmda – Performance Co-Pilot PMDA Generator"
---

<h2>NAME</h2>
<p> <code>genpmda</code> &#8211; Performance Co-Pilot PMDA Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>genpmda</code> [<code>-d</code>] [<code>-D</code> <i>domain</i>] [<code>-s</code> <i>stdpmid</i>] [<code>-t</code> <i>topdir</i>] [<code>-n</code> <i>pmns</i>] [<code>-o</code> <i>dir</i>] [<code>-v</code>] <code>-i</code> <i>IAM</i> <code>-c</code> <i>config</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Genpmda</code> is a rapid application development tool for creating new Performance Metrics Domain Agents, see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3). It provides a very easy and efficient way to extend the Performance Co-pilot (PCP) with new performance metrics without needing to understand the low level details of how PMDAs are constructed. </p>
<p> <code>Genpmda</code> reads a config file containing an augmented Performance Metrics Name Space, see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5), and automatically generates virtually all of the source code to implement a fully functional PMDA, including the Makefile, name space, support scripts for configuring the new PMDA, and the metrics help text. Fairly simple PMDAs can be automatically generated from the config file without writing any additional code. More complicated PMDAs, e.g. containing multiple instance domains, require only the refresh methods for the instance domains to be written manually. </p>
<p> An example of the config file format accepted by <code>genpmda</code> is given below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>Required options:</code></p>
<dd>
<dt><code>-c</code><i> config</i></p>
<dd> input <i>config</i> file, see example below</p>
<dt><code>-i</code><i> IAM</i></p>
<dd> pmda name <i>IAM</i>, should appear in <i>stdpmid</i> or the <code>-D</code> option must be used to specify a <i>domain</i>.</p>
<dt><code>Other options:</code></p>
<dd>
<dt><code>-d</code></p>
<dd> generate an Install script for a daemon PMDA (default is DSO)</p>
<dt><code>-t</code><i> topdir</i></p>
<dd> use <i>topdir</i> in generated GNUmakefile, default <code>../../..</code></p>
<dt><code>-n</code><i> pmns</i></p>
<dd> use <i>pmns</i> as root of the namespace (default matches <code>-i</code> flag)</p>
<dt><code>-D</code><i> domain</i></p>
<dd> use <i>domain</i> number in the generated <code>pmns</code> and <code>domain.h</code> (if <code>-s</code> is not given)</p>
<dt><code>-s</code><i> stdpmid</i></p>
<dd> path to <i>stdpmid</i> (default <code>../../pmns/stdpmid</code>)</p>
<dt><code>-o</code><i> dir</i></p>
<dd> use <i>dir</i> for generated source code, default <code>./generated</code></p>
<dt><code>-v</code></p>
<dd> print verbose messages about what <code>genpmda</code> is doing.</dl>
<p> Example:<br />
&nbsp;<wbr>Generate an&nbsp;<wbr>&quot;example&quot;&nbsp;<wbr>pmda using domain 99: </p>
<p>&nbsp;<wbr><code>genpmda -D 99 -v -i EXAMPLE -c example.conf</code> </p>
<p> Here is <i>example.conf</i> config file (for the required <code>-c</code> option): </p>
<pre><code>
example{
    metric} example.metric
{
    ##  metric            string
    ##  pmid              EXAMPLE:CLUSTER:0
    ##  indom             PM_INDOM_NULL
    ##  type              PM_TYPE_STRING
    ##  units             PMDA_PMUNITS(0,0,0,0,0,0)
    ##  semantics         PM_SEM_DISCRETE
    ##  briefhelptext     one line help text for example.metric.string
    ##  helptext          long help text for example.metric.string
    ##  helptext          This is the second line of the long help text
    ##  helptext          and this is the third line.
    ##  fetch             function example_string_fetch_callback
    ##  code              atom-&gt;cp = "hello world";
    ##code return 1;
    ##endmetric
}
</code></pre>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> Many, but all are intended to be easily understood. </p>
<h2>Index</h2>
