---
title: "wcmgr(1)"
name: "wcmgr"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wcmgr/"
description: "wcmgr – Webalizer (DNS) Cache file Manager"
---

<h2>NAME</h2>
<p> wcmgr &#8211; Webalizer (DNS) Cache file Manager</p>
<h2>SYNOPSIS</h2>
<p> <code>wcmgr</code> [<i> option &#8230; </i>] <i>cache-file</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>wcmgr</i> is a utility program which allows manipulation of the DNS cache files used and produced by The <i>Webalizer</i>. Each record in the cache file contains an IP address (either IPv4 or IPv6), a timestamp of when the entry was added to the cache, a flag to indicate if the record contains a resolved name or not, and either the same IP address or a resolved host name. All records are accessed by their IP address.</p>
<h2>RUNNING WCMGR</h2>
<p> <i>wcmgr</i> was designed to be run from the Unix shell command line. This facilitates its use in shell scripts and other automated processes. A valid DNS cache file <code>must</code> be specified. Command line options are optional, and if none are given, the default action is to list the contents of the specified cache file.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> Different functions are selected by using one or more of the following command line options. If no options are given, the default is to display the contents of the cache file to the screen (stdout). </p>
<dl>
<dt><code>-h</code></p>
<dd> Display all available command line options and exit.</p>
<dt><code>-v</code></p>
<dd> Be verbose. </p>
<dt><code>-V</code></p>
<dd> Display the program version and exit. Additional program specific information will be displayed if <i>verbose</i> mode is also used (e.g. &#8216;<i>-vV</i>&#8216;), which can be useful when submitting bug reports.</p>
<dt><code>-a </code><i>address</i> [<i>-n hostname</i>] [<i>-t0</i>]</p>
<dd> Add a new record to the cache file. The IP <i>address</i> will be added to the cache file using the current time as the timestamp and with a resolved name <i>hostname</i>. If <i>-t0</i> is specified, the record will be considered permanent, and will not be removed (during a purge) or expired. If a <i>hostname</i> is not specified with the <i>-n</i> option, then the <i>address</i> will be used instead, and the record will be flagged as unresolved.</p>
<dt><code>-c</code></p>
<dd> Create a new cache file. If used alone, this option will create a new, empty cache file. If used with the <i>import</i> option, a new cache file will be created before importing the data. An error will occur if the file <i>cache-file</i> already exists.</p>
<dt><code>-d </code><i>address</i></p>
<dd> Delete a record from the cache file using the specified <i>address</i>.</p>
<dt><code>-f </code><i>address</i></p>
<dd> Find and display information for <i>address</i> from the cache file. A single line similar to that produced by the <i>-l</i> option will be displayed unless <i>verbose</i> mode is enabled, in which case a more detailed listing will be produced.</p>
<dt><code>-i </code><i>name</i> [<i>-c</i>]</p>
<dd> Import data into the cache file from the file <i>name</i>. The import file must be a valid tab delimited text file, such as that created by the <i>export</i> option. If the imported data contains records already present in the cache file, those records will be overwritten by the imported data. The cache file must exist unless the <i>-c</i> option is specified, in which case, a new cache file will be created for the imported data.</p>
<dt><code>-l</code></p>
<dd> List the contents of the cache file. This is the default action of the program, so does not necessarily need to be specified. If <i>verbose</i> mode is enabled, a report title, column headers and summary totals will also be displayed.</p>
<dt><code>-p </code><i>num</i></p>
<dd> Purge the cache file of entries older than <i>num</i> days. If <i>num</i> is not specified, then a default of <code>7 days</code> will be used. if <i>verbose</i> mode is enabled, each purged record will be printed and the total number of purged records will be displayed.</p>
<dt><code>-s [</code><i>-t num</i>]</p>
<dd> Display cache file information/statistics. If a TTL value (in days) is specified using the <i>-t</i> option, it will be used to calculate how many records are older than <i>num</i> days, otherwise, the default value of <code>7 days</code> will be used.</p>
<dt><code>-n </code><i>name</i></p>
<dd> Specify the <i>name</i> to use as the resolved hostname when adding records to the cache.</p>
<dt><code>-t </code><i>num</i></p>
<dd> Time to live (TTL) value. If used along with the <i>-p</i> (purge) option, it specifies how many days a record will remain valid. Any record that is older than <i>num</i> days is considered expired and will be purged. If used with the <i>-a</i> (add) option, a zero value will cause the record to be considered permanent.</p>
<dt><code>-x </code><i>name</i></p>
<dd> Export data from a cache file to a tab delimited text file named <i>name</i>. If the text file <i>name</i> exists, it will be overwritten.</dl>
<h2>BUGS</h2>
<p> Please report bugs to the author.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2013 by Bradford L. Barrett. Distributed under the GNU GPL. See the files &quot;<i>COPYING</i>&quot; and &quot;<i>Copyright</i>&quot;, supplied with all distributions for additional information.</p>
<h2>AUTHOR</h2>
<p> Bradford L. Barrett &lt;<i>brad at mrunix dot net</i>&gt; </p>
<h2>Index</h2>
