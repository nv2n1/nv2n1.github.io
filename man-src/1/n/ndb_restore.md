---
title: "ndb_restore(1)"
name: "ndb_restore"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_restore/"
description: "ndb_restore – restore a MySQL Cluster backup"
---

<h2 class="name">NAME</h2>
<p> ndb_restore &#8211; restore a MySQL Cluster backup </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_restore </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<dd>The cluster restoration program is implemented as a separate command-line utility <code>ndb_restore</code>, which can normally be found in the MySQL bin directory. This program reads the files created as a result of the backup and inserts the stored information into the database. </p>
<p> <code>ndb_restore</code> must be executed once for each of the backup files that were created by the START BACKUP command used to create the backup (see Section 17.5.3.2, lqUsing The MySQL Cluster Management Client to Create a Backuprq). This is equal to the number of data nodes in the cluster at the time that the backup was created. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Before using <code>ndb_restore</code>, it is recommended that the cluster be running in single user mode, unless you are restoring multiple data nodes in parallel. See Section 17.5.6, lqMySQL Cluster Single User Moderq, for more information about single user mode. </p>
</dl>
<p> The following table includes options that are specific to the MySQL Cluster native backup restoration program <code>ndb_restore</code>. Additional descriptions follow the table. For options common to all MySQL Cluster programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq. </p>
<p> Typical options for this utility are shown here: </p>
<dl>
<dt>
<dd>
<pre><code>
ndb_restore[-c connectstring] - n node_id[-m] - b backup_id - r-- backup_path = / path / to / backup / files
</code></pre>
</dl>
<p> The <code>-c</code> option is used to specify a connectstring which tells ndb_restore where to locate the cluster management server. (See Section 17.3.2.3, lqThe MySQL Cluster Connectstringrq, for information on connectstrings.) If this option is not used, then <code>ndb_restore</code> attempts to connect to a management server on localhost:1186. This utility acts as a cluster API node, and so requires a free connection lqslotrq to connect to the cluster management server. This means that there must be at least one [api] or [mysqld] section that can be used by it in the cluster config.ini file. It is a good idea to keep at least one empty [api] or [mysqld] section in config.ini that is not being used for a MySQL server or other application for this reason (see Section 17.3.2.7, lqDefining SQL and Other API Nodes in a MySQL Clusterrq). </p>
<p> You can verify that <code>ndb_restore</code> is connected to the cluster by using the <code>SHOW</code> command in the <code>ndb_mgm</code> management client. You can also accomplish this from a system shell, as shown here: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ndb_mgm -e &quot;SHOW&quot;</code>
</pre>
</dl>
<p> <code>-n</code> is used to specify the node ID of the data node on which the backups were taken. </p>
<p> The first time you run the <code>ndb_restore</code> restoration program, you also need to restore the metadata. In other words, you must re-create the database tables &#8212; this can be done by running it with the <code>-m</code> option. Note that the cluster should have an empty database when starting to restore a backup. (In other words, you should start <code>ndbd</code> with <code>&#8211;initial</code> prior to performing the restore. You should also remove manually any Disk Data files present in the data node&#8217;s DataDir.) </p>
<p> It is possible to restore data without restoring table metadata. Prior to MySQL 5.1.17, <code>ndb_restore</code> did not perform any checks of table schemas; if a table was altered between the time the backup was taken and when <code>ndb_restore</code> was run, <code>ndb_restore</code> would still attempt to restore the data to the altered table. </p>
<p> Beginning with MySQL 5.1.17, the default behavior is for <code>ndb_restore</code> to fail with an error if table data do not match the table schema; this can be overridden using the <code>&#8211;skip-table-check</code> or <code>-s</code> option. Prior to MySQL 5.1.21, if this option is used, then <code>ndb_restore</code> attempts to fit data into the existing table schema, but the result of restoring a backup to a table schema that does not match the original is unspecified. </p>
<p> Beginning with MySQL Cluster NDB 6.3.8, <code>ndb_restore</code> supports limited attribute promotion in much the same way that it is supported by MySQL replication; that is, data backed up from a column of a given type can generally be restored to a column using a lqlarger, similarrq type. For example, data from a CHAR(20) column can be restored to a column declared as VARCHAR(20), VARCHAR(30), or CHAR(30); data from a MEDIUMINT column can be restored to a column of type INT or BIGINT. See Section 16.4.1.6.2, lqReplication of Columns Having Different Data Typesrq, for a table of type conversions currently supported by attribute promotion. </p>
<p> Attribute promotion by <code>ndb_restore</code> must be enabled explicitly, as follows: </p>
<dl>
<dt>
<dd> 1. Prepare the table to which the backup is to be restored. <code>ndb_restore</code> cannot be used to re-create the table with a different definition from the original; this means that you must either create the table manually, or alter the columns which you wish to promote using ALTER TABLE after restoring the table metadata but before restoring the data.</dl>
<dl>
<dt>
<dd> 2. Invoke <code>ndb_restore</code> with the <code>&#8211;promote-attributes</code> option (short form <code>-A</code>) when restoring the table data. Attribute promotion does not occur if this option is not used; instead, the restore operation fails with an error.</dl>
<p> In addition to <code>&#8211;promote-attributes</code>, a <code>&#8211;preserve-trailing-spaces</code> option is also available for use with <code>ndb_restore</code> beginning with MySQL Cluster NDB 6.3.8. This option (short form <code>-R</code>) causes trailing spaces to be preserved when promoting a CHAR column to VARCHAR or a BINARY column to VARBINARY. Otherwise, any trailing spaces are dropped from column values when they are inserted into the new columns. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Although you can promote CHAR columns to VARCHAR and BINARY columns to VARBINARY, you cannot promote VARCHAR columns to CHAR or VARBINARY columns to BINARY. </p>
</dl>
<p> The <code>-b</code> option is used to specify the ID or sequence number of the backup, and is the same number shown by the management client in the Backup <i>backup_id</i> completed message displayed upon completion of a backup. (See Section 17.5.3.2, lqUsing The MySQL Cluster Management Client to Create a Backuprq.) </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> When restoring cluster backups, you must be sure to restore all data nodes from backups having the same backup ID. Using files from different backups will at best result in restoring the cluster to an inconsistent state, and may fail altogether. </p>
</dl>
<p> <code>&#8211;restore_epoch</code> (short form: <code>-e</code>) adds (or restores) epoch information to the cluster replication status table. This is useful for starting replication on a MySQL Cluster replication slave. When this option is used, the row in the mysql.ndb_apply_status having 0 in the id column is updated if it already exists; such a row is inserted if it does not already exist. (See Section 17.6.9, lqMySQL Cluster Backups With MySQL Cluster Replicationrq.) </p>
<p> The path to the backup directory is required; this is supplied to <code>ndb_restore</code> using the <code>&#8211;backup_path</code> option, and must include the subdirectory corresponding to the ID backup of the backup to be restored. For example, if the data node&#8217;s DataDir is /var/lib/mysql-cluster, then the backup directory is /var/lib/mysql-cluster/BACKUP, and the backup files for the backup with the ID 3 can be found in /var/lib/mysql-cluster/BACKUP/BACKUP-3. The path may be absolute or relative to the directory in which the <code>ndb_restore</code> executable is located, and may be optionally prefixed with <code>backup_path=</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Previous to MySQL 5.1.17 and MySQL Cluster NDB 6.1.5, the path to the backup directory was specified as shown here, with <code>backup_path=</code> being optional: </p>
<dl>
<dt>
<dd>
<pre>
[backup_path=]<i>/path/to/backup/files</i>
</pre>
</dl>
<p> Beginning with MySQL 5.1.17 and MySQL Cluster NDB 6.1.5, this syntax changed to <code>&#8211;backup_path=</code><i>/path/to/backup/files</i>, to conform more closely with options used by other MySQL programs; <code>&#8211;backup_id</code> is required, and there is no short form for this option. </p>
</dl>
<p> It is possible to restore a backup to a database with a different configuration than it was created from. For example, suppose that a backup with backup ID 12, created in a cluster with two database nodes having the node IDs 2 and 3, is to be restored to a cluster with four nodes. Then <code>ndb_restore</code> must be run twice &#8212; once for each database node in the cluster where the backup was taken. However, <code>ndb_restore</code> cannot always restore backups made from a cluster running one version of MySQL to a cluster running a different MySQL version. See Section 17.2.6.2, lqMySQL Cluster 5.1 and MySQL Cluster NDB 6.x/7.x Upgrade and Downgrade Compatibilityrq, for more information. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> It is not possible to restore a backup made from a newer version of MySQL Cluster using an older version of <code>ndb_restore</code>. You can restore a backup made from a newer version of MySQL to an older cluster, but you must use a copy of <code>ndb_restore</code> from the newer MySQL Cluster version to do so. </p>
<p> For example, to restore a cluster backup taken from a cluster running MySQL Cluster NDB 6.2.15 to a cluster running MySQL 5.1.20, you must use a copy of <code>ndb_restore</code> from the MySQL Cluster NDB 6.2.15 distribution. </p>
</dl>
<p> For more rapid restoration, the data may be restored in parallel, provided that there is a sufficient number of cluster connections available. That is, when restoring to multiple nodes in parallel, you must have an [api] or [mysqld] section in the cluster config.ini file available for each concurrent <code>ndb_restore</code> process. However, the data files must always be applied before the logs. </p>
<p> Formerly, when using <code>ndb_restore</code> to restore a backup made from a MySQL 5.0 cluster to a 5.1 cluster, VARCHAR columns were not resized and were recreated using the 5.0 fixed format. Beginning with MySQL 5.1.19, ndb_restore recreates such VARCHAR columns using MySQL Cluster 5.1&#8217;s variable-width format. Also beginning with MySQL 5.1.19, this behavior can be overridden using the <code>&#8211;no-upgrade</code> option (short form: <code>-u</code>) when running <code>ndb_restore</code>. </p>
<p> This option causes <code>ndb_restore</code> to print its output to stdout. Beginning with MySQL 5.1.18, several additional options are available for use with the <code>&#8211;print_data</code> option in generating data dumps, either to stdout, or to a file. These are similar to some of the options used with <code>mysqldump</code>, and are shown in the following list: </p>
<dl>
<dt>
<dd> * <code>&#8211;tab</code>, <code>-T</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.18
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;tab=path
</td>
</tr>
</table>
<p> This option causes <code>&#8211;print_data</code> to create dump files, one per table, each named <i>tbl_name</i>.txt. It requires as its argument the path to the directory where the files should be saved; use . for the current directory.</dl>
<dl>
<dt>
<dd> * <code>&#8211;fields-enclosed-by=</code><i>string</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.18
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;fields-enclosed-by=char
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> Each column values are enclosed by the string passed to this option (regardless of data type; see next item).</dl>
<dl>
<dt>
<dd> * <code>&#8211;fields-optionally-enclosed-by=</code><i>string</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.18
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;fields-optionally-enclosed-by
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> The string passed to this option is used to enclose column values containing character data (such as CHAR, VARCHAR, BINARY, TEXT, or ENUM).</dl>
<dl>
<dt>
<dd> * <code>&#8211;fields-terminated-by=</code><i>string</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.18
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;fields-terminated-by=char
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> 	 (tab) </td>
</tr>
</table>
<p> The string passed to this option is used to separate column values. The default value is a tab character (	).</dl>
<dl>
<dt>
<dd> * <code>&#8211;hex</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.18
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;hex
</td>
</tr>
</table>
<p> If this option is used, all binary values are output in hexadecimal format.</dl>
<dl>
<dt>
<dd> * <code>&#8211;fields-terminated-by=</code><i>string</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.18
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;fields-terminated-by=char
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> 	 (tab) </td>
</tr>
</table>
<p> This option specifies the string used to end each line of output. The default is a linefeed character (
).</dl>
<dl>
<dt>
<dd> * <code>&#8211;append</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.18
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;append
</td>
</tr>
</table>
<p> When used with the <code>&#8211;tab</code> and <code>&#8211;print_data</code> options, this causes the data to be appended to any existing files having the same names.</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> If a table has no explicit primary key, then the output generated when using the <code>&#8211;print_data</code> option includes the table&#8217;s hidden primary key. </p>
</dl>
<p> Beginning with MySQL 5.1.18, it is possible to restore selected databases, or to restore selected tables from a given database using the syntax shown here: </p>
<dl>
<dt>
<dd>
ndb_restore other_options db_name, [db_name[, &#8230;] | tbl_name[, tbl_name][, &#8230;]]
</dl>
<p> In other words, you can specify either of the following to be restored: </p>
<dl>
<dt>
<dd> * All tables from one or more databases</dl>
<dl>
<dt>
<dd> * One or more tables from a single database</dl>
<p> <code>&#8211;include-databases=</code><i>db_name</i><code>[,</code><i>db_name</i><code>][,&#8230;]</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.32-ndb-6.4.3
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;include-databases=db-list
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> <code>&#8211;include-tables=</code><i>db_name.tbl_name</i><code>[,</code><i>db_name.tbl_name</i><code>][,&#8230;]</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.32-ndb-6.4.3
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;include-tables=table-list
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> Beginning with MySQL Cluster NDB 6.3.22 and MySQL Cluster NDB 6.4.3, you can (and should) use instead the <code>&#8211;include-databases</code> option or the <code>&#8211;include-tables</code> option for restoring only specific databases or tables, respectively. <code>&#8211;include-databases</code> takes a comma-delimited list of databases to be restored. <code>&#8211;include-tables</code> takes a comma-delimited list of tables (in <i>database</i>.<i>table</i> format) to be restored. </p>
<p> When <code>&#8211;include-databases</code> or <code>&#8211;include-tables</code> is used, only those databases or tables named by the option are restored; all other databases and tables are excluded by <code>ndb_restore</code>, and are not restored. </p>
<p> The following table shows several invocations of <code>ndb_restore</code> using <code>&#8211;include-*</code> options (other options possibly required have been omitted for clarity), and the effects these have on restoring from a MySQL Cluster backup: </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Option Used </code></td>
<td><code> Result </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;include-databases=db1</code> </td>
<td> Only tables in database db1 are restored; all tables<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in all other databases are ignored
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;include-databases=db1,db2</code> (or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;include-databases=db1</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;include-databases=db2</code>) </td>
<td> Only tables in databases db1 and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>db2 are restored;&nbsp;<wbr>all tables in all<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>other databases are ignored
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;include-tables=db1.t1</code> </td>
<td> Only table t1 in database db1 is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>restored;&nbsp;<wbr>no other tables in db1 or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in any other database are restored
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;include-tables=db1.t2,db2.t1</code> (or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;include-tables=db1.t2</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;include-tables=db2.t1</code>) </td>
<td> Only the table t2 in database db1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and the table t1 in database<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>db2 are restored;&nbsp;<wbr>no other tables<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in db1, db2, or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>any other database are restored
</td>
</tr>
</table>
<p> Beginning with MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10, you can use these two options together. For example, the following causes all tables in databases db1 and db2, together with the tables t1 and t2 in database db3, to be restored (and no other databases or tables): </p>
<dl>
<dt>
<dd>
shell &gt; ndb_restore[&#8230;]&#8211; include &#8211; databases = db1, db2&#8211; include &#8211; tables = db3.t1, db3.t2
</dl>
<p> (Again we have omitted other, possibly required, options in the example just shown.) </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Prior to MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10, multiple <code>&#8211;include-*</code> options were not handled correctly, and the result of the options shown in the previous example was that only the tables db3.t1 and db3.t2 were actually restored. (m[blue]<code>Bug#48907</code>m[]<font SIZE="-2">[1]</font>) </p>
</dl>
<p> <code>&#8211;exclude-databases=</code><i>db_name</i><code>[,</code><i>db_name</i><code>][,&#8230;]</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.32-ndb-6.4.3
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;exclude-databases=db-list
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> <code>&#8211;exclude-tables=</code><i>db_name.tbl_name</i><code>[,</code><i>db_name.tbl_name</i><code>][,&#8230;]</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.32-ndb-6.4.3
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;exclude-tables=table-list
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> Also beginning with MySQL Cluster NDB 6.3.22 and MySQL Cluster NDB 6.4.3, it is possible to exclude from being restored one or more databases or tables using the <code>ndb_restore</code> options <code>&#8211;exclude-databases</code> and <code>&#8211;exclude-tables</code>. <code>&#8211;exclude-databases</code> takes a comma-delimited list of one or more databases which should not be restored. <code>&#8211;exclude-tables</code> takes a comma-delimited list of one or more tables (using <i>database</i>.<i>table</i> format) which should not be restored. </p>
<p> When <code>&#8211;exclude-databases</code> or <code>&#8211;exclude-tables</code> is used, only those databases or tables named by the option are excluded; all other databases and tables are restored by <code>ndb_restore</code>. </p>
<p> This table shows several invocations of <code>ndb_restore</code> usng <code>&#8211;exclude-*</code> options (other options possibly required have been omitted for clarity), and the effects these options have on restoring from a MySQL Cluster backup: </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Option Used </code></td>
<td><code> Result </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;exclude-databases=db1</code> </td>
<td> All tables in all databases except db1 are restored;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no tables in db1 are restored
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;exclude-databases=db1,db2</code> (or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;exclude-databases=db1</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;exclude-databases=db2</code>) </td>
<td> All tables in all databases except db1 and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>db2 are restored;&nbsp;<wbr>no tables in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>db1 or db2 are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>restored
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;exclude-tables=db1.t1</code> </td>
<td> All tables except t1 in database<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>db1 are restored;&nbsp;<wbr>all other tables<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in db1 are restored;&nbsp;<wbr>all tables in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>all other databases are restored
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;exclude-tables=db1.t2,db2.t1</code> (or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;exclude-tables=db1.t2</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;exclude-tables=db2.t1)</code> </td>
<td> All tables in database db1 except for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t2 and all tables in database<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>db2 except for table<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t1 are restored;&nbsp;<wbr>no other tables in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>db1 or db2 are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>restored;&nbsp;<wbr>all tables in all other databases are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>restored
</td>
</tr>
</table>
<p> Beginning with MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10, you can use these two options together. For example, the following causes all tables in all databases <i>except for</i> databases db1 and db2, along with the tables t1 and t2 in database db3, <i>not</i> to be restored: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; ndb_restore[...]-- exclude - databases = db1, db2-- exclude - tables = db3.t1, db3.t2
</code></pre>
</dl>
<p> (Again, we have omitted other possibly necessary options in the interest of clarity and brevity from the example just shown.) </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Prior to MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10, multiple <code>&#8211;exclude-*</code> options were not handled correctly, with the result that the options shown in the previous example caused ndb_restore to exclude only the tables db3.t1 and db3.t2. (m[blue]<code>Bug#48907</code>m[]<font SIZE="-2">[1]</font>) </p>
</dl>
<p> Beginning with MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10, you can use <code>&#8211;include-*</code> and <code>&#8211;exclude-*</code> options together, subject to the following rules: </p>
<dl>
<dt>
<dd> * The actions of all <code>&#8211;include-*</code> and <code>&#8211;exclude-*</code> options are cumulative.</dl>
<dl>
<dt>
<dd> * All <code>&#8211;include-*</code> and <code>&#8211;exclude-*</code> options are evaluated in the order passed to ndb_restore, from right to left.</dl>
<dl>
<dt>
<dd> * In the event of conflicting options, the first (rightmost) option takes precedence. In other words, the first option (going from right to left) that matches against a given database or table lqwinsrq.</dl>
<p> For example, the following set of options causes <code>ndb_restore</code> to restore all tables from database db1 except db1.t1, while restoring no other tables from any other databases: </p>
<dl>
<dt>
<dd>
<pre>
--include-databases=db1 --exclude-tables=db1.t1
</pre>
</dl>
<p> However, reversing the order of the options just given simply causes all tables from database db1 to be restored (including db1.t1, but no tables from any other database), because the <code>&#8211;include-dabases</code> option, being farthest to the right, is the first match against database db1 and thus takes precedence over any other option that matches db1 or any tables in db1: </p>
<dl>
<dt>
<dd>
<pre>
--exclude-tables=db1.t1 --include-databases=db1
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Prior to MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10, it was not possible to use <code>&#8211;include-databases</code> or <code>&#8211;include-tables</code> together with <code>&#8211;exclude-databases</code> or <code>&#8211;exclude-tables</code>, as these combinations were evaluated inconsistently. (m[blue]<code>Bug#48907</code>m[]<font SIZE="-2">[1]</font>) </p>
</dl>
<p> <code>&#8211;exclude-missing-columns</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.35-ndb-7.0.7
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;exclude-missing-columns
</td>
</tr>
</table>
<p> Beginning with MySQL Cluster NDB 6.3.26 and MySQL Cluster NDB 7.0.7, it is also possible to restore only selected table columns using the <code>&#8211;exclude-missing-columns</code> option. When this option is used, <code>ndb_restore</code> ignores any columns missing from tables being restored as compared to the versions of those tables found in the backup. This option applies to all tables being restored. If you wish to apply this option only to selected tables or databases, you can use it in combination with one or more of the options described in the previous paragraph to do so, then restore data to the remaining tables using a complementary set of these options. </p>
<p> <code>&#8211;disable-indexes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.41-ndb-7.1.2
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;disable-indexes
</td>
</tr>
</table>
<p> Beginning with MySQL Cluster NDB 6.3.31, MySQL Cluster NDB 7.0.11, and MySQL CLuster NDB 7.1.2, you can use this option with <code>ndb_restore</code> to disable the indexes found in a backup for faster restoration of the data. </p>
<p> <code>&#8211;rebuild-indexes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.41-ndb-7.1.2
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;rebuild-indexes
</td>
</tr>
</table>
<p> Beginning with MySQL Cluster NDB 6.3.31, MySQL Cluster NDB 7.0.11, and MySQL CLuster NDB 7.1.2, you can use this option with <code>ndb_restore</code> to cause multi-threaded rebuilding of the ordered indexes found in a backup during the restoration process. </p>
<p> <code>Error reporting</code>. <code>ndb_restore</code> reports both temporary and permanent errors. In the case of temporary errors, it may able to recover from them. Beginning with MySQL 5.1.12, it reports Restore successful, but encountered temporary error, please look at configuration in such cases. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> After using <code>ndb_restore</code> to initialize a MySQL Cluster for use in circular replication, binary logs on the SQL node acting as the replication slave are not automatically created, and you must cause them to be created manually. In order to cause the binary logs to be created, issue a SHOW TABLES statement on that SQL node before running START SLAVE. </p>
<p> This is a known issue with MySQL Cluster management, which we intend to address in a future release. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Bug#48907</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bugs.mysql.com/bug.php?id=48907">http://bugs.mysql.com/bug.php?id=48907</a></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
