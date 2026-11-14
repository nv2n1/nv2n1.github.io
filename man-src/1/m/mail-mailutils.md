---
title: "mail-mailutils(1)"
name: "mail-mailutils"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mail-mailutils/"
description: "mail.mailutils – process mail messages"
---

<p>mail.mailutils &#8211; process mail messages </p>
<h2>Synopsis</h2>
<p><code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] [<i>,address/</i>&#8230;]<br />
 <code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTION/</i>&#8230;] [<i>,file/</i>]<br />
 <code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] <i>,&#8211;file /</i>[<i>,OPTION/</i>&#8230;] [<i>,file/</i>]<br />
 <code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] <i>,&#8211;file=file /</i>[<i>,OPTION/</i>&#8230;]</p>
<h2>Description</h2>
<p>GNU mail <code>&#8212;</code> process mail messages. If <code>-f</code> or <code>&#8211;file</code> is given, mail operates on the mailbox named by the first argument, or the user&#8217;s mbox, if no argument given.</p>
<dl COMPACT>
<dt><code>-A</code>, <code>&#8211;attach</code>=<i>,FILE/</i></p>
<dd>attach FILE</p>
<dt> <code>-a</code>, <code>&#8211;append</code>=<i>,HEADER/</i>: VALUE append given header to the message being sent</p>
<dt><code>&#8211;[no-]alternative</code></p>
<dd>
<dd>force multipart/alternative content type</p>
<dt><code>&#8211;attach-fd</code>=<i>,FD/</i></p>
<dd>attach from file descriptor FD</p>
<dt><code>&#8211;content-filename</code>=<i>,NAME/</i></p>
<dd>set the Content-Disposition filename parameter for the next <code>&#8211;attach</code> option</p>
<dt><code>&#8211;content-name</code>=<i>,NAME/</i></p>
<dd>set the Content-Type name parameter for the next <code>&#8211;attach</code> option</p>
<dt><code>&#8211;content-type</code>=<i>,TYPE/</i></p>
<dd>set content type for subsequent <code>&#8211;attach</code> options</p>
<dt><code>-E</code>, <code>&#8211;exec</code>=<i>,COMMAND/</i></p>
<dd>execute COMMAND</p>
<dt><code>-e</code>, <code>&#8211;exist</code></p>
<dd>return true if mail exists</p>
<dt><code>&#8211;encoding</code>=<i>,NAME/</i></p>
<dd>set encoding for subsequent <code>&#8211;attach</code> options</p>
<dt><code>-F</code>, <code>&#8211;byname</code></p>
<dd>save messages according to sender</p>
<dt><code>-H</code>, <code>&#8211;headers</code></p>
<dd>write a header summary and exit</p>
<dt><code>-i</code>, <code>&#8211;ignore</code></p>
<dd>ignore interrupts</p>
<dt><code>-M</code>, <code>&#8211;[no-]mime</code></p>
<dd>compose MIME messages</p>
<dt><code>-N</code>, <code>&#8211;nosum</code></p>
<dd>do not display initial header summary</p>
<dt><code>-n</code>, <code>&#8211;norc</code></p>
<dd>do not read the system mailrc file</p>
<dt><code>-p</code>, <code>&#8211;print</code>, <code>&#8211;read</code></p>
<dd>print all mail to standard output</p>
<dt><code>-q</code>, <code>&#8211;quit</code></p>
<dd>cause interrupts to terminate program</p>
<dt><code>-r</code>, <code>&#8211;return-address</code>=<i>,ADDRESS/</i></p>
<dd>use address as the return address when sending mail</p>
<dt><code>-s</code>, <code>&#8211;subject</code>=<i>,SUBJ/</i></p>
<dd>send a message with the given SUBJECT</p>
<dt><code>&#8211;[no-]skip-empty-attachments</code></p>
<dd>skip attachments with empty body</p>
<dt><code>-t</code>, <code>&#8211;to</code></p>
<dd>read recipients from the message header</p>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>,USER/</i></p>
<dd>operate on USER&#8217;s mailbox</p>
<dd>Global debugging settings</p>
<dt><code>&#8211;debug-level</code>=<i>,LEVEL/</i></p>
<dd>set Mailutils debugging level</p>
<dt> <code>&#8211;[no-]debug-line-info</code> show source info with debugging messages</p>
<dd>
<dd>Configuration handling</p>
<dt><code>&#8211;config-file</code>=<i>,FILE/</i></p>
<dd>load this configuration file; implies <code>&#8211;no-config</code></p>
<dt><code>&#8211;config-lint</code></p>
<dd>check configuration file syntax and exit</p>
<dt><code>&#8211;config-verbose</code></p>
<dd>verbosely log parsing of the configuration files</p>
<dt><code>&#8211;no-config</code></p>
<dd>do not load site and user configuration files</p>
<dt><code>&#8211;no-site-config</code></p>
<dd>do not load site-wide configuration file</p>
<dt><code>&#8211;no-user-config</code></p>
<dd>do not load user configuration file</p>
<dt><code>&#8211;set</code>=<i>,PARAM=VALUE/</i></p>
<dd>set configuration parameter</p>
<dd>Informational options</p>
<dt><code>&#8211;config-help</code></p>
<dd>show configuration file summary</p>
<dt><code>&#8211;show-config-options</code></p>
<dd>show compilation options</p>
<dt>-?, <code>&#8211;help</code></p>
<dd>give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd>give a short usage message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print program version</dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-mailutils [at] gnu.org&gt;.<br />
 GNU Mailutils home page: &lt;<a rel="nofollow" href="http://mailutils.org">http://mailutils.org</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2019 Free Software Foundation, inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>The complete GNU mailutils documentation is maintained as a Texinfo manual. If the <code>mailutils-doc</code> package is installed, the command</p>
<dl COMPACT>
<dd><code>info mailutils</code></dl>
<p> should give you access to the complete manual.<br />
 You can also find this manual online in the GNU mailutils webpage:<br />
 <a rel="nofollow" href="https://www.gnu.org/software/mailutils/manual/index.html.">https://www.gnu.org/software/mailutils/manual/index.html.</a><br />
 Please note this manpage was automatically generated by the Debian mailutils packagers. Do not file bugs for its content to the GNU Mailutils upstream authors.</p>
