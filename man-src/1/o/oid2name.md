---
title: "oid2name(1)"
name: "oid2name"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oid2name/"
description: "oid2name – resolve OIDs and file nodes in a PostgreSQL data directory"
---

<h2 class="name">NAME</h2>
<p> oid2name &#8211; resolve OIDs and file nodes in a PostgreSQL data directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>oid2name</code> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>oid2name is a utility program that helps administrators to examine the file structure used by PostgreSQL. To make use of it, you need to be familiar with the database file structure, which is described in Chapter 56, Database Physical Storage, in the documentation. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> The name &#8220;oid2name&#8221; is historical, and is actually rather misleading, since most of the time when you use it, you will really be concerned with tables&#8217; filenode numbers (which are the file names visible in the database directories). Be sure you understand the difference between table OIDs and table filenodes! </p>
</dl>
<p> oid2name connects to a target database and extracts OID, filenode, and/or table name information. You can also have it show database OIDs or tablespace OIDs.</p>
<h2>OPTIONS</h2>
<p> oid2name accepts the following command-line arguments: </p>
<p> <code>-f</code> <i>filenode</i></p>
<dl>
<dt>
<dd> show info for table with filenode <i>filenode</i></dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> include indexes and sequences in the listing</dl>
<p> <code>-o</code> <i>oid</i></p>
<dl>
<dt>
<dd> show info for table with OID <i>oid</i></dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> omit headers (useful for scripting)</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> show tablespace OIDs</dl>
<p> <code>-S</code></p>
<dl>
<dt>
<dd> include system objects (those in <code>information_schema</code>, <code>pg_toast</code> and <code>pg_catalog</code> schemas)</dl>
<p> <code>-t</code> <i>tablename_pattern</i></p>
<dl>
<dt>
<dd> show info for table(s) matching <i>tablename_pattern</i></dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the oid2name version and exit.</dl>
<p> <code>-x</code></p>
<dl>
<dt>
<dd> display more information about each object shown: tablespace name, schema name, and OID</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about oid2name command line arguments, and exit.</dl>
<p> oid2name also accepts the following command-line arguments for connection parameters: </p>
<p> <code>-d</code> <i>database</i></p>
<dl>
<dt>
<dd> database to connect to</dl>
<p> <code>-H</code> <i>host</i></p>
<dl>
<dt>
<dd> database server&#8217;s host</dl>
<p> <code>-p</code> <i>port</i></p>
<dl>
<dt>
<dd> database server&#8217;s port</dl>
<p> <code>-U</code> <i>username</i></p>
<dl>
<dt>
<dd> user name to connect as</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dt>
<dd> password (deprecated &#8212; putting this on the command line is a security hazard)</dl>
<p> To display specific tables, select which tables to show by using <code>-o</code>, <code>-f</code> and/or <code>-t</code>. <code>-o</code> takes an OID, <code>-f</code> takes a filenode, and <code>-t</code> takes a table name (actually, it&#8217;s a LIKE pattern, so you can use things like foo%). You can use as many of these options as you like, and the listing will include all objects matched by any of the options. But note that these options can only show objects in the database given by <code>-d</code>. </p>
<p> If you don&#8217;t give any of <code>-o</code>, <code>-f</code> or <code>-t</code>, but do give <code>-d</code>, it will list all tables in the database named by <code>-d</code>. In this mode, the <code>-S</code> and <code>-i</code> options control what gets listed. </p>
<p> If you don&#8217;t give <code>-d</code> either, it will show a listing of database OIDs. Alternatively you can give <code>-s</code> to get a tablespace listing.</p>
<h2>NOTES</h2>
<p> oid2name requires a running database server with non-corrupt system catalogs. It is therefore of only limited use for recovering from catastrophic database corruption situations.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
$ # what's in this database server, anyway?
$ oid2name
All databases:
    Oid  Database Name  Tablespace
----------------------------------
  17228       alvherre  pg_default
  17255     regression  pg_default
  17227      template0  pg_default
      1      template1  pg_default
$ oid2name -s
All tablespaces:
     Oid  Tablespace Name
-------------------------
    1663       pg_default
    1664        pg_global
  155151         fastdisk
  155152          bigdisk
$ # OK, let's look into database alvherre
$ cd $PGDATA/base/17228
$ # get top 10 db objects in the default tablespace, ordered by size
$ ls -lS * | head -10
-rw-------  1 alvherre alvherre 136536064 sep 14 09:51 155173
-rw-------  1 alvherre alvherre  17965056 sep 14 09:51 1155291
-rw-------  1 alvherre alvherre   1204224 sep 14 09:51 16717
-rw-------  1 alvherre alvherre    581632 sep  6 17:51 1255
-rw-------  1 alvherre alvherre    237568 sep 14 09:50 16674
-rw-------  1 alvherre alvherre    212992 sep 14 09:51 1249
-rw-------  1 alvherre alvherre    204800 sep 14 09:51 16684
-rw-------  1 alvherre alvherre    196608 sep 14 09:50 16700
-rw-------  1 alvherre alvherre    163840 sep 14 09:50 16699
-rw-------  1 alvherre alvherre    122880 sep  6 17:51 16751
$ # I wonder what file 155173 is ...
$ oid2name -d alvherre -f 155173
From database "alvherre":
  Filenode  Table Name
----------------------
    155173    accounts
$ # you can ask for more than one object
$ oid2name -d alvherre -f 155173 -f 1155291
From database "alvherre":
  Filenode     Table Name
-------------------------
    155173       accounts
   1155291  accounts_pkey
$ # you can mix the options, and get more details with -x
$ oid2name -d alvherre -t accounts -f 1155291 -x
From database "alvherre":
  Filenode     Table Name      Oid  Schema  Tablespace
------------------------------------------------------
    155173       accounts   155173  public  pg_default
   1155291  accounts_pkey  1155291  public  pg_default
$ # show disk space for every db object
$ du [0-9]* |
&gt; while read SIZE FILENODE
&gt; do
&gt;   echo "$SIZE       `oid2name -q -d alvherre -i -f $FILENODE`"
&gt; done
16            1155287  branches_pkey
16            1155289  tellers_pkey
17561            1155291  accounts_pkey
...
$ # same, but sort by size
$ du [0-9]* | sort -rn | while read SIZE FN
&gt; do
&gt;   echo "$SIZE   `oid2name -q -d alvherre -f $FN`"
&gt; done
133466             155173    accounts
17561            1155291  accounts_pkey
1177              16717  pg_proc_proname_args_nsp_index
...
$ # If you want to see what's in tablespaces, use the pg_tblspc directory
$ cd $PGDATA/pg_tblspc
$ oid2name -s
All tablespaces:
     Oid  Tablespace Name
-------------------------
    1663       pg_default
    1664        pg_global
  155151         fastdisk
  155152          bigdisk
$ # what databases have objects in tablespace "fastdisk"?
$ ls -d 155151/*
155151/17228/  155151/PG_VERSION
$ # Oh, what was database 17228 again?
$ oid2name
All databases:
    Oid  Database Name  Tablespace
----------------------------------
  17228       alvherre  pg_default
  17255     regression  pg_default
  17227      template0  pg_default
      1      template1  pg_default
$ # Let's see what objects does this database have in the tablespace.
$ cd 155151/17228
$ ls -l
total 0
-rw-------  1 postgres postgres 0 sep 13 23:20 155156
$ # OK, this is a pretty small table ... but which one is it?
$ oid2name -d alvherre -f 155156
From database "alvherre":
  Filenode  Table Name
----------------------
    155156         foo
</code></pre>
</dl>
<h2>AUTHOR</h2>
<p> B. Palmer &lt;bpalmer [at] crimelabs.net&gt; </p>
<h2>Index</h2>
