---
title: "debiannet(3)"
name: "debiannet"
section: "3"
letter: "d"
url: "/docs/linux/man/3-debiannet/"
description: "DebianNet – create, remove, enable or disable entry in /etc/inetd."
---

<p>DebianNet &#8211; create, remove, enable or disable entry in /etc/inetd. </p>
<h2>Description</h2>
<p>You can use the functions in <code>DebianNet</code> to to add, remove, enable or disable entries in the <i>/etc/inetd.conf</i> file. After the <i>/etc/inetd.conf</i> file has been changed, a <font SIZE="-1"><code>SIGHUP</code></font> signal will be sent to the inetd process to make sure that inetd will use the new <i>/etc/inetd.conf</i> file. The functions can also be used to add entries that are commented out by default. They will be treated like normal entries. That also means that if you already have an entry that is commented out you can&#8217;t add an entry for the same service without removing the old one first. </p>
<p> The <code>DebianNet</code> functions treat entries that are commented out by a single &#8216;<code>#</code>&#8216; character as entries that have been commented out by a user. It will not change such entries. </p>
<p> For shell scripts you can also use the <code>update-inetd</code> command. See <code><a href="/docs/linux/man/8-update-inetd/">update-inetd</a></code>(8) for further information.</p>
<h2>Variables</h2>
<dl COMPACT>
<dt>$DebianNet::INETD_CONF</p>
<dd>Contains a scalar filename to use as the inetd config file (e.g. for testing purposes). </p>
<p> Defaults to <i>/etc/inetd.conf</i>.</p>
<dt>$DebianNet::SEP</p>
<dd>Contains the entry comment characters. This is only necessary if you have to deal with two (or more) services of the same name. </p>
<p> Defaults to &quot;<code>#&lt;off&gt;# </code>&quot; as the comment characters.</p>
<dt>$DebianNet::MULTI</p>
<dd>Contains a boolean that decides whether to disable/remove more than one entry at a time. If you try to remove more than one entry at a time without using this option the program will show a warning and will ask the user whether to continue. </p>
<p> Defaults to false.</p>
<dt>$DebianNet::VERBOSE</p>
<dd>Contains a boolean to select whether to explain verbosely what is being done. </p>
<p> Defaults to false.</dl>
<h2>Functions</h2>
<dl COMPACT>
<dt>$rc = DebianNet::add_service($newentry, $group)</p>
<dd>Add <tt>$newentry</tt> to the group <tt>$group</tt> of the <i>/etc/inetd.conf</i> file. If the entry already exist it will be enabled (it will also detect entries with different program options). Using <tt>$group</tt> is optional (the default group is the group <font SIZE="-1">OTHER</font>). If the group does not exist the entry will be placed at the end of the file. </p>
<p> Returns 1 on success, and -1 on failure. This function might call <code>exit</code>() due to debconf prompt answers.</p>
<dt>$rc = DebianNet::remove_service($entry)</p>
<dd>Remove <tt>$entry</tt> from <i>/etc/inetd.conf</i>. You can use a regular expression to remove the entry. </p>
<p> Returns 1 on success, and -1 on failure.</p>
<dt>$rc = DebianNet::disable_service($service, $pattern)</p>
<dd>Disable <tt>$service</tt> (e.g. &quot;<i>ftp</i>&quot;) in <i>/etc/inetd.conf</i>. Using <tt>$pattern</tt> is optional (see <code>enable_service()</code>). </p>
<p> Returns 1 on success, and -1 on failure.</p>
<dt>$rc = DebianNet::enable_service($service, $pattern)</p>
<dd>Enable <tt>$service</tt> (e.g. &quot;<i>ftp</i>&quot;) in <i>/etc/inetd.conf</i>. Using <tt>$pattern</tt> is optional. It can be used to select a service. You only need this option if you have two (or more) services of the same name. </p>
<p> An example: you have three <i>ftp</i> entries in the <i>/etc/inetd.conf</i> file (all disabled by default) and you want to enable the entry which uses the <i>vsftpd</i> daemon. To do this, use the pattern &quot;<i>vsftpd</i>&quot; (or any other regular expression that matches this entry). </p>
<p> Returns 1 on success, and -1 on failure.</dl>
<h2>Changes</h2>
<h3>Version 1.13</h3>
<p>New variables: <tt>$VERSION</tt>, <tt>$VERBOSE</tt>, <tt>$MULTI</tt>, <tt>$SEP</tt>, <tt>$INETD_CONF</tt>. </p>
<p> Deprecated variables: <tt>$version</tt>, <tt>$verbose</tt>, <tt>$multi</tt>, <tt>$sep</tt>, <tt>$inetdcf</tt>.</p>
