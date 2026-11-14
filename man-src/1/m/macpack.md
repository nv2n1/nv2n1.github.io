---
title: "macpack(1)"
name: "macpack"
section: "1"
letter: "m"
url: "/docs/linux/man/1-macpack/"
description: "macpack – Macintosh OS X Packager for managed gui assemblies"
---

<h2>NAME</h2>
<p> macpack &#8211; Macintosh OS X Packager for managed gui assemblies</p>
<h2>SYNOPSIS</h2>
<p> <code>macpack [options] assembly</code></p>
<h2>DESCRIPTION</h2>
<p> <i>macpack</i> is a tool used to package managed assemblies (like System.Windows.Forms or Cocoa#) that require gui availability for deployment on Mac OS X. </p>
<p> macpack will prepare a OS X compatible bundle from the provided assembly and resources. The bundle will include the specified assembly as well as any of the provided resources (specified with the -resource: switch). </p>
<p> Developers can specify the kind of application to produce using the -mode: argument. This controls how the environment in the Mono class libraries is setup. </p>
<h2>OPTIONS</h2>
<p> <i>-a assembly</i> </p>
<p> This option tells macpack where the managed assembly that you want to bundle resides. This option is also used to point to the shell script to launch in the case of a X11/Gtk# application. </p>
<p> This is the same as just passing the assembly as an argument. </p>
<p> <i>-m [winforms,x11,console,cocoa]</i> or <i>-mode:[winforms,x11,console,cocoa]</i> </p>
<p> A value indicating the kind of application: WinForms is a Winforms application running on Quartz; X11 is an application that requires the X11 server to run; console is a non-graphical application; cocoa is an application based on Cocoa# </p>
<p> <i>-n NAME</i> or <i>-appname:NAME</i> </p>
<p> This option specifies the application name of the emitted bundle. This is what you will see in Finder. </p>
<p> <i>-o DIRECTORY</i> or <i>-output:DIRECTORY</i> </p>
<p> This option specifies the path to output the generated Application. </p>
<p> <i>-r RESOURCE</i> or <i>-resource:RESOURCE</i> </p>
<p> This option can be specified multiple times. It will place a copy of each resource into the bundles resources directory. Alternatively, you can use a comma separated list of resources.</p>
<h2>AUTHOR</h2>
<p> Geoff Norton</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
