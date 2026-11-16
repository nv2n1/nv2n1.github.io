---
title: "broctl(8)"
name: "broctl"
section: "8"
letter: "b"
url: "/docs/linux/man/8-broctl/"
description: "broctl – interactive shell for managing Bro installations"
---

<p><code>broctl</code> &#8211; interactive shell for managing Bro installations</p>
<h2>Synopsis</h2>
<p><code>broctl</code> [<i>command</i>] </p>
<h2>Description</h2>
<p><code>broctl</code> is an interactive interface for managing either a standalone or a Bro cluster installation. If a <code>broctl</code> command is specified directly on the command-line, then <code>broctl</code> performs the action associated with that command immediately (instead of running the interactive interface). </p>
<p> Before actually running <code>broctl</code> you first need to edit the <code>broctl.cfg</code>, <code>node.cfg</code>, and <code>networks.cfg</code> files. In the <code>broctl.cfg</code> file, you should review the <code>broctl</code> options and make sure the options are set correctly for your environment. Next, edit the <code>node.cfg</code> file and specify the nodes that you will be running. Finally, edit the <code>networks.cfg</code> file and list each network that is considered local to the monitored environment (see the examples in the file for the format to use). </p>
<p> When running <code>broctl</code> for the first time, you must run the <code>broctl</code> <code>deploy</code> command before running any other commands in order to apply the configuration settings. You must also run <code>broctl deploy</code> each time you change the configuration (including any Bro scripts) or upgrade Bro.</p>
<h2>Options</h2>
<dl>
<dt><code>capstats</code> [&lt;nodes&gt;] [&lt;secs&gt;]</dt>
<dd>Report interface statistics with capstats</dd>
<dt><code>check</code> [&lt;nodes&gt;]</dt>
<dd>Check configuration before installing it</dd>
<dt><code>cleanup</code> [&#8211;all] [&lt;nodes&gt;]</dt>
<dd>Delete working dirs (flush state) on nodes</dd>
<dt><code>config</code></dt>
<dd>Print broctl configuration</dd>
<dt><code>cron</code> [&#8211;no-watch]</dt>
<dd>Perform jobs intended to run from cron</dd>
<dt><code>cron</code> enable|disable|?</dt>
<dd>Enable/disable &quot;cron&quot; jobs</dd>
<dt><code>deploy</code></dt>
<dd>Check, install, and restart</dd>
<dt><code>df</code> [&lt;nodes&gt;]</dt>
<dd>Print nodes&#8217; current disk usage</dd>
<dt><code>diag</code> [&lt;nodes&gt;]</dt>
<dd>Output diagnostics for nodes</dd>
<dt><code>exec</code> &lt;shell cmd&gt;</dt>
<dd>Execute shell command on all hosts</dd>
<dt><code>exit</code></dt>
<dd>Exit from the interactive interface</dd>
<dt><code>install</code></dt>
<dd>Update broctl installation/configuration</dd>
<dt><code>netstats</code> [&lt;nodes&gt;]</dt>
<dd>Print nodes&#8217; current packet counters</dd>
<dt><code>nodes</code></dt>
<dd>Print node configuration</dd>
<dt><code>peerstatus</code> [&lt;nodes&gt;]</dt>
<dd>Print status of nodes&#8217; remote connections</dd>
<dt><code>print</code> &lt;id&gt; [&lt;nodes&gt;]</dt>
<dd>Print values of script variable at nodes</dd>
<dt><code>process</code> &lt;trace&gt; [&lt;op&gt;] [&#8211; &lt;sc&gt;]</dt>
<dd>Run Bro (with options and scripts) on trace</dd>
<dt><code>restart</code> [&#8211;clean] [&lt;nodes&gt;]</dt>
<dd>Stop and then restart processing</dd>
<dt><code>scripts</code> [-c] [&lt;nodes&gt;]</dt>
<dd>List the Bro scripts the nodes will load</dd>
<dt><code>start</code> [&lt;nodes&gt;]</dt>
<dd>Start processing</dd>
<dt><code>status</code> [&lt;nodes&gt;]</dt>
<dd>Summarize node status</dd>
<dt><code>stop</code> [&lt;nodes&gt;]</dt>
<dd>Stop processing</dd>
<dt><code>top</code> [&lt;nodes&gt;]</dt>
<dd>Show Bro processes ala top</dd>
<dt><code>update</code> [&lt;nodes&gt;]</dt>
<dd>Update configuration of nodes on the fly</dd></dl>
<p> Commands provided by plugins:</p>
<dl>
<dt><code>ps.bro</code> [&lt;nodes&gt;]</dt>
<dd>Show Bro processes on nodes&#8217; systems</dd></dl>
<h2>Author</h2>
<p><code>broctl</code> was written by The Bro Project &lt;info [at] bro.org&gt;.</p>
