---
title: "glutseticontitle(3)"
name: "glutseticontitle"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutseticontitle/"
description: "glutSetIconTitle – Requests changing the iconified title of the current window"
---

<p><code>glutSetIconTitle</code> &#8211; Requests changing the iconified title of the current window</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; window</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSetIconTitle const char* title</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>title Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>New window title</p>
<h2>Description</h2>
<p>Requests that the window system change the title of the icon (or whatever) that is displayed when the Bf Li<br />
&nbsp;<wbr>current window Ef<br />
&nbsp;<wbr>&nbsp;<wbr>is in iconified mode. </p>
<p> As discussed under glutIconifyWindow(), most window systems allow a window to be placed in some kind of minimized, or iconified, state. In that state, the normal interior of the window is likely to be obscured, and the only clue about the window contents may be the window title. </p>
<h2>Caveats</h2>
<p>Effect is system-dependant. </p>
<p> There Exactly what &quot;iconified&quot; means is system dependant. Iconification may not be supported, or the title may not be available&#8212;or legible. Avoid putting essential information into the icon title. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutsetwindowtitle/">glutSetWindowTitle</a>(3) <a href="/docs/linux/man/3-gluticonifywindow/">glutIconifyWindow</a>(3)</p>
