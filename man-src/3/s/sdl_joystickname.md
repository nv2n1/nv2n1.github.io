---
title: "sdl_joystickname(3)"
name: "sdl_joystickname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joystickname/"
description: "SDL_JoystickName – Get joystick name."
---

<p>SDL_JoystickName &#8211; Get joystick name.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> const char *SDL_JoystickName</code>(<code>int index</code>);</p>
<h2>Description</h2>
<p>Get the implementation dependent name of joystick. The <code>index</code> parameter refers to the N&#8217;th joystick on the system.</p>
<h2>Return Value</h2>
<p>Returns a char pointer to the joystick name.</p>
<h2>Examples</h2>
<pre><tt>/* Print the names of all attached joysticks */
int num_joy, i;
num_joy=SDL_NumJoysticks();
printf(&quot;%d joysticks found
&quot;, num_joy);
for(i=0;i&lt;num_joy;i++)
 printf(&quot;%s
&quot;, SDL_JoystickName(i));</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_JoystickOpen</code></p>
