---

title: "fdesign(1)"
name: "fdesign"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fdesign/"
description: "fdesign – Forms Library User Interface Designer"
---

<p> fdesign &#8211; Forms Library User Interface Designer</p>
<h2>SYNOPSIS</h2>
<p> fdesign [-xformoptions] [-options] [files]</p>
<h2>DESCRIPTION</h2>
<p> <i>fdesign</i> is a GUI builder that helps in the construction of graphical user interface in a WYSIWYG (&quot;what you see is what you get&quot;) way by allowing the user to directly manipulate various objects, such as buttons, sliders and menus etc. Once a satisfactory UI is constructed, the user can save the composed interface into a set of external files. Files with the extension &#8216;.fd&#8217; contain all information about the objects and can be read in again by <i>fdesign</i>. The files with C code and header files when compiled and linked against the <code>Forms Library</code>, generate code that at run-time constructs the exact same interface as the ones seen within <i>fdesign</i>. </p>
<p> A variety of output languages is possible via external filters. As of this writing, C, perl, ada95, Fortran, pascal, and PostScript output filters are known to exist. </p>
<h2>OPTIONS</h2>
<p> <i>fdesign</i> accepts all standard <code>Forms Library</code> command line options as well as the following:</p>
<dl>
<dt><code>-help</code></dt>
<dd> Prints a brief summary of all command line options. This option does not require a connection to the X server.</dd>
<dt><code>-version</code></dt>
<dd> Prints the current version of <i>fdesign</i> and exits.</dd>
<dt><code>-geometry</code><i> geom</i></dt>
<dd> Specifies the prefered size and location of main working area in which the UI is to be constructed.</dd>
<dt><code>-convert</code><i> fdfile-list</i></dt>
<dd> This option prevents <i>fdesign</i> from attempting to make a connection to the X server. The file list following this flag is converted to C code directly.</dd>
<dt><code>-dir</code><i> destdir</i></dt>
<dd> output any converted files in <i>destdir</i>.</dd>
<dt><code>-unit</code><i> pixel|point|mm|cp|cmm</i></dt>
<dd> selects the unit of measure for object geometries. For non-pixel unit, the interface created is screen resolution independent and may be desirable for many applications. Note that for typical screens, <i>point</i> (about 1/72 inch) and <i>mm</i> may be too coarse and subject to round-off errors. Use <i>cp</i> (centi-point, 100th of a point) and <i>cmm</i> (centi-mm) instead.</dd>
<dt><code>-altformat</code></dt>
<dd> selects an alternative format for the generated C code where global variables are used for the UI components.</dd>
<dt><code>-main</code></dt>
<dd> requests the output of main program template.</dd>
<dt><code>-callback</code></dt>
<dd> requests the output of callback function template.</dd>
<dt><code>-compensate</code></dt>
<dd> requests the emission of font/server resolution variation compensation code.</dd>
<dt><code>-I</code><i> headerfile</i></dt>
<dd> uses an alternative header file instead of the default forms.h in the output C code.</dd>
<dt><code>-lax</code></dt>
<dd> requests relaxed C syntax checking.</dd>
<dt><code>-ps</code></dt>
<dd> This option specifies that instead of emitting the c code for the user interface, PostScript code should be emitted.</dd>
<dt><code>-ada</code></dt>
<dd> This option requests ada95 code output</dd>
<dt><code>-perl</code></dt>
<dd> This option requests perl code output.</dd>
<dt><code>-fortran</code></dt>
<dd> This option requests Fortran code output.</dd>
<dt><code>-pascal</code></dt>
<dd> This option requests pascal code output.</dd>
<dt><code>-nocode</code></dt>
<dd> suppresses the output of UI code. Only the .fd file is written.</dd></dl>
<p> The most useful <code>Forms Library</code> command line options are</p>
<dl>
<dt><code>-display</code><i> host:dpy</i></dt>
<dd> This option specifies the X server to connect.</dd>
<dt><code>-flversion</code></dt>
<dd> This option prints the version string of the <code>Forms Library</code>, with which fdesign was build.</dd>
<dt><code>-name</code><i> appname</i></dt>
<dd> This option specifies the application name under which resources are to be obtained, instead of the executable name. <i>appname</i> should not contain . or *. <i>fdesign</i>.</dd></dl>
<h2>RESOURCES</h2>
<p> The program understands all of the <code>Forms Library</code>&#8216;s resource names and classes as well as the following</p>
<dl>
<dt>control.geometry (class Control.Geometry)</dt>
<dd> specifies the geometry of the control panel. Currently the size is ignored.</dd>
<dt>unit (Unit)</dt>
<dd> specifies the default unit of measure. Default is pixel. </dd>
<dt>attributes.geometry (class Attributes.Geometry)</dt>
<dd> specifies the geometry of the object attributes panel. Currently the size is ignored.</dd>
<dt>align.geometry (class Align.Geometry)</dt>
<dd> specifies the geometry of the object align panel. Currently the size is ignored.</dd>
<dt>xformsHeader (class XFormsHeader)</dt>
<dd> specifies the header filename generated in the output C code. Default is forms.h</dd>
<dt>filter (class Filter)</dt>
<dd> specifies post-processing filter (an external executable name).</dd>
<dt>language (class Language)</dt>
<dd> specifies target language name. </dd>
</dl>
<p> Among the standard <code>Forms Library</code> resources, the following are most useful</p>
<dl>
<dt>xform.fontsize (class XFORM.FontSize)</dt>
<dd> specifies the font size used for most object labels.</dd>
<dt>xform.pupfontsize (class XFORM.PupFontSize)</dt>
<dd> specifies the font size used in pop-up menus.</dd>
<dt>xform.browserFontSize (class XFORM.BrowserFontSize)</dt>
<dd> specifies the font size used for the text inside a browser. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-xforms/">xforms</a>(5), fd2ps(1L)</p>
<h2>AUTHOR</h2>
<p> Copyright (c) 1996-2002 T.C. Zhao &lt;tc_zhao [at] yahoo.com&gt; and Mark Overmars &lt;markov [at] cs.ruu.nl&gt;<br />
 Since 2002: GNU Lesser General Public License<br />
 Maintainers: Jean-Marc Lasgouttes, Angus Leeming and Jens Thoms Toerring &lt;jt [at] toerring.de&gt;</p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://xforms-toolkit.org">http://xforms-toolkit.org</a><br />
 <a rel="nofollow" href="http://savannah.nongnu.org/projects/xforms/">http://savannah.nongnu.org/projects/xforms/</a> </p>
