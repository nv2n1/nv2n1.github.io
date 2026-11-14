---
title: "tracker-store(1)"
name: "tracker-store"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-store/"
description: "tracker-store – database indexer and query daemon"
---

<h2 class="name">NAME</h2>
<p> tracker-store &#8211; database indexer and query daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker-store</code> [<i>OPTION</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>tracker-store</code> provides both a powerful database daemon which allows clients to query or update their data using the highly descriptive <code>SPARQL</code> language. </p>
<p> <code>tracker-store</code> does not do any file crawling or any mining of data itself, instead other processes do that while <code>tracker-store</code> serves as a daemon waiting for such requests from application miners like <code>tracker-miner-fs.</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> A brief help message including some examples.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Returns the version of this binary.</p>
<dt><code>-v, &#8211;verbosity={0|1|2|3}</code></p>
<dd> Sets the logging level, 0=errors, 1=minimal, 2=detailed, 3=debug.</p>
<dt><code>-r, &#8211;force-reindex</code></p>
<dd> This forces tracker-store to remove databases and to recreate fresh databases ready for data insertion from the miners. For more information about the miners, see <code>tracker-miner-fs.</code></p>
<dt><code>-n, &#8211;readonly-mode</code></p>
<dd> This starts <code>tracker-store</code> in a mode which disables writing to the database. Only <code>SPARQL</code> read requests can be serviced if this option is used. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_DB_ONTOLOGIES_DIR</code></p>
<dd> This is the directory which tracker uses to load the .ontology files from. If unset it will default to the correct place. This is used mainly for testing purposes. </p>
<dt><code>TRACKER_LANGUAGE_STOP_WORDS_DIR</code></p>
<dd> This is the directory which tracker uses to load the stop words dictionaries from. If unset it will default to the correct place. This is used mainly for testing purposes. </p>
<dt><code>TRACKER_STORE_MAX_TASK_TIME</code></p>
<dd> This is maximum time allowed for a process to finish before interruption happens. The actual moment of interruption depends also on the frequency of checks. The value 0 indicates no interruption. This environment variable is used mainly for testing purposes. </p>
<dt><code>TRACKER_STORE_SELECT_CACHE_SIZE / TRACKER_STORE_UPDATE_CACHE_SIZE</code></p>
<dd> Tracker caches database statements which occur frequently to make subsequent repeat queries much faster. The cache size is set to 100 by default for each type (select and update queries). This must be at least 2 as a minimum, any less and a value of 3 is used instead. The number represents the number of cached statements to keep around. This environment variable is used mainly for testing purposes. </p>
<dt><code>TRACKER_USE_LOG_FILES</code></p>
<dd> Don&#8217;t just log to stdout and stderr, but to log files too which are kept in $HOME/.local/share/tracker/. This came into effect in 0.15.3 and 0.16.0. After this version of Tracker, logging to file (usually useful for debugging) can only be done by declaring this environment variable. </p>
<dt><code>TRACKER_USE_CONFIG_FILES</code></p>
<dd> Don&#8217;t use GSettings, instead use a config file similar to how settings were saved in 0.10.x. That is, a file which is much like an .ini file. These are saved to $HOME/.config/tracker/ </p>
</dl>
<h2>NOTES</h2>
<p> <code>tracker-store</code> is highly bound to the D-Bus freedesktop project. A D-Bus session is needed for all Tracker processes to communicate between each other. D-Bus is our acting IPC. See <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a>(1)</code> for more information. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-applet/">tracker-applet</a></code>(1), <code><a href="/docs/linux/man/1-tracker-search-tool/">tracker-search-tool</a></code>(1), <code><a href="/docs/linux/man/1-tracker-search/">tracker-search</a></code>(1), <code><a href="/docs/linux/man/1-tracker-tag/">tracker-tag</a></code>(1), <code><a href="/docs/linux/man/1-tracker-stats/">tracker-stats</a></code>(1), <code><a href="/docs/linux/man/1-tracker-services/">tracker-services</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1), <code><a href="/docs/linux/man/1-tracker-control/">tracker-control</a></code>(1), </p>
<p> <code><a rel="nofollow" href="http://www.w3.org/TR/rdf-sparql-query/">http://www.w3.org/TR/rdf-sparql-query/</a></code> </p>
<p> <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), </p>
<p> <code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/dbus">http://www.freedesktop.org/wiki/Software/dbus</a></code> </p>
<h2>Index</h2>
