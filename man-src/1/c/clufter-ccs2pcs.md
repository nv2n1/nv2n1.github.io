---
title: "clufter-ccs2pcs(1)"
name: "clufter-ccs2pcs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clufter-ccs2pcs/"
description: "clufter – ccs2pcs"
---

<h2>NAME</h2>
<p> clufter &#8211; ccs2pcs</p>
<h2>SYNOPSIS</h2>
<p> <code>clufter</code> [<i>&lt;global option&gt; </i>&#8230;] <i>ccs2pcs </i>[<i>&lt;cmd option </i>&#8230;<i>&gt;</i>]<br />
 <code>clufter</code> [<i>&lt;global option&gt; </i>&#8230;] <i>ccs2pcs-needle </i>[<i>&lt;cmd option </i>&#8230;<i>&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> (CMAN,rgmanager)-&gt;(Corosync v2,Pacemaker) cluster cfg. </p>
<p> More specifically, the output is suitable for Pacemaker integrated with Corosync ver. 2 (Needle) as present, e.g., in RHEL 7, and consists of Pacemaker (~cib.xml) and Corosync (~corosync.conf) configurations.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show help message and exit</dd>
<dt><code>-H</code>, <code>&#8211;help-full</code></dt>
<dd> full help message and exit</dd>
<dt>
</dt><dd> Command options:</dd>
<dt><code>-i</code> INPUT, <code>&#8211;input</code>=<i>INPUT</i></dt>
<dd> input (CMAN,rgmanager) cluster configuration file [/etc/cluster/cluster.conf]</dd>
<dt><code>-c</code> CORO, <code>&#8211;coro</code>=<i>CORO</i></dt>
<dd> output Corosync v2 config. file [corosync-{ccs2ccsflat.in.hash}.conf]</dd>
<dt><code>&#8211;cib</code>=<i>CIB</i></dt>
<dd> output proper Pacemaker cluster config. file (CIB) [cib-{ccs2ccsflat.in.hash}.xml]</dd>
<dt><code>&#8211;nocheck</code></dt>
<dd> do not validate any step (even if self-checks present) [disabled]</dd>
<dt><code>&#8211;batch</code></dt>
<dd> do not interact (validation failure recovery, etc.) [disabled]</dd>
<dt><code>&#8211;editor</code>=<i>EDITOR</i></dt>
<dd> customize editor to run (unused in batch mode) [/usr/bin/nano]</dd>
<dt><code>&#8211;raw</code></dt>
<dd> do not care about pretty-printed output [disabled]</dd>
<dt><code>&#8211;noop</code>=<i>NOOP</i></dt>
<dd> (Advanced) debug only: NOOPize filter (2+: repeat) [none out of ccs2ccsflat, ccs-propagate-cman, ccs2needlexml, xml2simpleconfig, ccs-revitalize, ccsflat2cibprelude, cibprelude2cibcompact, cibcompact2cib, cib2cibfinal]</dd>
<dt><code>&#8211;dump</code>=<i>DUMP</i></dt>
<dd> (Advanced) debug only: dump (intermediate) output of the filter (2+: repeat) [none out of ccs2ccsflat, ccs-propagate-cman, ccs2needlexml, xml2simpleconfig, ccs-revitalize, ccsflat2cibprelude, cibprelude2cibcompact, cibcompact2cib, cib2cibfinal, ANY]</dd>
<dt><code>&#8211;profile</code></dt>
<dd> (Advanced) enable XSLT profiling (auxiliary files produced) [disabled]</dd>
<dt>
</dt><dd> Common options:</dd>
<dt>
</dt><dd> Either in global (before &lt;cmd&gt;) or command scope (after &lt;cmd&gt;).</dd>
<dt><code>&#8211;sys</code>=<i>SYS</i></dt>
<dd> (Advanced) override autodetected system [linux]</dd>
<dt><code>&#8211;dist</code>=<i>DIST</i></dt>
<dd> override target distro (for SYS=linux; see <code>&#8211;list-dists</code>) [centos,7.2.1511,Core]</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> refrain from unnecesary messages (usually on stderr)</dd>
<dt><code>&#8211;color</code>=<i>[WHEN]</i></dt>
<dd> colorize messages if available [auto out of auto, never, always]</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> shortcut for <code>&#8211;loglevel</code>=<i>DEBUG</i></dd>
<dt><code>&#8211;logfile</code>=<i>FILE</i></dt>
<dd> specify log file (instead of stderr)</dd>
<dt><code>&#8211;loglevel</code>=<i>LEVEL</i></dt>
<dd> specify log level [WARNING out of NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL]</dd></dl>
<p> Arguments to value-based `command options&#8217; can go without labels when the order wrt. parsing logic respected; skipping those backed by default values otherwise requiring specification then allowed by syntactic sugar: all can be passed as a single, first, ::-delimited argument; magic files: `-&#8216;, `@DIGIT+&#8217;. `{formula}&#8217; in output file spec: input-backed (e.g. hash) substitution recipe. All available commands listed as `clufter <code>&#8211;list</code>&#8216;.</p>
<h2>AUTHOR</h2>
<p> Written by Jan Pokorný &lt;jpokorny+pkg-clufter [at] redhat.com&gt; and plugin authors.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%207">https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%207</a>&amp;component=clufter&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Red Hat, Inc. Licensed under GPLv2+.</p>
<h2>SEE ALSO</h2>
<p> <i>/usr/share/doc/clufter-0.59.5/rgmanager-pacemaker</i>, <i>cluster.conf</i>(5), <i>ccs</i>(7), <i><a href="/docs/linux/man/1-clufter/">clufter</a></i>(1), </p>
<p> <i><a href="/docs/linux/man/1-clufter-ccs2pcs-flatiron/">clufter-ccs2pcs-flatiron</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcs-needle/">clufter-ccs2pcs-needle</a></i>(1), and perhaps more </p>
<h2>Index</h2>
