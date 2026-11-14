---
title: "control_rancid(1)"
name: "control_rancid"
section: "1"
letter: "c"
url: "/docs/linux/man/1-control_rancid/"
description: "control_rancid – run rancid for devices of a group"
---

<h2>NAME</h2>
<p> control_rancid &#8211; run rancid for devices of a group</p>
<h2>SYNOPSIS</h2>
<p> <code>control_rancid</code> [<code>-V</code>] [<code>-f&nbsp;<wbr></code>config_file]&nbsp;<wbr>[<code>-m&nbsp;<wbr></code>mail_rcpt]&nbsp;<wbr>[<code>-r&nbsp;<wbr></code>device_name]&nbsp;<wbr>group</p>
<h2>DESCRIPTION</h2>
<p> <code>control_rancid</code> is a <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) script to parse a group&#8217;s <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5), run rancid for each of the devices, possibly re-run rancid for devices that failed collection, e-mail diffs, and e-mail error reports. </p>
<p> <code>control_rancid</code> also creates and/or re-creates the .cvsignore/.gitignore files for each group. For the configs sub-directory, it includes &quot;.old&quot;, where a user may keep files they would like to be ignored. </p>
<p> The command-line options are as follows:</p>
<dl>
<dt><code>-V</code></p>
<dd> Prints package name and version strings.</p>
<dt><code>-f group_config_file</code></p>
<dd> Specify an alternative rancid.conf. The global rancid.conf file is read by <code>rancid-run,</code> which calls <code>control_rancid</code> for each group, and <code>control_rancid</code> reads the group-specific rancid.conf, thereby overriding the global file. </p>
<p> The group-specific rancid.conf may not exist. </p>
<p> Default: &lt;BASEDIR&gt;/&lt;group&gt;/rancid.conf</p>
<dt><code>-m mail_rcpt</code></p>
<dd> Specify the recipient of diff mail, which is normally rancid-&lt;group&gt;. The argument may be a single address, multiple comma separated addresses, or <code>-m</code> may be specified multiple times.</p>
<dt><code>-r device_name</code></p>
<dd> Specify the name, as it appears in the router.db, of a particular device to collect and generate diffs for. The device must be marked &quot;up&quot;. </p>
<p> The <code>-r</code> option alters the subject line of the diff mail. It will begin with &lt;group name&gt;/&lt;device name&gt; rather than just the group name alone.</dl>
<p> <code>control_rancid</code> is normally (and best) run via <code><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></code>(1) which provides a locking mechanism on a group basis and saves output in a log file for each group.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></code>(1), <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5) </p>
<h2>Index</h2>
