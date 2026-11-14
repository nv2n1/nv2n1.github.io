---
title: "sdl_cdname(3)"
name: "sdl_cdname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_cdname/"
description: "SDL_CDName – Returns a human-readable, system-dependent identifier for the CD-ROM."
---

<p>SDL_CDName &#8211; Returns a human-readable, system-dependent identifier for the CD-ROM.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> const char *SDL_CDName</code>(<code>int drive</code>);</p>
<h2>Description</h2>
<p>Returns a human-readable, system-dependent identifier for the CD-ROM. <code>drive</code> is the index of the drive. Drive indices start to 0 and end at <code>SDL_CDNumDrives()</code>-1.</p>
<h2>Examples</h2>
<dl COMPACT>
<dt> &bull;</p>
<dd>&quot;/dev/cdrom&quot;</p>
<dt> &bull;</p>
<dd>&quot;E:&quot;</p>
<dt> &bull;</p>
<dd>&quot;/dev/disk/ide/1/master&quot;</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_CDNumDrives</code></p>
