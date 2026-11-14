---
title: "gramps(1)"
name: "gramps"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gramps/"
description: "gramps – Genealogical Research and Analysis Management Programming System."
---

<h2>NAME</h2>
<p> gramps &#8211; Genealogical Research and Analysis Management Programming System. </p>
<h2>SYNOPSIS</h2>
<p> <code>gramps</code> [<code>-?|&#8211;help</code>] [<code>&#8211;usage</code>] [<code>&#8211;version</code>] [<code>-l</code>] [<code>-u|&#8211;force-unlock</code>] [<code>-O|&#8211;open=</code> <i>DATABASE</i> [<code>-f|&#8211;format=</code> <i>FORMAT</i>]] [<code>-i|&#8211;import=</code> <i>FILE</i> [<code>-f|&#8211;format=</code> <i>FORMAT</i>]] [<code>-i|&#8211;import=</code> <i>&#8230;</i>] [<code>-e|&#8211;export=</code> <i>FILE</i> [<code>-f|&#8211;format=</code> <i>FORMAT</i>]] [<code>-a|&#8211;action=</code> <i>ACTION</i>] [<code>-p|&#8211;options=</code> <i>OPTIONSTRING</i>]] [ <i>FILE</i> ] [<code>&#8211;version</code>] </p>
<h2>DESCRIPTION</h2>
<p> <i>Gramps</i> is a Free/OpenSource genealogy program. It is written in Python, using the GTK+/GNOME interface. Gramps should seem familiar to anyone who has used other genealogy programs before such as <i>Family Tree Maker (TM)</i>, <i>Personal Ancestral Files (TM)</i>, or the GNU Geneweb. It supports importing of the ever popular GEDCOM format which is used world wide by almost all other genealogy software. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>gramps</code><i> FILE</i></p>
<dd> When <i>FILE</i> is given (without any flags) as a family tree name or as a family tree database directory, then it is opened and an interactive session is started. If FILE is a file format understood by GRAMPS, an empty family tree is created whose name is based on the <i>FILE</i> name and the data is imported into it. The rest of the options is ignored. This way of launching is suitable for using gramps as a handler for genealogical data in e.g. web browsers. This invocation can accept any data format native to gramps, see below. </p>
<dt><code>-f,&#8211;format=</code><i> FORMAT</i></p>
<dd> Explicitly specify format of <i>FILE</i> given by preceding <code>-i</code>, or <code>-e</code> option. If the <code>-f</code> option is not given for any <i>FILE</i>, the format of that file is guessed according to its extension or MIME-type. </p>
<p> Formats available for output are <code>gramps-xml</code> (guessed if <i>FILE</i> ends with <code>.gramps</code>), <code>gedcom</code> (guessed if <i>FILE</i> ends with <code>.ged</code>), or any file export available through the GRAMPS plugin system. </p>
<p> Formats available for import are <code>grdb</code>, <code>gramps-xml</code>, <code>gedcom</code>, <code>gramps-pkg</code> (guessed if <i>FILE</i> ends with <code>.gpkg</code>), and <code>geneweb</code> (guessed if <i>FILE</i> ends with <code>.gw</code>). </p>
<p> Formats available for export are <code>gramps-xml</code>, <code>gedcom</code>, <code>gramps-pkg</code>, <code>wft</code> (guessed if <i>FILE</i> ends with <code>.wft</code>), <code>geneweb</code>, and <code>iso</code> (never guessed, always specify with <code>-f</code> option). </p>
<dt><code>-l</code></p>
<dd> Print a list of known family trees. </p>
<dt><code>-u,&#8211;force-unlock</code></p>
<dd> Unlock a locked database. </p>
<dt><code>-O,&#8211;open=</code><i> DATABASE</i></p>
<dd> Open <i>DATABASE</i> which must be an existing database directory or existing family tree name. If no action, import or export options are given on the command line then an interactive session is started using that database. </p>
<dt><code>-i,&#8211;import=</code><i> FILE</i></p>
<dd> Import data from <i>FILE</i>. If you haven&#8217;t specified a database then a temporary database is used; this is deleted when you exit gramps. </p>
<p> When more than one input file is given, each has to be preceded by <code>-i</code> flag. The files are imported in the specified order, i.e. <code>-i</code> <i>FILE1</i> <code>-i</code> <i>FILE2</i> and <code>-i</code> <i>FILE2</i> <code>-i</code> <i>FILE1</i> might produce different gramps IDs in the resulting database. </p>
<dt><code>-a,&#8211;action=</code><i> ACTION</i></p>
<dd> Perform <i>ACTION</i> on the imported data. This is done after all imports are successfully completed. Currently available actions are <code>summary</code> (same as Reports-&gt;View-&gt;Summary), <code>check</code> (same as Tools-&gt;Database Processing-&gt;Check and Repair), <code>report</code> (generates report), and <code>tool</code> (runs a plugin tool). Both <code>report</code> and <code>tool</code> need the <i>OPTIONSTRING</i> supplied by the <code>-p</code> flag). </p>
<p> The <i>OPTIONSTRING</i> should satisfy the following conditions:<br />
 It must not contain any spaces. If some arguments need to include spaces, the string should be enclosed with quotation marks, i.e., follow the shell syntax. Option string is a list of pairs with name and value (separated by the equality sign). The name and value pairs must be separated by commas. </p>
<p> Most of the report or tools options are specific for each report or tool. However, there are some common options. </p>
<p> <code>name=name</code><br />
 This mandatory option determines which report or tool will be run. If the supplied <i>name</i> does not correspond to any available report or tool, an error message will be printed followed by the list of available reports or tools (depending on the <i>ACTION</i>). </p>
<p> <code>show=all</code><br />
 This will produce the list of names for all options available for a given report or tool. </p>
<p> <code>show=optionname</code><br />
 This will print the description of the functionality supplied by <i>optionname</i>, as well as what are the acceptable types and values for this option. </p>
<p> Use the above options to find out everything about a given report. </p>
</dl>
<p> When more than one output action is given, each has to be preceded by <code>-a</code> flag. The actions are performed one by one, in the specified order. </p>
<dl>
<dt><code>-d,&#8211;debug=</code><i> LOGGER_NAME</i></p>
<dd> Enables debug logs for development and testing. Look at the source code for details</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the version number of gramps and then exits </p>
</dl>
<h2>Operation</h2>
<p> If the first argument on the command line does not start with dash (i.e. no flag), gramps will attempt to open the file with the name given by the first argument and start interactive session, ignoring the rest of the command line arguments. </p>
<p> If the <code>-O</code> flag is given, then gramps will try opening the supplied database and then work with that data, as instructed by the further command line parameters. </p>
<p> With or without the <code>-O</code> flag, there could be multiple imports, exports, and actions specified further on the command line by using <code>-i</code>, <code>-e</code>, and <code>-a</code> flags. </p>
<p> The order of <code>-i</code>, <code>-e</code>, or <code>-a</code> options does not matter. The actual order always is: all imports (if any) -&gt; all actions (if any) -&gt; all exports (if any). But opening must always be first! </p>
<p> If no <code>-O</code> or <code>-i</code> option is given, gramps will launch its main window and start the usual interactive session with the empty database, since there is no data to process, anyway. </p>
<p> If no <code>-e</code> or <code>-a</code> options are given, gramps will launch its main window and start the usual interactive session with the database resulted from all imports. This database resides in the <code>import_db.grdb</code> under <code>~/.gramps/import</code> directory. </p>
<p> The error encountered during import, export, or action, will be either dumped to <i>stdout</i> (if these are exceptions handled by gramps) or to <i>stderr</i> (if these are not handled). Use usual shell redirections of <i>stdout</i> and <i>stderr</i> to save messages and errors in files. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>To open an existing family tree and import an xml file into it, one may type:</p>
<dd> <code>gramps</code> <code>-O</code> <i>&#8216;My Family Tree&#8217;</i> <code>-i</code> <i>~/db3.gramps</i></p>
<dt>The above changes the opened family tree, to do the same, but import both in a temporary family tree and start an interactive session, one may type:</p>
<dd> <code>gramps</code> <code>-i</code> <i>&#8216;My Family Tree&#8217;</i> <code>-i</code> <i>~/db3.gramps</i></p>
<dt>To import four databases (whose formats can be determined from their names) and then check the resulting database for errors, one may type:</p>
<dd> <code>gramps</code> <code>-i</code> <i>file1.ged</i> <code>-i</code> <i>file2.tgz</i> <code>-i</code> <i>~/db3.gramps</i> <code>-i</code> <i>file4.wft</i> <code>-a</code> <i>check</i></p>
<dt>To explicitly specify the formats in the above example, append filenames with appropriate <code>-f</code> options:</p>
<dd> <code>gramps</code> <code>-i</code> <i>file1.ged</i> <code>-f</code> <i>gedcom</i> <code>-i</code> <i>file2.tgz</i> <code>-f</code> <i>gramps-pkg</i> <code>-i</code> <i>~/db3.gramps</i> <code>-f</code> <i>gramps-xml</i> <code>-i</code> <i>file4.wft</i> <code>-f</code> <i>wft</i> <code>-a</code> <i>check</i></p>
<dt>To record the database resulting from all imports, supply <code>-e</code> flag (use <code>-f</code> if the filename does not allow gramps to guess the format):</p>
<dd> <code>gramps</code> <code>-i</code> <i>file1.ged</i> <code>-i</code> <i>file2.tgz</i> <code>-e</code> <i>~/new-package</i> <code>-f</code> <i>gramps-pkg</i></p>
<dt>To import three databases and start interactive gramps session with the result:</p>
<dd> <code>gramps</code> <code>-i</code> <i>file1.ged</i> <code>-i</code> <i>file2.tgz</i> <code>-i</code> <i>~/db3.gramps</i></p>
<dt>To run the Verify tool from the commandline and output the result to stdout:</p>
<dd> <code>gramps</code> <code>-O</code> <i>&#8216;My Family Tree&#8217;</i> <code>-a</code> <i>tool</i> <code>-p</code> <code>name</code>=<i>verify</i></p>
<dt>Finally, to start normal interactive session type:</p>
<dd> <code>gramps</code> </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The program checks whether these environment variables are set: </p>
<p> <code>LANG</code> &#8211; describe, which language to use: Ex.: for polish language this variable has to be set to pl_PL.UTF-8. </p>
<p> <code>GRAMPSHOME</code> &#8211; if set, force GRAMPS to use the specified directory to keep program settings and databases there. By default, this variable is not set and gramps assumes that the folder with all databases and profile settings should be created within the user profile folder (described by environment variable HOME for Linux or USERPROFILE for Windows 2000/XP). </p>
<h2>CONCEPTS</h2>
<p> Supports a python-based plugin system, allowing import and export writers, report generators, tools, and display filters to be added without modification of the main program. </p>
<p> In addition to generating direct printer output, report generators also target other systems, such as <i>OpenOffice.org</i>, <i>AbiWord</i>, HTML, or LaTeX to allow the users to modify the format to suit their needs. </p>
<h2>KNOWN BUGS AND LIMITATIONS</h2>
<h2>FILES</h2>
<p> <i>${PREFIX}/bin/gramps</i><br />
 <i>${PREFIX}/share/gramps</i><br />
 <i>${HOME}/.gramps</i> </p>
<h2>AUTHORS</h2>
<p> Donald Allingham <i>&lt;don [at] gramps-project.org&gt;</i><br />
 <i><a rel="nofollow" href="http://gramps.sourceforge.net">http://gramps.sourceforge.net</a></i> </p>
<p> This man page was originally written by:<br />
 Brandon L. Griffith <i>&lt;brandon [at] debian.org&gt;</i><br />
 for inclusion in the Debian GNU/Linux system. </p>
<p> This man page is currently maintained by:<br />
 Gramps project <i>&lt;xxx [at] gramps-project.org&gt;</i> </p>
<h2>DOCUMENTATION</h2>
<p> The user documentation is available through standard GNOME Help browser in the form of Gramps Manual. The manual is also available in XML format as <code>gramps-manual.xml</code> under <i>doc/gramps-manual/$LANG</i> in the official source distribution. </p>
<p> The developer documentation can be found on the <i><a rel="nofollow" href="http://developers.gramps-project.org">http://developers.gramps-project.org</a></i> site. </p>
<h2>Index</h2>
