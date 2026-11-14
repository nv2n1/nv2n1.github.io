---
title: "update-rc-d(8)"
name: "update-rc-d"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-rc-d/"
description: "update-rc.d – install and remove System-V style init script links"
---

<p>update-rc.d &#8211; install and remove System-V style init script links</p>
<h2>Synopsis</h2>
<p><code>update-rc.d</code> [<i>-f</i>] <i>name</i> <code>remove</code> </p>
<p> <code>update-rc.d</code> <i>name</i> <code>defaults</code> </p>
<p> <code>update-rc.d</code> <i>name</i> <code>defaults-disabled</code> </p>
<p> <code>update-rc.d</code> <i>name</i> <code>disable|enable</code> [ <i>S|2|3|4|5</i> ]</p>
<h2>Description</h2>
<p><code>update-rc.d</code> updates the System V style init script links <code>/etc/rc</code><i>runlevel</i><code>.d/</code><i>NNname</i> whose target is the script <code>/etc/init.d/</code><i>name</i>. These links are run by <code>init</code> when it changes runlevels; they are generally used to start and stop system services such as daemons. <i>runlevel</i> is one of the runlevels supported by <code>init</code>, namely, <code>0123456789S</code>, and <i>NN</i> is the two-digit sequence number that determines where in the sequence <code>init</code> will run the scripts. </p>
<p> This manpage documents only the usage and behaviour of <code>update-rc.d</code>. For a discussion of the System V style init script arrangements please see <code><a href="/docs/linux/man/8-init/">init</a></code>(8) and the <i>Debian Policy Manual</i>.</p>
<h2>Installing Init Script Links</h2>
<p>update-rc.d requires dependency and runlevel information to be provided in the init.d script LSB comment header of all init.d scripts. See the <a href="/docs/linux/man/8-insserv/">insserv</a>(8) manual page for details about the LSB header format. </p>
<p> When run with the <code>defaults</code> option, <code>update-rc.d</code> makes links named <code>/etc/rc</code><i>runlevel</i><code>.d/[SK]</code><i>NNname</i> that point to the script <code>/etc/init.d/</code><i>name</i>, using runlevel and dependency information from the init.d script LSB comment header. </p>
<p> When run with the <code>defaults-disabled</code> option, <code>update-rc.d</code> makes links named <code>/etc/rc</code><i>runlevel</i><code>.d/K</code><i>NNname</i> that point to the script <code>/etc/init.d/</code><i>name</i>, using dependency information from the init.d script LSB comment header. This means that the init.d script will be disabled (see below). </p>
<p> If any files named <code>/etc/rc</code><i>runlevel</i><code>.d/[SK]??</code><i>name</i> already exist then <code>update-rc.d</code> does nothing. The program was written this way so that it will never change an existing configuration, which may have been customized by the system administrator. The program will only install links if none are present, i.e., if it appears that the service has never been installed before. </p>
<p> Older versions of <code>update-rc.d</code> also supported <code>start</code> and <code>stop</code> options. These options are no longer supported, and are now equivalent to the <code>defaults</code> option. </p>
<p> A common system administration error is to delete the links with the thought that this will &quot;disable&quot; the service, i.e., that this will prevent the service from being started. However, if all links have been deleted then the next time the package is upgraded, the package&#8217;s <i>postinst</i> script will run <code>update-rc.d</code> again and this will reinstall links at their factory default locations. The correct way to disable services is to configure the service as stopped in all runlevels in which it is started by default. In the System V init system this means renaming the service&#8217;s symbolic links from <code>S</code> to <code>K</code>. .P The script .BI /etc/init.d/ name must exist before <code>update-rc.d</code> is run to create the links.</p>
<h2>Removing Scripts</h2>
<p>When invoked with the <i>remove</i> option, update-rc.d removes any links in the <code>/etc/rc</code><i>runlevel</i><code>.d</code> directories to the script <code>/etc/init.d/</code><i>name</i>. The script must have been deleted already. If the script is still present then <code>update-rc.d</code> aborts with an error message. .P <code>update-rc.d</code> is usually called from a package&#8217;s post-removal script when that script is given the <code>purge</code> argument. Any files in the <code>/etc/rc</code><i>runlevel</i><code>.d</code> directories that are not symbolic links to the script <code>/etc/init.d/</code><i>name</i> will be left untouched.</p>
<h2>Disabling Init Script Start Links</h2>
<p>When run with the <code>disable</code> [ <i>S|2|3|4|5</i> ] options, <code>update-rc.d</code> modifies existing runlevel links for the script <code>/etc/init.d/</code><i>name</i> by renaming start links to stop links with a sequence number equal to the difference of 100 minus the original sequence number. </p>
<p> When run with the <code>enable</code> [ <i>S|2|3|4|5</i> ] options, <code>update-rc.d</code> modifies existing runlevel links for the script <code>/etc/init.d/</code><i>name</i> by renaming stop links to start links with a sequence number equal to the positive difference of current sequence number minus 100, thus returning to the original sequence number that the script had been installed with before disabling it. .P Both of these options only operate on start runlevel links of S, 2, 3, 4 or 5. If no start runlevel is specified after the disable or enable keywords, the script will attempt to modify links in all start runlevels.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Force removal of symlinks even if <code>/etc/init.d/</code><i>name</i> still exists.</dl>
<h2>Examples</h2>
<p>Insert links using the defaults: <code>update-rc.d foobar defaults</code> </p>
<p> The equivalent dependency header would have start and stop dependencies on $remote_fs and $syslog, and start in runlevels 2-5 and stop in runlevels 0, 1 and 6. </p>
<p> Remove all links for a script (assuming foobar has been deleted already): <code>update-rc.d foobar remove</code> </p>
<p> Example of disabling a service: <code>update-rc.d foobar disable</code> </p>
<p> Example of a command for installing a system initialization-and-shutdown script: <code>update-rc.d foobar defaults</code> </p>
<p> Example of a command for disabling a system initialization-and-shutdown script: <code>update-rc.d foobar disable</code></p>
<h2>Bugs</h2>
<p>See <i><a rel="nofollow" href="http://bugs.debian.org/sysv-rc">http://bugs.debian.org/sysv-rc</a></i> and <i><a rel="nofollow" href="http://bugs.debian.org/init-system-helpers">http://bugs.debian.org/init-system-helpers</a></i>.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/init.d/</code></p>
<dd>The directory containing the actual init scripts.</p>
<dt><code>/etc/rc?.d/</code></p>
<dd>The directories containing the links used by <code>init</code> and managed by <code>update-rc.d .</code></p>
<dt><code>/etc/init.d/skeleton</code></p>
<dd>Model for use by writers of <code>init.d</code> scripts.</dl>
<h2>See Also</h2>
<pre><i>Debian Policy Manual</i>,
<code>/etc/init.d/skeleton</code>,
<code><a href="//www.systutorials.com/docs/linux/man/8-insserv/">insserv</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-init/">init</a></code>(8)</pre>
<h2>Author</h2>
<p>Ian Jackson, Miquel van Smoorenburg </p>
<p> License: GNU General Public License v2 or Later (GPLv2+)</p>
<h2>Copyright</h2>
<p>2001 Henrique de Moraes Holschuh</p>
