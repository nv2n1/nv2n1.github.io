---
title: "logconv(1)"
name: "logconv"
section: "1"
letter: "l"
url: "/docs/linux/man/1-logconv/"
description: "logconv.pl – analyzes Directory Server access log files"
---

<h2 class="name">NAME</h2>
<p> logconv.pl &#8211; analyzes Directory Server access log files </p>
<h2>SYNOPSIS</h2>
<p> <code>logconv.pl </code> [<i>-h</i>] [<i>-d &lt;rootDN&gt;</i>] [<i>-s &lt;size limit&gt;</i>] [<i>-v</i>] [<i>-V</i>] [<i>-S &lt;start time&gt;</i>] [<i>-E &lt;end time&gt;</i>] [<i>-efcibaltnxgju</i>] [<i> access log &#8230; &#8230; </i>] </p>
<h2>DESCRIPTION</h2>
<p> Analyzes Directory Server access log files for specific information defined on the command line</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-h</code></p>
<dd> help/usage</p>
<dt><code>-d</code> &lt;Directory Managers DN&gt;</p>
<dd> DEFAULT -&gt; cn=directory manager</p>
<dt><code>-s</code> &lt;Number of results to return per category&gt;</p>
<dd> DEFAULT -&gt; 20</p>
<dt><code>-X</code> &lt;IP address to exclude from connection stats&gt;</p>
<dd> E.g. Load balancers</p>
<dt><code>-v</code> show version of tool</p>
<dd> Print version of the tool</p>
<dt><code>-S</code> &lt;time to begin analyzing logfile from&gt;</p>
<dd> Time to begin analyzing logfile from E.g. [28/Mar/2002:13:14:22 <code>-0800]</code></p>
<dt><code>-E</code> &lt;time to stop analyzing logfile&gt;</p>
<dd> Time to stop analyzing logfile from E.g. [28/Mar/2002:13:24:62 <code>-0800]</code></p>
<dt><code>-V</code> &lt;enable verbose output &#8211; includes all stats listed below&gt;</p>
<dd> Verbose output</p>
<dt><code>-[efcibaltnxgju]</code></p>
<dd>
 <code>e</code> Error Code stats<br />
 <code>f</code> Failed Login Stats<br />
 <code>c</code> Connection Code Stats<br />
 <code>i</code> Client Stats<br />
 <code>b</code> Bind Stats<br />
 <code>a</code> Search Base Stats<br />
 <code>l</code> Search Filter Stats<br />
 <code>t</code> Etime Stats<br />
 <code>n</code> Nentries Stats<br />
 <code>x</code> Extended Operations<br />
 <code>r</code> Most Requested Attribute Stats<br />
 <code>g</code> Abandoned Operation Stats<br />
 <code>j</code> Recommendations<br />
 <code>u</code> Unindexed Search Stats<br />
 <code>y</code> Connection Latency Stats<br />
 <code>p</code> Open Connection ID Stats</dl>
<h2>USAGE</h2>
<p> Examples:</p>
<dl>
<dt>
<dd> logconv.pl <code>-s</code> 10 <code>-V</code> access</p>
<dt>
<dd> logconv.pl <code>-d</code> &quot;cn=directory manager&quot; /export/server4/slapd-host/logs/access*</p>
<dt>
<dd> logconv.pl <code>-s</code> 50 <code>-ibgju</code> access*</p>
<dt>
<dd> logconv.pl <code>-S</code> &quot;[28/Mar/2002:13:14:22 <code>-0800]</code>&quot; <code>-E</code> &quot;[28/Mar/2002:13:50:05 <code>-0800]</code>&quot; <code>-e</code> access
</dl>
<h2>AUTHOR</h2>
<p> logconv.pl was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
