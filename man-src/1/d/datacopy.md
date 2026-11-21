---

title: "datacopy(1)"
name: "datacopy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-datacopy/"
description: "datacopy – move table data between two servers"
---

<p> <code>datacopy</code> &#8211; move table data between two servers </p>
<h2>SYNOPSIS</h2>
<p> [-<code>vdE</code> ] Br o &#8211;<code>t</code> | &#8211;<code>a</code> | &#8211;<code>c</code> <i>owner</i> Br c [-<code>b </code><i>batchsize</i> ] [-<code>p </code><i>packetsize</i> ] [-<code>S </code><i>server/username/password/database/table_or_view</i> ] [-<code>D </code><i>server/username/password/database/table</i> ] [-<code>T </code><i>textsize</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a utility distributed with FreeTDS. will move table data from one server to another without the need for intermediate files. is much faster and more efficient than is freebcp out/in. </p>
<p> makes use of the db-lib bcp API built into FreeTDS. This API is also available to application developers. </p>
<p> can be used to migrate data between Sybase ASE and SQL Server or vice versa.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code></dt>
<dd> Truncate target table before loading data.</dd>
<dt><code>-a</code></dt>
<dd> Append data to target table.</dd>
<dt><code>-c </code><i>owner</i></dt>
<dd> Create the target table with the same schema as the source table. will submit a `CREATE&#8217; TABLE command on the target server using the specified owner in the command, e.g. `CREATE&#8217; TABLE owner.table (&#8230;).</dd>
<dt><code>-b </code><i>batchsize</i></dt>
<dd> The number of rows per batch of data copied. Each batch of data is effectively &#8216;committed&#8217; to the database. The default is 1000.</dd>
<dt><code>-p </code><i>packetsize</i></dt>
<dd> The number of bytes, per network packet, sent to and from the servers. Increased packet size can enhance performance.</dd>
<dt><code>-T </code><i>textsize</i></dt>
<dd> Specify size of TEXT/IMAGE column from network.</dd>
<dt><code>-v</code></dt>
<dd> Produce verbose output, including diagnostic timings.</dd>
<dt><code>-d</code></dt>
<dd> Produce freetds TDSDUMP output. (Serious debug only!)</dd>
<dt><code>-S </code><i>server/username/password/database/table_or_view</i></dt>
<dd> The connection information for the source server and the location/name of the table (or view) to be copied. If not specified, prompts the user for the information.</dd>
<dt><code>-D </code><i>server/username/password/database/table</i></dt>
<dd> The connection information for the destination server and the location/name of the target table. If not specified, prompts the user for the information.</dd>
<dt><code>-E</code></dt>
<dd> Keep identity values.</dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-freebcp/">freebcp</a>(1),Xrdefncopy1,Xrbsqldb1,Xrtsql1, <i>FreeTDS User Guide.</i></p>
<h2>HISTORY</h2>
<p> first appeared in FreeTDS 0.64.</p>
<h2>AUTHORS</h2>
<p>&nbsp;<wbr>The&nbsp;<wbr> utility was written by An Bill Thompson Aq thompbil [at] exchange.uk.ml.com . </p>
