---
title: "magic(1)"
name: "magic"
section: "1"
letter: "m"
url: "/docs/linux/man/1-magic/"
description: "magic – VLSI layout editor"
---

<h2 class="name">NAME</h2>
<p> magic &#8211; VLSI layout editor </p>
<h2>SYNOPSIS</h2>
<p> <code>magic</code> [ <code>-T&nbsp;<wbr></code> <i>technology</i> ] [ <code>-d&nbsp;<wbr></code> <i>device_type</i> ] [ <code>-g&nbsp;<wbr></code> <i>graphics_port</i> ] [ <code>-m&nbsp;<wbr></code> <i>monitor_type</i> ] [ <code>-D</code> ] [ <i>file</i> ] </p>
<h2>DESCRIPTION</h2>
<p> Magic is an interactive editor for VLSI layouts that runs under all variants of UNIX, including Mac OS-X and Cygwin. This man page is a reference manual; if you are a first-time user, you should use the Magic tutorials to get acquainted with the system (see the online resources links below). </p>
<p> Magic uses two windows: one for text and a separate window for displaying layouts. Magic runs under the window system X11 (use under Cygwin requires the presence of an X11 server in Windows; the server that comes packaged with Cygwin works well). The command line switch &quot;-d&quot; can be used to tell Magic which kind of display you are running. Specifically, this is useful to tell magic to use OpenGL graphics instead of plain X11 (&quot;-d OGL&quot;), or to use 24 bit plane graphics instead of 8 bit planes (&quot;-d 24BITS&quot;) if both are available on a video card with overlay support. </p>
<p> Here are the options accepted by Magic:</p>
<dl>
<dt><code>-T</code></p>
<dd> The next argument is the name of a technology. The tile types, display information, and design rules for this technology are read by Magic from a technology file when it starts up. The technology defaults to &#8220;scmos&#8221;.</p>
<dt><code>-d</code></p>
<dd> The next argument is the type of workstation or graphics display being used. Magic supports these types:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>NULL</code></p>
<dd> A null device for running Magic without using a graphics display, such as a batch job. Note that the special case &quot;-dnull&quot; (lowercase, no space) has a more streamlined startup specifically for batch processing.</p>
<dt><code>X11</code></p>
<dd> X-windows, version 11. The is the preferred interface. Magic acts as a client to the X window server and interfaces to all graphics terminals supported by the X server.</p>
<dt><code>OGL</code></p>
<dd> OpenGL graphics running under X11. This is the preferred interface on systems having hardware-accelerated 3D graphics video cards and drivers.</p>
<dt>
<dd> Addition information on Magic&#8217;s X11 driver, including options for .Xdefaults files, may be found in &#8220;Magic Maintainer&#8217;s Manual #4: Using Magic Under X Windows&#8221;.</p>
<dt><code>XWIND</code></p>
<dd> Simply another name for the X11 driver.</dl>
</dl>
<p> If no device is specified, Magic tries to guess which driver is appropriate (by checking the environment variables and by poking around in /dev).</dl>
<p> When Magic starts up it looks for a command file in ${CAD_ROOT}/magic/sys/.magicrc and processes it if it exists. Then Magic looks for a file with the name &#8220;.magicrc&#8221; in the home directory and processes it if it exists. Finally, Magic looks for a .magicrc file in the current directory and reads it as a command file if it exists. The .magicrc file format is described under the <code>source</code> command. If magic is compiled with Tcl/Tk support, then any magic or Tcl/Tk commands may be used inside the startup file. The startup file name was changed to &quot;.magicrc&quot; to avoid conflicts with a common system file named &quot;.magic&quot;. However, the name &quot;.magic&quot; will be searched after &quot;.magicrc&quot; for backward compatibility. </p>
<h2>COMMANDS &#8212; GENERAL INFORMATION</h2>
<p> Magics uses types of commands: Key macros and long commands. The first form consists of single-key (or button) abbreviations called &#8220;macros&#8221;; macros are invoked by pressing a single key or mouse button. Certain macros are predefined in the systemwide ${CAD_ROOT}/magic/sys/.magicrc file, but you can override them and add your own macros using the <code>macro</code> command (described below under COMMANDS FOR ALL WINDOWS). The special macro &quot;.&quot; is reserved to mean &quot;execute the last typed long command&quot;. </p>
<p> You can enter long commands in the terminal console at the console prompt, or from the layout window by typing a <code>:</code> or <code>;</code> key, which are the two other reserved macros meaning &quot;switch keyboard focus to the console window&quot;. After typing the <code>:</code> or <code>;</code> key, type the text of the command, which will be written to the terminal window. Multiple commands may be specified on one line by separating them with semicolons. </p>
<p> Most commands deal with the window underneath the cursor, so if a command doesn&#8217;t do what you expect make sure that you are pointing to the correct place on the screen. There are several different kinds of windows in Magic (layout, color, and netlist); each window has a different command set, described in a separate section below. </p>
<h2>MOUSE BUTTONS FOR LAYOUT WINDOWS</h2>
<p> Magic uses a three button mouse. The buttons are interpreted in a way that depends on the current tool, as indicated by the shape of the cursor (see the <code>tool</code> command). The various tools are described below. The initial tool is <code>box</code>. These interpretations apply only when mouse buttons are pressed in the interior of a layout window.</p>
<dl>
<dt><code>Box Tool</code></p>
<dd> This is the default tool, and is indicated by a crosshair cursor. It is used to position the box and to paint and erase:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>left</code></p>
<dd> This button is used to move the box by one of its corners. Normally, this button picks up the box by its lower-left corner. To pick the box up by a different corner, click the right button while the left button is down. This switches the pick-up point to the corner nearest the cursor. When the button is released, the box is moved to position the corner at the cursor location. If the box has been set to snap to the window&#8217;s grid (see the <code>:snap</code> command), then the box corner is left aligned with the grid that the user has chosen for the window with the <code>:grid</code> command, even if that grid is not visible.</p>
<dt><code>right</code></p>
<dd> Change the size of the box by moving one corner. Normally this button moves the upper-right corner of the box. To move a different corner, click the left button while the right button is down. This switches the corner to the one nearest the cursor. When you release the button, three corners of the box move in order to place the selected corner at the cursor location (the corner opposite the one you picked up remains fixed). Snapping to the window&#8217;s grid is handled as for the left button.</p>
<dt><code>middle (bottom)</code></p>
<dd> Used to paint or erase. If the crosshair is over paint, then the area of the box is painted with the layer(s) underneath the crosshair. If the crosshair is over white space, then the area of the box is erased.</dl>
</dl>
<dt><code>Wiring Tool</code></p>
<dd> The wiring tool, indicated by an arrow cursor, is used to provide an efficient interface to the wiring commands:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>left</code></p>
<dd> Same as the long command <code>wire type</code>.</p>
<dt><code>right</code></p>
<dd> Same as the long command <code>wire leg</code>.</p>
<dt><code>middle (bottom) </code></p>
<dd> Same as the long command <code>wire switch</code>.</dl>
</dl>
<dt><code>Netlist Tool</code></p>
<dd> This tool is used to edit netlists interactively. It is indicated by a thick box cursor.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>left</code></p>
<dd> Select the net associated with the terminal nearest the cursor.</p>
<dt><code>right</code></p>
<dd> Find the terminal nearest the cursor, and toggle it into the current net (if it wasn&#8217;t already in the current net) or out of the current net (if it was previously in the net).</p>
<dt><code>middle (bottom) </code></p>
<dd> Find the terminal nearest the cursor, and join its net with the current net.</dl>
</dl>
<dt><code>Rsim Tool</code></p>
<dd> Used when running the IRSIM simulator under Magic. A pointing hand is used as the cursor.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>left</code></p>
<dd> Moves the box just like the box tool.</p>
<dt><code>right</code></p>
<dd> Moves the box just like the box tool.</p>
<dt><code>middle (bottom) </code></p>
<dd> Displays the Rsim node values of the selected paint.</dl>
</dl>
</dl>
<h2>LONG COMMANDS FOR LAYOUT WINDOWS</h2>
<p> These commands work if you are pointing to the interior of a layout window. Commands are invoked by typing a colon (&#8220;:&#8221;) or semi-colon (&#8220;;&#8221;), followed by a line containing a command name and zero or more parameters. In addition, macros may be used to invoke commands with single keystrokes. Useful default macros are set in the global <code>.magicrc</code> file (in <code>${CAD_ROOT}/magic/sys</code>, normally <code>/usr/local/lib/magic/sys</code>). You can list all current macros with the <code>macro</code> command, described under &#8220;LONG COMMANDS FOR ALL WINDOWS&#8221;. Unique abbreviations are acceptable for all keywords in commands. The commands are:</p>
<dl>
<dt><code>addpath </code><i>searchpath</i></p>
<dd> Add more directories to the end of Magic&#8217;s cell search path. See the documentation for the <code>path</code> command for an explanation of the search path.</p>
<dt><code>array </code><i>xsize ysize</i></p>
<dd> Make many copies of the selection. There will be <i>xsize</i> instances in the x-direction and <i>ysize</i> instances in the y-direction. Paint and labels are arrayed by copying them. Subcells are not copied, but instead each instance is turned into an array instance with elements numbered from 0 to <i>xsize</i>-1 in the x-direction, and from 0 to <i>ysize</i>-1 in the y-direction. The spacing between elements of the array is determined by the box x- and y-dimensions.</p>
<dt><code>array </code><i>xlo ylo xhi yhi</i></p>
<dd> Identical to the form of <code>array</code> above, except that the elements of arrayed cells are numbered left-to-right from <i>xlo</i> to <i>xhi</i> and bottom-to-top from <i>ylo</i> to <i>yhi</i>. It is legal for <i>xlo</i> to be greater than <i>xhi</i>, and also for <i>ylo</i> to be greater than <i>yhi</i>.</p>
<dt><code>box </code>[<i>args</i>]</p>
<dd> Used to change the size of the box or to find out its size. There are several sorts of arguments that may be given to this command:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>(No arguments.)</i></p>
<dd> Show the box size and its location in the edit cell, or root cell of its window if the edit cell isn&#8217;t in that window.</p>
<dt><i>direction</i> [<i>distance</i>]</p>
<dd> Move the box <i>distance</i> units in <i>direction</i>, which may be one of <code>left</code>, <code>right</code>, <code>up</code>, or <code>down</code>. <i>Distance</i> defaults to the width of the box if <i>direction</i> is <code>right</code> or <code>left</code>, and to the height of the box if <i>direction</i> is <code>up</code> or <code>down</code>.</p>
<dt><code>width [</code><i>size</i>]</p>
<dd>
<dt><code>height [</code><i>size</i>]</p>
<dd> Set the box to the width or height indicated. If <i>size</i> is not specified the width or height is reported.</p>
<dt><i>x1 y1 x2 y2</i></p>
<dd> Move the box to the coordinates specified (these are in edit cell coordinates if the edit cell is in the window under the cursor; otherwise these are in the root coordinates of the window). <i>x1</i> and <i>y1</i> are the coordinates of the lower left corner of the box, while <i>x2</i> and <i>y2</i> are the upper right corner. The coordinates must all be integers.</dl>
</dl>
<dt><code>calma </code>[<i>option</i>] [<i>args</i>]</p>
<dd> This command is used to read and write files in Calma GDS II Stream format (version 3.0, corresponding to GDS II Release 5.1). This format is like CIF, in that it describes physical mask layers instead of Magic layers. In fact, the technology file specifies a correspondence between CIF and Calma layers. The current CIF output style (see <code>cif ostyle</code>) controls how Calma stream layers are generated from Magic layers. If no arguments are given, the <code>calma</code> command generates a Calma stream file for the layout in the window beneath the cursor in <i>file</i><code>.strm</code>, where <i>file</i> is the name of the root cell. This stream file describes the entire cell hierarchy in the window. The name of the library is the same as the name of the root cell. <i>Option</i> and <i>args</i> may be used to invoke one of several additional operations:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>calma flatten</code></p>
<dd> Ordinarily, Magic arrays are output using the Calma ARRAY construct. After a <code>calma flatten</code> command, though, arrays will be output instead as a collection of individual cell uses, as occurs when writing CIF.</p>
<dt><code>calma help</code></p>
<dd> Print a short synopsis of all of the <code>calma</code> command options.</p>
<dt><code>calma labels</code></p>
<dd> Output labels whenever writing a Calma output file.</p>
<dt><code>calma lower</code></p>
<dd> Allow both upper and lower case to be output for label text. This is the default behavior; <code>calma nolower</code> causes lower case to be converted to upper case on output.</p>
<dt><code>calma noflatten</code></p>
<dd> Undoes the effect of a prior <code>:calma flatten</code> command, re-enabling the output of Magic arrays using the Calma ARRAY construct.</p>
<dt><code>calma nolabels</code></p>
<dd> Don&#8217;t output labels when writing a Calma output file.</p>
<dt><code>calma nolower</code></p>
<dd> Convert lower to upper case when outputting labels.</p>
<dt><code>calma read </code><i>file</i></p>
<dd> The file <i>file</i>.<code>strm</code> is read in Calma format and converted to a collection of Magic cells. The current CIF input style determines how the Calma layers are converted to Magic layers. The new cells are marked for design-rule checking. Calma format doesn&#8217;t identify the root of the collection of cells read in, so none of the cells read will appear on the display; use <code>load</code> to make them visible. If the Calma file had been produced by Magic, then the name of the root cell is the same as the library name printed by the <code>:calma read</code> command.</p>
<dt><code>calma write </code><i>fileName</i></p>
<dd> Writes a stream file just as if no arguments had been entered, except that the output is written into <i>fileName</i><code>.strm</code> instead of using the root cell name for the file name.</dl>
</dl>
<dt><code>channels</code></p>
<dd> This command will run just the channel decomposition part of the Magic router, deriving channels for the area under the box. The channels will be displayed as outlined feedback areas over the edit cell.</p>
<dt><code>cif </code>[<i>option</i>] [<i>args</i>]</p>
<dd> Read or write files in Caltech Intermediate Form (CIF). If no arguments are given, this command generates a CIF file for the window beneath the cursor in <i>file</i><code>.cif</code>, where <i>file</i> is the name of the root cell. The CIF file describes the entire cell hierarchy in the window. <i>Option</i> and <i>args</i> may be used to invoke one of several additional CIF operations:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cif arealabels </code>[<code>yes </code>|<code> no]</code></p>
<dd> Enables/disables the cif area-label extension. If enabled, area labels are written via the <code>95</code> cif extension. If disabled, labels are collapsed to points when writing cif and the <code>94</code> cif construct is used. Area-labels are disabled by default (many programs don&#8217;t understand cif area-labels).</p>
<dt><code>cif help</code></p>
<dd> Print a short synopsis of all of the cif command options.</p>
<dt><code>cif istyle </code>[<i>style</i>]</p>
<dd> Select the style to be used for CIF input. If no <i>style</i> argument is provided, then Magic prints the names of all CIF input styles defined in the technology file and identifies the current style. If <i>style</i> is provided, it is made the current style.</p>
<dt><code>cif ostyle </code>[<i>style</i>]</p>
<dd> Select the style to be used for CIF output. If no <i>style</i> argument is provided, then Magic prints the names of all CIF output styles defined in the technology file and identifies the current style. If <i>style</i> is provided, it is made the current style.</p>
<dt><code>cif read </code><i>file</i></p>
<dd> The file <i>file</i>.<code>cif</code> is read in CIF format and converted to a collection of Magic cells. The current input style determines how the CIF layers are converted to Magic layers. The new cells are marked for design-rule checking. Any information in the top-level CIF cell is copied into the edit cell. Note: this command is not undo-able (it would waste too much space and time to save information for undoing).</p>
<dt><code>cif see </code><i>layer</i></p>
<dd> In this command <i>layer</i> must be the CIF name for a layer in the current output style. Magic will display on the screen all the CIF for that layer that falls under the box, using stippled feedback areas. It&#8217;s a bad idea to look at CIF over a large area, since this command requires the area under the box to be flattened and therefore is slow.</p>
<dt><code>cif statistics</code></p>
<dd> Prints out statistics gathered by the CIF generator as it operates. This is probably not useful to anyone except system maintainers.</p>
<dt><code>cif write </code><i>fileName</i></p>
<dd> Writes out CIF just as if no arguments had been entered, except that the CIF is written into <i>fileName</i><code>.cif</code> instead of using the root cell name for the file name. The current output style controls how CIF layers are generated from Magic layers.</p>
<dt><code>cif flat </code><i>fileName</i></p>
<dd> Writes out CIF as in the <code>cif write</code> command, but flattens the design first (e.g. creates an internal version with the cell hierarchy removed). This is useful if one wishes to use the <code>and-not</code> feature of the CIF output styles, but is having problems with interactions of overlapping cells.</dl>
</dl>
<dt><code>clockwise </code>[<i>degrees</i>]</p>
<dd> Rotate the selection by <code>90</code>, <code>180</code> or <code>270</code> degrees. After the rotation, the lower-left corner of the selection&#8217;s bounding box will be in the same place as the lower-left corner of the bounding box before the rotation. <i>Degrees</i> defaults to <code>90</code>. If the box is in the same window as the selection, it is rotated too. Only material in the edit cell is affected.</p>
<dt><code>copy </code>[<i>direction </i>[<i>amount</i>]]</p>
<dd>
<dt><code>copy to </code><i>x y</i></p>
<dd> If no arguments are given, a copy of the selection is picking up at the point lying underneath the box lower-left corner, and placed so that this point lies at the cursor position. If <i>direction</i> is given, it must be a Manhattan direction (e.g. <code>north</code>, see the &#8220;DIRECTIONS&#8221; section below). The copy of the selection is moved in that direction by <i>amount</i>. If the box is in the same window as the selection, it is moved too. <i>Amount</i> defaults to <code>1</code>. The second form of the command behaves as though the cursor were pointing to (<i>x, y</i>) in the edit cell; a copy of the selection is picked up by the point beneath the lower-left corner of the box and placed so that this point lies at (<i>x</i>,<i>&nbsp;<wbr>y</i>).</p>
<dt><code>corner </code><i>direction1 direction2 </i>[layers]</p>
<dd> This command is similar to <code>fill</code>, except that it generates L-shaped wires that travel across the box first in <i>direction1</i> and then in <i>direction2</i>. For example, <code>corner north east</code> finds all paint under the bottom edge of the box and extends it up to the top of the box and then across to the right side of the box, generating neat corners at the top of the box. The box should be at least as tall as it is wide for this command to work correctly. <i>Direction1</i> and <i>direction2</i> must be Manhattan directions (see the section DIRECTIONS below) and must be orthogonal to each other. If <i>layers</i> is specified then only those layers are used; otherwise all layers are considered.</p>
<dt><code>delete</code></p>
<dd> Delete all the information in the current selection that is in the edit cell. When cells are deleted, only the selected use(s) of the cell is (are) deleted: other uses of the cell remain intact, as does the disk file containing the cell. Selected material outside the edit cell is not deleted.</p>
<dt><code>drc option </code>[<i>args</i>]</p>
<dd> This command is used to interact with the design rule checker. <i>Option</i> and <i>args</i> (if needed) are used to invoke a <code>drc</code> command in one of the following ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>drc catchup</code></p>
<dd> Let the checker process all the areas that need rechecking. This command will not return until design-rule checking is complete or an interrupt is typed. The checker will run even if the background checker has been disabled with <code>drc off</code>.</p>
<dt><code>drc check</code></p>
<dd> Mark the area under the box for rechecking in all cells that intersect the box. The recheck will occur in background after the command completes. This command is not normally necessary, since Magic automatically remembers which areas need to be rechecked. It should only be needed if the design rules are changed.</p>
<dt><code>drc count</code></p>
<dd> Print the number of errors in each cell under the box. Cells with no errors are skipped.</p>
<dt><code>drc find</code> [<i>nth</i>]</p>
<dd> Place the box over the <i>nth</i> error area in the selected cell or edit cell, and print out information about the error just as if <code>drc why</code> had been typed. If <i>nth</i> isn&#8217;t given (or is less than 1), the command moves to the next error area. Successive invocations of <code>drc find</code> cycle through all the error tiles in the cell. If multiple cells are selected, this command uses the upper-leftmost one. If no cells are selected, this command uses the edit cell.</p>
<dt><code>drc help</code></p>
<dd> Print a short synopsis of all the drc command options.</p>
<dt><code>drc off</code></p>
<dd> Turn off the background checker. From now on, Magic will not recheck design rules immediately after each command (but it will record the areas that need to be rechecked; the command <code>drc on</code> can be used to restart the checker).</p>
<dt><code>drc on</code></p>
<dd> Turn on the background checker. The checker will check whatever modifications have not already been checked. From now on, the checker will reverify modified areas as they result from commands. The checker is run in the background, not synchronously with commands, so it may get temporarily behind if massive changes are made.</p>
<dt><code>drc printrules </code>[<i>file</i>]</p>
<dd> Print out the compiled rule set in <i>file</i>, or on the text terminal if <i>file</i> isn&#8217;t given. For system maintenance only.</p>
<dt><code>drc rulestats</code></p>
<dd> Print out summary statistics about the compiled rule set. This is primarily for use in writing technology files.</p>
<dt><code>drc statistics</code></p>
<dd> Print out statistics kept by the design-rule checker. For each statistic, two values are printed: the count since the last time <code>drc statistics</code> was invoked, and the total count in this editing session. This command is intended primarily for system maintenance purposes.</p>
<dt><code>drc why</code></p>
<dd> Recheck the area underneath the box and print out the reason for each violation found. Since this command causes a recheck, the box should normally be placed around a small area (such as an error area).</dl>
</dl>
<dt><code>dump </code><i>cellName </i>[<code>child</code><i> refPointC</i>] [<code>parent</code><i> refPointP</i>]</p>
<dd> Copy the contents of cell <i>cellName</i> into the edit cell so that <i>refPointC</i> in the child is positioned at point <i>refPointP</i> in the edit cell. The reference points can either be the name of a label, in which case the lower-left corner of the label&#8217;s box is used as the reference point, or as a pair of numbers giving the (<i>x</i>,&nbsp;<wbr><i>y</i>) coordinates of a point explicitly. If <i>refPointC</i> is not specified, the lower-left corner of <i>cellName</i> cell is used. If <i>refPointP</i> is not specified, the lower-left corner of the box tool is used (the box must be in a window on the edit cell). After this command completes, the new information is selected.</p>
<dt><code>edit</code></p>
<dd> Make the selected cell the edit cell, and edit it in context. The edit cell is normally displayed in brighter colors than other cells (see the <code>see</code> command to change this). If more than one cell is selected, or if the selected cell is an array, the cursor position is used to select one of those cells as the new edit cell. Generally, Magic commands modify only the current edit cell.</p>
<dt><code>erase </code>[<i>layers</i>]</p>
<dd> For the area enclosed by the box, erase all paint in <i>layers</i>. (See the &#8220;LAYERS&#8221; section for the syntax of layer lists). If <i>layers</i> is omitted it defaults to <code>*,labels</code>. See your technology manual, or use the <code>layers</code> command, to find out about the available layer names.</p>
<dt><code>expand </code>[<code>toggle</code>]</p>
<dd> If the keyword <code>toggle</code> is supplied, all of the selected cells that are unexpanded are expanded, and all of the selected cells that are expanded are unexpanded. If <code>toggle</code> isn&#8217;t specified, then all of the cells underneath the box are expanded recursively until there is nothing but paint under the box.</p>
<dt><code>extract </code><i>option</i> [<i>args</i>]</p>
<dd> Extract a layout, producing one or more hierarchical <code>.ext</code> files that describe the electrical circuit implemented by the layout. The current extraction style (see <code>extract style</code> below) determines the parameters for parasitic resistance, capacitance, etc. that will be used. The <code>extract</code> command with no parameters checks timestamps and re-extracts as needed to bring all <code>.ext</code> files up-to-date for the cell in the window beneath the crosshair, and all cells beneath it. Magic displays any errors encountered during circuit extraction using stippled feedback areas over the area of the error, along with a message describing the type of error. Option and <i>args</i> are used in the following ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>extract all</code></p>
<dd> All cells in the window beneath the cursor are re-extracted regardless of whether they have changed since last being extracted.</p>
<dt><code>extract cell </code><i>name</i></p>
<dd> Extract only the currently selected cell, placing the output in the file <i>name</i>. If more than one cell is selected, this command uses the upper-leftmost one.</p>
<dt><code>extract do </code>[ <i>option</i> ]</p>
<dd>
<dt><code>extract no </code><i>option</i></p>
<dd> Enable or disable various options governing how the extractor will work. Use <code>:extract do</code> with no arguments to print a list of available options and their current settings. When the <code>adjust</code> option is enabled, the extractor will compute compensating capacitance and resistance whenever cells overlap or abut; if disabled, the extractor will not compute these adjustments but will run faster. If <code>capacitance</code> is enabled, node capacitances to substrate (perimeter and area) are computed; otherwise, all node capacitances are set to zero. Similarly, <code>resistance</code> governs whether or not node resistances are computed. The <code>coupling</code> option controls whether coupling capacitances are computed or not; if disabled, flat extraction is significantly faster than if coupling capacitance computation is enabled. Finally, the <code>length</code> option determines whether or not pathlengths in the root cell are computed (see <code>extract length</code> below).</p>
<dt><code>extract help</code></p>
<dd> Prints a short synopsis of all the <code>extract</code> command options.</p>
<dt><code>extract length</code> [ <i>option args</i> ]</p>
<dd> Provides several options for controlling which point-to-point path lengths are extracted explicitly. The extractor maintains two internal tables, one of <i>drivers</i>, or places where a signal is generated, and one of <i>receivers</i>, or places where a signal is sent. The components of each table are hierarchical label names, defined by means of the two commands <code>extract length driver </code><i>name1 </i>[<i>name2 &#8230;</i>] and <code>extract length receiver </code><i>name1 </i>[<i>name2 &#8230;</i>]. If extraction of pathlengths is enabled (&#8220;<code>:extract do length</code>&#8221;), then when the root cell in an extract command is being extracted, the extractor will compute the shortest and longest path between each driver and each receiver on the same electrical net, and output it to the <code>.ext</code> file for the root cell. Normally, one should create a file of these Magic commands for the circuit drivers and receivers of interest, and use <code>source</code> to read it in prior to circuit extraction. <code>Extract length clear</code> removes all the entries from both the driver and receiver tables.</p>
<dt><code>extract parents</code></p>
<dd> Extract the currently selected cell and all of its parents. All of its parents must be loaded in order for this to work correctly. If more than one cell is selected, this command uses the upper-leftmost one.</p>
<dt><code>extract showparents</code></p>
<dd> Like <code>extract parents</code>, but only print the cells that would be extracted; don&#8217;t actually extract them.</p>
<dt><code>extract style </code>[<i>style</i>]</p>
<dd> Select the style to be used for extraction parameters. If no <i>style</i> argument is provided, then Magic prints the names of all extraction parameter styles defined in the technology file and identifies the current style. If <i>style</i> is provided, it is made the current style.</p>
<dt><code>extract unique </code>[<code>#</code>]</p>
<dd> For each cell in the window beneath the cursor, check to insure that no label is attached to more than one node. If the <code>#</code> keyword was not specified, whenever a label is attached to more than one node, the labels in all but one of the nodes are changed by appending a numeric suffix to make them unique. If the <code>#</code> keyword is specified, only names that end in a &#8220;<code>#</code>&#8221; are made unique; any other duplicate nodenames that don&#8217;t end in a &#8220;<code>!</code>&#8221; are reported by leaving a warning feedback area. This command is provided for converting old designs that were intended for extraction with Mextra, which would automatically append unique suffixes to node names when they appeared more than once.</p>
<dt><code>extract warn</code> [ [<code>no</code>] <i>option</i> | [<code>no</code>] <code>all</code> ]</p>
<dd> The extractor always reports fatal errors. This command controls the types of warnings that are reported. <i>Option</i> may be one of the following: <code>dup</code>, to warn about two or more unconnected nodes in the same cell that have the same name, <code>fets</code>, to warn about transistors with fewer than the minimum number of terminals, and <code>labels</code>, to warn when nodes are not labeled in the area of cell overlap. In addition, <code>all</code> may be used to refer to all warnings. If a warning is preceded by <code>no</code>, it is disabled. To disable all warnings, use &#8220;<code>extract warn no all</code>&#8221;. To see which warning options are in effect, use &#8220;<code>extract warn</code>&#8221;.</dl>
</dl>
<dt><code>extresist [</code><i>cell</i> [<i>threshold</i>] ]</p>
<dd> Postprocessor for improving on the resistance calculation performed by the circuit extractor. To use this command, you first have to extract the design rooted at <i>cell</i> with <code>:extract&nbsp;<wbr></code><i>cell</i>, and then flatten the design using <i><a href="/docs/linux/man/1-ext2sim/">ext2sim</a></i>(1), producing the files <i>cell</i><code>.sim</code> and <i>cell</i><code>.nodes</code>. Then run <code>:extresist</code><i>&nbsp;<wbr>cell</i> to produce a file, <i>cell</i><code>.res.ext</code>, containing differences between the network described by the <code>.ext</code> files produced the first time around, and a new network that incorporates explicit two-point resistors where appropriate (see below). This file may be appended to <i>cell</i><code>.ext</code>, and then <i>ext2sim</i>run for a second time, to produce a new network with explicit resistors. The <i>threshold</i> parameter is used to control which nodes are turned into resistor networks: any node whose total resistance exceeds <i>threshold</i> times the smallest on-resistance of any transistor connected to that node will be approximated as a resistor network.</p>
<dt><code>feedback </code><i>option</i> [<i>args</i>]</p>
<dd> Examine feedback information that is created by several of the Magic commands to report problems or highlight certain things for users. <i>Option</i> and <i>args</i> are used in the following ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>feedback add </code><i>text</i> [<i>style</i>]</p>
<dd> Used to create a feedback area manually at the location of the box. This is intended as a way for other programs like Crystal to highlight things on a layout. They can generate a command file consisting of a <code>feedback clear</code> command, and a sequence of <code>box</code> and <code>feedback add</code> commands. <i>Text</i> is associated with the feedback (it will be printed by <code>feedback why</code> and <code>feedback find</code>). <i>Style</i> tells how to display the feedback, and is one of <code>dotted</code>, <code>medium</code>, <code>outline</code>, <code>pale</code>, and <code>solid</code> (if unspecified, <i>style</i> defaults to <code>pale</code>).</p>
<dt><code>feedback clear</code></p>
<dd> Clears all existing feedback information from the screen.</p>
<dt><code>feedback count</code></p>
<dd> Prints out a count of the current number of feedback areas.</p>
<dt><code>feedback find </code>[<i>nth</i>]</p>
<dd> Used to locate a particular feedback area. If <i>nth</i> is specified, the box is moved to the location of the <i>nth</i> feedback area. If <i>nth</i> isn&#8217;t specified, then the box is moved to the next sequential feedback area after the last one located with <code>feedback find</code>. In either event, the explanation associated with the feedback area is printed.</p>
<dt><code>feedback help</code></p>
<dd> Prints a short synopsis of all the <code>feedback</code> command options.</p>
<dt><code>feedback save </code><i>file</i></p>
<dd> This option will save information about all existing feedback areas in <i>file</i>. The information is stored as a collection of Magic commands, so that it can be recovered with the command <code>source </code><i>file</i>.</p>
<dt><code>feedback why</code></p>
<dd> Prints out the explanations associated with all feedback areas underneath the box.</dl>
</dl>
<dt><code>fill </code><i>direction</i> [<i>layers</i>]</p>
<dd> <i>Direction</i> is a Manhattan direction (see the section DIRECTIONS below). The paint visible under one edge of the box is sampled. Everywhere that the edge touches paint, the paint is extended in the given direction to the opposite side of the box. For example, if <i>direction</i> is <code>north</code>, then paint is sampled under the bottom edge of the box and extended to the top edge. If <i>layers</i> is specified, then only the given layers are considered; if <i>layers</i> isn&#8217;t specified, then all layers are considered.</p>
<dt><code>findbox </code>[<code>zoom</code>]</p>
<dd> Center the view on the box. If the optional <code>zoom</code> argument is present, zoom into the area specified by the box. This command will complain if the box is not in the window you are pointing to.</p>
<dt><code>flush </code>[<i>cellname</i>]</p>
<dd> Cell <i>cellname</i> is reloaded from disk. All changes made to the cell since it was last saved are discarded. If <i>cellname</i> is not given, the edit cell is flushed.</p>
<dt><code>garoute </code><i>option</i> [<i>args</i>]</p>
<dd> This command, with no <i>option</i> or <i>arg</i>, is like the <code>route</code> command: it generates routing in the edit cell to make connections specified in the current netlist. (See the <code>route</code> command for further information). Unlike the <code>route</code> command, this command is intended to be used for routing types of circuits, such as gate-arrays, whose routing channels can be determined in advance, and which require the ability to river-route across the tops of cells. The channels must have been predefined using <code>garoute channel</code> commands prior to this command being invoked. Unlike the <code>route</code> command, where the box indicates the routing area, this command ignores the box entirely. The new wires are placed in the edit cell. The netlist used is that selected by the <code>route netlist</code> command, or the current netlist being edited in a <code>netlist</code> window if no <code>route netlist</code> command has been given. <i>Options</i> and <i>args</i> have the following effects:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>garoute channel </code>[<i>type</i>]</p>
<dd>
<dt><code>garoute channel </code><i>xlo ylo xhi yhi </i>[<i>type]</i></p>
<dd> Define a channel. If <i>xlo</i>, <i>ylo</i>, <i>xhi</i>, and <i>yhi</i> are provided, they are interpreted as the coordinates of the lower-left and upper-right of the bounding box for the channel respectively. Otherwise, the coordinates of the box are used. The boundary of each channel is adjusted inward to lie halfway between routing grid lines if it does not lie there already; if the channel is adjusted, a warning message is printed. The channel defined is an ordinary routing channel if <i>type</i> is not specified; such channels are identical to those used by the router of the <code>route</code> command. If <i>type</i> is given, it must be either <code>h</code> or <code>v</code>. The channel thereby created will be a <i>river-routing</i> channel inside which only left-to-right routes are possible (&#8220;<code>h</code>&#8221;) or top-to-bottom (&#8220;<code>v</code>&#8221;). Unlike a normal channel, a river-routing channel may contain terminals in its interior.</p>
<dt><code>garoute generate</code><i> type </i>[<i>file</i>]</p>
<dd> Provides a primitive form of channel decomposition for regular structures such as gate-array or standard-cell layouts. Generates a collection of <code>garoute channel</code> commands, either to the standard output, or to <i>file</i> if the latter is specified. The <i>type</i> parameter must be either <code>h</code> or <code>v</code>. The entire area contained within the box is turned into routing channels. Each cell inside this area has its bounding box computed for purposes of routing by looking only at those layers considered to be &#8220;obstacles&#8221; to routing (see &#8220;Tutorial #7: Netlists and Routing&#8221; for details). The bounding box just computed is then extended all the way to the sides of the area of the box tool, vertically if <i>type</i> is <code>h</code> or horizontally if <i>type</i> is <code>v</code>. This extended area is then marked as belonging to a river-routing channel of type <i>type</i>; adjacent channels of this type are merged into a single channel. After all cells are processed, the areas not marked as being river-routing channels are output as normal channels.</p>
<dt><code>garoute help</code></p>
<dd> Print a short synopsis of all the <code>garoute</code> command options.</p>
<dt><code>garoute nowarn</code></p>
<dd> If a given terminal appears in more than one place inside a cell, the router can leave feedback if it is not possible to route to all of the places where the terminal appears. The <code>garoute nowarn</code> command instructs the router to leave feedback only if it is not possible to route to <i>any</i> of the locations of a terminal. (This is the default behavior of <code>garoute</code> router).</p>
<dt><code>garoute route</code> [<i>netlist</i>]</p>
<dd> Route the edit cell. If <i>netlist</i> is not specified, the netlist used is the same as when <code>garoute</code> is given with no options. If <i>netlist</i> is given, then it is used instead.</p>
<dt><code>garoute reset</code></p>
<dd> Clear all channels defined by <code>garoute channel</code> in preparation for redefining a new set of channels.</p>
<dt><code>garoute warn</code></p>
<dd> The opposite of <code>garoute nowarn</code>, this command instructs the router to leave feedback if it is not possible to route to all of the places where a terminal appears when a terminal has more than one location, even if not all of those locations are actually selected for routing by the global router.</dl>
</dl>
<dt><code>getcell </code><i>cellName </i>[<code>child</code><i> refPointC</i>] [<code>parent</code><i> refPointP</i>]</p>
<dd> This command adds a child cell instance to the edit cell. The instance refers to the cell <i>cellName</i>; it is positioned so that <i>refPointC</i> in the child is at point <i>refPointP</i> in the edit cell. The reference points can either be the name of a label, in which case the lower-left corner of the label&#8217;s box is used as the reference point, or as a pair of numbers giving the (<i>x</i>,&nbsp;<wbr><i>y</i>) coordinates of a point explicitly. If <i>refPointC</i> is not specified, the lower-left corner of <i>cellName</i> cell is used. If <i>refPointP</i> is not specified, the lower-left corner of the box tool is used (the box must be in a window on the edit cell). The new subcell is selected. The difference between this command and <code>dump</code> is that <code>dump</code> copies the contents of the cell, while <code>getcell</code> simply makes a reference to the original cell. <i>Cellname</i> must not be the edit cell or one of its ancestors.</p>
<dt><code>getnode </code>[<code>alias on</code> | <code>alias off</code>]</p>
<dd>
<dt><code>getnode </code>[<code>abort </code>[<i>str</i>]]</p>
<dd> Getnode prints out the node names (used by the extractor) for all selected paint. If aliasing turned on, getnode prints all the names it finds for a given node. It may not print every name that exists, however. When turned off, it just prints one name. The abort option allows the user to tell getnode that it is not important to completely search nodes that have certain names. For example, <code>getnode abort Vdd</code> will tell getnode not to continue searching the node if it determines that one of its names is Vdd. A <code>getnode abort</code>, without a string argument, will erase the list of names previously created by calling <code>getnode abort</code> with string arguments. Getnode can be safely aborted at any time by typing the interrupt character, usually ^C. See <i>Tutorial #11: Using IRSIM and RSIM with Magic</i> for more information on this command.</p>
<dt><code>grid </code>[<i>xSpacing</i> [<i>ySpacing </i>[<i>xOrigin yOrigin</i>]]]</p>
<dd>
<dt><code>grid off</code></p>
<dd> If no arguments are given, a one-unit grid is toggled on or off in the window underneath the cursor. <code>Grid off</code> always turns the grid off, regardless of whether it was on or off previously. If numerical arguments are given, the arguments determine the grid spacing and origin for the window under the cursor. In its most general form, <code>grid</code> takes four integer arguments. <code>XOrigin</code> and <code>yOrigin</code> specify an origin for the grid: horizontal and vertical grid lines will pass through this point. <code>XSpacing</code> and <code>ySpacing</code> determine the number of units between adjacent grid lines. If <code>xOrigin</code> and <code>yOrigin</code> are omitted, they default to 0. If <code>ySpacing</code> is also omitted, the xSpacing value is used for both spacings. Grid parameters will be retained for a window until explicitly changed by another <i>grid</i> command. When the grid is displayed, a solid box is drawn to show the origin of the edit cell.</p>
<dt><code>identify </code><i>instance_id</i></p>
<dd> Set the instance identifier of the selected cell use to <i>instance_id</i>. <i>Instance_id</i> must be unique among all instance identifiers in the parent of the selected cell. Initially, Magic guarantees uniqueness of identifiers by giving each cell an initial identifier consisting of the cell definition name followed by an underscore and a small integer.</p>
<dt><code>iroute </code><i>subcommand</i> [<i>args</i>]</p>
<dd> This command provides an interactive interface to the Magic maze-router. Routing is done one connection at a time. Three internal <i>hint</i> layers, <code>magnet</code>, <code>fence</code>, and <code>rotate</code>, allow the user to guide routing graphically. Routes are chosen close to magnets (if possible), routing does not cross fence boundaries, and rotate areas reverse the preferred routing directions for each layer. The maze-router seeks to find a lowest-cost path. Parameters specifying costs for horizontal and vertical routing on each layer, cost for jogs and contacts, and cost (per unit area) for distance between a path and magnets, help determine the nature of the routes. Several <i>search</i> parameters permit tuning to achieve acceptable routes in as short a time as possible. Routing can always be interrupted with <code>^C</code>. The iroute subcommands are as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>iroute</code></p>
<dd> Routes from cursor to inside box.</p>
<dt><code>iroute contact </code>[<i>type</i>] [<i>parameter</i>] [<i>value1</i>] &#8230; [<i>valuen</i>]</p>
<dd> An asterisk, <code>*</code>, can be used for <i>type</i> and <i>parameter</i>. This command is for setting and examining parameters related to contacts.</p>
<dt><code>iroute help </code>[<i>subcommand</i>]</p>
<dd> Summarizes irouter commands. If a <i>subcommand</i> is given, usage information for that subcommand is printed.</p>
<dt><code>iroute layers </code>[<i>type</i>] [<i>parameter</i>] [<i>value1</i>] &#8230; [<i>valuen</i>]</p>
<dd> An asterisk, <code>*</code>, can be used for <i>type</i> and <i>parameter</i>. This command is for setting and examining parameters related to route layers.</p>
<dt><code>iroute route </code>[<i>options</i>]</p>
<dd> Invokes the router. Options are as follows: </p>
<pre>
<code>-sLayers</code><i> layers</i> = layers route may start on
<code>-sCursor</code> = start route at cursor (DEFAULT)
<code>-sLabel </code><i>name</i> = start route at label of given name
<code>-sPoint </code><i>x y</i> = start route at given coordinates
<code>-dLayers</code><i> layers</i> = layers route may end on
<code>-dBox</code> = route to box (DEFAULT)
<code>-dLabel</code><i> name</i> = route to label of given name
<code>-dRect</code><i> xbot ybot xtop ytop</i> = route to rectangle of given coordinates
<code>-dSelection</code><i> = route to selection
</i></pre>
<dt><code>iroute saveParameters </code>&lt;<i>filename</i>&gt;</p>
<dd> Saves all current irouter parameter settings. The parameters can be restored to these values with the command &#8220;<code>source </code><i>filename</i>&#8221;.</p>
<dt><code>iroute search </code>[<i>searchParameter</i>] [<i>value</i>]</p>
<dd> Allows parameters controlling the search to be modified. If routing is too slow try increasing <code>rate</code>. If the router is producing bad results, try reducing <code>rate</code>. Its a good idea to make <code>width</code> at least twice as big as <code>rate</code>.</p>
<dt><code>iroute spacings </code>[<i>route-type</i>] [<i>type</i>] [<i>spacing</i>] &#8230; [<i>typen spacingn</i>]</p>
<dd> Default minimum spacings between a route-type placed by the router and other types are derived from the <code>drc</code> section of the technology file. The defaults can be overridden by this command. The special type <code>SUBCELL</code> is used to specify minimum spacing to unexpanded subcells.</p>
<dt><code>iroute verbosity </code>[<i>level</i>]</p>
<dd> Controls the number of messages printed during routing: </p>
<pre>
<code>0</code> = errors and warnings only,
<code>1</code> = brief,
<code>2</code> = lots of statistics.
</pre>
<dt><code>iroute version</code></p>
<dd> Prints irouter version information.</p>
<dt><code>iroute wizard </code>[<i>wizardparameter</i>] [<i>value</i>]</p>
<dd> Used to examine and set miscellaneous parameters. Most of these are best left alone by the unadventurous user.</dl>
</dl>
<dt><code>label </code><i>string </i>[<i>pos </i>[<i>layer</i>]]</p>
<dd> A label with text <i>string</i> is positioned at the box location. Labels may cover points, lines, or areas, and are associated with specific layers. Normally the box is collapsed to either a point or to a line (when labeling terminals on the edges of cells). Normally also, the area under the box is occupied by a single layer. If no <i>layer</i> argument is specified, then the label is attached to the layer under the box, or space if no layer covers the entire area of the box. If <i>layer</i> is specified but <i>layer</i> doesn&#8217;t cover the entire area of the box, the label will be moved to another layer or space. Labels attached to space will be considered by CIF processing programs to be attached to all layers overlapping the area of the label. <i>Pos</i> is optional, and specifies where the label text is to be displayed relative to the box (e.g. &#8220;north&#8221;). If <i>pos</i> isn&#8217;t given, Magic will pick a position to ensure that the label text doesn&#8217;t stick out past the edge of the cell.</p>
<dt><code>layers</code></p>
<dd> Prints out the names of all the layers defined for the current technology.</p>
<dt><code>load </code>[<i>file</i>]</p>
<dd> Load the cell hierarchy rooted at <i>file</i><code>.mag</code> into the window underneath the cursor. If no <i>file</i> is supplied, a new unnamed cell is created. The root cell of the hierarchy is made the edit cell unless there is already an edit cell in a different window.</p>
<dt><code>move </code>[<i>direction </i>[<i>amount</i>]]</p>
<dd>
<dt><code>move to </code><i>x y</i></p>
<dd> If no arguments are given, the selection is picked up by the point underneath the lower-left corner of the box and moved so that this point lies at the cursor location. If <i>direction</i> is given, it must be a Manhattan direction (e.g. <code>north</code>). The selection is moved in that direction by <i>amount</i>. If the box is in the same window as the selection, it is moved too. <i>Amount</i> defaults to 1. Selected material that is not in the edit cell, is not affected. The second form of the command is as though the cursor were pointing to (<i>x, y</i>) in the edit cell; the selection is picked up by the point beneath the lower-left corner of the box and moved so that this point lies at (<i>x</i>,<i>&nbsp;<wbr>y</i>).</p>
<dt><code>paint </code><i>layers</i></p>
<dd> The area underneath the box is painted in <i>layers</i>.</p>
<dt><code>path </code>[<i>searchpath</i>]</p>
<dd> This command tells Magic where to look for cells. <i>Searchpath</i> contains a list of directories separated by colons or spaces (if spaces are used, then <i>searchpath</i> must be surrounded by quotes). When looking for a cell, Magic will check each directory in the path in order, until the cell is found. If the cell is not found anywhere in the path, Magic will look in the system library for it. If the <i>path</i> command is invoked with no arguments, the current search path is printed.</p>
<dt><code>plot </code><i>option</i> [<i>args</i>]</p>
<dd> Used to generate hardcopy plots direct from Magic. <i>Options</i> and <i>args</i> are used in the following ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>plot gremlin </code><i>file</i> [<i>layers</i>]</p>
<dd> Generate a Gremlin-format description of everything under the box, and write the description in <i>file</i>. If <i>layers</i> isn&#8217;t specified, paint, labels, and unexpanded subcells are all included in the Gremlin file just as they appear on the screen. If <i>layers</i> is specified, then just the indicated layers are output in the Gremlin file. <i>Layers</i> may include the special layers <code>labels</code> and <code>subcell</code>. The Gremlin file is scaled to have a total size between 256 and 512 units; you should use the <code>width</code> and/or <code>height</code> Grn commands to ensure that the printed version is the size you want. Use the <code>mg</code> stipples in Grn. No plot parameters are used in Gremlin plotting.</p>
<dt><code>plot help</code></p>
<dd> Print a short synopsis of all the <code>plot</code> command options.</p>
<dt><code>plot parameters [</code><i>name value</i>]</p>
<dd> If <code>plot parameters</code> is invoked with no additional arguments, the values for all of the plot parameters are printed. If <i>name</i> and <i>value</i> are provided, then <i>name</i> is the name of a plot parameter and <i>value</i> is a new value for it. Plot parameters are used to control various aspects of plotting; all of them have &#8220;reasonable&#8221; initial values. Most of the parameters available now are used to control Versatec-style plotting. They are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cellIdFont</code></p>
<dd> The name of the font to use for cell instance ids in Versatec plots. This must be a file in Vfont format.</p>
<dt><code>cellNameFont</code></p>
<dd> The name of the font to use for cell names in Versatec plots. This must be a file in Vfont format.</p>
<dt><code>color</code></p>
<dd> If this is set to <code>true</code>, the <code>:plot versatec</code> command will generate output suitable for a four-color Versatec plotter, using the styles defined in the <code>colorversatec</code> style of the <code>plot</code> section of the technology file. If <code>color</code> is <code>false</code> (the default), then <code>:plot versatec</code> generates normal black-and-white plots.</p>
<dt><code>directory</code></p>
<dd> The name of the directory in which to create raster files for the Versatec. The raster files have names of the form <code>magicPlotXXXXXX</code>, where <code>XXXXXX</code> is a process-specific identifier.</p>
<dt><code>dotsPerInch</code></p>
<dd> Indicates how many dots per inch there are on the Versatec printer. This parameter is used only for computing the scale factor for plotting. Must be an integer greater than zero.</p>
<dt><code>labelFont</code></p>
<dd> The name of the font to use for labels in Versatec plots. This must be a file in Vfont format.</p>
<dt><code>printer</code></p>
<dd> The name of the printer to which to spool Versatec raster files.</p>
<dt><code>showcellnames</code></p>
<dd> If &#8220;true&#8221; (the default) then the name and instance-identifier of each unexpanded subcell is displayed inside its bounding box. If this parameter is &#8220;false&#8221; then only the bounding box of the cell is displayed.</p>
<dt><code>spoolCommand</code></p>
<dd> The command used to spool Versatec raster files. This must be a text string containing two &#8220;%s&#8221; formatting fields. The first &#8220;%s&#8221; will be replaced with the printer name, and the second one will be replaced with the name of the raster file.</p>
<dt><code>swathHeight</code></p>
<dd> How many raster lines of Versatec output to generate in memory at one time. The raster file is generated in swaths in order to keep the memory requirements reasonable. This parameter determines the size of the swaths. It must be an integer greater than zero, and should be a multiple of 16 in order to avoid misalignment of stipple patterns.</p>
<dt><code>width</code></p>
<dd> The number of pixels across the Versatec printer. Must be an integer greater than 0, and must be an even multiple of 32.</dl>
</dl>
<dt><code>plot versatec </code>[<i>size</i> [<i>layers</i>]]</p>
<dd> Generate a raster file describing all the the information underneath the box in a format suitable for printing on Versatec black-and-white or color printers, and spool the file for printing. See the plot parameters above for information about the parameters that are used to control Versatec plotting. <i>Size</i> is used to scale the plot: a scalefactor is chosen so that the area of the box is <i>size</i> inches across on the printed page. <i>Size</i> defaults to the width of the printer. <i>Layers</i> selects which layers (including labels and subcells) to plot; it defaults to everything visible on the screen.</dl>
</dl>
<dt><code>plow </code><i>direction</i> [<i>layers</i>]</p>
<dd>
<dt><code>plow </code><i>option</i> [<i>args</i>]</p>
<dd> The first form of this command invokes the plowing operation to stretch and/or compact a cell. <i>Direction</i> is a Manhattan direction. <i>Layers</i> is an optional collection of mask layers, which defaults to <code>*</code>. One of the edges of the box is treated as a plow and dragged to the opposite edge of the box (e.g. the left edge is used as the plow when <code>plow right</code> is invoked). All edges on <i>layers</i> that lie in the plow&#8217;s path are pushed ahead of it, and they push other edges ahead of them to maintain design rules, connectivity, and transistor and contact sizes. Subcells are moved in their entirety without being modified internally. Any mask information overlapping a subcell moved by plowing is also moved by the same amount. <i>Option</i> and <i>args</i> are used in the following ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>plow boundary</code></p>
<dd> The box specifies the area that may be modified by plowing. This area is highlighted with a pale stipple outline. Subsequent plows are not allowed to modify any area outside that specified by the box; if they do, the distance the plow moves is reduced by an amount sufficient to insure that no geometry outside the boundary gets affected.</p>
<dt><code>plow help</code></p>
<dd> Prints a short synopsis of all the <code>plow</code> command options.</p>
<dt><code>plow horizon</code><i>&nbsp;<wbr>n</i></p>
<dd>
<dt><code>plow horizon</code></p>
<dd> The first form sets the plowing jog horizon to <i>n</i> units. The second form simply prints the value of the jog horizon. Every time plowing considers introducing a jog in a piece of material, it looks up and down that piece of material for a distance equal to the jog horizon. If it finds an existing jog within this distance, it uses it. Only if no jog is found within the jog horizon does plowing introduce one of its own. A jog horizon of zero means that plowing will always introduce new jogs where needed. A jog horizon of infinity (<code>plow nojogs</code>) means that plowing will not introduce any new jogs of its own.</p>
<dt><code>plow jogs</code></p>
<dd> Re-enable jog insertion with a horizon of 0. This command is equivalent to <code>plow horizon 0</code>.</p>
<dt><code>plow noboundary</code></p>
<dd> Remove any boundary specified with a previous <code>plow boundary</code> command.</p>
<dt><code>plow nojogs</code></p>
<dd> Sets the jog horizon to infinity. This means that plowing will not introduce any jogs of its own; it will only use existing ones.</p>
<dt><code>plow nostraighten</code></p>
<dd> Don&#8217;t straighten jogs automatically after each plow operation.</p>
<dt><code>plow selection </code>[<i>direction </i>[<i>distance</i>]]</p>
<dd> Like the <code>move</code> or <code>stretch</code> commands, this moves all the material in the selection that belongs to the edit cell. However, any material not in the selection is pushed out of its way, just as though each piece of the selection were plowed individually. If no arguments are given, the selection is picked up by the point underneath the lower-left corner of the box and plowed so that this point lies at the cursor location. The box is moved along with the selection. If <i>direction</i> is given, it must be a Manhattan direction (e.g. <code>north</code>). The selection is moved in that direction by <i>amount</i>. If the box is in the same window as the selection, it is moved too. <i>Amount</i> defaults to 1. If there is selected material that isn&#8217;t in the edit cell, it is ignored (note that this is different from <code>select</code> and <code>move</code>). If <i>direction</i> isn&#8217;t given and the cursor isn&#8217;t exactly left, right, up, or down from the box corner, then Magic first rounds the cursor position off to a position that is one of those (whichever is closest).</p>
<dt><code>plow straighten</code></p>
<dd> Straighten jogs automatically after each plow operation. The effect will be as though the <code>straighten</code> command were invoked after each plow operation, with the same direction, and over the area changed by plowing.</dl>
</dl>
<dt><code>resist </code><i>cell</i> [<i>tolerance</i>]</p>
<dd> This command is similar to <code>extresist</code> above, but used for extracting resistance networks for individual nodes. Only the node underneath the box is processed. The network for this node is output to the file <i>cell</i><code>.res.ext</code>. See the description for <code>extresist</code> for an explanation of <i>tolerance</i>.</p>
<dt><code>route </code><i>option</i> [<i>args</i>]</p>
<dd> This command, with no <i>option</i> or <i>arg</i>, is used to generate routing using the Magic router in the edit cell to make connections specified in the current netlist. The box is used to indicate the routing area: no routing will be placed outside the area of the box. The new wires are placed in the edit cell. <i>Options</i> and <i>args</i> have the following effects:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>route end </code>[<i>real</i>]</p>
<dd> Print the value of the channel end constant used by the channel router. If a value is supplied, the channel end constant is set to that value. The channel end constant is a dimensionless multiplier used to compute how far from the end of a channel to begin preparations to make end connections.</p>
<dt><code>route help</code></p>
<dd> Print a short synopsis of all the <code>route</code> command options.</p>
<dt><code>route jog </code>[<i>int</i>]</p>
<dd> Print the value of the minimum jog length used by the channel router. If a value is supplied, the minimum jog length is set to that value. The channel router makes no vertical jogs shorter than the minimum jog length, measured in router grid units. Higher values for this constant may improve the quality of the routing by removing unnecessary jogs; however, prohibiting short jogs may make some channels unroutable.</p>
<dt><code>route metal</code></p>
<dd> Toggle metal maximization on or off. The route command routes the preferred routing layer (termed &#8220;metal&#8221;) horizontally and the alternate routing layer vertically. By default wires on the alternate routing layer are then converted, as much as possible, to the preferred layer before being painted into the layout. Enabling metal maximization improves the quality of the resulting routing, since the preferred routing layer generally has better electrical characteristics; however, designers wishing to do hand routing after automatic routing may find it easier to disable metal maximization and deal with a layer-per-direction layout.</p>
<dt><code>route netlist </code>[<i>file</i>]</p>
<dd> Print the name of the current netlist. If a file name is specified, it is opened if possible, and the new netlist is loaded. This option is provided primarily as a convenience so you need not open the netlist menu before routing.</p>
<dt><code>route obstacle </code>[<i>real</i>]</p>
<dd> Print the obstacle constant used by the channel router. If a value is supplied, set the channel router obstacle constant to that value. The obstacle constant is a dimensionless multiplier used in deciding how far in front of an obstacle the channel router should begin jogging nets out of the way. Larger values mean that nets will jog out of the way earlier; however, if nets jog out of the way too early routing area is wasted.</p>
<dt><code>route origin </code>[<i>x y</i>]</p>
<dd> Print the x- and y-coordinates of the origin of the routing grid. By default, the routing grid starts from (0,0). However, by supplying an <i>x</i> and <i>y</i> coordinate to the <code>route origin</code> command, the origin can be set to any other value. This command is primarily useful when routing a chip that has been designed with routing on the same pitch as the router will use, but where the left and bottom edges of the pre-existing routing don&#8217;t line up with the routing grid lines (for example, the pre-existing routing might have been centered on routing grid lines). The alternative to specifying a different origin for the routing grid would be to translate all the material in the cell to be routed so that the prewiring lined up properly with routing grid lines.</p>
<dt><code>route settings</code></p>
<dd> Print the values of all router parameters.</p>
<dt><code>route steady </code>[<i>int</i>]</p>
<dd> Print the value of the channel router&#8217;s steady net constant. If a value is supplied, set the steady net constant to the value. The steady net constant, measured in router grid units, specifies how far beyond the next terminal the channel router should look for a conflicting terminal before deciding that a net is rising or falling. Larger values mean that the net rises and falls less often.</p>
<dt><code>route tech</code></p>
<dd> Print the router technology information. This includes information such as the names of the preferred and alternate routing layers, their wire widths, the router grid spacing, and the contact size.</p>
<dt><code>route viamin</code></p>
<dd> Minimize vias in (previously) routed netlist. This subcommand removes unnecessary layer changes in all nets in the current netlist to minimize via count. The preferred routing layer, <code>layer1</code> in the <code>router</code> section of the technology file, is favored by the algorithm. Note that &#8220;<code>route viamin</code>&#8221; is an independent routing postpass that can be applied even if the routing was not generated by the <code>route</code> command, provided the layers and widths agree with the <code>router</code> section of the technology file.</p>
<dt><code>route vias </code>[<i>int</i>]</p>
<dd> Print the value of the metal maximization via constant. If a value is supplied, set the via constant to the value. The via constant, measured in router grid units, represents the tradeoff between metal maximization and the via count. In many cases it is possible to convert wiring on the alternate routing layer into routing on the preferred routing layer (&#8220;metal&#8221;) at the expense of introducing one or two vias. The via constant specifies the amount of converted wiring that makes it worthwhile to add vias to the routing.</dl>
</dl>
<dt><code>rsim </code>[<i>options</i>] [<i>filename</i>]</p>
<dd> Runs rsim under Magic. See <i>Tutorial #11: Using IRSIM and RSIM with Magic</i> for more information on what options and files are required by rsim. Normally, IRSIM requires a parameter file for the technology and a <code>.sim</code> file describing the circuit.</p>
<dt>
<dd> The <code>rsim</code> command without any options can be used to interact with a previously-started rsim. Type <code>rsim</code> and you will see the rsim prompt. To get back to magic, type <code>q</code>.</p>
<dt><code>save </code>[<i>name</i>]</p>
<dd> Save the edit cell on disk. If the edit cell is currently the &#8220;(UNNAMED)&#8221; cell, <i>name</i> must be specified; in this case the edit cell is renamed to <i>name</i> as well as being saved in the file <i>name</i>.<code>mag</code>. Otherwise, <i>name</i> is optional. If specified, the edit cell is saved in the file <i>name</i>.<code>mag</code>; otherwise, it is saved in the file from which it was originally read.</p>
<dt><code>see </code><i>option</i></p>
<dd> This command is used to control which layers are to be displayed in the window under the cursor. It has several forms:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>see no </code><i>layers</i></p>
<dd> Do not display the given layers in the window under the cursor. If <code>labels</code> is given as a layer name, don&#8217;t display labels in that window either. If <code>errors</code> is given as a layer, no design-rule violations will be displayed (the checker will continue to run, though). If <i>layers</i> is given as &quot;*&quot;, all mask layers will be disabled, but errors and labels will still be shown. See the &quot;LAYERS&quot; section at the end of this manual page for an explanation of layer naming in Magic.</p>
<dt><code>see </code><i>layers</i></p>
<dd> Reenable display of the given <i>layers</i>. Note that &quot;*&quot; expands to all mask layers, but does not include the label or error layers. See the &quot;LAYERS&quot; section at the end of this manual page for details.</p>
<dt><code>see no</code></p>
<dd> Don&#8217;t display any mask layers or labels. Only subcell bounding boxes will be displayed.</p>
<dt><code>see</code></p>
<dd> Reenable display of all mask layers, labels, and errors.</p>
<dt><code>see allSame</code></p>
<dd> Display all cells the same way. This disables the facility where the edit cell is displayed in bright colors and non-edit cells are in paler colors. After <code>see allSame</code>, all mask information will be displayed in bright colors.</p>
<dt><code>see no allSame</code></p>
<dd> Reenable the facility where non-edit cells are drawn in paler colors.</dl>
</dl>
<dt><code>select </code><i>option</i></p>
<dd> This command is used to select paint, labels, and subcells before operating on them with commands like <code>move</code> and <code>copy</code> and <code>delete</code>. It has several forms:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>select</code></p>
<dd> If the cursor is over empty space, then this command is identical to <code>select cell</code>. Otherwise, paint is selected. The first time the command is invoked, a chunk of paint is selected: the largest rectangular area of material of the same type visible underneath the cursor. If the command is invoked again without moving the cursor, the selection is extended to include all material of the same type, regardless of shape. If the command is invoked a third time, the selection is extended again to include all material that is visible and electrically connected to the point underneath the cursor.</p>
<dt><code>select more</code></p>
<dd> This command is identical to <code>select</code> except that the selection is not first cleared. The result is to add the newly-selected material to what is already in the selection.</p>
<dt><code>select less</code></p>
<dd> This chooses material just as <code>select</code> does, but the material is removed from the selection, rather than added to it. The result is to deselect the chosen material.</p>
<dt><code>select </code>[<code>more</code> | <code>less</code>] <code>area</code><i> layers</i></p>
<dd> Select material by area. If <i>layers</i> are not specified, then all paint, labels, and unexpanded subcells visible underneath the box are selected. If <i>layers</i> is specified, then only those layers are selected. If <code>more</code> is specified, the new material is added to the current selection rather than replacing it. If <code>less</code> is specified, the new material is removed from the selection (deselected).</p>
<dt><code>select </code>[<code>more</code> | <code>less</code>] <code>cell</code><i> name</i></p>
<dd> Select a subcell. If <i>name</i> isn&#8217;t given, this command finds a subcell that is visible underneath the cursor and selects it. If the command is repeated without moving the cursor then it will step through all the subcells under the cursor. If <i>name</i> is given, it is treated as a hierarchical instance identifier starting from the root of the window underneath the cursor. The named cell is selected. If <code>more</code> is specified, the new subcell is added to the current selection instead of replacing it. If <code>less</code> is specified, the new subcell is removed from the selection (deselected).</p>
<dt><code>select clear</code></p>
<dd> Clear out the selection. This does not affect the layout; it merely deselects everything.</p>
<dt><code>select help</code></p>
<dd> Print a short synopsis of the selection commands.</p>
<dt><code>select save </code><i>cell</i></p>
<dd> Save all the information in the selection as a Magic cell on disk. The selection will be saved in file <i>cell</i><code>.mag</code>.</p>
<dt><i>select and the see command</i></p>
<dd> Select interacts with the <code>see</code> command. When selecting individual pieces of material, only visible layers are candidates for selection. When selecting an entire area, however, both visible and non-visible material is selected. This behavior allows entire regions of material to be moved, even if <code>see</code> has been used to turn off the display of some of the layers.</dl>
</dl>
<dt><code>sideways</code></p>
<dd> Flip the selection left-to-right about a vertical axis running through the center of the selection&#8217;s area. If the box is in the same window as the selection, it is flipped too. Selected material not in the edit cell is not affected.</p>
<dt><code>simcmd </code><i>cmd</i></p>
<dd> Sends the command <i>cmd</i> to rsim for execution. See <i>Tutorial #11: Using IRSIM and RSIM with Magic</i> for more information.</p>
<dt><code>snap </code>[<code>on</code>]</p>
<dd>
<dt><code>snap </code>[<code>off</code>]</p>
<dd> Control whether the box and point are snapped to the grid selected for the windows in which they appear (the grid was set by the <code>grid</code> command), or to the standard 1&#215;1 grid. The default is for snapping to be <code>off</code>, i.e., snapping to a 1&#215;1 grid. With no arguments, <code>snap</code> prints whether snapping is enabled or not.</p>
<dt><code>startrsim </code>[<i>options</i>] [<i>filename</i>]</p>
<dd> Similar to the <code>rsim</code> command, except it returns to Magic as soon as rsim is started. See <i>Tutorial #11: Using IRSIM and RSIM with Magic</i> for more information.</p>
<dt><code>straighten </code><i>direction</i></p>
<dd> Straighten jogs in wires underneath the box by pulling them in <i>direction</i>. Jogs are only straightened if doing so will cause no additional geometry to move.</p>
<dt><code>stretch </code>[<i>direction </i>[<i>amount</i>]]</p>
<dd> This command is identical to <code>move</code> except that simple stretching occurs as the selection is moved. Each piece of paint in the selection causes the area through which it&#8217;s moved to be erased in that layer. Also, each piece of paint in the selection that touches unselected material along its back side causes extra material to be painted to fill in the gap left by the move. If <i>direction</i> isn&#8217;t given and the cursor isn&#8217;t exactly left, right, up, or down from the box corner, then Magic first rounds the cursor position off to a position that is one of those (whichever is closest).</p>
<dt><code>tool </code>[<i>name</i> | <code>info</code>]</p>
<dd> Change the current tool. The result is that the cursor shape is different and the mouse buttons mean different things. The command <code>tool info</code> prints out the meanings of the buttons for the current tool. <code>Tool </code><i>name</i> changes the current tool to <i>name</i>, where <i>name</i> is one of <code>box</code>, <code>wiring</code>, or <code>netlist</code>. If <code>tool</code> is invoked with no arguments, it picks a new tool in circular sequence: multiple invocations will cycle through all of the available tools.</p>
<dt><code>unexpand</code></p>
<dd> Unexpand all cells that touch the box but don&#8217;t completely contain it.</p>
<dt><code>upsidedown</code></p>
<dd> Flip the selection upside down about a horizontal axis running through the center of the selection&#8217;s area. If the box is in the same window as the selection then it is flipped too. Selected material that is not in the edit cell is not changed.</p>
<dt><code>what</code></p>
<dd> Print out information about all the things that are selected.</p>
<dt><code>wire </code><i>option </i>[<i>args</i>]</p>
<dd> This command provides a centerline-wiring style user interface. <i>Option</i> and <i>args</i> specify a particular wiring option, as described below. Some of the options can be invoked via mouse buttons when the <code>wiring</code> tool is active.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>wire help</code></p>
<dd> Print out a synopsis of the various wiring commands.</p>
<dt><code>wire horizontal</code></p>
<dd> Just like <code>wire leg</code> except that the new segment is forced to be horizontal.</p>
<dt><code>wire leg</code></p>
<dd> Paint a horizontal or vertical segment of wire from one side of the box over to the cursor&#8217;s x- or y-location (respectively). The direction (horizontal or vertical) is chosen so as to produce the longest possible segment. The segment is painted in the current wiring material and thickness. The new segment is selected, and the box is placed at its tip.</p>
<dt><code>wire switch [</code><i>layer width</i>]</p>
<dd> Switch routing layers and place a contact at the box location. The contact type is chosen to connect the old and new routing materials. The box is placed at the position of the contact, and the contact is selected. If <i>layer</i> and <i>width</i> are specified, they are used as the new routing material and width, respectively. If they are not specified, the new material and width are chosen to correspond to the material underneath the cursor.</p>
<dt><code>wire type [</code><i>layer width</i>]</p>
<dd> Pick a material and width for wiring. If <i>layer</i> and <i>width</i> are not given, then they are chosen from the material underneath the cursor, a square chunk of material is selected to indicate the layer and width that were chosen, and the box is placed over this chunk. If <i>layer</i> and <i>width</i> are given, then this command does not modify the box position.</p>
<dt><code>wire vertical</code></p>
<dd> Just like <code>wire leg</code> except that the new segment is forced to be vertical.</dl>
</dl>
<dt><code>writeall </code>[<code>force</code>]</p>
<dd> This command steps through all the cells that have been modified in this edit session and gives you a chance to write them out. If the <code>force</code> option is specified, then &#8220;autowrite&#8221; mode is used: all modified cells are automatically written without asking for permission. </p>
</dl>
<h2>COMMANDS FOR ALL WINDOWS</h2>
<p> These commands are not used for layout, but are instead used for overall, housekeeping functions. They are valid in all windows.</p>
<dl>
<dt><code>closewindow</code></p>
<dd> The window under the cursor is closed. That area of the screen will now show other windows or the background.</p>
<dt><code>echo </code>[<code>-n</code>] <i>str1 str2 &#8230; strN</i></p>
<dd> Prints <i>str1 str2 &#8230; strN</i> in the text window, separated by spaces and followed by a newline. If the <code>-n</code> switch is given, no newline is output after the command.</p>
<dt><code>help</code> [<i>pattern</i>]</p>
<dd> Displays a synopsis of commands that apply to the window you are pointing to. If <i>pattern</i> is given then only command descriptions containing the pattern are printed. <i>Pattern</i> may contain &#8216;*&#8217; and &#8216;?&#8217; characters, which match a string of non-blank characters or a single non-blank character (respectively).</p>
<dt><code>logcommands </code>[<i>file </i>[<code>update</code>]]]</p>
<dd> If <i>file</i> is given, all further commands are logged to that file. If no arguments are given, command logging is terminated. If the keyword <code>update</code> is present, commands are output to the file to cause the screen to be updated after each command when the command file is read back in.</p>
<dt><code>macro </code>[<i>char </i>[<i>command</i>]]</p>
<dd> <i>Command</i> is associated with <i>char</i> such that typing <i>char</i> on the keyboard is equivalent to typing &#8220;:&#8221; followed by <i>command</i>. If <i>command</i> is omitted, the current macro for <i>char</i> is printed. If <i>char</i> is also omitted, then all current macros are printed. If <i>command</i> contains spaces, tabs, or semicolons then it must be placed in quotes. The semicolon acts as a command separator allowing multiple commands to be combined in a single macro.</p>
<dt><code>openwindow </code>[<i>cell</i>]</p>
<dd> Open a new, empty window at the cursor position. Placement, sizing, and methods of manipulation are determined by the conventions of the window system in use. If <i>cell</i> is specified, then that cell is displayed in the new window. Otherwise the area of the box will be displayed in the new window.</p>
<dt><code>pushbutton </code><i>button action</i></p>
<dd> Simulates a button push. Button should be <code>left</code>, <code>middle</code>, or <code>right</code>. Action is one of <code>up</code>, or <code>down</code>. This command is normally invoked only from command scripts produced by the <code>logcommands</code> command.</p>
<dt><code>quit</code></p>
<dd> Exit Magic and return to the shell. If any cells, colormaps, or netlists have changed since they were last saved on disk, you are given a chance to abort the command and continue in Magic.</p>
<dt><code>redo </code>[<i>n</i>]</p>
<dd> Redo the last <i>n</i> commands that were undone using <code>undo</code> (see below). The number of commands to redo defaults to 1 if <i>n</i> is not specified.</p>
<dt><code>redraw</code></p>
<dd> Redraw the graphics screen.</p>
<dt><code>scroll </code><i>direction </i>[<i>amount</i>]</p>
<dd> The window under the cursor is moved by <i>amount</i> screenfulls in <i>direction</i> relative to the circuit. If <i>amount</i> is omitted, it defaults to 0.5.</p>
<dt><code>send </code><i>type command</i></p>
<dd> Send a <i>command</i> to the window client named by <i>type</i>. The result is just as if <i>command</i> had been typed in a window of type <i>type</i>. See <code>specialopen</code>, below, for the allowable types of windows.</p>
<dt><code>setpoint [</code><i>x y</i> [<i>windowID</i>]]</p>
<dd> Fakes the location of the cursor up until after the next interactive command. Without arguments, just prints out the current point location. This command is normally invoked only from command scripts.</p>
<dt>
<dd> If <i>windowID</i> is given, then the point is assumed to be in that window&#8217;s screen coordinate system rather than absolute screen coordinates.</p>
<dt><code>sleep </code><i>n</i></p>
<dd> Causes Magic to go to sleep for <i>n</i> seconds.</p>
<dt><code>source </code><i>filename</i></p>
<dd> Each line of <i>filename</i> is read and processed as one command. Any line whose last character is backslash is joined to the following line. The commands <code>setpoint</code>, <code>pushbutton</code>, <code>echo</code>, <code>sleep</code>, and <code>updatedisplay</code> are useful in command files, and seldom used elsewhere.</p>
<dt><code>specialopen </code>[<i>x1 y1 x2 y2</i>] <i>type</i> [<i>args</i>]</p>
<dd> Open a window of type <i>type</i>. If the optional <i>x1 y1 x2 y2</i> coordinates are given, then the new window will have its lower left corner at screen coordinates (<i>x1</i>, <i>y1</i>) and its upper right corner at screen coordinates (<i>x2</i>, <i>y2</i>). The <i>args</i> arguments are interpreted differently depending upon the type of the window. These types are known:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>layout</code></p>
<dd> This type of window is used to edit a VLSI cell. The command takes a single argument which is used as the name of a cell to be loaded. The command <center> <code>open </code><i>filename</i><br />
 </center> is a shorthand for the command <center> <code>specialopen layout </code><i>filename</i>.<br />
 </center></p>
<dt><code>color</code></p>
<dd> This type of window allows the color map to be edited. See the section COMMANDS FOR COLORMAP EDITING below.</p>
<dt><code>netlist</code></p>
<dd> This type of window presents a menu that can be used to place labels, and to generate and edit net-lists. See the section COMMANDS FOR NETLIST EDITING below.</dl>
</dl>
<dt><code>underneath</code></p>
<dd> Move the window pointed at so that it lies underneath the rest of the windows.</p>
<dt><code>undo </code>[<i>count</i>]</p>
<dd> Undoes the last <i>count</i> commands. Almost all commands in Magic are now undo-able. The only holdouts left are cell expansion/unexpansion, and window modifications (change of size, zooming, etc.). If <i>count</i> is unspecified, it defaults to 1.</p>
<dt><code>updatedisplay</code></p>
<dd> Update the display. This command is normally invoked only from command scripts. Scripts that do not contain this command update the screen only at the end of the script.</p>
<dt><code>view</code></p>
<dd> Choose a view for the window underneath the cursor so that everything in the window is visible.</p>
<dt><code>windscrollbars </code>[<i>on</i>|<i>off</i>]</p>
<dd> Set the flag that determines if new windows will have scroll bars.</p>
<dt><code>windowpositions </code>[<i>file</i>]</p>
<dd> Write out the positions of the windows in a format suitable for the <code>source</code> command. If <i>file</i> is specified, then write it out to that file instead of to the terminal.</p>
<dt><code>zoom </code>[<i>factor</i>]</p>
<dd> Zoom the view in the window underneath the cursor by <i>factor</i>. If <i>factor</i> is less than 1, we zoom in; if it is greater than one, we zoom out. </p>
</dl>
<h2>MOUSE BUTTONS FOR NETLIST WINDOWS</h2>
<p> When the netlist menu is opened using the command <code>special netlist</code>, a menu appears on the screen. The colored areas on the menu can be clicked with various mouse buttons to perform various actions, such as placing labels and editing netlists. For details on how to use the menu, see &#8220;Magic Tutorial #7: Netlists and Routing&#8221;. The menu buttons all correspond to commands that could be typed in netlist or layout windows. </p>
<h2>COMMANDS FOR NETLIST WINDOWS</h2>
<p> The commands described below work if you are pointing to the interior of the netlist menu. They may also be invoked when you are pointing at another window by using the <code>send netlist</code> command. Terminal names in all of the commands below are hierarchical names consisting of zero or more cell use ids separated by slashes, followed by the label name, e.g. <code>toplatch/shiftcell_1/in</code>. When processing the terminal paths, the search always starts in the edit cell.</p>
<dl>
<dt><code>add </code><i>term1 term2</i></p>
<dd> Add the terminal named <i>term1</i> to the net containing terminal <i>term2</i>. If <i>term2</i> isn&#8217;t in a net yet, make a new net containing just <i>term1</i> and <i>term2</i>.</p>
<dt><code>cleanup</code></p>
<dd> Check the netlist to make sure that for every terminal named in the list there is at least one label in the design. Also check to make sure that every net contains at least two distinct terminals, or one terminal with several labels by the same name. When errors are found, give the user an opportunity to delete offending terminals and nets. This command can also be invoked by clicking the &#8220;Cleanup&#8221; menu button.</p>
<dt><code>cull</code></p>
<dd> Examine the current netlist and the routing in the edit cell, and remove those nets from the netlist that are already routed. This command is often used after pre-routing nets by hand, so the router won&#8217;t try to implement them again.</p>
<dt><code>dnet </code><i>name name</i> &#8230;</p>
<dd> For each <i>name</i> given, delete the net containing that terminal. If no <i>name</i> is given, delete the currently-selected net, just as happens when the &#8220;No Net&#8221; menu button is clicked.</p>
<dt><code>dterm </code><i>name name</i> &#8230;</p>
<dd> For each <i>name</i> given, delete that terminal from its net.</p>
<dt><code>extract</code></p>
<dd> Pick a piece of paint in the edit cell that lies under the box. Starting from this, trace out all the electrically-connected material in the edit cell. Where this material touches subcells, find any terminals in the subcells and make a new net containing those terminals. Note: this is a different command from the <code>extract</code> command in layout windows.</p>
<dt><code>find </code><i>pattern </i>[<i>layers</i>]</p>
<dd> Search the area beneath the box for labels matching <i>pattern</i>, which may contain the regular-expression characters &#8220;<code>*</code>&#8221; &#8220;<code>?</code>&#8221;, &#8220;<code>[</code>&#8221;, &#8220;<code>]</code>&#8221;, and &#8220;<code>\</code>&#8221; (as matched by <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1); see the description of the <code>find</code> button in &#8220;Magic Tutorial #7: Netlists and Routing&#8221;). For each label found, leave feedback whose text is the layer on which the label appears, followed by a semicolon, followed by the full hierarchical pathname of the label. The feedback surrounds the area of the label by one unit on all sides. (The reason for the one-unit extension is that feedback rectangles must have positive area, while labels may have zero width or height). If <i>layers</i> are given, only labels attached to those layers are considered.</p>
<dt><code>flush </code>[<i>netlist</i>]</p>
<dd> The netlist named <i>netlist</i> is reloaded from the disk file <i>netlist</i><code>.net</code>. Any changes made to the netlist since the last time it was written are discarded. If <i>netlist</i> isn&#8217;t given, the current netlist is flushed.</p>
<dt><code>join </code><i>term1 term2</i></p>
<dd> Join together the nets containing terminals <i>term1</i> and <i>term2</i>. The result is a single net containing all the terminals from both the old nets.</p>
<dt><code>netlist </code>[<i>name</i>]</p>
<dd> Select a netlist to work on. If <i>name</i> is provided, read <i>name</i>.<code>net</code> (if it hasn&#8217;t already been read before) and make it the current netlist. If <i>name</i> isn&#8217;t provided, use the name of the edit cell instead.</p>
<dt><code>print </code>[<i>name</i>]</p>
<dd> Print the names of all the terminals in the net containing <i>name</i>. If <i>name</i> isn&#8217;t provided, print the terminals in the current net. This command has the same effect as clicking on the &#8220;Print&#8221; menu button.</p>
<dt><code>ripup </code>[<code>netlist</code>]</p>
<dd> This command has two forms. If <code>netlist</code> isn&#8217;t typed as an argument, then find a piece of paint in the edit cell under the box. Trace out all paint in the edit cell that is electrically connected to the starting piece, and delete all of this paint. If <code>netlist</code> is typed, find all paint in the edit cell that is electrically connected to any of the terminals in the current netlist, and delete all of this paint.</p>
<dt><code>savenetlist </code>[<i>file</i>]</p>
<dd> Save the current netlist on disk. If <i>file</i> is given, write the netlist in <i>file</i>.<code>net</code>. Otherwise, write the netlist back to the place from which it was read.</p>
<dt><code>shownet</code></p>
<dd> Find a piece of paint in any cell underneath the box. Starting from this paint, trace out all paint in all cells that is electrically connected to the starting piece and highlight this paint on the screen. To make the highlights go away, invoke the command with the box over empty space. This command has the same effect as clicking on the &#8220;Show&#8221; menu button.</p>
<dt><code>showterms</code></p>
<dd> Find the labels corresponding to each of the terminals in the current netlist, and generate a feedback area over each. This command has the same effect as clicking on the &#8220;Terms&#8221; menu button.</p>
<dt><code>trace</code> [<i>name</i>]</p>
<dd> This command is similar to <code>shownet</code> except that instead of starting from a piece of paint under the box, it starts from each of the terminals in the net containing <i>name</i> (or the current net if no <i>name</i> is given). All connected paint in all cells is highlighted.</p>
<dt><code>verify</code></p>
<dd> Compare the current netlist against the wiring in the edit cell to make sure that the nets are implemented exactly as specified in the netlist. If there are discrepancies, feedback areas are created to describe them. This command can also be invoked by clicking the &#8220;Verify&#8221; menu button.</p>
<dt><code>writeall</code></p>
<dd> Scan through all the netlists that have been read during this editing session. If any have been modified, ask the user whether or not to write them out. </p>
</dl>
<h2>MOUSE BUTTONS FOR COLORMAP WINDOWS</h2>
<p> Color windows display two sets of colored bars and a swatch of the color being edited. The left set of color bars is labeled Red, Green, and Blue; these correspond to the proportion of red, green, and blue in the color being edited. The right set of bars is labeled Hue, Saturation, and Value; these correspond to the same color but in a space whose axes are hue (spectral color), saturation (spectral purity vs. dilution with white), and value (light vs. dark). </p>
<p> The value of a color is changed by pointing inside the region spanned by one of the color bars and clicking any mouse button. The color bar will change so that it extends to the point selected by the crosshair when the button was pressed. The color can also be changed by clicking a button over one of the &#8220;pumps&#8221; next to a color bar. A left-button click makes a 1% increment or decrement, and a right-button click makes a 5% change. </p>
<p> The color being edited can be changed by pressing the left button over the current color box in the editing window, then moving the mouse and releasing the button over a point on the screen that contains the color to be edited. A color value can be copied from an existing color to the current color by pressing the right mouse button over the current color box, then releasing the button when the cursor is over the color whose value is to be copied into the current color. </p>
<h2>COMMANDS FOR COLORMAP WINDOWS</h2>
<p> These commands work if you are pointing to the interior of a colormap window. The commands are:</p>
<dl>
<dt><code>color </code>[<i>number</i>]</p>
<dd> Load <i>number</i> as the color being edited in the window. <i>Number</i> must be an octal number between 0 and 377; it corresponds to the entry in the color map that is to be edited. If no <i>number</i> is given, this command prints out the value of the color currently being edited.</p>
<dt><code>load </code>[<i>techStyle displayStyle monitorType</i>]</p>
<dd> Load a new color map. If no arguments are specified, the color map for the current technology style (e.g, <code>mos</code>), display style (e.g, <code>7bit</code>), and monitor type (e.g, <code>std</code>) is re-loaded. Otherwise, the color map is read from the file <i>techStyle</i>.<i>displayStyle</i>.<i>monitorType</i><code>.cmap</code> in the current directory or in the system library directory.</p>
<dt><code>save </code>[<i>techStyle displayStyle monitorType</i>]</p>
<dd> Save the current color map. If no arguments are specified, save the color map in a file determined by the current technology style, display style, and monitor type as above. Otherwise, save it in the file <i>techStyle</i>.<i>displayStyle</i>.<i>monitorType</i><code>.cmap</code> in the current directory or in the system library directory. </p>
</dl>
<h2>DIRECTIONS</h2>
<p> Many of the commands take a direction as an argument. The valid direction names are <code>north</code>, <code>south</code>, <code>east</code>, <code>west</code>, <code>top</code>, <code>bottom</code>, <code>up</code>, <code>down</code>, <code>left</code>, <code>right</code>, <code>northeast</code>, <code>ne</code>, <code>southeast</code>, <code>se</code>, <code>northwest</code>, <code>nw</code>, <code>southwest</code>, <code>sw</code>, and <code>center</code>. In some cases, only Manhattan directions are permitted, which means only <code>north</code>, <code>south</code>, <code>east</code>, <code>west</code>, and their synonyms, are allowed. </p>
<h2>LAYERS</h2>
<p> The mask layers are different for each technology, and are described in the technology manuals. The layers below are defined in all technologies:</p>
<dl>
<dt><code>*</code></p>
<dd> All mask layers. Does not include special layers like the label layer and the error layer (see below).</p>
<dt><code>$</code></p>
<dd> All layers underneath the cursor.</p>
<dt><code>errors</code></p>
<dd> Design-rule violations (useful primarily in the <code>see</code> command).</p>
<dt><code>labels</code></p>
<dd> Label layer.</p>
<dt><code>subcell</code></p>
<dd> Subcell layer.</dl>
<p> Layer masks may be formed by constructing comma-separated lists of individual layer names. The individual layer names may be abbreviated, as long as the abbreviations are unique. For example, to indicate polysilicon and n-diffusion, use <code>poly,ndiff</code> or <code>ndiff,poly</code>. The special character <code>&#8211;</code> causes all subsequent layers to be subtracted from the layer mask. For example, <code>*-p</code> means &#8220;all layers but polysilicon&#8221;. The special character <code>+</code> reverses the effect of a previous <code>&#8211;</code>; all subsequent layers are once again added to the layer mask. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ext2sim/">ext2sim</a>(1), <a href="/docs/linux/man/1-ext2spice/">ext2spice</a>(1), <a href="/docs/linux/man/5-cmap/">cmap</a>(5), <a href="/docs/linux/man/5-dstyle/">dstyle</a>(5), <a href="/docs/linux/man/5-ext/">ext</a>(5), <a href="/docs/linux/man/5-sim/">sim</a>(5), <a href="/docs/linux/man/5-glyphs/">glyphs</a>(5), <a href="/docs/linux/man/5-magic/">magic</a>(5), <a href="/docs/linux/man/5-displays/">displays</a>(5), <a href="/docs/linux/man/5-net/">net</a>(5) </p>
<p> Online documentation can be found at the following URLs:<br />
 <a rel="nofollow" href="http://opencircuitdesign.com/magic/">http://opencircuitdesign.com/magic/</a><br />
 <a rel="nofollow" href="http://vlsi.cornell.edu/magic/">http://vlsi.cornell.edu/magic/</a><br />
 The OpenCircuitDesign website contains HTML versions of all the documentation found in the Magic &quot;doc&quot; subdirectory, including tutorials, technology file manual; download, compile and install instructions, and command reference. </p>
<h2>FILES</h2>
<pre><code>
${CAD_ROOT} / magic / sys /.magicstartup file to create default macros

                           ~ /.magicuser -
    specific startup command file

            ${CAD_ROOT} /
        magic / nmos/*some standard nmos cells

${CAD_ROOT}/magic/scmos/*some standard scmos cells

${CAD_ROOT}/magic/sys/*.cmapcolormap files, see CMAP(5) man page

${CAD_ROOT}/magic/sys/*.dstyledisplay style files, see DSTYLE(5) man page

${CAD_ROOT}/magic/sys/*.glyphscursor and window bitmap files, see GLYPH(5) man page

${CAD_ROOT}/magic/sys/*.techtechnology files, see ``Maintainer's Manual
     #2: The Technology File''

${CAD_ROOT}/displaysconfiguration file for Magic serial-line displays
</code></pre>
<p> <i>CAD_ROOT variable.</i> If the shell environment variable <code>CAD_ROOT</code> is set, Magic uses that location instead of the installed location (/usr/local/lib, by default). Normally one would change the search path (see below) rather than redirect the entire <code>CAD_ROOT</code> location. </p>
<p> <i>Search path.</i> Magic&#8217;s system and library files, such as technology files and display-style files, normally are placed in the ${CAD_ROOT}/magic area. However, Magic first tries to find them in the user&#8217;s current directory. This makes it easier for an individual user to override installed system files. The search path is defined by the Magic command <code>path</code>, </p>
<h2>AUTHORS</h2>
<p> <code>Original</code>: Gordon Hamachi, Robert Mayo, John Ousterhout, Walter Scott, George Taylor </p>
<p> <code>Contributors</code>: Michael Arnold (Magic maze-router and Irouter command), Don Stark (new contact scheme, X11 interface, various other things), Mike Chow (Rsim interface). The X11 driver is the work of several people, including Don Stark, Walter Scott, and Doug Pan. </p>
<p> <code>Developers</code>: Ongoing development (magic version 6.5 and higher) made possible by Stefanos Sidiropolous, Tim Edwards, Rajit Manohar, Philippe Pouliquen, Michael Godfrey, and others. </p>
<p> Many other people have contributed to Magic, but it is impossible to list them all here. We appreciate their help!</p>
<h2>BUGS</h2>
<p> If Magic gets stuck for some reason, first try typing Control-C into the terminal window (in the Tcl/Tk version, this is the <i>original</i> terminal, not the Tk console window). Most of Magic&#8217;s lengthy database searches are interruptible. If this doesn&#8217;t work, kill the process. The Tcl/Tk version automatically creates periodic backups that may be recovered with &quot;magic -r&quot;. </p>
<p> Report bugs to <code>magic-dev [at] csl.cornell.edu</code>. Please be specific: tell us exactly what you did to cause the problem, what you expected to happen, and what happened instead. If possible send along small files that we can use to reproduce the bug. A list of known bugs and fixes is also available from the above address. Tell us which version of magic you are running. </p>
<h2>Index</h2>
