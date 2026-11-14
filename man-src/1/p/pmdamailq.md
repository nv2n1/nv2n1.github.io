---
title: "pmdamailq(1)"
name: "pmdamailq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdamailq/"
description: "pmdamailq – mail queue performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdamailq</code> &#8211; mail queue performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/mailq/pmdamailq</code> [<code>-b</code> <i>binlist</i>] [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-r</code> <i>regex</i>] [<code>-U</code> <i>username</i>] [<i>queuedir</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdamailq</code> is a Performance Metrics Domain Agent (PMDA) which extracts performance metrics describing the state of the e-mail queues managed by <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) and other mail transfer agents. </p>
<p> The <code>mailq</code> PMDA exports metrics that measure the total number of entries in the mail queue, and the subtotals for entries that have been queued for various time periods. </p>
<p> A brief description of the <code>pmdamailq</code> command line options follows:</p>
<dl>
<dt><code>-b</code></p>
<dd> The <i>binlist</i> argument specifies a list of delay thresholds used to &#8220;bin&#8221; the entries in the queue into a a histogram based on how long the entry has been in the mail queue. The default thresholds are: 1 hour, 4 hours, 8 hours, 1 day, 3 days and 7 days. The entries in <i>binlist</i> are comma separated time intervals, using the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for an update or reporting interval, e.g. the default list could be specified using the value <code>1hr,4hrs,8hrs,1day,3days,7days</code>.</p>
<dl>
<dt>
<dd>
<p> Values in <i>binlist</i> are assumed to be in ascending order, and mail items in the queue less than the first threshold are binned into a special bin labeled &#8220;recent&#8221;.</dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>mailq.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdamailq</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd .</code> If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-r</code></p>
<dd> Use an extended regular expression to match file names in the mail queue directory, rather than assuming all &quot;df&quot; prefixed files in the directory are mail files (the &quot;df&quot; prefix is the <code>sendmail</code> convention, but this convention is not followed by other mail daemons). The <i>regex</i> pattern specified should conform to the POSIX format described in <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3), and it describes file names that should be considered mail.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<p> The optional <i>queuedir</i> argument defines the directory in which <code>pmdamailq</code> expects to find the mail queue. The default is <code>/var/spool/mqueue</code>.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the mailq performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/mailq
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/mailq
# ./Remove
</pre>
<p> <code>pmdamailq</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdamailq</code></p>
<dt><code>$PCP_PMDAS_DIR/mailq/help</code></p>
<dd> default help text file for the mailq metrics</p>
<dt><code>$PCP_PMDAS_DIR/mailq/Install</code></p>
<dd> installation script for the <code>pmdamailq</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/mailq/Remove</code></p>
<dd> undo installation script for the <code>pmdamailq</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/mailq.log</code></p>
<dd> default log file for error messages and other information from <code>pmdamailq</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
