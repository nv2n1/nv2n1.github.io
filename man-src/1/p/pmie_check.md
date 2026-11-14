---
title: "pmie_check(1)"
name: "pmie_check"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmie_check/"
description: "pmie_check, pmie_daily – administration of the Performance Co-Pilot inference engine"
---

<h2>NAME</h2>
<p> <code>pmie_check</code>, <code>pmie_daily</code> &#8211; administration of the Performance Co-Pilot inference engine</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmie_check</code> [<code>-CNsV</code>] [<code>-c</code> <i>control</i>] [<code>-l</code> <i>logfile</i>]<br />
 <code>$PCP_BINADM_DIR/pmie_daily</code> [<code>-NV</code>] [<code>-c</code> <i>control</i>] [<code>-k</code> <i>discard</i>] [<code>-l</code> <i>logfile</i>] [<code>-m</code> <i>addresses</i>] [<code>-x</code> <i>compress</i>] [<code>-X</code> <i>program</i>] [<code>-Y</code> <i>regex</i>] </p>
<h2>DESCRIPTION</h2>
<p> This series of shell scripts and associated control files may be used to create a customized regime of administration and management for the Performance Co-Pilot (see <code><a href="/docs/linux/man/1-pcpintro/">PCPintro</a></code>(1)) inference engine, <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1). </p>
<p> <code>pmie_daily</code> is intended to be run once per day, preferably in the early morning, as soon after midnight as practicable. Its task is to rotate the log files for the running <code>pmie</code> processes &#8211; these files may grow without bound if the &#8220;print&#8221; action is used, or any other <code>pmie</code> action writes to its stdout/stderr streams. After some period, old <code>pmie</code> log files are discarded. This period is 14 days by default, but may be changed using the <code>-k</code> option. Two special values are recognized for the period (<i>discard</i>), namely <code>0</code> to keep no log files beyond the current one, and <code>forever</code> to prevent any log files being discarded. </p>
<p> Log files can optionally be compressed after some period (<i>compress</i>), to conserve disk space. This is particularly useful for large numbers of <code>pmie</code> processes under the control of <code>pmie_check</code>. The <code>-x</code> option specifies the number of days after which to compress archive data files, and the <code>-X</code> option specifies the program to use for compression &#8211; by default this is <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1). Use of the <code>-Y</code> option allows a regular expression to be specified causing files in the set of files matched for compression to be omitted &#8211; this allows only the data file to be compressed, and also prevents the program from attempting to compress it more than once. The default <i>regex</i> is &quot;.(meta|index|Z|gz|bz2|zip|xz|lzma|lzo|lz4)$&quot; &#8211; such files are filtered using the <code>-v</code> option to <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1). </p>
<p> Use of the <code>-m</code> option causes <code>pmie_daily</code> to construct a summary of the log files generated for all monitored hosts in the last 24 hours (lines matching &#8220; OK &#8221; are culled), and e-mail that summary to the set of space-separated <i>addresses</i>. </p>
<p> <code>pmie_check</code> may be run at any time, and is intended to check that the desired set of <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) processes are running, and if not to re-launch any failed inference engines. Use of the <code>-s</code> option provides the reverse functionality, allowing the set of <code>pmie</code> processes to be cleanly shutdown. Use of the <code>-C</code> option queries the system service runlevel information for <code>pmie</code>, and uses that to determine whether to start processes. </p>
<p> Both <code>pmie_check</code> and <code>pmie_daily</code> are controlled by PCP inference engine control file(s) that specify the <code>pmie</code> instances to be managed. The default control file is <code>$PCP_PMIECONTROL_PATH</code> but an alternate may be specified using the <code>-c</code> option. If the directory <code>$PCP_PMLOGGERCONTROL_PATH</code>.d (or <i>control</i>.d from the <code>-c</code> option) exists, then the contents of any additional control files therein will be appended to the main control file (which must exist). </p>
<p> <code>Warning</code>: The <code>$PCP_PMIECONTROL_PATH</code> and <code>$PCP_PMIECONTROL_PATH</code>.d files must not be writable by any user other than root. </p>
<p> The control file(s) should be customized according to the following rules that define for the current version (1.1) of the control file format.</p>
<dl>
<dt>1.</p>
<dd> Lines beginning with a &#8220;#&#8221; are comments.</p>
<dt>2.</p>
<dd> Lines beginning with a &#8220;$&#8221; are assumed to be assignments to environment variables in the style of <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), and all text following the &#8220;$&#8221; will be <code>eval</code>&#8216;ed by the script reading the control file, and the corresponding variable exported into the environment. This is particularly useful to set and export variables into the environment of the administrative script, e.g. </p>
<pre>
$ PMCD_CONNECT_TIMEOUT=20
</pre>
<dt>3.</p>
<dd> There <code>must</code> be a version line in the initial control file of the form: </p>
<pre>
$ version=1.1
</pre>
<dt>4.</p>
<dd> There should be one line in the control file(s) for each <code>pmie</code> instance of the form: </p>
<pre>
<i>host</i> <code>y</code>|<code>n</code> <code>y</code>|<code>n</code> <i>logfile</i> <i>args</i>
</pre>
<dt>5.</p>
<dd> Fields within a line of the control file(s) are separated by one or more spaces or tabs.</p>
<dt>6.</p>
<dd> The <i>first</i> field is the name of the host that is the default source of the performance metrics for this <code>pmie</code> instance.</p>
<dt>7.</p>
<dd> The <i>second</i> field indicates if this is a <i>primary</i> <code>pmie</code> instance (<code>y</code>) or not (<code>n</code>). Since the primary inference engine must run on the local host, and there may be at most one primary for a particular host, this field can be <code>y</code> for at most one <code>pmie</code> instance, in which case the host name must be the name of the local host. When generating <code>pmie</code> configuration files, the primary clause indicates that <code>pmieconf (1)</code> should enable all rules in the primary group, in addition to all other default rules.</p>
<dt>8.</p>
<dd> The <i>third</i> field indicates whether this <code>pmie</code> instance needs to be started under the control of <code><a href="/docs/linux/man/1-pmsocks/">pmsocks</a></code>(1) to connect to a <code>pmcd</code> through a firewall (<code>y</code> or <code>n</code>).</p>
<dt>9.</p>
<dd> The <i>fourth</i> field is the name of the <code>pmie</code> activity log file. A useful convention is that <code>pmie</code> instances monitoring the local host with hostname <i>myhost</i> are maintained in the directory <code>$PCP_LOG_DIR/pmie/</code><i>myhost</i>, while activity logs for the remote host <i>mumble</i> are maintained in <code>$PCP_LOG_DIR/pmie/</code><i>mumble</i>. This is consistent with the way <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) maintains its activity logs and archive files.</p>
<dt>10.</p>
<dd> All other fields are interpreted as arguments to be passed to <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1). Most typically this would be the <code>-c</code> option.</dl>
<p> The following sample control lines specify one <code>pmie</code> instance monitoring the local host (<i>wobbly</i>), and another monitoring performance metrics from the host <i>splat</i>. </p>
<pre>
wobbly  n  PCP_LOG_DIR/pmie/wobbly  -c config.default
splat   n  PCP_LOG_DIR/pmie/splat   -c splat/cpu.conf
</pre>
<p> Typical <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5) entries for periodic execution of <code>pmie_daily</code> and <code>pmie_check</code> are given in <code>$PCP_SYSCONF_DIR/pmie/crontab</code> (unless installed by default in <i>/etc/cron.d</i> already) and shown below. </p>
<pre>
# daily processing of pmie logs
08      0       *       *       *       $PCP_BINADM_DIR/pmie_daily
# every 30 minutes, check pmie instances are running
28,58   *       *       *       *       $PCP_BINADM_DIR/pmie_check
</pre>
<p> In order to ensure that mail is not unintentionally sent when these scripts are run from <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) diagnostics are always sent to log files. By default, these files are <code>$PCP_LOG_DIR/pmie/pmie_daily.log</code> and <code>$PCP_LOG_DIR/pmie/pmie_check.log</code> but this can be changed using the <code>-l</code> option. If this log file already exists when the script starts, it will be renamed with a <i>.prev</i> suffix (overwriting any log file saved earlier) before diagnostics are generated to the new log file. </p>
<p> The output from the <code>cron</code> execution of the scripts may be extended using the <code>-V</code> option to the scripts which will enable verbose tracing of their activity. By default the scripts generate no output unless some error or warning condition is encountered. </p>
<p> The <code>-N</code> option enables a &#8220;show me&#8221; mode, where the actions are echoed, but not executed, in the style of &#8220;make -n&#8221;. Using <code>-N</code> in conjunction with <code>-V</code> maximizes the diagnostic capabilities for debugging.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMIECONTROL_PATH</code></p>
<dd> the default PCP inference engine control file<br />
 <code>Warning</code>: this file must not be writable by any user other than root.</p>
<dt><code>$PCP_PMIECONTROL_PATH</code>.d</p>
<dd> optional directory containing additional PCP inference engine control files, typically one per host<br />
 <code>Warning</code>: this files herein must not be writable by any user other than root.</p>
<dt><code>$PCP_SYSCONF_DIR/pmie/crontab</code></p>
<dd> sample crontab for automated script execution by $PCP_USER (or root) &#8211; exists only if the platform does not support the <i>/etc/cron.d</i> mechanism.</p>
<dt><code>$PCP_VAR_DIR/config/pmie/config.default</code></p>
<dd> default <code>pmlogger</code> configuration file location for a localhost inference engine, typically generated automatically by <code><a href="/docs/linux/man/1-pmieconf/">pmieconf</a></code>(1).</p>
<dt><code>$PCP_LOG_DIR/pmie/</code><i>hostname</i></p>
<dd> default location for the pmie log file for the host <i>hostname</i></p>
<dt><code>$PCP_LOG_DIR/pmie/</code><i>hostname</i><code>/lock</code></p>
<dd> transient lock file to guarantee mutual exclusion during <code>pmie</code> administration for the host <i>hostname</i> &#8211; if present, can be safely removed if neither <code>pmie_daily</code> nor <code>pmie_check</code> are running</p>
<dt><code>$PCP_LOG_DIR/NOTICES</code></p>
<dd> PCP &#8220;notices&#8221; file used by <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) and friends</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPintro</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmieconf/">pmieconf</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) and <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8). </p>
<h2>Index</h2>
