---
title: "preludedb-admin(1)"
name: "preludedb-admin"
section: "1"
letter: "p"
url: "/docs/linux/man/1-preludedb-admin/"
description: "preludedb-admin – tool to copy, move, delete, save or restore a prelude database"
---

<h2>NAME</h2>
<p> preludedb-admin &#8211; tool to copy, move, delete, save or restore a prelude database</p>
<h2>SYNOPSIS</h2>
<p> <code>preludedb-admin</code> <i>copy|move|delete|load|save</i> <i>arguments</i></p>
<h2>DESCRIPTION</h2>
<p> preludedb-admin can be used to copy, move, delete, save or restore a prelude database, partly or in whole, while preserving IDMEF data consistency. </p>
<p> Mandatory arguments</p>
<dl>
<dt><code>copy</code></p>
<dd> Make a copy of a Prelude database to another database.</p>
<dt><code>delete</code></p>
<dd> Delete content of a Prelude database.</p>
<dt><code>load</code></p>
<dd> Load a Prelude database from a file.</p>
<dt><code>move</code></p>
<dd> Move content of a Prelude database to another database.</p>
<dt><code>save</code></p>
<dd> Save a Prelude database to a file.</dl>
<p> Running a command without providing arguments will display a detailed help.</p>
<h2>EXAMPLES</h2>
<p> Obtaining help on a specific command: </p>
<dl>
<dt>
<dd>
<pre><code>
#preludedb - admin save
Usage : save&lt;alert | heartbeat&gt;&lt;database&gt;&lt;filename&gt;[options] Example : preludedb - admin save alert "type=mysql name=dbname user=prelude" outputfile
                                                                                       Save messages from&lt;database&gt;
                                                                                           into[filename]
                                                                                               .If no filename argument is provided,
    data will be written to standard output.Database arguments : type : Type of database(mysql / pgsql).name : Name of the database.user : User to access the database.pass : Password to access the database.Valid options : --offset&lt;offset&gt; : Skip processing until 'offset' events.--count&lt;count&gt; : Process at most count events.--query - logging[filename] : Log SQL query to the specified file.--criteria&lt;criteria&gt; : Only process events matching criteria.--events - per - transaction : Maximum number of event to process per transaction(default 1000).
</code></pre>
</dl>
<p> Preludedb-admin can be useful to delete events from a prelude database : </p>
<dl>
<dt>
<dd>
<pre>
preludedb-admin delete alert --criteria &lt;criteria&gt; &quot;type=&lt;mysql&gt; name=&lt;dbname&gt; user=&lt;prelude-user&gt; pass=&lt;pass&gt;&quot;
</pre>
</dl>
<p> where <i>criteria</i> is an IDMEF criteria : </p>
<dl>
<dt>
<dd>
<pre>
preludedb-admin delete alert --criteria &quot;alert.classification.text == 'UDP packet dropped'&quot; &quot;type=mysql name=prelude user=prelude-user pass=prelude-pass&quot;
</pre>
</dl>
<p> This will delete all event with the classification text &quot;UDP packet dropped&quot; from the database.</p>
<h2>SEE ALSO</h2>
<p> The Prelude Handbook: <i><a rel="nofollow" href="https://www.prelude-siem.org/projects/prelude/wiki/ManualUser">https://www.prelude-siem.org/projects/prelude/wiki/ManualUser</a></i> </p>
<p> Prelude homepage: <i><a rel="nofollow" href="http://www.prelude-siem.com/">http://www.prelude-siem.com/</a></i> </p>
<p> Creating filter using IDMEF Criteria: <i><a rel="nofollow" href="https://www.prelude-siem.org/projects/prelude/wiki/IDMEFCriteria">https://www.prelude-siem.org/projects/prelude/wiki/IDMEFCriteria</a></i> </p>
<p> Prelude IDMEF Path: <i><a rel="nofollow" href="https://www.prelude-siem.org/projects/prelude/wiki/IDMEFPath">https://www.prelude-siem.org/projects/prelude/wiki/IDMEFPath</a></i></p>
<h2>BUGS</h2>
<p> To report a bug, please visit <i><a rel="nofollow" href="https://www.prelude-siem.org/">https://www.prelude-siem.org/</a></i></p>
<h2>AUTHOR</h2>
<p> This manpage was Written by Pierre Chifflier.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2016 CS-SI.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
