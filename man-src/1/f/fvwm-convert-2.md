---
title: "fvwm-convert-2(1)"
name: "fvwm-convert-2"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-convert-2/"
description: "fvwm-convert-2.6 – convert fvwm 2.4.x configuration file to fvwm 2.6 style"
---

<h2>NAME</h2>
<p> fvwm-convert-2.6 &#8211; convert fvwm 2.4.x configuration file to fvwm 2.6 style</p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-convert-2.6</code> [<i>&#8211;follow-read</i>|<i>-f</i>] [<i>&#8211;help</i>|<i>-h</i>] source [<i>dest</i>]</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>&#8211;help</code> | <code>-h</code></p>
<dd> Prints a usage message to the screen.</p>
<dt><code>&#8211;follow-read</code> | <code>-f</code></p>
<dd> Follows files found along with the <code>Read</code> command.</dl>
<h2>DESCRIPTION</h2>
<p> <code>fvwm-convert-2.6</code> converts an fvwm 2.4.x configuration file into a fvwm 2.6 file with compatible syntax. It is not suitable to convert older 2.x configuration files. Please use <code>fvwm-convert-2.2</code> to convert these to the 2.2.x format first, and then if necessary <code>fvwm-convert-2.4</code> </p>
<p> By default, <code>fvwm-convert-2.6</code> won&#8217;t look for a given config file. This must be specified as the first parameter to <code>fvwm-convert-2.6. </code> Different source and destination files may be given. If the destination file already exists, this program exits. If no destination file is given, then the filename is the same name as the source file with the suffix &quot;.converted&quot; added. Without an absolute path given as the destination path to the destination file, the program will create the destination file in the CWD. </p>
<p> <code>fvwm-convert-2.6</code> makes the following changes:</p>
<dl>
<dt><code>Style lines</code></p>
<dd> In fvwm 2.4, most style options could be negated from their counterparts using NoFoo &#8212; fvwm-convert-2.6 corrects this by now using !Foo.</p>
<dt><code>ModulePath</code></p>
<dd> In fvwm 2.4 and beyond, the ModulePath is compiled into fvwm. <code>fvwm-convert-2.6</code> comments out any ModulePath commands it finds. If you are using your own modules, (not the ones that come with fvwm), you will have to fix your configuration file after using <code>fvwm-convert-2.6</code>.</p>
<dt><code>Conditional command syntax</code></p>
<dd> In fvwm 2.4, the conditional command options were whitespace-separated &#8212; they should now be comma-separated instead. In addition, the older syntax to Next and Prev of using [*] to denote all windows has been removed entirely. Both these checks and conversions are done on function commands, key/mouse bindings.</p>
<dt><code>WindowShadeSteps</code></p>
<dd> In fvwm 2.4, the WindowShadeSteps command is replaced by the WindowShadeSteps Style option. <code>fvwm-convert-2.6</code> makes this change.</p>
<dt><code>FvwmTheme</code></p>
<dd> In fvwm 2.6, the FvwmTheme module is replaced by a series of Colorset commands. Whilst <code>fvwm-convert-2.6</code> will try and make this change, it is still recommended that this is checked after conversion.</p>
<dt><code>EdgeResistance</code></p>
<dd> In fvwm 2.6, the EdgeResistance command is has been split to include an additional style option for EdgeMoveResistance. <code>fvwm-convert-2.6</code> makes any changes necessary.</p>
<dt><code>StartFunction / RestartFunction / InitFunction</code></p>
<dd> In fvwm 2.6, the need for using InitFunction and/or RestartFunction is redundant when StartFunction is read at both of these times. <code>fvwm-convert-2.6 </code> attempts to convert this.</p>
<dt><code>Read</code></p>
<dd> If <code>-f</code> or <code>&#8211;follow-read</code> is given, any files <code>fvwm-convert-2.6</code> can detect and open will be converted automatically, else a list of files that can be followed are printed to the screen. </p>
<dt></dl>
<h2>BUGS</h2>
<dd>
<p> <i>InitFunction</i> and <i>RestartFunction</i> and hence <i>StartFunction</i> are printed at the end of the files &#8212; this slight reordering might put some comments before in an odd spot. </p>
<p> When converting over FvwmTheme lines, the colorset definitions might well be broken, but these cannot easily be converted. </p>
<p> Bug reports can be sent to the fvwm-workers mailing list (see the <i>FAQ</i>).</p>
<h2>AUTHOR</h2>
<p> Thomas Adam &lt;thomas.adam22 [at] gmail.com&gt; </p>
<h2>Index</h2>
