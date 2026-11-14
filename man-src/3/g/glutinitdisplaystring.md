---
title: "glutinitdisplaystring(3)"
name: "glutinitdisplaystring"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutinitdisplaystring/"
description: "glutInitDisplayString – Set the window creation display mode."
---

<p><code>glutInitDisplayString</code> &#8211; Set the window creation display mode.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutInitDisplayString const char *displayMode</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>displayMode Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Requested display mode string.</p>
<h2>Description</h2>
<p>glutInitDisplayString() permits you to define a display mode for subsequent windows that you open. In most regards, control is at least as fine as with glutInitDisplaymode(). </p>
<p> The Bf Sy<br />
&nbsp;<wbr>displayMode Ef<br />
&nbsp;<wbr>parameter is case-sensitive, and tokens are separated by ASCII TABs (	) and SPACEs. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>index Ef<br />
&nbsp;<wbr><br />
 Enables Bf Sy<br />
&nbsp;<wbr>GLUT_INDEX. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>luminance Ef<br />
&nbsp;<wbr><br />
 Enables Bf Sy<br />
&nbsp;<wbr>GLUT_LUMINANCE. Ef<br />
&nbsp;<wbr> Enables Bf Sy<br />
&nbsp;<wbr>GLUT_STENCIL. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>red Ef<br />
&nbsp;<wbr><br />
 Number of red channel bits. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>green Ef<br />
&nbsp;<wbr><br />
 Number of green channel bits. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>blue Ef<br />
&nbsp;<wbr><br />
 Number of blue channel bits. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>alpha Ef<br />
&nbsp;<wbr><br />
 Number of alpha channel bits. Enables Bf Sy<br />
&nbsp;<wbr>GLUT_ALPHA. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>rgb Ef<br />
&nbsp;<wbr><br />
 Number of Bf Sy<br />
&nbsp;<wbr>RGB Ef<br />
&nbsp;<wbr>channel bits, no aplha bits. Enables Bf Sy<br />
&nbsp;<wbr>GLUT_RGB. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>rgba Ef<br />
&nbsp;<wbr><br />
 Number of Bf Sy<br />
&nbsp;<wbr>RGBA Ef<br />
&nbsp;<wbr>channel bits. Enables Bf Sy<br />
&nbsp;<wbr>GLUT_RGBA. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>depth Ef<br />
&nbsp;<wbr><br />
 Number of depth buffer bits. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>stencil Ef<br />
&nbsp;<wbr><br />
 Number of stencil buffer bits. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>double Ef<br />
&nbsp;<wbr><br />
 Enables Bf Sy<br />
&nbsp;<wbr>GLUT_DOUBLE. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>single Ef<br />
&nbsp;<wbr><br />
 Enables Bf Sy<br />
&nbsp;<wbr>GLUT_SINGLE. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>stereo Ef<br />
&nbsp;<wbr><br />
 Enables Bf Sy<br />
&nbsp;<wbr>GLUT_STERO. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>acca Ef<br />
&nbsp;<wbr><br />
 Number of Bf Sy<br />
&nbsp;<wbr>RGBA Ef<br />
&nbsp;<wbr>accumulation bits. Enables Bf Sy<br />
&nbsp;<wbr>GLUT_ACCUM. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>acc Ef<br />
&nbsp;<wbr><br />
 Number of Bf Sy<br />
&nbsp;<wbr>RGB Ef<br />
&nbsp;<wbr>accumulation bits. Enables Bf Sy<br />
&nbsp;<wbr>GLUT_ACCUM. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>samples Ef<br />
&nbsp;<wbr><br />
 Number of samples for GLX&#8217;s Bf Sy<br />
&nbsp;<wbr>SGIS_Multisample. Ef<br />
&nbsp;<wbr> Enables Bf Sy<br />
&nbsp;<wbr>GLUT_MULTISAMPLE. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>buffer Ef<br />
&nbsp;<wbr><br />
 [TODO] Sets bits in index mode? </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>conformant Ef<br />
&nbsp;<wbr><br />
 [TODO] Conformant with what? Enables Bf Sy<br />
&nbsp;<wbr>GLUT_DEPTH. Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>slow Ef<br />
&nbsp;<wbr><br />
 [TODO] Indicates if a frame-buffer is slow. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>num Ef<br />
&nbsp;<wbr><br />
 [TODO] Appears to select a frame-buffer configuration by number from an unspecified list. Probably very non-portable. </p>
<p> A special capability name indicating where the value represents the Nth frame buffer configuration matching the description string </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>win32pdf Ef<br />
&nbsp;<wbr><br />
 Win32 specific: Pixel Format Descriptor </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>win32pfd Ef<br />
&nbsp;<wbr><br />
 Win32 specific: Pixel Format Descriptor </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>xvisual Ef<br />
&nbsp;<wbr><br />
 X11 specific: X Visual </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>xstaticgray Ef<br />
&nbsp;<wbr><br />
 X11 specific: &quot;staticgray&quot; mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>xgrayscale Ef<br />
&nbsp;<wbr><br />
 X11 specific: &quot;grayscale&quot; mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>xstaticcolor Ef<br />
&nbsp;<wbr><br />
 X11 specific: &quot;staticcolor&quot; mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>xpseudocolor Ef<br />
&nbsp;<wbr><br />
 X11 specific: &quot;pseudocolor&quot; mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>xtruecolor Ef<br />
&nbsp;<wbr><br />
 X11 specific: &quot;trueolor&quot; mode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>xdirectcolor Ef<br />
&nbsp;<wbr><br />
 X11 specific: &quot;directcolor&quot; mode. </p>
<h2>Caveats</h2>
<p>Conflicting modes, such as Bf Sy<br />
&nbsp;<wbr>single Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>double Ef<br />
&nbsp;<wbr>have the same interaction as for glutInitDisplayMode(). </p>
<h2>Todo</h2>
<p>Bf Sy<br />
&nbsp;<wbr>GLUT_BORDERLESS Ef<br />
&nbsp;<wbr>and&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_OFFSCREEN Ef<br />
&nbsp;<wbr>are not represented. </p>
<p> Not all features appear to be implemented. In particular, numeric parameters and comparator specifications are lacking. See GLUT 3.7 sources for example. </p>
<p> PyOpenGL &lt;a href=&quot;<a rel="nofollow" href="http://pyopengl.sourceforge.net/documentation/manual/glutInitDisplayString.3GLUT.html">http://pyopengl.sourceforge.net/documentation/manual/glutInitDisplayString.3GLUT.html</a>&quot;&gt; glutInitDisplayString&lt;/a&gt; documentation. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutinit/">glutInit</a>(3) <a href="/docs/linux/man/3-glutinitwindowposition/">glutInitWindowPosition</a>(3) <a href="/docs/linux/man/3-glutinitwindowsize/">glutInitWindowSize</a>(3) <a href="/docs/linux/man/3-glutinitdisplaymode/">glutInitDisplayMode</a>(3)</p>
