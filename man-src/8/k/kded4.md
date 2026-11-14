---
title: "kded4(8)"
name: "kded4"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kded4/"
description: "kded4 – KDE daemon – triggers Sycoca database updates when needed."
---

<p>kded4 &#8211; KDE daemon &#8211; triggers Sycoca database updates when needed.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kded4</code> [&#8211;help] [Generic options] [Qt-options] [KDE-options] [&#8211;check]</dl>
<h2>Description</h2>
<p><code>kded4</code></p>
<dd>is responsible for creating the sycoca file, i.e. the binary cache of servicetypes, mimetypes, and services for a particular user. </p>
<p> It monitors the directories containing .desktop files. When a file is added/removed, it waits 5 seconds (in case of a series of updates), and then launches <code>kbuildsycoca4</code> to update the sycoca. </p>
<p> It checks newly installed update files, i.e. the *.upd files used to update configuration files of users when the configuration file formats changes. <code>kconf_update</code> is launched to do the updates. </p>
<p> When the hostname changes, it will make the necessary changes to the KDE environment and X-server to allow continued proper operation, launching <code>kdontchangethehostname</code> to do the changes. </p>
<p> Those tasks are also performed always at kded4 start to ensure that the user configuration is up to date. </p>
<p> It is also responsible for launching the on-demand kded4 modules and init enabled kded4 modules like: </p>
<p> <code>Konqueror Browser Preloader</code></p>
<dl>
<dd>Reduces Konqueror startup time.</dl>
<p> <code>Directory Watcher</code></p>
<dl>
<dd>Monitors directories for changes.</dl>
<p> <code>Hardware Detection</code></p>
<dl>
<dd>Provides a user interface for hardware events.</dl>
<p> <code>SSL Certificate Policy</code></p>
<dl>
<dd>Provides the user configured SSL certificate policy to applications.</dl>
<p> <code>Network Proxy Configuration</code></p>
<dl>
<dd>Automatic proxy configuration.</dl>
<p> <code>Password Caching</code></p>
<dl>
<dd>Temporary password caching, for example: so that a webpage with HTTP authentication doesn&#8217;t ask for your password for every link and every image in the page. These passwords are forgotten when exiting KDE (unlike <code>KWallet</code>)</dl>
<p> <code>Sound Policy</code></p>
<dl>
<dd>Provides the sound system policy to applications.</dl>
<p> <code>Favicons</code></p>
<dl>
<dd>Stores website icons.</dl>
<p> <code>Display Management</code></p>
<dl>
<dd>Manages displays and video outputs.</dl>
<p> <code>Cookie jar</code></p>
<dl>
<dd>Stores network cookies.</dl>
<p> <code>Network Watcher</code></p>
<dl>
<dd>Keeps track of the network and updates directory listings of the network:/ KIO slave.</dl>
<p> <code>Subversion Module</code></p>
<dl>
<dd>Provides various subversion actions to filemanager and other software.</dl>
<p> <code>Network Status</code></p>
<dl>
<dd>Tracks status of network interfaces and provides notifications for applications using the network.</dl>
<p> <code>Write Daemon</code></p>
<dl>
<dd>Watches the messages from local users sent with <i><a href="/docs/linux/man/1-write/">write</a></i>(1) or <i><a href="/docs/linux/man/1-wall/">wall</a></i>(1).</dl>
<p> <code>Notification area watcher</code></p>
<dl>
<dd>Keeps track of applications that want to use the D-Bus based notification area.</dl>
<p> <code>KMixD</code></p>
<dl>
<dd>KMixD Mixer Service</dl>
<p> <code>Systemtray daemon</code></p>
<dl>
<dd>Keeps track of applications that want to use the D-Bus based system tray.</dl>
<p> <code>Keyboard Daemon</code></p>
<dl>
<dd>Keeps track of keyboard changes (new keyboard, changed layout)</dl>
<p> <code>Remote URL Change Notifier</code></p>
<dl>
<dd>Provides change notifications for network folders</dl>
<p> <code>Activity Manager</code></p>
<dl>
<dd>The Nepomuk activities manager backend</dl>
<p> <code>Display Management change monitor</code></p>
<dl>
<dd>Notifies how the display has been rotated (where available)</dl>
<p> <code>Free Space Notifier</code></p>
<dl>
<dd>Warns when running out of space in your home folder.</dl>
<p> <code>Removable Device Automounter</code></p>
<dl>
<dd>Automatically mounts devices as needed.</dl>
<p> <code>Nepomuk Search Module</code></p>
<dl>
<dd>Helper module for KIO to ensure automatic updates of Nepomuk search listings.</dl>
<p> <code>Power Management</code></p>
<dl>
<dd>Battery, Display and CPU power management and notifications.</dl>
<p> <code>K Remote Control Daemon</code></p>
<dl>
<dd>Manages the Remote Control commands received</dl>
<p> <code>Status Notifier Manager</code></p>
<dl>
<dd>Manages services that provide status notifier user interfaces.</dl>
<p> <code>DNS-SD Service Discovery Monitor</code></p>
<dl>
<dd>Monitors the network for DNS-SD services.</dl>
<p> <code>Drive Ejector</code></p>
<dl>
<dd>Automatically unmounts and releases drives when their eject button is pushed.</dl>
<p> <code>Time zone</code></p>
<dl>
<dd>Provides access to the system&#8217;s time zones for applications.</dl>
<p> <code>Input Actions</code></p>
<dl>
<dd>Input Actions service performing configured actions on key presses.</dl>
<p> The init modules can be enabled/disabled using <code>systemsettings</code>, in System Administration &gt; Startup and Shutdown &gt; Service Manager.</p>
<h2>Generic Options</h2>
<p><code>&#8211;author</code></p>
<dl>
<dd>Show author information.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show help about options.</dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dd>Show all options.</dl>
<p> <code>&#8211;help-kde</code></p>
<dl>
<dd>Show KDE specific options.</dl>
<p> <code>&#8211;help-qt</code></p>
<dl>
<dd>Show Qt specific options.</dl>
<p> <code>&#8211;license</code></p>
<dl>
<dd>Show license information.</dl>
<p> <code>-v</code> <code>&#8211;version</code></p>
<dl>
<dd>Show version information</dl>
<h2>Application Options</h2>
<p><code>&#8211;check</code></p>
<dl>
<dd>Check Sycoca database only once.</dl>
<h2>Usage</h2>
<p>If <code>kded4</code> is called without parameters and is already running, it shows the message: </p>
<dl>
<dd>
<pre>KDE Daemon (kded) already running.</pre>
</dl>
<p> If <code>kded4</code> is called with <code>kded4 &#8211;check</code>, then it updates the KDE sycoca using <code>kbuildsycoca4</code>.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-kdeoptions/">kdeoptions</a></i>(7), <i><a href="/docs/linux/man/7-qtoptions/">qtoptions</a></i>(7), <i><a href="/docs/linux/man/8-kbuildsycoca4/">kbuildsycoca4</a></i>(8)</p>
<h2>Bugs</h2>
<p>There are probably tons of bugs. Use m[blue]<code>bugs.kde.org</code>m[]<font SIZE="-2">[1]</font> to report them.</p>
<h2>Authors</h2>
<p><code>David Faure</code> &lt;faure [at] kde.org&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Waldo Bastian</code> &lt;bastian [at] kde.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>bugs.kde.org</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dl>
