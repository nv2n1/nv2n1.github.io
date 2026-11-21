---
title: "db_load(1)"
name: "db_load"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db_load/"
description: "db5.3_load – Load data from standard input"
---

<h2 class="name">NAME</h2>
<p> db5.3_load &#8211; Load data from standard input </p>
<h2>SYNOPSIS</h2>
<p> <code>db5.3_load</code> [-nTV] [-c name=value] [-f file] [-h home] [-P password] [-t btree | hash | queue | recno] file </p>
<p> <code>db5.3_load</code> [-r lsn | fileid] [-h home] [-P password] file</p>
<h2>DESCRIPTION</h2>
<p> The db5.3_load utility reads from the standard input and loads it into the database file. The database file is created if it does not already exist. </p>
<p> The input to db5.3_load must be in the output format specified by the db5.0_dump utility, utilities, or as specified for the -T below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd> Specify configuration options ignoring any value they may have based on the input. The command-line format is <code>name=value</code>. See the Supported Keywords section below for a list of keywords supported by the <code>-c</code> option.</dd>
<dt><code>-f</code></dt>
<dd> Read from the specified <code>input</code> file instead of from the standard input.</dd>
<dt><code>-h</code></dt>
<dd> Specify a home directory for the database environment. </dd>
<p> If a home directory is specified, the database environment is opened using the DB_INIT_LOCK, DB_INIT_LOG, DB_INIT_MPOOL, DB_INIT_TXN, and DB_USE_ENVIRON flags to DB_ENV-&gt;open. (This means that db5.3_load can be used to load data into databases while they are in use by other processes.) If the DB_ENV-&gt;open call fails, or if no home directory is specified, the database is still updated, but the environment is ignored; for example, no locking is done.</p>
<dt><code>-n</code></dt>
<dd> Do not overwrite existing keys in the database when loading into an already existing database. If a key/data pair cannot be loaded into the database for this reason, a warning message is displayed on the standard error output, and the key/data pair are skipped.</dd>
<dt><code>-P</code></dt>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</dd>
<dt><code>-r</code></dt>
<dd> Reset the database&#8217;s file ID or log sequence numbers (LSNs). </dd>
<p> All database pages in transactional environments contain references to the environment&#8217;s log records. In order to copy a database into a different database environment, database page references to the old environment&#8217;s log records must be reset, otherwise data corruption can occur when the database is modified in the new environment. The <code>-r</code> <code>lsn</code> option resets a database&#8217;s log sequence numbers. </p>
<p> All databases contain an ID string used to identify the database in the database environment cache. If a database is copied, and used in the same environment as another file with the same ID string, corruption can occur. The <code>-r</code> <code>fileid</code> option resets a database&#8217;s file ID to a new value. </p>
<p> <code>In both cases, the physical file specified by the file argument is modified in-place.</code></p>
<dt><code>-T</code></dt>
<dd> The <code>-T</code> option allows non-Berkeley DB applications to easily load text files into databases. </dd>
<p> If the database to be created is of type Btree or Hash, or the keyword <code>keys</code> is specified as set, the input must be paired lines of text, where the first line of the pair is the key item, and the second line of the pair is its corresponding data item. If the database to be created is of type Queue or Recno and the keyword <code>keys</code> is not set, the input must be lines of text, where each line is a new data item for the database. </p>
<p> A simple escape mechanism, where newline and backslash (\) characters are special, is applied to the text input. Newline characters are interpreted as record separators. Backslash characters in the text will be interpreted in one of two ways: If the backslash character precedes another backslash character, the pair will be interpreted as a literal backslash. If the backslash character precedes any other character, the two characters following the backslash will be interpreted as a hexadecimal specification of a single character; for example, \0a is a newline character in the ASCII character set. </p>
<p> For this reason, any backslash or newline characters that naturally occur in the text input must be escaped to avoid misinterpretation by db5.3_load. </p>
<p> If the <code>-T</code> option is specified, the underlying access method type must be specified using the <code>-t</code> option. </p>
<dt><code>-t</code></dt>
<dd> <p> Specify the underlying access method. If no <code>-t</code> option is specified, the database will be loaded into a database of the same type as was dumped; for example, a Hash database will be created if a Hash database was dumped. </p>
<p> Btree and Hash databases may be converted from one to the other. Queue and Recno databases may be converted from one to the other. If the <code>-k</code> option was specified on the call to db5.3_dump then Queue and Recno databases may be converted to Btree or Hash, with the key being the integer record number. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> Write the library version number to the standard output, and exit. </p>
 </dd></dl>
<p> The db5.3_load utility may be used with a Berkeley DB environment (as described for the <code>-h</code> option, the environment variable <code>DB_HOME</code>, or because the utility was run in a directory containing a Berkeley DB environment). In order to avoid environment corruption when using a Berkeley DB environment, db5.3_load should always be given the chance to detach from the environment and exit gracefully. To cause db5.3_load to release all environment resources and exit cleanly, send it an interrupt signal (SIGINT). </p>
<p> The db5.3_load utility exits 0 on success, 1 if one or more key/data pairs were not loaded into the database because the key already existed, and &gt;1 if an error occurs.  </p>
<h2>EXAMPLES</h2>
<p> The db5.3_load utility can be used to load text files into databases. For example, the following command loads the standard UNIX <i>/etc/passwd</i> file into a database, with the login name as the key item and the entire password entry as the data item: </p>
<dl>
<dt>awk -F: &#8216;{print $1; print $0}&#8216; &lt; /etc/passwd |</dt>
<dd> <p> sed &#8216;s/\\/\\\\/g&#8217; | db5.3_load -T -t hash passwd.db </p>
 </dd></dl>
<p> Note that backslash characters naturally occurring in the text are escaped to avoid interpretation as escape characters by db5.3_load.  </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DB_HOME</code></dt>
<dd> <p> If the <code>-h</code> option is not specified and the environment variable DB_HOME is set, it is used as the path of the database home, as described in DB_ENV-&gt;open. </p>
 </dd></dl>
<h2>SUPPORTED KEYWORDS</h2>
<p> The following keywords are supported for the <code>-c</code> command-line ption to the db5.3_load utility. See DB-&gt;open for further discussion of these keywords and what values should be specified. </p>
<p> The parenthetical listing specifies how the value part of the <code>name=value</code> pair is interpreted. Items listed as (boolean) expect value to be <code>1</code> (set) or <code>0</code> (unset). Items listed as (number) convert value to a number. Items listed as (string) use the string value without modification. </p>
<dl>
<dt>bt_minkey (number)</dt>
<dd> <p> The minimum number of keys per page. </p>
 </dd>
<dt>chksum (boolean)</dt>
<dd> <p> Enable page checksums. </p>
 </dd>
<dt>database (string)</dt>
<dd> <p> The database to load. </p>
 </dd>
<dt>db_lorder (number)</dt>
<dd> <p> The byte order for integers in the stored database metadata. </p>
 </dd>
<dt>db_pagesize (number)</dt>
<dd> <p> The size of database pages, in bytes. </p>
 </dd>
<dt>duplicates (boolean)</dt>
<dd> <p> The value of the DB_DUP flag. </p>
 </dd>
<dt>dupsort (boolean)</dt>
<dd> <p> The value of the DB_DUPSORT flag. </p>
 </dd>
<dt>extentsize (number)</dt>
<dd> <p> The size of database extents, in pages, for Queue databases configured to use extents. </p>
 </dd>
<dt>h_ffactor (number)</dt>
<dd> <p> The density within the Hash database. </p>
 </dd>
<dt>h_nelem (number)</dt>
<dd> <p> The size of the Hash database. </p>
 </dd>
<dt>keys (boolean)</dt>
<dd> <p> Specify whether keys are present for Queue or Recno databases. </p>
 </dd>
<dt>re_len (number)</dt>
<dd> <p> Specify fixed-length records of the specified length. </p>
 </dd>
<dt>re_pad (string)</dt>
<dd> <p> Specify the fixed-length record pad character. </p>
 </dd>
<dt>recnum (boolean)</dt>
<dd> <p> The value of the DB_RECNUM flag. </p>
 </dd>
<dt>renumber (boolean)</dt>
<dd> <p> The value of the DB_RENUMBER flag. </p>
 </dd>
<dt>subdatabase (string)</dt>
<dd> <p> The subdatabase to load. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> Sleepycat Software, Inc. This manual page was created based on the HTML documentation for db_load from Sleepycat, by Thijs Kinkhorst &lt;thijs [at] kinkhorst.com&gt;, for the Debian system (but may be used by others). </p>
