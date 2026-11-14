---
title: "conspy(1)"
name: "conspy"
section: "1"
letter: "c"
url: "/docs/linux/man/1-conspy/"
description: "conspy – virtual console spy tool"
---

<h2>NAME</h2>
<p> conspy &#8211; virtual console spy tool</p>
<h2>SYNOPSIS</h2>
<p> <code>conspy</code> [ options ] [ <i>console</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Conspy</i> allows the user to take control of a Linux virtual console. The user can see what is displayed on the console and their keystrokes are sent to it. </p>
<p> To exit from <i>conspy</i> press the escape key three times in quick succession. </p>
<h2>COMMAND LINE</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the program&#8217;s version and exit.</p>
<dt><code>-v</code>, <code>&#8211;viewonly</code></p>
<dd> Don&#8217;t send keystrokes to the virtual console.</p>
<dt><i>console</i></p>
<dd> If supplied, <i>console</i> must be a number in the range 1 .. 63, corresponding to the virtual console device /dev/tty1 .. /dev/tty63. If not supplied the currently active virtual console is opened and tracked.</dl>
<h2>LIMITATIONS</h2>
<p> <i>Conspy</i> will not pass keystrokes to a virtual console whose keyboard is configured to send scan codes. X configures its keyboard like this. If the terminal does not have at least 64 colours no colour will be displayed. <i>Conspy</i> ignores the mouse. <i>Conspy</i> may display some non-ASCII characters incorrectly. <i>Conspy</i> does not handle displays larger than 16000 characters (eg 200 rows x 80 columns). </p>
<p> <i>Conspy</i> depends on terminfo and curses working correctly for your terminal, and sometimes they don&#8217;t. Konsole is/was one example of where they don&#8217;t. Typing control-L will redraw the screen, which usually fixes the mess created. It also sends a control-L to the virtual console, of course.</p>
<h2>FILES</h2>
<dl>
<dt><code>/dev/ttyX</code>, <code>/dev/vc/X</code></p>
<dd> The characters typed are sent to this device. The latter is for devfs. It is only used if the former does not exist.</p>
<dt><code>/dev/vcsaX</code>, <code>/dev/vcc/aX</code></p>
<dd> The display of the virtual console is read from here. The latter is for devfs. It is only used if the former does not exist.</dl>
<h2>AUTHOR</h2>
<p> Russell Stuart, &lt;russell-conspy [at] stuart.id.au&gt;. </p>
<h2>Index</h2>
