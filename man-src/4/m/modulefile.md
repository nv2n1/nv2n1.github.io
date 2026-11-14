---
title: "modulefile(4)"
name: "modulefile"
section: "4"
letter: "m"
url: "/docs/linux/man/4-modulefile/"
description: "modulefile – files containing Tcl code for the Modules package"
---

<p>modulefile &#8211; files containing Tcl code for the Modules package</p>
<h2>Description</h2>
<p><i>modulefile</i>s are written in the Tool Command Language, <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3) and are interpreted by the <code>modulecmd</code> program via the <code><a href="/docs/linux/man/1-module/">module</a></code>(1) user interface. modulefiles can be loaded, unloaded, or switched on-the-fly while the user is working; and can be used to implement site policies regarding the access and use of applications. A <i>modulefile</i> begins with the magic cookie, &#8216;#%Module&#8217;. A version number may be placed after this string. The version number is useful as the <i>modulefile</i> format may change. If a version number doesn&#8217;t exist, then <code>modulecmd</code> will assume the <i>modulefile</i> is compatible with the latest version. The current <i>modulefile version</i> is <code>1.0.</code> Files without the magic cookie will not be interpreted by <code>modulecmd.</code> Each <i>modulefile</i> contains the changes to a user&#8217;s environment needed to access an application. Tcl is a simple programming language which permits modulefiles to be arbitrarily complex, depending upon the application&#8217;s and the modulefile writer&#8217;s needs. If support for extended tcl (tclX) has been configured for your installation of the Modules package, you may use all the extended commands provided by tclX, too. A typical <i>modulefile</i> is a simple bit of code that set or add entries to the PATH, MANPATH, or other environment variables. Tcl has conditional statements that are evaluated when the modulefile is loaded. This is very effective for managing path or environment changes due to different OS releases or architectures. The user environment information is encapsulated into a single <i>modulefile</i> kept in a central location. The same modulefile is used by every user on any machine. So, from the user&#8217;s perspective, starting an application is exactly the same irrespective of the machine or platform they are on. modulefiles also hide the notion of different types of shells. From the user&#8217;s perspective, changing the environment for one shell looks exactly the same as changing the environment for another shell. This is useful for new or novice users and eliminates the need for statements such as &quot;if you&#8217;re using the C Shell do this &#8230;, otherwise if you&#8217;re using the Bourne shell do this &#8230;&quot; Announcing and accessing new software is uniform and independent of the user&#8217;s shell. From the modulefile writer&#8217;s perspective, this means one set of information will take care of every type of shell. </p>
<h2>Modules Specific Tcl Commands</h2>
<p>The Modules Package uses commands which are extensions to the &quot;standard&quot; <i>Tool Command Language</i> <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3) package. Unless otherwise specified, the Module commands return the empty string. Some commands behave differently when a <i>modulefile</i> is loaded or unloaded. The command descriptions assume the <i>modulefile</i> is being loaded. </p>
<p> <code>break</code></p>
<dl>
<dd>This is not a Modules-specific command, it&#8217;s actually part of Tcl, which has been overloaded similar to the <i>continue</i> and <i>exit</i> commands to have the effect of causing the module not to be listed as loaded and not affect other modules being loaded concurrently. All non-environment commands within the module will be performed up to this point and processing will continue on to the next module on the command line. The <i>break</i> command will only have this effect if not used within a Tcl loop though. </p>
<p> An example: Suppose that a full selection of modulefiles are needed for various different architectures, but some of the modulefiles are not needed and the user should be alerted. Having the unnecessary modulefile be a link to the following <i>notavail</i> modulefile will perform the task as required. </p>
<pre>#%Module1.0
## notavail modulefile
##
proc ModulesHelp { } {
 puts stderr &quot;	This module does nothing but alert the user&quot;
 puts stderr &quot;	that the [module-info name] module is not available&quot;
}
module-whatis &quot;Notifies user that module is not available.&quot;
set curMod [module-info name]
if { [ module-info mode load ] } {
 puts stderr &quot;Note: '$curMod' is not available for [uname sysname].&quot;
}
break</pre>
</dl>
<p> <code>chdir</code> <i>directory</i></p>
<dl>
<dd>Set the current working directory to <i>directory</i>.</dl>
<p> <code>continue</code></p>
<dl>
<dd>This is not a modules specific command but another overloaded Tcl command and is similar to the <i>break</i> or <i>exit</i> commands except the module will be listed as loaded as well as performing any environment or Tcl commands up to this point and then continuing on to the next module on the command line. The <i>continue</i> command will only have this effect if not used within a Tcl loop though.</dl>
<p> <code>exit [N]</code></p>
<dl>
<dd>This is not a modules specific command but another overloaded Tcl command and is similar to the <i>break</i> or <i>continue</i> commands. However, this command will cause the immediate cessation of this module and any additional ones on the command line. This module and the subsequent modules will not be listed as loaded. No environment commands will be performed in the current module. </p>
<p> The integer value <i>N</i> after the <i>exit</i> command will be used as an command exit value; however, some shells (<i>bash</i> being one of them) do not carry this value through an <i>eval</i> though. For <i>bash</i> and those Bourne shells (<i>/bin/sh</i>) being emulated by the <i>bash</i> will have return a non-zero value as a result of <i>test 0 = 1</i> being appended to the evaluate string.</dl>
<p> <code>setenv</code> <i>variable</i> <i>value</i></p>
<dl>
<dd>Set environment <i>variable</i> to <i>value</i>. The <code>setenv</code> command will also change the process&#8217; environment. A reference using Tcl&#8217;s <code>env</code> associative array will reference changes made with the <code>setenv</code> command. Changes made using Tcl&#8217;s <code>env</code> associative array will <code>NOT</code> change the user&#8217;s environment variable like the <code>setenv</code> command. An environment change made this way will only affect the module parsing process. The <code>setenv</code> command is also useful for changing the environment prior to the <code>exec</code> or <code>system</code> command. When a <i>modulefile</i> is unloaded, <code>setenv</code> becomes <code>unsetenv</code>. If the environment variable had been defined it will be overwritten while loading the modulefile. A subsequent unload will unset the environment variable &#8211; the previous value cannot be restored! (Unless you handle it explicitly &#8230; see below.)</dl>
<p> <code>unsetenv</code> <i>variable</i> [<i>value</i>]</p>
<dl>
<dd>Unsets environment <i>variable</i>. However, if there is an optional <i>value</i>, then when unloading a module, it will set <i>variable</i> to <i>value</i>. The <code>unsetenv</code> command changes the process&#8217; environment like <code>setenv</code>.</dl>
<p> <code>append-path</code> [ <i>-d C</i> | <i>&#8211;delim C</i> | <i>&#8211;delim=C</i> ] <i>variable</i> <i>value</i><br />
 <code>prepend-path</code> [ <i>-d C</i> | <i>&#8211;delim C</i> | <i>&#8211;delim=C</i> ] <i>variable</i> <i>value</i></p>
<dl>
<dd>Append or prepend <i>value</i> to environment <i>variable</i>. The <i>variable</i> is a colon, or delimiter, separated list such as<br />
 &quot;PATH=directory:directory:directory&quot;. The default delimiter is a colon &#8216;:&#8217;, but an arbitrary one can be given by the <i>&#8211;delim</i> option. For example a space can be used instead (which will need to be handled in the Tcl specially by enclosing it in &quot; &quot; or { }). A space, however, can not be specified by the <i>&#8211;delim=C</i> form. </p>
<p> If the <i>variable</i> is not set, it is created. When a <i>modulefile</i> is unloaded, <code>append-path</code> and <code>prepend-path</code> become <code>remove-path</code>.</dl>
<p> <code>remove-path</code> [ <i>-d C</i> | <i>&#8211;delim C</i> | <i>&#8211;delim=C</i> ] <i>variable</i> <i>value</i></p>
<dl>
<dd>Remove <i>value</i> from the colon, or delimiter, separated list in <i>variable</i>. See <i>prepend-path</i> or <i>append-path</i> for further explanation of using an arbitrary delimiter. Every string between colons, or delimiters, in <i>variable</i> is compared to <i>value</i>. If the two match, <i>value</i> is removed from <i>variable</i>.</dl>
<p> <code>prereq</code> <i>modulefile</i> [ <i>modulefile</i> &#8230; ]<br />
 <code>conflict</code> <i>modulefile</i> [ <i>modulefile</i> &#8230; ]</p>
<dl>
<dd><code>prereq</code> and <code>conflict</code> control whether or not the <i>modulefile</i> will be loaded. The <code>prereq</code> command lists modulefiles which must have been previously loaded before the current <i>modulefile</i> will be loaded. Similarly, the <code>conflict</code> command lists modulefiles which conflict with the current <i>modulefile</i>. If a list contains more than one <i>modulefile</i>, then each member of the list acts as a Boolean OR operation. Multiple <code>prereq</code> and <code>conflict</code> commands may be used to create a Boolean AND operation. If one of the requirements have not been satisfied, an error is reported and the current <i>modulefile</i> makes no changes to the user&#8217;s environment. </p>
<p> If an argument for <code>prereq</code> is a directory and any <i>modulefile</i> from the directory has been loaded, then the prerequisite is met. For example, specifying <i>X11</i> as a prereq means that any version of <i>X11</i>, <i>X11/R4</i> or <i>X11/R5</i>, must be loaded before proceeding. </p>
<p> If an argument for <code>conflict</code> is a directory and any other <i>modulefile</i> from that directory has been loaded, then a conflict will occur. For example, specifying <i>X11</i> as a conflict will stop <i>X11/R4</i> and <i>X11/R5</i> from being loaded at the same time.</dl>
<p> <code>is-loaded</code> <i>modulefile</i> [ <i>modulefile</i> &#8230; ]</p>
<dl>
<dd>The <code>is-loaded</code> command returns a true value if any of the listed modulefiles has been loaded. If a list contains more than one <i>modulefile</i>, then each member acts as a boolean OR operation. If an argument for <code>is-loaded</code> is a directory and any <i>modulefile</i> from the directory has been loaded <code>is-loaded</code> would return a true value.</dl>
<p> <code>module</code> [ <i>sub-command</i> ] [ <i>sub-command-args</i> ]</p>
<dl>
<dd>Contains the same sub-commands as described in the <code><a href="/docs/linux/man/1-module/">module</a></code>(1) man page in the Module Sub-Commands section. This command permits a <i>modulefile</i> to load or remove other modulefiles. No checks are made to ensure that the <i>modulefile</i> does not try to load itself. Often it is useful to have a single <i>modulefile</i> that performs a number of <code>module load</code> commands. For example, if every user on the system requires a basic set of applications loaded, then a <i>core</i> <i>modulefile</i> would contain the necessary <code>module load</code> commands.</dl>
<p> <code>module-info</code> <i>option</i> [ <i>info-args</i> ]</p>
<dl>
<dd>Provide information about the <code>modulecmd</code> program&#8217;s state. Some of the information is specific to the internals of <code>modulecmd</code>. <i>option</i> is the type of information to be provided, and <i>info-args</i> are any arguments needed.</p>
<dl>
<dt><code>module-info type</code></p>
<dd>
<dl>
<dd>Returns either &quot;C&quot; or &quot;Tcl&quot; to indicate which module command is being executed, either the &quot;C&quot; version or the Tcl-only version, to allow the modulefile writer to handle any differences between the two.</dl>
<p> <code>module-info flags</code></p>
<dl>
<dd>Returns the integer value of <code>modulecmd&#8217;s</code> flags state.</dl>
<p> <code>module-info mode [</code><i>modetype</i>]</p>
<dl>
<dd>Returns the current <code>modulecmd&#8217;s</code> mode as a string if no <i>modetype</i> is given. </p>
<p> Returns 1 if <code>modulecmd&#8217;s</code> mode is <i>modetype</i>. <i>modetype</i> can be: <i>load, remove, display, help, whatis, switch, switch1, switch2,</i> or <code>switch3.</code></dl>
<dt><code>module-info name</code></p>
<dd>
<dl>
<dd>Return the name of the <i>modulefile</i>. This is not the full pathname for <i>modulefile</i>. See the Modules Variables section for information on the full pathname.</dl>
<dt><code>module-info specified</code></p>
<dd>
<dl>
<dd>Return the name of the <i>modulefile</i> specified on the command line.</dl>
<dt><code>module-info shell</code></p>
<dd>
<dl>
<dd>Return the current shell under which <i>modulecmd</i> was invoked. This is the first parameter of <i>modulecmd</i>, which is normally hidden by the <i>module</i> alias.</dl>
<dt><code>module-info shelltype</code></p>
<dd>
<dl>
<dd>Return the family of the shell under which <i>modulefile</i> was invoked. As of <i>module-info shell</i> this depends on the first parameter of <i>modulecmd</i>. The output reflects a shell type determining the shell syntax of the commands produced by <i>modulecmd</i>.</dl>
<dt><code>module-info alias </code><i>name</i></p>
<dd>
<dl>
<dd>Returns the full module file name to which the module file alias <i>name</i> is assigned</dl>
<dt><code>module-info version </code><i>module-file</i></p>
<dd>
<dl>
<dd>Returns a list of all symbolic versions assigned to the passed <i>module-file</i>. The paremeter <i>module-file</i> might either be a full qualified module file with name and version, another symbolic module file name or a module file alias.</dl>
</dl>
</dl>
<p> <code>module-version</code> <i>module-file</i> <i>version-name [version-name &#8230;]</i></p>
<dl>
<dd>Assigns the symbolic <i>version-name</i> to the module file <i>module-file</i> This command should be placed in one of the modulecmd rc files in order to provide shorthand invocations of frequently used module file names. </p>
<p> The special <i>version-name</i> <code>default</code> specifies the default version to be used for module commands, if no specific version is given. This replaces the definitions made in the <i>.version</i> file in former <code>modulecmd</code> releases. </p>
<p> The parameter <i>module-file</i> may be either </p>
<dl>
<dd><i>a fully qualified modulefile</i> with name and version</dl>
<dl>
<dd><i>a symbolic module file name</i></dl>
<dl>
<dd><i>another module file alias</i></dl>
</dl>
<p> <code>module-alias</code> <i>name</i> <i>module-file</i></p>
<dl>
<dd>Assignes the module file <i>module-file</i> to the alias <i>name</i>. This command should be placed in one of the modulecmd rc files in order to provide shorthand invocations of frequently used module file names. </p>
<p> The parameter <i>module-file</i> may be either </p>
<dl>
<dd><i>a fully qualified modulefile</i> with name and version</dl>
<dl>
<dd><i>a symbolic module file name</i></dl>
<dl>
<dd><i>another module file alias</i></dl>
</dl>
<p> <code>module-trace</code> <i>{on|off}</i> <i>[command [command &#8230;]]</i> <i>[-module modulefile [modulefile &#8230;]]</i></p>
<dl>
<dd>Switches tracing on or off. Without parameters this command will affect globally all tracing setups for all commands and modulefiles. The <i>command</i> parameter may be used to affect tracing of specified module commands only and the switch <i>-module</i> finally limits the affect of the <i>module-trace</i> command to a well defined set of module files. </p>
<p> The <i>command</i> may be one of the following </p>
<dl>
<dd><i>avail</i> &#8211; &#8216;module avail&#8217; command</dl>
<dl>
<dd><i>clear</i> &#8211; &#8216;module clear&#8217; command</dl>
<dl>
<dd><i>display</i> &#8211; &#8216;module display&#8217; command</dl>
<dl>
<dd><i>init</i> &#8211; &#8216;module init&#8217; command</dl>
<dl>
<dd><i>help</i> &#8211; &#8216;module help&#8217; command</dl>
<dl>
<dd><i>list</i> &#8211; &#8216;module list&#8217; command</dl>
<dl>
<dd><i>load</i> &#8211; &#8216;module load&#8217; command</dl>
<dl>
<dd><i>purge</i> &#8211; &#8216;module purge&#8217; command</dl>
<dl>
<dd><i>switch</i> &#8211; &#8216;module switch&#8217; command</dl>
<dl>
<dd><i>unuse</i> &#8211; &#8216;module unuse&#8217; command</dl>
<dl>
<dd><i>unload</i> &#8211; &#8216;module unload&#8217; command</dl>
<dl>
<dd><i>update</i> &#8211; &#8216;module update&#8217; command</dl>
<dl>
<dd><i>use</i> &#8211; &#8216;module use&#8217; command</dl>
<p> The <i>module</i> parameter specifies a set of module files using TCL regular expressions. For example </p>
<dl>
<dd><i>.*</i> will affect all module files</dl>
<dl>
<dd><i>*/2.0</i> affects all module files at version 2.0</dl>
<dl>
<dd><i>gnu/.*</i> affects all versions of the gnu modulefile</dl>
<dl>
<dd><i>gnu/2.0</i> affects only version 2.0 of the gnu modulefile</dl>
<p> The <i>module</i> parameter is prepended to the current tracing pattern list for the specified module command. It is evaluated from the left to the right. The first matching pattern defines the tracing parameter. </p>
<p> The internal trace pattern list is stored as a colon separated list. In advanced user level only, colons may be specified on the <i>module</i> parameter of the <i>module-trace</i> command. This will directly take effect in the internal trace pattern list. In novice or expert user level a warning messge will be generated.</dl>
<p> <code>module-user</code> <i>level</i></p>
<dl>
<dd>Defines the user level under wich <i>module-cmd</i> runs. This takes effect on the error messages being produced and on the behavior of <i>modulecmd</i> in case of detecting an outage. </p>
<p> The <i>level</i> parameter specifies the user level and may be one of the following values: </p>
<dl>
<dd><i>advanced, adv</i> &#8211; advanced user level</dl>
<dl>
<dd><i>expert, exp</i> &#8211; expert user level</dl>
<dl>
<dd><i>novice, nov</i> &#8211; novice user level</dl>
</dl>
<p> <code>module-verbosity</code> <i>{on|off}</i></p>
<dl>
<dd>Switches verbose <i>modulecmd</i> message display on or off.</dl>
<p> <code>module-log</code> <i>error-weight</i> <i>log-facility</i></p>
<dl>
<dd>Defines whether error messages of the specified weight should be logged and conditionally assignes a log-facility. </p>
<p> The <i>error-weight</i> parameter specifies the error level to be logged. It may be one of the following values: </p>
<dl>
<dd><i>verb</i> &#8211; verbose messages</dl>
<dl>
<dd><i>info</i> &#8211; informal messages</dl>
<dl>
<dd><i>debug</i> &#8211; debugging messages</dl>
<dl>
<dd><i>trace</i> &#8211; tracing output</dl>
<dl>
<dd><i>warn</i> &#8211; warnings</dl>
<dl>
<dd><i>prob</i> &#8211; problems (normally the modulecmd may be completed)</dl>
<dl>
<dd><i>error</i> &#8211; errors (which normally leads to unsuccessful end of the modulecmd)</dl>
<dl>
<dd><i>fatal</i> &#8211; fatal system errors</dl>
<dl>
<dd><i>panic</i> &#8211; very fatal system errors, e.g. internal program inconsistencies.</dl>
<p> The <i>log-facility</i> parameter specifies the log destination. This may either switch off logging for the specified <i>error-weight</i>, direct log messages to a special stream or a file or specify a syslog facility for logging. The following values are allowed: </p>
<dl>
<dd><i>stderr, stdout</i> &#8211; predefined output streams for normal and error outputs. Note, that stdout is normally used for passing parameters to the invoking shell. Directing error output to this stream might screw up the <i>modulecmd</i> integration to your shell.</dl>
<dl>
<dd><i>a syslog facility</i> &#8211; directs logging to the syslog. See <code><a href="/docs/linux/man/4-syslog-conf/">syslog.conf</a>(4)</code> for detailed description of the valid syslog facilities.</dl>
<dl>
<dd><i>null, none</i> &#8211; will suppress logging of the specified <i>error-weight</i>.</dl>
<dl>
<dd><i>a filename</i> &#8211; is recognized by the first character being either a &#8216;.&#8217; or a &#8216;/&#8217;. You must have write permission to the file you specify.</dl>
</dl>
<p> <code>module-whatis</code> <i>string</i></p>
<dl>
<dd>Defines a string which is displayed in case of the invocation of the &#8216;module whatis&#8217; command. There may be more than one <i>module-whatis</i> line in a modulefile. This command takes no actions in case of load, display, etc. invocations of <i>modulecmd</i>. </p>
<p> The <i>string</i> parameter has to be enclosed in double-quotes if there&#8217;s more than one word specified. Words are defined to be separated by whitespace characters (space, tab, cr).</dl>
<p> <code>set-alias</code> <i>alias-name</i> <i>alias-string</i></p>
<dl>
<dd>Sets an alias or function with the name <i>alias-name</i> in the user&#8217;s environment to the string <i>alias-string</i>. Arguments can be specified using the Bourne Shell style of function arguments. If the string contains &quot;$1&quot;, then this will become the first argument when the alias is interpreted by the shell. The string &quot;$*&quot; corresponds to all of the arguments given to the alias. The character &#8216;$&#8217; may be escaped using the &#8216;\&#8217; character. </p>
<p> For some shells, aliases are not possible and the command has no effect. For Bourne shell derivatives, a shell function will be written (if supported) to give the impression of an alias. When a <i>modulefile</i> is unloaded, <code>set-alias</code> becomes <code>unset-alias</code>.</dl>
<p> <code>unset-alias</code> <i>alias-name</i></p>
<dl>
<dd>Unsets an alias with the name <i>alias-name</i> in the user&#8217;s environment. If the shell supports functions then the shell is instructed to unset function <i>alias-name</i>.</dl>
<p> <code>system</code> <i>string</i></p>
<dl>
<dd>Pass <i>string</i> to the C library routine <code><a href="/docs/linux/man/3-system/">system</a></code>(3). For the <code><a href="/docs/linux/man/3-system/">system</a></code>(3) call <code>modulecmd</code> redirects stdout to stderr since stdout would be parsed by the evaluating shell. The exit status of the executed command is returned.</dl>
<p> <code>uname</code> <i>field</i></p>
<dl>
<dd>Provide fast lookup of system information on systems that support <code><a href="/docs/linux/man/3-uname/">uname</a></code>(3). <code>uname</code> is significantly faster than using <code>system</code> to execute a program to return host information. If <code><a href="/docs/linux/man/3-uname/">uname</a></code>(3) is not available, <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3) or some program will make the nodename available. <code>uname</code> will return the string &quot;unknown&quot; if information is unavailable for the <i>field</i>. </p>
<p> <code>uname</code> will invoke <code>getdomainname</code> in order to figure out the name of the domain. </p>
<p> <i>field</i> values are: </p>
<dl>
<dd><i>sysname</i> &#8211; the operating system name</dl>
<dl>
<dd><i>nodename</i> &#8211; the hostname</dl>
<dl>
<dd><i>domain</i> &#8211; the name of the domain</dl>
<dl>
<dd><i>release</i> &#8211; the operating system release</dl>
<dl>
<dd><i>version</i> &#8211; the operating system version</dl>
<dl>
<dd><i>machine</i> &#8211; a standard name that identifies the system&#8217;s hardware</dl>
</dl>
<p> <code>x-resource</code> <i>resource-string</i><br />
 <code>x-resource</code> <i>filename</i></p>
<dl>
<dd>Merge resources into the <i>X11</i> resource database. The resources are used to control look and behavior of <i>X11</i> applications. The command will attempt to read resources from <i>filename</i>. If the argument isn&#8217;t a valid file name, then string will be interpreted as a resource. If a file is found, it will be filtered through the <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) preprocessor, just as <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1) would do. </p>
<p> modulefiles that use this command, should in most cases contain one or more <i>x-resource</i> lines, each defining one <i>X11</i> resource. Reading resources from <i>filename</i> is much slower, due to the preprocessing. The DISPLAY environment variable should be properly set and the <i>X11</i> server should be accessible. If <code>x-resource</code> can&#8217;t manipulate the <i>X11</i> resource database, the <i>modulefile</i> will exit with an error message. </p>
<p> Examples:</p>
<dl>
<dt><code>x-resource /u2/staff/leif/.xres/Ileaf</code></p>
<dd>
<dl>
<dd>The file <i>Ileaf</i> is preprocessed by <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) and the result is merged into the <i>X11</i> resource database.</dl>
<dt><code>x-resource [glob ~/.xres/ileaf]</code></p>
<dd>
<dl>
<dd>The Tcl <i>glob</i> function is used to have the <i>modulefile</i> read different resource files for different users.</dl>
<dt><code>x-resource {Ileaf.popup.saveUnder: True}</code></p>
<dd>
<dl>
<dd>Merge the <i>Ileaf</i> resource into the <i>X11</i> resource database.</dl>
</dl>
</dl>
<h2>Modules Variables</h2>
<p>The <code>ModulesCurrentModulefile</code> variable contains the full pathname of the <i>modulefile</i> being interpreted.</p>
<h2>Locating Modulefiles</h2>
<p>Every directory in <font SIZE="-1">MODULEPATH</font> is searched to find the <i>modulefile</i>. A directory in <font SIZE="-1">MODULEPATH</font> can have an arbitrary number of sub-directories. If the user names a <i>modulefile</i> to be loaded which is actually a directory, the directory is opened and a search begins for an actual <i>modulefile</i>. First, <code>modulecmd</code> looks for a file with the name <i>.modulerc</i> in the directory. If this file exists, its contents will be evaluated as if it was a module file to be loaded. You may place <i>module-version</i> and <i>module-alias</i> commands inside this file. Additionally, before seeking for <i>.modulerc</i> files in the module directory, the global <i>.modulerc</i> file is sourced, too. If a named version <i>default</i> now exists for the module file to be loaded, the assigned modulefile now will be sourced. Otherwise the file <i>.version</i> is looked up in the directory. If the <i>.version</i> file exists, it is opened and interpreted as Tcl code and takes precedence over a <i>.modulerc</i> file in the same directory. If the Tcl variable <code>ModulesVersion</code> is set by the <i>.version</i> file, <code>modulecmd</code> will use the name as if it specifies a <i>modulefile</i> in the directory. This will become the <i>default</i> module file in this case. If <code>ModulesVersion</code> is a directory, the search begins anew down that directory. If the name does not match any files located in the current directory, the search continues through the remaining directories in <font SIZE="-1">MODULEPATH</font>. </p>
<p> Every <i>.version</i> and <i>.modulerc</i> file found is Tcl interpreted. So, changes made in these file will affect the subsequently interpreted <i>modulefile</i>. </p>
<p> If no <i>default</i> version may be figured out, then the highest lexicographically sorted <i>modulefile</i> under the directory using the &#8216;C&#8217; locale will be used. </p>
<p> For example, it is possible for a user to have a directory named <i>X11</i> which simply contains a <i>.version</i> file specifying which version of <i>X11</i> is to be loaded. Such a file would look like: </p>
<dl>
<dd>
<pre>#%Module1.0
##
## The desired version of <i>X11</i>
##
set ModulesVersion &quot;R4&quot;</pre>
</dl>
<h2>Modulefile Specific Help</h2>
<p>Users can request help about a specific <i>modulefile</i> through the <code><a href="/docs/linux/man/1-module/">module</a></code>(1) command. The <i>modulefile</i> can print helpful information or start help oriented programs by defining a <code>ModulesHelp</code> subroutine. The subroutine will be called when the &#8216;module help <i>modulefile</i>&#8216; command is used.</p>
<h2>Modulefile Display</h2>
<p>The &#8216;module display <i>modulefile</i>&#8216; command will detail all changes that will be made to the environment. After displaying all of the environment changes <code>modulecmd</code> will call the <code>ModulesDisplay</code> subroutine. The <code>ModulesDisplay</code> subroutine is a good place to put additional descriptive information about the <i>modulefile</i>.</p>
<h2>Environment</h2>
<dl>
<dt><code>${</code><font SIZE="-1"><code>MODULEPATH</code></font><code>}</code></p>
<dd>Path of directories containing <i>modulefiles</i>.</dl>
<h2>Version</h2>
<p>3.2.10</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-module/">module</a></code>(1), <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3), <code><a href="/docs/linux/man/3-tclx/">TclX</a></code>(3), <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1), <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1), <code><a href="/docs/linux/man/3-system/">system</a></code>(3), <code><a href="/docs/linux/man/3-uname/">uname</a></code>(3), <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3) <code><a href="/docs/linux/man/3-getdomainname/">getdomainname</a></code>(3)</p>
<h2>Notes</h2>
<p>Tcl was developed by John Ousterhout at the University of California at Berkeley. TclX was developed by Karl Lehenbauer and Mark Diekhans. </p>
