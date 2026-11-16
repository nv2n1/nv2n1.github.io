---
title: "sdl_joyhatevent(3)"
name: "sdl_joyhatevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_joyhatevent/"
description: "SDL_JoyHatEvent – Joystick hat position change event structure"
---

<p>SDL_JoyHatEvent &#8211; Joystick hat position change event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 Uint8 which;
 Uint8 hat;
 Uint8 value;
} SDL_JoyHatEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></dt>
<dd><code>SDL_JOY</code></dd>
<dt><code>which</code></dt>
<dd>Joystick device index</dd>
<dt><code>hat</code></dt>
<dd>Joystick hat index</dd>
<dt><code>value</code></dt>
<dd>Hat position</dd></dl>
<h2>Description</h2>
<p><code>SDL_JoyHatEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_JOYHATMOTION</code> is reported. </p>
<p> A <code>SDL_JOYHATMOTION</code> event occurs when ever a user moves a hat on the joystick. The field <code>which</code> is the index of the joystick that reported the event and <code>hat</code> is the index of the hat (for a more detailed exlaination see the <i>Joystick section</i>). <code>value</code> is the current position of the hat. It is a logically OR&#8217;d combination of the following values (whose meanings should be pretty obvious:) :</p>
<dl COMPACT>
<dd><code>SDL_HAT_CENTERED</code></dd>
<dd><code>SDL_HAT_UP</code></dd>
<dd><code>SDL_HAT_RIGHT</code></dd>
<dd><code>SDL_HAT_DOWN</code></dd>
<dd><code>SDL_HAT_LEFT</code></dd></dl>
<p> The following defines are also provided:</p>
<dl COMPACT>
<dd><code>SDL_HAT_RIGHTUP</code></dd>
<dd><code>SDL_HAT_RIGHTDOWN</code></dd>
<dd><code>SDL_HAT_LEFTUP</code></dd>
<dd><code>SDL_HAT_LEFTDOWN</code></dd></dl>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i>Joystick Functions</i>, <i></i><code>SDL_JoystickEventState</code>, <i></i><code>SDL_JoystickGetHat</code></p>
