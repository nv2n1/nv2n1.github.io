---
title: "rancid-run(1)"
name: "rancid-run"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rancid-run/"
description: "rancid-run – run rancid for each of the groups"
---

<h2>NAME</h2>
<p> rancid-run &#8211; run rancid for each of the groups</p>
<h2>SYNOPSIS</h2>
<p> <code>rancid-run</code> [<code>-V</code>] [<code>-f&nbsp;<wbr></code>rancid.conf]&nbsp;<wbr>[<code>-f&nbsp;<wbr></code>rancid.conf]&nbsp;<wbr>[<code>-m&nbsp;<wbr></code>mail_rcpt]&nbsp;<wbr>[<code>-r&nbsp;<wbr></code>device_name]&nbsp;<wbr>[group [group &#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>rancid-run</code> is a <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) script to run <i><a href="/docs/linux/man/1-rancid/">rancid</a></i>(1) for a set of rancid group(s). </p>
<p> <code>rancid-run</code> reads <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5) to configure itself, then uses <i><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></i>(1) to run <i><a href="/docs/linux/man/1-rancid/">rancid</a></i>(1) for each rancid group. The set of rancid groups can either be provided as command-line arguments or via the <i>LIST_OF_GROUPS</i> variable in <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), if the group argument is omitted. </p>
<p> A lock file is maintained per-group to prevent simultaneous runs for a given group by <i><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></i>(1). The lock file will be named <i>.&lt;group&gt;.run.lock</i> and will be located in <i>$TMPDIR</i> (see below). </p>
<p> A log file is produced under <i>$LOGDIR/logs</i> for each rancid group processed. The file name will be &lt;group&gt;.YYYYMMDD.HHMMSS (year month day . hour minute second). </p>
<p> <code>rancid-run</code> is normally used to run rancid from <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8). For example: </p>
<pre>
0 * * * *      /usr/local/rancid/bin/rancid-run
</pre>
<p> The command-line options are as follows:</p>
<dl>
<dt><code>-V</code></p>
<dd> Prints package name and version strings.</p>
<dt><code>-f rancid.conf</code></p>
<dd> Specify an alternate configuration file.</p>
<dt><code>-m mail_rcpt</code></p>
<dd> Specify the recipient of diff mail, which is normally rancid-&lt;group&gt;. The argument may be a single address, multiple comma separated addresses, or <code>-m</code> may be specified multiple times.</p>
<dt><code>-r device_name</code></p>
<dd> Run rancid for a single device, <i>device_name</i>. <i>device_name</i> should be name, as it appears in a group&#8217;s router.db. The device must be marked &quot;up&quot;. If a group is not specified on the command-line, rancid will be run against any group in which the device_name appears. </p>
<p> The <code>-r</code> option alters the subject line of the diff mail. It will begin with &lt;group name&gt;/&lt;device name&gt; rather than just the group name alone.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>rancid-run</code> utilizes the following environment variables from <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5).</p>
<dl>
<dt><code>BASEDIR</code></p>
<dd> Location of group directories, etc. This is set to the &quot;localstatedir&quot; by the configure script at installation time.</p>
<dt><code>LIST_OF_GROUPS</code></p>
<dd> List of rancid groups to collect.</p>
<dt><code>PATH</code></p>
<dd> Search path for utilities.</p>
<dt><code>TMPDIR</code></p>
<dd> Directory to hold temporary and lock files.</dl>
<h2>ERRORS</h2>
<p> If rancid fails to run or collect a device&#8217;s configuration, the particular group&#8217;s log file (mentioned above) should be consulted. Any errors produced by the revision control system (CVS, Subversion, or git) or any of the rancid scripts should be included there, whether they be a botched cvs tree, login authentication failure, rancid configuration error, etc. If the log file produces no clues, the next debugging step should be run the commands manually. For example, can the user who runs rancid login to the device with &#8216;clogin hostname&#8217;, and so on.</p>
<h2>FILES</h2>
<dl>
<dt><code>$BASEDIR/etc/rancid.conf</code></p>
<dd> <code>rancid-run</code> configuration file. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></code>(1), <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5)</p>
<h2>CAVEATS</h2>
<p> DO NOT leave temporary files in the &lt;group name&gt;/configs directory, they WILL be removed by <code><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></code>(1). </p>
<h2>Index</h2>
