---
title: "tracker-reset(1)"
name: "tracker-reset"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-reset/"
description: "tracker-reset – Reset the index and configuration"
---

<h2 class="name">NAME</h2>
<p> tracker-reset &#8211; Reset the index and configuration</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker reset</code> [&#8211;hard | &#8211;soft] [&#8211;config] [&#8211;file <i>FILE</i>] </p>
<h2>DESCRIPTION</h2>
<p> The reset command will change either your configuration or index irreversibly and should be used with care. Other than tags, actual data (e.g. files) should not be affected by this command. </p>
<p> The &quot;index&quot; is a link between your content (either locally or remotely) and how it can be found quickly using a number of different queries. Under the hood, this is done using a database. </p>
<p> Removing all data and starting again from the beginning with an empty data set (which is a common use of this command) is done by using the hard reset option. This behaves as if Tracker was just installed. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r, &#8211;hard</code></p>
<dd> This kills all processes in the same way that <code>tracker daemon &#8211;kill</code> does but it also removes all databases. Restarting <code>tracker-store</code> re-creates the databases.</p>
<dt><code>-e, &#8211;soft</code></p>
<dd> A soft reset works exactly the same way that <code>&#8211;hard</code> does, with the exception that the backup and journal are not removed. These are restored when <code>tracker-store</code> is restarted. This command is useful if you have a corrupt database but want to reply the journal to restore it to the last known good place.</p>
<dt><code>-c, &#8211;config</code></p>
<dd> Resets all configuration to its defaults.</p>
<dt><code>-f, &#8211;file </code><i>FILE</i></p>
<dd> Resets all indexed information about <i>FILE</i>, works recursively for directories. Nothing will be done if <i>FILE</i> is not currently indexed. After deletion, a request to reindex this data will be immediately issued. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-daemon/">tracker-daemon</a></code>(1). <code><a href="/docs/linux/man/1-tracker/">tracker</a></code>(1). </p>
<h2>Index</h2>
