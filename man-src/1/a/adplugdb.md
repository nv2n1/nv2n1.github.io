---
title: "adplugdb(1)"
name: "adplugdb"
section: "1"
letter: "a"
url: "/docs/linux/man/1-adplugdb/"
description: "adplugdb – AdPlug database maintenance utility"
---

<h2>NAME</h2>
<p> adplugdb &#8211; AdPlug database maintenance utility</p>
<h2>SYNOPSIS</h2>
<p> <code>adplugdb</code> [OPTION]&#8230; COMMAND [ARGUMENT]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>adplugdb</code> maintains database files in AdPlug database format. It can <code>add</code>, <code>list</code> and <code>remove</code> records within a central database, or <code>merge</code> a set of databases together into one single database. </p>
<p> <code>adplugdb</code> always operates on a central database file. The location of this database file is determined by first checking if the user has a home directory. If a home directory is present, the database file will be located in <code>~/.adplug/adplug.db</code>. If a home directory is not present, a database file <code>adplug.db</code> will be looked for in the current working directory. </p>
<p> A system-wide database file can be used instead, by specifying the <code>-s</code> commandline option. The system-wide database file is located in <code>/var/lib/adplug/adplug.db</code> and may only be manipulated as the superuser. An arbitrary database file might be used as well, by specifying the <code>-d</code> commandline parameter. Only one database file may be manipulated at a time.</p>
<h2>EXIT STATUS</h2>
<p> <code>adplugdb</code> returns with a successful exit status (<code>0</code> on most systems) on successful operation. An unsuccessful exit status (<code>1</code> on most systems) is returned otherwise.</p>
<h2>COMMANDS</h2>
<p> Commands control the main operation mode of <code>adplugdb</code>. Commands can have a number of arguments. Only one command may be specified at a time.</p>
<dl>
<dt><code>add</code></p>
<dd> This command takes a list of filenames, separated by spaces, as arguments. Each file is examined and a record is added to the database if the file is supported by AdPlug. By default, the record will be of type <code>Plain</code>, unless the <code>-t</code> commandline option is specified (see below). The default comment entry is the specified filename. If a record for a file is already in the database, it will be replaced by the new record.</p>
<dt><code>list</code></p>
<dd> This command takes an optional list of filenames or keys, separated by spaces, as arguments. Each file is examined and the corresponding record is looked up from the database and displayed on <code>stdout</code>, in a human-readable form. If no arguments are given, all records from the database are displayed.</p>
<dt><code>remove</code></p>
<dd> This command takes a list of filenames or keys, separated by spaces, as arguments. Each file is examined and the corresponding record is removed from the database.</p>
<dt><code>merge</code></p>
<dd> This command takes a list of database filenames, separated by spaces, as arguments. Each database file is loaded and the contents are merged and written to the central database file. The database files are processed in the order they are specified on the commandline. Records from databases that were specified earlier take precedence over records from databases that were specified later. Records from the central database take precedence over all other records. This means that only additional records from the other databases will be added to the central database and if a record is found that is not already in the central database, the version from the earliest specified database that contains this record will be taken. In no way will records ever be overwritten in the central database.</dl>
<h2>OPTIONS</h2>
<p> The order of the option commandline parameters is not important.</p>
<h3>Database options:</h3>
<dl>
<dt><code>-d &lt;file&gt;</code></p>
<dd> Specify an arbitrary file to use as the central database.</p>
<dt><code>-s</code></p>
<dd> Use the system-wide database file as the central database. This option is only present if <code>adplugdb</code> was compiled with system-wide database file support.</p>
<dt><code>-t &lt;type&gt;</code></p>
<dd> Specify a record type to be used as the type for all newly added records. Each record needs a special type to be useful to AdPlug&#8217;s players. The commandline help, displayed using the <code>-h</code> commandline option, presents a list of types that may be specified.</p>
<dt><code>-c</code></p>
<dd> Prompt for record comment. If this option is given, the user will be prompted and asked for each newly added record&#8217;s comment.</p>
<dt><code>-k</code></p>
<dd> Specify keys instead of filenames. If this option is given, all command arguments that normally are filenames are expected to be record keys instead. Each record in the database has a unique identifying key, generated from the corresponding file&#8217;s contents. To manipulate a record entry, you either must have the exact same file and specify its name, or you specify the record&#8217;s key, using this option. Keys are specified the same way they are displayed using the <code>list</code> command, as CRC16:CRC32 value in hexadecimal format.</dl>
<h3>Generic options:</h3>
<dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Be more quiet.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be more verbose.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of commandline commands, arguments and options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version and author information of the program.</dl>
<h2>AUTHOR</h2>
<p> Simon Peter &lt;dn.tlp [at] gmx.net&gt; </p>
<h2>Index</h2>
