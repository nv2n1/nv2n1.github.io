---
title: "mts(5)"
name: "mts"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mts/"
description: "mh-tailor, mts.conf – mail transport customization for nmh message handler"
---

<p>mh-tailor, mts.conf &#8211; mail transport customization for nmh message handler</p>
<h2>Synopsis</h2>
<p><i>/etc/nmh/mts.conf</i></p>
<h2>Description</h2>
<p>The file <i>/etc/nmh/mts.conf</i> defines run-time options for those <code>nmh</code> programs which interact (in some form) with the message transport system. At present, these (user) programs are: <code>ap</code>, <code>conflict</code>, <code>inc</code>, <code>msgchk</code>, <code>msh</code>, <code>post</code>, <code>rcvdist</code>, and <code>rcvpack</code>. Each option should be given on a single line. Blank lines and lines which begin with `#&#8217; are ignored. The options available along with default values and a description of their meanings are listed below: <code>mts</code>:</p>
<dl>
<dd>The mail transport method to use. The two acceptable options are <code>smtp</code> (which is the default), and <code>sendmail</code>. If you use <code>smtp</code>, this will enable a direct SMTP (simple mail transport protocol) interface in <code>nmh</code>. When sending mail, instead of passing the message to the mail transport agent, <code>post</code> will open a socket connection to the mail port on the machine specified in the <code>servers</code> entry. If you use <code>sendmail</code>, then <code>post</code> will send messages by forking a local copy of <code>sendmail</code>. Currently it will still speak SMTP with this local copy of <code>sendmail</code>.</dl>
<p> <code>localname</code>:</p>
<dl>
<dd>The hostname <code>nmh</code> considers local. It should typically be a fully qualified hostname. If this is not set, depending on the version of UNIX you&#8217;re running, <code>nmh</code> will query the system for this value (e.g. uname, gethostname, etc.), and attempt to fully qualify this value. If you are using POP to retrieve new messages, you may want to set this value to the name of the POP server, so that outgoing message appear to have originated on the POP server.</dl>
<p> <code>localdomain</code>:</p>
<dl>
<dd>If this is set, a `.&#8217; followed by this string will be appended to your hostname. This should only be needed, if for some reason <code>nmh</code> is not able to fully qualify the hostname returned by the system (e.g. uname, gethostname, etc.).</dl>
<p> <code>clientname</code>:</p>
<dl>
<dd>This option specifies the host name that <code>nmh</code> will give in the SMTP <code>HELO</code> (and <code>EHLO</code>) command, when posting mail. If not set, the default is to use the host name that <code>nmh</code> considers local (see <code>localname</code> above). If this option is set, but empty, no <code>HELO</code> command will be given. Although the /B HELO command is required by RFC-821, many SMTP servers do not require it. Early versions of <i>SendMail</i> will fail if the hostname given in the <code>HELO</code> command is the local host. Later versions of <i>SendMail</i> will complain if you omit the <code>HELO</code> command. If you run <i>SendMail</i>, find out what your system expects and set this field if needed.</dl>
<p> <code>systemname</code>:</p>
<dl>
<dd>This option is only used for UUCP mail. It specifies the name of the local host in the UUCP &#8220;domain&#8221;. If not set, depending on the version of UNIX you&#8217;re running, <code>nmh</code> will query the system for this value. This has no equivalent in the <code>nmh</code> configuration file.</dl>
<p> <code>mmdfldir</code>: /var/mail</p>
<dl>
<dd>The directory where maildrops are kept. If this option is set, but empty, the user&#8217;s home directory is used. This overrides the default value chosen at the time of compilation.</dl>
<p> <code>mmdflfil</code>:</p>
<dl>
<dd>The name of the maildrop file in the directory where maildrops are kept. If this is empty, the user&#8217;s login name is used. This overrides the default value (which is empty).</dl>
<p> <code>mmdelim1</code>: 
</p>
<dl>
<dd>The beginning-of-message delimiter for maildrops.</dl>
<p> <code>mmdelim2</code>: 
</p>
<dl>
<dd>The end-of-message delimiter for maildrops.</dl>
<p> <code>masquerade:</code></p>
<dl>
<dd>This directive controls three different types of email address masquerading. The three possible values, which may be specified in any combination on the line, separated by spaces, are &#8220;draft_from&#8221;, &#8220;mmailid&#8221;, and &#8220;username_extension&#8221;. &#8220;mmailid&#8221; was the only type of masquerading in the original MH package, and apparently stands for &#8220;masquerade mail identification&#8221;. This type of masquerading keys off of the GECOS field of the passwd file. When enabled, <code>nmh</code> will check if the user&#8217;s pw_gecos field in the passwd file is of the form:</p>
<dl>
<dd>Full Name &lt;fakeusername&gt;</dl>
<p> If it is, the internal <code>nmh</code> routines that find the username and full name of that user will return &#8220;fakeusername&#8221; and &#8220;Full Name&#8221; respectively. This is useful if you want the messages you send to always appear to come from the name of an MTA alias rather than your actual account name. For instance, many organizations set up &#8220;First.Last&#8221; sendmail aliases for all users. If this is the case, the GECOS field for each user should look like:</p>
<dl>
<dd>First [Middle] Last &lt;First.Last&gt;</dl>
<p> &#8220;username_extension&#8221;, when specified on the &#8220;masquerade:&#8221; line, allows a second type of username masquerading. If the user sets the <code>$USERNAME_EXTENSION</code> environment variable, its value will be appended to the actual login name. For instance, if I am &#8220;dan [at] company.com&#8221;, and I set <code>$USERNAME_EXTENSION</code> to &#8220;-www&#8221;, my mail will appear to come from &#8220;dan-www [at] company.com&#8221;. This is meant to interact with qmail&#8217;s &#8220;user-extension&#8221; feature, where mail sent to <i>user</i>&#8211;<i>string</i> will be delivered to <i>user</i>. Likewise, those using versions of sendmail for which &#8220;plussed user&#8221; processing is active can set <code>$USERNAME_EXTENSION</code> to &#8220;+<i>string</i>&#8221;. These MTA features are useful because they allow one to use different email addresses in different situations (to aid in automatic mail filtering or in determining where spammers got one&#8217;s address) while only actually having a single account. Note that <code>$USERNAME_EXTENSION</code> is only appended to the username when <i>post</i> is generating &#8220;[Resent-]From:&#8221; lines and the SMTP envelope &#8220;From:&#8221;. <code>inc</code>, for instance, will not try to read from a maildrop file called &#8220;dan-www&#8221; (to recall the earlier example). &#8220;draft_from&#8221; controls the most powerful type of address masquerading. Normally, when a user explicitly specifies a &#8220;From:&#8221; header in a draft, <code>nmh</code> uses it rather than constructing its own. However, to discourage email forgery, the SMTP envelope &#8220;From:&#8221; and a &#8220;Sender:&#8221; header are set to the user&#8217;s real address. When &#8220;draft_from&#8221; is turned on, though, the envelope &#8220;From:&#8221; will use the address specified in the draft, and there will be no &#8220;Sender:&#8221; header. This is useful when a user wants to pretend to be sending mail &#8220;directly&#8221; from a remote POP3 account, or when remote mail robots incorrectly use the envelope &#8220;From:&#8221; in preference to the body &#8220;From:&#8221; (or refuse to take action when the two don&#8217;t match). Note that the MTA may still reveal the user&#8217;s real identity (e.g. <code>sendmail</code>&#8216;s &#8220;X-Authentication-Warning:&#8221; header).</dl>
<p> <code>maildelivery</code>: /usr/libexec/nmh/maildelivery</p>
<dl>
<dd>The name of the system-wide default <i>maildelivery</i> file. See <code><a href="/docs/linux/man/1-slocal/">slocal</a></code>(1) for the details.</dl>
<p> <code>everyone</code>: 200</p>
<dl>
<dd>The highest user-id which should NOT receive mail addressed to &#8220;everyone&#8221;.</dl>
<p> <code>noshell</code>:</p>
<dl>
<dd>If set, then each user-id greater than &#8220;everyone&#8221; that has a login shell equivalent to the given value (e.g., &#8220;/bin/csh&#8221;) indicates that mail for &#8220;everyone&#8221; should not be sent to them. This is useful for handling admin, dummy, and guest logins.</dl>
<h3>SMTP support</h3>
<p>These options are only available if you set <code>mts</code> to <code>smtp</code>. <code>hostable</code>: /etc/nmh/hosts</p>
<dl>
<dd>The exceptions file for /etc/hosts used by <code>post</code> to try to find official names. The format of this file is quite simple:</p>
<dl>
<dt>1.</p>
<dd>Comments are surrounded by sharp (`#&#8217;) and newline.</p>
<dt>2.</p>
<dd>Words are surrounded by white space.</p>
<dt>3.</p>
<dd>The first word on the line is the official name of a host.</p>
<dt>4.</p>
<dd>All words following the official names are aliases for that host.</dl>
</dl>
<p> <code>servers</code>: localhost localnet</p>
<dl>
<dd>A lists of hosts and networks which to look for SMTP servers when posting local mail. It turns out this is a major win for hosts which don&#8217;t run an message transport system. The value of <code>servers</code> should be one or more items. Each item is the name of either a host or a net (in the latter case, precede the name of the net by a ). This list is searched when looking for a smtp server to post mail. If a host is present, the SMTP port on that host is tried. If a net is present, the SMTP port on each host in that net is tried. Note that if you are running with the BIND code, then any networks specified are ignored (sorry, the interface went away under BIND).</dl>
<h3>SendMail</h3>
<p>This option is only available if you set <code>mts</code> to <code>sendmail</code>. <code>sendmail</code>: /usr/lib/sendmail</p>
<dl>
<dd>The pathname to the <code>sendmail</code> program.</dl>
<h3>Post Office Protocol</h3>
<p>This option is only available if you have compiled <code>nmh</code> with POP support enabled (i.e., &#8220;&#8211;enable-pop&#8221;). <code>pophost</code>:</p>
<dl>
<dd>The name of the default POP service host. If this is not set, then <code>nmh</code> looks in the standard maildrop areas for waiting mail, otherwise the named POP service host is consulted.</dl>
<h3>File Locking</h3>
<p>A few words on locking: <code>nmh</code> has several methods for creating locks on files. When configuring <code>nmh</code>, you will need to decide on the locking style and locking directory (if any). The first controls the method of locking, the second says where lock files should be created. To configure <code>nmh</code> for kernel locking, use the &#8220;&#8211;with-locking=flock&#8221; configure option if you want to use the <code>flock</code> system call; use &#8220;&#8211;with-locking=lockf&#8221; if you want to use the <code>lockf</code> system call; or use &#8220;&#8211;with-locking=fcntl&#8221; if you want to use the <code>fcntl</code> system call for kernel-level locking. Instead of kernel locking, you can configure <code>nmh</code> to use dot locking by using &#8220;&#8211;with-locking=dot&#8221;. Dot locking specifies that a file should be created whose existence means &#8220;locked&#8221; and whose non-existence means &#8220;unlocked&#8221;. The name of this file is constructed by appending &#8220;.lock&#8221; to the name of the file being locked. If <code>LOCKDIR</code> is not specified, lock files will be created in the directory where the file being locked resides. Otherwise, lock files will be created in the directory specified by <code>LOCKDIR</code>. Prior to installing <code>nmh</code>, you should see how locking is done at your site, and set the appropriate values. </p>
<h2>Files</h2>
<pre>^/etc/nmh/mts.conf~^nmh mts configuration file</pre>
<h2>Profile Components</h2>
<p>None</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mh-mts/">mh-mts</a>(8), <a href="/docs/linux/man/8-post/">post</a>(8) </p>
<h2>Defaults</h2>
<p>As listed above</p>
