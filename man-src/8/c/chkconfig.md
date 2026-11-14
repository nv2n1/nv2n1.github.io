---
title: "chkconfig(8)"
name: "chkconfig"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chkconfig/"
description: "chkconfig – updates and queries runlevel information for system services"
---

<p>chkconfig &#8211; updates and queries runlevel information for system services</p>
<h2>Synopsis</h2>
<p><code>chkconfig</code> [<code>&#8211;list</code>] [<code>&#8211;type</code> <i>type</i>] [<i>name</i>]<br />
 <code>chkconfig</code> <code>&#8211;add</code> <i>name</i><br />
 <code>chkconfig</code> <code>&#8211;del</code> <i>name</i><br />
 <code>chkconfig</code> <code>&#8211;override</code> <i>name</i><br />
 <code>chkconfig</code> [<code>&#8211;level</code> <i>levels</i>] [<code>&#8211;type</code> <i>type</i>] [<code>&#8211;no-redirect</code>] <i>name</i> &lt;<code>on</code>|<code>off</code>|<code>reset</code>|<code>resetpriorities</code>&gt;<br />
 <code>chkconfig</code> [<code>&#8211;level</code> <i>levels</i>] [<code>&#8211;type</code> <i>type</i>] [<code>&#8211;no-redirect</code>] <i>name</i> </p>
<h2>Description</h2>
<p><code>chkconfig</code> provides a simple command-line tool for maintaining the /etc/rc[0-6].d directory hierarchy by relieving system administrators of the task of directly manipulating the numerous symbolic links in those directories. This implementation of <code>chkconfig</code> was inspired by the <code>chkconfig</code> command present in the IRIX operating system. Rather than maintaining configuration information outside of the /etc/rc[0-6].d hierarchy, however, this version directly manages the symlinks in /etc/rc[0-6].d. This leaves all of the configuration information regarding what services <i>init</i> starts in a single location. <code>chkconfig</code> has five distinct functions: adding new services for management, removing services from management, listing the current startup information for services, changing the startup information for services, and checking the startup state of a particular service. When <code>chkconfig</code> is run with only a service name, it checks to see if the service is configured to be started in the current runlevel. If it is, <code>chkconfig</code> returns true; otherwise it returns false. The <code>&#8211;level</code> option may be used to have <code>chkconfig</code> query an alternative runlevel rather than the current one. When <code>chkconfig</code> is run with the <code>&#8211;list</code> argument, or no arguments at all, a listing is displayed of all services and their current configuration. If one of <code>on</code>, <code>off</code>, <code>reset</code>, or <code>resetpriorities</code> is specified after the service name, <code>chkconfig</code> changes the startup information for the specified service. The <code>on</code> and <code>off</code> flags cause the service to be started or stopped, respectively, in the runlevels being changed. The <code>reset</code> flag resets the on/off state for all runlevels for the service to whatever is specified in the init script in question, while the <code>resetpriorities</code> flag resets the start/stop priorities for the service to whatever is specified in the init script. By default, the <code>on</code> and <code>off</code> options affect only runlevels 2, 3, 4, and 5, while <code>reset</code> and <code>resetpriorities</code> affects all of the runlevels. The <code>&#8211;level</code> option may be used to specify which runlevels are affected. Note that for every service, each runlevel has either a start script or a stop script. When switching runlevels, init will not re-start an already-started service, and will not re-stop a service that is not running. <code>chkconfig</code> also can manage xinetd scripts via the means of xinetd.d configuration files. Note that only the <code>on</code>, <code>off</code>, and <code>&#8211;list</code> commands are supported for xinetd.d services. <code>chkconfig</code> supports a <code>&#8211;type</code> argument to limit actions to only a specific type of services, in the case where services of either type may share a name. Possible values for <i>type</i> are <i>sysv</i> and <i>xinetd</i>. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;level </code><i>levels</i></p>
<dd>Specifies the run levels an operation should pertain to. It is given as a string of numbers from 0 to 6. For example, <code>&#8211;level 35</code> specifies runlevels 3 and 5. </p>
<dt><code>&#8211;no-redirect</code></p>
<dd>When chkconfig is run on a system that uses systemd as its init system, chkconfig will forward commands to systemd if a systemd service file exists for it. This switch turns off the redirection to systemd and only operates on the symlinks in /etc/rc[0-6].d. This option is only valid when <code>on</code>, <code>off</code>, or no command (to check enablement) is passed to a service. </p>
<dt><code>&#8211;add</code> <i>name</i></p>
<dd>This option adds a new service for management by <code>chkconfig</code>. When a new service is added, <code>chkconfig</code> ensures that the service has either a start or a kill entry in every runlevel. If any runlevel is missing such an entry, <code>chkconfig</code> creates the appropriate entry as specified by the default values in the init script. Note that default entries in LSB-delimited &#8216;INIT INFO&#8217; sections take precedence over the default runlevels in the initscript; if any Required-Start or Required-Stop entries are present, the start and stop priorities of the script will be adjusted to account for these dependencies. </p>
<dt><code>&#8211;del</code> <i>name</i></p>
<dd>The service is removed from <code>chkconfig</code> management, and any symbolic links in /etc/rc[0-6].d which pertain to it are removed. </p>
<p> Note that future package installs for this service may run <code>chkconfig &#8211;add</code>, which will re-add such links. To disable a service, run <code>chkconfig </code><i>name</i> <code>off</code>. </p>
<dt><code>&#8211;override</code> <i>name</i></p>
<dd>If service <i>name</i> is configured exactly as it would be if the <code>&#8211;add</code> option had been specified with no override file in /etc/chkconfig.d/<i>name</i>, and if /etc/chkconfig.d/<i>name</i> now exists and is specified differently from the base initscript, change the configuration for service <i>name</i> to follow the overrides instead of the base configuration. </p>
<dt><code>&#8211;list</code> <i>name</i></p>
<dd>This option lists all of the services which <code>chkconfig</code> knows about, and whether they are stopped or started in each runlevel. If <i>name</i> is specified, information in only display about service <i>name</i>. </p>
</dl>
<h2>Runlevel Files</h2>
<p>Each service which should be manageable by <code>chkconfig</code> needs two or more commented lines added to its init.d script. The first line tells <code>chkconfig</code> what runlevels the service should be started in by default, as well as the start and stop priority levels. If the service should not, by default, be started in any runlevels, a <code>&#8211;</code> should be used in place of the runlevels list. The second line contains a description for the service, and may be extended across multiple lines with backslash continuation. </p>
<p> For example, random.init has these three lines: </p>
<pre># chkconfig: 2345 20 80
# description: Saves and restores system entropy pool for \
# higher quality random number generation.</pre>
<p>This says that the random script should be started in levels 2, 3, 4, and 5, that its start priority should be 20, and that its stop priority should be 80. You should be able to figure out what the description says; the \ causes the line to be continued. The extra space in front of the line is ignored. </p>
<p> chkconfig also supports LSB-style init stanzas, and will apply them in preference to &quot;chkconfig:&quot; lines where available. A LSB stanza looks like: </p>
<pre>### BEGIN INIT INFO
# Provides: foo
# Required-Start: bar
# Defalt-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Description: Foo init script
### END INIT INFO</pre>
<p>In this case, the start priority of &quot;foo&quot; would be changed such that it is higher than the &quot;bar&quot; start priority, if &quot;bar&quot; is enabled. Care must be taken when adding dependencies, as they can cause vast shifts in the start and stop priorities of many scripts.</p>
<h2>Override Files</h2>
<p>Files in /etc/chkconfig.d/<i>servicename</i> are parsed using the same comments that chkconfig notices in init service scripts, and override values in the init service scripts themselves.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-init/">init</a></i>(8) <i><a href="/docs/linux/man/8-ntsysv/">ntsysv</a></i>(8) <i><a href="/docs/linux/man/8-system-config-services/">system-config-services</a></i>(8) </p>
<h2>Author</h2>
<pre>Erik Troan &lt;ewt [at] redhat.com&gt;</pre>
