---
title: "gnustep(7)"
name: "gnustep"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gnustep/"
description: "GNUstep – A free implementation of the OpenStep standard"
---

<p>GNUstep &#8211; A free implementation of the OpenStep standard </p>
<h2>Description</h2>
<p><code>GNUstep</code> provides an Object-Oriented application development framework and toolset for use on a wide variety of computer platforms. <code>GNUstep</code> is based on the original OpenStep specification provided by NeXT, Inc. (now Apple and called Cocoa). <code>GNUstep</code> is written in Objective-C, an object-oriented superset of the C programming language, similar to SmallTalk. However there exist a number of bridges and interfaces to develop <code>GNUstep</code> programs using other languages like JAVA or Ruby. The <code>GNUstep</code> core system consists of the following parts, which are jointly refered to as <i>gnustep-core</i> :</p>
<dl>
<dt><i>gnustep-make</i></p>
<dd>A set of scripts and makefiles that heavily ease the creation and maintenance of software projects.</p>
<dt><i>gnustep-base</i></p>
<dd>The FoundationKit libraries for non-GUI tools providing everything from string and array classes, filemanager classes to distributed objects.</p>
<dt><i>gnustep-gui</i></p>
<dd>The ApplicationKit containing widgets, workspace classes and means for applications to interact with the user. This is the frontend of <code>GNUstep</code>&#8216;s GUI part.</p>
<dt><i>gnustep-back</i></p>
<dd>This is the backend of <code>GNUstep</code>&#8216;s GUI part which does the actual rendering and event handling. It acts as a layer between gnustep-gui and the operating/drawing system. Backends exist for X11 (one using cairo, one using libart, one using xlib drawing) and win32.</dl>
<p> Apart from the above, there exist a number of addon libraries related to GNUstep, like <code>Renaissance</code> which allows developers to specify an application&#8217;s user interface in xml. For database access, there is <code>GDL2</code> &#8211; the GNUstep Database Library. Please refer to the <code>GNUstep</code> website for more information. <code>GNUstep</code> per default is self-contained. That means that all <code>GNUstep</code> applications, tools, libraries and add-ons are installed into the <code>GNUstep</code> directory hierarchy. However as of <i>gnustep-make-2.0.0</i> it is also possible to install everything in compliance with other filesystem hierarchies. See the <i>FilesystemLayouts</i> directory in the source package of <i>gnustep-make</i> for more information. There are four domains which are searched for files: the System domain, which should only contain the core system files, the Local domain which stores all that has later been installed on the system, the Network domain which should be used for importing data from a remote system, and the User domain which resides in the user&#8217;s home directory (mostly <i>~/GNUstep</i>). A complete description of the default <code>GNUstep</code> layout can be found in the <i>filesystem.pdf</i>.</p>
<h3>Tools And Applications</h3>
<p>In the world of GNUstep the term <i>tool</i> refers to command line programs whereas <i>applications </i> are fully fledged GUI programs. Naturally, <i>tools</i> reside in the domains&#8217; Tools folder, <i>applications</i> can be found in the domains&#8217; Applications folder. Applications are either launched using the <code>openapp</code> command or from the Workspace.</p>
<h3>Services</h3>
<p>In <code>GNUstep</code> applications globally offer functionality to other applications through <i>services</i>. They can be reached through the Services menu entry in an application&#8217;s main menu. Apart from <i>services</i> offered by applications, there may be programs whose sole purpose is the offering of services. They can be found in the domains&#8217; Libary/Services folders. The <code>make_services</code> tool makes sure the services are known to other applications when a application is newly installed.</p>
<h3>Bundles</h3>
<p>A bundle is a collection of resources making up a discrete package for use. There are currently three types of bundles: applications, frameworks and loadable bundles. A loadable bundle is a kind of plug-in. There are two types of loadable bundles, namely plug-ins and palettes. The plug-in is noramlly refered to as a bundle, which can make it a bit confusing. A plug-in is a bundle that can be loaded by an application to provide additional functionality, while a palette is a plug-in for <code>GORM</code>, the interface builder. A palette is used to extend <code>GORM</code> with custom UI objects. Palettes have a <i>.palette</i> extension.</p>
<h3>The Workspace</h3>
<p>The central place of the user interface is the <i>Workspace </i> or <i>Workspace Manager</i> which acts as an interface between the user and parts of the system like files, processes, etc. The GWorkspace application provides this functionality in GNUstep. See the GWorkspace website for more details.</p>
<h3>Developer Applications</h3>
<p>What would a development environment be without the applications to create applications? The applications provided by GNUstep for Rapid Application Development are:</p>
<dl>
<dt>GORM</p>
<dd><code>GORM</code> is the interface modeler. With <code>GORM</code> you can quickly create the graphical interface of your application.</p>
<dt>Project Center</p>
<dd><code>Project Center</code> is the program where you can develop your program. It offers you automatic generation of <i>GNUmakefiles</i> , project maintenance and of course a code editor. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gcc/">gcc</a>(1), <a href="/docs/linux/man/1-gdnc/">gdnc</a>(1), <a href="/docs/linux/man/8-gdomap/">gdomap</a>(8), <a href="/docs/linux/man/1-gopen/">gopen</a>(1), <a href="/docs/linux/man/1-gpbs/">gpbs</a>(1), <a href="/docs/linux/man/1-make/">make</a>(1), <a href="/docs/linux/man/1-openapp/">openapp</a>(1) </p>
<p> <code>GNUstep Websites:</code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnustep.org/">http://www.gnustep.org/</a></p>
<dd>Official GNUstep website</p>
<dt><a rel="nofollow" href="http://wiki.gnustep.org/">http://wiki.gnustep.org/</a></p>
<dd>GNUstep Wiki (lots of useful information)</p>
<dt><a rel="nofollow" href="http://savannah.gnu.org/projects/gnustep/">http://savannah.gnu.org/projects/gnustep/</a></p>
<dd>GNUstep Project Page</p>
<dt><a rel="nofollow" href="http://gnustep.made-it.com/">http://gnustep.made-it.com/</a></p>
<dd>GNUstep Documentation Library</p>
<dt><a rel="nofollow" href="http://www.collaboration-world.com">http://www.collaboration-world.com</a></p>
<dd>Collaboration World, the home of GNUmail</p>
<dt><a rel="nofollow" href="http://www.gnustep.it/">http://www.gnustep.it/</a></p>
<dd>The home of GWorkspace, JIGS, Renaissance and programming tutorials.</dl>
<p> <code>Mailinglists</code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnustep.org/information/gethelp.html">http://www.gnustep.org/information/gethelp.html</a></p>
<dd>Mailing lists and mailing list archives.</dl>
<p> <code>IRC</code></p>
<dl>
<dt>#GNUstep on FreeNode</p>
<dd>You are invited to join the #GNUstep IRC channel on FreeNode (irc.freenode.net).</dl>
<h2>History</h2>
<p><code>GNUstep</code> was at first a collaboration of two projects that wanted to create a single <code>GNUstep</code> project that complied to the OpenStep specification provided by NeXT Computer, Inc. and SunSoft, Inc. Development of this joint effort started around 1993-1994. For a more detailed history description see the GNUstep Documentation Library referenced in the <code>SEE ALSO</code> section. </p>
<p> GNUstep is developed and maintained by a large number of people. Please see &lt;<a rel="nofollow" href="http://www.gnustep.org/developers/whoiswho.html">http://www.gnustep.org/developers/whoiswho.html</a>&gt; for a list.</p>
<h2>Authors</h2>
<p>This man-page was first written by Martin Brecher &lt;martin [at] mb-itconsulting.com&gt; in august of 2003. </p>
<p> In December 2007 it was expanded by Dennis Leeuw &lt;dleeuw [at] made-it.com&gt; and made to comply with the gnustep-make-2.0.x releases.</p>
