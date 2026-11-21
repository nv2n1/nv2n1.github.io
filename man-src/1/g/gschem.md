---

title: "gschem(1)"
name: "gschem"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gschem/"
description: "gschem – gEDA/gaf Schematic Capture"
---

<p> gschem &#8211; gEDA/gaf Schematic Capture</p>
<h2>SYNOPSIS</h2>
<p> <code>gschem</code> [-q] [-v] [-t] [-r rcfilename] [-s scriptfilename] [-o outputfilename] [-p] [-h] [schematic1 &#8230; schematicN]</p>
<h2>DESCRIPTION</h2>
<p> <i>gschem</i> is the schematic capture program which is part gEDA (GPL Electronic Design Automation) toolset. This program is used to draw electronic schematics. Schematics consist of standard symbols (which are either part of a standard library or created by the user) which represent the various gates and components. These components are then interconnected by nets (wires). Schematics may be printed to a PostScript file for printing or further conversion to other output formats. Output to various image formats is also supported. </p>
<p> <i>gschem</i> is also the symbol creation editor. All the standard methods of creating schematics are used in the creation of symbols. There are a few special rules when creating symbols, so please refer to the (non-existant as of now) symbol creation document. </p>
<p> Please read the official documentation (very minimal at this point) on how to use <i>gschem</i>, since this man page just describes the command line arguments and a few examples on how to run <i>gschem</i>. </p>
<h2>OPTIONS</h2>
<p> <i>gschem</i> accepts the following options:</p>
<dl>
<dt><code>-q</code></dt>
<dd> Quiet mode on. This mode turns off all warnings/notes/messages. (optional)</dd>
<dt><code>-v </code></dt>
<dd> Verbose mode on. This mode gives as much feedback to the user as possible. (optional)</dd>
<dt><code>-t </code></dt>
<dd> Print out more information when using mouse strokes. With this command line flag and the middle button configured for mouse strokes, gschem will output the stroke sequence numbers as the user executes strokes. These numbers can be used to define new strokes in the system-gschemrc file.</dd>
<dt><code>-r filename</code></dt>
<dd> Specify a rc filename. Normally <i>gschem</i> searches for the system-gschemrc, then ~/.gEDA/gschemrc, and finally for a gschemrc in the current directory. This options allows the user to specify an additional rc file which is read after all the other rc files are read. (optional)</dd>
<dt><code>-s filename</code></dt>
<dd> Specify a guile script to be executed at startup. (optional)</dd>
<dt><code>-o filename</code></dt>
<dd> Specify a filename for postscript output. This command line argument is useful when running <i>gschem</i> from a shell script and with a guile script. The filename can be changed through the print dialog box.</dd>
<dt><code>-p </code></dt>
<dd> Automatically place the window, especially useful if running gschem from the command line and generating output.</dd>
<dt><code>-h </code></dt>
<dd> Print out short command line help.</dd>
<dt><code>schematic1 [&#8230; schematicN]</code></dt>
<dd> Schematic file to be loaded. Specifing a schematic file is optional. If multiple schematic files are specified they are read in sequentially and put on seperate pages. It is important that the schematic(s) follow all the options (ie last). </dd>
</dl>
<h2>EXAMPLES</h2>
<p> These examples assume that you have a schematic called stack_1.sch in the current directory </p>
<p> To run <i>gschem</i> and then interact with the program: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gschem </p>
<p> To run <i>gschem</i> in interactive mode but load a sample schematic: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gschem adders_1.sch</p>
<p> To run <i>gschem</i> and load up all schematics in the current subdirectory: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gschem *.sch</p>
<h2>ENVIRONMENT</h2>
<p> <i>gschem</i> respects the following environment variable: </p>
<dl>
<dt><code>GEDADATA </code></dt>
<dd> specifies where the various required scheme and rc files are located (the default is ${prefix}/share/gEDA). This environment variables does not need to be set by the end user unless they are moving the executables to a new install ${prefix}. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Ales Hvezda and many others </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnetlist/">gnetlist</a></code>(1), <code><a href="/docs/linux/man/1-gsymcheck/">gsymcheck</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<pre>
Copyright &#169;  1999-2008 Ales Hvezda
This document can be freely redistributed according to the terms of the 
GNU General Public License version 2.0
</pre>
