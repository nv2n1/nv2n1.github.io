---

title: "mailx(1)"
name: "mailx"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mailx/"
description: "mail.mailutils – process mail messages"
---

<p> mail.mailutils &#8211; process mail messages </p>
<h2>SYNOPSIS</h2>
<p> <code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] [<i>,address/</i>&#8230;]<br />
 <code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] [<i>,OPTION/</i>&#8230;] [<i>,file/</i>]<br />
 <code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] <i>,&#8211;file /</i>[<i>,OPTION/</i>&#8230;] [<i>,file/</i>]<br />
 <code>mail.mailutils</code> [<i>,OPTION/</i>&#8230;] <i>,&#8211;file=file /</i>[<i>,OPTION/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> GNU mail <code>&#8212;</code> process mail messages. If <code>-f</code> or <code>&#8211;file</code> is given, mail operates on the mailbox named by the first argument, or the user&#8217;s mbox, if no argument given.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;attach</code>=<i>,FILE/</i></dt>
<dd> attach FILE</dd>
<dt> <code>-a</code>, <code>&#8211;append</code>=<i>,HEADER/</i>: VALUE append given header to the message being sent</dt>
<dt><code>&#8211;[no-]alternative</code></dt>
<dd>
</dd><dd>force multipart/alternative content type</dd>
<dt><code>&#8211;attach-fd</code>=<i>,FD/</i></dt>
<dd> attach from file descriptor FD</dd>
<dt><code>&#8211;content-filename</code>=<i>,NAME/</i></dt>
<dd> set the Content-Disposition filename parameter for the next <code>&#8211;attach</code> option</dd>
<dt><code>&#8211;content-name</code>=<i>,NAME/</i></dt>
<dd> set the Content-Type name parameter for the next <code>&#8211;attach</code> option</dd>
<dt><code>&#8211;content-type</code>=<i>,TYPE/</i></dt>
<dd> set content type for subsequent <code>&#8211;attach</code> options</dd>
<dt><code>-E</code>, <code>&#8211;exec</code>=<i>,COMMAND/</i></dt>
<dd> execute COMMAND</dd>
<dt><code>-e</code>, <code>&#8211;exist</code></dt>
<dd> return true if mail exists</dd>
<dt><code>&#8211;encoding</code>=<i>,NAME/</i></dt>
<dd> set encoding for subsequent <code>&#8211;attach</code> options</dd>
<dt><code>-F</code>, <code>&#8211;byname</code></dt>
<dd> save messages according to sender</dd>
<dt><code>-H</code>, <code>&#8211;headers</code></dt>
<dd> write a header summary and exit</dd>
<dt><code>-i</code>, <code>&#8211;ignore</code></dt>
<dd> ignore interrupts</dd>
<dt><code>-M</code>, <code>&#8211;[no-]mime</code></dt>
<dd> compose MIME messages</dd>
<dt><code>-N</code>, <code>&#8211;nosum</code></dt>
<dd> do not display initial header summary</dd>
<dt><code>-n</code>, <code>&#8211;norc</code></dt>
<dd> do not read the system mailrc file</dd>
<dt><code>-p</code>, <code>&#8211;print</code>, <code>&#8211;read</code></dt>
<dd> print all mail to standard output</dd>
<dt><code>-q</code>, <code>&#8211;quit</code></dt>
<dd> cause interrupts to terminate program</dd>
<dt><code>-r</code>, <code>&#8211;return-address</code>=<i>,ADDRESS/</i></dt>
<dd> use address as the return address when sending mail</dd>
<dt><code>-s</code>, <code>&#8211;subject</code>=<i>,SUBJ/</i></dt>
<dd> send a message with the given SUBJECT</dd>
<dt><code>&#8211;[no-]skip-empty-attachments</code></dt>
<dd> skip attachments with empty body</dd>
<dt><code>-t</code>, <code>&#8211;to</code></dt>
<dd> read recipients from the message header</dd>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>,USER/</i></dt>
<dd> operate on USER&#8217;s mailbox</dd>
<dt>
</dt><dd> Global debugging settings</dd>
<dt><code>&#8211;debug-level</code>=<i>,LEVEL/</i></dt>
<dd> set Mailutils debugging level</dd>
<dt> <code>&#8211;[no-]debug-line-info</code> show source info with debugging messages</dt>
<dd>Configuration handling</dd>
<dt><code>&#8211;config-file</code>=<i>,FILE/</i></dt>
<dd> load this configuration file; implies <code>&#8211;no-config</code></dd>
<dt><code>&#8211;config-lint</code></dt>
<dd> check configuration file syntax and exit</dd>
<dt><code>&#8211;config-verbose</code></dt>
<dd> verbosely log parsing of the configuration files</dd>
<dt><code>&#8211;no-config</code></dt>
<dd> do not load site and user configuration files</dd>
<dt><code>&#8211;no-site-config</code></dt>
<dd> do not load site-wide configuration file</dd>
<dt><code>&#8211;no-user-config</code></dt>
<dd> do not load user configuration file</dd>
<dt><code>&#8211;set</code>=<i>,PARAM=VALUE/</i></dt>
<dd> set configuration parameter</dd>
<dt>
</dt><dd> Informational options</dd>
<dt><code>&#8211;config-help</code></dt>
<dd> show configuration file summary</dd>
<dt><code>&#8211;show-config-options</code></dt>
<dd> show compilation options</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd> give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd> give a short usage message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print program version</dd></dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-mailutils [at] gnu.org&gt;.<br />
 GNU Mailutils home page: &lt;<a rel="nofollow" href="http://mailutils.org">http://mailutils.org</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2019 Free Software Foundation, inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The complete GNU mailutils documentation is maintained as a Texinfo manual. If the <code>mailutils-doc</code> package is installed, the command</p>
<dl>
<dt>
</dt><dd> <code>info mailutils</code></dd></dl>
<p> should give you access to the complete manual.<br />
 You can also find this manual online in the GNU mailutils webpage:<br />
 <a rel="nofollow" href="https://www.gnu.org/software/mailutils/manual/index.html.">https://www.gnu.org/software/mailutils/manual/index.html.</a><br />
 Please note this manpage was automatically generated by the Debian mailutils packagers. Do not file bugs for its content to the GNU Mailutils upstream authors. </p>
