---

title: "clufter-cmd-wrap(1)"
name: "clufter-cmd-wrap"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clufter-cmd-wrap/"
description: "clufter – cmd-wrap"
---

<p> clufter &#8211; cmd-wrap</p>
<h2>SYNOPSIS</h2>
<p> <code>clufter</code> [<i>&lt;global option&gt; </i>&#8230;] <i>cmd-wrap </i>[<i>&lt;cmd option </i>&#8230;<i>&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> Wrap long lines carrying (fairly) convoluted shell commands</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show help message and exit</dd>
<dt><code>-H</code>, <code>&#8211;help-full</code></dt>
<dd> full help message and exit</dd>
<dt>
</dt><dd> Command options:</dd>
<dt><code>-i</code> INPUT, <code>&#8211;input</code>=<i>INPUT</i></dt>
<dd> lines carrying moderately convoluted shell commands [-]</dd>
<dt><code>-o</code> OUTPUT, <code>&#8211;output</code>=<i>OUTPUT</i></dt>
<dd> (hopefully) the same content fitting the text width [-]</dd>
<dt><code>-t</code> TEXT_WIDTH, <code>&#8211;text-width</code>=<i>TEXT_WIDTH</i></dt>
<dd> for commands rewrapping (0/-1/neg. ~ auto/disable/hi-limit) [0]</dd>
<dt><code>&#8211;noop</code>=<i>NOOP</i></dt>
<dd> (Advanced) debug only: NOOPize filter (2+: repeat) [none out of cmd-wrap]</dd>
<dt><code>&#8211;dump</code>=<i>DUMP</i></dt>
<dd> (Advanced) debug only: dump (intermediate) output of the filter (2+: repeat) [none out of cmd-wrap, ANY]</dd>
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
<p> <i><a href="/docs/linux/man/1-clufter/">clufter</a></i>(1), </p>
<p> <i><a href="/docs/linux/man/1-clufter-ccs2pcscmd/">clufter-ccs2pcscmd</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcscmd-flatiron/">clufter-ccs2pcscmd-flatiron</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcscmd-needle/">clufter-ccs2pcscmd-needle</a></i>(1), <i><a href="/docs/linux/man/1-clufter-cib2pcscmd/">clufter-cib2pcscmd</a></i>(1), <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd/">clufter-pcs2pcscmd</a></i>(1), <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd-flatiron/">clufter-pcs2pcscmd-flatiron</a></i>(1), <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd-needle/">clufter-pcs2pcscmd-needle</a></i>(1), and perhaps more </p>
