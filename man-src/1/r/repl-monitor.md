---
title: "repl-monitor(1)"
name: "repl-monitor"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repl-monitor/"
description: "repl-monitor – Directory Server replication monitor"
---

<h2 class="name">NAME</h2>
<p> repl-monitor &#8211; Directory Server replication monitor </p>
<h2>SYNOPSIS</h2>
<p> <code>repl-monitor</code> &nbsp;<wbr>[-f configuration-file] [<i>-h host</i>] [<i>-p port</i>] [<i>-r</i>] [<i>-c connection</i>] [<i>-a alias</i>] [<i>-k color</i>] [<i>-u refresh-url</i>] [<i>-s</i>] [<i>-t refresh-interval</i>] [<i>-v</i>] </p>
<h2>DESCRIPTION</h2>
<p> Outputs the status of all of the configured Directory Servers participating in replication. The servers to query for status are specified in the configuration file. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-h, &#8211;host</code> host</p>
<dd> Hostname of DS server</p>
<dt><code>-p, &#8211;port</code> port</p>
<dd> TCP port</p>
<dt><code>-f, &#8211;configfile</code> configuration-file</p>
<dd> Configuration file</p>
<dt><code>-c, &#8211;conn</code> connection</p>
<dd> Uses the same format as the configfile directive</p>
<dt><code>-a, &#8211;alias</code> alias</p>
<dd> Uses the same format as the configfile directive</p>
<dt><code>-k, &#8211;color</code> color</p>
<dd> Uses the same format as the configfile directive</p>
<dt><code>-r, &#8211;skip-header</code></p>
<dd> Removes extra HTML tags</p>
<dt><code>-u, &#8211;refreshurl</code> refresh url</p>
<dd> Refresh url</p>
<dt><code>-t, &#8211;interval</code> refresh interval</p>
<dd> Refresh interval</p>
<dt><code>-W, &#8211;prompt</code></p>
<dd> Prompt for passwords</p>
<dt><code>-s, &#8211;text</code></p>
<dd> Print plain text report </p>
</dl>
<h2>CONFIGURATION FILE</h2>
<p> This section describes the various directives that can be used in the configuration file.</p>
<dl>
<dt><code>[connection]</code></p>
<dd> The connection details about a replica </p>
<p> host:port:binddn:bindpwd:cert_file </p>
<p> or, </p>
<p> host:port=shadowport:binddn:bindpwd:cert_file</p>
<dt><code>[alias]</code></p>
<dd> Define an alias for a server, this alias is used in the report in place of the hostname/port </p>
<p> alias = host:port</p>
<dt><code>[color]</code></p>
<dd> Set a color based on the replicaton lag time lowmark (in minutes) </p>
</dl>
<h2>EXAMPLE</h2>
<p> Example of a configuration file: </p>
<p> [connection]<br />
 localhost.localdomain:3891:cn=directory manager:password:*<br />
 localhost2.localdomain:3892:cn=directory manager:password:* </p>
<p> [alias]<br />
 MY_SYSTEM1 = localhost.localdomain:3891<br />
 MY_SYSTEM2 = localhost2.localdomain:3892 </p>
<p> [color]<br />
 0 = #CCFFCC<br />
 5 = #FFFFCC<br />
 60 = #FFCCCC </p>
<h2>AUTHOR</h2>
<p> repl-monitor was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2016 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 Manual page updated by Mark Reynolds &lt;mreynolds [at] redhat.com&gt; 6/28/2016<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 3 with an exception for plug-in distribution. </p>
<h2>Index</h2>
