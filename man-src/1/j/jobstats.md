---

title: "jobstats(1)"
name: "jobstats"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jobstats/"
description: "jobstats – print historic job information or timeline view"
---

<p> <code>jobstats</code> [<code>-html</code>]<code>&nbsp;</code>[<code>-timeline</code>]<code>&nbsp;</code>[<code>-ntw</code>]<code>&nbsp;</code>[<code>-usage</code>] [<code>-available_slots</code> <i>s</i>] [<code>-start_jid</code> <i>jid</i>] [<code>-end_jid</code> <i>jid</i>] [<code>-owner</code> <i>opattern</i>] [<code>-name</code> <i>npatterm</i>] [<code>table_width</code> <i>w</i>] [<code>-nw</code> <i>w</i>] [<code>-nojoblist</code>]<code>&nbsp;</code>[<code>-tsort</code> <i>method</i>] [<i>file</i>&#8230;]</p>
<p> <i>jobstats</i> can show both a table of historic job information and a timeline view of job execution depending on output format (text or HTML). For the timeline view, the job is placed as a colour block on a timeline, and with one line per job. The colour of the job encodes a failed job, a qrsh login, a serial job and a parallel job. The job name is displayed and optionally followed by the number of slots used in braces in the case where a parallel job was run. </p>
<p> Note that some information may not be valid if the job failed with certain error codes. If only a certain job range is chosen, then the text output will be sized for the longest job name encountered. Use the <code>-nw</code> option to get around this if the field is very wide.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-start_jid&nbsp;</code><i>jid</i></dt>
<dd> Only start at job id <i>jid</i>. If <i>jid</i> is negative then start with this offset from the last job id in use (like <code>tail -n</code>).</dd>
<dt><code>-end_jid&nbsp;</code><i>jid</i></dt>
<dd> End at job id <i>jid</i>.</dd>
<dt><code>-owner&nbsp;</code><i>opattern</i></dt>
<dd> Only show output where the job owner matches the pattern. <code>-name&nbsp;</code><i>npattern</i> Only show output where the job name matches the pattern.</dd>
<dt><code>-ntw</code></dt>
<dd>
 Do not show the timing window (start and end times) for each job.</dd>
<dt><code>-tformat&nbsp;</code><i>fmt</i></dt>
<dd> Set time format for timing windows. Can be one of:<br />
 <code>epoch</code>: use Unix epoch time <code>fmt</code>: Specify format string. <code>-timeline</code> Produce a table with job timeline info showing visually where jobs ran. This forces HTML output.</dd>
<dt><code>-tsort&nbsp;</code><i>method</i></dt>
<dd> Define a method to sort the timeline:<br />
 <code>jid</code>: Sort by job id (default)<br />
 <code>start</code>: Sort by start time</dd>
<dt><code>-table_width&nbsp;</code><i>w</i></dt>
<dd> Define width of timeline table as <i>w</i> pixels (default 1100)</dd>
<dt><code>-nw&nbsp;</code><i>w</i></dt>
<dd>
 Limit the width of the job Name field in text output to <i>w</i>.</dd>
<dt><code>-nojoblist</code></dt>
<dd> Do not produce job list. <code>-html</code> Produce HTML output. <code>-usage</code> Show how each job&#8217;s slot usage aggregates. <code>-available_slots&nbsp;</code><i>s</i> Set the number of slots <i>s</i> available to jobs.</dd>
<dt><i>file</i></dt>
<dd> Job accounting file. If no file is given then <i>$SGE_ROOT/$SGE_CELL/common/accounting</i> will be used.</dd></dl>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>&nbsp;jobstats -start_jid 1070 sge_runs.acct<br />
&nbsp;<wbr>&nbsp;jobstats -start_jid -10<br />
&nbsp;<wbr>&nbsp;jobstats -html<br />
&nbsp;<wbr>&nbsp;jobstats -timeline -start_jid 1080<br />
&nbsp;<wbr>&nbsp;jobstats -tformat&nbsp;&#8216;%b_%e_%H:%M:%S&#8217;</p>
<h2>FILES</h2>
<p> <i>$SGE_ROOT/$SGE_CELL/common/accounting</i> </p>
