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
<dt><code>-c</code></p>
<dd> Specify configuration options ignoring any value they may have based on the input. The command-line format is <code>name=value</code>. See the Supported Keywords section below for a list of keywords supported by the <code>-c</code> option.</p>
<dt><code>-f</code></p>
<dd> Read from the specified <code>input</code> file instead of from the standard input.</p>
<dt><code>-h</code></p>
<dd> Specify a home directory for the database environment. </p>
<p> If a home directory is specified, the database environment is opened using the DB_INIT_LOCK, DB_INIT_LOG, DB_INIT_MPOOL, DB_INIT_TXN, and DB_USE_ENVIRON flags to DB_ENV-&gt;open. (This means that db5.3_load can be used to load data into databases while they are in use by other processes.) If the DB_ENV-&gt;open call fails, or if no home directory is specified, the database is still updated, but the environment is ignored; for example, no locking is done.</p>
<dt><code>-n</code></p>
<dd> Do not overwrite existing keys in the database when loading into an already existing database. If a key/data pair cannot be loaded into the database for this reason, a warning message is displayed on the standard error output, and the key/data pair are skipped.</p>
<dt><code>-P</code></p>
<dd> Specify an environment password. Although Berkeley DB utilities overwrite password strings as soon as possible, be aware there may be a window of vulnerability on systems where unprivileged users can see command-line arguments or where utilities are not able to overwrite the memory containing the command-line arguments.</p>
<dt><code>-r</code></p>
<dd> Reset the database&#8217;s file ID or log sequence numbers (LSNs). </p>
<p> All database pages in transactional environments contain references to the environment&#8217;s log records. In order to copy a database into a different database environment, database page references to the old environment&#8217;s log records must be reset, otherwise data corruption can occur when the database is modified in the new environment. The <code>-r</code> <code>lsn</code> option resets a database&#8217;s log sequence numbers. </p>
<p> All databases contain an ID string used to identify the database in the database environment cache. If a database is copied, and used in the same environment as another file with the same ID string, corruption can occur. The <code>-r</code> <code>fileid</code> option resets a database&#8217;s file ID to a new value. </p>
<p> <code>In both cases, the physical file specified by the file argument is modified in-place.</code></p>
<dt><code>-T</code></p>
<dd> The <code>-T</code> option allows non-Berkeley DB applications to easily load text files into databases. </p>
<p> If the database to be created is of type Btree or Hash, or the keyword <code>keys</code> is specified as set, the input must be paired lines of text, where the first line of the pair is the key item, and the second line of the pair is its corresponding data item. If the database to be created is of type Queue or Recno and the keyword <code>keys</code> is not set, the input must be lines of text, where each line is a new data item for the database. </p>
<p> A simple escape mechanism, where newline and backslash (\) characters are special, is applied to the text input. Newline characters are interpreted as record separators. Backslash characters in the text will be interpreted in one of two ways: If the backslash character precedes another backslash character, the pair will be interpreted as a literal backslash. If the backslash character precedes any other character, the two characters following the backslash will be interpreted as a hexadecimal specification of a single character; for example, 
