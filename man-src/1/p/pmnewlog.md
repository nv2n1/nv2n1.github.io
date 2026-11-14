---
title: "pmnewlog(1)"
name: "pmnewlog"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmnewlog/"
description: "pmnewlog – stop and restart archive logging for PCP performance metrics"
---

<h2>NAME</h2>
<p> <code>pmnewlog</code> &#8211; stop and restart archive logging for PCP performance metrics</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmnewlog</code> [<code>-a</code> <i>accessfile</i>] [<code>-C</code> <i>saveconfig</i>] [<code>-c</code> <i>configfile</i>] [<code>-N</code>] [<code>-n</code> <i>pmnsfile</i>] [<code>-P</code>] [<code>-p</code> <i>pid</i>] [<code>-s</code>] [<code>-V</code>] [<i>other pmlogger options</i>] <i>archive</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmnewlog</code> may be used to stop and restart a running instance of <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). This is most useful for managing multiple sets of Performance Co-Pilot (PCP) archive logs. These archive logs record the history of performance metric values that may be &#8220;played back&#8221; by other PCP tools, and they form the basis of the VCR paradigm and retrospective performance analysis services common to the PCP toolkit. </p>
<p> In normal usage, <code>pmnewlog</code> would be executed by <code><a href="/docs/linux/man/1-cron/">cron</a></code>(1) in the wee hours to terminate one PCP archive log and start another, i.e. to perform log rotation. </p>
<p> Even more common, would be the execution of <code>pmnewlog</code> from the PCP archive management script <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1). In this case, direct end-user execution of <code>pmnewlog</code> is most unlikely. </p>
<p> The mandatory argument <i>archive</i> is the base name for the physical files that will constitute the new archive log. </p>
<p> The <code>pmlogger</code> instance to be stopped and restarted must be running on the same system as <code>pmnewlog</code> and is either the primary logger (the default) or the logger with <i>pid</i> as specified by the <code>-p</code> option. </p>
<p> If the <code>-n</code> option is specified, then <code>pmnewlog</code> will use the namespace in the <i>pmnsfile</i>, rather than the default Performance Metrics Name Space (PMNS). </p>
<p> If no <code>-c</code> option is specified, <code>pmnewlog</code> will use <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) to connect to the running <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) and so determine all those metrics and instances that are subject to <code>mandatory</code> logging or <code>advisory on</code> logging, and the associated logging frequencies. This information is used to synthesize a new <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) configuration file. If the <code>-n</code> option is specified, it will also be used for these interactions with <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1). </p>
<p> If the <code>-c</code> option is specified, <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) will be restarted with <i>configfile</i> as the configuration file. Normally <i>configfile</i> would be the same configuration file used to start <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) in the first place, however note that since <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is restarted, any changes to the logging status made using <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) will be lost, unless these have also been reflected in changes to <i>configfile</i>. </p>
<p> If <i>configfile</i> does not exist, then a search is made in the directory <i>$PCP_VAR_DIR/config/pmlogger</i> for a file of the same name, and if found that file is used, e.g. if <i>config.mumble</i> does not exist in the current directory and the file <i>$PCP_VAR_DIR/config/pmlogger/config.mumble</i> does exist, then <code>-c config.mumble</code> and <code>-c $PCP_VAR_DIR/config/pmlogger/config.mumble</code> are equivalent. </p>
<p> Access controls specifications for the new <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) instance may optionally be provided via the <code>-a</code> option. The contents of <i>accessfile</i> should start with the literal token <code>[access]</code> and conform to the syntax of the access controls section as described for <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> The <code>-C</code> option may be used to save the configuration file that <code>pmnewlog</code> passes to the newly launched <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> If the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) instance needs to be started under the control of <code><a href="/docs/linux/man/1-pmsocks/">pmsocks</a></code>(1) to connect to a <code>pmcd</code> through a firewall, the <code>-s</code> option may be used. </p>
<p> The <code>-V</code> option enables verbose reporting of the activity. By default no output is generated unless some error or warning condition is encountered. </p>
<p> The <code>-N</code> option enables a &#8220;show me&#8221; mode, where the actions are echoed, but not executed, in the style of &#8220;make -n&#8221;. Using <code>-N</code> in conjunction with <code>-V</code> maximizes the diagnostic capabilities for debugging. </p>
<p> The <i>other pmlogger options</i> are as described for <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). Note that <code>pmnewlog</code> does <code>not</code> support the following options of <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1).</p>
<dl>
<dt><code>-h</code> <i>host</i></p>
<dd> <code>pmnewlog</code> determines the host to which the new <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) should connect based upon the current host connection for the old <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1).</p>
<dt><code>-s</code> <i>samples</i></p>
<dd> The new <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is expected to be long running, and the <code>-s</code> option of <code>pmnewlog</code> takes precedence.</p>
<dt><code>-T</code> <i>runtime</i></p>
<dd> The new <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is expected to be long running</p>
<dt><code>-V</code> <i>version</i></p>
<dd> The new <code>pmlogger</code> will always create the latest version PCP archive format, and the <code>-V</code> option of <code>pmnewlog</code> takes precedence.</p>
<dt><code>-x</code> <i>fd</i></p>
<dd> The launched <code>pmlogger</code> cannot be controlled by <code><a href="/docs/linux/man/3-pmrecordcontrol/">pmRecordControl</a></code>(3).</dl>
<h2>EXAMPLE</h2>
<p> The following <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) script could be executed by root via <code><a href="/docs/linux/man/1-cron/">cron</a></code>(1) to start a new set of archive logs for the primary logger each evening. A more complete version of this script may be found in <i>$PCP_BINADM_DIR/pmlogger_daily</i>, and is documented in the manual page for <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1). </p>
<pre><code>
#!/ bin / sh
#start new logs for PCP primary logger on this host
#standard place for logs
LOGDIR = $PCP_LOG_DIR / pmlogger /`hostname`
#each new log is named yymmdd.hh.mm
         LOGNAME =`date "+%Y%m%d.%H.%M"`
#do it
                      [!-d $LOGDIR] &amp;&amp;
                  mkdir - p $LOGDIR cd $LOGDIR $PCP_BINADM_DIR / pmnewlog - l $LOGDIR / pmlogger.log $LOGDIR
</code></pre>
<h2>FILES</h2>
<dl>
<dt><i>archive</i><code>.meta</p>
<dd> metadata (metric descriptions, instance domains, etc.) for the archive log</p>
<dt></code><i>archive</i><code>.0</p>
<dd> initial volume of metrics values (subsequent volumes have suffixes 1</code>, <code>2</code>, &#8230;)</p>
<dt><i>archive</i><code>.index</p>
<dd> temporal index to support rapid random access to the other files in the archive log</p>
<dt>$PCP_BINADM_DIR/pmlogger_daily</code></p>
<dd> sample script to rotate archives for a number of loggers</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1), <code><a href="/docs/linux/man/1-pmsocks/">pmsocks</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> Due to the precious nature of the archive logs, <code>pmnewlog</code> is rather paranoid in its checking and validation, and will try very hard to ensure that an appropriately configured <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) can be restarted, before terminating the existing <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> As a consequence of this checking, <code>pmnewlog</code> tends to generate rather verbose error and warning messages.</p>
<h2>CAVEATS</h2>
<p> If no <i>configfile</i> is specified, the method for synthesizing a configuration file using a <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) connection to the existing <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is, of necessity, incomplete. In particular, for metrics with dynamic underlying instance domains, it is not possible to identify a configuration that logs <code>all</code> instances of a metric all of the time, so rather the synthesized configuration file requests the continued logging of the set of instances that exist at the time <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is interrogated by <code>pmnewlog</code>. </p>
<p> If this situation is a concern, a fixed configuration file should be used, and passed to <code>pmnewlog</code> via the <code>-c</code> option. </p>
<h2>Index</h2>
