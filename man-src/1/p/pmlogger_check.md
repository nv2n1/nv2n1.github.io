---
title: "pmlogger_check(1)"
name: "pmlogger_check"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogger_check/"
description: "pmlogger_check, pmlogger_daily, pmlogger_merge – administration of Performance Co-Pilot archive log files"
---

<h2>NAME</h2>
<p> <code>pmlogger_check</code>, <code>pmlogger_daily</code>, <code>pmlogger_merge</code> &#8211; administration of Performance Co-Pilot archive log files</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmlogger_check</code> [<code>-CNsTV</code>] [<code>-c</code> <i>control</i>] [<code>-l</code> <i>logfile</i>]<br />
 <code>$PCP_BINADM_DIR/pmlogger_daily</code> [<code>-NorV</code>] [<code>-c</code> <i>control</i>] [<code>-k</code> <i>discard</i>] [<code>-l</code> <i>logfile</i>] [<code>-m</code> <i>addresses</i>] [<code>-s</code> <i>size</i>] [<code>-t</code> <i>want</i>] [<code>-x</code> <i>compress</i>] [<code>-X</code> <i>program</i>] [<code>-Y</code> <i>regex</i>]<br />
 <code>$PCP_BINADM_DIR/pmlogger_merge</code> [<code>-fNV</code>] [<i>input-basename</i> &#8230; <i>output-name</i>] </p>
<h2>DESCRIPTION</h2>
<p> This series of shell scripts and associated control files may be used to create a customized regime of administration and management for Performance Co-Pilot (see <code><a href="/docs/linux/man/1-pcpintro/">PCPintro</a></code>(1)) archive log files. </p>
<p> <code>pmlogger_daily</code> is intended to be run once per day, preferably in the early morning, as soon after midnight as practicable. Its task is to aggregate and rotate one or more sets of PCP archives. After some period, old PCP archives are discarded. This period is 14 days by default, but may be changed using the <code>-k</code> option. Two special values are recognized for the period (<i>discard</i>), namely <code>0</code> to keep no archives beyond the current one, and <code>forever</code> to prevent any archives being discarded. </p>
<p> Archive data files can optionally be compressed after some period to conserve disk space. This is particularly useful for large numbers of <code>pmlogger</code> processes under the control of <code>pmlogger_check</code>. By default no compression is done. The <code>-x</code> option enables compression and specifies the number of days after which to compress archive data files, and the <code>-X</code> option specifies the program to use for compression &#8211; by default this is <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1). Use of the <code>-Y</code> option allows a regular expression to be specified causing files in the set of files matched for compression to be omitted &#8211; this allows only the data file to be compressed, and also prevents the program from attempting to compress it more than once. The default <i>regex</i> is &quot;.(meta|index|Z|gz|bz2|zip|xz|lzma|lzo|lz4)$&quot; &#8211; such files are filtered using the <code>-v</code> option to <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1). </p>
<p> To accommodate the evolution of PMDAs and changes in production logging environments, <code>pmlogger_daily</code> is integrated with <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1) to allow optional and automatic rewriting of archives before merging. If there are global rewriting rules to be applied across all archives mentioned in the control file(s), then create the directory <code>$PCP_SYSCONF_DIR/pmlogrewrite</code> and place any <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1) rewriting rules in this directory. For rewriting rules that are specific to only one family of archives, use the directory name from the control file(s) &#8211; i.e. the <i>fourth</i> field &#8211; and create a file, or a directory, or a symbolic link named <code>pmlogrewrite</code> within this directory and place the required rewriting rule(s) in the <code>pmlogrewrite</code> file or in files within the <code>pmlogrewrite</code> subdirectory. <code>pmlogger_daily</code> will choose rewriting rules from the archive directory if they exist, else rewriting rules from <code>$PCP_SYSCONF_DIR/pmlogrewrite</code> if that directory exists, else no rewriting is attempted. </p>
<p> The <code>-r</code> command line option acts as an over-ride and prevents all archive rewriting with <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1) independent of the presence of any rewriting rule files or directories. </p>
<p> By default all possible archives will be merged. The <code>-o</code> option reinstates the old behaviour in which only yesterday&#8217;s archives will be considered as merge candidates. </p>
<p> In the special case where only a single input archive needs to be merged, <code><a href="/docs/linux/man/1-pmlogmv/">pmlogmv</a></code>(1) is used to rename the archive, rather than copy the input archive using <code>pmlogger_merge</code>. </p>
<p> The <code>-M</code> option may be used to disable archive merging (or renaming) and rewriting (<code>-M</code> implies <code>-r</code>). This is most useful in cases where the archives are being incrementally copied to a remote repository, e.g. using <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1). Merging, renaming and rewriting all risk an increase in the synchronization load, especially immediately after <code>pmlogger_daily</code> has run, so <code>-M</code> may be useful in these cases. </p>
<p> To assist with debugging or diagnosing intermittent failures the <code>-t</code> option may be used. This will turn on very verbose tracing (<code>-VV</code>) and capture the trace output in a file named <code>$PCP_LOG_DIR/pmlogger/daily.</code><i>datestamp</i><code>.trace,</code> where <i>datestamp</i> is the time <code>pmlogger_daily</code> was run in the format YYYYMMDD.HH.MM. In addition, the <i>want</i> argument will ensure that trace files created with <code>-t</code> will be kept for <i>want</i> days and then discarded. </p>
<p> In addition, if the PCP &#8220;notices&#8221; file (<code>$PCP_LOG_DIR/NOTICES</code>) is larger than 20480 bytes, <code>pmlogger_daily</code> will rename the file with a &#8220;.old&#8221; suffix, and start a new &#8220;notices&#8221; file. The rotate threshold may be changed from 20480 to <i>size</i> bytes using the <code>-s</code> option. </p>
<p> Use of the <code>-m</code> option causes <code>pmlogger_daily</code> to construct a summary of the &#8220;notices&#8221; file entries which were generated in the last 24 hours, and e-mail that summary to the set of space-separated <i>addresses</i>. This daily summary is stored in the file <code>$PCP_LOG_DIR/NOTICES.daily</code>, which will be empty when no new &#8220;notices&#8221; entries were made in the previous 24 hour period. </p>
<p> The script <code>$PCP_BINADM_DIR/pmlogger_daily</code> could be copied and modified to implement a site-specific procedure for end-of-week and/or end-of-month management for a set of PCP archives. </p>
<p> <code>pmlogger_check</code> may be run at any time, and is intended to check that the desired set of <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) processes are running, and if not to re-launch any failed loggers. Use of the <code>-s</code> option provides the reverse functionality, allowing the set of <code>pmlogger</code> processes to be cleanly shutdown. Use of the <code>-C</code> option queries the system service runlevel information for <code>pmlogger</code>, and uses that to determine whether to start processes. </p>
<p> The <code>-T</code> option provides a terser form of output for <code>pmlogger_check</code> that is most suitable for a <i>pmlogger</i> &#8220;farm&#8221; where many instances of <i>pmlogger</i> are expected to be running. </p>
<p> <code>pmlogger_merge</code> is a wrapper script for <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1) that merges all of the archive logs matching the <i>input-basename</i> arguments, and creates a new archive using <i>output-name</i> as the base name for the physical files that constitute an archive log. The <i>input-basename</i> arguments may contain meta characters in the style of <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1). If specified, the <code>-f</code> option causes all of the input files to be removed once the output archive has been created. </p>
<p> <code>pmlogger_merge</code> is used by <code>pmlogger_daily</code>. </p>
<p> Both <code>pmlogger_daily</code> and <code>pmlogger_check</code> are controlled by PCP logger control file(s) that specifies the <code>pmlogger</code> instances to be managed. The default control file is <code>$PCP_PMLOGGERCONTROL_PATH</code>, but an alternate may be specified using the <code>-c</code> option. If the directory <code>$PCP_PMLOGGERCONTROL_PATH</code>.d (or <i>control</i>.d from the <code>-c</code> option) exists, then the contents of any additional control files therein will be appended to the main control file (which must exist). </p>
<p> <code>Warning</code>: The <code>$PCP_PMLOGGERCONTROL_PATH</code> and <code>$PCP_PMLOGGERCONTROL_PATH</code>.d files must not be writable by any user other than root. </p>
<p> The control file(s) should be customized according to the following rules that define for the current version (1.1) of the control file format.</p>
<dl>
<dt>1.</p>
<dd> Lines beginning with a &#8220;#&#8221; are comments.</p>
<dt>2.</p>
<dd> Lines beginning with a &#8220;$&#8221; are assumed to be assignments to environment variables in the style of <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), and all text following the &#8220;$&#8221; will be <code>eval</code>&#8216;ed by the script reading the control file, and the corresponding variable exported into the environment. This is particularly useful to set and export variables into the environment of the administrative scripts, e.g. </p>
<pre>
$ PMCD_CONNECT_TIMEOUT=20
</pre>
<dt>3.</p>
<dd> There <code>must</code> be a version line in the initial control file of the form: </p>
<pre>
$ version=1.1
</pre>
<dt>4.</p>
<dd> There should be one line in the control file(s) for each <code>pmlogger</code> instance of the form: </p>
<pre>
<i>host</i> <code>y</code>|<code>n</code> <code>y</code>|<code>n</code> <i>directory</i> <i>args</i>
</pre>
<dt>5.</p>
<dd> Fields within a line of the control file(s) are usually separated by one or more spaces or tabs (although refer to the description of the <i>directory</i> field for some important exceptions).</p>
<dt>6.</p>
<dd> The <i>first</i> field is the name of the host that is the source of the performance metrics for this <code>pmlogger</code> instance.</p>
<dt>7.</p>
<dd> The <i>second</i> field indicates if this is a <i>primary</i> <code>pmlogger</code> instance (<code>y</code>) or not (<code>n</code>). Since the primary logger must run on the local host, and there may be at most one primary logger for a particular host, this field can be <code>y</code> for at most one <code>pmlogger</code> instance, in which case the host name must be the name of the local host.</p>
<dt>8.</p>
<dd> The <i>third</i> field indicates if this <code>pmlogger</code> instance needs to be started under the control of <code><a href="/docs/linux/man/1-pmsocks/">pmsocks</a></code>(1) to connect to a <code>pmcd</code> through a firewall (<code>y</code> or <code>n</code>).</p>
<dt>9.</p>
<dd> The <i>fourth</i> field is a directory name. All files associated with this <code>pmlogger</code> instance will be created in this directory, and this will be the current directory for the execution of any programs required in the maintenance of those archives. A useful convention is that primary logger archives for the local host with hostname <i>myhost</i> are maintained in the directory <code>$PCP_LOG_DIR/pmlogger/</code><i>myhost</i> (this is where the default <code>pmlogger</code> start-up script in <code>$PCP_RC_DIR/pcp</code> will create the archives), while archives for the remote host <i>mumble</i> are maintained in <code>$PCP_LOG_DIR/pmlogger/</code><i>mumble</i>.</p>
<dt>10.</p>
<dd> The directory field may contain embedded shell syntax that will be evaluated by <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) to produce the real directory name to be used. The allowed constructs are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Any text (including white space) enclosed with <code>$(</code> and <code>).</code></p>
<dt>&bull;</p>
<dd> Any text (including white space) enclosed with <code>`</code> and <code>`</code> (back quotes).</p>
<dt>&bull;</p>
<dd> Any text (including white space) enclosed with <code>&quot;</code> and <code>&quot;</code> (double quotes).</p>
<dt>&bull;</p>
<dd> Any word containing a <code>$</code> (assumed to introduce an environment variable name). <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) and/or <code><a href="/docs/linux/man/1-pmnewlog/">pmnewlog</a></code>(1). Most typically this would be the <code>-c</code> option.</dl>
<p> The following sample control lines specify a primary logger on the local host (<i>bozo</i>), and non-primary loggers to collect and log performance metrics from the hosts <i>wobbly</i> and <i>boing</i>. </p>
<pre>
$version=1.1
bozo   y  n  $PCP_LOG_DIR/pmlogger/bozo   -c config.default
wobbly n  n  &quot;/store/wobbly/$(date +%Y)&quot;  -c ./wobbly.config
boing  n  n  $PCP_LOG_DIR/pmlogger/boing  -c ./pmlogger.config
</pre>
<p> Typical <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5) entries for periodic execution of <code>pmlogger_daily</code> and <code>pmlogger_check</code> are given in <code>$PCP_SYSCONF_DIR/pmlogger/crontab</code> (unless installed by default in <i>/etc/cron.d</i> already) and shown below. </p>
<pre>
# daily processing of archive logs
14      0       *       *       *       $PCP_BINADM_DIR/pmlogger_daily
# every 30 minutes, check pmlogger instances are running
25,55   *       *       *       *       $PCP_BINADM_DIR/pmlogger_check
</pre>
<p> In order to ensure that mail is not unintentionally sent when these scripts are run from <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) diagnostics are always sent to a log file. By default, this file is <code>$PCP_LOG_DIR/pmlogger/pmlogger_daily.log</code> or <code>$PCP_LOG_DIR/pmlogger/pmlogger_check.log</code> but this can be changed using the <code>-l</code> option. If this log file already exists when the script starts, it will be renamed with a <i>.prev</i> suffix (overwriting any log file saved earlier) before diagnostics are generated to the log file. The <code>-l</code> and <code>-t</code> options cannot be used together. </p>
<p> The output from the <code>cron</code> execution of the scripts may be extended using the <code>-V</code> option to the scripts which will enable verbose tracing of their activity. By default the scripts generate no output unless some error or warning condition is encountered. </p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMLOGGERCONTROL_PATH</code></p>
<dd> the PCP logger control file<br />
 <code>Warning</code>: this file must not be writable by any user other than root.</p>
<dt><code>$PCP_PMLOGGERCONTROL_PATH</code>.d</p>
<dd> optional directory containing additional PCP logger control files, typically one per host<br />
 <code>Warning</code>: the files herein must not be writable by any user other than root.</p>
<dt><code>$PCP_SYSCONF_DIR/pmlogger/crontab</code></p>
<dd> sample crontab for automated script execution by $PCP_USER (or root). Exists only if the platform does not support the /etc/cron.d mechanism.</p>
<dt><code>$PCP_VAR_DIR/config/pmlogger/config.default</code></p>
<dd> default <code>pmlogger</code> configuration file location for the local primary logger, typically generated automatically by <code><a href="/docs/linux/man/1-pmlogconf/">pmlogconf</a></code>(1).</p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i></p>
<dd> default location for archives of performance information collected from the host <i>hostname</i></p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i><code>/lock</code></p>
<dd> transient lock file to guarantee mutual exclusion during <code>pmlogger</code> administration for the host <i>hostname</i> &#8211; if present, can be safely removed if neither <code>pmlogger_daily</code> nor <code>pmlogger_check</code> are running</p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i><code>/Latest</code></p>
<dd> PCP archive folio created by <code><a href="/docs/linux/man/1-mkaf/">mkaf</a></code>(1) for the most recently launched archive containing performance metrics from the host <i>hostname</i></p>
<dt><code>$PCP_LOG_DIR/NOTICES</code></p>
<dd> PCP &#8220;notices&#8221; file used by <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) and friends</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1), <code><a href="/docs/linux/man/1-pmlogconf/">pmlogconf</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogmv/">pmlogmv</a></code>(1), <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1), <code><a href="/docs/linux/man/1-pmnewlog/">pmnewlog</a></code>(1), <code><a href="/docs/linux/man/1-pmsocks/">pmsocks</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) and <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8). </p>
<h2>Index</h2>
