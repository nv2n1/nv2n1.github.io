---
title: "pg_resetxlog(1)"
name: "pg_resetxlog"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_resetxlog/"
description: "pg_resetxlog – reset the write-ahead log and other control information of a PostgreSQL database cluster"
---

<h2 class="name">NAME</h2>
<p> pg_resetxlog &#8211; reset the write-ahead log and other control information of a PostgreSQL database cluster </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_resetxlog</code> [<code>-f</code>] [<code>-n</code>] [<code>-o</code>&nbsp;<wbr><i>oid</i>] [<code>-x</code>&nbsp;<wbr><i>xid</i>] [<code>-e</code>&nbsp;<wbr><i>xid_epoch</i>] [<code>-m</code>&nbsp;<wbr><i>mxid</i>] [<code>-O</code>&nbsp;<wbr><i>mxoff</i>] [<code>-l</code>&nbsp;<wbr><i>timelineid</i>,<i>fileid</i>,<i>seg</i>] <i>datadir</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>pg_resetxlog</code></p>
<dd>clears the write-ahead log (WAL) and optionally resets some other control information stored in the pg_control file. This function is sometimes needed if these files have become corrupted. It should be used only as a last resort, when the server will not start due to such corruption. </p>
<p> After running this command, it should be possible to start the server, but bear in mind that the database might contain inconsistent data due to partially-committed transactions. You should immediately dump your data, run <code>initdb</code>, and reload. After reload, check for inconsistencies and repair as needed. </p>
<p> This utility can only be run by the user who installed the server, because it requires read/write access to the data directory. For safety reasons, you must specify the data directory on the command line. <code>pg_resetxlog</code> does not use the environment variable <code>PGDATA</code>. </p>
<p> If <code>pg_resetxlog</code> complains that it cannot determine valid data for pg_control, you can force it to proceed anyway by specifying the <code>-f</code> (force) option. In this case plausible values will be substituted for the missing data. Most of the fields can be expected to match, but manual assistance might be needed for the next OID, next transaction ID and epoch, next multitransaction ID and offset, and WAL starting address fields. These fields can be set using the options discussed below. If you are not able to determine correct values for all these fields, <code>-f</code> can still be used, but the recovered database must be treated with even more suspicion than usual: an immediate dump and reload is imperative. <i>Do not</i> execute any data-modifying operations in the database before you dump, as any such action is likely to make the corruption worse. </p>
<p> The <code>-o</code>, <code>-x</code>, <code>-e</code>, <code>-m</code>, <code>-O</code>, and <code>-l</code> options allow the next OID, next transaction ID, next transaction ID&#8217;s epoch, next multitransaction ID, next multitransaction offset, and WAL starting address values to be set manually. These are only needed when <code>pg_resetxlog</code> is unable to determine appropriate values by reading pg_control. Safe values can be determined as follows: </p>
<dl>
<dt>
<dd> &bull; A safe value for the next transaction ID (<code>-x</code>) can be determined by looking for the numerically largest file name in the directory pg_clog under the data directory, adding one, and then multiplying by 1048576. Note that the file names are in hexadecimal. It is usually easiest to specify the option value in hexadecimal too. For example, if 0011 is the largest entry in pg_clog, -x 0x1200000 will work (five trailing zeroes provide the proper multiplier).</dl>
<dl>
<dt>
<dd> &bull; A safe value for the next multitransaction ID (<code>-m</code>) can be determined by looking for the numerically largest file name in the directory pg_multixact/offsets under the data directory, adding one, and then multiplying by 65536. As above, the file names are in hexadecimal, so the easiest way to do this is to specify the option value in hexadecimal and add four zeroes.</dl>
<dl>
<dt>
<dd> &bull; A safe value for the next multitransaction offset (<code>-O</code>) can be determined by looking for the numerically largest file name in the directory pg_multixact/members under the data directory, adding one, and then multiplying by 65536. As above, the file names are in hexadecimal, so the easiest way to do this is to specify the option value in hexadecimal and add four zeroes.</dl>
<dl>
<dt>
<dd> &bull; The WAL starting address (<code>-l</code>) should be larger than any WAL segment file name currently existing in the directory pg_xlog under the data directory. These names are also in hexadecimal and have three parts. The first part is the &#8220;timeline ID&#8221; and should usually be kept the same. Do not choose a value larger than 255 (0xFF) for the third part; instead increment the second part and reset the third part to 0. For example, if 00000001000000320000004A is the largest entry in pg_xlog, -l 0x1,0x32,0x4B will work; but if the largest entry is 000000010000003A000000FF, choose -l 0x1,0x3B,0x0 or more. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 <code>pg_resetxlog</code> itself looks at the files in pg_xlog and chooses a default <code>-l</code> setting beyond the last existing file name. Therefore, manual adjustment of <code>-l</code> should only be needed if you are aware of WAL segment files that are not currently present in pg_xlog, such as entries in an offline archive; or if the contents of pg_xlog have been lost entirely. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; There is no comparably easy way to determine a next OID that&#8217;s beyond the largest one in the database, but fortunately it is not critical to get the next-OID setting right.</dl>
<dl>
<dt>
<dd> &bull; The transaction ID epoch is not actually stored anywhere in the database except in the field that is set by <code>pg_resetxlog</code>, so any value will work so far as the database itself is concerned. You might need to adjust this value to ensure that replication systems such as Slony-I work correctly &#8212; if so, an appropriate value should be obtainable from the state of the downstream replicated database.</dl>
<p> The <code>-n</code> (no operation) option instructs <code>pg_resetxlog</code> to print the values reconstructed from pg_control and then exit without modifying anything. This is mainly a debugging tool, but can be useful as a sanity check before allowing <code>pg_resetxlog</code> to proceed for real. </p>
<p> The <code>-V</code> and <code>&#8211;version</code> options print the pg_resetxlog version and exit. The options <code>-?</code> and <code>&#8211;help</code> show supported arguments, and exit.</p>
<h2>NOTES</h2>
<p> This command must not be used when the server is running. <code>pg_resetxlog</code> will refuse to start up if it finds a server lock file in the data directory. If the server crashed then a lock file might have been left behind; in that case you can remove the lock file to allow <code>pg_resetxlog</code> to run. But before you do so, make doubly certain that there is no server process still alive. </p>
<h2>Index</h2>
