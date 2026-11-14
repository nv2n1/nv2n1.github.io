---
title: "mimedefang(8)"
name: "mimedefang"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mimedefang/"
description: "mimedefang – Sendmail MIME mail filter"
---

<p>mimedefang &#8211; Sendmail MIME mail filter</p>
<h2>Synopsis</h2>
<p><code>mimedefang prcap</code> <code>mimedefang </code>-p <i>connection</i> -m <i>mx_socket_name</i> -U <i>user</i> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>mimedefang</code> is a filter built around Sendmail 8.11&#8217;s <i>milter</i> API for mail filters. It collects each incoming message and runs a filter on the message. This is useful for deleting attachments which may be a security risk on poorly-designed systems like Microsoft Windows. <code>mimedefang</code> does not actually run the Perl filter; instead, it communicates with <code><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8), which manages a pool of persistent Perl processes. See the <code>mimedefang-multiplexor</code> man page for additional information. </p>
<h2>Options</h2>
<p>If you invoke <code>mimedefang</code> with the single argument <code>prcap</code>, it prints information about the version of Milter it is linked against and exits. Otherwise, you should invoke <code>mimedefang</code> as shown in the second line of the SYNOPSIS. </p>
<dl>
<dt><code>-U </code><i>user</i></p>
<dd>Runs <code>mimedefang</code> as <i>user</i> rather than <i>root</i>. The <i>user</i> argument must match the argument to <code>mimedefang-multiplexor</code>&#8216;s <code>-U</code> option as well. </p>
<dt><code>-y</code></p>
<dd>If the <code>-y</code> command-line option is given, MIMEDefang will call smfi_setsymlist to set the list of macros it wants. <i>This function leaked memory in versions of Sendmail prior to 8.14.4</i> so by default we do not call it. If you are running an older version of sendmail, you should explicitly set the list of macros you want in the Sendmail configuration file. </p>
<dt><code>-z </code><i>spooldir</i></p>
<dd>Set the spool directory to <i>spooldir</i>. If this option is omitted, the spool directory defaults to /var/spool/MIMEDefang. </p>
<dt><code>-p </code><i>connection</i></p>
<dd>The <code>-p</code> switch is required and specifies the <i>milter</i> connection type. Typically, you should run <code>mimedefang</code> on the same computer as <code>sendmail</code>. Therefore, you should use a UNIX-domain socket for the connection type. The suggested value for the <code>-p</code> switch is <code>mimedefang.sock</code> under the spool directory. </p>
<dt><code>-m </code><i>mx_socket_name</i></p>
<dd>Specifies the socket for communicating with <code><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8). The <i>mx_socket_name</i> specifies the path of the UNIX-domain socket. See <code><a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a></code>(8) for details. </p>
<dt><code>-b </code><i>backlog</i></p>
<dd>Sets the &quot;backlog&quot; argument to the <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) system call to <i>backlog</i>. If this option is omitted, then the operating-system default backlog is used. </p>
<dt><code>-G</code></p>
<dd>Normally, <code>mimedefang</code> uses a umask of 077 when creating the milter socket and files. If you would like the socket to be readable and writeable by the group and files to be group-readable, supply the <code>-G</code> option. This causes the umask to be 007 whenever UNIX-domain sockets are created and 027 whenever files are created. <i>Note</i>: if your milter library is too old to have the smfi_opensocket() function, the <code>-G</code> option causes <code>mimedefang</code> to use a umask of 007 throughout its execution. </p>
<p> Note that by default, /var/spool/MIMEDefang is created with mode 0700. If you use the <code>-G</code> option, you probably should change the mode to 0750. </p>
<dt><code>-d</code></p>
<dd>The <code>-d</code> switch causes <code>mimedefang</code> <i>not</i> to delete the temporary spool files it creates for incoming messages. This is for debugging purposes only and should <i>never</i> be used on a production mail server. </p>
<dt><code>-r</code></p>
<dd>Causes <code>mimedefang</code> to perform a relay check before processing any messages. It calls into a user-supplied Perl function called <code>filter_relay</code> with the IP address and host name of the sending relay. (See <code><a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a></code>(5) for details.) </p>
<dt><code>-H</code></p>
<dd>Causes <code>mimedefang</code> to perform a HELO check before processing any messages. It calls into a user-supplied Perl function called <code>filter_helo</code> with the IP address and host name of the sending relay, and the HELO argument. (See <code><a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a></code>(5) for details.) </p>
<dt><code>-s</code></p>
<dd>Causes <code>mimedefang</code> to perform a sender check before processing the message body. It calls into a user-supplied Perl function called <code>filter_sender</code> with the envelope address of the sender. (See <code><a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a></code>(5) for details.) </p>
<dt><code>-t</code></p>
<dd>Causes <code>mimedefang</code> to perform recipient checks before processing the message body. It calls into a user-supplied Perl function called <code>filter_recipient</code> with the envelope address of each recipient. (See <code><a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a></code>(5) for details.) </p>
<dt><code>-q</code></p>
<dd>Permits the multiplexor to queue new connections. See the section QUEUEING REQUESTS in the mimedefang-multiplexor man page. Note that this option and the <code>-R</code> option are mutually-exclusive. If you supply <code>-q</code>, then <code>-R</code> is ignored. </p>
<dt><code>-k</code></p>
<dd>Causes <code>mimedefang</code> <i>not</i> to delete working directories if a filter fails. This lets you obtain the message which caused the filter to fail and determine what went wrong. <code>mimedefang</code> logs the directory containing the failed message using syslog. </p>
<dt><code>-P </code><i>fileName</i></p>
<dd>Causes <code>mimedefang</code> to write its process-ID (after becoming a daemon) to the specified file. </p>
<dt><code>-R </code><i>num</i></p>
<dd>Normally, <code>mimedefang</code> tempfails a new SMTP connection if there are no free slaves. Supplying the <code>-R</code> <i>num</i> option makes <code>mimedefang</code> tempfail new connections if there are fewer than <i>num</i> free slaves, <i>unless</i> the connection is from the local host. This allows you to favour connections from localhost so your clientmqueue doesn&#8217;t build up. Note that supplying <code>-R 0</code> is subtly different from omitting the option; in this case, <code>mimedefang</code> permits new connections from localhost to queue, but not connections from other hosts (unless you also supply the <code>-q</code> option.) </p>
<p> The purpose of the <code>-R</code> option is to reserve resources for clientmqueue runs. Otherwise, on a very busy mail server, clientmqueue runs can starve for a long time, leading to delays for locally-generated or streamed mail. We recommend using a small number for <i>num</i>; probably no more than 3 or 10% of the total number of slaves (whichever is smaller.) </p>
<p> Note that this option and the <code>-q</code> option are mutually-exclusive. If you supply <code>-q</code>, then <code>-R</code> is ignored. </p>
<dt><code>-C</code></p>
<dd>Conserve file descriptors by opening and closing disk files more often. (Disk files are never held open across Milter callbacks.) While this shortens the length of time a file descriptor is open, it also leaves more opportunities for the open to fail. We do not recommend the use of this flag except on very busy systems that exhibit failures due to a shortage of file descriptors. </p>
<dt><code>-T</code></p>
<dd>Causes <code>mimedefang</code> to log the run-time of the Perl filter using syslog. </p>
<dt><code>-x </code><i>string</i></p>
<dd>Add <i>string</i> as the content of the X-Scanned-By: header. If you set <i>string</i> to the empty string (i.e. -x &quot;&quot;), then no X-Scanned-By: header will be added. </p>
<dt><code>-X</code></p>
<dd>Do not add an X-Scanned-By: header. Specifying -X is equivalent to specifying -x &quot;&quot;. </p>
<dt><code>-D</code></p>
<dd>Do not fork into the background and become a daemon. Instead, stay in the foreground. Useful mainly for debugging or if you have a supervisory process managing <code>mimedefang</code>. </p>
<dt><code>-M</code></p>
<dd>This option is obsolete; it is accepted for backward-compatibility, but is ignored. </p>
<dt><code>-N</code></p>
<dd>Normally, <code>mimedefang</code> sees all envelope recipients, even ones that Sendmail knows to be invalid. If you don&#8217;t want Sendmail to perform a milter callback for recipients it knows to be invalid, invoke <code>mimedefang</code> with the -N flag. <i>Please note that this flag only works with Sendmail and Milter 8.14.0 and newer. It has no effect if you&#8217;re running an older version of Sendmail or Milter.</i> </p>
<dt>-S <i>facility</i></p>
<dd>Specifies the syslog facility for log messages. The default is <i>mail</i>. See <code><a href="/docs/linux/man/3-openlog/">openlog</a></code>(3) for a list of valid facilities. You can use either the short name (&quot;mail&quot;) or long name (&quot;LOG_MAIL&quot;) for the facility name. </p>
<dt>-a <i>macro</i></p>
<dd>Pass the value of the specified Sendmail macro through to the Perl filter. You can repeat the -a option to write more macros than the built-in defaults. Note that in addition to asking <code>mimedefang</code> to pass the macro value to the filter, you must configure Sendmail to pass the macro through to <code>mimedefang</code> using the confMILTER_MACROS_ENVFROM definition in Sendmail&#8217;s m4 configuration file. </p>
<dt><code>-c</code></p>
<dd>Strip &quot;bare&quot; carriage-returns (CR) characters from the message body. A bare CR should never appear in an e-mail message. Older versions of <code>mimedefang</code> used to strip them out automatically, but now they are left in by default. The <code>-c</code> option enables the older behavior.</p>
<dt><code>-h</code></p>
<dd>Print usage information and exit. </p>
</dl>
<h2>Operation</h2>
<p>When <code>mimedefang</code> starts, it connects to <code>sendmail</code> using the <i>milter</i> API. (See the Sendmail 8.11 documentation.) For each incoming message, <code>mimedefang</code> creates a temporary directory and saves information in the directory. At various phases during the SMTP conversation, <code>mimedefang</code> communicates with <code>mimedefang-multiplexor</code> to perform various operations. <code>mimedefang-multiplexor</code> manages a pool of persistent Perl processes that actually perform the mail scanning operations. </p>
<p> When a Perl process scans an e-mail, the temporary spool directory contains certain files; details of the communication protocol between <code>mimedefang</code> and the Perl script are in <code><a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a></code>(7).</p>
<h2>Warnings</h2>
<p><code>mimedefang</code> does violence to the flow of e-mail. The Perl filter is quite picky and assumes that MIME e-mail messages are well-formed. While I have tried to make the script safe, I take <i>no responsibility</i> for lost or mangled e-mail messages or any security holes this script may introduce.</p>
<h2>Author</h2>
<p><code>mimedefang</code> was written by Dianne Skoll &lt;dfs [at] roaringpenguin.com&gt;. The <code>mimedefang</code> home page is <i><a rel="nofollow" href="http://www.mimedefang.org/">http://www.mimedefang.org/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mimedefang-pl/">mimedefang.pl</a>(8), <a href="/docs/linux/man/5-mimedefang-filter/">mimedefang-filter</a>(5), <a href="/docs/linux/man/8-mimedefang-multiplexor/">mimedefang-multiplexor</a>(8), <a href="/docs/linux/man/7-mimedefang-protocol/">mimedefang-protocol</a>(7) </p>
