---
title: "clush(1)"
name: "clush"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clush/"
description: "clush – execute shell commands on a cluster"
---

<h2>NAME</h2>
<p> clush &#8211; execute shell commands on a cluster</p>
<h2>SYNOPSIS</h2>
<p> <code>clush</code> <code>-a</code> | <code>-g</code> <i>group</i> | <code>-w</code> <i>nodes</i> [OPTIONS] </p>
<p> <code>clush</code> <code>-a</code> | <code>-g</code> <i>group</i> | <code>-w</code> <i>nodes</i> [OPTIONS] <i>command</i> </p>
<p> <code>clush</code> <code>-a</code> | <code>-g</code> <i>group</i> | <code>-w</code> <i>nodes</i> [OPTIONS] &#8211;copy <i>file</i> | <i>dir</i> [ <i>file</i> | <i>dir</i> &#8230;] [ &#8211;dest <i>path</i> ] </p>
<p> <code>clush</code> <code>-a</code> | <code>-g</code> <i>group</i> | <code>-w</code> <i>nodes</i> [OPTIONS] &#8211;rcopy <i>file</i> | <i>dir</i> [ <i>file</i> | <i>dir</i> &#8230;] [ &#8211;dest <i>path</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>clush</code> is a program for executing commands in parallel on a cluster and for gathering their results. <code>clush</code> executes commands interactively or can be used within shell scripts and other applications. It is a partial front-end to the ClusterShell library that ensures a light, unified and robust parallel command execution framework. Thus, it allows traditional shell scripts to benefit from some of the library features. <code>clush</code> currently makes use of the Ssh worker of ClusterShell, by default, that only requires <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) (OpenSSH SSH client).</p>
<h2>INVOCATION</h2>
<p> <code>clush</code> can be started non-interactively to run a shell <i>command</i>, or can be invoked as an interactive shell. To start a <code>clush</code> interactive session, invoke the <code>clush</code> command without providing <i>command</i>.</p>
<dl>
<dt><code>Non-interactive mode</code></dt>
<dd> When <code>clush</code> is started non-interactively, the <i>command</i> is executed on the specified remote hosts in parallel. If option <code>-b</code> or <code>&#8211;dshbak</code> is specified, <code>clush</code> waits for command completion and then displays gathered output results. </dd>
<p> The <code>-w</code> option allows you to specify remote hosts by using ClusterShell NodeSet syntax, including the node groups <code>@group</code> special syntax and the <code>Extended Patterns</code> syntax to benefits from NodeSet basic arithmetics (like <code>@Agroup\&amp;@Bgroup</code>). See EXTENDED PATTERNS in <code><a href="/docs/linux/man/1-nodeset/">nodeset</a></code>(1) and also <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) for more information. </p>
<p> Unless option <code>&#8211;nostdin</code> is specified, <code>clush</code> detects when its standard input is connected to a terminal (as determined by <code>isatty</code>(3)). If actually connected to a terminal, <code>clush</code> listens to standard input when commands are running, waiting for an <i>Enter</i> key press. Doing so will display the status of current nodes. If standard input is not connected to a terminal, and unless option <code>&#8211;nostdin</code> is specified, <code>clush</code> binds the standard input of the remote commands to its own standard input, allowing scripting methods like: </p>
<pre><code>
#echo foo | clush - w node[40 - 42] - b cat
-- -- -- -- -- -- -- -node[40 - 42]-- -- -- -- -- -- -- -foo
</code></pre>
<p> Please see some other great examples in the EXAMPLES section below.</p>
<dt><code>Interactive session</code></dt>
<dd> If a <i>command</i> is not specified, and its standard input is connected to a terminal, <code>clush</code> runs interactively. In this mode, <code>clush</code> uses the GNU <code>readline</code> library to read command lines. Readline provides commands for searching through the command history for lines containing a specified string. For instance, type Control-R to search in the history for the next entry matching the search string typed so far. <code>clush</code> also recognizes special single-character prefixes that allows the user to see and modify the current nodeset (the nodes where the commands are executed).</dd>
<dt><code>Single-character interactive commands are:</code></dt>
<dd>
</dd><dt><code>clush&gt; ?</code></dt>
<dd> show current nodeset</dd>
<dt><code>clush&gt; =&lt;NODESET&gt;</code></dt>
<dd> set current nodeset</dd>
<dt><code>clush&gt; +&lt;NODESET&gt;</code></dt>
<dd> add nodes to current nodeset</dd>
<dt><code>clush&gt; -&lt;NODESET&gt;</code></dt>
<dd> remove nodes from current nodeset</dd>
<dt><code>clush&gt; !COMMAND</code></dt>
<dd> execute COMMAND on the local system</dd>
<dt><code>clush&gt; =</code></dt>
<dd> toggle the output format (gathered or standard mode) </dd>
<p> To leave an interactive session, type <code>quit</code> or Control-D.</p>
<dt><code>Local execution ( &#8211;worker=exec</code> or <code>-R exec</code> )</dt>
<dd> Instead of running provided command on remote nodes, <code>clush</code> can use the dedicated <i>exec</i> worker to launch the command <i>locally</i>, for each node. Some parameters could be used in the command line to make a different command for each node. <code>%h</code> or <code>%host</code> will be replaced by node name and <code>%r</code> or <code>%rank</code> by the remote rank [0-N] (to get a literal % use %%)</dd>
<dt><code>File copying mode ( &#8211;copy</code> )</dt>
<dd> When <code>clush</code> is started with the <code>-c</code> or <code>&#8211;copy</code> option, it will attempt to copy specified <i>file</i> and/or <i>dir</i> to the provided target cluster nodes. If the <code>&#8211;dest</code> option is specified, it will put the copied files there.</dd>
<dt><code>Reverse file copying mode ( &#8211;rcopy</code> )</dt>
<dd> When <code>clush</code> is started with the <code>&#8211;rcopy</code> option, it will attempt to retrieve specified <i>file</i> and/or <i>dir</i> from provided cluster nodes. If the <code>&#8211;dest</code> option is specified, it must be a directory path where the files will be stored with their hostname appended. If the destination path is not specified, it will take the first <i>file</i> or <i>dir</i> basename directory as the local destination.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show <code>clush</code> version number and exit</dd>
<dt><code>-s</code><i>&nbsp;<wbr>GROUPSOURCE</i>,<code>&nbsp;<wbr>&#8211;groupsource=</code><i>GROUPSOURCE</i></dt>
<dd> optional <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) group source to use</dd>
<dt><code>&#8211;nostdin</code></dt>
<dd> do not watch for possible input from stdin</dd>
<dt><code>-O</code><i>&nbsp;<wbr>&lt;KEY=VALUE&gt;</i>,<code>&nbsp;<wbr>&#8211;option=</code><i>&lt;KEY=VALUE&gt;</i></dt>
<dd> override any key=value <code><a href="/docs/linux/man/5-clush-conf/">clush.conf</a></code>(5) options (repeat as needed)</dd>
<dt><code>Selecting target nodes:</code></dt>
<dd>
</dd><dt><code>-w</code><i>&nbsp;<wbr>NODES</i></dt>
<dd> nodes where to run the command</dd>
<dt><code>-x</code><i>&nbsp;<wbr>NODES</i></dt>
<dd> exclude nodes from the node list</dd>
<dt><code>-a</code>,<code> &#8211;all</code></dt>
<dd> run command on all nodes</dd>
<dt><code>-g</code><i>&nbsp;<wbr>GROUP</i>,<code>&nbsp;<wbr>&#8211;group=</code><i>GROUP</i></dt>
<dd> run command on a group of nodes</dd>
<dt><code>-X</code><i>&nbsp;<wbr>GROUP</i></dt>
<dd> exclude nodes from this group</dd>
<dt><code>&#8211;hostfile=</code><i>FILE</i>,<code>&nbsp;<wbr>&#8211;machinefile=</code><i>FILE</i></dt>
<dd> path to a file containing a list of single hosts, node sets or node groups, separated by spaces and lines (may be specified multiple times, one per file)</dd>
<dt><code>&#8211;topology=</code><i>FILE</i></dt>
<dd> topology configuration file to use for tree mode</dd>
<dt><code>&#8211;pick=</code><i>N</i></dt>
<dd> pick N node(s) at random in nodeset</dd>
<dt><code>Output behaviour:</code></dt>
<dd>
</dd><dt><code>-q</code>,<code> &#8211;quiet</code></dt>
<dd> be quiet, print essential output only</dd>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd> be verbose, print informative messages</dd>
<dt><code>-d</code>,<code> &#8211;debug</code></dt>
<dd> output more messages for debugging purpose</dd>
<dt><code>-G</code>,<code> &#8211;groupbase</code></dt>
<dd> do not display group source prefix</dd>
<dt><code>-L</code></dt>
<dd> disable header block and order output by nodes; if -b/-B is not specified, <code>clush</code> will wait for all commands to finish and then display aggregated output of commands with same return codes, ordered by node name; alternatively, when used in conjunction with -b/-B (eg. -bL), <code>clush</code> will enable a &quot;life gathering&quot; of results by line, such as the next line is displayed as soon as possible (eg. when all nodes have sent the line)</dd>
<dt><code>-N</code></dt>
<dd> disable labeling of command line</dd>
<dt><code>-P</code>,<code> &#8211;progress</code></dt>
<dd> show progress during command execution; if writing is performed to standard input, the live progress indicator will display the global bandwidth of data written to the target nodes</dd>
<dt><code>-b</code>,<code> &#8211;dshbak</code></dt>
<dd> display gathered results in a dshbak-like way (note: it will only try to aggregate the output of commands with same return codes)</dd>
<dt><code>-B</code></dt>
<dd> like -b but including standard error</dd>
<dt><code>-r</code>,<code> &#8211;regroup</code></dt>
<dd> fold nodeset using node groups</dd>
<dt><code>-S</code></dt>
<dd> return the largest of command return codes</dd>
<dt><code>&#8211;color=</code><i>WHENCOLOR</i></dt>
<dd> whether to use ANSI colors to surround node or nodeset prefix/header with escape sequences to display them in color on the terminal. <i>WHENCOLOR</i> is <code>never</code>, <code>always</code> or <code>auto</code> (which use color if standard output/error refer to a terminal). Colors are set to [34m (blue foreground text) for stdout and [31m (red foreground text) for stderr, and cannot be modified.</dd>
<dt><code>&#8211;diff</code></dt>
<dd> show diff between common outputs (find the best reference output by focusing on largest nodeset and also smaller command return code)</dd>
<dt><code>File copying:</code></dt>
<dd>
</dd><dt><code>-c</code>,<code> &#8211;copy</code></dt>
<dd> copy local file or directory to remote nodes</dd>
<dt><code>&#8211;rcopy</code></dt>
<dd> copy file or directory from remote nodes</dd>
<dt><code>&#8211;dest=</code><i>DEST_PATH</i></dt>
<dd> destination file or directory on the nodes (optional: use the first source directory path when not specified)</dd>
<dt><code>-p</code></dt>
<dd> preserve modification times and modes</dd>
<dt><code>Connection options:</code></dt>
<dd>
</dd><dt><code>-f</code><i>&nbsp;<wbr>FANOUT</i>,<code>&nbsp;<wbr>&#8211;fanout=</code><i>FANOUT</i></dt>
<dd> do not execute more than FANOUT commands at the same time, useful to limit resource usage. In tree mode, the same <i>fanout</i> value is used on the head node and on each gateway (the <i>fanout</i> value is propagated). That is, if the <i>fanout</i> is <code>16</code>, each gateway will initate up to <code>16</code> connections to their target nodes at the same time. Default <i>fanout</i> value is defined in <code><a href="/docs/linux/man/5-clush-conf/">clush.conf</a></code>(5).</dd>
<dt><code>-l</code><i>&nbsp;<wbr>USER</i>,<code>&nbsp;<wbr>&#8211;user=</code><i>USER</i></dt>
<dd> execute remote command as user</dd>
<dt><code>-o</code><i>&nbsp;<wbr>OPTIONS</i>,<code>&nbsp;<wbr>&#8211;options=</code><i>OPTIONS</i></dt>
<dd> can be used to give ssh options, eg. <code>-o &quot;-p 2022 -i ~/.ssh/myidrsa&quot;</code>; these options are added first to ssh and override default ones</dd>
<dt><code>-t</code><i>&nbsp;<wbr>CONNECT_TIMEOUT</i>,<code>&nbsp;<wbr>&#8211;connect_timeout=</code><i>CONNECT_TIMEOUT</i></dt>
<dd> limit time to connect to a node</dd>
<dt><code>-u</code><i>&nbsp;<wbr>COMMAND_TIMEOUT</i>,<code>&nbsp;<wbr>&#8211;command_timeout=</code><i>COMMAND_TIMEOUT</i></dt>
<dd> limit time for command to run on the node</dd>
<dt><code>-R</code><i>&nbsp;<wbr>WORKER</i>,<code>&nbsp;<wbr>&#8211;worker=</code><i>WORKER</i></dt>
<dd> worker name to use for connection (<code>exec</code>, <code>ssh</code>, <code>rsh</code>, <code>pdsh</code>), default is <code>ssh</code></dd>
<dt><code>&#8211;remote=</code><i>REMOTE</i></dt>
<dd> whether to enable remote execution: in tree mode, &#8216;yes&#8217; forces connections to the leaf nodes for execution, &#8216;no&#8217; establishes connections up to the leaf parent nodes for execution (default is &#8216;yes&#8217;) </dd>
<p> For a short explanation of these options, see <code>-h, &#8211;help</code>.</dl>
<h2>EXIT STATUS</h2>
<p> By default, an exit status of zero indicates success of the <code>clush</code> command but gives no information about the remote commands exit status. However, when the <code>-S</code> option is specified, the exit status of <code>clush</code> is the largest value of the remote commands return codes. </p>
<p> For failed remote commands whose exit status is non-zero, and unless the combination of options <code>-qS</code> is specified, <code>clush</code> displays messages similar to:</p>
<dl>
<dt><code>clush: node[40-42]: exited with exit code 1</code></dt>
<dd></dd></dl>
<h2>EXAMPLES</h2>
<h3>Remote parallel execution</h3>
<dl>
<dt><code># clush -w node[3-5,62] uname -r</code></dt>
<dd> Run command <i>uname -r</i> in parallel on nodes: node3, node4, node5 and node62</dd></dl>
<h3>Local parallel execution</h3>
<dl>
<dt><code># clush -w node[1-3] &#8211;worker=exec ping -c1 %host</code></dt>
<dd> Run locally, in parallel, a ping command for nodes: node1, node2 and node3. You may also use <code>-R exec</code> as the shorter and pdsh compatible option.</dd></dl>
<h3>Display features</h3>
<dl>
<dt><code># clush -w node[3-5,62] -b uname -r</code></dt>
<dd> Run command <i>uname -r</i> on nodes[3-5,62] and display gathered output results (integrated <code>dshbak</code>-like).</dd>
<dt><code># clush -w node[3-5,62] -bL uname -r</code></dt>
<dd> Line mode: run command <i>uname -r</i> on nodes[3-5,62] and display gathered output results without default header block.</dd>
<dt><code># ssh node32 find /etc/yum.repos.d -type f | clush -w node[40-42] -b xargs ls -l</code></dt>
<dd> Search some files on node32 in /etc/yum.repos.d and use clush to list the matching ones on node[40-42], and use <code>-b</code> to display gathered results.</dd>
<dt><code># clush -w node[3-5,62] &#8211;diff dmidecode -s bios-version</code></dt>
<dd> Run this Linux command to get BIOS version on nodes[3-5,62] and show version differences (if any).</dd></dl>
<h3>All nodes</h3>
<dl>
<dt><code># clush -a uname -r</code></dt>
<dd> Run command <i>uname -r</i> on all cluster nodes, see <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) to setup all cluster nodes (<i>all:</i> field).</dd>
<dt><code># clush -a -x node[5,7] uname -r</code></dt>
<dd> Run command <i>uname -r</i> on all cluster nodes except on nodes node5 and node7.</dd>
<dt><code># clush -a &#8211;diff cat /some/file</code></dt>
<dd> Run command <i>cat /some/file</i> on all cluster nodes and show differences (if any), line by line, between common outputs.</dd></dl>
<h3>Node groups</h3>
<dl>
<dt><code># clush -w @oss modprobe lustre</code></dt>
<dd> Run command <i>modprobe lustre</i> on nodes from node group named <i>oss</i>, see <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) to setup node groups (<i>map:</i> field).</dd>
<dt><code># clush -g oss modprobe lustre</code></dt>
<dd> Same as previous example but using <code>-g</code> to avoid <i>@</i> group prefix.</dd>
<dt><code># clush -w @mds,@oss modprobe lustre</code></dt>
<dd> You may specify several node groups by separating them with commas (please see EXTENDED PATTERNS in <code><a href="/docs/linux/man/1-nodeset/">nodeset</a></code>(1) and also <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) for more information).</dd></dl>
<h3>Copy files</h3>
<dl>
<dt><code># clush -w node[3-5,62] &#8211;copy /etc/motd</code></dt>
<dd> Copy local file <i>/etc/motd</i> to remote nodes node[3-5,62].</dd>
<dt><code># clush -w node[3-5,62] &#8211;copy /etc/motd &#8211;dest /tmp/motd2</code></dt>
<dd> Copy local file <i>/etc/motd</i> to remote nodes node[3-5,62] at path <i>/tmp/motd2</i>.</dd>
<dt><code># clush -w node[3-5,62] -c /usr/share/doc/clustershell</code></dt>
<dd> Recursively copy local directory <i>/usr/share/doc/clustershell</i> to the same path on remote nodes node[3-5,62].</dd>
<dt><code># clush -w node[3-5,62] &#8211;rcopy /etc/motd &#8211;dest /tmp</code></dt>
<dd> Copy <i>/etc/motd</i> from remote nodes node[3-5,62] to local <i>/tmp</i> directory, each file having their remote hostname appended, eg. <i>/tmp/motd.node3</i>.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/clustershell/clush.conf</i></dt>
<dd> System-wide <code>clush</code> configuration file.</dd>
<dt><i>~/.clush.conf</i></dt>
<dd> This is the per-user <code>clush</code> configuration file.</dd>
<dt><i>~/.clush_history</i></dt>
<dd> File in which interactive <code>clush</code> command history is saved.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-clubak/">clubak</a></code>(1), <code><a href="/docs/linux/man/1-nodeset/">nodeset</a></code>(1), <code><a href="/docs/linux/man/3-readline/">readline</a></code>(3), <code><a href="/docs/linux/man/5-clush-conf/">clush.conf</a></code>(5), <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5).</p>
<h2>BUG REPORTS</h2>
<dl>
<dt><code>Use the following URL to submit a bug report or feedback:</code></dt>
<dd> <i><a rel="nofollow" href="https://github.com/cea-hpc/clustershell/issues">https://github.com/cea-hpc/clustershell/issues</a></i></dd></dl>
<h2>AUTHOR</h2>
<p> Stephane Thiell &lt;sthiell [at] stanford.edu&gt;</p>
<h2>COPYRIGHT</h2>
<p> GNU Lesser General Public License version 2.1 or later (LGPLv2.1+) </p>
<h2>Index</h2>
