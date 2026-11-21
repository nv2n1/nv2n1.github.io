---

title: "repl-monitor(1)"
name: "repl-monitor"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repl-monitor/"
description: "repl-monitor – Directory Server replication monitor"
---

<p> <code>repl-monitor</code> &nbsp;<wbr>[-f configuration-file] [<i>-h host</i>] [<i>-p port</i>] [<i>-r</i>] [<i>-c connection</i>] [<i>-a alias</i>] [<i>-k color</i>] [<i>-u refresh-url</i>] [<i>-s</i>] [<i>-t refresh-interval</i>] [<i>-v</i>] </p>
<p> Outputs the status of all of the configured Directory Servers participating in replication. The servers to query for status are specified in the configuration file. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-h, &#8211;host</code> host</dt>
<dd> Hostname of DS server</dd>
<dt><code>-p, &#8211;port</code> port</dt>
<dd> TCP port</dd>
<dt><code>-f, &#8211;configfile</code> configuration-file</dt>
<dd> Configuration file</dd>
<dt><code>-c, &#8211;conn</code> connection</dt>
<dd> Uses the same format as the configfile directive</dd>
<dt><code>-a, &#8211;alias</code> alias</dt>
<dd> Uses the same format as the configfile directive</dd>
<dt><code>-k, &#8211;color</code> color</dt>
<dd> Uses the same format as the configfile directive</dd>
<dt><code>-r, &#8211;skip-header</code></dt>
<dd> Removes extra HTML tags</dd>
<dt><code>-u, &#8211;refreshurl</code> refresh url</dt>
<dd> Refresh url</dd>
<dt><code>-t, &#8211;interval</code> refresh interval</dt>
<dd> Refresh interval</dd>
<dt><code>-W, &#8211;prompt</code></dt>
<dd> Prompt for passwords</dd>
<dt><code>-s, &#8211;text</code></dt>
<dd> Print plain text report </dd>
</dl>
<h2>CONFIGURATION FILE</h2>
<p> This section describes the various directives that can be used in the configuration file.</p>
<dl>
<dt><code>[connection]</code></dt>
<dd> The connection details about a replica </dd>
<p> host:port:binddn:bindpwd:cert_file </p>
<p> or, </p>
<p> host:port=shadowport:binddn:bindpwd:cert_file</p>
<dt><code>[alias]</code></dt>
<dd> Define an alias for a server, this alias is used in the report in place of the hostname/port </dd>
<p> alias = host:port</p>
<dt><code>[color]</code></dt>
<dd> Set a color based on the replicaton lag time lowmark (in minutes) </dd>
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
