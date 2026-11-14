---
title: "kea-admin(8)"
name: "kea-admin"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kea-admin/"
description: "kea-admin – Shell script for managing Kea databases"
---

<p>kea-admin &#8211; Shell script for managing Kea databases</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kea-admin</code> [command] [backend] [<code>-u&nbsp;<wbr></code><i>database username</i>] [<code>-p&nbsp;<wbr></code><i>database password</i>] [<code>-n&nbsp;<wbr></code><i>database name</i>] [<code>-d&nbsp;<wbr></code><i>scripts directory</i>] [<code>-4 | -6</code>] [<code>-o&nbsp;<wbr></code><i>output file</i>]</dl>
<h2>Description</h2>
<dd>kea-admin is a shell script which offers database maintenance. In particular, it features database initialization, database version checking and database schema upgrade.</p>
<h2>Options</h2>
<p><i>command</i></p>
<dl>
<dd>Command to be issued to the servers. It can be one of the following: </p>
<p> lease-init</p>
<dl>
<dd>Initializes a new lease database. Useful during first Kea installation. The database is initialized to the latest version supported by the version of the software.</dl>
<p> lease-version</p>
<dl>
<dd>Reports lease database version. This is not necessarily equal to Kea version as each backend has its own versioning scheme.</dl>
<p> lease-upgrade</p>
<dl>
<dd>Conducts lease database upgrade. This is useful when migrating between old and new Kea versions.</dl>
<p> lease-dump</p>
<dl>
<dd>Dumps the contents of the lease database (MySQL and PostgreSQL backends) to text file. The content of the file consists of comma-separated-values (CSV) where each line in the file contains all of the values for a single lease. The first line of file is a header line containing the column names.</dl>
</dl>
<p> <i>backend</i></p>
<dl>
<dd>Specifies backend type. Currently allowed backends are: memfile, mysql and pgsql.</dl>
<p> <code>-u|&#8211;user </code><i>username</i></p>
<dl>
<dd>Specify the username when connecting to a database. If not specified, the default value of keatest is used.</dl>
<p> <code>-p|&#8211;password </code><i>password</i></p>
<dl>
<dd>Specifies the password when connecting to a database. If not specified, the default value of keatest is used.</dl>
<p> <code>-n|&#8211;name </code><i>database-name</i></p>
<dl>
<dd>Specifies the database name to connect to. If not specified, the default value of keatest is used.</dl>
<p> <code>-d|&#8211;directory </code><i>script-directory</i></p>
<dl>
<dd>Used for override scripts directory. That script is used during upgrades, database initialization and possibly other operations. If not specified, the default value of (prefix)/share/kea/scripts/ is used.</dl>
<p> <code>-o|&#8211;output </code><i>output_file</i></p>
<dl>
<dd>Required for lease-dump, Specifies the file to which the lease data will be dumped.</dl>
<p> <code>-4</code></p>
<dl>
<dd>Directs kea-admin to lease-dump the DHCPv4 leases. Incompatible with the -6 option.</dl>
<p> <code>-6</code></p>
<dl>
<dd>Directs kea-admin to lease-dump the DHCPv6 leases. Incompatible with the -4 option.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-keactrl/">keactrl</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp4/">kea-dhcp4</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp6/">kea-dhcp6</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp-ddns/">kea-dhcp-ddns</a></code>(8), <code><a href="/docs/linux/man/8-keactrl/">keactrl</a></code>(8), <code><a href="/docs/linux/man/8-perfdhcp/">perfdhcp</a></code>(8), Kea Administrator Guide.</p>
<h2>Author</h2>
<p>The Kea software has been written by a number of engineers working for ISC: Tomek Mrugalski, Stephen Morris, Marcin Siodelski, Thomas Markwalder, Francis Dupont, Jeremy C. Reed, Wlodek Wencel and Shawn Routhier. That list is roughly in the chronological order in which the authors made their first contribution. For a complete list of authors and contributors, see AUTHORS file.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2014-2016 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
