---
title: "sdl_event(3)"
name: "sdl_event"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_event/"
description: "SDL_Event – General event structure"
---

<p>SDL_Event &#8211; General event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef union{
 Uint8 type;
 SDL_ActiveEvent active;
 SDL_KeyboardEvent key;
 SDL_MouseMotionEvent motion;
 SDL_MouseButtonEvent button;
 SDL_JoyAxisEvent jaxis;
 SDL_JoyBallEvent jball;
 SDL_JoyHatEvent jhat;
 SDL_JoyButtonEvent jbutton;
 SDL_ResizeEvent resize;
 SDL_ExposeEvent expose;
 SDL_QuitEvent quit;
 SDL_UserEvent user;
 SDL_SysWMEvent syswm;
} SDL_Event;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></dt>
<dd>The type of event</dd>
<dt><code>active</code></dt>
<dd><i>Activation event</i></dd>
<dt><code>key</code></dt>
<dd><i>Keyboard event</i></dd>
<dt><code>motion</code></dt>
<dd><i>Mouse motion event</i></dd>
<dt><code>button</code></dt>
<dd><i>Mouse button event</i></dd>
<dt><code>jaxis</code></dt>
<dd><i>Joystick axis motion event</i></dd>
<dt><code>jball</code></dt>
<dd><i>Joystick trackball motion event</i></dd>
<dt><code>jhat</code></dt>
<dd><i>Joystick hat motion event</i></dd>
<dt><code>jbutton</code></dt>
<dd><i>Joystick button event</i></dd>
<dt><code>resize</code></dt>
<dd><i>Application window resize event</i></dd>
<dt><code>expose</code></dt>
<dd><i>Application window expose event</i></dd>
<dt><code>quit</code></dt>
<dd><i>Application quit request event</i></dd>
<dt><code>user</code></dt>
<dd><i>User defined event</i></dd>
<dt><code>syswm</code></dt>
<dd><i>Undefined window manager event</i></dd></dl>
<h2>Description</h2>
<p>The <code>SDL_Event</code> union is the core to all event handling is SDL, its probably the most important structure after <code>SDL_Surface</code>. <code>SDL_Event</code> is a union of all event structures used in SDL, using it is a simple matter of knowing which union member relates to which event <code>type</code>. </p>
<dl COMPACT>
<dt><code>Event type</code></dt>
<dd><code>Event Structure</code></dd>
<dt><code>SDL_ACTIVEEVENT</code></dt>
<dd><i></i><code>SDL_ActiveEvent</code></dd>
<dt><code>SDL_KEYDOWN/UP</code></dt>
<dd><i></i><code>SDL_KeyboardEvent</code></dd>
<dt><code>SDL_MOUSEMOTION</code></dt>
<dd><i></i><code>SDL_MouseMotionEvent</code></dd>
<dt><code>SDL_MOUSEBUTTONDOWN/UP</code></dt>
<dd><i></i><code>SDL_MouseButtonEvent</code></dd>
<dt><code>SDL_JOYAXISMOTION</code></dt>
<dd><i></i><code>SDL_JoyAxisEvent</code></dd>
<dt><code>SDL_JOYBALLMOTION</code></dt>
<dd><i></i><code>SDL_JoyBallEvent</code></dd>
<dt><code>SDL_JOYHATMOTION</code></dt>
<dd><i></i><code>SDL_JoyHatEvent</code></dd>
<dt><code>SDL_JOYBUTTONDOWN/UP</code></dt>
<dd><i></i><code>SDL_JoyButtonEvent</code></dd>
<dt><code>SDL_QUIT</code></dt>
<dd><i></i><code>SDL_QuitEvent</code></dd>
<dt><code>SDL_SYSWMEVENT</code></dt>
<dd><i></i><code>SDL_SysWMEvent</code></dd>
<dt><code>SDL_VIDEORESIZE</code></dt>
<dd><i></i><code>SDL_ResizeEvent</code></dd>
<dt><code>SDL_VIDEOEXPOSE</code></dt>
<dd><i></i><code>SDL_ExposeEvent</code></dd>
<dt><code>SDL_USEREVENT</code></dt>
<dd><i></i><code>SDL_UserEvent</code></dd></dl>
<h2>Use</h2>
<p>The <code>SDL_Event</code> structure has two uses</p>
<dl COMPACT>
<dt> &bull;</dt>
<dd>Reading events on the event queue</dd>
<dt> &bull;</dt>
<dd>Placing events on the event queue</dd></dl>
<p> Reading events from the event queue is done with either <i></i><code>SDL_PollEvent</code> or <i></i><code>SDL_PeepEvents</code>. We&#8217;ll use <code>SDL_PollEvent</code> and step through an example. </p>
<p> First off, we create an empty <code>SDL_Event</code> structure. </p>
<pre><tt>SDL_Event test_event;</tt></pre>
<p>&nbsp;<wbr><code>SDL_PollEvent</code>&nbsp;<wbr>removes the next event from the event queue, if there are no events on the queue it returns&nbsp;<wbr><code>0</code>&nbsp;<wbr>otherwise it returns&nbsp;<wbr><code>1</code>. We use a&nbsp;<wbr><code>while</code>&nbsp;<wbr>loop to process each event in turn.&nbsp;<wbr> </p>
<pre><tt>while(SDL_PollEvent(&amp;test_event)) {</tt></pre>
<p>&nbsp;<wbr>The&nbsp;<wbr><code>SDL_PollEvent</code>&nbsp;<wbr>function take a pointer to an&nbsp;<wbr><code>SDL_Event</code>&nbsp;<wbr>structure that is to be filled with event information. We know that if&nbsp;<wbr><code>SDL_PollEvent</code>&nbsp;<wbr>removes an event from the queue then the event information will be placed in our&nbsp;<wbr><code>test_event</code>&nbsp;<wbr>structure, but we also know that the&nbsp;<wbr><i>type</i>&nbsp;<wbr>of event will be placed in the&nbsp;<wbr><code>type</code>&nbsp;<wbr>member of&nbsp;<wbr><code>test_event</code>. So to handle each event&nbsp;<wbr><code>type</code>&nbsp;<wbr>seperately we use a&nbsp;<wbr><code>switch</code>&nbsp;<wbr>statement.&nbsp;<wbr> </p>
<pre><tt> switch(test_event.type) {</tt></pre>
<p>&nbsp;<wbr>We need to know what kind of events we&#8217;re looking for&nbsp;<wbr><i>and</i>&nbsp;<wbr>the event&nbsp;<wbr><code>type</code>&#8216;s of those events. So lets assume we want to detect where the user is moving the mouse pointer within our application. We look through our event types and notice that&nbsp;<wbr><code>SDL_MOUSEMOTION</code>&nbsp;<wbr>is, more than likely, the event we&#8217;re looking for. A little&nbsp;<wbr><i>more</i>&nbsp;<wbr>research tells use that&nbsp;<wbr><code>SDL_MOUSEMOTION</code>&nbsp;<wbr>events are handled within the&nbsp;<wbr><i></i><code>SDL_MouseMotionEvent</code>&nbsp;<wbr>structure which is the&nbsp;<wbr><code>motion</code>&nbsp;<wbr>member of&nbsp;<wbr><code>SDL_Event</code>. We can check for the&nbsp;<wbr><code>SDL_MOUSEMOTION</code>&nbsp;<wbr>event&nbsp;<wbr><code>type</code>&nbsp;<wbr>within our&nbsp;<wbr><code>switch</code>&nbsp;<wbr>statement like so:&nbsp;<wbr> </p>
<pre><tt> case SDL_MOUSEMOTION:</tt></pre>
<p>&nbsp;<wbr>All we need do now is read the information out of the&nbsp;<wbr><code>motion</code>&nbsp;<wbr>member of&nbsp;<wbr><code>test_event</code>.&nbsp;<wbr> </p>
<pre><tt> printf(&quot;We got a motion event.
&quot;);
 printf(&quot;Current mouse position is: (%d, %d)
&quot;, test_event.motion.x, test_event.motion.y);
 break;
 default:
 printf(&quot;Unhandled Event!
&quot;);
 break;
 }
}
printf(&quot;Event queue empty.
&quot;);</tt></pre>
<p>It is also possible to push events onto the event queue and so use it as a two-way communication path. Both <i></i><code>SDL_PushEvent</code> and <i></i><code>SDL_PeepEvents</code> allow you to place events onto the event queue. This is usually used to place a <code>SDL_USEREVENT</code> on the event queue, however you could use it to post fake input events if you wished. Creating your own events is a simple matter of choosing the event type you want, setting the <code>type</code> member and filling the appropriate member structure with information. </p>
<pre><tt>SDL_Event user_event;
user_event.type=SDL_USEREVENT;
user_event.user.code=2;
user_event.user.data1=NULL;
user_event.user.data2=NULL;
SDL_PushEvent(&amp;user_event);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_PollEvent</code>, <i></i><code>SDL_PushEvent</code>, <i></i><code>SDL_PeepEvents</code></p>
