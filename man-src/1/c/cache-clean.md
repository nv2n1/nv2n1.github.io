---
title: "cache-clean(1)"
name: "cache-clean"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cache-clean/"
description: "cache-clean – Administration tool for the A-REX cache."
---

<h2>NAME</h2>
<p> cache-clean &#8211; Administration tool for the A-REX cache. </p>
<h2>SYNOPSIS</h2>
<p> cache-clean [-h] [-s] [-S] [-m NN -M NN] [-E N] [-D debug_level]<br />
&nbsp;<wbr>&nbsp;<wbr>[-f space_command]&nbsp;<wbr>[&nbsp;<wbr>-c&nbsp;<wbr>&lt;arex_config_file&gt;&nbsp;<wbr>|&nbsp;<wbr>&lt;dir1&gt;&nbsp;<wbr>[&lt;dir2&gt;&nbsp;<wbr>[&#8230;]]&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> <code>cache-clean</code> is a tool for administrators of ARC server installations to safely remove A-REX cache data and to provide an overview of the contents of the cache. It is used by the A-REX to automatically manage cache contents. </p>
<p> There are two modes of operation &#8211; printing statistics and deleting files. If <code>-s</code> is used, then statistics are printed on each cache. If <code>-m</code> and <code>-M</code> are used then files in each cache are deleted if the space used by the cache on the file system is more than that given by <code>-M,</code> in the order of least recently accessed, until the space used by the cache is equal to what is specified by <code>-m.</code> If <code>-E</code> is used, then all files accessed less recently than the given time are deleted. <code>-E</code> can be used in combination with <code>-m</code> and <code>-M</code> but deleting files using <code>-E</code> is carried out first. If after this the cache used space is still more than that given by <code>-M</code> then cleaning according to those options is performed. </p>
<p> If the cache is on a file system shared with other data then <code>-S</code> should be specified so that the space used by the cache is calculated. Otherwise all the used space on the file system is assumed to be for the cache. Using <code>-S</code> is slower so should only be used when the cache is shared. </p>
<p> By default the &quot;df&quot; command is used to determine total and (if <code>-S</code> is not specified) used space. If this command is not supported on the cache file system then <code>-f</code> can be used to specify an alternate command. The output of this command must be &quot;total_bytes used_bytes&quot;, and so the command would normally be a small script around the file system space information tool. The cache directory is passed as the last argument to this command. </p>
<p> Cache directories are given by <code>dir1, dir2..</code> or taken from the config file specified by <code>-c</code> or the ARC_CONFIG environment variable. </p>
<p> <code>-h</code> &#8211; print short help </p>
<p> <code>-s</code> &#8211; print cache statistics, without deleting anything. The output displays for each cache the number of deletable (and locked) files, the total size of these files, the percentage usage of the file system in which the cache is stored, and a histogram of access times of the files in the cache. </p>
<p> <code>-S</code> &#8211; Calculate the size of the cache instead of taking used space on the file system. This should only be used when the cache file system is shared with other data. </p>
<p> <code>-M</code> &#8211; the maximum used space (as % of the file system) at which to start cleaning </p>
<p> <code>-m</code> &#8211; the minimum used space (as % of the file system) at which to stop cleaning </p>
<p> <code>-E</code> &#8211; files accessed less recently than the given time period will be deleted. Example values of this option are 1800, 90s, 24h, 30d. The default when no suffix is given is seconds. </p>
<p> <code>-f</code> &#8211; alternative command to &quot;df&quot; for obtaining the file system total and used space. The output of this command must be &quot;total_bytes used_bytes&quot;. The cache directory is passed as the last argument to this command. </p>
<p> <code>-D</code> &#8211; debug level. Possible values are FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG. Default level is INFO. </p>
<p> <code>-c</code> &#8211; path to an A-REX config file, xml or ini format </p>
<p> This tool is run periodically by the A-REX to keep the size of each cache within the limits specified in the configuration file. Therefore cleaning should not be performed manually, unless the cache size needs to be reduced temporarily. For performance reasons it may however be desirable to run cache-clean independently on the machine hosting the cache file system, if this is different from the A-REX host. The most useful function for administrators is to give an overview of the contents of the cache, using the <code>-s</code> option. </p>
<p> Within each cache directory specified in the configuration file, there is a subdirectory for data (data/) and one for per-job hard links (joblinks/). See the A-REX Administration Guide for more details. <code>cache-clean</code> should only operate on the data subdirectory, therefore when giving <code>dir</code> arguments they should be the top level cache directory. <code>cache-clean</code> will then automatically only look at files within the data directory. </p>
<h2>EXAMPLE</h2>
<p> <code>cache-clean -m20 -M30 -E30d -D VERBOSE -c /etc/arc.conf</code> </p>
<p> Cache directories are taken from the configuration file <code>/etc/arc.conf</code> and all cache files accessed more than 30 days ago are deleted. Then if the used space in a cache is above 30%, data is deleted until the used space reaches 20%. Verbose debug output is enabled so information is output on each file that is deleted. </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>Index</h2>
