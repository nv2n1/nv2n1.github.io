---
title: "dbmon-sh(8)"
name: "dbmon-sh"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dbmon-sh/"
description: "dbmon.sh – Directory Server script for monitoring database and entry cache usage"
---

<p>dbmon.sh &#8211; Directory Server script for monitoring database and entry cache usage</p>
<h2>Synopsis</h2>
<p>[INCR=num] [HOST=hostname] [PORT=num] [BINDDN=binddn] [BINDPW=password] [DBLIST=databases] [INDEXLIST=indexes] [VERBOSE=num] dbmon.sh</p>
<h2>Description</h2>
<p>dbmon.sh is a tool used to monitor database and entry cache usage. It is especially useful for database cache and entry/dn cache tuning &#8211; how much space is left, is the cache full, how much space on average do I need per entry/dn.</p>
<h2>Options</h2>
<p>It doesn&#8217;t take any command line arguments, so all options must be passed in as environment variables. </p>
<p> dbmon.sh will loop repeatedly showing the db information until it is killed or Ctrl-C </p>
<p> All arguments are optional, but you will most likely have to provide BINDPW </p>
<dl>
<dt><code>INCR</code> &#8211; show results every INCR seconds &#8211; default is 1 second</p>
<dd>
<dt><code>HOST</code> &#8211; name of host or IP address &#8211; default is localhost</p>
<dd>
<dt><code>PORT</code> &#8211; port number (LDAP not LDAPS) &#8211; default is 389</p>
<dd>
<dt><code>BINDDN</code> &#8211; DN to use to bind &#8211; must have permission to read everything under cn=config &#8211; default is cn=Directory Manager</p>
<dd>
<dt><code>BINDPW</code> &#8211; password for BINDDN &#8211; default is secret</p>
<dd>
<dt><code>DBLIST</code> &#8211; a list of databases you want to check &#8211; default is all; for more than one, delimit with spaces e.g. DBLIST=one two three</p>
<dd>
<dt><code>INDEXLIST</code> &#8211; a list of indexes to show for each named database &#8211; default is none; specify all for all indexes, or named e.g. INDEXLIST=id2entry entryrdn</p>
<dd>
<dt><code>VERBOSE</code> &#8211; output level &#8211; 0 == suitable for parsing by a script &#8211; 1 == has column headings &#8211; 2 == provides detailed descriptions of the data &#8211; default is 0</p>
<dd></dl>
<h2>Example</h2>
<p>INCR=1 HOST=ldap.example.com BINDDN=&quot;cn=directory manager&quot; BINDPW=&quot;secret&quot; VERBOSE=2 dbmon.sh </p>
<h2>Author</h2>
<p>dbmon.sh was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2014 Red Hat, Inc.</p>
