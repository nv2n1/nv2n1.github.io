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
<dt><code>capstats</code> [&lt;nodes&gt;] [&lt;secs&gt;]</p>
<dd>Report interface statistics with capstats</p>
<dt><code>check</code> [&lt;nodes&gt;]</p>
<dd>Check configuration before installing it</p>
<dt><code>cleanup</code> [&#8211;all] [&lt;nodes&gt;]</p>
<dd>Delete working dirs (flush state) on nodes</p>
<dt><code>config</code></p>
<dd>Print broctl configuration</p>
<dt><code>cron</code> [&#8211;no-watch]</p>
<dd>Perform jobs intended to run from cron</p>
<dt><code>cron</code> enable|disable|?</p>
<dd>Enable/disable &quot;cron&quot; jobs</p>
<dt><code>deploy</code></p>
<dd>Check, install, and restart</p>
<dt><code>df</code> [&lt;nodes&gt;]</p>
<dd>Print nodes&#8217; current disk usage</p>
<dt><code>diag</code> [&lt;nodes&gt;]</p>
<dd>Output diagnostics for nodes</p>
<dt><code>exec</code> &lt;shell cmd&gt;</p>
<dd>Execute shell command on all hosts</p>
<dt><code>exit</code></p>
<dd>Exit from the interactive interface</p>
<dt><code>install</code></p>
<dd>Update broctl installation/configuration</p>
<dt><code>netstats</code> [&lt;nodes&gt;]</p>
<dd>Print nodes&#8217; current packet counters</p>
<dt><code>nodes</code></p>
<dd>Print node configuration</p>
<dt><code>peerstatus</code> [&lt;nodes&gt;]</p>
<dd>Print status of nodes&#8217; remote connections</p>
<dt><code>print</code> &lt;id&gt; [&lt;nodes&gt;]</p>
<dd>Print values of script variable at nodes</p>
<dt><code>process</code> &lt;trace&gt; [&lt;op&gt;] [&#8211; &lt;sc&gt;]</p>
<dd>Run Bro (with options and scripts) on trace</p>
<dt><code>restart</code> [&#8211;clean] [&lt;nodes&gt;]</p>
<dd>Stop and then restart processing</p>
<dt><code>scripts</code> [-c] [&lt;nodes&gt;]</p>
<dd>List the Bro scripts the nodes will load</p>
<dt><code>start</code> [&lt;nodes&gt;]</p>
<dd>Start processing</p>
<dt><code>status</code> [&lt;nodes&gt;]</p>
<dd>Summarize node status</p>
<dt><code>stop</code> [&lt;nodes&gt;]</p>
<dd>Stop processing</p>
<dt><code>top</code> [&lt;nodes&gt;]</p>
<dd>Show Bro processes ala top</p>
<dt><code>update</code> [&lt;nodes&gt;]</p>
<dd>Update configuration of nodes on the fly</dl>
<p> Commands provided by plugins:</p>
<dl>
<dt><code>ps.bro</code> [&lt;nodes&gt;]</p>
<dd>Show Bro processes on nodes&#8217; systems</dl>
<h2>Author</h2>
<p><code>broctl</code> was written by The Bro Project &lt;info [at] bro.org&gt;.</p>
