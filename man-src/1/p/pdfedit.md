---
title: "pdfedit(1)"
name: "pdfedit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfedit/"
description: "pdfedit – Editor for PDF files"
---

<h2>NAME</h2>
<p> pdfedit &#8211; Editor for PDF files</p>
<h2>SYNOPSIS</h2>
<p> pdfedit [file(s)] [&#8211;help] [&#8211;version] [-d (n)] [-console] [-script (filename)] [-run (filename)] [-eval (code)] [-s (filename)] [&#8211;]</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;help</i></p>
<dd> Print brief help about commandline options to STDOUT and exit</p>
<dt><i>&#8211;version</i></p>
<dd> Print version of editor to STDOUT and exit</p>
<dt><i>-d (n)</i></p>
<dd> Set verbosity of debugging messages reported by editor. Only messages below or equal level specified in parameter will be shown, default is debugging level 1. Also, any of symbolic constants defined below (case insensitive), or starting part of them may be given instead of corresponding number. </p>
<p> <code>Explanation of debugging levels</code><br />
&nbsp;<wbr> <code>0</code> <code>PANIC</code> <code>Critical errors</code><br />
&nbsp;<wbr> <code>1</code> <code>CRITICAL</code> <code>Critical errors, but at least the program can exit somewhat gracefully</code><br />
&nbsp;<wbr> <code>2</code> <code>ERROR</code> <code>Usual errors</code><br />
&nbsp;<wbr> <code>3</code> <code>WARNING</code> <code>Comments about some unusual behavior</code><br />
&nbsp;<wbr> <code>4</code> <code>INFO</code> <code>Information about some internal behavior</code><br />
&nbsp;<wbr> <code>5</code> <code>DEBUG</code> <code>Debugging messages</code><br />
&nbsp;<wbr> Setting this to -1 mean no debug messages will be shown at all, not even the most critical ones. Debugging messages are sent to STDERR.</p>
<dt><i>-console</i></p>
<dd> Run in commandline mode. No editor windows are opened and commandline init script is executed.</p>
<dt><i>-script (filename)</i></p>
<dd> Run script with given filename. Look for the script in script path. If not found, look for the script in current directory.</p>
<dt><i>-run (filename)</i></p>
<dd> Run script with given filename, but unlike <code>-script</code> option, script path is not searched.</p>
<dt><i>-eval (code)</i></p>
<dd> Evaluate given script code</p>
<dt><i>-s (filename)</i></p>
<dd> This is just shortcut for <code>-console -script (filename)</code></p>
<dt><i>&#8212;</i></p>
<dd> Stop processing options. Any further parameters after this one are treated as filenames. This can be useful if you want to open file, that have name beginning with a dash.</dl>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr>You can specify any number of filenames as parameters on commandline. One window will be opened for each file specified. If no file is specified on commandline, editor will be loaded initially empty.&nbsp;<wbr><br />
&nbsp;<wbr>Name of files can be mixed with options&nbsp;<wbr>(parameter that begin with a dash). Invalid option on commandline will cause editor to abort with error message. Names of options are case sensitive.&nbsp;<wbr><br />
&nbsp;<wbr>Options which require a parameter can be specified in&nbsp;<wbr>&quot;short form&quot;, like <code>-d1</code> or &quot;long form&quot;, like <code>-d 1</code> , both of these mean option <code>-d</code> with parameter <code>1</code><br />
&nbsp;<wbr>Use <code>-script</code> , <code>-eval</code> and <code>-run</code> options to run any script besides the init script. These parameters are run/evaluated in the order they are specified on commandline and may be specified multiple times. If these parameters are specified in GUI mode, they are used in each window opened on program start, in commandline mode (console mode) they are used after commandline init script. After these scripts finish execution, the editor terminates.</p>
<h2>LOCALIZATION</h2>
<p>&nbsp;<wbr>PDF Editor is run in english language by default, but by setting environment variable <code>LANG</code> before launching the program, you can tell PDF Editor to look for specific language file. If the localization you requested is not available, english will be used instead.<br />
&nbsp;<wbr>Aside default english, these localizations are available:<br />
&nbsp;<wbr> <code>cs</code> <code>&#8211; Czech</code><br />
&nbsp;<wbr> <code>de</code> <code>&#8211; German</code><br />
&nbsp;<wbr> <code>es</code> <code>&#8211; Spanish</code><br />
&nbsp;<wbr> <code>ru</code> <code>&#8211; Russian</code><br />
&nbsp;<wbr> <code>fr</code> <code>&#8211; French</code><br />
&nbsp;<wbr> <code>zh_TW</code> <code>&#8211; Chinese (traditional)</code><br />
&nbsp;<wbr> </p>
<h2>Index</h2>
