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
<dt><code>-c</code></dt>
<dd> Set &quot;clearvalues&quot; flag when deleting an attribute (will remove any attribute value records when an attribute is deleted).</dd>
<dt><code>-d</code></dt>
<dd> Decorate the output. By default the output is presented without decorations. Using this option restores decorations in the original style.</dd>
<dt><code>-h</code></dt>
<dd> Show usage.</dd>
<dt><code>-i inputfile</code></dt>
<dd> Read bulk input parameters from the input file. Each row of the input file corresponds to an individual operation of the command. If inputfile is replaced with &#8216;-&#8216; input parameters will be read from stdin.</dd>
<dt><code>-l reslimit</code></dt>
<dd> Set limit on number of results returned by wildcard query at a time. Zero means no limit.</dd>
<dt><code>-s</code></dt>
<dd> Use SQL style wildcards (% and _).</dd>
<dt><code>-t timeout</code></dt>
<dd> Set timeout (in seconds) for RLS server requests. Default is 30 seconds.</dd>
<dt><code>-u</code></dt>
<dd> Use Unix style wildcards (* and ?).</dd>
<dt><code>-v</code></dt>
<dd> Show version.</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>add &lt;lfn&gt; &lt;pfn&gt;</code></dt>
<dd> Add <i>pfn</i> to mappings of <i>lfn</i> in an LRC catalog.</dd>
<dt><code>attribute add &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt; &lt;value&gt;</code></dt>
<dd> Add an attribute to an object, <i>object</i> should be the lfn or pfn name. <i>obj-type</i> should be one of lfn or pfn. <i>attr-type</i> should be one of date, float int, or string. If <i>&lt;value&gt;</i> is of type date then it should be in the form &quot;YYYY-MM-DD HH:MM:DD&quot;.</dd>
<dt><code>attribute bulk add &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt; &lt;val&gt; &#8230;</code></dt>
<dd> Bulk add attribute values.</dd>
<dt><code>attribute bulk delete &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &#8230;</code></dt>
<dd> Bulk delete attributes.</dd>
<dt><code>attribute bulk query &lt;attr&gt; &lt;obj-type&gt; &lt;object&gt; &#8230;</code></dt>
<dd> Bulk query attributes.</dd>
<dt><code>attribute define &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt;</code></dt>
<dd> Define new attribute.</dd>
<dt><code>attribute delete &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt;</code></dt>
<dd> Remove attribute from <i>object.</i></dd>
<dt><code>attribute modify &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt; &lt;attr-type&gt; &lt;new value&gt;</code></dt>
<dd> Modify the value of an attribute.</dd>
<dt><code>attribute query &lt;object&gt; &lt;attr&gt; &lt;obj-type&gt;</code></dt>
<dd> Retrieve value of specified attribute for <i>object.</i></dd>
<dt><code>attribute search &lt;attr&gt; &lt;obj-type&gt; &lt;operator&gt; &lt;attr-type&gt; &lt;value&gt;</code></dt>
<dd> Search for objects which have the specified attribute matching <i>operator</i> and <i>value.</i> <i>operator</i> should be one of =, !=, &gt;, &gt;=, &lt;, &lt;=, like.</dd>
<dt><code>attribute show &lt;attr&gt; &lt;obj-type&gt;</code></dt>
<dd> Show attribute definition. If <i>attr</i> is a hypen (-) then all attributes are shown.</dd>
<dt><code>attribute undefine &lt;attr&gt; &lt;obj-type&gt;</code></dt>
<dd> Delete an attribute definition. Will return an error if any objects possess this attribute.</dd>
<dt><code>bulk add &lt;lfn&gt; &lt;pfn&gt; [&lt;lfn&gt; &lt;pfn&gt; &#8230;]</code></dt>
<dd> Bulk add lfn, pfn mappings.</dd>
<dt><code>bulk create &lt;lfn&gt; &lt;pfn&gt; [&lt;lfn&gt; &lt;pfn&gt; &#8230;]</code></dt>
<dd> Bulk create lfn, pfn mappings.</dd>
<dt><code>bulk delete &lt;lfn&gt; &lt;pfn&gt; [&lt;lfn&gt; &lt;pfn&gt; &#8230;]</code></dt>
<dd> Bulk delete lfn, pfn mappings.</dd>
<dt><code>bulk exists lrc lfn showall|showexists|shownotexists [&lt;lfn&gt; &#8230;]</code></dt>
<dd> Bulk exists lrc for lfns.</dd>
<dt><code>bulk exists lrc pfn showall|showexists|shownotexists [&lt;pfn&gt; &#8230;]</code></dt>
<dd> Bulk exists lrc for pfns.</dd>
<dt><code>bulk exists rli lfn showall|showexists|shownotexists [&lt;lfn&gt; &#8230;]</code></dt>
<dd> Bulk exists rli for lfns.</dd>
<dt><code>bulk query lrc lfn [&lt;lfn&gt; &#8230;]</code></dt>
<dd> Bulk query lrc for lfns.</dd>
<dt><code>bulk query lrc pfn [&lt;pfn&gt; &#8230;]</code></dt>
<dd> Bulk query lrc for pfns.</dd>
<dt><code>bulk query rli lfn [&lt;lfn&gt; &#8230;]</code></dt>
<dd> Bulk query rli for lfns.</dd>
<dt><code>bulk rename lrc lfn &lt;lfn&gt; &lt;newname&gt; [&lt;lfn&gt; &lt;newname&gt; &#8230;]</code></dt>
<dd> Bulk rename lfns in an LRC server. First lfn identifies original lfn, which must exist. Second newname identifies new lfn name, which must not exist. When immediate mode is on, the LRC will update the RLI with the changes.</dd>
<dt><code>bulk rename lrc pfn &lt;pfn&gt; &lt;newname&gt; [&lt;pfn&gt; &lt;newname&gt; &#8230;]</code></dt>
<dd> Bulk rename pfns in an LRC server. First pfn identifies original pfn, which must exist. Second newname identifies new pfn name, which must not exist.</dd>
<dt><code>create &lt;lfn&gt; &lt;pfn&gt;</code></dt>
<dd> Create a new <i>lfn, pfn</i> mapping in an LRC catalog.</dd>
<dt><code>delete &lt;lfn&gt; &lt;pfn&gt;</code></dt>
<dd> Delete a <i>lfn, pfn</i> mapping from an LRC catalog.</dd>
<dt><code>exists lrc lfn &lt;lfn&gt;</code></dt>
<dd> Check an LRC server for existence of <i>lfn.</i></dd>
<dt><code>exists lrc pfn &lt;pfn&gt;</code></dt>
<dd> Check an LRC server for existence of <i>pfn.</i></dd>
<dt><code>exists rli lfn &lt;lfn&gt;</code></dt>
<dd> Check an RLI server for existence of <i>lfn.</i></dd>
<dt><code>exit</code></dt>
<dd> Exit interactive session.</dd>
<dt><code>help</code></dt>
<dd> Print help message.</dd>
<dt><code>query lrc lfn &lt;lfn&gt;</code></dt>
<dd> Query an LRC server for mappings of <i>lfn.</i></dd>
<dt><code>query lrc pfn &lt;pfn&gt;</code></dt>
<dd> Query an LRC server for mappings to <i>pfn.</i></dd>
<dt><code>query rli lfn &lt;lfn&gt;</code></dt>
<dd> Query an RLI server for mappings of <i>lfn.</i></dd>
<dt><code>query wildcard lrc lfn &lt;lfn-pattern&gt;</code></dt>
<dd> Perform a wildcarded query of an LRC server for mappings of <i>lfn-pattern.</i> Patterns use the standard Unix wildcard characters, an asterisk (*) matches 0 or more characters, and a question mark (?) matches any single character.</dd>
<dt><code>query wildcard lrc pfn &lt;pfn-pattern&gt;</code></dt>
<dd> Query an LRC server for mappings to <i>pfn-pattern.</i> Patterns use the standard Unix wildcard characters, an asterisk (*) matches 0 or more characters, and a question mark (?) matches any single character.</dd>
<dt><code>query wildcard rli lfn &lt;lfn-pattern&gt;</code></dt>
<dd> Query an RLI server for mappings of <i>lfn-pattern.</i> Patterns use the standard Unix wildcard characters, an asterisk (*) matches 0 or more characters, and a question mark (?) matches any single character.</dd>
<dt><code>rename lrc lfn &lt;lfn&gt; &lt;newname&gt;</code></dt>
<dd> Rename a lfn in an LRC server. First lfn identifies original lfn, which must exist. Second newname identifies new lfn name, which must not exist. When immediate mode is on, the LRC will update the RLI with the change.</dd>
<dt><code>rename lrc pfn &lt;pfn&gt; &lt;newname&gt;</code></dt>
<dd> Rename a pfn in an LRC server. First pfn identifies original pfn, which must exist. Second newname identifies new pfn name, which must not exist.</dd>
<dt><code>set reslimit &lt;limit&gt;</code></dt>
<dd> Set limit on number of results returned at a time by a wildcard query. Zero means no limit.</dd>
<dt><code>set timeout &lt;timeout&gt;</code></dt>
<dd> Set timeout on calls to the RLS server. The default is 30 seconds.</dd>
<dt><code>version</code></dt>
<dd> Show version and exit.</dd></dl>
<h2>SEEL ALSO</h2>
<p> <a href="/docs/linux/man/8-globus-rls-server/">globus-rls-server</a>(8), globus_rls_client man pages </p>
