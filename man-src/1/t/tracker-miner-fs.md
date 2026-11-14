---
title: "tracker-miner-fs(1)"
name: "tracker-miner-fs"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-miner-fs/"
description: "tracker-miner-fs – Used to crawl the file system to mine data."
---

<h2 class="name">NAME</h2>
<p> tracker-miner-fs &#8211; Used to crawl the file system to mine data.</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker-miner-fs</code> [<i>OPTION</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>tracker-miner-fs</code> is not supposed to be run by the user since it is started by its .desktop file when the user logs in. It can also be started manually of course for debugging purposes. You can not run more than one instance of this at the same time. </p>
<p> <code>tracker-miner-fs</code> mines information about applications and files only. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Returns the version of this binary.</p>
<dt><code>-v, &#8211;verbosity={0|1|2|3}</code></p>
<dd> Sets the logging level, 0=errors, 1=minimal, 2=detailed, 3=debug.</p>
<dt><code>-s, &#8211;initial-sleep=SECONDS</code></p>
<dd> Sets the initial sleep time before crawling the file system is started. If the <code>&#8211;no-daemon</code> option is used, this option is ignored.</p>
<dt><code>-n, &#8211;no-daemon</code></p>
<dd> Tells the miner to exit once all indexing has finished and the database is up to date. This is not the default mode of operation for the miner, usually it stays around acting like a daemon to monitor file updates which may occur over time. This option renders the <code>&#8211;initial-sleep</code> option moot.</p>
<dt><code>-e, &#8211;eligible=FILE</code></p>
<dd> Checks if <code>FILE </code> is eligible for being mined based on the current configuration rules. In addition to this, it will check if <code>FILE</code> would be monitored for changes. This works with non-existing <code>FILE</code> arguments as well as existing <code>FILE</code> arguments. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_USE_LOG_FILES</code></p>
<dd> Don&#8217;t just log to stdout and stderr, but to log files too which are kept in $HOME/.local/share/tracker/. This came into effect in 0.15.3 and 0.16.0. After this version of Tracker, logging to file (usually useful for debugging) can only be done by declaring this environment variable.</p>
<dt><code>TRACKER_USE_CONFIG_FILES</code></p>
<dd> Don&#8217;t use GSettings, instead use a config file similar to how settings were saved in 0.10.x. That is, a file which is much like an .ini file. These are saved to $HOME/.config/tracker/ </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1). </p>
<h2>Index</h2>
