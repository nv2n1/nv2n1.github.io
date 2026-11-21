---

title: "gtklp(1)"
name: "gtklp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtklp/"
description: "gtklp – print files via CUPS"
---

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
<dt>-P <i>printer</i></dt>
<dd>
 Use <i>printer</i> as default destination.</dd>
<dt>-d <i>printer</i></dt>
<dd>
 This option is equivalent to &quot;-P&quot;.</dd>
<dt>-c <i>configdir</i></dt>
<dd>
 Use <i>configdir</i> to set an alternative path to the configfiles for <code>GtkLP</code>. </dd>
<dt>-S <i>server</i></dt>
<dd>
 The name of the CUPS-Server.</dd>
<dt>-h <i>server</i></dt>
<dd>
 The same as -S.</dd>
<dt>-p <i>port</i></dt>
<dd>
 The port of CUPS-Server, 631 per default.</dd>
<dt>-l</dt>
<dd>
 Only list the chosen options as a list of commandline-parameters for lpr.<br />
 Nice for scripting purposes&#8230;</dd>
<dt>-D</dt>
<dd>
 Debug.</dd>
<dt>-V</dt>
<dd>
 Displays the version of <code>GtkLP</code>.</dd>
<dt>-b</dt>
<dd>
 Use builtin defaults instead of saved options</dd>
<dt>-i</dt>
<dd>
 Ignore data on stdin.<br />
 Sometimes useful, e.g. for printing from some versions of the Acrobat Reader.</dd>
<dt>-U <i>user</i></dt>
<dd>
 The name of the cups-User to use.</dd>
<dt>-# <i>n</i></dt>
<dd>
 Make <i>n</i> copies per default.</dd>
<dt>-n <i>n</i></dt>
<dd>
 The same as -#.</dd>
<dt>-H</dt>
<dd>
 Help</dd>
<dt>-C</dt>
<dd>
 Force console-mode</dd>
<dt>-o <i>option=value</i></dt>
<dd>
 Specify extra options, same syntax as lpr</dd>
<dt>-E</dt>
<dd>
 Forces encryption when connecting to the server.</dd>
<dt>-q <i>priority</i></dt>
<dd>
 Specify the priority of the print job, from 1 (lowest) to 100 (highest)</dd>
<dt>-t <i>jobname</i></dt>
<dd>
 Specify the jobname</dd>
<dt>-J <i>jobname</i></dt>
<dd>
 The same as -t.</dd>
<dt>
</dt><dd>
 If called as lp, the following options differ from GtkLP`s options:</dd>
<dt>-X</dt>
<dd> Force X-Mode, even if GTKLP_FORCEX is not set to 1 <code>.TP</code>5 -P <i>page-list</i><br />
 Specifies which pages to print in the document. The list can contain a list of numbers and ranges (#-#) separated by commas (e.g. 1,3-5,16). </dd>
<dt>-H <i>handling</i></dt>
<dd> Specifies when the job should be printed. A value of <i>immediate</i> will print the file immediately, a value of <i>hold</i> will hold the job indefinitely, and a time value (HH:MM) will hold the job until the specified time. (does this option work ?)</dd>
<dt>
</dt><dd>
 If called as lpr, the following options differ from GtkLP`s options:</dd>
<dt>-X</dt>
<dd> Force X-Mode, even if GTKLP_FORCEX is not set to 1 <code>.TP</code>5 -C <i>jobname</i> Specify the jobname <code>.TP</code>5 -T <i>jobname</i> The same as -C. <code>.TP</code>5 -p Specifies that the print file should be formatted with a shaded header with the date, time, job name, and page number. This option is equivalent to &quot;-oprettyprint&quot; and is only useful when printing text files. <code>.TP</code>5 -l Specifies that the print file is already formatted for the destination and should be sent without filtering. This option is equivalent to &quot;-oraw&quot;.</dd>
<dt><code>Some</code>other<code>options</code>from<code>systemv`s</code>lp<code>and</code>berkeley`s<code>lpr</code>are<code>ignored</code></dt>
<dd> without error message</dd></dl>
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
<p> GtkLP produces the following Error-Codes:</p>
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
