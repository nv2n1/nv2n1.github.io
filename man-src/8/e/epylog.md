---
title: "epylog(8)"
name: "epylog"
section: "8"
letter: "e"
url: "/docs/linux/man/8-epylog/"
description: "epylog – Syslog new log notifier and parser."
---

<p><code>epylog</code> &#8211; Syslog new log notifier and parser.</p>
<h2>Synopsis</h2>
<p><code>epylog</code> [-c epylog.conf] [-d LOGLEVEL] [&#8211;last PERIOD]<br />
&nbsp;<wbr>[&#8211;store-offsets]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;cron] </p>
<h2>Description</h2>
<p>Epylog is a new log notifier and parser which runs periodically out of cron, looks at your logs, processes the entries in order to present them in a more comprehensive format, and then provides you with the output. It is written specifically with large network clusters in mind where a lot of machines (around 50 and upwards) log to the same loghost using syslog or syslog-ng. Alternatively, Epylog can be invoked from the command line and provide a log report based on a certain provided time period. In this case it relies on syslog timestamps to find the offsets, as opposed to the end-of-log offsets stored during the last run, though this behavior is not as reliable and is easily thwarted by skewed clocks. </p>
<h2>Options</h2>
<dl>
<dt><code>-c config.file</code></p>
<dd>Provide an alternative config file to Epylog. By default, it will look in /etc/epylog/epylog.conf.</p>
<dt><code>-d LOGLEVEL</code></p>
<dd>Logging level. The default is 1. 0 will produce no output except for critical errors (useful for cron runs). 2 and above are debugging levels. 5 is the most verbose.</p>
<dt><code>&#8211;last PERIOD</code></p>
<dd>Will make a report on events that occurred in the last PERIOD. PERIOD can be either &quot;hour&quot;, &quot;day&quot;, &quot;week&quot;, &quot;month&quot;, or more granular: &quot;1h&quot;, &quot;2h&quot;, &quot;3d&quot;, &quot;2w&quot;, etc. When &#8211;last is specified, epylog will ignore the saved offsets and locate the entries by timestamps. <i>CAUTION</i>: this process is not to be trusted, since the timestamps are not checked for any validity when arriving to the loghost. One reporting machine with a skewed clock may confuse Epylog enough to miss a lot of valid entries.</p>
<dt><code>&#8211;store-offsets</code></p>
<dd>When specified, will store the offset of the last log entry processed in offsets.xml. During the cron runs epylog relies on the offset information to find out what new entries to process. This is more trustworthy than relying on timestamps. The default behavior is not to store the offsets, as this allows to run epylog both from cron and manually without the two interfering with each-other. The location of offset.xml is specified in epylog.conf. See <code><a href="/docs/linux/man/5-epylog-conf/">epylog.conf</a>(5)</code> for more details.</p>
<dt><code>&#8211;quiet</code></p>
<dd>In every way identical to -d 0.</p>
<dt><code>&#8211;cron</code></p>
<dd>This is essentially &#8211;quiet &#8211;store-offsets, plus a lockfile will be created and consulted, preventing more than one instance of epylog from running. You can still run epylog manually &#8212; the lockfile is only checked when running in &#8211;cron mode. </p>
</dl>
<h2>Features</h2>
<dl>
<dd>The core of epylog is written in python. It handles things like timestamp lookups, unwrapping of &quot;last message repeated&quot; lines, handling of rotated files, preparing and publishing the reports, etc. </p>
<p> The modules are pluggable and can be either &quot;internal&quot;, written in python, or external. External modules can be written in any language, but at a price of some convenience. For more info see <code><a href="/docs/linux/man/5-epylog-modules/">epylog-modules</a>(5)</code>. </p>
</dl>
<h2>Initial Run</h2>
<dl>
<dd>Depending on the size of your logs, you might want to initialize your offsets before letting epylog run from cron. When the offsets.xml file is missing, epylog will by default process the entire log, and depending on your configuration, that can be a lot of entries. A good way to init epylog is to run: </p>
<p> <code>epylog &#8211;last day &#8211;store-offsets</code> </p>
</dl>
<h2>Files</h2>
<p><i>/etc/epylog/epylog.conf</i><br />
 <i>/usr/sbin/epylog</i><br />
 <i>/etc/cron.daily/epylog.cron</i><br />
 <i>/etc/epylog/*</i><br />
 <i>/var/lib/epylog/*</i><br />
 <i>/usr/share/epylog/modules/*</i></p>
<h2>Examples</h2>
<p>The useful way to run from a command line is with &#8211;last. E.g.: <code>epylog &#8211;last day</code><br />
 <code>epylog &#8211;last 2w</code> When running from cron, you want to store the offsets and not rely on timestamps. There is a mode that allows you to do this: <code>epylog &#8211;cron</code> </p>
<h2>Authors</h2>
<p>Konstantin Ryabitsev &lt;icon [at] linux.duke.edu&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-epylog-conf/">epylog.conf</a>(5) <a href="/docs/linux/man/5-epylog-modules/">epylog-modules</a>(5) </p>
