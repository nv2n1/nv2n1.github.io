---
title: "userhelper(8)"
name: "userhelper"
section: "8"
letter: "u"
url: "/docs/linux/man/8-userhelper/"
description: "userhelper – A helper interface to PAM."
---

<p>userhelper &#8211; A helper interface to PAM.</p>
<h2>Synopsis</h2>
<p><code>userhelper</code> [&nbsp;<wbr>-t&nbsp;<wbr>] [&nbsp;<wbr>-w prog args&nbsp;<wbr>] [&nbsp;<wbr>-c&nbsp;<wbr>] [&nbsp;<wbr>-f full-name&nbsp;<wbr>] [&nbsp;<wbr>-o office&nbsp;<wbr>] [&nbsp;<wbr>-p office-phone&nbsp;<wbr>] [&nbsp;<wbr>-h home-phone&nbsp;<wbr>] [&nbsp;<wbr>-s shell&nbsp;<wbr>] [&nbsp;<wbr>username ] </p>
<h2>Description</h2>
<p>NOTE this program is NOT intended to be run interactively. If you want to change this information on the command line use <i><a href="/docs/linux/man/1-passwd/">passwd</a></i>(1), <i><a href="/docs/linux/man/1-chfn/">chfn</a></i>(1), or <i><a href="/docs/linux/man/1-chsh/">chsh</a></i>(1). This program provides a basic interface to change a user&#8217;s password, gecos information, and shell. The main difference between this program and its traditional equivalents is that prompts are written to standard out to make it easy for a GUI wrapper to interface to it as a child process. The output is in the form of:</p>
<dl>
<dt>&lt;number&gt; &lt;string&gt;</p>
<dd></dl>
<p> Where the number is the type of prompt returned from libpam, and the string is the prompt to give the user. The prompt numbers are as follows:</p>
<dl>
<dt>1</p>
<dd>Prompt with visible input.</p>
<dt>2</p>
<dd>Prompt with invisible input.</p>
<dt>3</p>
<dd>Suggested answer for the current prompt.</p>
<dt>4</p>
<dd>Informational message.</p>
<dt>5</p>
<dd>Error message.</p>
<dt>6</p>
<dd>Count of messages sent in this block so far.</p>
<dt>7</p>
<dd>The name of the service being used.</p>
<dt>8</p>
<dd>Whether or not the command will be executed as the user if authentication fails.</p>
<dt>9</p>
<dd>The name of the user being authenticated. </p>
<h2>Options</h2>
<dl>
<dt><i>-t</i></p>
<dd>Use text mode authentication instead of the numbered message types just described; only used with -w.</p>
<dt><i>-w</i></p>
<dd>Specify a program name to be run and arguments to be passed to it. userhelper will look in the file /etc/security/console.apps/<i>programname</i> for the name of a user to authenticate, the path of the binary to be run, and other settings described below. userhelper will then attempt to authenticate the user using PAM, specifying <i>programname</i> as the PAM service name. If authentication succeeds, the binary will be run with superuser privileges. If the configuration file specifies that PAM session management should be performed, userhelper will also open a PAM session before starting the program, and close the session when the program terminates. If authentication fails, userhelper can be configured run the program with the user&#8217;s privileges instead.</p>
<dt><i>-c </i></p>
<dd>Change the current user&#8217;s password. Note that this option cannot be used with any of the other options. This is due to the limitation in the interface to libpam.</p>
<dt><i>-f</i></p>
<dd>Specify a new Full Name.</p>
<dt><i>-o</i></p>
<dd>Specify a new Office.</p>
<dt><i>-p</i></p>
<dd>Specify a new Office Phone.</p>
<dt><i>-h</i></p>
<dd>Specify a new Home Phone.</p>
<dt><i>-s</i></p>
<dd>Specify a new shell.</dl>
<h2>Wrapper Configuration</h2>
<p>The wrapper configuration file used with <i>-w</i> contains variable assignments and file inclusions. </p>
<p> A file inclusion line has the following form:</p>
<dl>
<dd><code>. </code><i>path</i></dl>
<p> (that is a dot and a space, followed by <i>path</i>). If <i>path</i> is relative, it is interpreted relative to the directory containing the current file. The file inclusion line is interpreted by inserting contents of <i>path</i> to the current file. Nested file inclusions are possible, recursive file inclusion results in undefined behavior. </p>
<p> A variable assignment line has the following form:</p>
<dl>
<dd><i>name</i><code>=</code><i>value</i></dl>
<p> No additional white space is allowed. If <i>value</i> is surrounded by a matching pair of or <code>&#8216;</code> quotes, the quotes are removed; otherwise, the <code>\</code> characters are removed, except that <code>\</code> is replaced by a single <code>\</code>. </p>
<p> The following variables are recognized:</p>
<dl>
<dt><i>USER</i></p>
<dd>The name of the user userhelper should attempt to authenticate the invoking user as. Typically this is <i>root</i>. The special value <i>&lt;user&gt;</i> (which is also the default) indicates that userhelper should authenticate the invoking user. </p>
<p> The special value <i>&lt;none&gt;</i> indicates that access should be denied; when used in conjunction with UGROUPS, members of the given groups can authenticate but all others are given an Insufficient Rights message.</p>
<dt><i>UGROUPS</i></p>
<dd>A comma-separated list of groups whose members will be authenticated as if USER were set to the special value <i>&lt;user&gt;</i>. If the invoking user is not a member of one of these groups, the name defined in USER will be used as normal. For example, setting UGROUPS to <i>wheel</i> and USER to <i>root</i> allows members of <i>wheel</i> (traditionally used for administrative privileges) to authenticate with their own credentials and requires other users to provide the root password.</p>
<dt><i>PROGRAM</i></p>
<dd>The name of the binary to execute if authentication succeeds. This should always be specified as an absolute path. If not specified, userhelper will attempt to run /sbin/<i>programname</i> first, and failing that, it will attempt to run /usr/sbin/<i>programname</i>.</p>
<dt><i>SESSION</i></p>
<dd>Specifies whether or not userhelper should perform PAM session management when running the program. Typically this is needed if the PAM configuration uses a module such as <i>pam_xauth.so</i> to forward X11 authentication tokens for use by the program. Valid values are <i>yes</i> and <i>no</i>, with the default being <i>no</i>.</p>
<dt><i>KEEP_ENV_VARS</i></p>
<dd>A comma-separated list of names of environment variables that should be kept in the environment of the wrapped program. The environment is cleared by default and only a few selected variables are kept in the environment if they do not contain any potentially dangerous substrings.</p>
<dt><i>RETRY</i></p>
<dd>Specifies the number of times userhelper should attempt to authenticate the user if the initial attempt fails. The default value is 2, which causes userhelper to attempt to authenticate the user a total of 3 times.</p>
<dt><i>FALLBACK</i></p>
<dd>Specifies whether or not the specified binary should be run with the invoking user&#8217;s privileges if authentication fails. This option is useful for running applications which gain additional abilities when run with superuser privileges, but which are still useful when run without them.</p>
<dt><i>NOXOPTION</i></p>
<dd>The name of an option which, if passed to userhelper as an argument for the program it will run, will cause userhelper to behave as if the <i>-t</i> flag had been passed to it.</p>
<dt><i>GUI</i></p>
<dd>Specifies whether or not userhelper should use consolehelper to present graphical dialog boxes when prompting the user for information. This is the inverse of the <i>-t</i> option. Valid values are <i>yes</i> and <i>no</i>, with the default being <i>yes</i>.</p>
<dt><i>BANNER</i></p>
<dd>Specifies specific text which userhelper should present to the user when userhelper prompts for information. The default is a generic message based on the PAM service name.</p>
<dt><i>BANNER_DOMAIN</i></p>
<dd>Specifies the text domain in which translations of the banner are stored. This setting is deprecated in favor of the <i>DOMAIN</i> setting.</p>
<dt><i>DOMAIN</i></p>
<dd>Specifies the text domain in which translations of strings are stored. If this setting is specified, it overrides any setting for <i>BANNER_DOMAIN</i> which may also be set.</p>
<dt><i>STARTUP_NOTIFICATION_NAME</i></p>
<dd>Specifies the startup notification name used for startup notification.</p>
<dt><i>STARTUP_NOTIFICATION_DESCRIPTION</i></p>
<dd>Specifies the startup notification name used for startup notification.</p>
<dt><i>STARTUP_NOTIFICATION_WORKSPACE</i></p>
<dd>Specifies the startup notification workspace used for startup notification.</p>
<dt><i>STARTUP_NOTIFICATION_WMCLASS</i></p>
<dd>Specifies the startup notification binary wmclass used for startup notification.</p>
<dt><i>STARTUP_NOTIFICATION_BINARY_NAME</i></p>
<dd>Specifies the startup notification binary name used for startup notification.</p>
<dt><i>STARTUP_NOTIFICATION_ICON_NAME</i></p>
<dd>Specifies the startup notification icon name used for startup notification. </p>
</dl>
<h2>Exit Status</h2>
<p>A non-zero exit status indicates an error occurred. Those errors are:</p>
<dl>
<dt>1</p>
<dd>The authentication passwords was incorrect.</p>
<dt>2</p>
<dd>One or more of the GECOS fields is invalid. This occurs when there is a colon supplied in one of the fields.</p>
<dt>3</p>
<dd>Password resetting error.</p>
<dt>4</p>
<dd>Some system files are locked.</p>
<dt>5</p>
<dd>User unknown.</p>
<dt>6</p>
<dd>Insufficient rights.</p>
<dt>7</p>
<dd>Invalid call to this program.</p>
<dt>8</p>
<dd>The shell provided is not valid (i.e., does not exist in /etc/shells).</p>
<dt>9</p>
<dd>Ran out of memory.</p>
<dt>10</p>
<dd>Could not find the program.</p>
<dt>11</p>
<dd>exec failed even though program exists.</p>
<dt>12</p>
<dd>the user canceled the operation.</p>
<dt>255</p>
<dd>Unknown error.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/passwd</i></p>
<dd>The gecos and shell information is stored in this file.</p>
<dt><i>/etc/shells</i></p>
<dd>This file is checked to see if the new shell supplied is valid.</p>
<dt><i>/etc/security/console.apps/prog</i></p>
<dd>This file contains the values which will be used for the variables when userhelper is used with the <i>-w</i> flag.</p>
<dt><i>/etc/pam.d/prog</i></p>
<dd>This file contains the PAM configuration used when userhelper is used with the <i>-w</i> flag.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-userpasswd/">userpasswd</a></i>(1), <i><a href="/docs/linux/man/1-userinfo/">userinfo</a></i>(1), <i><a href="/docs/linux/man/8-consolehelper/">consolehelper</a></i>(8), <i><a href="/docs/linux/man/1-chfn/">chfn</a></i>(1), <i><a href="/docs/linux/man/1-chsh/">chsh</a></i>(1), <i><a href="/docs/linux/man/5-passwd/">passwd</a></i>(5)</p>
<h2>Author</h2>
<p>Otto Hammersmith &lt;otto [at] redhat.com&gt;<br />
 Michael K. Johnson &lt;johnsonm [at] redhat.com&gt;</p>
