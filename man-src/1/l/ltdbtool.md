---
title: "ltdbtool(1)"
name: "ltdbtool"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ltdbtool/"
description: "ltdbtool – manipulate CTDB’s local TDB files"
---

<h2 class="name">NAME</h2>
<p> ltdbtool &#8211; manipulate CTDB&#8217;s local TDB files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ltdbtool</code> [<i>OPTION</i>&#8230;] {<i>COMMAND</i>} [<i>COMMAND-ARGS</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>ltdbtool is a utility to manipulate CTDB&#8217;s local TDB databases (LTDBs) without connecting to a CTDB daemon. </p>
<p> It can be used to: </p>
<dl>
<dt>
<dd> &bull; dump the contents of a LTDB, optionally printing the CTDB record header information,</dl>
<dl>
<dt>
<dd> &bull; convert between an LTDB and a non-clustered tdb by adding or removing CTDB headers and</dl>
<dl>
<dt>
<dd> &bull; convert between 64 and 32 bit LTDBs where the CTDB record headers differ by 4 bytes of padding.</dl>
<h2>OPTIONS</h2>
<p> -e</p>
<dl>
<dt>
<dd> Dump empty records. These are normally excluded.</dl>
<p> -p</p>
<dl>
<dt>
<dd> Dump with header information, similar to &quot;ctdb catdb&quot;.</dl>
<p> -s {0 | 32 | 64}</p>
<dl>
<dt>
<dd> Specify how to determine the CTDB record header size for the input database: </p>
<p> 0</p>
<dl>
<dt>
<dd> no CTDB header</dl>
<p> 32</p>
<dl>
<dt>
<dd> CTDB header size of a 32 bit system (20 bytes)</dl>
<p> 64</p>
<dl>
<dt>
<dd> CTDB header size of a 64 bit system (24 bytes)</dl>
<p> The default is 32 or 64 depending on the system architecture.</dl>
<p> -o {0 | 32 | 64}</p>
<dl>
<dt>
<dd> Specify how to determine the CTDB record header size for the output database, see -s.</dl>
<p> -S <i>SIZE</i></p>
<dl>
<dt>
<dd> Explicitly specify the CTDB record header SIZE of the input database in bytes.</dl>
<p> -O <i>SIZE</i></p>
<dl>
<dt>
<dd> Explicitly specify the CTDB record header SIZE for the output database in bytes.</dl>
<p> -h</p>
<dl>
<dt>
<dd> Print help text.</dl>
<h2>COMMANDS</h2>
<p> help</p>
<dl>
<dt>
<dd> Print help text.</dl>
<p> dump <i>IDB</i></p>
<dl>
<dt>
<dd> Dump the contents of an LTDB input file IDB to standard output in a human-readable format.</dl>
<p> convert <i>IDB</i> <i>ODB</i></p>
<dl>
<dt>
<dd> Copy an LTDB input file IDB to output file ODB, optionally adding or removing CTDB headers.</dl>
<h2>EXAMPLES</h2>
<p> Print a local tdb in &quot;tdbdump&quot; style: </p>
<dl>
<dt>
<dd>
<pre>
      ltdbtool dump idmap2.tdb.0
    
</pre>
</dl>
<p> Print a local tdb with header information similar to &quot;ctdb catdb&quot;: </p>
<dl>
<dt>
<dd>
<pre>
      ltdbtool dump -p idmap2.tdb.0
    
</pre>
</dl>
<p> Strip the CTDB headers from records: </p>
<dl>
<dt>
<dd>
<pre>
      ltdbtool convert -o0 idmap2.tdb.0 idmap.tdb
    
</pre>
</dl>
<p> Strip 64 bit CTDB headers from records, running on i386: </p>
<dl>
<dt>
<dd>
<pre>
      ltdbtool convert -s64 -o0 idmap2.tdb.0 idmap.tdb
    
</pre>
</dl>
<p> Strip the CTDB headers from records by piping through tdbrestore: </p>
<dl>
<dt>
<dd>
<pre>
      ltdbtool dump idmap2.tdb.0 | tdbrestore idmap.tdb
    
</pre>
</dl>
<p> Convert a local tdb from a 64 bit system for usage on a 32 bit system: </p>
<dl>
<dt>
<dd>
<pre>
      ltdbtool convert -s64 -o32 idmap2.tdb.0 idmap2.tdb.1
    
</pre>
</dl>
<p> Add a default header: </p>
<dl>
<dt>
<dd>
<pre>
      ltdbtool convert -s0 idmap.tdb idmap2.tdb.0
    
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1), <code><a href="/docs/linux/man/1-tdbdump/">tdbdump</a></code>(1), <code><a href="/docs/linux/man/1-tdbrestore/">tdbrestore</a></code>(1), <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> This documentation was written by Gregor Beck</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2011 Gregor Beck, Michael Adam </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[]. </p>
<h2>Index</h2>
