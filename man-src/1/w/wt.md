---
title: "wt(1)"
name: "wt"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wt/"
description: "wt – WiredTiger command line utility WiredTiger includes a command line utility, wt."
---

<h2 class="name">NAME</h2>
<p> wt &#8211; WiredTiger command line utility WiredTiger includes a command line utility, wt. </p>
<h2>SYNOPSIS</h2>
<p> wt [-LRVv] [-C config] [-E secretkey ] [-h directory] command [command-specific arguments]</p>
<h2>DESCRIPTION</h2>
<p> The wt tool is a command-line utility that provides access to various pieces of the WiredTiger functionality.</p>
<h2>OPTIONS</h2>
<p> There are several global options: </p>
<p> <code>-C config</code></p>
<dl>
<dt>
<dd> Specify configuration strings for the <code>wiredtiger_open</code> function.</dl>
<p> <code>-E secretkey</code></p>
<dl>
<dt>
<dd> Specify an encryption secret key for the <code>wiredtiger_open</code> function.</dl>
<p> <code>-h directory</code></p>
<dl>
<dt>
<dd> Specify a database home directory.</dl>
<p> <code>-L</code></p>
<dl>
<dt>
<dd> Forcibly turn off logging subsystem for debugging purposes.</dl>
<p> <code>-R</code></p>
<dl>
<dt>
<dd> Run recovery if the underlying database is configured to do so.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Display WiredTiger version and exit.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Set verbose output.</dl>
<p> Unless otherwise described by a wt command, the wt tool exits zero on success and non-zero on error. </p>
<p> The wt tool supports several commands. If configured in the underlying database, some commands will run recovery when opening the database. If the user wants to force recovery on any command, use the -r option. In general, commands that modify the database or tables will run recovery by default and commands that only read data will not run recovery. </p>
<p>&nbsp;<wbr></p>
<h2>wt backup</h2>
<p> Perform a backup of a database or set of data sources. </p>
<p> The backup command performs a backup of the database, copying the database files to a specified directory, which can be subsequently opened as a WiredTiger database. See <code>Backups</code> for more information, and <code>File permissions</code> for specifics on the copied file permissions.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] backup [-t uri] directory</p>
<h3>Options</h3>
<p> The following are command-specific options for the backup command: </p>
<p> <code>-t uri</code></p>
<dl>
<dt>
<dd> By default, the backup command does a backup of the entire database; the -t option changes the backup command to do a backup of only the named data sources.</dl>
<p>&nbsp;<wbr></p>
<h2>wt compact</h2>
<p> Compact a table or file. </p>
<p> The compact command attempts to rewrite the specified table or file to consume less disk space.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] compact uri</p>
<h3>Options</h3>
<p> The compact command has no command-specific options. </p>
<p>&nbsp;<wbr></p>
<h2>wt create</h2>
<p> Create a table or file. </p>
<p> The create command creates the specified uri with the specified configuration. It is equivalent to a call to <code>WT_SESSION::create</code> with the specified string arguments.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] create [-c config] uri</p>
<h3>Options</h3>
<p> The following are command-specific options for the create command: </p>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Include a configuration string to be passed to <code>WT_SESSION::create</code>.</dl>
<p>&nbsp;<wbr></p>
<h2>wt drop</h2>
<p> Drop a table or file. </p>
<p> The drop command drops the specified uri. It is equivalent to a call to <code>WT_SESSION::drop</code> with the &#8216;force&#8217; configuration argument.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] drop uri</p>
<h3>Options</h3>
<p> The drop command has no command-specific options. </p>
<p>&nbsp;<wbr></p>
<h2>wt dump</h2>
<p> Export data in a text format. </p>
<p> The dump command outputs the specified table in a portable format which can be re-loaded into a new table using the load command. </p>
<p> See <code>Dump Formats</code> for details of the dump file formats.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] dump [-jrx] [-c checkpoint] [-f output] uri</p>
<h3>Options</h3>
<p> The following are command-specific options for the dump command: </p>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> By default, the dump command opens the most recent version of the data source; the -c option changes the dump command to open the named checkpoint.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> By default, the dump command output is written to the standard output; the -f option re-directs the output to the specified file.</dl>
<p> <code>-j</code></p>
<dl>
<dt>
<dd> Dump in JSON (JavaScript Object Notation) format.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Dump in reverse order, from largest key to smallest.</dl>
<p> <code>-x</code></p>
<dl>
<dt>
<dd> Dump all characters in a hexadecimal encoding (the default is to leave printable characters unencoded).</dl>
<p>&nbsp;<wbr></p>
<h2>wt list</h2>
<p> List the tables and files in the database. </p>
<p> By default, the list command prints out the tables and files stored in the database. If a URI is specified as an argument, only information about that data source is printed.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] list [-cv] [uri]</p>
<h3>Options</h3>
<p> The following are command-specific options for the list command: </p>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> If the -c option is specified, the data source&#8217;s checkpoints are printed in a human-readable format.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> If the -v option is specified, the data source&#8217;s complete schema table value is printed.</dl>
<p>&nbsp;<wbr></p>
<h2>wt load</h2>
<p> Load a table or file from dump output. </p>
<p> The load command reads the standard input for data and loads it into a table or file, creating the table or file if it does not yet exist. The data should be the format produced by the dump command; see <code>Dump Formats</code> for details. </p>
<p> By default, if the table or file already exists, data in the file or table will be overwritten by the new data (use the -n option to make an attempt to overwrite existing data return an error).</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] load [-ajn] [-f input] [-r name] [uri configuration &#8230;]</p>
<h3>Options</h3>
<p> The following are command-specific options for the load command: </p>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> If the -a option is specified, record number keys in the input are ignored and the data is appended to the data source and assigned new record number keys. The -a option is only applicable when loading into a column store.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> By default, the load command reads from the standard input; the -f option reads the input from the specified file.</dl>
<p> <code>-j</code></p>
<dl>
<dt>
<dd> Load input in the JSON (JavaScript Object Notation) format that was created by the dump -j command.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> By default, input data will overwrite existing data where the key/value pair already exists in the data source; the -n option causes the load command to fail if there&#8217;s an attempt to overwrite already existing data.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> By default, the load command uses the table or file name taken from the input; the -r option renames the data source.</dl>
<p> Additionally, uri and configuration pairs may be specified to the load command. These configuration pairs can be used to modify the configuration values from the dump header passed to the <code>WT_SESSION::create</code> call. </p>
<p> The uri part of the configuration pair should match only one of the objects being loaded, but may be a prefix of the object being matched. For example, the following two sets of configuration pairs are equivalent in the case of loading a single table named xxx. </p>
<pre>
table block_allocation=first
table:xxx block_allocation=first
</pre>
<p> It&#8217;s an error, however, to specify a matching prefix that matches more than a single object being loaded. </p>
<p> Multiple configuration arguments may be specified. For example, the following two sets of configuration pairs are equivalent: </p>
<pre>
table:xxx block_allocation=first,prefix_compress=false
table:xxx block_allocation=first table:xxx prefix_compress=false
</pre>
<p>&nbsp;<wbr></p>
<h2>wt loadtext</h2>
<p> Load text into a table or file. </p>
<p> The loadtext command reads the standard input for text and loads it into a table or file. The input data should be printable characters, with newline delimiters for each key or value. </p>
<p> The loadtext command does not create the file if it does not yet exist. </p>
<p> In the case of inserting values into a column-store table or file, each value is appended to the table or file; in the case of inserting values into a row-store table or file, lines are handled in pairs, where the first line is the key and the second line is the value. If the row-store table or file already exists, data in the table or file will be overwritten by the new data.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] loadtext [-f input]</p>
<h3>Options</h3>
<p> The following are command-specific options for the loadtext command: </p>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> By default, the loadtext command reads from the standard input; the -f option reads the input from the specified file.</dl>
<p>&nbsp;<wbr></p>
<h2>wt printlog</h2>
<p> Display the database log. </p>
<p> The printlog command outputs the database log.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] printlog [-p] [-f output]</p>
<h3>Options</h3>
<p> The following are command-specific options for the printlog command: </p>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> By default, the printlog command output is written to the standard output; the -f option re-directs the output to the specified file.</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Display the log in a printable format.</dl>
<p>&nbsp;<wbr></p>
<h2>wt read</h2>
<p> Read records from a table or file. </p>
<p> The read command prints out the records associated with the specified keys from the specified data source. The data source must be configured with string or record number keys and string values. </p>
<p> The read command exits non-zero if a specified record is not found.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] read uri key &#8230;</p>
<h3>Options</h3>
<p> The read command has no command-specific options. </p>
<p>&nbsp;<wbr></p>
<h2>wt rename</h2>
<p> Rename a table or file. </p>
<p> The rename command renames the specified table or file.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] rename uri name</p>
<h3>Options</h3>
<p> The rename command has no command-specific options. </p>
<p>&nbsp;<wbr></p>
<h2>wt salvage</h2>
<p> Recover data from a corrupted file. </p>
<p> The salvage command salvages the specified data source, discarding any data that cannot be recovered. Underlying files are re-written in place, overwriting the original file contents.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] salvage [-F force] uri</p>
<h3>Options</h3>
<p> The following are command-specific options for the salvage command: </p>
<p> <code>-F</code></p>
<dl>
<dt>
<dd> By default, salvage will refuse to salvage files that fail basic tests (for example, files that don&#8217;t appear to be in a WiredTiger format). The -F option forces the salvage of the file, regardless.</dl>
<p>&nbsp;<wbr></p>
<h2>wt stat</h2>
<p> Display database or data source statistics. </p>
<p> The stat command outputs run-time statistics for the WiredTiger engine, or, if specified, for the URI on the command-line.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] stat [-f] [uri]</p>
<h3>Options</h3>
<p> The following are command-specific options for the stat command: </p>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Include only &#8216;fast&#8217; statistics in the output (equivalent to passing statistics=(fast)) to <code>WT_SESSION::open_cursor</code>.</dl>
<p>&nbsp;<wbr></p>
<h2>wt upgrade</h2>
<p> Upgrade a table or file. </p>
<p> The upgrade command upgrades the specified table or file, exiting success if the data source is up-to-date, and failure if the data source cannot be upgraded.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] upgrade uri</p>
<h3>Options</h3>
<p> The upgrade command has no command-specific options. </p>
<p>&nbsp;<wbr></p>
<h2>wt verify</h2>
<p> Check the structural integrity of a table or file. </p>
<p> The verify command verifies the specified table or file, exiting success if the data source is correct, and failure if the data source is corrupted.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] verify uri</p>
<h3>Options</h3>
<p> The verify command has no command-specific options. </p>
<p>&nbsp;<wbr></p>
<h2>wt write</h2>
<p> Write records to a table or file. </p>
<p> The write command stores records into the specified data source. The data source must be configured with string or record number keys and string values. </p>
<p> If the write command is called with the -a option, each command-line argument is a single value to be appended to the specified column-store data source. If the write command is not called with the -a option, the command-line arguments are key/value pairs. </p>
<p> Attempting to overwrite an already existing record will fail.</p>
<h3>Synopsis</h3>
<p> wt [-rVv] [-C config] [-E secretkey ] [-h directory] write -a uri value &#8230; </p>
<p>&nbsp;<wbr>wt&nbsp;<wbr>[-rVv]&nbsp;<wbr>[-C config]&nbsp;<wbr>[-E secretkey&nbsp;<wbr>]&nbsp;<wbr>[-h directory]&nbsp;<wbr>write&nbsp;<wbr>[-o]&nbsp;<wbr>uri key value &#8230;&nbsp;<wbr></p>
<h3>Options</h3>
<p> The following are command-specific options for the write command: </p>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Append each value as a new record in the data source.</dl>
<p> <code>-o</code></p>
<dl>
<dt>
<dd> By default, attempting to overwrite an already existing record will fail. The -o option changes write to overwrite previously existing records.</dl>
<h2>Index</h2>
