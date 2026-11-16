---
title: "accessdb(8)"
name: "accessdb"
section: "8"
letter: "a"
url: "/docs/linux/man/8-accessdb/"
description: "accessdb – dumps the content of a man-db database in a human readable format"
---

<p>accessdb &#8211; dumps the content of a man-db database in a human readable format</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/accessdb</code> [<code>-d?V</code>] [<i>&lt;index-file&gt;</i>]</p>
<h2>Description</h2>
<p><code>accessdb</code> will output the data contained within a man-db database in a human readable form. By default, it will dump the data from <code>/var/cache/man/index.&lt;db-type&gt;,</code> where &lt;db-type&gt; is dependent on the database library in use. </p>
<p> Supplying an argument to accessdb will override this default.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd>Print debugging information.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd>Print a help message and exit.</dd>
<dt><code>&#8211;usage</code></dt>
<dd>Print a short usage message and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Display version information.</dd></dl>
<h2>Author</h2>
<pre>Wilf. (G.Wilford [at] ee.surrey.ac.uk).
Fabrizio Polacco (fpolacco [at] debian.org).
Colin Watson (cjwatson [at] debian.org).</pre>
<h2>Bugs</h2>
<p><a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
