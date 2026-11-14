---
title: "groups-conf(5)"
name: "groups-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-groups-conf/"
description: "groups.conf – Configuration file for ClusterShell node groups"
---

<p>groups.conf &#8211; Configuration file for ClusterShell node groups</p>
<h2>Description</h2>
<p>The ClusterShell library obtains its node groups configuration from the following sources in the following order:</p>
<dl>
<dt>1.</p>
<dd>user configuration file (<i>$XDG_CONFIG_HOME/clustershell/groups.conf</i>)</p>
<dt>2.</p>
<dd>local pip user installation (<i>$HOME/.local/etc/clustershell/groups.conf</i>)</p>
<dt>3.</p>
<dd>system-wide configuration file (<i>/etc/clustershell/groups.conf</i>) </p>
<p> If no <i>groups.conf</i> is found, group support will be disabled. </p>
<p> Additional configuration files are also read from the directories set by the confdir option, if present. See the <code>confdir</code> option below for further details. </p>
<p> Configuration files have a format in the style of RFC 822 potentially composed of several sections which may be present in any order. There are two types of sections: Main and <i>Group_source</i>:</p>
<dt><code>Main</code></p>
<dd>Global configuration options. There should be only one Main section.</p>
<dt><i>Group_source</i></p>
<dd>The <i>Group_source</i> section(s) define the configuration for each node group source (or namespace). This configuration consists in external commands definition (map, all, list and reverse). </p>
<p> Only <i>Group_source</i> section(s) are allowed in additional configuration files.</dl>
<h3>[Main] OPTIONS</h3>
<p>Configuration parameters of the <code>Main</code> section are described below.</p>
<dl>
<dt><code>default</code></p>
<dd>Specify the default group source (group namespace) used by the NodeSet parser when the user does not explicitly specify the group source (eg. &quot;@io&quot;).</p>
<dt><code>confdir</code></p>
<dd>Optional list of directories where the ClusterShell library should look for <code>.conf</code> files which define group sources to use. Each file in these directories with the .conf suffix should contain one or more <i>Group_source</i> sections as documented in [<i>Group_source</i>] options below. These will be merged with the group sources defined in <i>/etc/clustershell/groups.conf</i> to form the complete set of group sources that ClusterShell will use. Duplicate <i>Group_source</i> sections are not allowed. Note: .conf files that are not readable by the current user are ignored (except the one that defines the default group source). The variable <i>$CFGDIR</i> is replaced by the path of the highest priority configuration directory found (where groups.conf resides). The default confdir value enables both system-wide and any installed user configuration (thanks to <i>$CFGDIR</i>). Duplicate directory paths are ignored.</p>
<dt><code>autodir</code></p>
<dd>Optional list of directories where the ClusterShell library should look for <code>.yaml</code> files that define in-file group dictionaries. No need to call external commands for these files, they are parsed by the ClusterShell library itself. Multiple group source definitions in the same file is supported. The variable <i>$CFGDIR</i> is replaced by the path of the highest priority configuration directory found (where groups.conf resides). The default confdir value enables both system-wide and any installed user configuration (thanks to <i>$CFGDIR</i>). Duplicate directory paths are ignored.</dl>
<h3>[<i>Group_source</i>] OPTIONS</h3>
<p>Configuration parameters of each group source section are described below.</p>
<dl>
<dt><code>map</code></p>
<dd>Specify the external shell command used to resolve a group name into a nodeset, list of nodes or list of nodeset (separated by space characters or by carriage returns). The variable <i>$GROUP</i> is replaced before executing the command.</p>
<dt><code>all</code></p>
<dd>Optional external shell command that should return a nodeset, list of nodes or list of nodeset of all nodes for this group source. If not specified, the library will try to resolve all nodes by using the <code>list</code> external command in the same group source followed by <code>map</code> for each group.</p>
<dt><code>list</code></p>
<dd>Optional external shell command that should return the list of all groups for this group source (separated by space characters or by carriage returns).</p>
<dt><code>reverse</code></p>
<dd>Optional external shell command used to find the group(s) of a single node. The variable $NODE is previously replaced. If this upcall is not specified, the reverse operation is computed in memory by the library from the <i>list</i> and <i>map</i> external calls. Also, if the number of nodes to reverse is greater than the number of available groups, the <i>reverse</i> external command is avoided automatically.</p>
<dt><code>cache_time</code></p>
<dd>Number of seconds each upcall result is kept in cache, in memory only. Default is 3600 seconds. This is useful only for daemons using nodegroups. </p>
<p> When the library executes a group source external shell command, the current working directory is previously set to the corresponding confdir. This allows the use of relative paths for third party files in the command. </p>
<p> In addition to context-dependent $GROUP and $NODE variables described above, the two following variables are always available and also replaced before executing shell commands:</p>
<dt>&bull;</p>
<dd><i>$CFGDIR</i> is replaced by groups.conf highest priority base directory path</p>
<dt>&bull;</p>
<dd><i>$SOURCE</i> is replaced by current source name </p>
<p> Each external command might return a non-zero return code when the operation is not doable. But if the call return zero, for instance, for a non-existing group, the user will not receive any error when trying to resolve such unknown group. The desired behaviour is up to the system administrator.</dl>
<h2>Resource Usage</h2>
<p>All external command results are cached in memory to avoid multiple calls. Each result is kept for a limited amount of time. See cache_time option to tune this behaviour.</p>
<h2>Examples</h2>
<p>Simple configuration file for local groups and slurm partitions binding.</p>
<h3><i>groups.conf</i></h3>
<pre>[Main]
default: local
confdir: /etc/clustershell/groups.conf.d $CFGDIR/groups.conf.d
autodir: /etc/clustershell/groups.d $CFGDIR/groups.d
[local]
map: sed -n 's/^$GROUP:(.*)/1/p' /etc/clustershell/groups
list: sed -n 's/^\(<code>[0-9A-Za-z_-]</code>*\):.*/\1/p' /etc/clustershell/groups
[slurm]
map: sinfo -h -o &quot;%N&quot; -p $GROUP
all: sinfo -h -o &quot;%N&quot;
list: sinfo -h -o &quot;%P&quot;
reverse: sinfo -h -N -o &quot;%P&quot; -n $NODE</pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/clustershell/groups.conf</i></p>
<dd>System-wide node groups configuration file.</p>
<dt><i>/etc/clustershell/groups.conf.d/</i></p>
<dd>Recommended directory for additional configuration files.</p>
<dt><i>/etc/clustershell/groups.d/</i></p>
<dd>Recommended directory for <i>autodir</i>, where native group definition files (.yaml files) are found.</p>
<dt><i>$XDG_CONFIG_HOME/clustershell/groups.conf</i></p>
<dd>Main user groups.conf configuration file. If $XDG_CONFIG_HOME is not defined, <i>$HOME/.config/clustershell/groups.conf</i> is used instead.</p>
<dt><i>$HOME/.local/etc/clustershell/groups.conf</i></p>
<dd>Local groups.conf user configuration file (default installation for pip &#8211;user)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-clush/">clush</a></code>(1), <code><a href="/docs/linux/man/1-clubak/">clubak</a></code>(1), <code><a href="/docs/linux/man/1-nodeset/">nodeset</a></code>(1) </p>
<p> <i><a rel="nofollow" href="http://clustershell.sourceforge.net/">http://clustershell.sourceforge.net/</a></i></p>
<h2>Author</h2>
<p>Stephane Thiell, &lt;sthiell [at] stanford.edu&gt;</p>
<h2>Copyright</h2>
<p>GNU Lesser General Public License version 2.1 or later (LGPLv2.1+)</p>
