---
title: "sdl_joystickgetball(3)"
name: "sdl_joystickgetball"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickgetball/"
description: "SDL_JoystickGetBall – Get relative trackball motion"
---

<p>SDL_JoystickGetBall &#8211; Get relative trackball motion</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_JoystickGetBall</code>(<code>SDL_Joystick *joystick, int ball, int *dx, int *dy</code>);</p>
<h2>Description</h2>
<p>Get the <code>ball</code> axis change. </p>
<p> Trackballs can only return relative motion since the last call to <code>SDL_JoystickGetBall</code>, these motion deltas a placed into <code>dx</code> and <code>dy</code>.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> on success or <code>-1</code> on failure</p>
<h2>Examples</h2>
<pre><tt>int delta_x, delta_y;
SDL_Joystick *joy;
.
.
.
SDL_JoystickUpdate();
if(SDL_JoystickGetBall(joy, 0, &amp;delta_x, &amp;delta_y)==-1)
 printf(&quot;TrackBall Read Error!
&quot;);
printf(&quot;Trackball Delta- X:%d, Y:%d
&quot;, delta_x, delta_y);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickNumBalls</code></p>
