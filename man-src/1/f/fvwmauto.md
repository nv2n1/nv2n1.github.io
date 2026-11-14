---
title: "fvwmauto(1)"
name: "fvwmauto"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmauto/"
description: "FvwmAuto – the fvwm auto-raise module"
---

<p><i>FvwmAuto</i> &#8211; the fvwm auto-raise module </p>
<h2>Synopsis</h2>
<pre>Module FvwmAuto Timeout [-passid] [-menter|-menterleave|-mfocus] [EnterCommand [LeaveCommand]]</pre>
<p><i>FvwmAuto</i> can only be invoked by fvwm. Command line invocation of the <i>FvwmAuto</i> will not work. </p>
<h2>Description</h2>
<p>The <i>FvwmAuto</i> module is most often used to automatically raise focused windows. </p>
<h2>Invocation</h2>
<p>The correct syntax is: </p>
<pre>Module FvwmAuto Timeout [-passid] [-menter|-menterleave|-mfocus] [EnterCommand [LeaveCommand]]
AddToMenu Modules
+ &quot;Auto Raise (300 ms)&quot; Module FvwmAuto 300
+ &quot;Auto Raise/Lower&quot; Module FvwmAuto 300 &quot;Silent Raise&quot; &quot;Silent Lower&quot;</pre>
<p>The <i>Timeout</i> argument is required. It specifies how long a window must retain the keyboard input focus before the command is executed. The delay is measured in milliseconds, and any integer greater than zero is valid. </p>
<p> If the literal option <i>-passid</i> is given, the window id of the window just entered or left is appended to the command that is sent to fvwm. This can be used with the <code>WindowId</code> command of fvwm. </p>
<p> The options <i>-menter</i>, <i>-menterleave</i> and <i>-mfocus</i> influence the actions FvwmAuto reacts to. No more than one of the options can be chosen. In <i>-mfocus</i> mode, FvwmAuto raises the window that has the focus. In <i>-menter</i> mode, FvwmAuto raises the window under the pointer when the pointer enters a window. The <i>LeaveCommand</i> is executed on the window that was below the pointer before it entered the new window. When the pointer leaves a window and enters the root window, the <i>EnterCommand</i> is executed too, but without a window to operate on. In <i>-menterleave</i> mode, FvwmAuto works just like in <i>-menter</i> mode, but the <i>LeaveCommand</i> is also executed if the pointer moves out of a window but does not enter a new window. The latter two modes of operation are useful with windows that do not accept the focus. </p>
<p> Note: -menterleave mode can interfere with popup windows of some applications. One example is the zoom menu of Ghostview. Please do not complain about this to us &#8211; it is a bug in Ghostview. </p>
<p> <i>EnterCommand</i> and <i>LeaveCommand</i> are optional. <i>EnterCommand</i> is executed <i>Timeout</i> milliseconds after a window gets the input focus, <i>LeaveCommand</i> is executed <i>Timeout</i> milliseconds after the window has lost focus. Note that you always should use the &#8216;Silent&#8217; keyword before the command itself. FvwmAuto prepends &quot;Silent &quot; to the command string on its own if yor forget this. Without this prefix fvwm would ask you for a window to act on if the window has died before the command sent by FvwmAuto has been processed by fvwm. This can for example happen with popup menus. </p>
<p> &quot;Silent Raise&quot; is the default for <i>EnterCommand</i>, but any fvwm function is allowed. I would not use &quot;Close&quot; or &quot;Destroy&quot; with a low timeout, though. The <i>LeaveCommand</i> can be handy for a tidy desktop. Experiment with: </p>
<pre>Module FvwmAuto 0 Nop &quot;Silent Lower&quot;
Module FvwmAuto 0 Nop &quot;Silent Iconify&quot;</pre>
<p>An example for auto raising windows with ClickToFocus: </p>
<pre>Style * ClickToFocus
FvwmAuto 0 -menter &quot;Silent Raise&quot;</pre>
<p>An example for auto raising and lowering only some windows: </p>
<pre>To start FvwmAuto:
FvwmAuto 0 -passid -menter \
&quot;Silent selective_raiselower raise&quot; \
&quot;Silent selective_raiselower lower&quot;</pre>
<p>And put this in your .fvwm2rc: </p>
<pre>AddToFunc selective_raiselower
+ I WindowId $1 (FvwmIconMan) $0
+ I WindowId $1 (FvwmButtons) $0
+ I WindowId $1 (xclock) $0
...</pre>
<p>More complex example (three FvwmAuto&#8217;s are running): </p>
<pre>DestroyFunc RestoreIconified
AddToFunc RestoreIconified
+ I Current (Iconic) Iconify false
DestroyFunc RegisterFocus
AddToFunc RegisterFocus
+ I Exec date +&quot;%T $n focused&quot; &gt;&gt;/tmp/focus-stats.txt
DestroyFunc RegisterUnfocus
AddToFunc RegisterUnfocus
+ I Exec date +&quot;%T $n unfocused&quot; &gt;&gt;/tmp/focus-stats.txt
KillModule FvwmAuto
Module FvwmAuto 250 Raise Nop
Module FvwmAuto 800 RestoreIconified Nop
Module FvwmAuto 0 RegisterFocus RegisterUnfocus</pre>
<h2>Notes</h2>
<p>There is a special Raise/Lower support in FvwmAuto. It was added to improve Raise/Lower callbacks, since most of FvwmAuto usages is auto-raising or auto-lowering. This improvement includes locking on M_RAISE_WINDOW and M_LOWER_WINDOW packets and not raising/lowering explicitly raised windows. The special Raise/Lower support is enabled only when either <i>EnterCommand</i> or <i>LeaveCommand</i> contain substring &quot;Raise&quot; or &quot;Lower&quot;. You can use this fact to enable/disable any special support by renaming these commands, if FvwmAuto does not automatically do want you expect it to do. </p>
<p> Using <i>FvwmAuto</i> in conjunction with <i>EdgeCommand</i> can be even more powerful. There is a short example in the <i>fvwm</i> man page. </p>
<h2>Author</h2>
<pre>FvwmAuto just appeared one day, nobody knows how.
FvwmAuto was simply rewritten 09/96, nobody knows by whom.</pre>
