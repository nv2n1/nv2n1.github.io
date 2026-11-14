---
title: "rasqlinsert(1)"
name: "rasqlinsert"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasqlinsert/"
description: "rasqlinsert – write argus(8) data into mysql database tables."
---

<h2>NAME</h2>
<p> <code>rasqlinsert</code> &#8211; write <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data into mysql database tables.</p>
<h2>SYNOPSIS</h2>
<p> <code>rasqlinsert</code> [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Rasqlinsert</code> writes <code>argus</code> data into a mysql database. </p>
<p> The principal function of <code>rasqlinsert</code> is to insert and update flow data attributes, into a MySQL database table. Using the same syntax and strategies for all other ra* programs, <code>rasqlinsert</code> creates databases and database tables, based on the print specification on the either the command-line or the .rarc file. </p>
<p> The concept is that where a ra* program would print fields to standard out in ascii, <code>rasqlinsert</code> will insert those fields into the database as attributes. The flow key, as defined by the &quot;-m fields&quot; option, provides the definition of any keys that would be used in the schema. A &quot;-m none&quot; option, will remove the use of any DBMS keys for inserted data, and is the method to use when inserting streaming, unprocessed, primitive argus data into a database table. </p>
<p> The schema is important for database utility and performance. You can use MySQL querys against the attributes that you insert into the tables, such searching and sorting on IP addresses, time, packet counts, etc&#8230;. While <code>rasqlinsert</code> does not limit you to the number of attributes (columns) per record you provide, the RDBMS performance will quide you as to how many fields are useful. </p>
<p> <code>Rasqlinsert</code> by default, includes the actual binary argus &#8216;record&#8217; in the schema, and inserts and updates the binary record when needed. This enables a large number of fucnctions that extend beyond simple RDBMS schema&#8217;s that are useful. Adding the &#8216;record&#8217; is expensive, and some will elect to not use this feature. This can be controlled using the option &#8216;-s -record&#8217; as a print field option in the standard <code>ra.1</code> command line. When the &#8216;record&#8217; attribute is present, <code>rasql.1</code> can read the records directly from the database, to provide additional processing on the database table contents. </p>
<p> When keys are used, the database will enforce that any insertions meet the relaitional requirements, i.e. that the keys be unique. This requirement demands a sense of caching and key tracking, which <code>rasqlinsert</code> is specifically designed to provide. </p>
<p> <code>Rasqlinsert</code> by default, will append data to existing tables, without checking the schema for consistency. If your schema has keys, and you attempt to append new records to an existing table, there is a high likelyhood for error, as <code>rasqlinsert</code> will attempt to insert a record that collides with an existing flow key. Use the &quot;-M cache&quot; option to cause <code>rasqlinsert</code> to reference the table contents prior to aggregation and insertion. </p>
<p> The binary data <code>rasqlinsert</code> inserts by default, is read using <code>rasql</code>. </p>
<h2>RASQLINSERT SPECIFIC OPTIONS</h2>
<p> <code>Rasqlinsert</code>, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. <code><a href="/docs/linux/man/1-rasqlinsert/">Rasqlinsert</a>(1)</code> specific options are:</p>
<dl>
<dt><code>-M cache</code></p>
<dd> This causes <code>rasqlinsert</code> to use the database table as its persistent cache store. This mechanism is used to control memory use when dealing with large amounts of data and flow keys.</p>
<dt><code>-M drop</code></p>
<dd> This causes <code>rasqlinsert</code> to drop any pre-existing database table that has the same name as the target table name, on startup. </p>
</dl>
<h2>INVOCATION</h2>
<p> This invocation writes aggregated <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from the <i>file</i> into a database table. The standard 5-tuple fields, &#8216;saddr daddr proto sport dport&#8217; are used as keys for each entry. <code>rasqlinsert</code> will aggregate all the data prior to inserting the data into the database: </p>
<pre>
 
   <code>rasqlinsert</code> -r file -w <a href="mysql://user@localhost/db/table">mysql://user@localhost/db/table</a>
</pre>
<p> Because aggregation can require a lot of memory, <code>rasqlinsert</code> provides an option &#8216;-M cache&#8217; to have <code>rasqlinsert</code> use the database table as the persistent cache store for the aggregation. With this example, the standard 5-tuple fields, <code>rasqlinsert</code> will aggregate data over short spans of time as it reads the data from the file, and then commit the data to the database. If additional data arrives that matches that unique flow, <code>rasqlinsert</code> will fetch the entry from the database, aggregate, and then update the data entry in the database. </p>
<pre>
   <code>rasqlinsert</code> -M cache -r file -w <a href="mysql://user@localhost/db/table">mysql://user@localhost/db/table</a> 
 
</pre>
<p> <code>rasqlinsert</code> can provide the same function for streaming data read directly from an argus data source. This allows <code>rasqlinsert</code> to reassemble all status records for an individual flow, such that the resulting table has only a single entry for each communciation relationship seen. </p>
<pre>
  
   <code>rasqlinsert</code> -M cache -S argus -w <a href="mysql://user@localhost/db/table">mysql://user@localhost/db/table</a>
  
</pre>
<p> This invocation writes <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from the <i>file</i> into a database table, without aggregation, by specifying no relational key in the data. </p>
<pre>
  
   <code>rasqlinsert</code> -m none -r file -w <a href="mysql://user@localhost/db/table">mysql://user@localhost/db/table</a>
  
</pre>
<p> This invocation writes <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from the <i>stream</i> into a database table, without modification. </p>
<pre>
 
   <code>rasqlinsert</code> -m none -S argus -w <a href="mysql://user@localhost/db/table">mysql://user@localhost/db/table</a>
</pre>
<p> This invocation writes <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from the <i>stream</i> into a daily database table, without modification. <code>rasqlinsert</code> will generate table names based on time and insert its data relative to the timestamps found in the flow records it processes. In this specific example, &quot;-M time 1d&quot; specifies daily tables. </p>
<pre>
   <code>rasqlinsert</code> -m none -S argus -w <a href="mysql://user@localhost/db/table_%Y_%m_%d">mysql://user@localhost/db/table_%Y_%m_%d</a> -M time 1d
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rasql/">rasql</a>(1),</code> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>Index</h2>
