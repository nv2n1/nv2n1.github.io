---
title: "xbindkeys(1)"
name: "xbindkeys"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xbindkeys/"
description: "xbindkeys – a grabbing keys program for X"
---

<h2 class="name">NAME</h2>
<p> xbindkeys &#8211; a grabbing keys program for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xbindkeys</code> [ <i>options</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>XbindKeys</i> is a program that grab keys and mouse button events in X and starts associated shell command. </p>
<h2>COMMAND LINE OPTIONS</h2>
<p> Available command line options are as follows:</p>
<dl>
<dt><code>-d, &#8211;defaults</code></p>
<dd> Print a default rc file</p>
<dt><code>-f, &#8211;file</code></p>
<dd> Use an alternative rc file</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Short help on options plus version/author info.</p>
<dt><code>-X, &#8211;display</code></p>
<dd> Set X display to use</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> More information on xbindkeys when it run </p>
<dt><code>-k, &#8211;key</code></p>
<dd> Identify one key pressed (useful to fill the configuration file) </p>
<dt><code>-mk, &#8211;multikey</code></p>
<dd> Identify multi key pressed (useful to fill the configuration file) </p>
<dt><code>-g, &#8211;geometry</code></p>
<dd> size and position of window with -k|-mk option </p>
<dt><code>-n, &#8211;nodaemon</code></p>
<dd> don&#8217;t start as daemon </p>
</dl>
<p> If guile support have not been disabled:</p>
<dl>
<dt><code>-dg, &#8211;defaults-guile</code></p>
<dd> Print a default guile configuration file </p>
<dt><code>-fg, &#8211;file-guile</code></p>
<dd> Use an alternative guile configuration file </p>
</dl>
<h2>XBINDKEYSRC</h2>
<p> XBindKeys uses a configuration files. This file is $HOME/.xbindkeysrc, used only for one user. All whitespace is ignored in the files except for within the commands names double quotes. </p>
<p> The configuration file consists of commands names in double quotes, and associated keys in the next line. </p>
<p> Comments are started with a pound (#) and extend to the end of the line. </p>
<p> You can see a default file with the &#8211;defaults option or create a default $HOME/.xbindkeysrc with </p>
<pre>
 'xbindkeys --defaults &gt; $HOME/.xbindkeysrc'.
</pre>
<h2>KEYSYMS</h2>
<p> The program expects combinations of keysyms to be used by using plus(+) characters to combine them together. </p>
<p> The format of a command line is: </p>
<pre>
    &quot;command to start &amp;&quot;
       associated key
</pre>
<p> To specify an associated key, you can use &#8216;xbindkeys &#8211;key&#8217; or<br />
&nbsp;<wbr>&#8216;xbindkeys &#8211;multikey&#8217;&nbsp;<wbr>and put one of the two lines in the&nbsp;<wbr> configuration file. </p>
<p> A list of keys is in /usr/include/X11/keysym.h and in /usr/include/X11/keysymdef.h. The XK_ is not needed. </p>
<p> List of modifiers: </p>
<pre>
    Release, Control, Shift, Mod1 (Alt), Mod2 (NumLock),
    Mod3 (CapsLock), Mod4, Mod5 (Scroll).
</pre>
<p> The release modifier is not a standard X modifier, but you can use it if you want to catch release events instead of press events. </p>
<p> By defaults, xbindkeys does not pay attention with the modifiers NumLock, CapsLock and ScrollLock. Add the lines above in the configuration file, if you want to pay attention to them. </p>
<p>&nbsp;<wbr>keystate_numlock&nbsp;<wbr>=&nbsp;<wbr>enable </p>
<pre>
    keystate_capslock = enable
    keystate_scrolllock= enable
</pre>
<h2>EXAMPLES</h2>
<p> # control+shift+d starts an xterm (it&#8217;s a comment) </p>
<pre>
&quot;xterm&quot; 
  control+shift + q
# Menu key starts xbindkeys_show
&quot;xbindkeys_show&quot;
  Menu
# Control + mouse button 1 starts an xterm
&quot;xterm&quot;
  Control + b:1
# Control+Shift+a  release event starts rxvt
&quot;rxvt&quot;
  release+control+shift + a
# Control + mouse button 2 release event starts rxvt
&quot;rxvt&quot;
  Control + b:2 + Release
</pre>
<h2>SCHEME CONFIGURATION STYLE</h2>
<p> If the guile support have not been disabled, you can use an alternate configuration file written in scheme. xbindkeys read first the scheme configuration file, and if this file doesn&#8217;t exist, it read the standard configuration file. </p>
<p> For more details, please see here </p>
<pre><code>
  http://www.gnu.org/software/guile/guile.html
Note: The guile configuration file is the prefered way if you have a non trivial
configuration like for example double click, timed click or keys combinations.
The defaults is ~/.xbindkeysrc.scm
Use xbindkeys --defaults-guile for more details.
And xbindkeys --defaults-guile &gt; ~/.xbindkeysrc.scm to use this method.
</code></pre>
<h2>NOTE</h2>
<p> xbindkeys reload its configuration file each time it has changed. But if you want to force it reloading its configuration file, you can send a HUP signal: </p>
<p> killall -HUP xbindkeys </p>
<p> When HUP signal is send to xbindkeys, changes in $HOME/.xbindkeysrc takes effect only after moving mouse. </p>
<h2>BUGS</h2>
<p> If you find a bug, please send a mail to &lt;hocwp [at] free.fr&gt; </p>
<h2>HOMEPAGE</h2>
<pre>
<a rel="nofollow" href="http://hocwp.free.fr/xbindkeys">http://hocwp.free.fr/xbindkeys</a>
</pre>
<h2>AUTHOR</h2>
<p> Philippe Brochard &lt;hocwp [at] free.fr&gt; </p>
<pre>
Marcello Mathias Herreshoff for the guile support &lt;marcello [at] hummer.stanford.edu&gt;
</pre>
<h2>FILES</h2>
<pre>
$HOME/.xbindkeysrc
        The users configuration file.
$HOME/.xbindkeysrc.scm
        The users configuration file in scheme style (if guile support have not been disabled).
</pre>
<h2>SEE ALSO</h2>
<pre>
<code>xbindkeys_show</code>
    Utility for showing the actual keybinding with xbindkeys
<code><a href="//www.systutorials.com/docs/linux/man/1x-xmodmap/">xmodmap</a>(1x)</code>
    Utility for modifying keymap &amp; button mappings in X.
<code><a href="//www.systutorials.com/docs/linux/man/1x-xev/">xev</a>(1x)</code>
    Print contents of X events.
<code>/usr/include/X11/keysymdef.h</code>
    X11 KeySym definitions.
</pre>
<h2>Index</h2>
