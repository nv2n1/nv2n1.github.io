---
title: "tracker-extract-cfg(5)"
name: "tracker-extract-cfg"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tracker-extract-cfg/"
description: "tracker-extract.cfg"
---

<p>tracker-extract.cfg</p>
<h2>Synopsis</h2>
<p>$HOME/.config/tracker/tracker-extract.cfg </p>
<h2>Description</h2>
<p>Tracker&#8217;s configuration is built on top of GSettings, part of GLib. This means that there is a proper schema for configurations and they can be viewed (normally) using the <code>dconf-editor</code> tool. Tracker also allows switching from the GSettings database, used by most (cross) desktop applications, to a key/value formatted files (like Microsoft&#8217;s INI format). To do this, the environment variable <code>TRACKER_USE_CONFIG_FILES</code> must be defined before running the application using that configuration. So where is this configuration? Well, normally they&#8217;re stored in <i>$HOME/.config/tracker/</i>, however, default values are not stored to config files, only <code>different</code> values are. This man page describes what keys and values can be used. See EXAMPLES for a general overview. </p>
<h2>Options</h2>
<dl>
<dt><code>verbosity</code>=&#8217;errors&#8217;</p>
<dd>
<pre>Log verbosity.</pre>
<dt><code>sched-idle</code>=&#8217;first-index&#8217;</p>
<dd>
<pre>The scheduler is the kernel component that decides which runnable application will be executed by the CPU next. Each application has an associated scheduling policy and priority.</pre>
<dt><code>max-bytes</code>=1048576</p>
<dd>
<pre>Maximum number of UTF-8 bytes to extract.
Values range from 0 to 10485760.</pre>
<dt><code>max-media-art-width</code>=0</p>
<dd>
<pre>Maximum width in pixels for any media art extracted. Anything bigger is resized. Set to -1 to disable saving media art from files. Setting to 0 sets no limit on the media art width.
Values range from -1 to 2048.</pre>
<dt><code>wait-for-miner-fs</code>=false</p>
<dd>
<pre>When true, tracker-extract will wait for tracker-miner-fs to be done crawling before extracting meta-data. This option is useful on constrained environment where it is important to list files as fast as possible and can wait to get meta-data later.</pre>
</dl>
<h2>Examples</h2>
<p>The top level group is &quot;General&quot;. The default configuration (if saved to tracker-extract.cfg), would look like: </p>
<pre><code>[General] verbosity = 'errors';
sched - idle = 'first-index';
max - bytes = 1048576;
max - media - art - width = 0;
    wait-for-miner-fs=false;
</code></pre>
<h2>See Also</h2>
<p><code>tracker-extractfg</code> </p>
