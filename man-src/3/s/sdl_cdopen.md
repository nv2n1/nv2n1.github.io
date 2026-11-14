---
title: "sdl_cdopen(3)"
name: "sdl_cdopen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_cdopen/"
description: "SDL_CDOpen – Opens a CD-ROM drive for access."
---

<p>SDL_CDOpen &#8211; Opens a CD-ROM drive for access.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_CD *SDL_CDOpen</code>(<code>int drive</code>);</p>
<h2>Description</h2>
<p>Opens a CD-ROM drive for access. It returns a <i></i><code>SDL_CD</code> structure on success, or <code>NULL</code> if the drive was invalid or busy. This newly opened CD-ROM becomes the default CD used when other CD functions are passed a <code>NULL</code> CD-ROM handle. </p>
<p> Drives are numbered starting with 0. Drive 0 is the system default CD-ROM.</p>
<h2>Examples</h2>
<pre><tt>SDL_CD *cdrom;
int cur_track;
int min, sec, frame;
SDL_Init(SDL_INIT_CDROM);
atexit(SDL_Quit);
/* Check for CD drives */
if(!SDL_CDNumDrives()){
 /* None found */
 fprintf(stderr, &quot;No CDROM devices available
&quot;);
 exit(-1);
}
/* Open the default drive */
cdrom=SDL_CDOpen(0);
/* Did if open? Check if cdrom is NULL */
if(!cdrom){
 fprintf(stderr, &quot;Couldn't open drive: %s
&quot;, SDL_GetError());
 exit(-1);
}
/* Print Volume info */
printf(&quot;Name: %s
&quot;, SDL_CDName(0));
printf(&quot;Tracks: %d
&quot;, cdrom-&gt;numtracks);
for(cur_track=0;cur_track &lt; cdrom-&gt;numtracks; cur_track++){
 FRAMES_TO_MSF(cdrom-&gt;track[cur_track].length, &amp;min, &amp;sec, &amp;frame);
 printf(&quot; Track %d: Length %d:%d
&quot;, cur_track, min, sec);
}
SDL_CDClose(cdrom);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CD</code>, <i></i><code>SDL_CDtrack</code>, <i></i><code>SDL_CDClose</code></p>
