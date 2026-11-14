---
title: "tracker-miner-fs-cfg(5)"
name: "tracker-miner-fs-cfg"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tracker-miner-fs-cfg/"
description: "tracker-miner-fs.cfg"
---

<p>tracker-miner-fs.cfg</p>
<h2>Synopsis</h2>
<p>$HOME/.config/tracker/tracker-miner-fs.cfg </p>
<h2>Description</h2>
<p>Tracker&#8217;s configuration is built on top of GSettings, part of GLib. This means that there is a proper schema for configurations and they can be viewed (normally) using the <code>dconf-editor</code> tool. Tracker also allows switching from the GSettings database, used by most (cross) desktop applications, to a key/value formatted files (like Microsoft&#8217;s INI format). To do this, the environment variable <code>TRACKER_USE_CONFIG_FILES</code> must be defined before running the application using that configuration. So where is this configuration? Well, normally they&#8217;re stored in <i>$HOME/.config/tracker/</i>, however, default values are not stored to config files, only <code>different</code> values are. This man page describes what keys and values can be used. See EXAMPLES for a general overview. </p>
<h2>Options</h2>
<dl>
<dt><code>verbosity</code>=&#8217;errors&#8217;</p>
<dd>
<pre>Log verbosity.</pre>
<dt><code>initial-sleep</code>=15</p>
<dd>
<pre>Initial sleep time, in seconds.
Values range from 0 to 1000.</pre>
<dt><code>sched-idle</code>=&#8217;first-index&#8217;</p>
<dd>
<pre>The scheduler is the kernel component that decides which runnable application will be executed by the CPU next. Each application has an associated scheduling policy and priority.</pre>
<dt><code>throttle</code>=0</p>
<dd>
<pre>Indexing speed, the higher the slower.
Values range from 0 to 20.</pre>
<dt><code>low-disk-space-limit</code>=-1</p>
<dd>
<pre>Disk space threshold in percent at which to pause indexing, or -1 to disable.
Values range from -1 to 100.</pre>
<dt><code>crawling-interval</code>=-1</p>
<dd>
<pre>Interval in days to check whether the filesystem is up to date in the database. 0 forces crawling anytime, -1 forces it only after unclean shutdowns, and -2 disables it entirely.
Values range from -2 to 365.</pre>
<dt><code>removable-days-threshold</code>=3</p>
<dd>
<pre>Threshold in days after which files from removables devices will be removed from database if not mounted. 0 means never, maximum is 365.
Values range from 0 to 365.</pre>
<dt><code>enable-monitors</code>=true</p>
<dd>
<pre>Set to false to completely disable any file monitoring</pre>
<dt><code>enable-writeback</code>=true</p>
<dd>
<pre>Set to false to completely disable any file writeback</pre>
<dt><code>index-removable-devices</code>=false</p>
<dd>
<pre>Set to true to enable indexing mounted directories for removable devices.</pre>
<dt><code>index-optical-discs</code>=false</p>
<dd>
<pre>Set to true to enable indexing CDs, DVDs, and generally optical media (if removable devices are not indexed, optical discs won't be either)</pre>
<dt><code>index-on-battery</code>=true</p>
<dd>
<pre>Set to true to index while running on battery</pre>
<dt><code>index-on-battery-first-time</code>=true</p>
<dd>
<pre>Set to true to index while running on battery for the first time only</pre>
<dt><code>index-recursive-directories</code>=&#8217;&amp;DESKTOP&#8217;,&#8217;&amp;DOCUMENTS&#8217;,&#8217;&amp;DOWNLOAD&#8217;,&#8217;&amp;MUSIC&#8217;,&#8217;&amp;PICTURES&#8217;,&#8217;&amp;VIDEOS&#8217;</p>
<dd>
<pre>List of directories to index recursively, Special values include: &amp;DESKTOP, &amp;DOCUMENTS, &amp;DOWNLOAD, &amp;MUSIC, &amp;PICTURES, &amp;PUBLIC_SHARE, &amp;TEMPLATES, &amp;VIDEOS. See /etc/xdg/user-dirs.defaults and $HOME/.config/user-dirs.default</pre>
<dt><code>index-single-directories</code>=&#8217;$HOME&#8217;</p>
<dd>
<pre>List of directories to index without inspecting subfolders, Special values include: &amp;DESKTOP, &amp;DOCUMENTS, &amp;DOWNLOAD, &amp;MUSIC, &amp;PICTURES, &amp;PUBLIC_SHARE, &amp;TEMPLATES, &amp;VIDEOS. See /etc/xdg/user-dirs.defaults and $HOME/.config/user-dirs.default</pre>
<dt><code>ignored-files</code>=&#8217;*~&#8217;,&#8217;*.o&#8217;,&#8217;*.la&#8217;,&#8217;*.lo&#8217;,&#8217;*.loT&#8217;,&#8217;*.in&#8217;,&#8217;*.csproj&#8217;,&#8217;*.m4&#8242;,&#8217;*.rej&#8217;,&#8217;*.gmo&#8217;,&#8217;*.orig&#8217;,&#8217;*.pc&#8217;,&#8217;*.omf&#8217;,&#8217;*.aux&#8217;,&#8217;*.tmp&#8217;,&#8217;*.po&#8217;,&#8217;*.vmdk&#8217;,&#8217;*.vm*&#8217;,&#8217;*.nvram&#8217;,&#8217;*.part&#8217;,&#8217;*.rcore&#8217;,&#8217;*.lzo&#8217;,&#8217;autom4te&#8217;,&#8217;conftest&#8217;,&#8217;confstat&#8217;,&#8217;Makefile&#8217;,&#8217;SCCS&#8217;,&#8217;ltmain.sh&#8217;,&#8217;libtool&#8217;,&#8217;config.status&#8217;,&#8217;confdefs.h&#8217;,&#8217;configure&#8217;</p>
<dd>
<pre>List of file patterns to avoid</pre>
<dt><code>ignored-directories</code>=&#8217;po&#8217;,&#8217;CVS&#8217;,&#8217;core-dumps&#8217;,&#8217;lost+found&#8217;</p>
<dd>
<pre>List of directories to avoid</pre>
<dt><code>ignored-directories-with-content</code>=&#8217;.trackerignore&#8217;</p>
<dd>
<pre>Avoid any directory containing a file blacklisted here</pre>
</dl>
<h2>Examples</h2>
<p>The top level group is &quot;General&quot;. The default configuration (if saved to tracker-miner-fs.cfg), would look like: </p>
<pre><code>[General]
verbosity='errors';
initial-sleep=15;
sched-idle='first-index';
throttle=0;
low-disk-space-limit=-1;
crawling-interval=-1;
removable-days-threshold=3;
enable-monitors=true;
enable-writeback=true;
index-removable-devices=false;
index-optical-discs=false;
index-on-battery=true;
index-on-battery-first-time=true;
index-recursive-directories='&amp;DESKTOP','&amp;DOCUMENTS','&amp;DOWNLOAD','&amp;MUSIC','&amp;PICTURES','&amp;VIDEOS';
index-single-directories='$HOME';
ignored-files='*~','*.o','*.la','*.lo','*.loT','*.in','*.csproj','*.m4','*.rej','*.gmo','*.orig','*.pc','*.omf','*.aux','*.tmp','*.po','*.vmdk','*.vm*','*.nvram','*.part','*.rcore','*.lzo','autom4te','conftest','confstat','Makefile','SCCS','ltmain.sh','libtool','config.status','confdefs.h','configure';
ignored-directories='po','CVS','core-dumps','lost+found';
ignored-directories-with-content='.trackerignore';
</code></pre>
<h2>See Also</h2>
<p><code>tracker-miner-fsfg</code> </p>
