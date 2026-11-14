---
title: "xapian-replicate(1)"
name: "xapian-replicate"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xapian-replicate/"
description: "xapian-replicate – Replicate a database from a master server to a local copy"
---

<h2>NAME</h2>
<p> xapian-replicate &#8211; Replicate a database from a master server to a local copy</p>
<h2>SYNOPSIS</h2>
<p> <code>xapian-replicate</code> [<i>OPTIONS</i>] <i>DATABASE</i></p>
<h2>DESCRIPTION</h2>
<p> xapian-replicate &#8211; Replicate a database from a master server to a local copy</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;host</code>=<i>HOST</i></p>
<dd> host to connect to (required)</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> port to connect to (required)</p>
<dt><code>-m</code>, <code>&#8211;master</code>=<i>DB</i></p>
<dd> replicate database DB from the master (default: DATABASE)</p>
<dt><code>-i</code>, <code>&#8211;interval</code>=<i>N</i></p>
<dd> wait N seconds between each connection to the master (default: 60)</p>
<dt><code>-r</code>, <code>&#8211;reader-time</code>=<i>N</i> wait N seconds to allow readers time to close before</p>
<dd> applying repeated changesets (default: 30)</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>N</i></p>
<dd> set socket timeouts (if supported) to N seconds; N=0 for no timeout (default: 0)</p>
<dt><code>-f</code>, <code>&#8211;force-copy</code></p>
<dd> force a full copy of the database to be sent (and then replicate as normal)</p>
<dt><code>-o</code>, <code>&#8211;one-shot</code></p>
<dd> replicate only once and then exit</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> only report errors</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be more verbose</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit </p>
</dl>
<h2>Index</h2>
