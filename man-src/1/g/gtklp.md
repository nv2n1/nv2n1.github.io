---
title: "gtklp(1)"
name: "gtklp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtklp/"
description: "gtklp – print files via CUPS"
---

<h2>NAME</h2>
<p> gtklp &#8211; print files via CUPS</p>
<h2>SYNOPSIS</h2>
<p> <code>gtklp</code> [-P|-d <i>printer</i>] [-c <i>configdir</i>] [-S|-h <i>server</i>] [-p <i>port</i>] [-l] [-D] [-V] [-b] [-i] [-H] [-C] [-U <i>user</i>] [-#|-n <i>n</i>] [-E] [-q <i>priority</i>] [-t|-J <i>jobname</i>] [-o <i>option=value</i> &#8230; ][<i>file(s)</i>] </p>
<p> <code>lp</code> [-d <i>printer</i>] [-S|-h <i>server</i>] [-p <i>port</i>] [-D] [-V] [-b] [-U <i>user</i>] [-#|-n <i>n</i>] [-E] [-q <i>priority</i>] [-t|-J <i>jobname</i>] [-P <i>page-list</i> [-H handling] [-X] [-o <i>option=value</i> &#8230; ][<i>file(s)</i>] </p>
<p> <code>lpr</code> [-P|-d <i>printer</i>] [-S|-h <i>server</i>] [-p <i>port</i>] [-D] [-V] [-b] [-U <i>user</i>] [-#|-n <i>n</i>] [-E] [-q <i>priority</i>] [-t|-J|-C|-T <i>jobname</i>] [-X] [-o <i>option=value</i> &#8230; ][<i>file(s)</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>GtkLP</code> is an graphical frontend for <i>CUPS</i>, the Common UNIX Printing System.<br />
 It is used to have an easy (and graphical) access to all of the many options of cups-managed printers.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <code>gtklp</code>:</p>
<dl>
<dt>-P <i>printer</i></p>
<dd>
 Use <i>printer</i> as default destination.</p>
<dt>-d <i>printer</i></p>
<dd>
 This option is equivalent to &quot;-P&quot;.</p>
<dt>-c <i>configdir</i></p>
<dd>
 Use <i>configdir</i> to set an alternative path to the configfiles for <code>GtkLP</code>. </p>
<dt>-S <i>server</i></p>
<dd>
 The name of the CUPS-Server.</p>
<dt>-h <i>server</i></p>
<dd>
 The same as -S.</p>
<dt>-p <i>port</i></p>
<dd>
 The port of CUPS-Server, 631 per default.</p>
<dt>-l</p>
<dd>
 Only list the chosen options as a list of commandline-parameters for lpr.<br />
 Nice for scripting purposes&#8230;</p>
<dt>-D</p>
<dd>
 Debug.</p>
<dt>-V</p>
<dd>
 Displays the version of <code>GtkLP</code>.</p>
<dt>-b</p>
<dd>
 Use builtin defaults instead of saved options</p>
<dt>-i</p>
<dd>
 Ignore data on stdin.<br />
 Sometimes useful, e.g. for printing from some versions of the Acrobat Reader.</p>
<dt>-U <i>user</i></p>
<dd>
 The name of the cups-User to use.</p>
<dt>-# <i>n</i></p>
<dd>
 Make <i>n</i> copies per default.</p>
<dt>-n <i>n</i></p>
<dd>
 The same as -#.</p>
<dt>-H</p>
<dd>
 Help</p>
<dt>-C</p>
<dd>
 Force console-mode</p>
<dt>-o <i>option=value</i></p>
<dd>
 Specify extra options, same syntax as lpr</p>
<dt>-E</p>
<dd>
 Forces encryption when connecting to the server.</p>
<dt>-q <i>priority</i></p>
<dd>
 Specify the priority of the print job, from 1 (lowest) to 100 (highest)</p>
<dt>-t <i>jobname</i></p>
<dd>
 Specify the jobname</p>
<dt>-J <i>jobname</i></p>
<dd>
 The same as -t.</p>
<dt>
<dd>
 If called as lp, the following options differ from GtkLP`s options:</p>
<dt>-X</p>
<dd> Force X-Mode, even if GTKLP_FORCEX is not set to 1 <code>.TP</code>5 -P <i>page-list</i><br />
 Specifies which pages to print in the document. The list can contain a list of numbers and ranges (#-#) separated by commas (e.g. 1,3-5,16). </p>
<dt>-H <i>handling</i></p>
<dd> Specifies when the job should be printed. A value of <i>immediate</i> will print the file immediately, a value of <i>hold</i> will hold the job indefinitely, and a time value (HH:MM) will hold the job until the specified time. (does this option work ?)</p>
<dt>
<dd>
 If called as lpr, the following options differ from GtkLP`s options:</p>
<dt>-X</p>
<dd> Force X-Mode, even if GTKLP_FORCEX is not set to 1 <code>.TP</code>5 -C <i>jobname</i> Specify the jobname <code>.TP</code>5 -T <i>jobname</i> The same as -C. <code>.TP</code>5 -p Specifies that the print file should be formatted with a shaded header with the date, time, job name, and page number. This option is equivalent to &quot;-oprettyprint&quot; and is only useful when printing text files. <code>.TP</code>5 -l Specifies that the print file is already formatted for the destination and should be sent without filtering. This option is equivalent to &quot;-oraw&quot;.</p>
<dt><code>Some</code>other<code>options</code>from<code>systemv`s</code>lp<code>and</code>berkeley`s<code>lpr</code>are<code>ignored</code></p>
<dd> without error message</dl>
<h2>PATHS</h2>
<p> <code>GtkLP</code> looks for config-files under<br />
 <i>&lt;configdir&gt;</i><br />
 then under<br />
 <i>$HOME/.gtklp/</i><br />
 and at last under<br />
 <i>/etc/gtklp/</i>. </p>
<p> To hide Printers from users, use the following pathes:<br />
 <i>/etc/gtklp/accept/</i><br />
 <i>/etc/gtklp/deny/</i><br />
 <i>$HOME/.gtklp/</i> </p>
<p> Just put an empty file with the name of the printer the user should see by default to <i>accept</i>, put an empty file with the name of the printer the user should never see to <i>deny</i>. If only <i>accept</i> exists, all but the accepted printers are allowed. If only <i>deny</i> exists, all but the denied printers are accepted.<br />
 All users can <i>deny</i> accepted printers, but they can&#8217;t unhide denied ones.</p>
<h2>SPECIAL</h2>
<p> In GtkLP you can define a browser to open the help URL, the CUPS-Homepage and so on. Just use the your favorite HTML browser. The first $1 in command-line will be substituted by the URL. </p>
<p> If you can&#8217;t connect to an X-Server, GtkLP acts as console-lpr. </p>
<p> If called as lpr, or lp, GtkLP acts on console and has some other command-line parameters, see above.</p>
<h2>VARIABLES</h2>
<p> You can set the following environment variables to influence the behaviour of GtkLP:</p>
<dl>
<dt>CUPS_SERVER</p>
<dd>
 The default CUPS-server to connect to</p>
<dt>IPP_PORT</p>
<dd>
 The default Port of the CUPS-server to connect to</p>
<dt>PRINTER</p>
<dd>
 The default printer to use</p>
<dt>GTKLP_FORCEX</p>
<dd>
 Set to 1 to force X-Mode for lpr and lp</dl>
<h2>ERROR</h2>
<p> GtkLP produces the following Error-Codes:</p>
<dl>
<dt>0</p>
<dd> normal program termination </p>
<dt>1</p>
<dd> small error, wrong parameters, etc. </p>
<dt>2</p>
<dd> Server Problems, server not found, no default printer found, etc. </p>
<dt>3</p>
<dd> BAD error. Fields declared too short, too many printers, etc.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gtklpq/">gtklpq</a>(1), <a href="/docs/linux/man/1-lpr/">lpr</a>(1), CUPS Software Users Manual<br />
 <a rel="nofollow" href="http://localhost:631/documentation.html">http://localhost:631/documentation.html</a></p>
<h2>COPYRIGHT</h2>
<p> This program was written by T. Mueller, 2000, 2001, 2002.<br />
 It is licensed under the Terms of the GNU GENERAL PUBLIC LICENSE,<br />
 see also <a rel="nofollow" href="http://www.gnu.org.">http://www.gnu.org.</a> </p>
<h2>CONTACT</h2>
<p> The latest version of <code>GtkLP</code> is always available under<br />
 <a rel="nofollow" href="http://gtklp.sourceforge.net/">http://gtklp.sourceforge.net/</a> </p>
<p> Feel also free to contact me.<br />
 Please mail also, if you like the software !!! ;-) </p>
<h2>Index</h2>
