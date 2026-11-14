---
title: "update-inetd(1)"
name: "update-inetd"
section: "1"
letter: "u"
url: "/docs/linux/man/1-update-inetd/"
description: "update-inetd – create, remove, enable or disable entry /etc/inetd.conf"
---

<h2 class="name">NAME</h2>
<p> update-inetd &#8211; create, remove, enable or disable entry /etc/inetd.conf </p>
<h2>SYNOPSIS</h2>
<p> <code>update-inetd</code> [<i>option</i>&#8230;] <i>command</i> <i>argument</i></p>
<h2>DESCRIPTION</h2>
<p> <code>update-inetd</code> can be used to add, remove, enable or disable entries in the <i>/etc/inetd.conf</i> file (you can specify a different file by using the <code>&#8211;file</code> option). After the <i>/etc/inetd.conf</i> file has been changed, <code>update-inetd</code> will send a <font SIZE="-1"><code>SIGHUP</code></font> signal to the inetd process to make sure that inetd will use the new <i>/etc/inetd.conf</i> file. For Perl scripts you can also use the Perl module <code>DebianNet</code>. See <code><a href="//www.systutorials.com/docs/linux/man/3pm-DebianNet/">DebianNet</a></code>(3pm) for further information. <code>update-inetd</code> can also be used to add entries that are commented out by default. They will be treated like normal entries. That also means that if you already have an entry that is commented out you cannot add an entry for the same service without removing the old one first. </p>
<p> In accordance with the Debian Policy, <code>update-inetd</code> treats entries that are prefixed with a single &#8216;<code>#</code>&#8216; character as commented out by a user. This means that for a user to disable a service using <code>update-inetd</code>, and for the service to remain disabled after upgrades, the user must run <code>update-inetd</code> with <code>&#8211;comment-chars &#8216;#&#8217;</code> (see relevant option below). Conversely, package maintainer scripts should not override the default comment chars (and when they do, they must not use &#8216;<code>#</code>&#8216;). </p>
<p> Also note that <code>&#8211;enable</code> and <code>&#8211;remove</code> will not be acted upon for service entries that are commented out using anything but the value specified with <code>&#8211;comment-chars</code> (or the default value if none is specified).</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;add</code> <i>entry-line</i></p>
<dd> Add an entry to <i>/etc/inetd.conf</i>. A description of the <i>entry-line</i> format can be found in the <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) or <code><a href="/docs/linux/man/5-inetd-conf/">inetd.conf</a></code>(5) manual pages (or just look at <i>/etc/inetd.conf</i>). In order to prevent the shell from changing your <i>entry-line</i> definition you have to quote the <i>entry-line</i> using single or double quotes. You can use tabs (tab character or 	) and spaces to separate the fields of the <i>entry-line</i>. To add the <i>entry-line</i> to a specific section in the <i>/etc/inetd.conf</i> file please use the <code>&#8211;group</code> option. </p>
<p> If you are trying to add an entry which already exists, <code>update-inetd</code> will not add the entry. For uncommented entries it will do nothing and for entries that are commented out by the comment-chars (see option <code>&#8211;comment-chars</code>) it will enable the existing entry. If you want to completely replace an entry just remove the entry with the <code>&#8211;remove</code> command first.</p>
<dt><code>&#8211;remove</code> <i>entry-regex</i></p>
<dd> Remove an entry-line matching <i>entry-regex</i> (e.g. &quot;<i>telnet</i>&quot;) from <i>/etc/inetd.conf</i>. The <i>entry-regex</i> will be anchored at the beginning of the entry line.</p>
<dt><code>&#8211;enable</code> <i>service</i>[,&#8230;]</p>
<dd> Enable <i>service</i> (e.g. &quot;<i>ftp</i>&quot;) in <i>/etc/inetd.conf</i>. If you want to enable more than one <i>service</i> you can use a comma-separated list of services (no whitespace characters allowed).</p>
<dt><code>&#8211;disable</code> <i>service</i>[,&#8230;]</p>
<dd> Disable <i>service</i> (e.g. &quot;<i>ftp</i>&quot;) in <i>/etc/inetd.conf</i>. If you want to disable more than one <i>service</i> you can use a comma-separated list of services (no whitespace characters allowed).</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;group</code> <i>groupname</i></p>
<dd> Specify that the new entry should be placed in group <i>groupname</i> (e.g. &quot;<i></i><font SIZE="-1"><i>MAIL</i></font><i></i>&#8220;). If the group does not exist the entry will be placed at the end of the file. The default group is &#8221;<font SIZE="-1"><code>OTHER</code></font>&quot;. </p>
<p> This option is only relevant with the <code>&#8211;add</code> command.</p>
<dt><code>&#8211;pattern</code> <i>pattern</i></p>
<dd> This option can be used to select a service. You only need this option if you have two (or more) services of the same name. </p>
<p> This option is not relevant with the <code>&#8211;add</code> command.</p>
<dt><code>&#8211;comment-chars</code> <i>characters</i></p>
<dd> <code>update-inetd</code> uses &quot;<code>#&lt;off&gt;# </code>&quot; as the default comment characters. You can use this option to specify different comment characters. This is only necessary if you have to deal with two (or more) services of the same name. If you do use this option, it is your responsibility to eventually remove the commented out entry.</p>
<dt><code>&#8211;multi</code></p>
<dd> If you want to disable/remove more than one entry at a time you should use this option. If you try to remove more than one entry at a time without using this option the program will show a warning and prompt the user for an explicit confirmation.</p>
<dt><code>&#8211;file</code> <i>filename</i></p>
<dd> Use <i>filename</i> instead of <i>/etc/inetd.conf</i>.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Explain what is being done.</p>
<dt><code>&#8211;debug</code></p>
<dd> Enables debugging mode.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a usage message on standard output and exit successfully.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information on standard output and exit successfully.</dl>
<h2>EXAMPLES</h2>
<p> You have installed ssh (secure encrypting remote shell) and wish to disable its unencrypted cousins: </p>
<pre>
  update-inetd --comment-chars '#' --disable login,shell,exec,telnet
</pre>
<p> Using a single &#8216;<code>#</code>&#8216; character as a comment-char prevents <code>update-inetd</code> to re-enable the services on package upgrades. </p>
<p> You think the clock on your computer is often inaccurate and wish to make sure other computers cannot read it: </p>
<pre>
  update-inetd --comment-chars '#' --disable time,daytime
</pre>
<p> You get the clock fixed: </p>
<pre>
  update-inetd --enable time,daytime
</pre>
<p> You hear a rumor that inetd is easily crashed via a <font SIZE="-1">SYN</font> attack against the time and daytime services, you want to turn off only their <font SIZE="-1">TCP</font> versions, while leaving the analogous <font SIZE="-1">UDP</font> services enabled: </p>
<pre>
  update-inetd --comment-chars '#' --pattern tcp --disable time,daytime
</pre>
<p> You just finished writing a <font SIZE="-1">POP3</font> server and want to install the <i>/etc/inetd.conf</i> entry from the Makefile: </p>
<pre>
  update-inetd --group MAIL --add \
    'pop-3		stream	tcp	nowait	root	/usr/sbin/tcpd	/usr/sbin/in.pop3d'
</pre>
<h2>FILES</h2>
<p> <i>/etc/inetd.conf</i> <i>/var/run/inetd.pid</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="//www.systutorials.com/docs/linux/man/3pm-DebianNet/">DebianNet</a></code>(3pm) </p>
<h2>Index</h2>
