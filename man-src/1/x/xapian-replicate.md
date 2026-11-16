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
<dt><code>-h</code>, <code>&#8211;host</code>=<i>HOST</i></dt>
<dd> host to connect to (required)</dd>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></dt>
<dd> port to connect to (required)</dd>
<dt><code>-m</code>, <code>&#8211;master</code>=<i>DB</i></dt>
<dd> replicate database DB from the master (default: DATABASE)</dd>
<dt><code>-i</code>, <code>&#8211;interval</code>=<i>N</i></dt>
<dd> wait N seconds between each connection to the master (default: 60)</dd>
<dt><code>-r</code>, <code>&#8211;reader-time</code>=<i>N</i> wait N seconds to allow readers time to close before</dt>
<dd> applying repeated changesets (default: 30)</dd>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>N</i></dt>
<dd> set socket timeouts (if supported) to N seconds; N=0 for no timeout (default: 0)</dd>
<dt><code>-f</code>, <code>&#8211;force-copy</code></dt>
<dd> force a full copy of the database to be sent (and then replicate as normal)</dd>
<dt><code>-o</code>, <code>&#8211;one-shot</code></dt>
<dd> replicate only once and then exit</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> only report errors</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be more verbose</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit </dd>
</dl>
<h2>Index</h2>
