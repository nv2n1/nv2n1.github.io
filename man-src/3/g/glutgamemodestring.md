---
title: "glutgamemodestring(3)"
name: "glutgamemodestring"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutgamemodestring/"
description: "glutGameModeString – Set the game mode display string"
---

<p><code>glutGameModeString</code> &#8211; Set the game mode display string</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; gamemode</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutGameModeString const char *string</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>string Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A configuration parameter as a string.</p>
<h2>Description</h2>
<p>Sets the gamemode status according to an undocumented string. </p>
<p> Glancing at old GLUT 3.7, the freeglut codebase that we inherited does not implement more than a single GLUT gamemode &#8220;criteria&#8221;. It may not even do that much correctly. </p>
<p> In principle, this code lets you set the video dimensions, rendering depth, and video refresh rate. In practice, the combination that you request may be unsupportable and the target host may even refuse to honor any such changes. </p>
<p> If you use this function but do not set all options, the following defaults may be substituted for some values: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>width Ef<br />
&nbsp;<wbr>640<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>height Ef<br />
&nbsp;<wbr>480<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>depth Ef<br />
&nbsp;<wbr>16<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>refresh Ef<br />
&nbsp;<wbr>72 </p>
<h2>Todo</h2>
<p>Documentation </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutgamemodestring/">glutGameModeString</a>(3) <a href="/docs/linux/man/3-glutentergamemode/">glutEnterGameMode</a>(3) <a href="/docs/linux/man/3-glutleavegamemode/">glutLeaveGameMode</a>(3) <a href="/docs/linux/man/3-glutgamemodeget/">glutGameModeGet</a>(3)</p>
