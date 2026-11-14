---
title: "logconv-pl(1)"
name: "logconv-pl"
section: "1"
letter: "l"
url: "/docs/linux/man/1-logconv-pl/"
description: "logconv.pl – analyzes Directory Server access log files"
---

<p>logconv.pl &#8211; analyzes Directory Server access log files </p>
<h2>Synopsis</h2>
<p><code>logconv.pl </code> [<i>-h</i>] [<i>-d &lt;rootDN&gt;</i>] [<i>-s &lt;size limit&gt;</i>] [<i>-v</i>] [<i>-V</i>] [<i>-S &lt;start time&gt;</i>] [<i>-E &lt;end time&gt;</i>] [<i>-T &lt;min etime&gt;</i>] [<i>-efcibaltnxgjuU</i>] [<i> access log &#8230; &#8230; </i>] </p>
<h2>Description</h2>
<p>Analyzes Directory Server access log files for specific information defined on the command line</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>help/usage</p>
<dt><code>-d, &#8211;rootDN</code> &lt;Directory Managers DN&gt;</p>
<dd>DEFAULT -&gt; cn=directory manager</p>
<dt><code>-D, &#8211;data</code> &lt;Location for temporary data files&gt;</p>
<dd>DEFAULT -&gt; /tmp<br />
 TIP -&gt; If there is not enough RAM, a RAM disk can be used instead: </p>
<p>&nbsp;<wbr>mkdir&nbsp;<wbr>/dev/shm/logconv, and use this directory for the&nbsp;<wbr>&quot;-D&quot;&nbsp;<wbr>value.</p>
<dt><code>-s, &#8211;sizeLimit</code> &lt;Number of results to return per category&gt;</p>
<dd>DEFAULT -&gt; 20</p>
<dt><code>-X, &#8211;excludeIP</code> &lt;IP address to exclude from connection stats&gt;</p>
<dd>E.g. Load balancers</p>
<dt><code>-v, &#8211;version</code> show version of tool</p>
<dd>Print version of the tool</p>
<dt><code>-S, &#8211;startTime</code> &lt;time to begin analyzing logfile from&gt;</p>
<dd>Time to begin analyzing logfile from E.g. [28/Mar/2002:13:14:22 <code>-0800]</code></p>
<dt><code>-E, &#8211;endTime</code> &lt;time to stop analyzing logfile&gt;</p>
<dd>Time to stop analyzing logfile from E.g. [28/Mar/2002:13:24:62 <code>-0800]</code></p>
<dt><code>-T, &#8211;minEtime</code> &lt;minimum etime to report unindexed searches&gt;</p>
<dd>The minimum etime that is required to record and report on an unindexed search. Default is zero.</p>
<dt><code>-M, &#8211;reportFileMins</code> &lt;CSV output file&gt;</p>
<dd>This option creates a CSV report for spreadsheets.</p>
<dt><code>-m, &#8211;reportFileSecs</code> &lt;CSV output file&gt;</p>
<dd>This option creates a CSV report for spreadsheets.</p>
<dt><code>-B, &#8211;bind</code> &lt;ALL | ANONYMOUS | Bind DN&gt;</p>
<dd>This generates a report based on either ALL bind dn&#8217;s, anonymous binds, or a specific DN.</p>
<dt><code>-V, &#8211;verbose</code> &lt;enable verbose output &#8211; includes all stats listed below except U&gt;</p>
<dd>Verbose output</p>
<dt><code>-[efcibaltnxgjuU]</code></p>
<dd><code>e</code> Error Code stats<br />
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
 <code>u</code> Unindexed Search Stats (very detailed)<br />
 <code>y</code> Connection Latency Stats<br />
 <code>p</code> Open Connection ID Stats<br />
 <code>U</code> Unindexed Search Summary</dl>
<h2>Usage</h2>
<p>Examples:</p>
<dl>
<dd>logconv.pl <code>-s</code> 10 <code>-V</code> access</p>
<dd>logconv.pl <code>-d</code> &quot;cn=directory manager&quot; /export/server4/slapd-host/logs/access*</p>
<dd>logconv.pl <code>-s</code> 50 <code>-ibgju</code> access*</p>
<dd>logconv.pl <code>-S</code> &quot;[28/Mar/2002:13:14:22 <code>-0800]</code>&quot; <code>-E</code> &quot;[28/Mar/2002:13:50:05 <code>-0800]</code>&quot; <code>-e</code> access
</dl>
<h2>Author</h2>
<p>logconv.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution.</p>
