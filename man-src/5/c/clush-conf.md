---
title: "clush-conf(5)"
name: "clush-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-clush-conf/"
description: "clush.conf – Configuration file for clush"
---

<p>clush.conf &#8211; Configuration file for clush</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/1-clush/">clush</a></code>(1) obtains configuration options from the following sources in the following order:</p>
<dl>
<dt>1.</p>
<dd>command-line options</p>
<dt>2.</p>
<dd>user configuration file (<i>$XDG_CONFIG_HOME/clustershell/clush.conf</i>)</p>
<dt>3.</p>
<dd>local pip user installation (<i>$HOME/.local/etc/clustershell/clush.conf</i>)</p>
<dt>4.</p>
<dd>system-wide configuration file (<i>/etc/clustershell/clush.conf</i>) </p>
<p> For each parameter, the first obtained value will be used. </p>
<p> The configuration file has a format in the style of RFC 822 composed of one main section:</p>
<dt><code>Main</code></p>
<dd>Program options definition</dl>
<h3>[Main]</h3>
<p>Configuration parameters of the <code>Main</code> section are described below.</p>
<dl>
<dt><code>fanout</code></p>
<dd>Size of the sliding window (fanout) of active commands for <code>clush</code>. This <i>fanout</i> is used to avoid too many concurrent connections and to conserve resources on the initiating hosts. In tree mode, the same <i>fanout</i> value is used on the head node and on each gateway (the <i>fanout</i> value is propagated). That is, if the <i>fanout</i> is <code>16</code> on the head node, each gateway will initate up to <code>16</code> connections to their target nodes at the same time.</p>
<dt><code>connect_timeout</code></p>
<dd>Timeout in seconds to allow a connection to establish. This parameter is passed to ssh. If set to <i>0</i>, no timeout occurs.</p>
<dt><code>command_timeout</code></p>
<dd>Timeout in seconds to allow a command to complete since the connection has been established. This parameter is passed to ssh. In addition, the ClusterShell library ensures that any commands complete in less than ( connect_timeout + command_timeout ). If set to <i>0</i>, no timeout occurs.</p>
<dt><code>color</code></p>
<dd>Whether to use ANSI colors to surround node or nodeset prefix/header with escape sequences to display them in color on the terminal. Valid arguments are <code>never</code>, <code>always</code> or <code>auto</code> (which use color if standard output/error refer to a terminal). Colors are set to [34m (blue foreground text) for stdout and [31m (red foreground text) for stderr, and cannot be modified.</p>
<dt><code>fd_max</code></p>
<dd>Maximum number of open file descriptors permitted per clush process (soft resource limit for open files). This limit can never exceed the system (hard) limit. The <i>fd_max</i> (soft) and system (hard) limits should be high enough to run <code>clush</code>, although their values depend on your <i>fanout</i> value.</p>
<dt><code>history_size</code></p>
<dd>Set the maximum number of history entries saved in the GNU readline history list. Negative values imply unlimited history file size.</p>
<dt><code>node_count</code></p>
<dd>Should <code>clush</code> display additional (node count) information in buffer header? (<i>yes</i>/<i>no</i>)</p>
<dt><code>verbosity</code></p>
<dd>Set the verbosity level: <i>0</i> (quiet), <i>1</i> (default), <i>2</i> (verbose) or more (debug).</p>
<dt><code>ssh_user</code></p>
<dd>Set the ssh user to use for remote connection (default is to not specify).</p>
<dt><code>ssh_path</code></p>
<dd>Set the ssh binary path to use for remote connection (default is <i>ssh</i>).</p>
<dt><code>ssh_options</code></p>
<dd>Set additional options to pass to the underlying ssh command.</p>
<dt><code>scp_path</code></p>
<dd>Set the scp binary path to use for remote copy (default is <i>scp</i>).</p>
<dt><code>scp_options</code></p>
<dd>Set additional options to pass to the underlying scp command. If not specified, ssh_options are used instead.</p>
<dt><code>rsh_path</code></p>
<dd>Set the rsh binary path to use for remote connection (default is <i>rsh</i>). You could easily use mrsh or krsh by simply changing this value.</p>
<dt><code>rcp_path</code></p>
<dd>Same a rsh_path for rcp command. (Default is <i>rcp</i>)</p>
<dt><code>rsh_options</code></p>
<dd>Set additional options to pass to the underlying rsh/rcp command.</dl>
<h2>Examples</h2>
<p>Simple configuration file.</p>
<h3><i>clush.conf</i></h3>
<pre>[Main]
fanout: 128
connect_timeout: 15
command_timeout: 0
history_size: 100
color: auto
fd_max: 10240
node_count: yes</pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/clustershell/clush.conf</i></p>
<dd>System-wide clush configuration file.</p>
<dt><i>$XDG_CONFIG_HOME/clustershell/clush.conf</i></p>
<dd>User configuration file for clush. If $XDG_CONFIG_HOME is not defined, <i>$HOME/.config/clustershell/clush.conf</i> is used instead.</p>
<dt><i>$HOME/.local/etc/clustershell/clush.conf</i></p>
<dd>Local user configuration file for clush (default installation for pip &#8211;user)</p>
<dt><i>~/.clush.conf</i></p>
<dd>Deprecated per-user clush configuration file.</dl>
<h2>History</h2>
<p>As of ClusterShell version 1.3, the <code>External</code> section has been removed from <i>clush.conf</i>. External commands whose outputs were used by <code>clush</code> (-a, -g, -X) are now handled by the library itself and defined in <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-clush/">clush</a></code>(1), <code><a href="/docs/linux/man/1-nodeset/">nodeset</a></code>(1), <code><a href="/docs/linux/man/5-groups-conf/">groups.conf</a></code>(5) </p>
<p> <i><a rel="nofollow" href="http://clustershell.sourceforge.net/">http://clustershell.sourceforge.net/</a></i></p>
<h2>Author</h2>
<p>Stephane Thiell, &lt;sthiell [at] stanford.edu&gt;</p>
<h2>Copyright</h2>
<p>GNU Lesser General Public License version 2.1 or later (LGPLv2.1+)</p>
