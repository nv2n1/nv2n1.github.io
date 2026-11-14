---
title: "logwatch(8)"
name: "logwatch"
section: "8"
letter: "l"
url: "/docs/linux/man/8-logwatch/"
description: "logwatch – system log analyzer and reporter"
---

<p>logwatch &#8211; system log analyzer and reporter</p>
<h2>Synopsis</h2>
<p><code>logwatch [&#8211;detail</code> <i>level</i> <code>] [&#8211;logfile</code> <i>log-file-group</i> <code>] [&#8211;service</code> <i>service-name</i> <code>] [&#8211;mailto</code> <i>address</i> <code>] [&#8211;archives] [&#8211;range</code> <i>range</i> <code>] [&#8211;debug</code> <i>level</i> <code>] [&#8211;filename</code> <i>file-name</i> <code>] [&#8211;logdir</code> <i>directory</i> <code>] [&#8211;hostlimit</code> <i>hosts</i> <code>] [&#8211;hostname</code> <i>hostname</i> <code>] [&#8211;html_wrap</code> <i>number of characters</i> <code>] [&#8211;hostformat </code> <i>host based options</i> <code>] [&#8211;output</code> <i>output-type</i> <code>] [&#8211;format</code> <i>report format</i> <code>] [&#8211;encode</code> <i>encoding to use</i> <code>] [&#8211;numeric] [&#8211;no-oldfiles-log] [&#8211;version] [&#8211;help|&#8211;usage]</code></p>
<h2>Description</h2>
<p><code>Logwatch</code> is a customizable, pluggable log-monitoring system. It will go through your logs for a given period of time and make a report in the areas that you wish with the detail that you wish. Logwatch is being used for Linux and many types of UNIX.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;detail</code> level</p>
<dd>This is the detail level of the report. <i>level</i> can be a positive integer, or high, med, low, which correspond to the integers 10, 5, and 0, respectively.</p>
<dt><code>&#8211;logfile</code> log-file-group</p>
<dd>This will force Logwatch to process only the set of logfiles defined by <i>log-file-group</i> (i.e. messages, xferlog, &#8230;). Logwatch will therefore process all services that use those logfiles. This option can be specified more than once to specify multiple logfile-groups.</p>
<dt><code>&#8211;service</code> service-name</p>
<dd>This will force Logwatch to process only the service specified in <i>service-name</i> (i.e. login, pam, identd, &#8230;). Logwatch will therefore also process any log-file-groups necessary to process these services. This option can be specified more than once to specify multiple services to process. A useful <i>service-name</i> is <i>All</i> which will process all services (and logfile-groups) for which you have filters installed.</p>
<dt><code>&#8211;mailto</code> address</p>
<dd>Mail the results to the email address or user specified in <i>address.</i></p>
<dt><code>&#8211;range</code> range</p>
<dd>You can specify a date-range to process. Common ranges are <i>Yesterday, Today, All,</i> and <i>Help.</i> Additional options are listed when invoked with the <i>Help</i> parameter.</p>
<dt><code>&#8211;archives</code></p>
<dd>Each log-file-group has basic logfiles (i.e. /var/log/messages) as well as archives (i.e. /var/log/messages.? or /var/log/messages.?.gz). When used with &quot;&#8211;range all&quot;, this option will make Logwatch search through the archives in addition to the regular logfiles. For other values of &#8211;range, Logwatch will search the appropriate archived logs.</p>
<dt><code>&#8211;debug</code> level</p>
<dd>For debugging purposes. <i>level</i> can range from 0 to 100. This will <i>really</i> clutter up your output. You probably don&#8217;t want to use this.</p>
<dt><code>&#8211;filename</code> file-name</p>
<dd>Save the output to <i>file-name</i> instead of displaying or mailing it.</p>
<dt><code>&#8211;logdir</code> directory</p>
<dd>Look in <i>directory</i> for log subdirectories or log files instead of the default directory.</p>
<dt><code>&#8211;hostlimit</code> host1,host2</p>
<dd>Limit report to hostname &#8211; host1, host2.</p>
<dt><code>&#8211;hostname</code> hostname</p>
<dd>Use <i>hostname</i> for the reports instead of this system&#8217;s hostname. In addition, if HostLimit is set in the logwatch.conf configuration file (see <code>MORE INFORMATION</code>, below), then only logs from this hostname will be processed (where appropriate).</p>
<dt><code>&#8211;html_wrap</code> num-characters</p>
<dd>Number of characters that html output should be wrapped to. Default is 80.</p>
<dt><code>&#8211;numeric</code></p>
<dd>Inhibits additional name lookups, displaying IP addresses numerically.</p>
<dt><code>&#8211;no-oldfiles-log</code></p>
<dd>Suppress the logwatch log, which informs about the old files in logwatch tmpdir.</p>
<dt><code>&#8211;usage</code></p>
<dd>Displays usage information</p>
<dt><code>&#8211;help</code></p>
<dd>same as &#8211;usage.</dl>
<h2>Files</h2>
<dl>
<dt>/usr/share/logwatch/</p>
<dd>
<dl>
<dd>This directory contains all the perl executables and configuration files shipped with the logwatch distribution.</dl>
<dt>/etc/logwatch</p>
<dd>
<dl>
<dd>This directory contains local configuration files that override the default configuration. See <code>MORE INFORMATION</code> below for more information.</dl>
</dl>
<h2>Examples</h2>
<p><code>logwatch &#8211;service ftpd-xferlog &#8211;range all &#8211;detail high &#8211;archives</code></p>
<dl>
<dd>This will print out all FTP transfers that are stored in all current and archived xferlogs.</dl>
<p> <code>logwatch &#8211;service pam_pwdb &#8211;range yesterday &#8211;detail high </code></p>
<dl>
<dd>This will print out login information for the previous day&#8230;</dl>
<h2>More Information</h2>
<p>The directory /usr/share/doc/logwatch-* contains several files with additional documentation: <i>HOWTO-Customize-LogWatch</i></p>
<dl>
<dd>Documents the directory structure of Logwatch configuration and executable files, and describes how to customize Logwatch by overriding these default files.</dl>
<p> <i>LICENSE</i></p>
<dl>
<dd>Describes the License under which Logwatch is distributed. Additional clauses may be specified in individual files.</dl>
<p> <i>README</i></p>
<dl>
<dd>Describes how to install, where to find it, mailing lists, and other useful information.</dl>
<h2>Author</h2>
<p>Kirk Bauer &lt;kirk [at] kaybee.org&gt; <a rel="nofollow" href="http://www.kaybee.org/~kirk">http://www.kaybee.org/~kirk</a> <a href="ftp://ftp.kaybee.org/pub/redhat/RPMS">ftp://ftp.kaybee.org/pub/redhat/RPMS</a></p>
