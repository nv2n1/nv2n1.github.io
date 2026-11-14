---
title: "gendarme(1)"
name: "gendarme"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gendarme/"
description: "Gendarme – Rule-based code analysis for Mono::"
---

<h2>NAME</h2>
<p> Gendarme &#8211; Rule-based code analysis for Mono::</p>
<h2>SYNOPSIS</h2>
<p> <code>gendarme [&#8211;config configfile] [&#8211;set ruleset] [&#8211;log file | &#8211;xml file | &#8211;html file] [options] assemblies &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <i>Gendarme</i> is a extensible rule-based tool to find problems in .NET applications and libraries. Gendarme inspects programs and libraries that contain code in ECMA CIL format (Mono and .NET) and looks for common problems with the code, problems that compiler do not typically check or have not historically checked.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;config configfile</i></p>
<dd> Specify the configuration file. Default is &#8216;rules.xml&#8217;.</p>
<dt><i>&#8211;set ruleset</i></p>
<dd> Specify the set of rules to verify. Default is &#8216;*&#8217;.</p>
<dt><i>&#8211;log file</i></p>
<dd> Save the text output to the specified file.</p>
<dt><i>&#8211;xml file</i></p>
<dd> Save the output, formatted as XML, to the specified file.</p>
<dt><i>&#8211;html file</i></p>
<dd> Save the output, formatted as HTML, to the specified file.</p>
<dt><i>&#8211;ignore ignore-file</i></p>
<dd> Do not report the known defects that are part of the specified file.</p>
<dt><i>&#8211;limit N</i></p>
<dd> Stop reporting after N defects are found.</p>
<dt><i>&#8211;severity [all | audit[+] | low[+|-] | medium[+|-] | high[+|-] | critical[-]],&#8230;</i></p>
<dd> Filter the reported defects to include the specified severity levels. Default is &#8216;medium+&#8217; (i.e. low and audit levels are ignored).</p>
<dt><i>&#8211;confidence [all | low[+] | normal[+|-] | high[+|-] | total[-]],&#8230;</i></p>
<dd> Filter the reported defects to include the specified confidence levels. Default is &#8216;normal+&#8217; (i.e. low level is ignored).</p>
<dt><i>&#8211;quiet</i></p>
<dd> Display minimal output (results) from the runner.</p>
<dt><i>&#8211;v|verbose</i></p>
<dd> Enable debugging output. You can supply several -v to augment debugging verbosity.</p>
<dt><i>&#8211;version</i></p>
<dd> Display Gendarme&#8217;s version number. This number match the Mono release where it was released.</p>
<dt><i>assemblies &#8230;</i></p>
<dd> Specify the assemblies to verify. You can specify multiple filenames, including masks (? and *). You can also provide a file that list several assemblies (one by line) by prefixing the filename with @ on the command line.</dl>
<h2>FILES</h2>
<dl>
<dt><i>rules.xml</i></p>
<dd> This files contains a list of all the rulesets available to Gendarme. Each ruleset includes a list of assemblies in which some, or all, rules can be verified (include) or not (exclude). +.TP +.I gendarme.exe.config +Used by debug versions of Gendarme to enable logging for rules. A config +file will be generated automatically by the make file. To enable logging +for a rule add a switch using the rule&#8217;s name and set the value to 1.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>GENDARME_COLOR</i></p>
<dd> The runner will use colors when displaying defects on the console. By default colors are dark in order to display correctly on any background. You can change this default to &quot;light&quot; (lighter colors looks nice on a dark background, or &quot;none&quot; so no colors will be used. E.g. </p>
<pre>
    GENDARME_COLOR=none gendarme ...
</pre>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005-2008 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>MAILING LISTS</h2>
<p> Mailing lists are listed at the <a rel="nofollow" href="http://groups.google.com/group/gendarme">http://groups.google.com/group/gendarme</a></p>
<h2>WEB SITE</h2>
<p> <a rel="nofollow" href="http://www.mono-project.com/Gendarme">http://www.mono-project.com/Gendarme</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a>(1)</code> </p>
<h2>Index</h2>
