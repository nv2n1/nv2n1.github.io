---
title: "pidof(8)"
name: "pidof"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pidof/"
description: "pidof — find the process ID of a running program."
---

<p>pidof &#8212; find the process ID of a running program.</p>
<h2>Synopsis</h2>
<p><code>pidof</code> [<code>-s</code>] [<code>-c</code>] [<code>-n</code>] [<code>-x</code>] [<code>-z</code>] [<code>-o</code> <i>omitpid[,omitpid&#8230;]</i>] [<code>-o</code> <i>omitpid[,omitpid&#8230;]&#8230;</i>] [<code>-d</code> <i>sep</i>] <code>program</code> [<code>program&#8230;</code>]</p>
<h2>Description</h2>
<p><code>Pidof</code> finds the process id&#8217;s (PIDs) of the named programs. It prints those id&#8217;s on the standard output. This program is on some systems used in run-level change scripts, especially when the system has a <i>System-V</i> like <i>rc</i> structure. In that case these scripts are located in /etc/rc?.d, where ? is the runlevel. If the system has a <code>start-stop-daemon</code> (8) program that should be used instead.</p>
<h2>Options</h2>
<dl>
<dt>-s</p>
<dd>Single shot &#8211; this instructs the program to only return one <i>pid</i>.</p>
<dt>-c</p>
<dd>Only return process PIDs that are running with the same root directory. This option is ignored for non-root users, as they will be unable to check the current root directory of processes they do not own.</p>
<dt>-n</p>
<dd>Avoid <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system function call on all binaries which are located on network based file systems like <code>NFS</code>. Instead of using this option the variable <code>PIDOF_NETFS</code> may be set and exported.</p>
<dt>-q</p>
<dd>Do not display matched PIDs to standard out. Simply exit with a status of true or false to indicate whether a matching PID was found.</p>
<dt>-x</p>
<dd>Scripts too &#8211; this causes the program to also return process id&#8217;s of shells running the named scripts.</p>
<dt>-z</p>
<dd>Try to detect processes which are stuck in zombie (Z) status. Usually these processes are skipped as trying to deal with them can cause pidof or related tools to hang. Note: In the past pidof would ignore processes in the uninterruptable state (D), unless the -z flag was specified. This is no longer the case. The pidof program will find and report processes in the D state whether -z is specified or not.</p>
<dt>-d <i>sep</i></p>
<dd>Tells <i>pidof</i> to use <i>sep</i> as an output separator if more than one PID is shown. The default separator is a space.</p>
<dt>-o <i>omitpid</i></p>
<dd>Tells <i>pidof</i> to omit processes with that process id. The special pid <code>%PPID</code> can be used to name the parent process of the <i>pidof</i> program, in other words the calling shell or shell script.</dl>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></p>
<dd>At least one program was found with the requested name.</p>
<dt><code>1</code></p>
<dd>No program was found with the requested name.</dl>
<h2>Notes</h2>
<p><i>pidof</i> is actually the same program as <i>killall5</i>; the program behaves according to the name under which it is called. When <i>pidof</i> is invoked with a full pathname to the program it should find the pid of, it is reasonably safe. Otherwise it is possible that it returns PIDs of running programs that happen to have the same name as the program you&#8217;re after but are actually other programs. Note that the executable name of running processes is calculated with <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), so symbolic links to executables will also match. Zombie processes or processes in disk sleep (states Z and D, respectively) are ignored, as attempts to access the stats of these will sometimes fail. The -z flag (see above) tells pidof to try to detect these sleeping and zombie processes, at the risk of failing or hanging. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-halt/">halt</a></code>(8), <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8), <code><a href="/docs/linux/man/8-killall5/">killall5</a></code>(8)</p>
<h2>Author</h2>
<p>Miquel van Smoorenburg, miquels [at] cistron.nl</p>
