---
title: "irxevent(1)"
name: "irxevent"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irxevent/"
description: "irxevent – infrared X-event sender"
---

<h2>NAME</h2>
<p> irxevent &#8211; infrared X-event sender</p>
<h2>SYNOPSIS</h2>
<p> <code>irxevent</code> [<i>option</i>]&#8230; [<i>config file</i>]</p>
<h2>DESCRIPTION</h2>
<p> Irxevent is a program that I wrote to send button clicks and key presses to X applications triggered by a LIRC driven remote control. You can control your favorite CD/MP3 player or your TV tuner program or any other X application that responds to keyboard or mouse input. If you like to you can send emacs ^X^S from your armchair. </p>
<p> Irxevent is a complement to irexec and irpty.</p>
<dl>
<dt><code>-d</code> <code>&#8211;daemon</code></p>
<dd> fork and run in background</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display usage summary</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> display version</dl>
<h2>FILES</h2>
<p> Irxevent works with the same config file as irexec and irpty (~/.lircrc). For a complete sample .lircrc look at examples/lircrc. </p>
<p> <code>Part of your .lircrc could look like this:</code> </p>
<pre>
<dl><dt><dd>begin
        prog = irxevent
        button = VIDEO_UP    
        config = Key SHIFT-KP_Add CurrentWindow
end
begin
        prog = irxevent
        button = VIDEO_DOWN
        config = Key SHIFT-KP_Subtract CurrentWindow
end
begin
        prog = irxevent
        button = STOP
        config = Key ctrl-c CurrentWindow
end
begin
        prog = irxevent
        button = 0
        config = Key f xawtv
        config = Key f xawtv
end
begin
        prog = irxevent
        button = POWER
        config = Key q xawtv
end
begin
        prog = irxevent
        button = CH_DOWN
        config = Button 1 329 92 kscd
end
begin
        prog = irxevent
        button = UP
        config = Button 1 110 80 GQmpeg
end
begin
        prog = irxevent
        button = DOWN
        config = Button 1 130 80 GQmpeg
end
</dl>
</pre>
<p> <code>Simply said </code><i>config</i><code> = lines may look like this:</code> </p>
<pre><code>
config = Key[shift - ][ctrl - ][alt - ]&lt;key&gt;[Focus]&lt;windowname&gt; | WindowID&lt;id&gt; | CurrentWindow | RootWindow config = Button&lt;button&gt;&lt;x&gt;&lt;y&gt;[Focus]&lt;windowname&gt; | WindowID&lt;id&gt; | CurrentWindow | RootWindow config = xy_Key&lt;x&gt;&lt;y&gt;[shift - ][ctrl - ][alt - ]&lt;key&gt;[Focus]&lt;windowname&gt; | WindowID id | CurrentWindow | RootWindow
</code></pre>
<p> <code>some more examples:</code> </p>
<pre>
<dl><dt><dd>config = Key Up xawtv
config = Key Down xawtv
config = Button 1 50 110 xclickme
config = Key q xawtv
config = Key ctrl-c mpg123
config = Key shift-Page_Up rxvt
</dl>
</pre>
<p> <code>In BNF this looks like:</code> </p>
<dl>
<dt>
<dd>
<pre><code>
LINE = "config =" &lt; KEY | BUTTON | XYKEY &gt; &lt;TARGET&gt; |
       "config =" &lt; KEY | BUTTON | XYKEY &gt; "Focus" &lt; TARGET &gt; XYKEY = "xy_Key" &lt; x_position &gt; &lt;y_position&gt;&lt;MOD&gt;&lt;KEYSPEC&gt;
                                                                                                  KEY = "Key" &lt; MOD &gt; &lt;KEYSPEC&gt;
                                                                                                                          MOD = ["shift-"]["numlock-"]["ctrl-"]["alt-"]["meta-"]
                                                                                                                                          ["numlock-"]["mod3-"]["mod4-"]["scrlock-"] KEYSPEC = Keyname | "KeySym:" KeySym | "KeyCode:" KeyCode BUTTON = "Button" &lt; 1..5 &gt; &lt;x_position&gt;&lt;y_position&gt;
                                                                                                                                                                                                                                                                              TARGET = Windowname | "WindowID" id | "CurrentWindow" | "RootWindow"
</code></pre>
<p> <i>Keyname:</i></p>
<dl>
<dt>
<dd> is the key symbol that is declared in X windows. E.g. &quot;Up&quot; refers to the cursor arrow pointing up. &quot;KP_Add&quot; is the plus sign on the key pad. Just take a look at irxevent.keys (in the documentation directory) if you are not sure about a symbol&#8217;s name.</dl>
<p> <i>KeySym:</i></p>
<dl>
<dt>
<dd> number as returned by <a href="//www.systutorials.com/docs/linux/man/3x-XStringToKeysym/">XStringToKeysym</a>(3x).</dl>
<p> <i>KeyCode:</i></p>
<dl>
<dt>
<dd> number as returned by <a href="//www.systutorials.com/docs/linux/man/3x-XKeysymToKeycode/">XKeysymToKeycode</a>(3x).</dl>
<p> <i>Windowname:</i></p>
<dl>
<dt>
<dd> can be the first characters of the window name displayed by the window manager or the name that is displayed below the icon. Some programs use the name displayed by the window manager to show a lot of status information but don&#8217;t change the icon name (like xawtv). Others append information to the window name (&quot;GQmpeg &#8211; kill_windooz.mp3&quot;). If neither window name nor icon name match the given Windowname information from <a href="//www.systutorials.com/docs/linux/man/3x-XClassHint/">XClassHint</a>(3x) will be checked.</dl>
<p> <i>CurrentWindow:</i></p>
<dl>
<dt>
<dd> refers to the active window as returned by <a href="//www.systutorials.com/docs/linux/man/3x-XGetInputFocus/">XGetInputFocus</a>(3x). Most times this is the window with your mouse pointer in it.</dl>
<p> <i>RootWindow:</i></p>
<dl>
<dt>
<dd> refers to the <i>root</i> window as returned by <a href="//www.systutorials.com/docs/linux/man/3x-RootWindow/">RootWindow</a>(3x). You may need this to send events to the window manager.</dl>
<p> <i>WindowID id:</i></p>
<dl>
<dt>
<dd> refers to the window with window identifier <i>id</i>. <i>id</i> should be a decimal number. It is useful when irxevent can&#8217;t find the desired window by other means.</dl>
<p> <i>Focus:</i></p>
<dl>
<dt>
<dd> will send the specified event to the given window only if it currently has the input focus. This of course does not make much sense when combined with CurrentWindow.</dl>
</dl>
<h2>TROUBLESHOOTING</h2>
<p> If you have problems finding the coordinates for a button click you can try xev -id &lt;window_id&gt;. The window_id can be found using xwininfo. If xev and xwininfo are not part of your distribution you can find them at a FTP server using the search engine at: <a rel="nofollow" href="http://ftpsearch.ntnu.no/">http://ftpsearch.ntnu.no/</a> . xev also reports the names of key symbols like &quot;Control_L&quot; (your left control key) or &quot;KP_Subtract&quot; (the &#8216;minus&#8217; key on your keypad). </p>
<p> There are programs that do not accept any synthetic X-events by default because they can cause security problems. Currently xterm and xemacs are known to ignore events simulated by irxevent. </p>
<p> You can however make xterm accept external events by enabling &quot;Allow SendEvents&quot; in the &quot;Main Options&quot; (hold down the Ctrl button and press the left mouse button inside the xterm window). You can as well place this line into your .Xresources file to change this permanently: </p>
<dl>
<dt>
<dd> XTerm.vt100.allowSendEvents: true</dl>
<p> Yet another possibility is to start xterm like this: </p>
<dl>
<dt>
<dd> xterm -xrm &quot;XTerm.vt100.allowSendEvents: true&quot;</dl>
<p> xemacs will accept events if you set a built-in variable. The following was taken from the online help: </p>
<dl>
<dt>
<dd> `x-allow-sendevents&#8217; is a built-in boolean variable. </p>
<p> Value: t </p>
<p> Documentation: </p>
<p> *Non-nil means to allow synthetic events. Nil means they are ignored. </p>
<p> Beware: allowing emacs to process SendEvents opens a big security hole. </p>
<p> In order to allow events you have to evaluate this lisp code (press Meta-x and enter the following expression): </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (setq x-allow-sendevents t)</p>
<p> Placing this line into your .xemacs-options file should have the same result.</dl>
<p> If you have problems sending events please drop me an email.</p>
<h2>AUTHOR</h2>
<p> Written by Heinrich Langos &lt;heinrich [at] mad.scientist.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<h2>Index</h2>
