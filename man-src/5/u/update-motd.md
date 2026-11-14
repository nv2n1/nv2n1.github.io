---
title: "update-motd(5)"
name: "update-motd"
section: "5"
letter: "u"
url: "/docs/linux/man/5-update-motd/"
description: "update-motd – dynamic MOTD generation"
---

<p>update-motd &#8211; dynamic MOTD generation</p>
<h2>Synopsis</h2>
<p><code>/etc/update-motd.d/*</code> </p>
<h2>Description</h2>
<p>UNIX/Linux system adminstrators often communicate important information to console and remote users by maintaining text in the file <i>/etc/motd</i>, which is displayed by the <code><a href="/docs/linux/man/8-pam_motd/">pam_motd</a></code>(8) module on interactive shell logins. Traditionally, this file is static text, typically installed by the distribution and only updated on release upgrades, or overwritten by the local administrator with pertinent information. Ubuntu introduced the <code>update-motd</code> framework, by which the <code><a href="/docs/linux/man/5-motd/">motd</a></code>(5) is dynamically assembled from a collection of scripts at login. Executable scripts in <i>/etc/update-motd.d/*</i> are executed by <code><a href="/docs/linux/man/8-pam_motd/">pam_motd</a></code>(8) as the root user at each login, and this information is concatenated in <i>/run/motd.dynamic</i>. The order of script execution is determined by the <code><a href="/docs/linux/man/8-run-parts/">run-parts</a></code>(8) &#8211;lsbsysinit option (basically alphabetical order, with a few caveats). On Ubuntu systems, <i>/etc/motd</i> is typically a symbolic link to <i>/run/motd.dynamic</i>. </p>
<h2>Best Practices</h2>
<p>MOTD fragments must be scripts in <i>/etc/update-motd.d</i>, must be executable, and must emit information on standard out. </p>
<p> Scripts should be named named NN-xxxxxx where NN is a two digit number indicating their position in the MOTD, and xxxxxx is an appropriate name for the script. </p>
<p> Scripts must not have filename extensions, per <code><a href="/docs/linux/man/8-run-parts/">run-parts</a></code>(8) &#8211;lsbsysinit instructions. </p>
<p> Packages should add scripts directly into <i>/etc/update-motd.d</i>, rather than symlinks to other scripts, such that administrators can modify or remove these scripts and upgrades will not wipe the local changes. Consider using a simple shell script that simply calls <code>exec</code> on the external utility. </p>
<p> Long running operations (such as network calls) or resource intensive scripts should cache output, and only update that output if it is deemed expired. For instance: </p>
<p>&nbsp;<wbr>&nbsp;/etc/update-motd.d/50-news<br />
&nbsp;<wbr>&nbsp;#!/bin/sh<br />
&nbsp;<wbr>&nbsp;out=/run/foo<br />
&nbsp;<wbr>&nbsp;script=&quot;w3m -dump&nbsp;<a rel="nofollow" href="http://news.google.com/">http://news.google.com/</a>&quot;<br />
&nbsp;<wbr>&nbsp;if&nbsp;[&nbsp;-f&nbsp;&quot;$out&quot;&nbsp;];&nbsp;then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;Output exists, print it<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;echo<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cat&nbsp;&quot;$out&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;See if it&#8217;s expired, and background update<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lastrun=$(stat -c&nbsp;%Y&nbsp;&quot;$out&quot;)&nbsp;|| lastrun=0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;expiration=$(expr&nbsp;$lastrun&nbsp;+&nbsp;86400)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;[&nbsp;$(date&nbsp;+%s)&nbsp;-ge&nbsp;$expiration&nbsp;];&nbsp;then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$script&nbsp;&gt;&nbsp;&quot;$out&quot;&nbsp;&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fi<br />
&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;No cache at all, so update in the background<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$script&nbsp;&gt;&nbsp;&quot;$out&quot;&nbsp;&amp;<br />
&nbsp;<wbr>&nbsp;fi </p>
<p> Scripts should emit a blank line before output, and end with a newline character. For instance: </p>
<p>&nbsp;<wbr>&nbsp;/etc/update-motd/05-lsb-release<br />
&nbsp;<wbr>&nbsp;#!/bin/sh<br />
&nbsp;<wbr>&nbsp;echo<br />
&nbsp;<wbr>&nbsp;lsb-release -a</p>
<h2>Files</h2>
<p><i>/etc/motd</i>, <i>/run/motd.dynamic</i>, <i>/etc/update-motd.d</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-motd/">motd</a></code>(5), <code><a href="/docs/linux/man/8-pam_motd/">pam_motd</a></code>(8), <code><a href="/docs/linux/man/8-run-parts/">run-parts</a></code>(8) </p>
<h2>Author</h2>
<p>This manpage and the update-motd framework was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
