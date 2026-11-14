---
title: "amadmin(8)"
name: "amadmin"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amadmin/"
description: "amadmin – administrative interface to control Amanda backups"
---

<p>amadmin &#8211; administrative interface to control Amanda backups</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amadmin</code> [&#8211;version] [&#8211;no-default] [&#8211;print-source] [&#8211;exact-match] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> <i>command</i> [<i>command_options</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>Amadmin</code></p>
<dd>performs various administrative tasks on the <i>config</i> Amanda configuration. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>&#8211;version</code></p>
<dl>
<dd>Print the version and exit.</dl>
<p> <code>&#8211;no-default</code></p>
<dl>
<dd>Do not print default values for <code>config</code> and <code>disklist</code> commands.</dl>
<p> <code>&#8211;print-source</code></p>
<dl>
<dd>Print where a value is defined for <code>config</code> and <code>disklist</code> commands.</dl>
<p> <code>&#8211;exact-match</code></p>
<dl>
<dd>The host and disk are parsed as exact values</dl>
<h2>Commands</h2>
<p>Commands that take a <i>hostname</i> [ <i>disks</i> ] parameter pair operate on all disks in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) for that <i>hostname</i> if no disks are specified. Where <i>hostname</i> is also marked as being optional, the command operates on all hosts and disks in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) when no hostname is given. Both <i>hostname</i> and <i>disks</i> are match expressions; see <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) for a description. </p>
<p> <code>version</code></p>
<dl>
<dd>Show the current version and some compile time and runtime parameters. The <i>config</i> parameter must be present but is ignored.</dl>
<p> <code>estimate</code> [ <i>hostname</i> [ <i>disks</i> ]* ]*</p>
<dl>
<dd>Print the server estimate for the dles, each output lines have the following format: </p>
<pre> hostname diskname level size</pre>
<p>hostname</p>
<dl>
<dd>The quoted hostname</dl>
<p> diskname</p>
<dl>
<dd>The quoted diskname</dl>
<p> level</p>
<dl>
<dd>The level of the estimate</dl>
<p> size</p>
<dl>
<dd>The estimate size in kbytes</dl>
</dl>
<p> <code>force-bump</code> [ <i>hostname</i> [ <i>disks</i> ]* ]+</p>
<dl>
<dd>Force the <i>disks</i> on <i>hostname</i> to bump to a new incremental level during the next Amanda run.</dl>
<p> <code>force-no-bump</code> [ <i>hostname</i> [ <i>disks</i> ]* ]+</p>
<dl>
<dd>Force the <i>disks</i> on <i>hostname</i> to not bump to a new incremental level during the next Amanda run.</dl>
<p> <code>unforce-bump</code> [ <i>hostname</i> [ <i>disks</i> ]* ]+</p>
<dl>
<dd>Undo a previous <code>force-bump</code> or <code>force-no-bump</code> command.</dl>
<p> <code>force</code> [ <i>hostname</i> [ <i>disks</i> ]* ]+</p>
<dl>
<dd>Force the <i>disks</i> on <i>hostname</i> to do a full (level 0) backup during the next Amanda run.</dl>
<p> <code>unforce</code> [ <i>hostname</i> [ <i>disks</i> ]* ]+</p>
<dl>
<dd>Undo a previous <code>force</code> command.</dl>
<p> <code>reuse</code> <i>tapelabel</i> [ &#8230; ]</p>
<dl>
<dd>The tapes listed will be available for reuse at their point in the tape cycle.</dl>
<p> <code>no-reuse</code> <i>tapelabel</i> [ &#8230; ]</p>
<dl>
<dd>The tapes listed will not be reused when their turn comes up again in the tape cycle. Note that if this causes the number of reusable tapes to drop below the <code>amanda.conf</code> <i>tapecycle</i> value, Amanda will request new tapes until the count is satisfied again. </p>
<p> Tape marked <i>no-reuse</i> are available for recovery, marking them <i>no-reuse</i> is a security to be sure amanda will not overwrite them.</dl>
<p> <code>due</code> [ <i>hostname</i> [ <i>disks</i> ]* ]*</p>
<dl>
<dd>Show when the next full dump is due.</dl>
<p> <code>find</code> [ <code>&#8211;sort</code> <i>hkdlpbfw</i> ] [ <i>hostname</i> [ <i>disks</i> ]* ]*</p>
<dl>
<dd>Display all backups currently on tape or in the holding disk. The tape label or holding disk filename, file number, and status are displayed. </p>
<p> The <code>&#8211;sort</code> option changes the sort order using the following flags: </p>
<pre><i>h</i>: host name
<i>k</i>: disk name
<i>d</i>: dump timestamp
<i>l</i>: backup level
<i>p</i>: dump part
<i>b</i>: tape label
<i>f</i>: filenum on tape
<i>w</i>: write timestamp</pre>
<p>An uppercase letter reverses the sort order for that key. The default sort order is <code>hkdlpbfw</code>.</dl>
<p> <code>holding delete</code> <i>hostname</i> [ <i>disk</i> [ <i>datestamp</i> [ .. ] ] ]</p>
<dl>
<dd>Delete holding files matching the given specification. At least a hostname must be provided.</dl>
<p> <code>holding list</code> [-l] [-d] [ <i>hostname</i> [ <i>disk</i> [ <i>datestamp</i> [ .. ] ] ] ]</p>
<dl>
<dd>List holding files matching the given dump specification, or all holding files if no specification is provided. See <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) for more information on dump specifications. With &#8216;-l&#8217;, additional information (size, level, and whether the dump is outdated) is provided. With &#8216;-d&#8217;, only outdated dumps are shown. </p>
<p> An outdated holding file is one which is not required for a restore of the <i>most recent</i> dump. Note that outdated dumps may still be required for restores at earlier dates. For example, assume that a DLE had a level 0 on Monday, level 1&#8217;s Tuesday through Thursday, and a level 2 on Friday. Then the files required for a restore of Fridays (the most recent) dump are those from Monday (level 0), Thursday (level 1), and Friday (level 2). Tuesday and Wednesday&#8217;s files are outdated.</dl>
<p> <code>delete</code> [ <i>hostname</i> [ <i>disks</i> ]* ]+</p>
<dl>
<dd>Delete the specified <i>disks</i> on <i>hostname</i> from the Amanda database. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If you do not also remove the disk from the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file, Amanda will treat it as a new disk during the next run. </p>
</dl>
</dl>
<p> <code>tape</code></p>
<dl>
<dd>Display the tape(s) Amanda expects to write to during the next run. See also <code><a href="/docs/linux/man/8-amcheck/">amcheck</a></code>(8).</dl>
<p> <code>bumpsize</code></p>
<dl>
<dd>Display the current bump threshold parameters, calculated for all backup levels.</dl>
<p> <code>balance</code> [ <code>&#8211;days</code> <i>&lt;num&gt;</i> ]</p>
<dl>
<dd>Display the distribution of full backups throughout the dump schedule.</dl>
<p> <code>export</code> [ <i>hostname</i> [ <i>disks</i> ]* ]*</p>
<dl>
<dd>Convert records from the Amanda database to a text format that may be transmitted to another Amanda machine and <code>import</code>ed.</dl>
<p> <code>import</code></p>
<dl>
<dd>Convert <code>export</code>ed records read from standard input to a form Amanda uses and insert them into the database on this machine.</dl>
<p> <code>disklist</code> [ <i>hostname</i> [ <i>disks</i> ]* ]*</p>
<dl>
<dd>Display the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) information for each of the <i>disks</i> on <i>hostname</i> (or all hosts). Mostly used for debugging.</dl>
<p> <code>hosts</code></p>
<dl>
<dd>Output a list of distinct hosts in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5), one per line, for easy use in shell scripts.</dl>
<p> <code>dles</code></p>
<dl>
<dd>Output a list of distinct DLEs in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5), one per line with host and diskname separated by a space, for easy use in shell scripts.</dl>
<p> <code>info</code> [ <i>hostname</i> [ <i>disks</i> ]* ]*</p>
<dl>
<dd>Display the database record for each of the <i>disks</i> on <i>hostname</i> (or all hosts). Mostly used for debugging.</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Examples</h2>
<p>Request three specific file systems on <i>machine-a</i> get a full level 0 backup during the next Amanda run. </p>
<pre>$ amadmin daily force machine-a / /var /usr
amadmin: machine-a:/ is set to a forced level 0 tonight.
amadmin: machine-a:/var is set to a forced level 0 tonight.
amadmin: machine-a:/usr is set to a forced level 0 tonight.</pre>
<p>Request all file systems on <i>machine-b</i> get a full level 0 backup during the next Amanda run. </p>
<pre>$ amadmin daily force machine-b
amadmin: machine-b:/ is set to a forced level 0 tonight.
amadmin: machine-b:/var is set to a forced level 0 tonight.
amadmin: machine-b:/usr is set to a forced level 0 tonight.
amadmin: machine-b:/home is set to a forced level 0 tonight.</pre>
<p>Undo the previous <code>force</code> request for /home on <i>machine-b</i>. The other file systems will still get a full level 0 backup. </p>
<pre>$ amadmin daily unforce machine-b /home
amadmin: force command for machine-b:/home cleared.</pre>
<p>Locate backup images of /var from <i>machine-c</i>. The <i>tape or file</i> column displays either a tape label or a filename depending on whether the image is on tape or is still in the holding disk. If the image is on tape, the <i>file</i> column tells you which file on the tape has the image (file number zero is a tape label). This column shows zero and is not meaningful if the image is still in the holding disk. The <i>status</i> column tells you whether the backup was successful or had some type of error. </p>
<pre>$ amadmin daily find machine-c /var
date host disk lv tape or file file part status
2000-11-09 machine-c /var 0 000110 9 -- OK
2000-11-08 machine-c /var 2 000109 2 -- OK
2000-11-07 machine-c /var 2 /amanda/20001107/machine-c._var.2 0 OK
2000-11-06 machine-c /var 2 000107 2 -- OK
2000-11-05 machine-c /var 2 000106 3 -- OK
2000-11-04 machine-c /var 2 000105 2 -- OK
2000-11-03 machine-c /var 2 000104 2 -- OK
2000-11-02 machine-c /var 2 000103 2 -- OK
2000-11-01 machine-c /var 1 000102 5 -- OK
2000-10-31 machine-c /var 1 000101 3 -- OK</pre>
<p>Forget about the /workspace disk on <i>machine-d</i>. If you do not also remove the disk from the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file, Amanda will treat it as a new disk during the next run. </p>
<pre>$ amadmin daily delete machine-d /workspace
amadmin: machine-d:/workspace deleted from database.
amadmin: NOTE: you'll have to remove these from the <code><a href="//www.systutorials.com/docs/linux/man/5-disklist/">disklist</a></code>(5) yourself.</pre>
<p>Find the next tape Amanda will use (in this case, 123456). </p>
<pre>$ amadmin daily tape
The next Amanda run should go onto tape 123456 or a new tape.</pre>
<p>Show how well full backups are balanced across the dump cycle. The <i>due-date</i> column is the day the backups are due for a full backup. <i>#fs</i> shows the number of filesystems doing full backups that night, and <i>orig KB</i> and <i>out KB</i> show the estimated total size of the backups before and after any compression, respectively. </p>
<p> The <i>balance</i> column shows how far off that night&#8217;s backups are from the average size (shown at the bottom of the balance column). Amanda tries to keep the backups within +/- 5%, but since the amount of data on each filesystem is always changing, and Amanda will never delay backups just to rebalance the schedule, it is common for the schedule to fluctuate by larger percentages. In particular, in the case of a tape or backup failure, a bump will occur the following night, which will not be smoothed out until the next pass through the schedule. </p>
<p> The last line also shows an estimate of how many Amanda runs will be made between full backups for a file system. In the example, a file system will probably have a full backup done every eight times Amanda is run (e.g. every eight days). </p>
<pre>$ amadmin daily balance
 due-date #fs orig KB out KB balance
-------------------------------------------
11/10 Mon 21 930389 768753 +5.1%
11/11 Tue 29 1236272 733211 +0.2%
11/12 Wed 31 1552381 735796 +0.6%
11/13 Thu 23 1368447 684552 -6.4%
11/14 Fri 32 1065603 758155 +3.6%
11/15 Sat 14 1300535 738430 +0.9%
11/16 Sun 31 1362696 740365 +1.2%
11/17 Mon 30 1427936 773397 +5.7%
11/18 Tue 11 1059191 721786 -1.3%
11/19 Wed 19 1108737 661867 -9.5%
-------------------------------------------
TOTAL 241 12412187 7316312 731631 (estimated 8 runs per dumpcycle)</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amcheck/">amcheck</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/8-amfetchdump/">amfetchdump</a></code>(8), <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
