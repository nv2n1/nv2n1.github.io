---
title: "gsisftp-server(8)"
name: "gsisftp-server"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gsisftp-server/"
description: "sftp-server – SFTP server subsystem"
---

<p><code>sftp-server</code> &#8211; SFTP server subsystem</p>
<h2>Synopsis</h2>
<p><code>sftp-server</code> -words [-<code>ehR</code> ] [-<code>d </code><i>start_directory</i> ] [-<code>f </code><i>log_facility</i> ] [-<code>l </code><i>log_level</i> ] [-<code>P </code><i>blacklisted_requests</i> ] [-<code>p </code><i>whitelisted_requests</i> ] [-<code>u </code><i>umask</i> ] [-<code>m </code><i>force_file_perms</i> ]<br />
<code>sftp-server</code> &#8211;<code>Q </code><i>protocol_feature</i></p>
<h2>Description</h2>
<p><code>sftp-server</code> is a program that speaks the server side of SFTP protocol to stdout and expects client requests from stdin. <code>sftp-server</code> is not intended to be called directly, but from <a href="/docs/linux/man/8-sshd/">sshd</a>(8) using the <code>Subsystem</code> option. </p>
<p> Command-line flags to <code>sftp-server</code> should be specified in the <code>Subsystem</code> declaration. See sshd_config5 for more information. </p>
<p> Valid options are:</p>
<dl>
<dt><code>-d </code><i>start_directory</i></p>
<dd>specifies an alternate starting directory for users. The pathname may contain the following tokens that are expanded at runtime: %% is replaced by a literal &#8216;%&#8217;, %h is replaced by the home directory of the user being authenticated, and %u is replaced by the username of that user. The default is to use the user&#8217;s home directory. This option is useful in conjunction with the sshd_config5 <code>ChrootDirectory</code> option.</p>
<dt><code>-e</code></p>
<dd>Causes <code>sftp-server</code> to print logging information to stderr instead of syslog for debugging.</p>
<dt><code>-f </code><i>log_facility</i></p>
<dd>Specifies the facility code that is used when logging messages from <code>.</code> The possible values are: DAEMON, USER, AUTH, LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7. The default is AUTH.</p>
<dt><code>-h</code></p>
<dd>Displays <code>sftp-server</code> usage information.</p>
<dt><code>-l </code><i>log_level</i></p>
<dd>Specifies which messages will be logged by <code>.</code> The possible values are: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, and DEBUG3. INFO and VERBOSE log transactions that <code>sftp-server</code> performs on behalf of the client. DEBUG and DEBUG1 are equivalent. DEBUG2 and DEBUG3 each specify higher levels of debugging output. The default is ERROR.</p>
<dt><code>-P </code><i>blacklisted_requests</i></p>
<dd>Specify a comma-separated list of SFTP protocol requests that are banned by the server. <code>sftp-server</code> will reply to any blacklisted request with a failure. The &#8211;<code>Q</code> flag can be used to determine the supported request types. If both a blacklist and a whitelist are specified, then the blacklist is applied before the whitelist.</p>
<dt><code>-p </code><i>whitelisted_requests</i></p>
<dd>Specify a comma-separated list of SFTP protocol requests that are permitted by the server. All request types that are not on the whitelist will be logged and replied to with a failure message. </p>
<p> Care must be taken when using this feature to ensure that requests made implicitly by SFTP clients are permitted.</p>
<dt><code>-Q </code><i>protocol_feature</i></p>
<dd>Query protocol features supported by <code>.</code> At present the only feature that may be queried is &#8220;requests&#8221; which may be used for black or whitelisting (flags &#8211;<code>P</code> and &#8211;<code>p</code> respectively).</p>
<dt><code>-R</code></p>
<dd>Places this instance of <code>sftp-server</code> into a read-only mode. Attempts to open files for writing, as well as other operations that change the state of the filesystem, will be denied.</p>
<dt><code>-u </code><i>umask</i></p>
<dd>Sets an explicit <a href="/docs/linux/man/2-umask/">umask</a>(2) to be applied to newly-created files and directories, instead of the user&#8217;s default mask.</p>
<dt><code>-m </code><i>force_file_perms</i></p>
<dd>Sets explicit file permissions to be applied to newly-created files instead of the default or client requested mode. Numeric values include: 777, 755, 750, 666, 644, 640, etc. Option -u is ineffective if -m is set.</dl>
<p> For logging to work, <code>sftp-server</code> must be able to access /dev/log Use of <code>sftp-server</code> in a chroot configuration therefore requires that <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8) establish a logging socket inside the chroot directory.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-sftp/">sftp</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), sshd_config5, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<dl>
<dd>T. Ylonen S. Lehtinen <i>&quot;SSH File Transfer Protocol&quot;</i> draft-ietf-secsh-filexfer-02.txt October 2001 work in progress material</dl>
<h2>History</h2>
<p><code>sftp-server</code> first appeared in Ox 2.8 .</p>
<h2>Authors</h2>
<p>An Markus Friedl Aq Mt markus [at] openbsd.org</p>
