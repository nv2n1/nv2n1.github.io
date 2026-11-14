---
title: "tracker-miner-fs-3(1)"
name: "tracker-miner-fs-3"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-miner-fs-3/"
description: "tracker-miner-fs-3 – Used to crawl the file system to mine data."
---

<h2 class="name">NAME</h2>
<p> tracker-miner-fs-3 &#8211; Used to crawl the file system to mine data. </p>
<h2>SYNOPSIS</h2>
<p> <code>tracker-miner-fs-3</code> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>tracker-miner-fs-3</code> is not supposed to be run by the user since it is started by its .desktop file when the user logs in. It can also be started manually of course for debugging purposes. You can not run more than one instance of this at the same time. </p>
<p> <code>tracker-miner-fs-3</code> mines information about applications and files only.</p>
<h2>OPTIONS</h2>
<p> <code>-?, &#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
<dd> Returns the version of this binary.</dl>
<p> <code>-s, &#8211;initial-sleep=SECONDS</code></p>
<dl>
<dt>
<dd> Sets the initial sleep time before crawling the file system is started. If the <code>&#8211;no-daemon</code> option is used, this option is ignored.</dl>
<p> <code>-n, &#8211;no-daemon</code></p>
<dl>
<dt>
<dd> Tells the miner to exit once all indexing has finished and the database is up to date. This is not the default mode of operation for the miner, usually it stays around acting like a daemon to monitor file updates which may occur over time. This option renders the <code>&#8211;initial-sleep</code> option moot.</dl>
<p> <code>-e, &#8211;eligible=FILE</code></p>
<dl>
<dt>
<dd> Checks if <code>FILE</code> is eligible for being mined based on the current configuration rules. In addition to this, it will check if <code>FILE</code> would be monitored for changes. This works with non-existing <code>FILE</code> arguments as well as existing <code>FILE</code> arguments.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>G_MESSAGES_DEBUG</code></p>
<dl>
<dt>
<dd> Controls verbose log output from GLib-based code. Use G_MESSAGES_DEBUG=Tracker to see only Tracker-related logs, or G_MESSAGES_DEBUG=all to see everything.</dl>
<p> <code>TRACKER_DEBUG</code></p>
<dl>
<dt>
<dd> Enables more specialized debug output. Pass a comma-separated list of one or more keywords: </p>
<p> config</p>
<dl>
<dt>
<dd> miner configuration</dl>
<p> miner-fs-events</p>
<dl>
<dt>
<dd> internal processing of tracker-miner-fs</dl>
<p> monitors</p>
<dl>
<dt>
<dd> change events from filesystem monitors</dl>
<p> statistics</p>
<dl>
<dt>
<dd> show statistics about how many files were processed</dl>
<p> status</p>
<dl>
<dt>
<dd> log the status messages that are published over D-Bus</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-info/">tracker3-info</a></code>(1). </p>
<h2>Index</h2>
