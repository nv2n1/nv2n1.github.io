---
title: "amreport(8)"
name: "amreport"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amreport/"
description: "amreport – generate a formatted output of statistics for an Amanda run"
---

<p>amreport &#8211; generate a formatted output of statistics for an Amanda run</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amreport</code> [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] [(1)&nbsp;<wbr><i>command-line options</i> | (2)&nbsp;<wbr><i>script options</i>] [<i>config</i>]</p>
<dd>
<dt> (1)&nbsp;<wbr>[&#8211;log=<i>logfile</i>] [&#8211;ps=<i>filename</i>] [&#8211;text=<i>filename</i>] [&#8211;xml=<i>filename</i>] [&#8211;print=<i>printer</i>] [&#8211;mail-text=<i>recipient</i>]</p>
<dt> (2)&nbsp;<wbr>[-i] [-M&nbsp;<wbr><i>address</i>] [-l&nbsp;<wbr><i>logfile</i>] [-f&nbsp;<wbr><i>outputfile</i>] [-p&nbsp;<wbr><i>postscriptfile</i>] [&#8211;from-amdump]</dl>
<h2>Description</h2>
<p><code>Amreport</code></p>
<dd>generates a summary report of an Amanda backup run. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><i>config</i></p>
<dl>
<dd>Name of the configuration to process. If no configuration name is specified, amanda.conf is read from the current directory.</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<p> Amreport operates in two distinct modes. Command-line mode is intended for use by an administrator from the command line, and uses long command-line options for clarity. Script mode is intended for use from scripts such as amdump, and has a lot of non-obvious default behaviors to suit that need. </p>
<p> Unless a script-mode option is given, amreport defaults to command-line mode. If no options are given, amreport writes a report for the most recent logfile to stdout.</p>
<h3>Command-Line Mode Options</h3>
<p><code>&#8211;log=</code><i>logfile</i></p>
<dl>
<dd>Use this logfile as the basis for the report. If this option is given, then the report is a &quot;historical&quot; report and will not include current state from e.g., holding disk and curinfo. If this option is not specified, then the most recent logfile will be used.</dl>
<p> <code>&#8211;ps=</code><i>filename</i></p>
<dl>
<dd>Write a postscript label to <i>filename</i>. See &quot;LABEL PRINTING&quot; below. If filename is not specified, then the label is written to stdout.</dl>
<p> <code>&#8211;text=</code><i>filename</i></p>
<dl>
<dd>Write a human-readable text report to <i>filename</i>. If filename is not specified, then the report is written to stdout.</dl>
<p> <code>&#8211;xml=</code><i>filename</i></p>
<dl>
<dd>Write an XML-formatted report to <i>filename</i>. If filename is not specified, then the report is written to stdout.</dl>
<p> <code>&#8211;print=</code><i>printer</i></p>
<dl>
<dd>Pipe a postscript label to <code>lp</code> or <code>lpr</code>, specifying the given <i>printer</i>. If the printer is not specified, uses the default from the Amanda configuration, or the system default printer.</dl>
<p> <code>&#8211;mail-text=</code><i>recipient</i></p>
<dl>
<dd>Send a human-readable text report to the given <i>recipient</i> via the mailer specified in the Amanda configuration. If the recipient is not specified, this uses the <i>mailto</i> from the Amanda configuration.</dl>
<h3>Script Mode Options</h3>
<p><code>-i</code></p>
<dl>
<dd>Don&#8217;t email the report.</dl>
<p> <code>-M</code> <i>address</i></p>
<dl>
<dd>Mail the report to <i>address</i> instead of the <code>mailto</code> value from <i>amanda.conf</i>.</dl>
<p> <code>-l</code> <i>logfile</i></p>
<dl>
<dd>Name of the log file to parse to generate the report. If a log file is not specified, it defaults to the file $logdir/log, where $logdir is the log directory defined in amanda.conf.</dl>
<p> <code>-f</code> <i>outputfile</i></p>
<dl>
<dd>Normally, <code>amreport</code> sends the report via e-mail to the <i>mailto</i> user as defined in the amanda.conf file. If <i>outputfile</i> is specified, then the report is put in <i>outputfile</i>.</dl>
<p> <code>-p</code> <i>postscriptfile</i></p>
<dl>
<dd>Send the postscript output to the file <i>postscriptfile</i> instead of to the <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1) command. This option has an effect only if the <i>lbl-templ</i> directive is specified in amanda.conf.</dl>
<p> <code>&#8211;from-amdump</code></p>
<dl>
<dd>Force script mode. Has no other effect.</dl>
<h2>Text Report Format</h2>
<p>Amanda&#8217;s text report format is divided into several sections. Some of these sections only appear if they are not empty. </p>
<p> Although newer versions of Amanda try to use the term &quot;volume&quot; to refer to a unit of storage, amreport still uses the term &quot;tape&quot;, even if backups are done to non-tape devices, to allow scripts which parse amreport&#8217;s output to continue to function.</p>
<h3>Summary</h3>
<pre>Hostname: bkserver
Org : DailySet1
Config : Daily
Date : February 25, 2009
These dumps were to tape Daily-103.
The next tape Amanda expects to use is: Daily-142
FAILURE DUMP SUMMARY:
 jamon.slikon.local /var lev 0 FAILED [/bin/tar exited with status 2]</pre>
<p>The summary section describes the run in broad terms, giving the server hostname, organization (from the <code>org</code> configuration parameter), configuration name, and dump date. This is followed by a description of the volumes and holding disk used, and an rough estimate of the volume(s) Amanda will use on the next run. </p>
<p> Brief notices of any unusual circumstances will also be included here.</p>
<h3>Statistics</h3>
<pre>STATISTICS:
 Total Full Incr.
 -------- -------- --------
Estimate Time (hrs:min) 0:00
Run Time (hrs:min) 0:01
Dump Time (hrs:min) 0:00 0:00 0:00
Output Size (meg) 1.6 0.0 1.6
Original Size (meg) 1.6 0.0 1.6
Avg Compressed Size (%) 100.0 100.0 100.0 (level:#disks ...)
Filesystems Dumped 4 1 3 (1:3)
Avg Dump Rate (k/s) 1555.1 134.2 1787.3
Tape Time (hrs:min) 0:00 0:00 0:00
Tape Size (meg) 1.6 0.0 1.6
Tape Used (%) 5.5 0.1 5.4 (level:#disks ...)
Filesystems Taped 4 1 3 (1:3)
 (level:#parts ...)
Parts Taped 4 1 3 (1:3)
Avg Tp Write Rate (k/s) 143966 27624.3 151811
USAGE BY TAPE:
 Label Time Size % DLEs Parts
 metals-013 0:00 1650k 5.4 4 4</pre>
<p>This section contains aggregate statistics for the entire run. The three columns break down the results into a total for all data handled, only full dumps, and only incremental dumps. In the right margin, amreport indicates the breakdown of dump levels at the dumper and the taper. </p>
<p> The rows have the following meanings: </p>
<p> Estimate Time</p>
<dl>
<dd>The time used by the planner to estimate dump sizes.</dl>
<p> Run Time</p>
<dl>
<dd>Total runtime, from the invocation of amdump to its completion.</dl>
<p> Dump Time</p>
<dl>
<dd>Total time spent dumping clients.</dl>
<p> Output Size</p>
<dl>
<dd>Total quantity of data dumped, after compression.</dl>
<p> Original Size</p>
<dl>
<dd>Total quantity of data dumped, before compression.</dl>
<p> Avg Compressed Size</p>
<dl>
<dd>Compression ratio, calculated from the previous two rows.</dl>
<p> Filesystems Dumped</p>
<dl>
<dd>Number of DLEs dumped.</dl>
<p> Avg Dump Rate</p>
<dl>
<dd>Average speed at which clients produced data. Note that, for dumps done directly to a slow device, rather than to holding disk, this rate may reflect a write speed constrained by the device speed.</dl>
<p> Tape Time</p>
<dl>
<dd>Total time spent writing to storage volumes. This includes time spent changing tapes, including time spent waiting for flush thresholds to be met.</dl>
<p> Tape Size</p>
<dl>
<dd>Total quantity of data written to storage volumes.</dl>
<p> Tape Used</p>
<dl>
<dd>Fraction of the total allocated storage (tapetype length times runtapes) actually used.</dl>
<p> Filesystems Taped</p>
<dl>
<dd>Number of filesystems written to storage. This may be larger or smaller than the number of filesystems dumped, due to flushes or dumps left on holding disk.</dl>
<p> Parts Taped</p>
<dl>
<dd>Number of split parts writtten to storage. If this number is very large, then the split size may be too small.</dl>
<p> Avg Tp Write Rate</p>
<dl>
<dd>Taper speed, based on the tape time and tape size, above. Note that, because the tape time includes time spent on tasks other than writing to tape, this does not necessary reflect the device&#8217;s real write speed. However, the value is useful for capacity planning, as it reflects a realistic estimate of how quickly Amanda can write data to storage.</dl>
<h3>Usage by Tape</h3>
<pre>USAGE BY TAPE:
 Label Time Size % DLEs Parts
 Conf-001 0:00 20320k 66.2 1 4
 Conf-002 0:00 6470k 21.1 0 2</pre>
<p>This short section gives per-volume statistics: time spent writing to the volume; bytes written to the volume; portion of the expected tape length used; number of DLEs started, and total number of split parts written.</p>
<h3>Notes</h3>
<pre>NOTES:
 taper: tape DAILY-37 kb 30720 fm 3 [OK]</pre>
<p>This section contains any informational log messages from the run. Most messages are self-explanatory. The taper message shown in the example is always present, and is redundant to the previous section. It indicates that 30720 kb were written to &quot;DAILY-37&quot; in 3 files.</p>
<h3>Failure and Strange Details</h3>
<pre>FAILED DUMP DETAILS:
/-- jamon.slikon.local /var lev 0 FAILED [/bin/tar exited with status 2]
sendbackup: info BACKUP=APPLICATION
sendbackup: info APPLICATION=amgtar
sendbackup: info RECOVER_CMD=/usr/bin/gzip -dc |amgtar -f... -
sendbackup: info COMPRESS_SUFFIX=.gz
sendbackup: info end
? /bin/tar: ./gdm: Cannot savedir: Permission denied
| Total bytes written: 943831040 (901MiB, 4.9MiB/s)
| /bin/tar: Error exit delayed from previous errors
sendbackup: error [/bin/tar exited with status 2]
sendbackup: size 921710
sendbackup: end
\--------
STRANGE DUMP DETAILS:
/-- bsdfw.slikon.local / lev 0 STRANGE
sendbackup: info BACKUP=APPLICATION
sendbackup: info APPLICATION=amgtar
sendbackup: info RECOVER_CMD=/usr/bin/gzip -dc |amgtar -f... -
sendbackup: info COMPRESS_SUFFIX=.gz
sendbackup: info end
| /bin/tar: ./tmp/.X11-unix/X0: socket ignored
| Total bytes written: 5530869760 (5.2GiB, 3.0MiB/s)
sendbackup: size 5401240
sendbackup: end
\--------</pre>
<p>This section expands on failures and strange results indicated in earlier sections. In both cases, the details contain a messages produced by the underlying backup tool &#8211; GNU tar, in this example. Failed dumps have actually failed, and the reasons are usually clear. Strange dumps, however, are regarded as successful by Amanda, but contain messages that Amanda did not recognize and which may be of interest to the operator.</p>
<h3>Dump Summary</h3>
<pre>DUMP SUMMARY:
 DUMPER STATS TAPER STATS
HOSTNAME DISK L ORIG-kB OUT-kB COMP% MMM:SS KB/s MMM:SS KB/s
-------------------------- ------------------------------------- ---------------
strontium /etc 1 270 270 -- 0:00 1146.3 0:00 140918.6
strontium -me/elantra 1 10 10 -- 0:00 65.6 0:00 9033.4
strontium /local 0 20 20 -- 0:00 133.9 0:00 27624.3
strontium -ository_13 1 1350 1350 -- 0:01 2568.5 0:00 175006.5</pre>
<p>The dump summary table has one row for each DLE processed during the run. The &quot;L&quot; column gives the level of the dump. The remaining colums are divided into dumper stats and taper stats. </p>
<p> The dumper stats give the original (before compression) and output (after compression) size of each dump, as well as a compression ratio, if applicable. The column labeled &quot;MMM:SS&quot; gives the time spent on that dump, and the next column is the calculated dump rate. </p>
<p> The taper stats give the time and speed with which the dump was written to storage. This value is the sum of the times for each part, and as such does not include time spent switching volumes.</p>
<h2>Label Printing</h2>
<p>Amanda can print postscript labels describing the contents of tape(s) written in a run. The labels are designed to be folded and inserted into the tape case along with the tape or hole punched and put in a 3-ring binder. Various label templates are provided to format data for different tape sizes. </p>
<p> The information printed varies slightly between label templates due to size constraints. Labels contain one line for each host/file-system pair and may also contain the file number on the tape, the level of the dump, the original size of the dump and the size of the (possibly compressed) tape file. </p>
<p> Add the <i>lbl-templ</i> parameter to the tapetype definition in amanda.conf to enable labels. If you don&#8217;t add this line to your tapetype definition, <code>amreport</code> will not print tape labels. </p>
<p> You may use the <i>printer</i> keyword in amanda.conf to print to other than the system default printer.</p>
<h2>Templates</h2>
<p>Amanda provides label templates for the following tape types. These are pretty generic labels and should be easy to customize for other tape types or particular site needs. </p>
<dl>
<dd>
<pre>* ExaByte 8mm tapes
* DAT 4mm tapes
* DLT tapes
* 3-ring binder</pre>
</dl>
<p> The 3-ring binder type is the most generic. It may be used to make a hardcopy log of the tapes.</p>
<h2>Exit Code</h2>
<p>The exit code of <code>amreport</code> is the ORed value of: </p>
<pre> 0 = success
 1 = error
 2 = a dle give strange message
 4 = a dle failed
 8 = Don't know the status of a dle (RESULT_MISSING in the report)
 16 = tape error or no more tape</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amflush/">amflush</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
