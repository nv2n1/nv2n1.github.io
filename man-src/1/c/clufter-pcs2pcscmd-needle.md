---

title: "clufter-pcs2pcscmd-needle(1)"
name: "clufter-pcs2pcscmd-needle"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clufter-pcs2pcscmd-needle/"
description: "clufter – pcs2pcscmd-needle"
---

<h2>NAME</h2>
<p> clufter &#8211; pcs2pcscmd-needle</p>
<p> <code>clufter</code> [<i>&lt;global option&gt; </i>&#8230;] <i>pcs2pcscmd-needle </i>[<i>&lt;cmd option </i>&#8230;<i>&gt;</i>]</p>
<p> (Corosync v2,Pacemaker) cluster cfg. -&gt; reinstating pcs commands</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show help message and exit</dd>
<dt><code>-H</code>, <code>&#8211;help-full</code></dt>
<dd> full help message and exit</dd>
<dt>
</dt><dd> Command options:</dd>
<dt><code>-c</code> CORO, <code>&#8211;coro</code>=<i>CORO</i></dt>
<dd> input Corosync v2 configuration file [/etc/corosync/corosync.conf]</dd>
<dt><code>-i</code> CIB, <code>&#8211;cib</code>=<i>CIB</i></dt>
<dd> input proper Pacemaker cluster config. file (CIB) [/var/lib/pacemaker/cib/cib.xml]</dd>
<dt><code>-o</code> OUTPUT, <code>&#8211;output</code>=<i>OUTPUT</i></dt>
<dd> pcs commands to reinstate the cluster per the inputs [-]</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> may the force be with emitted pcs commands [disabled]</dd>
<dt><code>-n</code>, <code>&#8211;noauth</code></dt>
<dd> skip authentication step (OK if already set up) [disabled]</dd>
<dt><code>-s</code>, <code>&#8211;silent</code></dt>
<dd> do not track the progress along the steps execution (echoes) [disabled]</dd>
<dt><code>-t</code> TMP_CIB, <code>&#8211;tmp-cib</code>=<i>TMP_CIB</i></dt>
<dd> file to accumulate the changes (empty ~ direct push, avoid!) [tmp-cib.xml]</dd>
<dt><code>-r</code>, <code>&#8211;dry-run</code></dt>
<dd> omit intrusive commands (TMP_CIB reset if empty) [disabled]</dd>
<dt><code>-e</code>, <code>&#8211;enable</code></dt>
<dd> enable cluster infrastructure services (autostart on reboot) [disabled]</dd>
<dt><code>-w</code> START_WAIT, <code>&#8211;start-wait</code>=<i>START_WAIT</i></dt>
<dd> fixed seconds to give cluster to come up initially [60]</dd>
<dt><code>-g</code>, <code>&#8211;noguidance</code></dt>
<dd> omit extraneous guiding [disabled]</dd>
<dt><code>-x</code> TEXT_WIDTH, <code>&#8211;text-width</code>=<i>TEXT_WIDTH</i></dt>
<dd> for commands rewrapping (0/-1/neg. ~ auto/disable/hi-limit) [0]</dd>
<dt><code>&#8211;nocheck</code></dt>
<dd> do not validate any step (even if self-checks present) [disabled]</dd>
<dt><code>&#8211;batch</code></dt>
<dd> do not interact (validation failure recovery, etc.) [disabled]</dd>
<dt><code>&#8211;editor</code>=<i>EDITOR</i></dt>
<dd> customize editor to run (unused in batch mode) [/usr/bin/nano]</dd>
<dt><code>&#8211;raw</code></dt>
<dd> do not care about pretty-printed output [disabled]</dd>
<dt><code>&#8211;noop</code>=<i>NOOP</i></dt>
<dd> (Advanced) debug only: NOOPize filter (2+: repeat) [none out of cmd-annotate, cmd-wrap, simpleconfig-normalize, simpleconfig2needlexml, needlexml2pcscmd, needleqdevicexml2pcscmd, cib-revitalize, cib-meld-templates, cib2pcscmd]</dd>
<dt><code>&#8211;dump</code>=<i>DUMP</i></dt>
<dd> (Advanced) debug only: dump (intermediate) output of the filter (2+: repeat) [none out of cmd-annotate, cmd-wrap, simpleconfig-normalize, simpleconfig2needlexml, needlexml2pcscmd, needleqdevicexml2pcscmd, cib-revitalize, cib-meld-templates, cib2pcscmd, ANY]</dd>
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
<p> <i><a href="/docs/linux/man/8-pcs/">pcs</a></i>(8), <i><a href="/docs/linux/man/1-clufter/">clufter</a></i>(1), </p>
<p> <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd/">clufter-pcs2pcscmd</a></i>(1), <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd-flatiron/">clufter-pcs2pcscmd-flatiron</a></i>(1), and perhaps more </p>
