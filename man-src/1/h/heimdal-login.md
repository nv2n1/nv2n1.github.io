---
title: "heimdal-login(1)"
name: "heimdal-login"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-login/"
description: "login – authenticate a user and start new session"
---

<h2 class="name">NAME</h2>
<p> <code>login</code> &#8211; authenticate a user and start new session </p>
<h2>SYNOPSIS</h2>
<p> [-<code>fp</code> ] [-<code>a </code><i>level</i> ] [-<code>h </code><i>hostname</i> ] <i>[username]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>login</code> program distributed with the Heimdal Kerberos 5 implementation, it may differ in important ways from your system version. </p>
<p> The <code>login</code> programs logs users into the system. It is intended to be run by system daemons like <a href="/docs/linux/man/8-getty/">getty</a>(8) or <a href="/docs/linux/man/8-telnetd/">telnetd</a>(8). If you are already logged in, but want to change to another user, you should use <a href="/docs/linux/man/1-su/">su</a>(1). </p>
<p> A username can be given on the command line, else one will be prompted for. </p>
<p> A password is required to login, unless the &#8211;<code>f</code> option is given (indicating that the calling program has already done proper authentication). With &#8211;<code>f</code> the user will be logged in without further questions. </p>
<p> For password authentication Kerberos 5, Kerberos 4 (if compiled in), OTP (if compiled in) and local <code>( /etc/passwd </code> passwords are supported. OTP will be used if the the user is registered to use it, and <code>login</code> is given the option &#8211;<code>a otp</code> When using OTP, a challenge is shown to the user. </p>
<p> Further options are:</p>
<dl>
<dt><code>-a </code><i>string</i></p>
<dd> Which authentication mode to use, the only supported value is currently &#8220;otp&#8221;</p>
<dt><code>-f</code></p>
<dd> Indicates that the user is already authenticated. This happens, for instance, when login is started by telnetd, and the user has proved authentic via Kerberos.</p>
<dt><code>-h </code><i>hostname</i></p>
<dd> Indicates which host the user is logging in from. This is passed from telnetd, and is entered into the login database.</p>
<dt><code>-p</code></p>
<dd> This tells <code>login</code> to preserve all environment variables. If not given, only the <code>TERM</code> and <code>TZ</code> variables are preserved. It could be a security risk to pass random variables to <code>login</code> or the user shell, so the calling daemon should make sure it only passes &#8220;safe&#8221; variables.</dl>
<p> The process of logging user in proceeds as follows. </p>
<p> First a check is made that logins are allowed at all. This usually means checking /etc/nologin If it exists, and the user trying to login is not root, the contents is printed, and then login exits. </p>
<p> Then various system parameters are set up, like changing the owner of the tty to the user, setting up signals, setting the group list, and user and group id. Also various machine specific tasks are performed. </p>
<p> Next <code>login</code> changes to the users home directory, or if that fails, to / The environment is setup, by adding some required variables (such as <code>PATH )</code> and also authentication related ones (such as <code>KRB5CCNAME )</code> If an environment file exists <code>( /etc/environment </code> variables are set according to it. </p>
<p> If one or more login message files are configured, their contents is printed to the terminal. </p>
<p> If a login time command is configured, it is executed. A logout time command can also be configured, which makes <code>login</code> fork, and wait for the user shell to exit, and then run the command. This can be used to clean up user credentials. </p>
<p> Finally, the user&#8217;s shell is executed. If the user logging in is root, and root&#8217;s login shell does not exist, a default shell (usually /bin/sh is also tried before giving up.</p>
<h2>ENVIRONMENT</h2>
<p> These environment variables are set by login (not including ones set by /etc/environment ) </p>
<dl>
<dt><code>PATH</code></p>
<dd> the default system path</p>
<dt><code>HOME</code></p>
<dd> the user&#8217;s home directory (or possibly /</p>
<dt><code>USER , LOGNAME</code></p>
<dd> both set to the username</p>
<dt><code>SHELL</code></p>
<dd> the user&#8217;s shell</p>
<dt><code>TERM , TZ</code></p>
<dd> set to whatever is passed to <code>login</code></p>
<dt><code>KRB5CCNAME</code></p>
<dd> if the password is verified via Kerberos 5, this will point to the credentials cache file</p>
<dt><code>KRBTKFILE</code></p>
<dd> if the password is verified via Kerberos 4, this will point to the ticket file</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/environment </code></p>
<dd> Contains a set of environment variables that should be set in addition to the ones above. It should contain sh-style assignments like &#8220;VARIABLE=value&#8221; Note that they are not parsed the way a shell would. No variable expansion is performed, and all strings are literal, and quotation marks should not be used. Everything after a hash mark is considered a comment. The following are all different (the last will set the variable <code>BAR</code> not <code>FOO )</code> </p>
<blockquote>
<pre>
FOO=this is a string
FOO=&quot;this is a string&quot;
BAR= FOO='this is a string'
</pre>
</blockquote>
<dt><code>/etc/login.access </code></p>
<dd> See login.access5.</p>
<dt><code>/etc/login.conf </code></p>
<dd> This is a termcap style configuration file, that contains various settings used by <code>login</code> Currently only the &#8220;default&#8221; capability record is used. The possible capability strings include: </p>
<dl>
<dt><code>environment</code></p>
<dd> This is a comma separated list of environment files that are read in the order specified. If this is missing the default /etc/environment is used.</p>
<dt><code>login_program</code></p>
<dd> This program will be executed just before the user&#8217;s shell is started. It will be called without arguments.</p>
<dt><code>logout_program</code></p>
<dd> This program will be executed just after the user&#8217;s shell has terminated. It will be called without arguments. This program will be the parent process of the spawned shell.</p>
<dt><code>motd</code></p>
<dd> A comma separated list of text files that will be printed to the user&#8217;s terminal before starting the shell. The string <code>welcome</code> works similarly, but points to a single file.</p>
<dt><code>limits</code></p>
<dd> Points to a file containing ulimit settings for various users. Syntax is inspired by what pam_limits uses, and the default is /etc/security/limits.conf</dl>
<dt><code>/etc/nologin </code></p>
<dd> If it exists, login is denied to all but root. The contents of this file is printed before login exits.</dl>
<p> Other <code>login</code> programs typically print all sorts of information by default, such as last time you logged in, if you have mail, and system message files. This version of <code>login</code> does not, so there is no reason for .hushlogin files or similar. We feel that these tasks are best left to the user&#8217;s shell, but the <code>login_program</code> facility allows for a shell independent solution, if that is desired.</p>
<h2>EXAMPLES</h2>
<p> A login.conf file could look like: </p>
<blockquote>
<pre>
default:\
        :motd=/etc/motd,/etc/motd.local:\
        :limits=/etc/limits.conf:
</pre>
</blockquote>
<p> The limits.conf file consists of a table with four whitespace separated fields. First field is a username or a groupname (prefixed with `@ )&#8217; or `*&#8217; Second field is `soft&#8217; `hard&#8217; or `-&#8216; (the last meaning both soft and hard). Third field is a limit name (such as `cpu&#8217; or `core )&#8217; Last field is the limit value (a number or `-&#8216; for unlimited). In the case of data sizes, the value is in kilobytes, and cputime is in minutes.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-su/">su</a>(1), login.access5, <a href="/docs/linux/man/8-getty/">getty</a>(8), <a href="/docs/linux/man/8-telnetd/">telnetd</a>(8)</p>
<h2>AUTHORS</h2>
<p> This login program was written for the Heimdal Kerberos 5 implementation. The login.access code was written by Wietse Venema. </p>
<h2>Index</h2>
