---
title: "tracker3-reset(1)"
name: "tracker3-reset"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-reset/"
description: "tracker3-reset – Reset the index and configuration"
---

<h2 class="name">NAME</h2>
<p> tracker3-reset &#8211; Reset the index and configuration </p>
<h2>SYNOPSIS</h2>
<p> <code>tracker3 reset</code> [&#8211;filesystem | &#8211;rss] [&#8211;file <i>FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> The reset command will change either your configuration or index irreversibly and should be used with care. Other than tags, actual data (e.g. files) should not be affected by this command. </p>
<p> The &quot;index&quot; is a link between your content (either locally or remotely) and how it can be found quickly using a number of different queries. Under the hood, this is done using a database. </p>
<p> Removing all data and starting again from the beginning with an empty data set (which is a common use of this command) is done by using the hard reset option. This behaves as if Tracker was just installed.</p>
<h2>OPTIONS</h2>
<p> <code>-s, &#8211;filesystem</code></p>
<dl>
<dt>
<dd> Removes data stored by <a href="/docs/linux/man/1-tracker-miner-fs/">tracker-miner-fs</a>(1). The miner will automatically recreate its cache from the filesystem when it restarts.</dl>
<p> <code>-r, &#8211;rss</code></p>
<dl>
<dt>
<dd> Removes data stored by <a href="/docs/linux/man/1-tracker-miner-rss/">tracker-miner-rss</a>(1).</dl>
<p> <code>-f, &#8211;file </code><i>FILE</i></p>
<dl>
<dt>
<dd> Resets all indexed information about <i>FILE</i>, works recursively for directories. Nothing will be done if <i>FILE</i> is not currently indexed. After deletion, a request to reindex this data will be immediately issued.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-daemon/">tracker3-daemon</a></code>(1). <code><a href="/docs/linux/man/1-tracker-miner-fs-3/">tracker-miner-fs-3</a></code>(1), <code><a href="/docs/linux/man/1-tracker-miner-rss-3/">tracker-miner-rss-3</a></code>(1). </p>
<h2>Index</h2>
