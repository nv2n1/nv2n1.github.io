---
title: "sdl_keyboardevent(3)"
name: "sdl_keyboardevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_keyboardevent/"
description: "SDL_KeyboardEvent – Keyboard event structure"
---

<p>SDL_KeyboardEvent &#8211; Keyboard event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 Uint8 state;
 SDL_keysym keysym;
} SDL_KeyboardEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_KEYDOWN</code> or <code>SDL_KEYUP</code></p>
<dt><code>state</code></p>
<dd><code>SDL_PRESSED</code> or <code>SDL_RELEASED</code></p>
<dt><code>keysym</code></p>
<dd>Contains key press information</dl>
<h2>Description</h2>
<p><code>SDL_KeyboardEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_KEYDOWN</code> or <code>SDL_KEYUP</code> is reported. </p>
<p> The <code>type</code> and <code>state</code> actually report the same information, they just use different values to do it! A keyboard event occurs when a key is released (<code>type</code>=<code>SDK_KEYUP</code> or <code>state</code>=<code>SDL_RELEASED</code>) and when a key is pressed (<code>type</code>=<code>SDL_KEYDOWN</code> or <code>state</code>=<code>SDL_PRESSED</code>). The information on what key was pressed or released is in the <i></i><code>keysym</code> structure. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> Repeating SDL_KEYDOWN</code> events will occur if key repeat is enabled (see <i></i><code>SDL_EnableKeyRepeat</code>).</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_keysym</code>, <i></i><code>SDL_EnableKeyRepeat</code>, <i></i><code>SDL_EnableUNICODE</code></p>
