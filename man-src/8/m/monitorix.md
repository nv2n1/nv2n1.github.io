---
title: "monitorix(8)"
name: "monitorix"
section: "8"
letter: "m"
url: "/docs/linux/man/8-monitorix/"
description: "monitorix – a lightweight system monitoring tool"
---

<p>monitorix &#8211; a lightweight system monitoring tool</p>
<h2>Synopsis</h2>
<p><code>monitorix</code> <code>-c</code> configfile [<code>-p</code> pidfile] [<code>-d</code> none | graph[,graph] | all] [<code>-v</code>] [<code>-n</code>]</p>
<h2>Description</h2>
<p>This Perl daemon starts the main Monitorix process, which gathers statistics about the system it is running on and stores this information in a set of RRD files.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <i>configfile</i></p>
<dd>The default location of the main configuration file varies depending on the operating system:</dl>
<dl>
<dd>Linux: <i>/etc/monitorix/monitorix.conf</i><br />
 FreeBSD: <i>/usr/local/etc/monitorix.conf</i> </p>
<p> Extra configuration files can be placed in <i>/etc/monitorix/conf.d</i>, they will be loaded right after the main configuration file (overriding previous options).</dl>
<dl>
<dt><code>-p</code> <i>pidfile</i></p>
<dd>Stores the daemon&#8217;s process ID into the specified file.</p>
<dt><code>-d</code> none | graph[,graph] | all</p>
<dd>Logs more information about what <code>monitorix</code> is doing internally. The keys reflect if the data collected must be displayed on each case. If <code>all</code> is defined, the data collected of all enabled graphs will be shown. If <code>none</code> is defined no data collected will be shown. Finally it is also possible to define a comma-separated list of graph names from which show their data collected.<br />
 For a reference of all graph names check the option <code>graph_name</code> in the <i>monitorix.conf</i> configuration file.</p>
<dt><code>-v</code></p>
<dd>Displays version information.</p>
<dt><code>-n</code></p>
<dd>This argument will prevent Monitorix from daemonizing, and hence, forcing it to run in foreground. This is specially usefull for debugging purposes.</dl>
<h2>Signals</h2>
<p>On receipt of a SIGHUP, <code>monitorix</code> will close and reopen its log file. This is useful in scripts which rotate and age log files. </p>
<p> Note that the configuration file is not re-read.</p>
<h2>Files</h2>
<p>The following set of the files are created on every startup:</p>
<dl>
<dt><code>&lt;base_dir&gt;/cgi/monitorix.conf.path</code></p>
<dd>Stores the path of <i>configfile</i>.</p>
<dt><code>&lt;base_dir&gt;/cgi/monitorix.hplog</code></p>
<dd>Stores the output of <i>hplog</i> command.</p>
<dt><code>&lt;base_dir&gt;/index.html</code></p>
<dd>HTML main page.</dl>
<h2>Author</h2>
<p>Monitorix is written by Jordi Sanfeliu &lt;jordi [at] fibranet.cat&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2015 Jordi Sanfeliu<br />
 Licensed under the GNU General Public License version 2 (GPLv2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-monitorix-conf/">monitorix.conf</a></code>(5) </p>
