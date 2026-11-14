---
title: "clufter(1)"
name: "clufter"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clufter/"
description: "clufter – CLUster FilTER"
---

<h2>NAME</h2>
<p> clufter &#8211; CLUster FilTER</p>
<h2>SYNOPSIS</h2>
<p> <code>clufter</code> [<i>&lt;global option&gt; </i>&#8230;] [<i>&lt;cmd&gt; </i>[<i>&lt;cmd option </i>&#8230;<i>&gt;</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Tool/library for transforming/analyzing cluster configuration formats </p>
<p> While primarily aimed at (CMAN,rgmanager)-&gt;(Corosync/CMAN,Pacemaker) cluster stacks configuration conversion (as per RHEL trend), the command-filter-format framework (capable of XSLT) offers also other uses through its plugin library.</p>
<h3>Commands (as available, but stable); built-in only, use &#8211;list to get all:</h3>
<dl>
<dt>ccs-artefacts</p>
<dd> Output artefacts referenced in the config. in CVS format</p>
<dt>ccs-disable-rg</p>
<dd> Make config. prevent RGManager from (accidentally) starting</p>
<dt>ccs-obfuscate</p>
<dd> Obfuscate credentials/IDs in CMAN-based cluster config.</p>
<dt>ccs-revitalize</p>
<dd> Migrate deprecated config&#8217;s props (agent params, etc.)</p>
<dt>ccs2pcs-flatiron</p>
<dd> (CMAN,rgmanager)-&gt;(Corosync/CMAN,Pacemaker) cluster cfg.</p>
<dt>ccs2pcs-needle</p>
<dd> (CMAN,rgmanager)-&gt;(Corosync v2,Pacemaker) cluster cfg.</p>
<dt>ccs2pcscmd-flatiron</p>
<dd> (CMAN,rgmanager) cluster cfg. -&gt; equivalent in pcs commands</p>
<dt>ccs2pcscmd-needle</p>
<dd> (CMAN,rgmanager) cluster cfg. -&gt; equivalent in pcs commands</p>
<dt>cib-revitalize</p>
<dd> Migrate deprecated configuration items in CIB</p>
<dt>cib2pcscmd</p>
<dd> CIB -&gt; equivalent in pcs commands</p>
<dt>cmd-wrap</p>
<dd> Wrap long lines carrying (fairly) convoluted shell commands</p>
<dt>pcs2pcscmd-flatiron</p>
<dd> (Corosync/CMAN,Pacemaker) cluster cfg. -&gt; reinstating pcs commands</p>
<dt>pcs2pcscmd-needle</p>
<dd> (Corosync v2,Pacemaker) cluster cfg. -&gt; reinstating pcs commands</dl>
<h3>Aliases thereof (environment-specific):</h3>
<dl>
<dt>ccs2pcs</p>
<dd> alias for ccs2pcs-needle</p>
<dt>ccs2pcscmd</p>
<dd> alias for ccs2pcscmd-needle</p>
<dt>pcs2pcscmd</p>
<dd> alias for pcs2pcscmd-needle</dl>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd> Standalone global options:</p>
<dt>
<dd> These take precedence over any command.</p>
<dt><code>-h</code> [CMD], <code>&#8211;help</code>=<i>[CMD]</i></p>
<dd> show help message (can be command-specific) and exit</p>
<dt><code>-H</code> [CMD], <code>&#8211;help-full</code>=<i>[CMD]</i></p>
<dd> full help message (can be command-specific) and exit</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> list commands and exit</p>
<dt><code>&#8211;list-dists</code>=<i>[VERBOSITY]</i></p>
<dd> (Advanced) list explicitly supported <code>&#8211;dist</code> option arguments and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show version details and exit</p>
<dt><code>-e</code> EXT_USER, <code>&#8211;ext</code>=<i>EXT_USER</i></p>
<dd> (Advanced) specify dir/s (as PATH/multiplied) scanned for plugins</p>
<dt><code>-s</code>, <code>&#8211;skip-ext</code></p>
<dd> do not use standard external plugins</p>
<dt><code>&#8211;completion-bash</code></p>
<dd> generate bash completion and exit</p>
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
<p> To get help for given command, just precede or follow it with <code>&#8211;help</code>.</p>
<h2>AUTHOR</h2>
<p> Written by Jan Pokorný &lt;jpokorny+pkg-clufter [at] redhat.com&gt; and plugin authors.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%207">https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%207</a>&amp;component=clufter&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Red Hat, Inc. Licensed under GPLv2+.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-clufter-ccs-artefacts/">clufter-ccs-artefacts</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs-disable-rg/">clufter-ccs-disable-rg</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs-obfuscate/">clufter-ccs-obfuscate</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs-revitalize/">clufter-ccs-revitalize</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcs/">clufter-ccs2pcs</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcs-flatiron/">clufter-ccs2pcs-flatiron</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcs-needle/">clufter-ccs2pcs-needle</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcscmd/">clufter-ccs2pcscmd</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcscmd-flatiron/">clufter-ccs2pcscmd-flatiron</a></i>(1), <i><a href="/docs/linux/man/1-clufter-ccs2pcscmd-needle/">clufter-ccs2pcscmd-needle</a></i>(1), <i><a href="/docs/linux/man/1-clufter-cib-revitalize/">clufter-cib-revitalize</a></i>(1), <i><a href="/docs/linux/man/1-clufter-cib2pcscmd/">clufter-cib2pcscmd</a></i>(1), <i><a href="/docs/linux/man/1-clufter-cmd-wrap/">clufter-cmd-wrap</a></i>(1), <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd/">clufter-pcs2pcscmd</a></i>(1), <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd-flatiron/">clufter-pcs2pcscmd-flatiron</a></i>(1), <i><a href="/docs/linux/man/1-clufter-pcs2pcscmd-needle/">clufter-pcs2pcscmd-needle</a></i>(1), and perhaps more </p>
<h2>Index</h2>
