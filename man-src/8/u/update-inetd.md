---
title: "update-inetd(8)"
name: "update-inetd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-inetd/"
description: "update-inetd – create, remove, enable or disable entry in /etc/inetd.conf"
---

<p>update-inetd &#8211; create, remove, enable or disable entry in /etc/inetd.conf</p>
<h2>Synopsis</h2>
<p><code>update-inetd</code> [&#8211;file FILENAME] [&#8211;help] [&#8211;version] [&#8211;verbose] [&#8211;comment-chars CHARACTERS] [&#8211;debug] [&#8211;group GROUPNAME] &#8211;add ENTRY <code>update-inetd</code> [&#8211;file FILENAME] [&#8211;help] [&#8211;version] [&#8211;verbose] [&#8211;pattern PATTERN] [&#8211;multi] [&#8211;debug] &#8211;remove SERVICE <code>update-inetd</code> [&#8211;file FILENAME] [&#8211;help] [&#8211;version] [&#8211;verbose] [&#8211;comment-chars CHARACTERS] [&#8211;pattern PATTERN] [&#8211;multi] [&#8211;debug] &#8211;enable SERVICE <code>update-inetd</code> [&#8211;file FILENAME] [&#8211;help] [&#8211;version] [&#8211;verbose] [&#8211;comment-chars CHARACTERS] [&#8211;pattern PATTERN] [&#8211;multi] [&#8211;debug] &#8211;disable SERVICE </p>
<h2>Description</h2>
<p><code>update-inetd</code> can be used to add, remove, enable or disable entries in the <i>/etc/inetd.conf</i> file (you can specify a different file by using the <code>&#8211;file</code> option). After the <i>/etc/inetd.conf</i> file has been changed, <code>update-inetd</code> will send a SIGHUP signal to the inetd process to make sure that inetd will use the new <i>/etc/inetd.conf</i> file. For Perl scripts you can also use the Perl module <code>DebianNet.pm</code> . See <code><a href="//www.systutorials.com/docs/linux/man/3pm-DebianNet/">DebianNet</a></code>(3pm) for further information. <code>update-inetd</code> can also be used to add entries that are commented out by default. They will be treated like normal entries. That also means that if you already have an entry that is commented out you can&#8217;t add an entry for the same service without removing the old one first. In accordance with the Debian Policy, update-inetd treats entries that are prefixed with a single `#&#8217; character as commented out by a user. This means that for a user to disable a service using update-inetd, and for the service to remain disabled after upgrades, the user must run update-inetd with &#8211;comment-chars &#8216;#&#8217; (see relevant option below). Conversely, package maintainer scripts should not override the default comment chars (and when they do, they must not use &#8216;#&#8217;). Also note that &#8211;enable and &#8211;remove will not be acted upon for service entries that are commented out using anything but the value specified with &#8211;comment-chars (or the default value if none is specified). </p>
<h2>Options</h2>
<dl>
<dt><i>&#8211;version</i></p>
<dd>Print version information on standard output and exit successfully. </p>
<dt><i>&#8211;help</i></p>
<dd>Print a usage message on standard output and exit successfully. </p>
<dt><i>&#8211;verbose</i></p>
<dd>Explain what is being done. </p>
<dt><i>&#8211;debug</i></p>
<dd>Enables debugging mode. </p>
<dt><i>&#8211;file FILENAME</i></p>
<dd>Use FILENAME instead of <i>/etc/inetd.conf</i> . </p>
<dt><i>&#8211;group GROUPNAME</i></p>
<dd>Specify that the new entry should be placed in group GROUPNAME (e.g. &#8221;MAIL&quot;). If the group does not exist the entry will be placed at the end of the file. The default group is &#8221;OTHER&quot;. </p>
<dt><i>&#8211;comment-chars CHARACTERS</i></p>
<dd>update-inetd uses &#8221;#&lt;off&gt;#&nbsp;&#8221; as the default comment characters. You can use this option to specify different comment characters. This is only necessary if you have to deal with two (or more) services of the same name. If you do use this option, it is your responsibility to eventually remove the commented out entry. </p>
<dt><i>&#8211;pattern PATTERN</i></p>
<dd>This option can be used to select a service. You only need this option if you have two (or more) services of the same name. </p>
<dt><i>&#8211;multi</i></p>
<dd>If you want to disable/remove more than one entry at a time you should use this option. If you try to remove more than one entry at a time without using this option the program will show a warning and prompt the user for an explicit confirmation. </p>
<dt><i>&#8211;add ENTRY</i></p>
<dd>Add an entry to <i>/etc/inetd.conf</i> . A description of the ENTRY format can be found in the <a href="/docs/linux/man/8-inetd/">inetd</a>(8) or <a href="/docs/linux/man/5-inetd-conf/">inetd.conf</a>(5) manual pages (or just look at /etc/inetd.conf). In order to prevent the shell from changing your ENTRY definition you have to quote the ENTRY using single or double quotes. You can use tabs (the tab character or 	) and spaces to separate the fields of the ENTRY. To add the ENTRY to a specific section in the /etc/inetd.conf file please use the <code>&#8211;group</code> option in addition to the <code>&#8211;add</code> option. </p>
<p> If you are trying to add an entry which already exists update-inetd won&#8217;t add the entry. For uncommented entries it will do nothing and for entries that are commented out by the comment-chars (see option <code>&#8211;comment-chars</code> ) it will enable the existing entry. If you want to completely replace an entry just remove the entry with the <code>&#8211;remove</code> option first. </p>
<dt><i>&#8211;remove SERVICE</i></p>
<dd>Remove SERVICE (e.g. telnet) from <i>/etc/inetd.conf</i> </p>
<dt><i>&#8211;enable SERVICE</i></p>
<dd>Enable SERVICE (e.g. &#8221;ftp&quot;) in <i>/etc/inetd.conf</i> . If you want to enable more than one SERVICE you can use a comma separated list of services (no whitespace characters allowed). </p>
<dt><i>&#8211;disable SERVICE</i></p>
<dd>Disable SERVICE (e.g. &#8221;ftp&quot;) in <i>/etc/inetd.conf</i> . If you want to disable more than one SERVICE you can use a comma separated list of services (no whitespace characters allowed).</dl>
<p> In order to prevent the shell from changing your ENTRY definition you have to quote the ENTRY using single or double quotes. You can use tabs (the tab character or 	) and spaces to separate the fields of the ENTRY. If you want to enable/disable more than one SERVICE you can use a comma separated list of services (no whitespace characters allowed).</p>
<h2>Examples</h2>
<p>You&#8217;ve installed ssh (secure encrypting remote shell) and wish to disable its unencrypted cousins:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;update-inetd &#8211;comment-chars&nbsp;&#8216;#&#8217;&nbsp;&#8211;disable login,shell,exec,telnet Using a single &#8216;#&#8217; character as a comment-char prevents update-inetd to re-enable the services on package upgrades. You think the clock on your computer is often inaccurate and wish to make sure other computers cannot read it:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;update-inetd &#8211;comment-chars&nbsp;&#8216;#&#8217;&nbsp;&#8211;disable time,daytime You get the clock fixed:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;update-inetd &#8211;enable time,daytime You hear a rumor that inetd is easily crashed via a SYN attack against the time and daytime services, you want to turn off only their TCP versions, while leaving the analogous UDP services enabled:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;update-inetd &#8211;comment-chars&nbsp;&#8216;#&#8217;&nbsp;&#8211;pattern tcp &#8211;disable time,daytime You just finished writing a POP3 server and want to install the /etc/inetd.conf entry from the makefile:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;update-inetd &#8211;group MAIL &#8211;add&nbsp;\ &#8216;pop-3		stream	tcp	nowait	root	/usr/sbin/tcpd	/usr/sbin/in.pop3d&#8217; </p>
<h2>Files</h2>
<p>/etc/inetd.conf /var/run/inetd.pid</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/3pm-DebianNet/">DebianNet</a>(3pm)</p>
<h2>Author</h2>
<p>Peter Tobias, &lt;tobias [at] et-inf.fho-emden.de&gt;</p>
