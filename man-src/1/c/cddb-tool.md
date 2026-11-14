---
title: "cddb-tool(1)"
name: "cddb-tool"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cddb-tool/"
description: "cddb-tool – Get CDDB information"
---

<h2>NAME</h2>
<p> cddb-tool &#8211; Get CDDB information</p>
<h2>SYNOPSIS</h2>
<p> <code>cddb-tool parse </code> <i>file [-i|-d|-a|-t] [num|-c|-p]</i> </p>
<p> <code>cddb-tool template disc-id tracks</code> </p>
<p> <code>cddb-tool send</code> <i>[file] address</i> </p>
<p> <code>cddb-tool query</code> <i>server user host disc-id tracks</i> </p>
<p> <code>cddb-tool read</code> <i>server user host disc-id genre</i> </p>
<p> <code>cddb-tool help</code> </p>
<h2>DESCRIPTION</h2>
<p> cddb-tool is a backend tool for abcde. It is passed information from cd-discid and uses it look up the CD title, artist, and track information on the cddb database (<a rel="nofollow" href="http://freedb.freedb.org)">http://freedb.freedb.org)</a> on the internet.</p>
<h2>COMMANDS</h2>
<p> <code>parse</code> <i>[file] option</i> </p>
<p> Get data out of a cddb file (use &quot;-&quot; for stdin). Options (use one and only one):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>id</code></p>
<dd> prints disc id</p>
<dt><code>album</code></p>
<dd> prints album title</p>
<dt><code>track num</code></p>
<dd> prints title of track num</p>
<dt><code>artist</code></p>
<dd> prints artist</p>
<dt><code>category</code></p>
<dd> prints category</p>
<dt><code>cddbgenre</code></p>
<dd> synonym for category</p>
<dt><code>all</code></p>
<dd> parse file and dumps to stdout in a form sourceable by the shell</dl>
</dl>
<p> <code>send</code> <i>[file] address</i> </p>
<p> Mails file file (or stdin of no file specified) to specified address, using correct format. Category should be one of blues, classical, country, data, folk, jazz, newage, reggae, rock, soundtrack, misc. </p>
<p> <code>template</code> <i>[disc-id] [tracks]</i> </p>
<p> Generates a template (empty) cddb file to stdout. The command line should be essentially the output of cd-discid. </p>
<p> <code>query</code> <i>[server] [user] [host] [disc-id] [tracks]</i> </p>
<p> Looks up disc on server (should be of form &quot;<a rel="nofollow" href="http://host/cddb/cddb.cgi">http://host/cddb/cddb.cgi</a>&quot;) remainder of command line is in the same form as that returned by the cd-discid program. Uses wget, so if you need to use a proxy then just configure wget to do so. user and host will be used for identifying ourselves to the CDDB server. Outputs response code and entries with matching CDDB entries, if successful, from the CDDB server. </p>
<p> <code>read</code> <i>[server] [user] [host] [disc-id] [genre]</i> </p>
<p> Dumps CDDB entry to stdout. File will contain an extra #CATEGORY= line, which leaves it a valid CDDB file but which will be recognized by parse and send commands. Uses wget, so if you need to use a proxy then just configure wget to do so. user and host will be used for identifying ourselves to the CDDB server. </p>
<p> <code>help</code> </p>
<p> Prints usage information. </p>
<h2>AUTHOR</h2>
<p> Nathaniel Smith &lt;njs [at] uclink4.berkeley.edu&gt;, maintained as part of abcde by Robert Woodcock &lt;rcw [at] debian.org&gt;. Manual page compiled from help information by Robert Woodcock. </p>
<h2>Index</h2>
