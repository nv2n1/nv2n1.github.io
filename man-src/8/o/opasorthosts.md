---
title: "opasorthosts(8)"
name: "opasorthosts"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opasorthosts/"
description: "opasorthosts"
---

<p>opasorthosts </p>
<p> Sorts its standard input in a typical host name order and sorts to standard output. Hosts are sorted alphabetically (case-insensitively) by any alpha-numeric prefix, and then sorted numerically by any numeric suffix. Host names may end in a numeric field which may optionally have leading zeros. Unlike a pure alphabetic sort, this command results in intuitive sequencing of host names such as: host1, host2, host10 </p>
<p> This command does not remove duplicates; any duplicates are listed in adjacent lines. </p>
<p> Use this command to build mpi_hosts input files for applications or cable tests that place hosts in order by name.</p>
<h2>Syntax</h2>
<p>opasorthosts #8217lt; <i>hostlist</i>&gt; <i>output_file</i></p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>
&nbsp;<wbr><i>hostlist</i>&nbsp;<wbr></p>
<dd>List of host names. </p>
<dt>
&nbsp;<wbr><i>output_file</i>&nbsp;<wbr></p>
<dd>Sorted list output. </p>
</dl>
<h2>Examples</h2>
<p>opasorthosts #8217lt; host.xml &gt; Sorted_host</p>
<dl>
<dt><code>Standard Input</code></p>
<dd>opasorthosts<br />
 osd04<br />
 osd1<br />
 compute20<br />
 compute3<br />
 mgmt1<br />
 mgmt2<br />
 login</p>
<dt><code>Standard Output</code></p>
<dd>compute3<br />
 compute20<br />
 login<br />
 mgmt1<br />
 mgmt2<br />
 osd1<br />
 osd04 </p>
