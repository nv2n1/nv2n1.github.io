---
title: "tracker-db-cfg(5)"
name: "tracker-db-cfg"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tracker-db-cfg/"
description: "tracker-db.cfg"
---

<p>tracker-db.cfg</p>
<h2>Synopsis</h2>
<p>$HOME/.config/tracker/tracker-db.cfg </p>
<h2>Description</h2>
<p>Tracker&#8217;s configuration is built on top of GSettings, part of GLib. This means that there is a proper schema for configurations and they can be viewed (normally) using the <code>dconf-editor</code> tool. Tracker also allows switching from the GSettings database, used by most (cross) desktop applications, to a key/value formatted files (like Microsoft&#8217;s INI format). To do this, the environment variable <code>TRACKER_USE_CONFIG_FILES</code> must be defined before running the application using that configuration. So where is this configuration? Well, normally they&#8217;re stored in <i>$HOME/.config/tracker/</i>, however, default values are not stored to config files, only <code>different</code> values are. This man page describes what keys and values can be used. See EXAMPLES for a general overview. </p>
<h2>Options</h2>
<dl>
<dt><code>journal-chunk-size</code>=50</p>
<dd>
<pre>Size of the journal at rotation in MB. Use -1 to disable rotating.</pre>
<dt><code>journal-rotate-destination</code>=&#8221;</p>
<dd>
<pre>Where to store a journal chunk when it hits the max size.</pre>
</dl>
<h2>Examples</h2>
<p>The top level group is &quot;General&quot;. The default configuration (if saved to tracker-db.cfg), would look like: </p>
<pre><code>[General]
journal-chunk-size=50;
journal-rotate-destination='';
</code></pre>
<h2>See Also</h2>
<p><code>tracker-dbfg</code> </p>
