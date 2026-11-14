---
title: "cl-dump(1)"
name: "cl-dump"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cl-dump/"
description: "cl-dump – Dump and decode Directory Server replication change log"
---

<h2 class="name">NAME</h2>
<p> cl-dump &#8211; Dump and decode Directory Server replication change log </p>
<h2>SYNOPSIS</h2>
<p> <code>cl-dump</code> [<i>-h host</i>] [<i>-p port</i>] [<i>-D bind-dn</i>] -w bind-password | -P bind-cert<br />
&nbsp;<wbr>[<i>-r replica-roots</i>]&nbsp;<wbr>[<i>-o output-file</i>]&nbsp;<wbr>[<i>-c</i>]&nbsp;<wbr>[<i>-v</i>] </p>
<p> <code>cl-dump</code> -i changelog-ldif-file-with-base64encoding [<i>-o output-file</i>] [<i>-c</i>] </p>
<h2>DESCRIPTION</h2>
<p> Dump and decode Directory Server replication change log </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-c </code></p>
<dd> Dump and interpret CSN only. This option can be used with or without -i option.</p>
<dt><code>-D bind-dn</code></p>
<dd> Directory server&#8217;s bind DN. Default to &quot;cn=Directory Manager&quot; if the option is omitted.</p>
<dt><code>-h host</code></p>
<dd> Directory server&#8217;s host. Default to the server where the script is running.</p>
<dt><code>-i changelog-ldif-file-with-base64encoding</code></p>
<dd> If you already have a ldif-like changelog, but the changes in that file are encoded, you may use this option to decode that ldif-like changelog.</p>
<dt><code>-o output-file</code></p>
<dd> Path name for the final result. Default to STDOUT if omitted.</p>
<dt><code>-p port</code></p>
<dd> Directory server&#8217;s port. Default to 389.</p>
<dt><code>-P bind-cert</code></p>
<dd> Pathname of binding certificate DB</p>
<dt><code>-r replica-roots</code></p>
<dd> Specify replica roots whose changelog you want to dump. The replica roots may be separated by comma. All the replica roots would be dumped if the option is omitted.</p>
<dt><code>-v </code></p>
<dd> Print the version of this script.</p>
<dt><code>-w bind-password</code></p>
<dd> Password for the bind DN</dl>
<h2>RESTRICTIONS</h2>
<p> If you are not using -i option, the script should be run when the server is running, and from where the server&#8217;s changelog directory is accessible. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-repl-monitor/">repl-monitor</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> cl-dump was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
