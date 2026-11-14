---
title: "gtk-gnutella(1)"
name: "gtk-gnutella"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-gnutella/"
description: "gtk-gnutella – A Gnutella client for Gtk+"
---

<h2>NAME</h2>
<p> gtk-gnutella &#8211; A Gnutella client for Gtk+</p>
<h2>SYNOPSIS</h2>
<p> <code>gtk-gnutella</code></p>
<h2>DESCRIPTION</h2>
<p> <i>gtk-gnutella</i> is a GTK+ Gnutella client for Unix. It supports both searching and sharing with the 0.6 version of the Gnutella protocol and includes support for numerous protocol improvements and additions that have been added to the Gnutella network since. </p>
<p> The Gnutella network allows users to search for files and to advertise files shared locally, but is not handling file transfers which is done through HTTP. The addition of Gnutella-specific HTTP headers makes each Gnutella client a powerful file swarmer where even firewalled hosts can contribute. </p>
<p> Great care has been devoted into making <i>gtk-gnutella</i> powerful, efficient and reliable.</p>
<h2>OPTIONS</h2>
<p> All the options can be abbreviated as long as the supplied name is not ambiguous.</p>
<dl>
<dt><code>&#8211;cleanup</code></p>
<dd> For developers mostly: this requests a final memory cleanup sequence at exit time in an attempt to be able to spot memory leaks by looking at all the remaining allocated blocks, letting the developpers figuring out, perhaps, why they were not cleaned-up properly.</p>
<dt><code>&#8211;compile-info</code></p>
<dd> Tell <i>gtk-gnutella</i> to output a list of variables describing compile-time configuration information that was gathered when the program was built.</p>
<dt><code>&#8211;daemonize</code></p>
<dd> This options causes <i>gtk-gnutella</i> to become a daemon. It detaches from the terminal (if started from one) and forks itself into the background. It also changes it working directory to the root directory i.e., &quot;/&quot; so that it doesn&#8217;t block a mount point for example. This is mainly meant for headless mode but you can also use it if the Gtk+ GUI is enabled. </p>
<p> For example, if you do not start gtk-gnutella from a terminal but from a window manager menu, there&#8217;s little reason to not daemonize gtk-gnutella. Thus you might want to add the &#8211;daemonize option in this case. </p>
<p> Please note that when <i>gtk-gnutella</i> is started as a daemon all output which is normally send to the standard output and standard error output (usually your terminal or a common log file such as ~/.xsession-errors), is sent to /dev/null. The options <code>&#8211;log-stderr</code> and <code>&#8211;log-stdout</code> can be used to redirect log output in this case.</p>
<dt><code>&#8211;exec-on-crash </code><i>path</i></p>
<dd> Execute command specified in <i>path</i> when <i>gtk-gnutella</i> crashes.</p>
<dt><code>&#8211;geometry</code></p>
<dd> This option can be used to force the main window of the GUI to a certain location on your screen and/or give it certain dimensions. </p>
<p> For example, the following would position the window in the lower right corner with a width of 800 pixels and a height of 600 pixels: </p>
<p>&nbsp;<wbr>gtk-gnutella &#8211;geometry 800&#215;600-0-0 </p>
<p> Note that none of this can be guaranteed, your window manager has the last word on this. This option is a traditional command-line switch supported by most X11 applications.</p>
<dt><code>&#8211;minimized</code></p>
<dd> Launches <i>gtk-gnutella</i> with a minimized main window. Recommended when starting <i>gtk-gnutella in</i> the background on login.</p>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of all supported options.</p>
<dt><code>&#8211;log-stderr, &#8211;log-stdout</code></p>
<dd> These options allow you to log everything which is written to stderr respectively stdout to some files. A typical use would look like this: </p>
<p>gtk-gnutella &#8211;daemonize&nbsp;<wbr>&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;log-stderr&nbsp;<wbr>~/logs/gtkg.stderr&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;log-stdout&nbsp;<wbr>~/logs/gtkg.stdout </p>
<p> Redirecting these log messages also works without <code>&#8211;daemonize.</code> Of course, log files can become large and you might want to archive them or delete them periodically. After moving or deleting the log files, you can send <i>gtk-gnutella</i> a SIGHUP signal to create new log files.</p>
<dt><code>&#8211;log-supervise</code></p>
<dd> Redirects the logs for the supervisor process.</p>
<dt><code>&#8211;no-dbus</code></p>
<dd> Disable notifications of <i>gtk-gnutella</i> events to D-BUS.</p>
<dt><code>&#8211;no-restart</code></p>
<dd> Prevents <i>gtk-gnutella</i> from auto-restarting itself when crashing on a platform where core dumps are not possible or disabled.</p>
<dt><code>&#8211;no-supervise</code></p>
<dd> Prevents <i>gtk-gnutella</i> from starting a supervising process that will monitor the main process and automatically restart a new instance when the previous one exits abnormally.</p>
<dt><code>&#8211;no-xshm</code></p>
<dd> Disable MIT shared memory extension, when running with the X graphical user-interface.</p>
<dt><code>&#8211;pause-on-crash</code></p>
<dd> Pause the process on crash, so that a debugger may be attached to inspect the current state for instance.</p>
<dt><code>&#8211;ping</code></p>
<dd> This option allows you to check whether <i>gtk-gnutella</i> is currently running. This option returns with a success code when <i>gtk-gnutella</i> is already running, and with a failure code when it is not. </p>
<p> This allows you to use the following code to start <i>gtk-gnutella </i> from a cron job or window manager menu and avoid starting it twice: </p>
<p>&nbsp;<wbr>gtk-gnutella &#8211;ping || gtk-gnutella</p>
<dt><code>&#8211;restart-on-crash</code></p>
<dd> Asks <i>gtk-gnutella</i> to auto-restart itself after crashing on a platform where core dumps are allowed. </p>
<p> Regardless of core dumping options, <code>&#8211;no-restart</code> will always prevent a restart whilst <code>&#8211;restart-on-crash</code> will always request one if possible. It is not allowed to supply both options at the same time.</p>
<dt><code>&#8211;shell</code></p>
<dd> When this option is used to connect to an already running <i>gtk-gnutella</i> process over a local unix domain socket. This socket is located at &quot;$GTK_GNUTELLA_DIR/ipc/socket&quot;, thus normally &quot;~/.gtk-gnutella/ipc/socket&quot;. The socket is only accessible by the user running gtk-gnutella which is enforced by filesystem permissions. The socket is in a dedicated directory because apparently not all systems honor the access permissions on sockets as seen through the filesystem. </p>
<p> You can disable this feature by setting the property &quot;enable_local_socket&quot; to FALSE. It is recommendable to use this local socket whenever possible instead of the TCP socket to access the shell interface remotely. The reason is that the authentication token is passed non-encrypted over the network and everyone who can sniff the network is able to connect to the remote shell. This may not matter over the loopback interface or a LAN, but it&#8217;s a bad idea to use this over the Internet.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the user-agent string used on the Gnutella network which also holds the version information.</p>
<dt><code>&#8211;topless</code></p>
<dd> Starts gtk-gnutella without the graphical user-interface.</dl>
<h2>GETTING STARTED</h2>
<p> When <i>gtk-gnutella</i> is first started, it will attempt to connect to a well-known hosts server for some hosts to connect to. If you know a host you want to connect to, you can enter it in the box on the GnutellaNet tab and push the Add button. When first connecting to the gnutella network, it can take some time to establish a stable connection. Be patient.</p>
<h2>SEARCHING</h2>
<p> To search files just type your query in the search box at the top of the screen. All searches, both active and inactive, are shown in the sidebar. </p>
<p> You can have multiple searches running at once. To start another search while the first one is running, simply enter another search term into the edit box at the top of the window. </p>
<p> To stop a particular search and remove its tab from the search window, select the search by clicking on its tab and click the &quot;Close search&quot; button. If you want to clear the list for a particular search, but want to continue to see new files that are received for this search, click the &quot;Clear results&quot; button. </p>
<p> It is possible to apply filtering to search results using the filter editor. Click on &quot;Edit filters&quot; to access the editor. Use of the filtering editor goes beyond the scope of this man page, but there is a tutorial on this topic on the <i>gtk-gnutella</i> homepage. </p>
<p> When you find a file that you want to download, select the file in the list and click &quot;Download selected&quot;. This file will be placed in the download queue. On the downloads view you can watch the download progress of the file(s) you are downloading. </p>
<p> It is also possible to select a bunch of files for downloading at once. By holding down the control or shift keys while clicking files, you can select several files and then click &quot;Download selected&quot; to put them all in the download queue at once.</p>
<h2>CONFIGURATION</h2>
<p> Most of the configuration can be done via the &quot;Preferences&quot; window that can be accesed using the &quot;File -&gt; Preferences&quot; menu-option. You will find several tabs there, each tab regrouping common information. But some specific information pertaining to downloads or searches are directly available on the &quot;Downloads&quot; and &quot;Uploads&quot; panes. </p>
<p> If you linger your mouse over each configuration parameter, a tooltip window will popup explaining the meaning of that parameter. You may have to press &quot;Enter&quot; after a text input, or move the focus to another parameter to validate your entry. Items configured via spin buttons normally take effect immediately, unless you type text instead of using the spin buttons.</p>
<h2>FILES</h2>
<dl>
<dt><i>$GTK_GNUTELLA_DIR/config_gnet</i></p>
<dd>
<dl>
<dt>
<dd> Per-user configuration file, for core settings. This can be edited when the program is not running, but it is best to use the GUI to change configuration variables. <code>gtk-gnutella</code> saves this file every time the program is exited normally.</dl>
<dt><i>$GTK_GNUTELLA_DIR/config_gui</i></p>
<dd>
<dl>
<dt>
<dd> GUI configuration. It is best to not edit this file.</dl>
<dt><i>$GTK_GNUTELLA_DIR/dmesh</i></p>
<dd>
<dl>
<dt>
<dd> This is where the download mesh is persisted. You don&#8217;t need to worry about this.</dl>
<dt><i>$GTK_GNUTELLA_DIR/dmesh_ban</i></p>
<dd>
<dl>
<dt>
<dd> This is where temporarily banned download mesh entries are stored.</dl>
<dt><i>$GTK_GNUTELLA_DIR/done.namesize</i></p>
<dd>
<dl>
<dt>
<dd> This file holds the name and size of files completely downloaded by <code>gtk-gnutella</code> and which will now be ignored.</dl>
<dt><i>$GTK_GNUTELLA_DIR/done.sha1</i></p>
<dd>
<dl>
<dt>
<dd> This file holds the SHA1 of files completely downloaded by <code>gtk-gnutella</code> and which will now be ignored.</dl>
<dt><i>$GTK_GNUTELLA_DIR/downloads</i></p>
<dd>
<dl>
<dt>
<dd> This is where the download queue is persisted. Only the direct downloads (i.e. non-pushed) can be saved, since they don&#8217;t need routing information.</dl>
<dt><i>$GTK_GNUTELLA_DIR/hosts</i></p>
<dd>
<dl>
<dt>
<dd> This is the host cache. This is saved by <code>gtk-gnutella</code> on exit and should not be edited by hand.</dl>
<dt><i>$GTK_GNUTELLA_DIR/searches.xml</i></p>
<dd>
<dl>
<dt>
<dd> This is where the open searches and all the search filters are saved.</dl>
<dt><i>$GTK_GNUTELLA_DIR/sha1_cache</i></p>
<dd>
<dl>
<dt>
<dd> This is where the cache of all the computed SHA1 is stored.</dl>
<dt><i>$GTK_GNUTELLA_DIR/tth_cache</i></p>
<dd>
<dl>
<dt>
<dd> This is the directory under which all the computed TTH trees are stored. These files are binary data.</dl>
<dt><i>$GTK_GNUTELLA_DIR/upload_stats</i></p>
<dd>
<dl>
<dt>
<dd> This file keeps track of the upload statistics.</dl>
</dl>
<h2>ENVIRONMENT</h2>
<p> <i>gtk-gnutella</i> searches <code>GTK_GNUTELLA_DIR</code> for configuration files. If this variable is not set, <code>HOME</code> is used instead. If <code>HOME</code> is not set, then no configuration information will be saved when <i>gtk-gnutella</i> exits.</p>
<h2>MAILING LISTS</h2>
<p> There are a couple of mailing lists for <i>gtk-gnutella.</i> See <a rel="nofollow" href="http://sourceforge.net/mail/?group_id=4467">http://sourceforge.net/mail/?group_id=4467</a> for more info.</p>
<h2>BUGS</h2>
<p> <i>gtk-gnutella</i> is production-quality software, but still has minor bugs and incomplete or missing features. But which software doesn&#8217;t for its authors? </p>
<p> There are probably other missing features that should be listed here. </p>
<p> A list of known bugs might be available at the <i>gtk-gnutella</i> web site (see below.)</p>
<h2>SEE ALSO</h2>
<p> Additional information about gtk-gnutella and the latest version are available at <code><a rel="nofollow" href="http://gtk-gnutella.sourceforge.net/">http://gtk-gnutella.sourceforge.net/</a></code> </p>
<p> Additional information about gnutella is available at <code><a rel="nofollow" href="http://www.the\-gdf.org/">http://www.the\-gdf.org/</a></code> <code><a rel="nofollow" href="http://www.infoanarchy.org/en/Gnutella">http://www.infoanarchy.org/en/Gnutella</a></code> <code><a rel="nofollow" href="http://rfc\-gnutella.sourceforge.net/">http://rfc\-gnutella.sourceforge.net/</a></code></p>
<h2>AUTHORS</h2>
<p> Yann Grossel wrote the original <code>gtk-gnutella</code> which was running as a Gnutella 0.4 client in 2000. </p>
<p> Raphael Manfredi &lt;Raphael_Manfredi [at] pobox.com&gt; is the current maintainer and project leader (since version 0.14, released early September 2001).<br />
 For support, please contact the developer list, which can be reached at &lt;gtk-gnutella-devel [at] lists.sourceforge.net&gt;. </p>
<p> For a full list of contributors, open the &quot;About&quot; menu. </p>
<p> Brian St. Pierre &lt;bstpierre [at] bstpierre.org&gt; wrote the initial version of this manpage.</p>
<h2>COPYRIGHT</h2>
<p> <i>gtk-gnutella</i> is Copyright (c) 2000, Yann Grossel, with additional copyrights held by other contributors 2000-2014. </p>
<p> License to use and copy <i>gtk-gnutella</i> is given under the terms of the GNU General Public License (GPL), version 2. Please see the file COPYING in the distribution for complete information. </p>
<p> This manual page can also be redistributed under the same conditions as <i>gtk-gnutella</i> itself. </p>
<h2>Index</h2>
