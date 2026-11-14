---
title: "makedbm(8)"
name: "makedbm"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makedbm/"
description: "makedbm – create or dump a ypserv database file"
---

<p>makedbm &#8211; create or dump a ypserv database file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/lib/yp/makedbm</code> [-a | -r] [-b] [-c] [-s] [-l] [-i&nbsp;<wbr><i>YP_INPUT_NAME</i>] [-o&nbsp;<wbr><i>YP_OUTPUT_NAME</i>] [-m&nbsp;<wbr><i>YP_MASTER_NAME</i>] <i>inputfile</i> <i>dbname</i></p>
<dt> <code>/usr/lib/yp/makedbm</code> -u&nbsp;<wbr><i>dbname</i></p>
<dt> <code>/usr/lib/yp/makedbm</code> -c</p>
<dt> <code>/usr/lib/yp/makedbm</code> &#8211;version</dl>
<h2>Description</h2>
<p><code>makedbm</code></p>
<dd>takes the inputfile and converts it to a ypserv database file. In the moment, GDBM is used as database. Each line of the input file is converted to a single record. All characters up to the first TAB or SPACE are the key, and the rest of the line is the data. <code>makedbm</code> does not treat `#&#8217; as a special character.</p>
<h2>Options</h2>
<p><code>-a</code></p>
<dl>
<dd>Special support for mail aliases. We couldn&#8217;t use sendmail for it, since sendmail uses db, but ypserv gdbm as database format.</dl>
<p> <code>-b</code></p>
<dl>
<dd>Insert the <code>YP_INTERDOMAIN</code> into the output. This key causes <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8) to use <code>DNS</code> for host name and address lookups for hosts not found in the maps.</dl>
<p> <code>-c</code></p>
<dl>
<dd>send a <code>YPPROC_CLEAR</code> to the local <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8). This causes ypserv to invalidate all cached entries.</dl>
<p> <code>-l</code></p>
<dl>
<dd>Convert the keys of the given map to lower case.</dl>
<p> <code>-i</code><i> YP_INPUT_NAME</i></p>
<dl>
<dd>Create a special entry with the key <code>YP_INPUT_NAME</code>.</dl>
<p> <code>-m</code><i> YP_MASTER_NAME</i></p>
<dl>
<dd>Create a special entry with the key <code>YP_MASTER_NAME</code>. If no master host name is specified, <code>YP_MASTER_NAME</code> will be set to the local host name.</dl>
<p> <code>-o</code><i> YP_OUTPUT_NAME</i></p>
<dl>
<dd>Create a special entry with the key <code>YP_OUTPUT_NAME</code>.</dl>
<p> <code>-r</code></p>
<dl>
<dd>Handle `#&#8217; as comment sign and remove the comment.</dl>
<p> <code>-s</code></p>
<dl>
<dd>Secure map. Accept connections from secure <code>NIS</code> networks only (reserved ports).</dl>
<p> <code>-u</code><i> dbname</i></p>
<dl>
<dd>Dump a ypserv database file. Prints out the file in text format, one entry per line, with a single space separating keys from values.</dl>
<p> <code>&#8211;no-limit-check</code></p>
<dl>
<dd>Don&#8217;t check for NIS key and data limit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8)</p>
<h2>Author</h2>
<p><code>makedbm</code> was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;.</p>
