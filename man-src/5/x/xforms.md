---
title: "xforms(5)"
name: "xforms"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xforms/"
description: "xforms – A GUI Toolkit for X Window Systems"
---

<p>xforms &#8211; A GUI Toolkit for X Window Systems</p>
<h2>Synopsis</h2>
<p><code>Forms Library for X</code> (xforms) is a GUI toolkit and builder for the X Window Systems and runs on all major UNIX platforms as well as OpenVMS and OS2. <code>Forms Library</code> is too complex to be described in the &quot;man&quot; page format. Ask your system administrator for the location of the HTML, PDF or PostScript document or follow the links on the <code>Forms Library</code>&#8216;s home page for an online version of the documentation.</p>
<h2>Description</h2>
<p><code>Forms Library</code> is a graphical user interface toolkit based on Xlib for X Window Systems. It comes with a rich set of objects such as buttons, browsers, sliders and menus integrated into an elegant event/object callback execution model that allows fast and easy construction of X applications. In addition, the library has support for image read and write, format conversion and simple image processing. The library consists of a flexible set of C-routines that can be used in C and C++ programs (As of this writing, perl, ada95, pascal, scheme and Fortran bindings to the <code>Forms Library</code> are in beta.) </p>
<p> The library is efficient and portable and runs on all major Unix platforms, including Sun, SGI, HP, DEC Alpha/OSF, IBM RS6000, Convex, Cray, Linux, FreeBSD, NetBSD, SCO, Unixware, OpenBSD , BSDi, DecSystem(mips)/Ultrix and others. Non-unix platforms include OpenVMS, OS/2, and Window/NT. </p>
<p> Bundled with the library is also a Form designer, <i>fdesign,</i> which can be used to build interaction forms in a WYSIWYG (what you see is what you get) way and to generate the corresponding C (or any of the binding languages) code for you. 50+ demos in source code are distributed with the library.</p>
<h2>Options</h2>
<p>All programs written using the <code>Forms Library</code> recognize the following command line options</p>
<dl>
<dt><code>-display</code><i> host:dpy</i></p>
<dd>specifies the server to connect to.</p>
<dt><code>-bw</code><i> borderwidth</i></p>
<dd>specifies the border width to use for built-in objects.</p>
<dt><code>-flversion</code></p>
<dd>prints the xforms version information.</p>
<dt><code>-visual</code><i> visualName</i></p>
<dd>requests a visual by name such as TrueColor etc. By default the <code>Forms Library</code> always selects the visual that has the most depth.</p>
<dt><code>-depth</code><i> depth</i></p>
<dd>requests a specific depth.</p>
<dt><code>-fldebug</code><i> level</i></p>
<dd>generates some info about the state of the <code>XForms.</code> where <i>level</i> is an integer between 1-5 and controls the amount of information to output. Depending on the options used when the <code>Forms Library</code> was built, a level more than 3 might not be available.</p>
<dt><code>-sync</code></p>
<dd>runs the application in synchronous mode with debug level set to 4.</p>
<dt><code>-private</code></p>
<dd>requests a private colormap for the application.</p>
<dt><code>-shared</code></p>
<dd>requests a shared colormap even if the application needs more colors than available. For those colors that can&#8217;t be allocated in the shared colormap, substitutions are made so the closest matching color is used.</p>
<dt><code>-stdcmap</code></p>
<dd>requests a standard colormap.</p>
<dt><code>-name newname</code></p>
<dd>specifies the application name under which resources are to be obtained, rather than the default executable file name. <code></dl>
<p> </code></p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1L-fdesign/">fdesign</a>(1L), <a href="//www.systutorials.com/docs/linux/man/1L-fd2ps/">fd2ps</a>(1L) </p>
<h2>Author</h2>
<p>Copyright (c) 1996-2002 T.C. Zhao, Mark Overmars and Steve Lamont<br />
 Since 2002: GNU Lesser General Public License<br />
 Maintainers: Jean-Marc Lasgouttes, Angus Leeming, Jens Thoms Toerring &lt;jt [at] toerring.de&gt;</p>
<h2>Home Page</h2>
<p><a rel="nofollow" href="http://xforms-toolkit.org">http://xforms-toolkit.org</a><br />
 <a rel="nofollow" href="http://savannah.nongnu.org/projects/xforms/">http://savannah.nongnu.org/projects/xforms/</a></p>
