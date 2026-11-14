---
title: "fvwm-convert-2-4(1)"
name: "fvwm-convert-2-4"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-convert-2-4/"
description: "fvwm-convert-2.4 – convert fvwm 2.2.x configuration file to fvwm 2.4 syntax"
---

<p>fvwm-convert-2.4 &#8211; convert fvwm 2.2.x configuration file to fvwm 2.4 syntax</p>
<h2>Synopsis</h2>
<p><code>fvwm-convert-2.4</code> [<i>source</i>] [<i>dest</i>]</p>
<h2>Description</h2>
<p><code>fvwm-convert-2.4</code> converts an fvwm 2.2.x configuration file into an fvwm 2.4 compatible syntax. It is not suitable to convert older 1.x configuration files. Please use <code>fvwm-convert-2.2</code> to convert these to the 2.2.x format first. </p>
<p> By default, <code>fvwm-convert-2.4</code> converts <i>~/.fvwm2rc,</i> saving the results in <i>~/.fvwm/.fvwm2rc.</i> You must create the <i>~/.fvwm</i> directory before running this command. Starting with the 2.4 release, the directory <i>~/.fvwm</i> is the default location for fvwm user configuration files. Different source and destination files may be given. If the destination file already exists, this program exits. While the program runs it will generate a temporary file with the same name as the destination file with the suffix &quot;.pass1&quot; added. </p>
<p> <code>fvwm-convert-2.4</code> makes the following changes:</p>
<dl>
<dt><code>PixmapPath/IconPath</code></p>
<dd>In fvwm 2.4, the PixmapPath and IconPath commands are replaced by the ImagePath command. In addition, the ImagePath can be compiled into fvwm. <code>fvwm-convert-2.4</code> changes the PixmapPath and IconPath commands to ImagePath commands and removes any directories that are compiled into fvwm. Paths starting with a dollar sign are also removed.</p>
<dt><code>ModulePath</code></p>
<dd>In fvwm 2.4, the ModulePath is compiled into fvwm. <code>fvwm-convert-2.4</code> removes any ModulePath commands it finds. If you are using your own modules, (not the ones that come with fvwm), you will have to fix your configuration file after using <code>fvwm-convert-2.4</code>.</p>
<dt><code>HilightColor</code></p>
<dd>In fvwm 2.4, the HighlightColor command is replaced by a Style command using the HilightFore and HilightBack arguments. <code>fvwm-convert-2.4</code> makes these changes.</p>
<dt><code>HilightColorset</code></p>
<dd>In fvwm 2.4, the HighlightColorset command that was present in some of the 2.3.x beta releases is replaced by a Style command using the HilightColorset style. <code>fvwm-convert-2.4</code> makes these changes.</p>
<dt><code>WindowShadeAnimate</code></p>
<dd>In fvwm 2.4, the WindowShadeAnimate command is replaced by the WindowShadeSteps Style option. <code>fvwm-convert-2.4</code> makes this change.</p>
<dt><code>WindowFont</code></p>
<dd>In fvwm 2.4, the WindowFont command is replaced by a Style command using the Font argument. <code>fvwm-convert-2.4</code> makes this change.</p>
<dt><code>ColorLimit</code></p>
<dd>In fvwm 2.4, the ColorLimit command is automatic. If you have a limited colormap, color limiting is the default. <code>fvwm-convert-2.4</code> removes any ColorLimit command that it finds.</p>
<dt><code>GlobalOpts</code></p>
<dd>The GlobalOpts command is converted to <code>Style</code> options and the <code>BugOpts</code> command. Some options can not be converted automatically, though.</p>
<dt><code>Read</code></p>
<dd>Prints a message identifying any read commands found. The files being read may need to be converted also.</p>
<dt><code>Placement Styles</code></p>
<dd>Any of the old placement Styles found in the file can not be converted automatically. Instead, <code>fvwm-convert-2.4</code> prints a warning. For details about the conversion, please refer to the &quot;Window manager placement&quot; section of the fvwm man page.</p>
<dt><code>FvwmConfig and FvwmPipe</code></p>
<dd>These modules are no longer a part of the fvwm distribution. <code>fvwm-convert-2.4</code> prints a warning if these modules are found in the file.</p>
<dt><code>FvwmButtons panels</code></p>
<dd>The syntax of panels in FvwmButtons has changed. The conversion can not be done automatically. <code>fvwm-convert-2.4</code> prints a message when it encounters a potential panel definition. For details about the conversion, please refer to the &quot;CONVERTING OLD PANEL CONFIGURATIONS&quot; section of the FvwmButtons man page.</dl>
<h2>Bugs</h2>
<p>You need Perl to be installed. </p>
<p> <i>WindowFont</i> and <i>HilightColor</i> commands embedded in functions are not found. If you have either of these commands in functions, they are not detected. </p>
<p> Known bugs can be found in the fvwm bug tracking system (accessible from the fvwm home page). </p>
<p> Bug reports can be sent to the fvwm-workers mailing list (see the <i>FAQ</i>). </p>
<h2>Author</h2>
<p>Dan Espen &lt;despen [at] telcordia.com&gt;.</p>
