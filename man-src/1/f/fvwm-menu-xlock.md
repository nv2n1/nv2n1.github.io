---
title: "fvwm-menu-xlock(1)"
name: "fvwm-menu-xlock"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-menu-xlock/"
description: "fvwm-menu-xlock – builds xlock menu definition for fvwm"
---

<h2 class="name">NAME</h2>
<p> fvwm-menu-xlock &#8211; builds xlock menu definition for fvwm </p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-menu-xlock</code> [ <code>&#8211;help</code>|<code>-h</code>|<code>-?</code> ] [ <code>&#8211;version</code>|<code>-V</code> ] [ <code>&#8211;name</code>|<code>-n</code> name ] [ <code>&#8211;title</code>|<code>-t</code> title ] [ <code>&#8211;item</code> format ] [ <code>&#8211;icon-title</code> icon ] [ <code>&#8211;icon-item</code> icon ] [ <code>&#8211;special-first</code>|<code>-s</code> ] [ &#8212; xlock params ]</p>
<h2>DESCRIPTION</h2>
<p> A simple perl script which parses xlock&#8217;s output to build an fvwm menu definition of all xlock&#8217;s modes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> show the help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> show the version and exit</p>
<dt><code>&#8211;name</code> name</p>
<dd> define menu name in the following argument. Default is &#8220;XLockMenu&#8221;</p>
<dt><code>&#8211;title</code> title</p>
<dd> define menu title in the following argument. Default is &#8220;XLock Modes&#8221;.</p>
<dt><code>&#8211;item</code> format</p>
<dd> define menu item format in the following argument, default is &#8216;%n	(%d)&#8217;. <font SIZE="-1">TAB</font> can be specified as &#8216;	&#8217;, but in .fvwm2rc you should specify a double backslash or a real <font SIZE="-1">TAB</font>. </p>
<p> Format specifiers: </p>
<pre>
  %n - mode name
  %d - mode description
  %D - mode description without &quot;Shows &quot; prefix if any
</pre>
<p> These specifiers can receive an optional integer size, positive for right adjusted string or negative for left adjusted, example: <tt>%8x</tt>; and optional *num or *-num, which means to leave only the first or last (if minus) num of chars, the num must be greater than 3, since the striped part is replaced with &#8220;&#8230;&#8221;, example: %*30x. Both can be combined: %-10*-20x, this instructs to get only the 20 last characters, but if the length is less then 10 &#8211; to fill with up to 10 spaces on the right.</p>
<dt><code>&#8211;icon-title</code> icon</p>
<dd>
<dt><code>&#8211;icon-item</code> icon</p>
<dd> define menu icon for title and regular item accordingly. Default is no menu icons (equivalent to an empty icon argument).</p>
<dt><code>&#8211;wm-icons</code></p>
<dd> define icon names suitable for use with wm-icons package. Currently this is equivalent to: &#8211;icon-title &#8221; &#8211;icon-item menu/lock.xpm.</p>
<dt><code>&#8211;special-first</code></p>
<dd> instructs to include special modes (usually black, bomb and random) first.</dl>
<p> Option parameters can be specified either using &#8216;=&#8217; or in the next argument. Short options are ok if not ambiguous: -h, -t; but be careful with short options, what is now unambiguous, can became ambiguous in the next versions. </p>
<p> Additional arguments (after <code>&#8212;</code>) will be passed to xlock. </p>
<p> Please see the <code><a href="/docs/linux/man/1-xlock/">xlock</a></code>(1) man page for the xlock options.</p>
<h2>USAGE</h2>
<p> Add these lines to your fvwm configuration file: </p>
<pre><code>
PipeRead 'fvwm-menu-xlock --name MenuSSaver --title "Screensaver" \
    --icon-item mini-bball.xpm --special-first -- -nice 19 -nolock' PipeRead 'fvwm-menu-xlock --name MenuSLock --title "Lock Screen" \
    --icon-item mini-rball.xpm --special-first -- -nice 19' AddToMenu "Utilities"
                                                                      "Screensaver%mini-monitor.xpm%" Popup MenuSSaver
                                                                          AddToMenu "Utilities"
                                                                      "Screenlock%mini-lock.xpm%" Popup MenuSLock
</code></pre>
<h2>AUTHORS</h2>
<p> Charles K. Hines &lt;chuck_hines [at] vnet.ibm.com&gt;, initial version. </p>
<p> Mikhael Goikhman &lt;migo [at] homemail.com&gt;, from 24 Feb 1999.</p>
<h2>COPYING</h2>
<p> The script is distributed by the same terms as fvwm itself. See <font SIZE="-1">GNU</font> General Public License for details.</p>
<h2>BUGS</h2>
<p> Depends on the output of xlock. Will produce an empty menu if the structure of the output is changed. </p>
<p> Report bugs to fvwm-bug [at] fvwm.org. </p>
<h2>Index</h2>
