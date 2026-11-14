---
title: "fdesign(1)"
name: "fdesign"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fdesign/"
description: "fdesign – Forms Library User Interface Designer"
---

<h2>NAME</h2>
<p> fdesign &#8211; Forms Library User Interface Designer</p>
<h2>SYNOPSIS</h2>
<p> fdesign [-xformoptions] [-options] [files]</p>
<h2>DESCRIPTION</h2>
<p> <i>fdesign</i> is a GUI builder that helps in the construction of graphical user interface in a WYSIWYG (&quot;what you see is what you get&quot;) way by allowing the user to directly manipulate various objects, such as buttons, sliders and menus etc. Once a satisfactory UI is constructed, the user can save the composed interface into a set of external files. Files with the extension &#8216;.fd&#8217; contain all information about the objects and can be read in again by <i>fdesign</i>. The files with C code and header files when compiled and linked against the <code>Forms Library</code>, generate code that at run-time constructs the exact same interface as the ones seen within <i>fdesign</i>. </p>
<p> A variety of output languages is possible via external filters. As of this writing, C, perl, ada95, Fortran, pascal, and PostScript output filters are known to exist. </p>
<h2>OPTIONS</h2>
<p> <i>fdesign</i> accepts all standard <code>Forms Library</code> command line options as well as the following:</p>
<dl>
<dt><code>-help</code></p>
<dd> Prints a brief summary of all command line options. This option does not require a connection to the X server.</p>
<dt><code>-version</code></p>
<dd> Prints the current version of <i>fdesign</i> and exits.</p>
<dt><code>-geometry</code><i> geom</i></p>
<dd> Specifies the prefered size and location of main working area in which the UI is to be constructed.</p>
<dt><code>-convert</code><i> fdfile-list</i></p>
<dd> This option prevents <i>fdesign</i> from attempting to make a connection to the X server. The file list following this flag is converted to C code directly.</p>
<dt><code>-dir</code><i> destdir</i></p>
<dd> output any converted files in <i>destdir</i>.</p>
<dt><code>-unit</code><i> pixel|point|mm|cp|cmm</i></p>
<dd> selects the unit of measure for object geometries. For non-pixel unit, the interface created is screen resolution independent and may be desirable for many applications. Note that for typical screens, <i>point</i> (about 1/72 inch) and <i>mm</i> may be too coarse and subject to round-off errors. Use <i>cp</i> (centi-point, 100th of a point) and <i>cmm</i> (centi-mm) instead.</p>
<dt><code>-altformat</code></p>
<dd> selects an alternative format for the generated C code where global variables are used for the UI components.</p>
<dt><code>-main</code></p>
<dd> requests the output of main program template.</p>
<dt><code>-callback</code></p>
<dd> requests the output of callback function template.</p>
<dt><code>-compensate</code></p>
<dd> requests the emission of font/server resolution variation compensation code.</p>
<dt><code>-I</code><i> headerfile</i></p>
<dd> uses an alternative header file instead of the default forms.h in the output C code.</p>
<dt><code>-lax</code></p>
<dd> requests relaxed C syntax checking.</p>
<dt><code>-ps</code></p>
<dd> This option specifies that instead of emitting the c code for the user interface, PostScript code should be emitted.</p>
<dt><code>-ada</code></p>
<dd> This option requests ada95 code output</p>
<dt><code>-perl</code></p>
<dd> This option requests perl code output.</p>
<dt><code>-fortran</code></p>
<dd> This option requests Fortran code output.</p>
<dt><code>-pascal</code></p>
<dd> This option requests pascal code output.</p>
<dt><code>-nocode</code></p>
<dd> suppresses the output of UI code. Only the .fd file is written.</dl>
<p> The most useful <code>Forms Library</code> command line options are</p>
<dl>
<dt><code>-display</code><i> host:dpy</i></p>
<dd> This option specifies the X server to connect.</p>
<dt><code>-flversion</code></p>
<dd> This option prints the version string of the <code>Forms Library</code>, with which fdesign was build.</p>
<dt><code>-name</code><i> appname</i></p>
<dd> This option specifies the application name under which resources are to be obtained, instead of the executable name. <i>appname</i> should not contain . or *. <i>fdesign</i>.</dl>
<h2>RESOURCES</h2>
<p> The program understands all of the <code>Forms Library</code>&#8216;s resource names and classes as well as the following</p>
<dl>
<dt>control.geometry (class Control.Geometry)</p>
<dd> specifies the geometry of the control panel. Currently the size is ignored.</p>
<dt>unit (Unit)</p>
<dd> specifies the default unit of measure. Default is pixel. </p>
<dt>attributes.geometry (class Attributes.Geometry)</p>
<dd> specifies the geometry of the object attributes panel. Currently the size is ignored.</p>
<dt>align.geometry (class Align.Geometry)</p>
<dd> specifies the geometry of the object align panel. Currently the size is ignored.</p>
<dt>xformsHeader (class XFormsHeader)</p>
<dd> specifies the header filename generated in the output C code. Default is forms.h</p>
<dt>filter (class Filter)</p>
<dd> specifies post-processing filter (an external executable name).</p>
<dt>language (class Language)</p>
<dd> specifies target language name. </p>
</dl>
<p> Among the standard <code>Forms Library</code> resources, the following are most useful</p>
<dl>
<dt>xform.fontsize (class XFORM.FontSize)</p>
<dd> specifies the font size used for most object labels.</p>
<dt>xform.pupfontsize (class XFORM.PupFontSize)</p>
<dd> specifies the font size used in pop-up menus.</p>
<dt>xform.browserFontSize (class XFORM.BrowserFontSize)</p>
<dd> specifies the font size used for the text inside a browser. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-xforms/">xforms</a>(5), <a href="//www.systutorials.com/docs/linux/man/1L-fd2ps/">fd2ps</a>(1L)</p>
<h2>AUTHOR</h2>
<p> Copyright (c) 1996-2002 T.C. Zhao &lt;tc_zhao [at] yahoo.com&gt; and Mark Overmars &lt;markov [at] cs.ruu.nl&gt;<br />
 Since 2002: GNU Lesser General Public License<br />
 Maintainers: Jean-Marc Lasgouttes, Angus Leeming and Jens Thoms Toerring &lt;jt [at] toerring.de&gt;</p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://xforms-toolkit.org">http://xforms-toolkit.org</a><br />
 <a rel="nofollow" href="http://savannah.nongnu.org/projects/xforms/">http://savannah.nongnu.org/projects/xforms/</a> </p>
<h2>Index</h2>
