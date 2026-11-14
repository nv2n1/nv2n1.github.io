---
title: "set_display_switch_mode(3)"
name: "set_display_switch_mode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_display_switch_mode/"
description: "set_display_switch_mode – Tells Allegro how the program handles background switching."
---

<p>set_display_switch_mode &#8211; Tells Allegro how the program handles background switching.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int set_display_switch_mode(int mode);</code></pre>
<h2>Description</h2>
<p>Sets how the program should handle being switched into the background, if the user tabs away from it. Not all of the possible modes will be supported by every graphics driver on every platform. The available modes are: </p>
<p> SWITCH_NONE </p>
<p> Disables switching. This is the default in single-tasking systems like DOS. It may be supported on other platforms, but you should use it with caution, because your users won&#8217;t be impressed if they want to switch away from your program, but you don&#8217;t let them! </p>
<p> SWITCH_PAUSE </p>
<p> Pauses the program whenever it is in the background. Execution will be resumed as soon as the user switches back to it. This is the default in most fullscreen multitasking environments, for example the Linux console, but not under Windows. </p>
<p> SWITCH_AMNESIA </p>
<p> Like SWITCH_PAUSE, but this mode doesn&#8217;t bother to remember the contents of video memory, so the screen, and any video bitmaps that you have created, will be erased after the user switches away and then back to your program. This is not a terribly useful mode to have, but it is the default for the fullscreen drivers under Windows because DirectDraw is too dumb to implement anything better. </p>
<p> SWITCH_BACKGROUND </p>
<p> The program will carry on running in the background, with the screen bitmap temporarily being pointed at a memory buffer for the fullscreen drivers. You must take special care when using this mode, because bad things will happen if the screen bitmap gets changed around when your program isn&#8217;t expecting it (see below). </p>
<p> SWITCH_BACKAMNESIA </p>
<p> Like SWITCH_BACKGROUND, but this mode doesn&#8217;t bother to remember the contents of video memory (see SWITCH_AMNESIA). It is again the only mode supported by the fullscreen drivers under Windows that lets the program keep running in the background. </p>
<p> Note that you should be very careful when you are using graphics routines in the switching context: you must always call acquire_screen() before the start of any drawing code onto the screen and not release it until you are completely finished, because the automatic locking mechanism may not be good enough to work when the program runs in the background or has just been raised in the foreground.</p>
<h2>Return Value</h2>
<p>Returns zero on success, invalidating at the same time all callbacks previously registered with set_display_switch_callback(). Returns -1 if the requested mode is not currently possible. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_display_switch_callback/">set_display_switch_callback</a></code>(3), <code><a href="/docs/linux/man/3-get_display_switch_mode/">get_display_switch_mode</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3) </p>
