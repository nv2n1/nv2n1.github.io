---
title: "sdl_joystickopen(3)"
name: "sdl_joystickopen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickopen/"
description: "SDL_JoystickOpen – Opens a joystick for use."
---

<p>SDL_JoystickOpen &#8211; Opens a joystick for use.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_Joystick *SDL_JoystickOpen</code>(<code>int index</code>);</p>
<h2>Description</h2>
<p>Opens a joystick for use within SDL. The <code>index</code> refers to the N&#8217;th joystick in the system. A joystick must be opened before it game be used.</p>
<h2>Return Value</h2>
<p>Returns a <code>SDL_Joystick</code> structure on success. <code>NULL</code> on failure.</p>
<h2>Examples</h2>
<pre><tt>SDL_Joystick *joy;
// Check for joystick
if(SDL_NumJoysticks()&gt;0){
 // Open joystick
 joy=SDL_JoystickOpen(0);
 
 if(joy)
 {
 printf(&quot;Opened Joystick 0
&quot;);
 printf(&quot;Name: %s
&quot;, SDL_JoystickName(0));
 printf(&quot;Number of Axes: %d
&quot;, SDL_JoystickNumAxes(joy));
 printf(&quot;Number of Buttons: %d
&quot;, SDL_JoystickNumButtons(joy));
 printf(&quot;Number of Balls: %d
&quot;, SDL_JoystickNumBalls(joy));
 }
 else
 printf(&quot;Couldn't open Joystick 0
&quot;);
 
 // Close if opened
 if(SDL_JoystickOpened(0))
 SDL_JoystickClose(joy);
}</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickClose</code></p>
