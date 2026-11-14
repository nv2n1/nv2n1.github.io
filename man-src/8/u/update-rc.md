---
title: "update-rc(8)"
name: "update-rc"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-rc/"
description: "update-rc.d – install and remove System-V style init script links"
---

<p>update-rc.d &#8211; install and remove System-V style init script links</p>
<h2>Synopsis</h2>
<p><code>update-rc.d</code> [<i>-n</i>] [<i>-f</i>] <i>name</i><code> remove</code></p>
<dl>
<dt> <code>update-rc.d</code> [<i>-n</i>] <i>name</i><code> defaults</code> [<i>NN</i> | <i>SS</i> <i>KK</i>]</p>
<dt> <code>update-rc.d</code> [<i>-n</i>] <i>name</i> <code>start</code>|<code>stop</code> <i>NN runlevel</i> [<i>runlevel</i>]&#8230; <code>.</code> <code>start</code>|<code>stop</code> <i>NN runlevel</i> [<i>runlevel</i>]&#8230; <code>.</code> &#8230;</p>
<dt> <code>update-rc.d</code> [<i>-n</i>] <i>name</i><code> disable|enable </code> [<i> S|2|3|4|5 </i>]</dl>
<h2>Description</h2>
<p><code>update-rc.d</code></p>
<dd>updates the System V style init script links <code>/etc/rc</code><i>runlevel</i><code>.d/</code><i>NNname</i> whose target is the script <code>/etc/init.d/</code><i>name</i>. These links are run by <code>init</code> when it changes runlevels; they are generally used to start and stop system services such as daemons. <i>runlevel</i> is one of the runlevels supported by <code>init</code>, namely, <code>0123456789S</code>, and <i>NN</i> is the two-digit sequence number that determines where in the sequence <code>init</code> will run the scripts. This manpage documents only the usage and behaviour of <code>update-rc.d</code>. For a discussion of the System V style init script arrangements please see <code><a href="/docs/linux/man/8-init/">init</a></code>(8) and the <i>Debian Policy Manual</i>. </p>
<h2>Installing Init Script Links</h2>
<p>update-rc.d has two modes of operation for installing scripts into the boot sequence. A legacy mode where command line arguments are used to decide the sequence and runlevel configuration, and the default mode where dependency and runlevel information in the init.d script LSB comment header is used instead. Such header is required to be present in init.d scripts. See the <a href="/docs/linux/man/8-insserv/">insserv</a>(8) manual page for details about the LSB header format. The boot sequencing method is decided during installation or upgrades. During upgrades, if there are no loops in the dependencies declared by LSB headers of all installed init.d scripts and no obsolete init.d scripts, the boot system is converted to dependency based boot sequencing. The conversion to dependency based boot sequencing is one-way. The machines using the legacy mode will have a file /etc/init.d/.legacy-bootordering . </p>
<p> Packages installing init.d scripts should make sure both methods work, for compatiblity with systems where the migration have not been done yet. </p>
<p> For legacy mode, the following section documents the old behaviour. </p>
<p> When run with either the <code>defaults</code>, <code>start</code>, or <code>stop</code> options, <code>update-rc.d</code> makes links <code>/etc/rc</code><i>runlevel</i><code>.d/[SK]</code><i>NNname</i> that point to the script <code>/etc/init.d/</code><i>name</i>. </p>
<p> If any files <code>/etc/rc</code><i>runlevel</i><code>.d/[SK]??</code><i>name</i> already exist then <code>update-rc.d</code> does nothing. The program was written this way so that it will never change an existing configuration, which may have been customized by the system administrator. The program will only install links if none are present, i.e., if it appears that the service has never been installed before. </p>
<p> A common system administration error is to delete the links with the thought that this will &quot;disable&quot; the service, i.e., that this will prevent the service from being started. However, if all links have been deleted then the next time the package is upgraded, the package&#8217;s <i>postinst</i> script will run <code>update-rc.d</code> again and this will reinstall links at their factory default locations. The correct way to disable services is to configure the service as stopped in all runlevels in which it is started by default. In the System V init system this means renaming the service&#8217;s symbolic links from <code>S</code> to <code>K</code>. </p>
<p> If <code>defaults</code> is used then <code>update-rc.d</code> will make links to start the service in runlevels <code>2345</code> and to stop the service in runlevels <code>016</code>. By default all the links will have sequence number 20, but this should be overridden if there are dependencies. For example if daemon B depends on A, then A must be started before B and B must be killed before A. You accomplish this by supplying two NN arguments. In general, core daemons should start early and be killed late, whilst applications can start late and be killed early. See EXAMPLES below. </p>
<p> The first NN argument supplies the start sequence number and the second NN argument supplies the kill sequence number. Kill scripts are called first, passing a stop argument. Then start scripts are called passing a start argument. In either case, calls happen in ascending sequence number order. </p>
<p> Supplying a single NN argument will use the same number for both start and kill links. This is supported for backward compatibility but is discouraged, as it may lead to inconsistent settings. As a rule of thumb, if you increase the start sequence number you should also decrease the stop sequence number, and vice-versa. </p>
<p> As a rule of thumb, the sequence number of the stop link should be 100 minus the sequence number of the start link; this causes services to be stopped in the opposite order to that in which they are started. Obviously, therefore, the default stop sequence number should be 80. Defaulting to 20, as <code>update-rc.d</code> does, is an old bug that cannot be fixed because of the risk of breaking things. </p>
<p> Instead of <code>defaults</code> one can give one or more sets of arguments specifying particular runlevels in which to start or stop the service. Each of these sets of arguments starts with the keyword <code>start</code> or <code>stop</code> and a sequence number <i>NN</i>, followed by one or more runlevel numbers. The set is terminated by a solitary full stop character. When explicit specification, rather than <code>defaults</code>, is used there will usually be one <code>start</code> and one <code>stop</code> set. If different sequence codes are required in different runlevels then several <code>start</code> sets or several <code>stop</code> sets may be specified. If this is done and the same runlevel is named in multiple sets then only the last one counts. Therefore it is not possible to create multiple <code>start</code> or multiple <code>stop</code> links for a service in a single runlevel directory. </p>
<p> The script <code>/etc/init.d/</code><i>name</i> must exist before <code>update-rc.d</code> is run to create the links.</p>
<h2>Removing Scripts</h2>
<p>When invoked with the <i>remove</i> option, update-rc.d removes any links in the <code>/etc/rc</code><i>runlevel</i><code>.d</code> directories to the script <code>/etc/init.d/</code><i>name</i>. The script must have been deleted already. If the script is still present then <code>update-rc.d</code> aborts with an error message. </p>
<p> <code>update-rc.d</code> is usually called from a package&#8217;s post-removal script when that script is given the <code>purge</code> argument. Any files in the <code>/etc/rc</code><i>runlevel</i><code>.d</code> directories that are not symbolic links to the script <code>/etc/init.d/</code><i>name</i> will be left untouched.</p>
<h2>Disabling Init Script Start Links</h2>
<p>When run with the <code>disable</code> [ <code>S|2|3|4|5</code> ] options, <code>update-rc.d</code> modifies existing runlevel links for the script <code>/etc/init.d/</code><i>name</i> by renaming start links to stop links with a sequence number equal to the difference of 100 minus the original sequence number. </p>
<p> When run with the <code>enable</code> [ <code>S|2|3|4|5</code> ] options, <code>update-rc.d</code> modifies existing runlevel links for the script <code>/etc/init.d/</code><i>name</i> by renaming stop links to start links with a sequence number equal to the positive difference of current sequence number minus 100, thus returning to the original sequence number that the script had been installed with before disabling it. </p>
<p> Both of these options only operate on start runlevel links of S, 2, 3, 4 or 5. If no start runlevel is specified after the disable or enable keywords, the script will attempt to modify links in all start runlevels.</p>
<h2>Options</h2>
<dl>
<dt><i>-n</i></p>
<dd>Don&#8217;t do anything, just show what we would do.</p>
<dt><i>-f</i></p>
<dd>Force removal of symlinks even if <code>/etc/init.d/</code><i>name</i> still exists.</dl>
<h2>Examples</h2>
<p>Insert links using the defaults: </p>
<pre><code> update-rc.d foobar defaults</code>
The equivalent dependency header would have start and stop
dependencies on $remote_fs and $syslog, and start in
runlevels 2-5 and stop in runlevels 0, 1 and 6.</pre>
<p>Equivalent command using explicit argument sets: </p>
<pre><code> update-rc.d foobar start 20 2 3 4 5 . stop 20 0 1 6 .</code></pre>
<p>More typical command using explicit argument sets: </p>
<pre><code> update-rc.d foobar start 30 2 3 4 5 . stop 70 0 1 6 .</code></pre>
<p>Insert links at default runlevels when B requires A </p>
<pre><code> update-rc.d script_for_A defaults 80 20</code>
<code> update-rc.d script_for_B defaults 90 10</code></pre>
<p>Insert a link to a service that (presumably) will not be needed by any other daemon </p>
<pre><code> update-rc.d top_level_app defaults 98 02</code></pre>
<p>Insert links for a script that requires services that start/stop at sequence number 20 </p>
<pre><code> update-rc.d script_depends_on_svc20 defaults 21 19</code></pre>
<p>Remove all links for a script (assuming foobar has been deleted already): </p>
<pre><code> update-rc.d foobar remove</code></pre>
<p>Example of disabling a service: </p>
<pre><code> update-rc.d -f foobar remove</code>
<code> update-rc.d foobar stop 20 2 3 4 5 .</code></pre>
<p>Example of a command for installing a system initialization-and-shutdown script: </p>
<pre><code> update-rc.d foobar start 45 S . stop 31 0 6 .</code></pre>
<p>Example of a command for disabling a system initialization-and-shutdown script: </p>
<pre><code> update-rc.d -f foobar remove</code>
<code> update-rc.d foobar stop 45 S .</code></pre>
<h2>Bugs</h2>
<p>See <a rel="nofollow" href="http://bugs.debian.org/sysv-rc.">http://bugs.debian.org/sysv-rc.</a></p>
<h2>Files</h2>
<dl>
<dt><code>/etc/init.d/</code></p>
<dd>The directory containing the actual init scripts.</p>
<dt><code>/etc/rc?.d/</code></p>
<dd>The directories containing the links used by <code>init</code> and managed by <code>update-rc.d</code>.</p>
<dt><code>/etc/init.d/skeleton</code></p>
<dd>Model for use by writers of <code>init.d</code> scripts.</dl>
<h2>See Also</h2>
<p><i>Debian Policy Manual</i>,<br />
 <code>/etc/init.d/skeleton</code>,<br />
 <code><a href="/docs/linux/man/8-insserv/">insserv</a></code>(8), <code><a href="/docs/linux/man/8-sysv-rc-conf/">sysv-rc-conf</a></code>(8), <code><a href="/docs/linux/man/8-bum/">bum</a></code>(8), <code><a href="/docs/linux/man/8-init/">init</a></code>(8). </p>
