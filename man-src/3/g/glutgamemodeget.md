---
title: "glutgamemodeget(3)"
name: "glutgamemodeget"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutgamemodeget/"
description: "glutGameModeGet – Return the value of a game mode parameter"
---

<p><code>glutGameModeGet</code> &#8211; Return the value of a game mode parameter</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; gamemode</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutGameModeGet GLenum pname</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>pname Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The parameter value to be returned</p>
<h2>Description</h2>
<p>Bf Sy<br />
&nbsp;<wbr>pname Ef<br />
&nbsp;<wbr>is one of: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_ACTIVE Ef<br />
&nbsp;<wbr><br />
 Return non-zero if we are presently in gamemode. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_POSSIBLE Ef<br />
&nbsp;<wbr><br />
 Return whether the requested gamemode settings are viable. (May also actually change the mode?) Does not necessarily tell you whether entering gamemode will have any effect. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_WIDTH Ef<br />
&nbsp;<wbr><br />
 Return the game mode width. (in pixels) </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_HEIGHT Ef<br />
&nbsp;<wbr><br />
 Return the game mode height. (in pixels) </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_PIXEL_DEPTH Ef<br />
&nbsp;<wbr><br />
 Return the game mode pixel depth. (in bits) </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_REFRESH_RATE Ef<br />
&nbsp;<wbr><br />
 Return the game mode vertical refresh frequency. (in Hz) </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr> Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_DISPLAY_CHANGED Ef<br />
&nbsp;<wbr><br />
 Return non-zero if we are presently in gamemode. (Same as Bf Sy<br />
&nbsp;<wbr>GLUT_GAME_MODE_ACTIVE.) Ef<br />
&nbsp;<wbr> </p>
<p> If Bf Sy<br />
&nbsp;<wbr>pname Ef<br />
&nbsp;<wbr>is unknown, a warning is printed and a value of<br />
&nbsp;<wbr>-1 is returned. </p>
<h2>Todo</h2>
<p>Documentation </p>
<p> OpenGLUT intrepretation of GLUT_GAME_MODE_DISPLAY_CHANGED </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutgamemodestring/">glutGameModeString</a>(3) <a href="/docs/linux/man/3-glutentergamemode/">glutEnterGameMode</a>(3) <a href="/docs/linux/man/3-glutleavegamemode/">glutLeaveGameMode</a>(3) <a href="/docs/linux/man/3-glutgamemodeget/">glutGameModeGet</a>(3)</p>
