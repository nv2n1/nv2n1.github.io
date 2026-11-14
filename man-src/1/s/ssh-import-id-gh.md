---
title: "ssh-import-id-gh(1)"
name: "ssh-import-id-gh"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssh-import-id-gh/"
description: "ssh-import-id – retrieve one or more public keys from a public keyserver and append them to the current user’s authorized_keys file (or some other specified file)"
---

<h2 class="name">NAME</h2>
<p> <code>ssh-import-id</code> &#8211; retrieve one or more public keys from a public keyserver and append them to the current user&#8217;s authorized_keys file (or some other specified file)</p>
<h2>SYNOPSIS</h2>
<p> <code>ssh-import-id [options] USER_ID_1 [gh:USER_ID_2] &#8230; [lp:USER_ID_n]</code> </p>
<p> <code>ssh-import-id-lp USER_ID_1 [USER_ID_2] &#8230; [USER_ID_n]</code> </p>
<p> <code>ssh-import-id-gh USER_ID_1 [USER_ID_2] &#8230; [USER_ID_n]</code> </p>
<h2>OPTIONS</h2>
<p>&nbsp;-h | &#8211;help<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>usage</p>
<p>&nbsp;-o | &#8211;output F<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>write output to file&nbsp;&#8216;F&#8217;&nbsp;(default&nbsp;~/.ssh/authorized_keys, use&nbsp;&quot;-&quot;&nbsp;for standard out)</p>
<p>&nbsp;-r | &#8211;remove&nbsp;<wbr>&nbsp;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>remove keys from authorized keys file&nbsp;&#8216;F&#8217;</p>
<p>&nbsp;-u | &#8211;useragent U<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>append U to the user agent string</p>
<p>&nbsp;PROTO:USER_ID<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Protocol can be&nbsp;&#8216;lp&#8217;&nbsp;for Launchpad.net, or&nbsp;&#8216;gh&#8217;&nbsp;for Github.com</p>
<h2>DESCRIPTION</h2>
<p> This utility will securely contact a public keyserver and retrieve one or more user&#8217;s public keys, and append these to the current user&#8217;s <i>~/.ssh/authorized_keys</i> file, standard output or any other specified output file. </p>
<p> User IDs can be prepended by a protocol: </p>
<p>&nbsp;&#8211;&nbsp;<code>lp:</code>&nbsp;to use&nbsp;<i><a rel="nofollow" href="https://launchpad.net/~%s/+sshkeys">https://launchpad.net/~%s/+sshkeys</a></i><br />
&nbsp;&#8211;&nbsp;<code>gh:</code>&nbsp;to use&nbsp;<i><a rel="nofollow" href="https://api.github.com/users/%s/keys">https://api.github.com/users/%s/keys</a></i> </p>
<p> If the protocol is not explicitly specified, then <code>ssh-import-id</code> will read a URL variable string from <i>/etc/ssh/ssh_import_id</i> as installed by your package manager and configured by your system administrator. You can override this locally by exporting the string you want in a URL environment variable. If all of these are empty, then the protocol is assumed to be &quot;lp:&quot;, which was the original target implementation of this tool. </p>
<p> Any keys added will be &quot;labled&quot; with a trailing comment, &quot;# ssh-import-id PROTO:USER_ID&quot;. Revoking keys will first look for lines in the authorized keys file ending with that label. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ssh/">ssh</a></i>(1) </p>
<h2>FILES</h2>
<p> <i>/etc/ssh/ssh_import_id</i> </p>
<h2>AUTHOR</h2>
<p> This manpage and the utility was written by Dustin Kirkland &lt;dustin.kirkland [at] gmail.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
