---
title: "openapp(1)"
name: "openapp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openapp/"
description: "openapp – launch applications from the command line"
---

<h2>NAME</h2>
<p> openapp &#8211; launch applications from the command line </p>
<h2>SYNOPSIS</h2>
<p> <code>openapp</code> [<code>&#8211;find</code>] [<code>&#8211;debug</code> [<code>&#8211;gdb=</code> <i>debuger</i>]] [ <code>&#8211;library-combo=</code><i>library-combo</i> ] <i>application</i> [<i>arguments&#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>openapp</code> command allows you to launch graphical GNUstep applications from the command line. </p>
<p> <i>application</i> is the complete or relative name of the application program with or without the .app extension, like <code>Ink.app. </code> </p>
<p> <i>arguments</i> are the arguments passed to the application. </p>
<p> <code>openapp</code> first checks whether the application is in the current working directory. If not then searches the GNUstep domains&#8217; Applications folders in the following order: User (i.e. <i>~/GNUstep/Applications</i>), Local, Network, System. First match wins. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;find</code><i> application</i></p>
<dd> will print out the full path of the application executable which would be executed, without actually executing it. It will also list all paths that are attempted.</p>
<dt><code>&#8211;debug</code><i> application</i></p>
<dd> starts the application in the debugger. By default <code>gdb</code>, but this can be changed with the <code>&#8211;gdb=</code> argument or through the <code>GDB</code> shell variable.</p>
<dt><code>&#8211;library-combo=</code><i>library-combo</i></p>
<dd> Starts the application with the specified library combo. This is a rarely used option in a non-flattened setup. See the <code><a href="/docs/linux/man/7-library-combo/">library-combo</a></code>(7) man-page for more information about the different library combinations.</p>
<dt><code>&#8211;help</code></p>
<dd> print above usage description. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Start <code>Ink.app</code> without additional parameters: </p>
<p> <code>openapp Ink.app </code> </p>
<p> Launch <code>Ink.app</code> and pass it the <code>&#8211;debug</code> argument: </p>
<p> <code>openapp &#8211;debug Ink.app</code> </p>
<p> To determine which executable is launched by openapp, type: </p>
<p> <code>openapp &#8211;find Ink.app</code> </p>
<p> The output of the above command might be something like: <i>/usr/GNUstep/Local/Applications/Ink.app/Ink</i> </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GNUSTEP_CONFIG_FILE</code></p>
<dd> is used to determine where the <code>GNUstep.sh</code> configuration file is located. If the variable is not set <code>openapp</code> tries to locate it in the folder where <code>openapp</code> was started, then in the user domain, and as a last resort in the system domain (or actually the place you configured (<i>&#8211;with-config-file=</i>) during building).</p>
<dt><code>GDB</code></p>
<dd> Sets the debugger to use when <code>&#8211;debug</code> is used. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-debugapp/">debugapp</a>(1), <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7), <a href="/docs/linux/man/1-gopen/">gopen</a>(1), <a href="/docs/linux/man/7-library-combo/">library-combo</a>(7), <a href="/docs/linux/man/1-opentool/">opentool</a>(1) </p>
<h2>HISTORY</h2>
<p> Work on <code>openapp</code> started October 1997. </p>
<p> <code>openapp</code> was originally written by Ovidiu Predescu &lt;ovidiu [at] net-community.com&gt; and is now maintained by Nicola Pero &lt;nicola.pero [at] meta-innovation.com&gt; </p>
<h2>AUTHORS</h2>
<p> This manual page was first written July 2003 by Martin Brecher &lt;martin [at] mb-itconsulting.com&gt;. </p>
<p> Updated with notes from Hubert Chathi &lt;uhoreg [at] debian.org&gt; and Dennis Leeuw &lt;dleeuw [at] made-it.com&gt;, December 2007 by Dennis Leeuw. </p>
<h2>Index</h2>
