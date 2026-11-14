---
title: "visudo(8)"
name: "visudo"
section: "8"
letter: "v"
url: "/docs/linux/man/8-visudo/"
description: "visudo – edit the sudoers file"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>visudo</code> &#8211; edit the sudoers file</p>
<h2>Synopsis</h2>
<p><code>visudo</code> [-<code>chOPqsV</code> ] [Bo &#8211;<code>f Bc </code><i>sudoers</i> ]</p>
<h2>Description</h2>
<p><code>visudo</code> edits the <i>sudoers</i> file in a safe fashion, analogous to <a href="/docs/linux/man/8-vipw/">vipw</a>(8). <code>visudo</code> locks the <i>sudoers</i> file against multiple simultaneous edits, performs basic validity checks, and checks for syntax errors before installing the edited file. If the <i>sudoers</i> file is currently being edited you will receive a message to try again later. </p>
<p> <code>visudo</code> parses the <i>sudoers</i> file after editing and will not save the changes if there is a syntax error. Upon finding an error, <code>visudo</code> will print a message stating the line number(s) where the error occurred and the user will receive the &#8220;What now?&#8221; prompt. At this point the user may enter `e&#8217; to re-edit the <i>sudoers</i> file, `x&#8217; to exit without saving the changes, or `Q&#8217; to quit and save changes. The `Q&#8217; option should be used with extreme caution because if <code>visudo</code> believes there to be a syntax error, so will <code>sudo</code> If `e&#8217; is typed to edit the <i>sudoers</i> file after a syntax error has been detected, the cursor will be placed on the line where the error occurred (if the editor supports this feature). </p>
<p> There are two <i>sudoers</i> settings that determine which editor <code>visudo</code> will run.</p>
<dl>
<dt><code>editor</code></p>
<dd>A colon (`:&#8217; ) separated list of editors allowed to be used with <code>visudo.</code> <code>visudo</code> will choose the editor that matches the user&#8217;s <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> environment variable if possible, or the first editor in the list that exists and is executable. Note that <code>sudo</code> does not preserve the <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> environment variables unless they are present in the <i>env_keep</i> list or the <i>env_reset</i> option is disabled in the <i>sudoers</i> file. The default editor path is /usr/bin/editor which can be set at compile time via the <code>&#8211;with-editor</code> configure option.</p>
<dt><code>env_editor</code></p>
<dd>If set, <code>visudo</code> will use the value of the <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> environment variables before falling back on the default editor list. Note that <code>visudo</code> is typically run as root so this option may allow a user with <code>visudo</code> privileges to run arbitrary commands as root without logging. An alternative is to place a colon-separated list of &#8220;safe&#8221; editors int the <i>editor</i> variable. <code>visudo</code> will then only use <code>SUDO_EDITOR</code> <code>VISUAL</code> or <code>EDITOR</code> if they match a value specified in <i>editor</i> If the <i>env_reset</i> flag is enabled, the <code>SUDO_EDITOR</code> <code>VISUAL</code> and/or <code>EDITOR</code> environment variables must be present in the <i>env_keep</i> list for the <i>env_editor</i> flag to function when <code>visudo</code> is invoked via <code>sudo</code> The default value is <i>on</i> which can be set at compile time via the <code>&#8211;with-env-editor</code> configure option.</dl>
<p> The options are as follows:</p>
<dl>
<dt><code>-c , -check</code></p>
<dd>Enable <i>check-only</i> mode. The existing <i>sudoers</i> file (and any other files it includes) will be checked for syntax errors. If the path to the <i>sudoers</i> file was not specified, <code>visudo</code> will also check the file ownership and permissions (see the &#8211;<code>O</code> and &#8211;<code>P</code> options). A message will be printed to the standard output describing the status of <i>sudoers</i> unless the &#8211;<code>q</code> option was specified. If the check completes successfully, <code>visudo</code> will exit with a value of 0. If an error is encountered, <code>visudo</code> will exit with a value of 1.</p>
<dt><code>-f </code><i>sudoers , &#8211;</i><code>-file = </code><i>sudoers</i></p>
<dd>Specify an alternate <i>sudoers</i> file location, see below. As of version 1.8.27, the <i>sudoers</i> path can be specified without using the &#8211;<code>f</code> option.</p>
<dt><code>-h , -help</code></p>
<dd>Display a short help message to the standard output and exit.</p>
<dt><code>-O , -owner</code></p>
<dd>Enforce the default ownership (user and group) of the <i>sudoers</i> file. In edit mode, the owner of the edited file will be set to the default. In check mode (-<code>c</code> ) an error will be reported if the owner is incorrect. This option is enabled by default if the <i>sudoers</i> file was not specified.</p>
<dt><code>-P , -perms</code></p>
<dd>Enforce the default permissions (mode) of the <i>sudoers</i> file. In edit mode, the permissions of the edited file will be set to the default. In check mode (-<code>c</code> ) an error will be reported if the file permissions are incorrect. This option is enabled by default if the <i>sudoers</i> file was not specified.</p>
<dt><code>-q , -quiet</code></p>
<dd>Enable <i>quiet</i> mode. In this mode details about syntax errors are not printed. This option is only useful when combined with the &#8211;<code>c</code> option.</p>
<dt><code>-s , -strict</code></p>
<dd>Enable <i>strict</i> checking of the <i>sudoers</i> file. If an alias is referenced but not actually defined or if there is a cycle in an alias, <code>visudo</code> will consider this a syntax error. Note that it is not possible to differentiate between an alias and a host name or user name that consists solely of uppercase letters, digits, and the underscore (`_&#8217; ) character.</p>
<dt><code>-V , -version</code></p>
<dd>Print the <code>visudo</code> and <i>sudoers</i> grammar versions and exit.</dl>
<p> A <i>sudoers</i> file may be specified instead of the default, /etc/sudoers The temporary file used is the specified <i>sudoers</i> file with &#8220;.tmp&#8221; appended to it. In <i>check-only</i> mode only, `-&#8216; may be used to indicate that <i>sudoers</i> will be read from the standard input. Because the policy is evaluated in its entirety, it is not sufficient to check an individual <i>sudoers</i> include file for syntax errors.</p>
<h3>Debugging and sudoers plugin arguments</h3>
<p><code>visudo</code> versions 1.8.4 and higher support a flexible debugging framework that is configured via <code>Debug</code> lines in the sudo.conf5 file. </p>
<p> Starting with <code>sudo</code> 1.8.12, <code>visudo</code> will also parse the arguments to the <i>sudoers</i> plugin to override the default <i>sudoers</i> path name, user-ID, group-ID, and file mode. These arguments, if present, should be listed after the path to the plugin (i.e., after sudoers.so ) Multiple arguments may be specified, separated by white space. For example: </p>
<blockquote>
<pre>Plugin sudoers_policy sudoers.so sudoers_mode=0400</pre>
</blockquote>
<p> The following arguments are supported:</p>
<dl>
<dt><code>sudoers_file=pathname</code></p>
<dd>The <i>sudoers_file</i> argument can be used to override the default path to the <i>sudoers</i> file.</p>
<dt><code>sudoers_uid=user-ID</code></p>
<dd>The <i>sudoers_uid</i> argument can be used to override the default owner of the sudoers file. It should be specified as a numeric user-ID.</p>
<dt><code>sudoers_gid=group-ID</code></p>
<dd>The <i>sudoers_gid</i> argument can be used to override the default group of the sudoers file. It must be specified as a numeric group-ID (not a group name).</p>
<dt><code>sudoers_mode=mode</code></p>
<dd>The <i>sudoers_mode</i> argument can be used to override the default file mode for the sudoers file. It should be specified as an octal value.</dl>
<p> For more information on configuring sudo.conf5, please refer to its manual.</p>
<h2>Environment</h2>
<p>The following environment variables may be consulted depending on the value of the <i>editor</i> and <i>env_editor</i> <i>sudoers</i> settings:</p>
<dl>
<dt><code>SUDO_EDITOR</code></p>
<dd>Invoked by <code>visudo</code> as the editor to use</p>
<dt><code>VISUAL</code></p>
<dd>Used by <code>visudo</code> if <code>SUDO_EDITOR</code> is not set</p>
<dt><code>EDITOR</code></p>
<dd>Used by <code>visudo</code> if neither <code>SUDO_EDITOR</code> nor <code>VISUAL</code> is set</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo.conf </code></p>
<dd>Sudo front-end configuration</p>
<dt><code>/etc/sudoers </code></p>
<dd>List of who can run what</p>
<dt><code>/etc/sudoers.tmp </code></p>
<dd>Default temporary file used by visudo</dl>
<h2>Diagnostics</h2>
<p>In addition to reporting <i>sudoers</i> syntax errors, <code>visudo</code> may produce the following messages:</p>
<dl>
<dt><code>sudoers file busy, try again later.</code></p>
<dd>Someone else is currently editing the <i>sudoers</i> file.</p>
<dt><code>/etc/sudoers: Permission denied</code></p>
<dd>You didn&#8217;t run <code>visudo</code> as root.</p>
<dt><code>you do not exist in the passwd database</code></p>
<dd>Your user-ID does not appear in the system passwd database.</p>
<dt><code>Warning: {User,Runas,Host,Cmnd}_Alias referenced but not defined</code></p>
<dd>Either you are trying to use an undeclared {User,Runas,Host,Cmnd}_Alias or you have a user or host name listed that consists solely of uppercase letters, digits, and the underscore (`_&#8217; ) character. In the latter case, you can ignore the warnings Po <code>sudo</code> will not complain Pc . The message is prefixed with the path name of the <i>sudoers</i> file and the line number where the undefined alias was used. In &#8211;<code>s</code> (strict) mode these are errors, not warnings.</p>
<dt><code>Warning: unused {User,Runas,Host,Cmnd}_Alias</code></p>
<dd>The specified {User,Runas,Host,Cmnd}_Alias was defined but never used. The message is prefixed with the path name of the <i>sudoers</i> file and the line number where the unused alias was defined. You may wish to comment out or remove the unused alias.</p>
<dt><code>Warning: cycle in {User,Runas,Host,Cmnd}_Alias</code></p>
<dd>The specified {User,Runas,Host,Cmnd}_Alias includes a reference to itself, either directly or through an alias it includes. The message is prefixed with the path name of the <i>sudoers</i> file and the line number where the cycle was detected. This is only a warning unless <code>visudo</code> is run in &#8211;<code>s</code> (strict) mode as <code>sudo</code> will ignore cycles when parsing the <i>sudoers</i> file.</p>
<dt><code>unknown defaults entry name</code></p>
<dd>The <i>sudoers</i> file contains a <code>Defaults</code> setting not recognized by <code>visudo.</code></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-vi/">vi</a>(1), sudo.conf5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), <a href="/docs/linux/man/8-sudo/">sudo</a>(8), <a href="/docs/linux/man/8-vipw/">vipw</a>(8)</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Caveats</h2>
<p>There is no easy way to prevent a user from gaining a root shell if the editor used by <code>visudo</code> allows shell escapes.</p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>visudo,</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>visudo</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
