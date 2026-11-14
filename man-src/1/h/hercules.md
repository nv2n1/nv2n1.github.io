---
title: "hercules(1)"
name: "hercules"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hercules/"
description: "Hercules – IBM System/370, ESA/390, and z/Architecture Emulator"
---

<h2>NAME</h2>
<p> <code>Hercules</code> &#8211; IBM System/370, ESA/390, and z/Architecture Emulator</p>
<h2>SYNOPSIS</h2>
<p> <code>hercules</code> [<code>-f</code> <i>config-filename</i>] [<code>-d</code>] [<code>-b</code> <i>logo-filename</i>] [<code>-p</code> <i>dyn-load-dir</i>] [[<code>-l</code> <i>dynmod-to-load</i>]&#8230;] [&gt; <i>logfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Hercules</code> is a software implementation of the System/370, ESA/390 and z/Architecture mainframe architectures. </p>
<p> It means that your PC can emulate an IBM mainframe processor. The mainframe can range from a System/360 to a z10 &#8211; running in &quot;S/370&quot; mode, &quot;ESA/390&quot; mode, or &quot;z/Architecture&quot; mode. </p>
<p> <code>Hercules</code> executes S/370, ESA/390, and z/Architecture instructions and channel programs. It emulates mainframe I/O devices by using PC devices. For example, 3390 DASD devices are emulated by large files on your hard disk, and local 3270 screens are emulated by tn3270 sessions. (Note: Not all 370 and 390 features have been implemented in <code>Hercules</code>. Also, certain non-standard models, 360/20s, and the 360/67 virtual memory mode are not emulated.) </p>
<p> <code>Hercules</code> implements only the raw S/370, ESA/390, and z/Architecture instruction set; it does not provide any operating system facilities. This means that you need to provide an operating system or standalone program which <code>Hercules</code> can load from an emulated disk or tape device. You will have to write the operating system or standalone program yourself, unless you can manage to obtain a license from IBM to run one of their operating systems on your PC, or use IBM programs and operating systems which have been placed in the public domain.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> <i>config-filename</i></p>
<dd> Sets the name of the configuration file. The default, if none is specified, is <code>hercules.cnf</code>. The default may be overridden via the <code>HERCULES_CNF</code> environment variable.</p>
<dt><code>-d</code></p>
<dd> Specifies that Hercules is to be run in &#8216;daemon&#8217; mode, wherein it runs invisibly with no attached console.</p>
<dt><code>-b</code> <i>logo-filename</i></p>
<dd> Sets the name of the file containg the screen logo that&#8217;s presented when a 3270 terminal connects. When not specified the default <code>herclogo.txt</code> file is looked for and when not found the built-in logo is used.</p>
<dt><code>-p</code> <i>dyn-load-dir</i></p>
<dd> Sets the directory from which dynamic modules are to be loaded. The default depends on the host platform on which Hercules is being run. This option overrides the default.</p>
<dt><code>-l</code> <i>dynmod-to-load</i></p>
<dd> Sets the name of an additional dynamic module to be loaded at startup. More than one additional module may be specified, although each must be preceded with the <code>-l</code> option specifier.</p>
<dt><i>logfile</i></p>
<dd> Sets an optional log file which will receive a copy of all messages displayed on the control panel</dl>
<h2>FILES</h2>
<p> <code>hercules.cnf</code></p>
<h2>ENVIRONMENT</h2>
<p> <code>HERCULES_CNF</code></p>
<h2>AUTHORS</h2>
<p> <code>Hercules</code> was created by Roger Bowler. Jay Maynard (“the Tron Guy”) was the maintainer from 2000 to 2012. Jan Jaeger designed and implemented many of the advanced features of <code>Hercules</code>, including dynamic reconfiguration, integrated console, interpretive execution and z/Architecture support. A dedicated crew of programmers is constantly at work implementing new features and fixing bugs. </p>
<p> This manual page was written by Dan Horák using text snippets from the <code>Hercules</code> web site.</p>
<h2>SEE ALSO</h2>
<p> <code>Hercules</code> Homepage: <code><a rel="nofollow" href="http://www.hercules-s390.eu">http://www.hercules-s390.eu</a></code> </p>
<h2>Index</h2>
