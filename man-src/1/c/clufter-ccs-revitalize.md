---
title: "clufter-ccs-revitalize(1)"
name: "clufter-ccs-revitalize"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clufter-ccs-revitalize/"
description: "clufter – ccs-revitalize"
---

<h2>NAME</h2>
<p> clufter &#8211; ccs-revitalize</p>
<h2>SYNOPSIS</h2>
<p> <code>clufter</code> [<i>&lt;global option&gt; </i>&#8230;] <i>ccs-revitalize </i>[<i>&lt;cmd option </i>&#8230;<i>&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> Migrate deprecated config&#8217;s props (agent params, etc.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show help message and exit</p>
<dt><code>-H</code>, <code>&#8211;help-full</code></p>
<dd> full help message and exit</p>
<dt>
<dd> Command options:</p>
<dt><code>-i</code> INPUT, <code>&#8211;input</code>=<i>INPUT</i></p>
<dd> input CMAN-based cluster configuration file [/etc/cluster/cluster.conf]</p>
<dt><code>-o</code> OUTPUT, <code>&#8211;output</code>=<i>OUTPUT</i></p>
<dd> output file with &quot;revitalized&quot; content [cluster-revitalized-{ccs-revitalize.in.hash}.conf]</p>
<dt><code>&#8211;noop</code>=<i>NOOP</i></p>
<dd> (Advanced) debug only: NOOPize filter (2+: repeat) [none out of ccs-revitalize]</p>
<dt><code>&#8211;dump</code>=<i>DUMP</i></p>
<dd> (Advanced) debug only: dump (intermediate) output of the filter (2+: repeat) [none out of ccs-revitalize, ANY]</p>
<dt>
<dd> Common options:</p>
<dt>
<dd> Either in global (before &lt;cmd&gt;) or command scope (after &lt;cmd&gt;).</p>
<dt><code>&#8211;sys</code>=<i>SYS</i></p>
<dd> (Advanced) override autodetected system [linux]</p>
<dt><code>&#8211;dist</code>=<i>DIST</i></p>
<dd> override target distro (for SYS=linux; see <code>&#8211;list-dists</code>) [centos,7.2.1511,Core]</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> refrain from unnecesary messages (usually on stderr)</p>
<dt><code>&#8211;color</code>=<i>[WHEN]</i></p>
<dd> colorize messages if available [auto out of auto, never, always]</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> shortcut for <code>&#8211;loglevel</code>=<i>DEBUG</i></p>
<dt><code>&#8211;logfile</code>=<i>FILE</i></p>
<dd> specify log file (instead of stderr)</p>
<dt><code>&#8211;loglevel</code>=<i>LEVEL</i></p>
<dd> specify log level [WARNING out of NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL]</dl>
<p> Arguments to value-based `command options&#8217; can go without labels when the order wrt. parsing logic respected; skipping those backed by default values otherwise requiring specification then allowed by syntactic sugar: all can be passed as a single, first, ::-delimited argument; magic files: `-&#8216;, `@DIGIT+&#8217;. `{formula}&#8217; in output file spec: input-backed (e.g. hash) substitution recipe. All available commands listed as `clufter <code>&#8211;list</code>&#8216;.</p>
<h2>AUTHOR</h2>
<p> Written by Jan Pokorný &lt;jpokorny+pkg-clufter [at] redhat.com&gt; and plugin authors.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%207">https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%207</a>&amp;component=clufter&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Red Hat, Inc. Licensed under GPLv2+.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a></i>(5), <i><a href="/docs/linux/man/7-ccs/">ccs</a></i>(7), <i><a href="/docs/linux/man/1-clufter/">clufter</a></i>(1), </p>
<p> <i><a href="/docs/linux/man/1-clufter-ccs-artefacts/">clufter-ccs-artefacts</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs-disable-rg/">clufter-ccs-disable-rg</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs-obfuscate/">clufter-ccs-obfuscate</a></i>(1), and perhaps more </p>
<h2>Index</h2>
