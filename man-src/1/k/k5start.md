---
title: "k5start(1)"
name: "k5start"
section: "1"
letter: "k"
url: "/docs/linux/man/1-k5start/"
description: "k5start – Obtain and optionally keep active a Kerberos ticket"
---

<h2 class="name">NAME</h2>
<p> k5start &#8211; Obtain and optionally keep active a Kerberos ticket </p>
<h2>SYNOPSIS</h2>
<p> <code>k5start</code> [<code>-bFhLnPqstvx</code>] [<code>-c</code> <i>child pid file</i>] [<code>-f</code> <i>keytab</i>]<br />
&nbsp;<wbr>[<code>-g</code>&nbsp;<wbr><i>group</i>]&nbsp;<wbr>[<code>-H</code>&nbsp;<wbr><i>minutes</i>]&nbsp;<wbr>[<code>-I</code>&nbsp;<wbr><i>service instance</i>]<br />
&nbsp;<wbr>[<code>-i</code>&nbsp;<wbr><i>client instance</i>]&nbsp;<wbr>[<code>-K</code>&nbsp;<wbr><i>minutes</i>]&nbsp;<wbr>[<code>-k</code>&nbsp;<wbr><i>ticket cache</i>]<br />
&nbsp;<wbr>[<code>-l</code>&nbsp;<wbr><i>time string</i>]&nbsp;<wbr>[<code>-m</code>&nbsp;<wbr><i>mode</i>]&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>owner</i>]<br />
&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr><i>pid file</i>]&nbsp;<wbr>[<code>-r</code>&nbsp;<wbr><i>service realm</i>]&nbsp;<wbr>[<code>-S</code>&nbsp;<wbr><i>service name</i>]<br />
&nbsp;<wbr>[<code>-u</code>&nbsp;<wbr><i>client principal</i>]&nbsp;<wbr>[<i>username</i>&nbsp;<wbr>[<i>command</i>&nbsp;<wbr>&#8230;]] </p>
<p> <code>k5start</code> <code>-U</code> <code>-f</code> <i>keytab</i> [<code>-bFhLnPqstvx</code>] [<code>-c</code> <i>child pid file</i>]<br />
&nbsp;<wbr>[<code>-g</code>&nbsp;<wbr><i>group</i>]&nbsp;<wbr>[<code>-H</code>&nbsp;<wbr><i>minutes</i>]&nbsp;<wbr>[<code>-I</code>&nbsp;<wbr><i>service instance</i>]<br />
&nbsp;<wbr>[<code>-K</code>&nbsp;<wbr><i>minutes</i>]&nbsp;<wbr>[<code>-k</code>&nbsp;<wbr><i>ticket cache</i>]&nbsp;<wbr>[<code>-l</code>&nbsp;<wbr><i>time string</i>]<br />
&nbsp;<wbr>[<code>-m</code>&nbsp;<wbr><i>mode</i>]&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>owner</i>]&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr><i>pid file</i>]<br />
&nbsp;<wbr>[<code>-r</code>&nbsp;<wbr><i>service realm</i>]&nbsp;<wbr>[<code>-S</code>&nbsp;<wbr><i>service name</i>]&nbsp;<wbr>[<i>command</i>&nbsp;<wbr>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>k5start</code> obtains and caches an initial Kerberos ticket-granting ticket for a principal. <code>k5start</code> can be used as an alternative to <code>kinit</code>, but it is primarily intended to be used by programs that want to use a keytab to obtain Kerberos credentials, such as a web server that needs to authenticate to another service such as an <font SIZE="-1">LDAP</font> server. </p>
<p> Normally, the principal for which to give tickets should be specified as the first argument. <i>username</i> may be either just a principal name (including the optional instance) or a full principal and realm string. The <code>-u</code> and <code>-i</code> options can be used as an alternative mechanism for specifying the principal, but generally aren&#8217;t as convenient. If no username is given as either the first argument or the argument to the <code>-u</code> option, the client principal defaults to the Unix username of the user running <code>k5start</code> in the default local realm. </p>
<p> Optionally, a command may be given on the command line of <code>k5start</code>. If so, that command is run after Kerberos authentication (and running <code>aklog</code> if desired), with the appropriate environment variables set to point it to the right ticket cache. <code>k5start</code> will then continue running, waking up periodically to refresh credentials slightly before they would expire, until the command completes. (The frequency with which it wakes up to refresh credentials can still be controlled with the <code>-K</code> option.) To run in this mode, the principal must either be specified as a regular command-line argument or via the <code>-U</code> option; the <code>-u</code> and <code>-i</code> options may not be used. Also, a keytab must be specified with <code>-f</code> to run a specific command. </p>
<p> The command will not be run using the shell, so if you want to use shell metacharacters in the command with their special meaning, give <tt>&quot;sh -c </tt>command<tt>&quot;</tt> as the command to run and quote <i>command</i>. </p>
<p> If the command contains command-line options (like <tt>&quot;-c&quot;</tt>), put &#8212; on the command line before the beginning of the command to tell <code>k5start</code> to not parse those options as its own. </p>
<p> When running a command, <code>k5start</code> propagates <font SIZE="-1">HUP</font>, <font SIZE="-1">TERM</font>, <font SIZE="-1">INT</font>, and <font SIZE="-1">QUIT</font> signals to the child process and does not exit when those signals are received. (If the propagated signal causes the child process to exit, <code>k5start</code> will then exit.) This allows <code>k5start</code> to react properly when run under a command supervision system such as <i><a href="/docs/linux/man/8-runit/">runit</a></i>(8) or <i><a href="/docs/linux/man/8-svscan/">svscan</a></i>(8) that uses signals to control supervised commands, and to run interactive commands that should receive Ctrl-C. </p>
<p> If a running <code>k5start</code> receives an <font SIZE="-1">ALRM</font> signal, it immediately refreshes the ticket cache regardless of whether it is in danger of expiring.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> After starting, detach from the controlling terminal and run in the background. This option only makes sense in combination with <code>-K</code> or a command that <code>k5start</code> will be running and can only be used if a keytab is specified with <i>-f</i>. <code>k5start</code> will not background itself until after it does the initial authentication, so that any initial errors will be reported, but it will then redirect output to <i>/dev/null</i> and no subsequent errors will be reported. </p>
<p> If this flag is given, <code>k5start</code> will also change directories to <tt>&quot;/&quot;</tt>. All paths (such as to a command to run or a <font SIZE="-1">PID</font> file) should therefore be given as absolute, not relative, paths. </p>
<p> If used in conjunction with a command to run, that command will also run in the background and will also have its input and output redirected to <i>/dev/null</i>. It will have to report any errors via some other mechanism for the errors to be seen. </p>
<p> Note that on Mac <font SIZE="-1">OS</font> X, the default ticket cache type is per-session and using the <code>-b</code> flag will disassociate <code>k5start</code> from the existing ticket cache. When using <code>-b</code> in conjunction with <code>-K</code> on Mac <font SIZE="-1">OS</font> X, you probably also want to use the <code>-k</code> flag to specify a ticket cache file and force the use of a file cache. </p>
<p> When using this option, consider also using <code>-L</code> to report <code>k5start</code> errors to syslog.</p>
<dt><code>-c</code> <i>child pid file</i></p>
<dd> Save the process <font SIZE="-1">ID</font> (<font SIZE="-1">PID</font>) of the child process into <i>child pid file</i>. <i>child pid file</i> is created if it doesn&#8217;t exist and overwritten if it does exist. This option is only allowed when a command was given on the command line and is most useful in conjunction with <code>-b</code> to allow management of the running child process. </p>
<p> Note that, when used with <code>-b</code>, the <font SIZE="-1">PID</font> file is written out after <code>k5start</code> is backgrounded and changes its working directory to <i>/</i>, so relative paths for the <font SIZE="-1">PID</font> file will be relative to <i>/</i> (probably not what you want).</p>
<dt><code>-F</code></p>
<dd> Do not get forwardable tickets even if the local configuration says to get forwardable tickets by default. Without this flag, <code>k5start</code> does whatever the library default is.</p>
<dt><code>-f</code> <i>keytab</i></p>
<dd> Authenticate using the keytab <i>keytab</i> rather than asking for a password. A key for the client principal must be present in <i>keytab</i>.</p>
<dt><code>-g</code> <i>group</i></p>
<dd> After creating the ticket cache, change its group ownership to <i>group</i>, which may be either the name of a group or a numeric group <font SIZE="-1">ID</font>. Ticket caches are created with <tt>0600</tt> permissions by default, so this will have no useful effect unless used with <code>-m</code>.</p>
<dt><code>-H</code> <i>minutes</i></p>
<dd> Check for a happy ticket, defined as one that has a remaining lifetime of at least <i>minutes</i> minutes. If such a ticket is found, do not attempt authentication. Instead, just run the command (if one was specified) or exit immediately with status 0 (if none was). Otherwise, try to obtain a new ticket and then run the command, if any. Cannot be used with <code>-K</code>. </p>
<p> If <code>-H</code> is used with <code>-t</code>, the external program will always be run even if a ticket with a sufficient remaining lifetime was found.</p>
<dt><code>-h</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-I</code> <i>service instance</i></p>
<dd> The instance portion of the service principal. The default is the default realm of the machine. Note that unlike the client principal, a non-default service principal must be specified with <code>-I</code> and <code>-S</code>; one cannot provide the instance portion as part of the argument to <code>-S</code>.</p>
<dt><code>-i</code> <i>client instance</i></p>
<dd> Specifies the instance portion of the principal. This option doesn&#8217;t make sense except in combination with <code>-u</code>. Note that the instance can be specified as part of <i>username</i> through the normal convention of appending a slash and then the instance, so one never has to use this option.</p>
<dt><code>-K</code> <i>minutes</i></p>
<dd> Run in daemon mode to keep a ticket alive indefinitely. The program reawakens after <i>minutes</i> minutes, checks if the ticket will expire before or less than two minutes after the next scheduled check, and gets a new ticket if needed. If this option is not given but a command was given on the command line, an interval appropriate for the ticket lifetime will be used. </p>
<p> If an error occurs in refreshing the ticket cache, the wake-up interval will be shortened to one minute and the operation retried at that interval for as long as the error persists.</p>
<dt><code>-k</code> <i>ticket cache</i></p>
<dd> Use <i>ticket cache</i> as the ticket cache rather than the contents of the environment variable <font SIZE="-1">KRB5CCNAME</font> or the library default. <i>ticket cache</i> may be any ticket cache identifier recognized by the underlying Kerberos libraries. This generally supports a path to a file, with or without a leading <tt>&quot;FILE:&quot;</tt> string, but may also support other ticket cache types. </p>
<p> If any of <code>-o</code>, <code>-g</code>, or <code>-m</code> are given, <i>ticket cache</i> must be either a simple path to a file or start with <tt>&quot;FILE:&quot;</tt> or <tt>&quot;WRFILE:&quot;</tt>.</p>
<dt><code>-L</code></p>
<dd> Report messages to syslog as well as to standard output or standard error. All messages will be logged with facility <font SIZE="-1">LOG_DAEMON</font>. Regular messages that are displayed on standard output are logged with level <font SIZE="-1">LOG_NOTICE</font>. Errors that don&#8217;t cause <code>k5start</code> to terminate are logged with level <font SIZE="-1">LOG_WARNING</font>. Fatal errors are logged with level <font SIZE="-1">LOG_ERR</font>. </p>
<p> This is useful when debugging problems in combination with <code>-b</code>.</p>
<dt><code>-l</code> <i>time string</i></p>
<dd> Set the ticket lifetime. <i>time string</i> should be in a format recognized by the Kerberos libraries for specifying times, such as <tt>&quot;10h&quot;</tt> (ten hours) or <tt>&quot;10m&quot;</tt> (ten minutes). Known units are <tt>&quot;s&quot;</tt>, <tt>&quot;m&quot;</tt>, <tt>&quot;h&quot;</tt>, and <tt>&quot;d&quot;</tt>. For more information, see <i><a href="/docs/linux/man/1-kinit/">kinit</a></i>(1).</p>
<dt><code>-m</code> <i>mode</i></p>
<dd> After creating the ticket cache, change its file permissions to <i>mode</i>, which must be a file mode in octal (<tt>640</tt> or <tt>444</tt>, for example). </p>
<p> Setting a <i>mode</i> that does not allow <code>k5start</code> to read or write to the ticket cache will cause <code>k5start</code> to fail and exit when using the <code>-K</code> option or running a command.</p>
<dt><code>-n</code></p>
<dd> Ignored, present for option compatibility with the now-obsolete <code>k4start</code>.</p>
<dt><code>-o</code> <i>owner</i></p>
<dd> After creating the ticket cache, change its ownership to <i>owner</i>, which may be either the name of a user or a numeric user <font SIZE="-1">ID</font>. If <i>owner</i> is the name of a user and <code>-g</code> was not also given, also change the group ownership of the ticket cache to the default group for that user.</p>
<dt><code>-P</code></p>
<dd> Do not get proxiable tickets even if the local configuration says to get proxiable tickets by default. Without this flag, <code>k5start</code> does whatever the library default is.</p>
<dt><code>-p</code> <i>pid file</i></p>
<dd> Save the process <font SIZE="-1">ID</font> (<font SIZE="-1">PID</font>) of the running <code>k5start</code> process into <i>pid file</i>. <i>pid file</i> is created if it doesn&#8217;t exist and overwritten if it does exist. This option is most useful in conjunction with <code>-b</code> to allow management of the running <code>k5start</code> daemon. </p>
<p> Note that, when used with <code>-b</code> the <font SIZE="-1">PID</font> file is written out after <code>k5start</code> is backgrounded and changes its working directory to <i>/</i>, so relative paths for the <font SIZE="-1">PID</font> file will be relative to <i>/</i> (probably not what you want).</p>
<dt><code>-q</code></p>
<dd> Quiet. Suppresses the printing of the initial banner message saying what Kerberos principal tickets are being obtained for, and also suppresses the password prompt when the <code>-s</code> option is given.</p>
<dt><code>-r</code> <i>service realm</i></p>
<dd> The realm for the service principal. This defaults to the default local realm.</p>
<dt><code>-S</code> <i>service name</i></p>
<dd> Specifies the principal for which <code>k5start</code> is getting a service ticket. The default value is <tt>&quot;krbtgt&quot;</tt>, to obtain a ticket-granting ticket. This option (along with <code>-I</code>) may be used if one only needs access to a single service. Note that unlike the client principal, a non-default service principal must be specified with both <code>-S</code> and <code>-I</code>; one cannot provide the instance portion as part of the argument to <code>-S</code>.</p>
<dt><code>-s</code></p>
<dd> Read the password from standard input. This bypasses the normal password prompt, which means echo isn&#8217;t suppressed and input isn&#8217;t forced to be from the controlling terminal. Most uses of this option are a security risk. You normally want to use a keytab and the <code>-f</code> option instead.</p>
<dt><code>-t</code></p>
<dd> Run an external program after getting a ticket. The default use of this is to run <code>aklog</code> to get a token. If the environment variable <font SIZE="-1">KINIT_PROG</font> is set, it overrides the compiled-in default. </p>
<p> If <code>k5start</code> has been built with <font SIZE="-1">AFS</font> <i>setpag()</i> support and a command was given on the command line, <code>k5start</code> will create a new <font SIZE="-1">PAG</font> before obtaining <font SIZE="-1">AFS</font> tokens. Otherwise, it will obtain tokens in the current <font SIZE="-1">PAG</font>.</p>
<dt><code>-U</code></p>
<dd> Rather than requiring the authentication principal be given on the command line, read it from the keytab specified with <code>-f</code>. The principal will be taken from the first entry in the keytab. <code>-f</code> must be specified if this option is used. </p>
<p> When <code>-U</code> is given, <code>k5start</code> will not expect a principal name to be given on the command line, and any arguments after the options will be taken as a command to run.</p>
<dt><code>-u</code> <i>client principal</i></p>
<dd> This specifies the principal to obtain credentials as. The entire principal may be specified here, or alternatively just the first portion may be specified with this flag and the instance specified with <code>-i</code>. </p>
<p> Note that there&#8217;s normally no reason to use this flag rather than simply giving the principal on the command line as the first regular argument.</p>
<dt><code>-v</code></p>
<dd> Be verbose. This will print out a bit of additional information about what is being attempted and what the results are.</p>
<dt><code>-x</code></p>
<dd> Exit immediately on any error. Normally, when running a command or when run with the <code>-K</code> option, <code>k5start</code> keeps running even if it fails to refresh the ticket cache and will try again at the next check interval. With this option, <code>k5start</code> will instead exit.</dl>
<h2>RETURN VALUES</h2>
<p> The program exits with status 0 if it successfully gets a ticket or has a happy ticket (see <code>-H</code>). If <code>k5start</code> runs aklog or some other program <code>k5start</code> returns the exit status of that program.</p>
<h2>EXAMPLE</h2>
<p> Use the <i>/etc/krb5.keytab</i> keytab to obtain a ticket granting ticket for the principal host/example.com, putting the ticket cache in <i>/tmp/service.tkt</i>. The lifetime is 10 hours and the program wakes up every 10 minutes to check if the ticket is about to expire. </p>
<pre>
    k5start -k /tmp/service.tkt -f /etc/krb5.keytab -K 10 -l 10h \
        host/example.com
</pre>
<p> Do the same, but using the default ticket cache and run the command /usr/local/bin/auth-backup. <code>k5start</code> will continue running until the command finishes. </p>
<pre>
    k5start -f /etc/krb5.keytab -K 10 -l 10h host/example.com \
        /usr/local/bin/auth-backup
</pre>
<p> Shows the permissions of the temporary cache file created by <code>k5start</code>: </p>
<pre>
    k5start -f /etc/krb5.keytab host/example.com \
        -- sh -c 'ls -l $KRB5CCNAME'
</pre>
<p> Notice the <tt>&quot;--&quot;</tt> before the command to keep <code>k5start</code> from parsing the <tt>&quot;-c&quot;</tt> as its own option. </p>
<p> Do the same thing, but determine the principal from the keytab: </p>
<pre>
    k5start -f /etc/krb5.keytab -U -- sh -c 'ls -l $KRB5CCNAME'
</pre>
<p> Note that no principal is given before the command. </p>
<p> Starts <code>k5start</code> as a daemon using the Debian <code>start-stop-daemon</code> management program. This is the sort of line that one could put into a Debian init script: </p>
<pre><code>
start - stop - daemon-- start-- pidfile / var / run / k5start.pid-- exec / usr / local / bin / k5start-- - b - p / var / run / k5start.pid - f / etc / krb5.keytab host / example.com
</code></pre>
<p> This uses <i>/var/run/k5start.pid</i> as the <font SIZE="-1">PID</font> file and obtains host/example.com tickets from the system keytab file. <code>k5start</code> would then be stopped with: </p>
<pre>
    start-stop-daemon --stop --pidfile /var/run/k5start.pid
    rm -f /var/run/k5start.pid
</pre>
<p> This code could be added to an init script for Apache, for example, to start a <code>k5start</code> process alongside Apache to manage its Kerberos credentials.</p>
<h2>ENVIRONMENT</h2>
<p> If the environment variable <font SIZE="-1">AKLOG</font> is set, its value will be used as the program to run with <code>-t</code> rather than the default complied into <code>k5start</code>. If <font SIZE="-1">AKLOG</font> is not set and <font SIZE="-1">KINIT_PROG</font> is set, its value will be used instead. <font SIZE="-1">KINIT_PROG</font> is honored for backward compatibility but its use is not recommended due to its confusing name. </p>
<p> If no ticket file (with <code>-k</code>) or command is specified on the command line, <code>k5start</code> will use the environment variable <font SIZE="-1">KRB5CCNAME</font> to determine the location of the the ticket granting ticket. If either a command is specified or the <code>-k</code> option is used, <font SIZE="-1">KRB5CCNAME</font> will be set to point to the ticket file before running the <code>aklog</code> program or any command given on the command line.</p>
<h2>FILES</h2>
<p> The default ticket cache is determined by the underlying Kerberos libraries. The default path for aklog is determined at build time, and will normally be whichever of <code>aklog</code> or <code>afslog</code> is found in the user&#8217;s path. </p>
<p> If a command is specified and <code>-k</code> was not given, <code>k5start</code> will create a temporary ticket cache file of the form <tt>&quot;/tmp/krb5cc_%d_%s&quot;</tt> where <tt>%d</tt> is the <font SIZE="-1">UID</font> <code>k5start</code> is running as and <tt>%s</tt> is a random string.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kinit/">kinit</a></i>(1), <i><a href="/docs/linux/man/1-krenew/">krenew</a></i>(1) </p>
<p> The kstart web page at &lt;<a rel="nofollow" href="http://www.eyrie.org/~eagle/software/kstart/">http://www.eyrie.org/~eagle/software/kstart/</a>&gt; will have the current version of <code>k5start</code> and <code>krenew</code>.</p>
<h2>AUTHORS</h2>
<p> <code>k5start</code> was based on the k4start code written by Robert Morgan. It was ported to Kerberos v5 by Booker C. Bense. Additional cleanup and current maintenance are done by Russ Allbery &lt;rra [at] stanford.edu&gt;. </p>
<p> Implementations of <code>-b</code> and <code>-p</code> and the example for a Debian init script are based on code contributed by Navid Golpayegani. </p>
<h2>Index</h2>
