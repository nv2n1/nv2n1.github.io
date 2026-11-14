---
title: "mts-conf(5)"
name: "mts-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mts-conf/"
description: "mh-tailor, mts.conf – mail transport configuration for nmh message handler"
---

<p>mh-tailor, mts.conf &#8211; mail transport configuration for nmh message handler</p>
<h2>Description</h2>
<p>The file <i>/etc/nmh/mts.conf</i> defines run-time options for those <code>nmh</code> programs which interact (in some form) with the message transport system. At present, these (user) programs are: <code>ap</code>, <code>conflict</code>, <code>inc</code>, <code>msgchk</code>, <code>msh</code>, <code>post</code>, <code>rcvdist</code>, and <code>rcvpack</code>. </p>
<p> Each option should be given on a single line. Blank lines and lines which begin with `#&#8217; are ignored. The options available along with default values and a description of their meanings are listed below: </p>
<p> <code>mts</code>:</p>
<dl>
<dd>The mail transport method to use. The three acceptable options are <code>smtp</code> (which is the default), <code>sendmail/smtp</code>, and <code>sendmail/pipe</code>. </p>
<p> If you use <code>smtp</code>, this will enable a direct SMTP (simple mail transport protocol) interface in <code>nmh</code>. When sending mail, instead of passing the message to the mail transport agent, <code>post</code> will open a socket connection to the mail port on the machine specified in the <code>servers</code> entry. </p>
<p> If you use <code>sendmail/smtp</code>, then <code>post</code> will send messages by forking a local copy of <code>sendmail</code>. It will still speak SMTP with this local copy of <code>sendmail</code>. For backward compatibility, <code>sendmail/smtp</code> can be abbreviated to <code>sendmail</code>. </p>
<p> The third alternative, <code>sendmail/pipe</code>, also forks a local copy of <code>sendmail</code> but feeds the message directly to it, using <code>sendmail</code> <code>-t</code>. This replaces the old, undocumented <code>spost</code> mechanism and retains some of its limitations, such as lack of support for the <code>-whom</code> switch and &#8220;Dcc:&#8221; header field.</dl>
<p> <code>localname</code>:</p>
<dl>
<dd>The hostname <code>nmh</code> considers local. It should typically be a fully qualified hostname. If this is not set, depending on the version of UNIX you&#8217;re running, <code>nmh</code> will query the system for this value (e.g. uname, gethostname, etc.), and attempt to fully qualify this value. </p>
<p> If you are using POP to retrieve new messages, you may want to set this value to the name of the POP server, so that outgoing message appear to have originated on the POP server.</dl>
<p> <code>localdomain</code>:</p>
<dl>
<dd>If this is set, a `.&#8217; followed by this string will be appended to your hostname. </p>
<p> This should only be needed, if for some reason <code>nmh</code> is not able to fully qualify the hostname returned by the system (e.g. uname, gethostname, etc.).</dl>
<p> <code>clientname</code>:</p>
<dl>
<dd>This option specifies the host name that <code>nmh</code> will give in the SMTP <code>HELO</code> (and <code>EHLO</code>) command, when posting mail. If not set, the default is to use the host name that <code>nmh</code> considers local (see <code>localname</code> above). If this option is set, but empty, no <code>HELO</code> command will be given. </p>
<p> Although the <code>HELO</code> command is required by RFC 821, many SMTP servers do not require it. Early versions of <i>SendMail</i> will fail if the hostname given in the <code>HELO</code> command is the local host. Later versions of <i>SendMail</i> will complain if you omit the <code>HELO</code> command. If you run <i>SendMail</i>, find out what your system expects and set this field if needed.</dl>
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
<p> <code>spoollocking</code>: fcntl</p>
<dl>
<dd>The locking algorithm to use when opening the maildrop. Can be any one of the following: </p>
<dl>
<dd>
<pre>fcntl dot flock lockf</pre>
</dl>
</dl>
<p> <code>maildelivery</code>: /usr/libexec/nmh/maildelivery</p>
<dl>
<dd>The name of the system-wide default <i>maildelivery</i> file. See <i><a href="/docs/linux/man/1-slocal/">slocal</a></i>(1) for the details.</dl>
<p> <code>everyone</code>: 200</p>
<dl>
<dd>The highest user-id which should NOT receive mail addressed to &#8220;everyone&#8221;.</dl>
<p> <code>noshell</code>:</p>
<dl>
<dd>If set, then each user-id greater than &#8220;everyone&#8221; that has a login shell equivalent to the given value (e.g., &#8220;/bin/csh&#8221;) indicates that mail for &#8220;everyone&#8221; should not be sent to them. This is useful for handling admin, dummy, and guest logins.</dl>
<h3>SMTP support</h3>
<p>This option is only available if you set <code>mts</code> to <code>smtp</code>. </p>
<p> <code>servers</code>: localhost</p>
<dl>
<dd>A lists of hosts and networks which to look for SMTP servers when posting non-local mail. It turns out this is a major win for hosts which don&#8217;t run an message transport system. The value of <code>servers</code> should be one or more items. Each item is the name of a host which is (hopefully) running a SMTP server.</dl>
<h3>SendMail</h3>
<p>This option is only available if you set <code>mts</code> to <code>sendmail</code>. </p>
<p> <code>sendmail</code>: /usr/sbin/sendmail</p>
<dl>
<dd>The pathname to the <code>sendmail</code> program.</dl>
<h3>Post Office Protocol</h3>
<p><code>pophost</code>:</p>
<dl>
<dd>The name of the default POP service host. If this is not set, then <code>nmh</code> looks in the standard maildrop areas for waiting mail, otherwise the named POP service host is consulted.</dl>
<h3>File Locking</h3>
<p>A few words on locking: <code>nmh</code> has two main uses for locking: locking the mail spool during mail incorporation, and locking metadata files (sequence files, the context) during updates. These locking methods can be configured separately from each other. </p>
<p> For locking the mail spool, the <i>spoollocking</i> entry in <i><a href="/docs/linux/man/5-mh-tailor/">mh-tailor</a></i>(5) will control the locking algorithm to use when <code>inc</code> incorporates mail from the spool file. If no entry is given, a default based on the operating system type will be chosen. </p>
<p> For locking all other files, the <i>datalocking</i> entry in <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5) controls the locking algorithm used for all other file access. If no entry is given, the <i>fcntl</i> lock method will be chosen. </p>
<p> If you do not wish to use kernel-based locking, <i>dot</i> locking is an option available. If &#8220;&#8211;enable-lockdir=directory&#8221; is not specified at build time, lock files will be created in the directory where the file being locked resides. Otherwise, lock files will be created in the directory specified by &#8220;&#8211;enable-lockdir&#8221;. </p>
<p> Prior to installing <code>nmh</code>, you should see how locking is done at your site, and set the appropriate values.</p>
<h2>Files</h2>
<pre>^/etc/nmh/mts.conf~^nmh mts configuration file</pre>
<h2>Profile Components</h2>
<p>None</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-mh-mts/">mh-mts</a></i>(8), <i><a href="/docs/linux/man/8-post/">post</a></i>(8)</p>
<h2>Defaults</h2>
<p>As listed above. The path of the mail transport configuration file can be changed with the <code>MHMTSCONF</code> environment variable and augmented with the <code>MHMTSUSERCONF</code> environment variable, see <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5).</p>
<h2>Bugs</h2>
<p>Failure to open any mail transport configuration file is silently ignored. Therefore, it&#8217;s best to avoid dynamic creation of such a file with the intent of use via the <code>MHMTSCONF</code> or <code>MHMTSUSERCONF</code> environment variables. If such use is necessary, the ability to successfully open the file should first be verified. </p>
