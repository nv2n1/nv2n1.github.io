---
title: "glutentergamemode(3)"
name: "glutentergamemode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutentergamemode/"
description: "glutEnterGameMode – Enter game mode"
---

<p><code>glutEnterGameMode</code> &#8211; Enter game mode</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; gamemode</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft int Fn glutEnterGameMode void</p>
<h2>Description</h2>
<p>Any combination of the following may apply: </p>
<p>&nbsp;<wbr>&#8211; Resolution change, possibly to the requested resolution, possibly to a &quot;nearest match&quot;.<br />
&nbsp;<wbr>&#8211; Refresh frequency change.<br />
&nbsp;<wbr>&#8211; A window with a drawable area equal to the requested screen resolution will be opened.<br />
&nbsp;<wbr>&#8211; The mouse may be restricted to operate within your window. </p>
<h2>Caveats</h2>
<p>Varies in behavior; X users can disable the resolution change by an OpenGLUT compile-time option. </p>
<h2>Todo</h2>
<p>Documentation </p>
<p> OpenGLUT may be unable to restore the original settings (this has been observed on WIN32). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutgamemodestring/">glutGameModeString</a>(3) <a href="/docs/linux/man/3-glutentergamemode/">glutEnterGameMode</a>(3) <a href="/docs/linux/man/3-glutleavegamemode/">glutLeaveGameMode</a>(3) <a href="/docs/linux/man/3-glutgamemodeget/">glutGameModeGet</a>(3)</p>
