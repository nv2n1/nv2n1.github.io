---

title: "qstatus(1)"
name: "qstatus"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qstatus/"
description: "qstatus – xxQS_NAMExx qstatus script"
---

<p> qstatus &#8211; xxQS_NAMExx qstatus script </p>
<h2>SYNOPSIS</h2>
<p> <code>qstatus</code> [<code>-acghjlmnot</code>] [<code>-s </code><i>SORT_FIELD_LIST</i>] [<i>USER</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents <code>qstatus</code>, a script to reformat the output of the xxQS_NAMExx command </p>
<p> The reformatted list is by default limited to the actual user account. This can be changed to request a job list of any user by supplying the username <i>USER</i> as the last argument, or requesting an output for all users by the <code>-a</code> switch (see below).</p>
<h3>Options</h3>
<dl>
<dt><code>-a</code></dt>
<dd> Display the jobs of all users. May not be used when there is a dedicated user specified. This also implies the output of the owner of the jobs.</dd>
<dt><code>-c</code></dt>
<dd> Calculate a statistic of the listed jobs.</dd>
<dt><code>-g</code></dt>
<dd> Group output by owner. Only applicable if the owner is listed, either by the <code>-o</code> switch or implied by <code>-a</code>. This is a short form of &#8216;<code>-s</code> <code>owner</code>,<code>running</code>&#8216;. Can&#8217;t be used together with the <code>-s</code> option.</dd>
<dt><code>-h</code></dt>
<dd> Print help.</dd>
<dt><code>-j</code></dt>
<dd> Include jobs which are suspended.</dd>
<dt><code>-l</code></dt>
<dd> Suppress the output of the list of jobs. Maybe useful in case you are only interested in the statistic with the <code>-c</code> switch.</dd>
<dt><code>-m</code></dt>
<dd> Display the machine instead of the name of the queue the job is running in under the column &#8216;running in&#8217;. Only meaningful for SGE 6.0 or above.</dd>
<dt><code>-n</code></dt>
<dd> Suppress the listing of the individual owner, mostly useful when all jobs are listed. Takes precedence over any other implied options. If used together with <code>-o</code>, only the later one is relevant.</dd>
<dt><code>-o</code></dt>
<dd> List the owner of the individual job. Takes precedence over any other implied option. If used together with <code>-n</code>, only the later one is relevant.</dd>
<dt><code>-r</code></dt>
<dd> Display times relative to submit- or start-times, as appropriate.</dd>
<dt><code>-s </code><i>SORT_FIELD_LIST</i></dt>
<dd> Sort the output according to the given columns. The <i>SORT_FIELD_LIST</i> has the format <i>SORT_FIELD_LIST</i>=<i>SORT_FIELD</i>[,<i>SORT_FIELD</i>]* where <i>SORT_FIELD</i> can be one of <code>job</code>, <code>name</code>, <code>none</code>, <code>owner</code>, <code>running</code>, <code>slots</code>, <code>time</code>.</dd>
<dl>
<dt>
</dt><dd>
<p> The option <code>none</code> will supersede any other column names and set the complete sort order to none. </p>
<p> The column <code>owner</code> can only be used if the owner of the job is displayed at all. Otherwise it will be ignored. </p>
<p> The sort by <code>running</code> will only be used for the running jobs, not for the waiting ones. </p>
<p> This will overwrite the default sort order, which is: </p>
</dd><dl>
<dl>
<dt>running jobs:</dt>
<dd> <code>running</code></dd>
<dt>waiting jobs:</dt>
<dd> <code>none</code></dd></dl>
</dl>
<p> If the option <code>-g</code> is specified, the default sort order is changed to: </p>
<dl>
<dl>
<dt>running jobs:</dt>
<dd> <code>owner</code>,<code>running</code></dd>
<dt>waiting jobs:</dt>
<dd> <code>owner</code> </dd>
</dl>
</dl>
</dl>
<dt><code>-t</code></dt>
<dd> Append task ID to the jobname for array tasks. This option has no meaning for non-array jobs.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Reuti.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;reuti [at] staff.uni-marburg.de&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2010 Philipps-University of Marburg.<br/>
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;URL: <a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a> &gt;. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> of xxQS_NAMExx.</p>
<h2>BUGS</h2>
<p> Does not support the PBS or Torque resource manager. The Awk script used probably isn&#8217;t portable and may require GNU Awk version 3 or higher. </p>
