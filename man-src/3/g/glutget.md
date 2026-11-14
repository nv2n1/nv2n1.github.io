---
title: "glutget(3)"
name: "glutget"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutget/"
description: "glutGet – Allows you to query some general state/option variables."
---

<p><code>glutGet</code> &#8211; Allows you to query some general state/option variables.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; state</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutGet GLenum eWhat</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>eWhat Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Enumerated parameter ID.</p>
<h2>Description</h2>
<p>This function permits you to query for the current value of many different OpenGLUT state variables. The current list is: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ACTION_ON_WINDOW_CLOSE Ef<br />
&nbsp;<wbr><br />
 Allows you to do something other than die if the user closes one of your windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_DISPLAY_MODE_POSSIBLE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_ELAPSED_TIME Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_DISPLAY_MODE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_STATE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_HEIGHT Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_WIDTH Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_X Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_INIT_WINDOW_Y Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_MENU_NUM_ITEMS Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_RENDERING_CONTEXT Ef<br />
&nbsp;<wbr><br />
 Allows you to specify context-sharing when you open new windows. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_SCREEN_HEIGHT Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_SCREEN_HEIGHT_MM Ef<br />
&nbsp;<wbr><br />
 Height in millimeters. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_SCREEN_WIDTH Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_SCREEN_WIDTH_MM Ef<br />
&nbsp;<wbr><br />
 Width in millimeters. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_VERSION Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_ACCUM_ALPHA_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_ACCUM_BLUE_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_ACCUM_GREEN_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_ACCUM_RED_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_ALPHA_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_BLUE_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_BORDER_WIDTH Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_BUFFER_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_COLORMAP_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_CURSOR Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_DEPTH_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_DOUBLEBUFFER Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_FORMAT_ID Ef<br />
&nbsp;<wbr><br />
 System dependant. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_GREEN_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_HEADER_HEIGHT Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_HEIGHT Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_NUM_CHILDREN Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_NUM_SAMPLES Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_PARENT Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_RED_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_RGBA Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_STENCIL_SIZE Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_STEREO Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_WIDTH Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_X Ef<br />
&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_WINDOW_Y Ef<br />
&nbsp;<wbr> </p>
<p> Most of the above are very obvious, and so full documentation is postponed for now. </p>
<h2>Todo</h2>
<p>Go back and flesh out the above list. </p>
<p> This function is a bit messy, especially the WINCE part. Fix. </p>
<p> Lots of code uses return to hop out. Since it&#8217;s such a sprawling function, it&#8217;s easy to be in the middle and not be 100% sure if there&#8217;s anything important at the end of the function, or if it is safe to just &quot;drop out&quot; of the current case and head for the bottom. </p>
<p> Causes crashes (assertion failure) if you call this before having called glutInit()&#8212;other than GLUT_INIT_STATE and GLUT_ELAPSED_TIME. Because various things can cause OpenGLUT to become deinitialized, we should probably either return default values of some kind or do minimal initialization if we are called without proper initialization. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetoption/">glutSetOption</a>(3) <a href="/docs/linux/man/3-glutdeviceget/">glutDeviceGet</a>(3) <a href="/docs/linux/man/3-glutgetmodifiers/">glutGetModifiers</a>(3) <a href="/docs/linux/man/3-glutlayerget/">glutLayerGet</a>(3)</p>
