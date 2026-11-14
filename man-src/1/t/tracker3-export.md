---
title: "tracker3-export(1)"
name: "tracker3-export"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-export/"
description: "tracker3-export – Export all data from a Tracker database."
---

<h2 class="name">NAME</h2>
<p> tracker3-export &#8211; Export all data from a Tracker database. </p>
<h2>SYNOPSIS</h2>
<p> <code>tracker3 export</code> [<i>options</i>&#8230;] [<code>IRI</code>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>tracker3 export</code> exports data stored in a Tracker database, in Turtle format. By default all data is exported, if any <code>IRI</code>, only those resources will be printed. </p>
<p> The output is intended to be machine-readable, not human readable. Use a tool such as <a href="/docs/linux/man/1-rapper/">rapper</a>(1) to convert the data to different formats.</p>
<h2>OPTIONS</h2>
<p> <code>-g, &#8211;show-graphs</code></p>
<dl>
<dt>
<dd> Tracker can separate data into multiple graphs. This feature is used by the filesystem miner to separate different types of content. This flag causes the relevant GRAPH statements to be output along with the data. </p>
<dl>
<dt>
<dd>
<pre>
In this mode the output is TriG syntax rather than Turtle, due to
the extra GRAPH statements. Some tools which understand Turtle do not
understand TriG.
</pre>
</dl>
</dl>
<p> <code>&#8211;2to3</code></p>
<dl>
<dt>
<dd> Helper for migrating data from Tracker 2.x databases. This option takes an argument specifying the scope. Only the &#8220;files-starred&#8221; argument is available so far.</dl>
<p> <code>&#8211;keyfile</code></p>
<dl>
<dt>
<dd> Outputs the data in a key file format. Only may be used with &#8211;2to3</dl>
<h2>EXAMPLES</h2>
<p> Export all data from Tracker Index and prettify the output using <a href="/docs/linux/man/1-rapper/">rapper</a>(1).:: </p>
<dl>
<dt>
<dd>
<pre>
$ tracker3 export -b org.freedesktop.Tracker3.Miner.Files | rapper - -I . -i turtle -o turtle
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-import/">tracker3-import</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a></code>(1). </p>
<h2>Index</h2>
