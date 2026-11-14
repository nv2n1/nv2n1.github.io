---
title: "logcheck(8)"
name: "logcheck"
section: "8"
letter: "l"
url: "/docs/linux/man/8-logcheck/"
description: "logcheck – program to scan system logs for interesting lines"
---

<p>logcheck &#8211; program to scan system logs for interesting lines</p>
<h2>Synopsis</h2>
<p><code>logcheck</code> [ <code>OPTIONS</code> ]</p>
<h2>Description</h2>
<p>The <code>logcheck</code> program helps spot problems and security violations in your logfiles automatically and will send the results to you periodically in an e-mail. By default logcheck runs as an hourly cronjob just off the hour and after every reboot. </p>
<p> <code>logcheck</code> supports three level of filtering: &quot;paranoid&quot; is for high-security machines running as few services as possible. Don&#8217;t use it if you can&#8217;t handle its verbose messages. &quot;server&quot; is the default and contains rules for many different daemons. &quot;workstation&quot; is for sheltered machines and filters most of the messages. The ignore rules work in additive manner. &quot;paranoid&quot; rules are also included at level &quot;server&quot;. &quot;workstation&quot; level includes both &quot;paranoid&quot; and &quot;server&quot; rules. </p>
<p> The messages reported are sorted into three layers, system events, security events and attack alerts. The verbosity of system events is controlled by which level you choose, paranoid, server or workstation. However, security events and attack alerts are not affected by this.</p>
<h2>Examples</h2>
<p><code>logcheck</code> can be invoked directly thanks to <a href="/docs/linux/man/8-su/">su</a>(8) or <a href="/docs/linux/man/8-sudo/">sudo</a>(8), which change the user ID. The following example checks the logfiles without updating the offset and outputs everything to STDOUT. </p>
<p> sudo -u logcheck <code>logcheck</code> -o -t</p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-c CFG</code></p>
<dd>Overrule default configuration file.</p>
<dt><code>-d</code></p>
<dd>Debug mode.</p>
<dt><code>-h</code></p>
<dd>Show usage information.</p>
<dt><code>-H</code></p>
<dd>Use this hostname string in the subject of logcheck mail.</p>
<dt><code>-l LOG</code></p>
<dd>Run logfile through logcheck.</p>
<dt><code>-L CFG</code></p>
<dd>Overrule default logfiles list.</p>
<dt><code>-m</code></p>
<dd>Mail report to recipient.</p>
<dt><code>-o</code></p>
<dd>STDOUT mode, not sending mail.</p>
<dt><code>-p</code></p>
<dd>Set the report level to &quot;paranoid&quot;.</p>
<dt><code>-r DIR</code></p>
<dd>Overrule default rules directory.</p>
<dt><code>-R</code></p>
<dd>Adds &quot;Reboot:&quot; to the email subject line.</p>
<dt><code>-s</code></p>
<dd>Set the report level to &quot;server&quot;.</p>
<dt><code>-S DIR</code></p>
<dd>Overrule default state directory.</p>
<dt><code>-t</code></p>
<dd>Testing mode does not update offset.</p>
<dt><code>-T</code></p>
<dd>Do not remove the TMPDIR.</p>
<dt><code>-u</code></p>
<dd>Enable syslog-summary.</p>
<dt><code>-v</code></p>
<dd>Print current version.</p>
<dt><code>-w</code></p>
<dd>Set the report level to &quot;workstation&quot;.</dl>
<h2>Files</h2>
<p>/etc/logcheck/logcheck.conf is the main configuration file. </p>
<p> /etc/logcheck/logcheck.logfiles is the list of files to monitor. </p>
<p> /usr/share/doc/logcheck-database/README.logcheck-database.gz for hints on how to write, test and maintain rules.</p>
<h2>Exit Status</h2>
<p>0 upon success; 1 upon failure</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-logtail/">logtail</a></code>(8)</p>
<h2>Author</h2>
<p>logcheck is developed by Debian logcheck Team at alioth: <a rel="nofollow" href="http://alioth.debian.org/projects/logcheck/.">http://alioth.debian.org/projects/logcheck/.</a> </p>
<p> This manual page was written by Jon Middleton.</p>
