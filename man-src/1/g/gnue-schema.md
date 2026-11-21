---

title: "gnue-schema(1)"
name: "gnue-schema"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnue-schema/"
description: "gnue-schema – gnue-schema"
---

<p> gnue-schema &#8211; gnue-schema</p>
<h2>SYNOPSIS</h2>
<p> <code>gnue-schema</code> [ <i>options</i> ] <i>file</i> <i>[,</i> <i>file,</i> <i>&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> Import GNUe Schema Definition files into a given connection </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>GENERAL OPTIONS</code></dt>
<dd>
</dd><dt>
</dt><dt><code>&#8211;connection &lt;connectionname&gt;, -c</code></dt>
<dd>
</dd><dd> Use the connection &lt;connectionname&gt; for creating the schema</dd>
<dt><code>&#8211;connections &lt;location&gt;</code></dt>
<dd> Specifies the location of the connection definition file. &lt;location&gt; may specify a file name (/usr/local/gnue/etc/connections.conf),or a URL location (<a rel="nofollow" href="http://localhost/connections.conf).If">http://localhost/connections.conf).If</a> this option is not specified, the environent variable GNUE_CONNECTIONS is checked. If neither of them is set, &quot;/home/reinhard/gnue/etc/connections. conf&quot; is used as a default.</dd>
<dt><code>&#8211;createdb, -d</code></dt>
<dd> If this option is set, the database will be created before any schema creation is done. There must be an owner or a username either from the given connection-configuration or from the command line. This user becomes the owner of the database and will be implicitly created.</dd>
<dt><code>&#8211;debug-file &lt;filename&gt;</code></dt>
<dd> Sends all debugging messages to a specified file (e.g., &quot;&#8211;debug-file trace.log&quot; sends all output to &quot;trace.log&quot;)</dd>
<dt><code>&#8211;debug-level &lt;level&gt;</code></dt>
<dd> Enables debugging messages. Argument specifies the level of messages to display (e.g., &quot;&#8211;debug-level 5&quot; displays all debugging messages at level 5 or below.)</dd>
<dt><code>&#8211;file-only, -f</code></dt>
<dd> If this flag is set, only code is sent to the output file and the schema is not created automatically.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Displays this help screen.</dd>
<dt><code>&#8211;help-config</code></dt>
<dd> Displays a list of valid configuration file entries, their purpose, and their default values.</dd>
<dt><code>&#8211;help-connections</code></dt>
<dd> Display help information related to database connections, including a list of available drivers.</dd>
<dt><code>&#8211;help-dev</code></dt>
<dd> Display all options of interest to core developers.</dd>
<dt><code>&#8211;mode &lt;both|schema|data&gt;, -m</code></dt>
<dd> Mode of operation. If mode is &#8216;schema&#8217;, only schema creation is done.<br />
&nbsp;<wbr>If mode is&nbsp;<wbr>&#8216;data&#8217;&nbsp;<wbr>only data integration is done.</dd>
<dt><code>&#8211;output &lt;filename&gt;, -o</code></dt>
<dd> Also send the code for creating the schema to this file.</dd>
<dt><code>&#8211;owner &lt;owner&gt;, -O</code></dt>
<dd> If the database is to be created this will be its owner.</dd>
<dt><code>&#8211;ownerpassword &lt;ownerpwd&gt;, -P</code></dt>
<dd> If the database is to be created this will be the password used for the database owner.</dd>
<dt><code>&#8211;password &lt;password&gt;, -p</code></dt>
<dd> Set the password to connect to the database.</dd>
<dt><code>&#8211;silent</code></dt>
<dd> Displays no output at all.</dd>
<dt><code>&#8211;username &lt;user&gt;, -u</code></dt>
<dd> Set the username to connect to the database. If the database is to be created and no owner (&#8211;owner) is specified, this username will be it&#8217;s owner.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Displays the version information for this program.</dd>
<dt><code>&#8211;yes, -y</code></dt>
<dd> If this option is set, the program runs in batch-mode, which means all questions are answered with &#8216;yes&#8217; automatically.</dd>
<dt><code>DEVELOPER OPTIONS</code></dt>
<dd>
</dd><dt>
</dt><dt><code>&#8211;debug-gc &lt;logfile&gt;, -g</code></dt>
<dd>
</dd><dd> Debug Python&#8217;s garbage collection on a SIGUSR1. If the argument is empty &#8216;garbage.log&#8217; will be used as logfile.</dd>
<dt><code>&#8211;debug-imports</code></dt>
<dd> All python imports are logged to stdout</dd>
<dt><code>&#8211;interactive-debugger</code></dt>
<dd> Run the app inside Python&#8217;s built-in debugger</dd>
<dt><code>&#8211;profile</code></dt>
<dd> Run Python&#8217;s built-in profiler and display the resulting run statistics.</dd>
<dt><code>&#8211;selfdoc &lt;type[,subtype]&gt;</code></dt>
<dd> Generates self-documentation.</dd>
<dt><code>&#8211;selfdoc-file &lt;filename&gt;</code></dt>
<dd> Specifies the filename that selfdoc should write to. If not provided,<br />
&nbsp;<wbr>output is sent to stdout.</dd>
<dt><code>&#8211;selfdoc-format &lt;format&gt;</code></dt>
<dd> Format to output the self-documentation in. Supported formats are dependent on the type of selfdoc being created.</dd>
<dt><code>&#8211;selfdoc-options &lt;options&gt;</code></dt>
<dd> Options specific to individual selfdoc types.</dd></dl>
<h2>AUTHOR</h2>
<p> GNU Enterprise Project &lt;info [at] gnue.org&gt;</p>
<h2>BUGS</h2>
<p> Please report any bugs to info [at] gnue.org. Include a complete, self-contained example that will allow the bug to be reproduced, and say which version of this tool you are using.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2007 Free Software Foundation, Inc. </p>
<p> gnue-schema is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> gnue-schema is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with gnue-schema; see the file COPYING. If not, write to the Free Software Foundation, 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA. </p>
