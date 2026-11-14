---
title: "globus-rls-cli(1)"
name: "globus-rls-cli"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-rls-cli/"
description: "globus-rls-cli – Globus Replica Location Service Command Line Interface"
---

<h2>NAME</h2>
<p> globus-rls-cli &#8211; Globus Replica Location Service Command Line Interface</p>
<h2>SYNOPSIS</h2>
<p> <code>globus-rls-cli</code> <i>command</i> [ <i>-c</i> ] [ <i>-d</i> ] [ <i>-h</i> ] [ <i>-i inputfile</i> ] [ <i>-l reslimit</i> ] [ <i>-s</i> ] [ <i>-t timeout</i> ] [ <i>-u</i> ] [ command ] <i>rls-server</i></p>
<h2>DESCRIPTION</h2>
<p> <code>globus-rls-cli</code> provides a command line interface to some of the functions supported by the Globus Replica Location service. It also supports an interactive interface (if <i>command</i> is not specified). In interactive move double quotes may be used to encode an argument that contains white space.</p>
<h2>OPTIONS</h2>
<p> <code>globus-rls-cli</code> uses <a href="/docs/linux/man/3-getopt/">getopt</a>(3) to do command line parsing. Some versions will continue scanning for options (works that begin with a hyphen) for the entire command, line, which makes it impossible to specify negative integer or floating point value for an attribute. The workaround for this problem is to tell getopt() that there are no more options, by including 2 hyphens, eg to specify the value &quot;-2&quot; enter &quot;&#8211; -2&quot;.</p>
<dl>
<dt><code>-c</code></p>
<dd> Set &quot;clearvalues&quot; flag when deleting an attribute (will remove any attribute value records when an attribute is deleted).</p>
<dt><code>-d</code></p>
<dd> Decorate the output. By default the output is presented without decorations. Using this option restores decorations in the original style.</p>
<dt><code>-h</code></p>
<dd> Show usage.</p>
<dt><code>-i inputfile</code></p>
<dd> Read bulk input parameters from the input file. Each row of the input file corresponds to an individual operation of the command. If inputfile is replaced with &#8216;-&#8216; input parameters will be read from stdin.</p>
<dt><code>-l reslimit</code></p>
<dd> Set limit on number of results returned by wildcard query at a time. Zero means no limit.</p>
<dt><code>-s</code></p>
<dd> Use SQL style wildcards (% and _).</p>
<dt><code>-t timeout</code></p>
<dd> Set timeout (in seconds) for RLS server requests. Default is 30 seconds.</p>
<dt><code>-u</code></p>
<dd> Use Unix style wildcards (* and ?).</p>
<dt><code>-v</code></p>
<dd> Show version.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>add &lt;lfn&gt; &lt;pfn&gt;</code></p>
<dd> Add <i>pfn</i> to mappings of <i>lfn</i> in an LRC catalog.</p>
<dt><code>attribute add &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt; &lt;value&gt;</code></p>
<dd> Add an attribute to an object, <i>object</i> should be the lfn or pfn name. <i>obj-type</i> should be one of lfn or pfn. <i>attr-type</i> should be one of date, float int, or string. If <i>&lt;value&gt;</i> is of type date then it should be in the form &quot;YYYY-MM-DD HH:MM:DD&quot;.</p>
<dt><code>attribute bulk add &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt; &lt;val&gt; &#8230;</code></p>
<dd> Bulk add attribute values.</p>
<dt><code>attribute bulk delete &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &#8230;</code></p>
<dd> Bulk delete attributes.</p>
<dt><code>attribute bulk query &lt;attr&gt; &lt;obj-type&gt; &lt;object&gt; &#8230;</code></p>
<dd> Bulk query attributes.</p>
<dt><code>attribute define &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt;</code></p>
<dd> Define new attribute.</p>
<dt><code>attribute delete &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt;</code></p>
<dd> Remove attribute from <i>object.</i></p>
<dt><code>attribute modify &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt; &lt;new value&gt;</code></p>
<dd> Modify the value of an attribute.</p>
<dt><code>attribute query &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt;</code></p>
<dd> Retrieve value of specified attribute for <i>object.</i></p>
<dt><code>attribute search &lt;attr&gt; &lt;obj-type&gt; &lt;operator&gt; &lt;attr-type&gt; &lt;value&gt;</code></p>
<dd> Search for objects which have the specified attribute matching <i>operator</i> and <i>value.</i> <i>operator</i> should be one of =, !=, &gt;, &gt;=, &lt;, &lt;=, like.</p>
<dt><code>attribute show &lt;attr&gt; &lt;obj-type&gt;</code></p>
<dd> Show attribute definition. If <i>attr</i> is a hypen (-) then all attributes are shown.</p>
<dt><code>attribute undefine &lt;attr&gt; &lt;obj-type&gt;</code></p>
<dd> Delete an attribute definition. Will return an error if any objects possess this attribute.</p>
<dt><code>bulk add &lt;lfn&gt; &lt;pfn&gt; [&lt;lfn&gt; &lt;pfn&gt; &#8230;]</code></p>
<dd> Bulk add lfn, pfn mappings.</p>
<dt><code>bulk create &lt;lfn&gt; &lt;pfn&gt; [&lt;lfn&gt; &lt;pfn&gt; &#8230;]</code></p>
<dd> Bulk create lfn, pfn mappings.</p>
<dt><code>bulk delete &lt;lfn&gt; &lt;pfn&gt; [&lt;lfn&gt; &lt;pfn&gt; &#8230;]</code></p>
<dd> Bulk delete lfn, pfn mappings.</p>
<dt><code>bulk exists lrc lfn showall|showexists|shownotexists [&lt;lfn&gt; &#8230;]</code></p>
<dd> Bulk exists lrc for lfns.</p>
<dt><code>bulk exists lrc pfn showall|showexists|shownotexists [&lt;pfn&gt; &#8230;]</code></p>
<dd> Bulk exists lrc for pfns.</p>
<dt><code>bulk exists rli lfn showall|showexists|shownotexists [&lt;lfn&gt; &#8230;]</code></p>
<dd> Bulk exists rli for lfns.</p>
<dt><code>bulk query lrc lfn [&lt;lfn&gt; &#8230;]</code></p>
<dd> Bulk query lrc for lfns.</p>
<dt><code>bulk query lrc pfn [&lt;pfn&gt; &#8230;]</code></p>
<dd> Bulk query lrc for pfns.</p>
<dt><code>bulk query rli lfn [&lt;lfn&gt; &#8230;]</code></p>
<dd> Bulk query rli for lfns.</p>
<dt><code>bulk rename lrc lfn &lt;lfn&gt; &lt;newname&gt; [&lt;lfn&gt; &lt;newname&gt; &#8230;]</code></p>
<dd> Bulk rename lfns in an LRC server. First lfn identifies original lfn, which must exist. Second newname identifies new lfn name, which must not exist. When immediate mode is on, the LRC will update the RLI with the changes.</p>
<dt><code>bulk rename lrc pfn &lt;pfn&gt; &lt;newname&gt; [&lt;pfn&gt; &lt;newname&gt; &#8230;]</code></p>
<dd> Bulk rename pfns in an LRC server. First pfn identifies original pfn, which must exist. Second newname identifies new pfn name, which must not exist.</p>
<dt><code>create &lt;lfn&gt; &lt;pfn&gt;</code></p>
<dd> Create a new <i>lfn, pfn</i> mapping in an LRC catalog.</p>
<dt><code>delete &lt;lfn&gt; &lt;pfn&gt;</code></p>
<dd> Delete a <i>lfn, pfn</i> mapping from an LRC catalog.</p>
<dt><code>exists lrc lfn &lt;lfn&gt;</code></p>
<dd> Check an LRC server for existence of <i>lfn.</i></p>
<dt><code>exists lrc pfn &lt;pfn&gt;</code></p>
<dd> Check an LRC server for existence of <i>pfn.</i></p>
<dt><code>exists rli lfn &lt;lfn&gt;</code></p>
<dd> Check an RLI server for existence of <i>lfn.</i></p>
<dt><code>exit</code></p>
<dd> Exit interactive session.</p>
<dt><code>help</code></p>
<dd> Print help message.</p>
<dt><code>query lrc lfn &lt;lfn&gt;</code></p>
<dd> Query an LRC server for mappings of <i>lfn.</i></p>
<dt><code>query lrc pfn &lt;pfn&gt;</code></p>
<dd> Query an LRC server for mappings to <i>pfn.</i></p>
<dt><code>query rli lfn &lt;lfn&gt;</code></p>
<dd> Query an RLI server for mappings of <i>lfn.</i></p>
<dt><code>query wildcard lrc lfn &lt;lfn-pattern&gt;</code></p>
<dd> Perform a wildcarded query of an LRC server for mappings of <i>lfn-pattern.</i> Patterns use the standard Unix wildcard characters, an asterisk (*) matches 0 or more characters, and a question mark (?) matches any single character.</p>
<dt><code>query wildcard lrc pfn &lt;pfn-pattern&gt;</code></p>
<dd> Query an LRC server for mappings to <i>pfn-pattern.</i> Patterns use the standard Unix wildcard characters, an asterisk (*) matches 0 or more characters, and a question mark (?) matches any single character.</p>
<dt><code>query wildcard rli lfn &lt;lfn-pattern&gt;</code></p>
<dd> Query an RLI server for mappings of <i>lfn-pattern.</i> Patterns use the standard Unix wildcard characters, an asterisk (*) matches 0 or more characters, and a question mark (?) matches any single character.</p>
<dt><code>rename lrc lfn &lt;lfn&gt; &lt;newname&gt;</code></p>
<dd> Rename a lfn in an LRC server. First lfn identifies original lfn, which must exist. Second newname identifies new lfn name, which must not exist. When immediate mode is on, the LRC will update the RLI with the change.</p>
<dt><code>rename lrc pfn &lt;pfn&gt; &lt;newname&gt;</code></p>
<dd> Rename a pfn in an LRC server. First pfn identifies original pfn, which must exist. Second newname identifies new pfn name, which must not exist.</p>
<dt><code>set reslimit &lt;limit&gt;</code></p>
<dd> Set limit on number of results returned at a time by a wildcard query. Zero means no limit.</p>
<dt><code>set timeout &lt;timeout&gt;</code></p>
<dd> Set timeout on calls to the RLS server. The default is 30 seconds.</p>
<dt><code>version</code></p>
<dd> Show version and exit.</dl>
<h2>SEEL ALSO</h2>
<p> <a href="/docs/linux/man/8-globus-rls-server/">globus-rls-server</a>(8), globus_rls_client man pages </p>
<h2>Index</h2>
