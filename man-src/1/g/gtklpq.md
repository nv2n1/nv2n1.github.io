---

title: "gtklpq(1)"
name: "gtklpq"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtklpq/"
description: "gtklpq – manage print queues via CUPS"
---

<p> gtklpq &#8211; manage print queues via CUPS</p>
<h2>SYNOPSIS</h2>
<p> <code>gtklpq</code> [-P|-d <i>printer</i>] [-S <i>server</i>] [-p <i>port</i>] [-D] [-V] [-U <i>user</i>] [-t <i>timeout</i>] [-g <i>X</i>x<i>Y</i>] [-C] [-h] [-E] </p>
<p> <code>lpq</code> [-P|-d <i>printer</i>] [-S <i>server</i>] [-p <i>port</i>] [-D] [-V] [-U <i>user</i>] [-t <i>timeout</i>] [-E] </p>
<p> <code>lprm</code> [-P|-d <i>printer</i>] [-S <i>server</i>] [-p <i>port</i>] [-D] [-V] [-U <i>user</i>] [-E] [-] [job ID(s)] </p>
<p> <code>reject</code> [-h <i>server</i>] [-p <i>port</i>] [-D] [-V] [-U <i>user</i>] [-E] [-r <i>reason</i>] [destination(s)] </p>
<p> <code>accept</code> [-h <i>server</i>] [-p <i>port</i>] [-D] [-V] [-U <i>user</i>] [-E] [-r <i>reason</i>] [destination(s)] </p>
<p> <code>disable</code> [-h <i>server</i>] [-c] [-p <i>port</i>] [-D] [-V] [-U <i>user</i>] [-E] [-r <i>reason</i>] [destination(s)] </p>
<p> <code>enable</code> [-h <i>server</i>] [-p <i>port</i>] [-D] [-V] [-U <i>user</i>] [-E] [-r <i>reason</i>] [destination(s)]</p>
<h2>DESCRIPTION</h2>
<p> <code>GtkLPQ</code> is an graphical frontend for <i>CUPS</i>, the Common UNIX Printing System.<br/>
 It is used to manage CUPS-Printqueues. </p>
<dl>
<dt>
</dt><dd> GtkLPQ<br/>
 Graphical Frontend</dd>
<dt>lpq</dt>
<dd>
 Show print queue</dd>
<dt>lprm</dt>
<dd>
 Remove jobs</dd>
<dt>disable/enable</dt>
<dd>
 Disable/enable printer</dd>
<dt>reject/accept</dt>
<dd>
 Reject/Accept printjobs for this printer</dd>
<dt>
</dt><dd> <code>GtkLPQ</code> is part of the <code>GtkLP</code>-package.</dd></dl>
<h2>OPTIONS</h2>
<p> The following options are recognized by <code>gtklpq</code>:</p>
<dl>
<dt>-P <i>printer</i></dt>
<dd>
 Use <i>printer</i> as default destination.</dd>
<dt>-d <i>printer</i></dt>
<dd>
 This option is equivalent to &quot;-P&quot;.</dd>
<dt>-S <i>server</i></dt>
<dd>
 The name of the CUPS-Server.</dd>
<dt>-p <i>port</i></dt>
<dd>
 The port of CUPS-Server, 631 per default.</dd>
<dt>-D</dt>
<dd>
 Debug.</dd>
<dt>-V</dt>
<dd>
 Displays the version of <code>GtkLPQ</code>.</dd>
<dt>-U <i>user</i></dt>
<dd>
 The name of the cups-User to use.</dd>
<dt>-t <i>timeout</i></dt>
<dd>
 The intervall in seconds between two queue-updates.</dd>
<dt>-g <i>X</i>x<i>Y</i></dt>
<dd>
 Pop up GtkLPQ at position (X,Y).</dd>
<dt>-h</dt>
<dd>
 Help</dd>
<dt>-C</dt>
<dd>
 Force console-mode.</dd>
<dt>-E</dt>
<dd>
 Forces encryption when connecting to the server.</dd>
<dt>
</dt><dd>
 If called as lpq, the following options differ from GtkLPQ`s options:</dd>
<dt>-X</dt>
<dd>
 Force X-Mode, even if GTKLP_FORCEX is not set to 1</dd>
<dt>
</dt><dd> If called as lprm, the following options differ from GtkLPQ`s options:</dd>
<dt>&#8211;</dt>
<dd>
 Cancel all jobs</dd>
<dt>
</dt><dd> Without any given jobs, lprm removes the current job.</dd>
<dt>
</dt><dd> If called as disable, the following options differ from GtkLPQ`s options:</dd>
<dt>-c</dt>
<dd>
 Cancel all jobs</dd>
<dt>-r reason</dt>
<dd> Give an reason, why you do so </dd>
<dt>
</dt><dd> If called as reject, the following options differ from GtkLPQ`s options:</dd>
<dt>-r reason</dt>
<dd> Give an reason, why you do so</dd></dl>
<h2>PATHS</h2>
<p> To hide Printers from users, use the following pathes:<br/>
 <i>/etc/gtklp/accept/</i><br/>
 <i>/etc/gtklp/deny/</i><br/>
 <i>$HOME/.gtklp/</i> </p>
<p> Just put an empty file with the name of the printer the user should see by default to <i>accept</i>, put an empty file with the name of the printer the user should never see to <i>deny</i>.<br/>
 The <i>accept</i> values can be overwritten by the user, the <i>deny</i> values can&#8217;t.</p>
<h2>SPECIAL</h2>
<p> If you can`t connect to an X-Server, GtkLPQ acts as console-lpq. </p>
<p> If called as lpq, enable, disable, accept, or reject, GtkLPQ acts on console like these tools and has some other command-line parameters, see above. </p>
<h2>VARIABLES</h2>
<p> You can set the following environment variables to influence the behaviour of GtkLPQ:</p>
<dl>
<dt>CUPS_SERVER</dt>
<dd>
 The default CUPS-server to connect to</dd>
<dt>IPP_PORT</dt>
<dd>
 The default Port of the CUPS-server to connect to</dd>
<dt>PRINTER</dt>
<dd>
 The default printer to use</dd>
<dt>GTKLP_FORCEX</dt>
<dd>
 Set to 1 to force X-Mode for lpr and lp</dd></dl>
<h2>ERROR</h2>
<p> GtkLPQ produces the follwoing Error-Codes:</p>
<dl>
<dt>0</dt>
<dd> normal program termination </dd>
<dt>1</dt>
<dd> small error, wrong parameters, etc. </dd>
<dt>2</dt>
<dd> Server Problems, server not found, no default printer found, etc. </dd>
<dt>3</dt>
<dd> BAD error. Fields declared too short, too many printers, etc.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gtklp/">gtklp</a>(1), <a href="/docs/linux/man/1-lprm/">lprm</a>(1), <a href="/docs/linux/man/1-lp/">lp</a>(1), CUPS Software Users Manual<br/>
 <a rel="nofollow" href="http://localhost:631/documentation.html">http://localhost:631/documentation.html</a></p>
<h2>COPYRIGHT</h2>
<p> This program was written by T. Mueller, 2000, 2001, 2002.<br/>
 It is licensed under the Terms of the GNU GENERAL PUBLIC LICENSE,<br/>
 see also <a rel="nofollow" href="http://www.gnu.org.">http://www.gnu.org.</a> </p>
<h2>CONTACT</h2>
<p> The latest version of <code>GtkLPQ</code> is always available under<br/>
 <a rel="nofollow" href="http://gtklp.sourceforge.net/">http://gtklp.sourceforge.net/</a><br/>
 It is part of the <code>GtkLP</code>-package.<br/>
 Feel also free to contact me.<br/>
 Please mail also, if you like the software !!! ;-) </p>
