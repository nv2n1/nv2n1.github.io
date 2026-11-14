---
title: "kded5(8)"
name: "kded5"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kded5/"
description: "kded5 – KDE daemon – triggers Sycoca database updates when needed."
---

<p>kded5 &#8211; KDE daemon &#8211; triggers Sycoca database updates when needed.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kded5</code> [&#8211;check]</dl>
<h2>Description</h2>
<p><code>kded5</code></p>
<dd>consolidates several small services in one process. These are mostly D-Bus services provided by KDED modules, but it also manages sycoca (a binary cache of servicetypes, mimetypes and services used by KService) and KConfig update scripts as needed. </p>
<p> For sycoca, it monitors the directories containing .desktop files. When a file is added/removed, it waits 5 seconds (in case of a series of updates), and then launches <code>kbuildsycoca5</code> to update the sycoca. </p>
<p> For KConfig, it checks newly-installed update files, i.e. the *.upd files used to update configuration files of users when the configuration file formats changes, and runs the KConfig update utility to perform the updates. </p>
<p> Those tasks are also run when <code>kded5</code> is started to ensure that the user configuration is up to date. </p>
<p> You do not normally need to run <code>kded5</code> directly; Plasma desktop sessions run it automatically, and it is started on demand when an application attempts to use a D-Bus interface provided by it or one of its modules.</p>
<h2>Options</h2>
<p><code>&#8211;check</code></p>
<dl>
<dd>Check the sycoca database, updating it if necessary, and exit.</dl>
<h2>Configuration</h2>
<p><code>kded5</code> can be configured with the kded5rc ini-style configuration file. On Unix systems, this can be found at <i>$XDG_CONFIG_HOME</i>/kded5rc; if <i>$XDG_CONFIG_HOME</i> is not set, this defaults to ~/.config/kded5rc. </p>
<p> Configuration file entries are read on-demand, so changes can be made while <code>kded5</code> is running. However, all the current configuration options only really affect the startup behaviour of <code>kded5</code>. </p>
<p> The <code>[General]</code> section has the following options: </p>
<p> <code>CheckSycoca</code></p>
<dl>
<dd>Whether to update sycoca at startup (default: <code>true</code>).</dl>
<p> <code>CheckUpdates</code></p>
<dl>
<dd>Whether to perform outstanding KConfig updates at startup (default: <code>true</code>).</dl>
<p> <code>CheckFileStamps</code></p>
<dl>
<dd>Whether to check file timestamps when performing the initial sycoca update (default: <code>true</code>). See the documentation for <code>kbuildsycoca5</code> for more details.</dl>
<p> <code>DelayedCheck</code></p>
<dl>
<dd>Whether to delay the initial sycoca update until about a minute after starting (default: <code>false</code>).</dl>
<p> Each module also has a <code>[Module-</code><i>name</i><code>]</code> section in kded5rc, where <i>name</i> is the name of the module&#8217;s desktop file without the .desktop extension. This contains an <code>autoload</code> option that specifies whether the module should be automatically loaded when <code>kded5</code> is started (default: <code>false</code>). Note that this setting can also be changed via <code>kded5</code>&#8216;s D-Bus interface.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-kbuildsycoca5/">kbuildsycoca5</a></code>(8), <code><a href="/docs/linux/man/8-kdeinit5/">kdeinit5</a></code>(8)</p>
<h2>Bugs</h2>
<p>Please use m[blue]<code>KDE&#8217;s bugtracker</code>m[]<font SIZE="-2">[1]</font> to report bugs.</p>
<h2>Authors</h2>
<p><code>David Faure</code> &lt;faure [at] kde.org&gt;</p>
<dl>
<dd>Maintainer</dl>
<p> <code>Waldo Bastian</code> &lt;bastian [at] kde.org&gt;</p>
<dl>
<dd>Original author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>KDE&#8217;s bugtracker</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dl>
