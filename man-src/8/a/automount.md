---
title: "automount(8)"
name: "automount"
section: "8"
letter: "a"
url: "/docs/linux/man/8-automount/"
description: "automount – manage autofs mount points"
---

<p>automount &#8211; manage autofs mount points</p>
<h2>Synopsis</h2>
<p><code>automount</code> [<i>options</i>] [<i>master_map</i>]</p>
<h2>Description</h2>
<p>The <code>automount</code> program is used to manage mount points for autofs, the inlined Linux automounter. <code>automount</code> works by reading the <code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5) map and sets up mount points for each entry in the master map allowing them to be automatically mounted when accessed. The file systems are then automatically umounted after a period of inactivity.</p>
<h2>Options</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd>Print brief help on program usage.</p>
<dt><i>-p, &#8211;pid-file</i></p>
<dd>Write the pid of the daemon to the specified file.</p>
<dt><i>-t &lt;seconds&gt;, &#8211;timeout &lt;seconds&gt;</i></p>
<dd>Set the global minimum timeout, in seconds, until directories are unmounted. The default is 10 minutes. Setting the timeout to zero disables umounts completely. The internal program default is 10 minutes, but the default installed configuration overrides this and sets the timeout to 5 minutes to be consistent with earlier autofs releases.</p>
<dt><i>-M &lt;seconds&gt;, &#8211;master-wait &lt;seconds&gt;</i></p>
<dd>Set the maximum time to wait for the master map to become available if it cannot be read at program start.</p>
<dt><i>-n &lt;seconds&gt;, &#8211;negative-timeout &lt;seconds&gt;</i></p>
<dd>Set the default timeout for caching failed key lookups. The default is 60 seconds.</p>
<dt><i>-v, &#8211;verbose</i></p>
<dd>Enables logging of general status and progress messages for all autofs managed mounts.</p>
<dt><i>-d, &#8211;debug</i></p>
<dd>Enables logging of general status and progress messages as well as debugging messages for all autofs managed mounts.</p>
<dt><i>-Dvariable=value, &#8211;define variable=value</i></p>
<dd>Define a global macro substitution variable. Global definitions are over-ridden macro definitions of the same name specified in mount entries.</p>
<dt><i>-f, &#8211;foreground</i></p>
<dd>Run the daemon in the foreground and log to stderr instead of syslog.&quot;</p>
<dt><i>-r, &#8211;random-multimount-selection</i></p>
<dd>Enables the use of ramdom selection when choosing a host from a list of replicated servers.</p>
<dt><i>-m, &#8211;dumpmaps [&lt;map type&gt; &lt;map name&gt;]</i></p>
<dd>With no parameters, list information about the configured automounter maps, then exit. </p>
<p> If the dumpmaps option is given and is followed by two parameters, &quot;&lt;map type&gt; &lt;map name&gt;&quot; then simple &quot;&lt;key, value&gt;&quot; pairs that would be read in by a map read are printed to stdout if the given map type and map name are found in the map configuration. </p>
<p> If the map is an LDAP map and there is more than one map of same name in different base dns only the first map encountered by autofs will be listed. Similarly, if the map is a file map and there is more than one map of the same name in different directories, only the first map encountered will be listed. </p>
<p> If the map type is an old style multi-map and any one of the map names in the multi-map entry matches the given map name the entries that would be used by autofs for the whole multi-map will be listed.</p>
<dt><i>-O, &#8211;global-options</i></p>
<dd>Allows the specification of global mount options used for all master map entries. These options will either replace or be appened to options given in a master map entry depending on the APPEND_OPTIONS configuration setting.</p>
<dt><i>-V, &#8211;version</i></p>
<dd>Display the version number, then exit.</p>
<dt><i>-l, &#8211;set-log-priority priority path [path,&#8230;]</i></p>
<dd>Set the daemon log priority to the specified value. Valid values include the numbers 0-7, or the strings emerg, alert, crit, err, warning, notice, info, or debug. Log level debug will log everything, log levels info, warn (or warning), or notice with enable the daemon verbose logging. Any other level will set basic logging. Note that enabling debug or verbose logging in the autofs global configuration will override dynamic log level changes. For example, if verbose logging is set in the configuration then attempting to set logging to basic logging, by using alert, crit, err or emerg won&#8217;t stop the verbose logging. However, setting logging to debug will lead to everything (debug logging) being logged witch can then also be disabled, returning the daemon to verbose logging. This option can be specified to change the logging priority of an already running automount process.</dl>
<p> The <i>path</i> argument corresponds to the automounted path name as specified in the master map.</p>
<dl>
<dt><i>-C, &#8211;dont-check-daemon</i></p>
<dd>Don&#8217;t check if the daemon is currently running (see NOTES).</p>
<dt><i>-F, &#8211;force</i></p>
<dd>Force an unlink umount of existing mounts under autofs managed mount points during startup. This can cause problems for processes with working directories within these mounts (see NOTES).</dl>
<h2>Arguments</h2>
<p><code>automount</code> takes one optional argument, the name of the master map to use.</p>
<dl>
<dt><code>master_map</code></p>
<dd>Location for autofs master map that defines autofs managed mount points and the mount maps they will use. The default is <code>auto.master</code>.</dl>
<h2>Notes</h2>
<p>If the <code>automount</code> daemon catches a USR1 signal, it will umount all currently unused autofs managed mounted file systems and continue running (forced expire). If it catches the TERM signal it will umount all unused autofs managed mounted file systems and exit if there are no remaining busy file systems. If autofs has been compiled with the option to ignore busy mounts on exit it will exit leaving any busy mounts in place otherwise busy file systems will not be umounted and autofs will not exit. Alternatively, if autofs has been compiled with the option to enable forced shutdown then a USR2 signal to the daemon will cause all mounts to be umounted and any busy mounts to be forcibly umounted, including autofs mount point directories (summary execution). Note that the forced umount is an unlink operation and the actual umount will not happen in the kernel until active file handles are released. The daemon also responds to a HUP signal which triggers an update of the maps for each mount point. </p>
<p> If any autofs mount point directories are busy when the daemon is sent an exit signal the daemon will not exit. The exception to this is if autofs has been built with configure options to either ignore busy mounts at exit or force umount at exit. If the ignore busy mounts at exit option is used the filesystems will be left in a catatonic (non-functional) state and can be manually umounted when they become unused. If the force umount at exit option is used the filesystems will be umounted but the mount will not be released by the kernel until they are no longer in use by the processes that held them busy. If automount managed filesystems are found mounted when autofs is started they will be recovered unless they are no longer present in the map in which case they need to umounted manually. </p>
<p> If the option to disable the check to see if the daemon is already running is used be aware that autofs currently may not function correctly for certain types of automount maps. The mounts of the seperate daemons might interfere with one another. The implications of running multiple daemon instances needs to be checked and tested before we can say this is supported. </p>
<p> If the option to force an unlink of mounts at startup is used then processes whose working directory is within unlinked automounted directories will not get the correct pwd from the system. This is because, after the mount is unlinked from the mount tree, anything that needs to walk back up the mount tree to construct a path, such as <a href="/docs/linux/man/2-getcwd/">getcwd</a>(2) and the proc filesystem /proc/&lt;pid&gt;/cwd, cannot work because the point from which the path is constructed has been detached from the mount tree.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5), <code><a href="/docs/linux/man/8-autofs/">autofs</a></code>(8), <code><a href="/docs/linux/man/5-autofs-conf/">autofs.conf</a></code>(5), <code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). <code><a href="/docs/linux/man/5-autofs_ldap_auth-conf/">autofs_ldap_auth.conf</a></code>(5)</p>
<h2>Bugs</h2>
<p>Don&#8217;t know, I&#8217;ve fixed everything I know about. </p>
<p> The documentation could be better. </p>
<p> Please report other bugs along with a detailed description to &lt;autofs [at] linux.kernel.org&gt;. For instructions on how to join the list and for archives visit <a rel="nofollow" href="http://linux.kernel.org/mailman/listinfo/autofs">http://linux.kernel.org/mailman/listinfo/autofs</a></p>
<h2>Author</h2>
<p>H. Peter Anvin &lt;hpa [at] transmeta.com&gt; and Ian Kent &lt;raven [at] themaw.net&gt;.</p>
