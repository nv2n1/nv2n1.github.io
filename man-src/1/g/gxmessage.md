---
title: "gxmessage(1)"
name: "gxmessage"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gxmessage/"
description: "gxmessage – a GTK-based xmessage clone"
---

<h2 class="name">NAME</h2>
<p> gxmessage &#8211; a GTK-based xmessage clone </p>
<h2>SYNOPSIS</h2>
<p> <code>gxmessage</code> [<i>OPTIONS</i>] <code>message</code> &#8230;<br />
 <code>gxmessage</code> [<i>OPTIONS</i>] -file <i>FILENAME</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gxmessage</code> opens a window to display a message obtained from the command line, from a file, or from <i>stdin</i>. The window includes a row of buttons, each of which causes the program to exit with a different return code. </p>
<p> The GNU Info entry for gxmessage contains detailed information and examples.</p>
<h2>OPTIONS</h2>
<p> <code>gxmessage</code> should accept any option <code>xmessage</code> would, although some (such as <code>-bw</code> and <code>-xrm</code>) are silently ignored. Options supported by <code>gxmessage</code> are as follows:</p>
<dl>
<dt><code>-bg</code> <i>COLOR</i></p>
<dd>
 Sets the background color of the message to <i>COLOR</i>. Examples: red, &quot;#c90&quot;, &quot;#446a7e&quot;.</p>
<dt><code>-borderless</code></p>
<dd>
 Opens the <code>gxmessage</code> window without the usual window frame. This option is not compatible with <code>xmessage</code>.</p>
<dt><code>-buttons</code> <i>BUTTON_LIST</i></p>
<dd>
 Defines the buttons to be created. <i>BUTTON_LIST</i> is a comma-separated list of <i>LABEL</i><code>:</code><i>VALUE</i> pairs, one for each button. The <i>LABEL</i> is the text that appears on the button. The <i>VALUE</i> (0..255) is the code the program will exit with if that button is pressed. Commas and colons can be escaped using backslashes (\). As well as ordinary text, the <i>LABEL</i> can specify a GTK &quot;stock&quot; button, like &quot;GTK_STOCK_CANCEL&quot;, or it can include an underscore (_) to specify a keyboard accelerator. If <i>VALUE</i>s are omitted, they default to 101, 102, 103, etc., in order. If no <code>-buttons</code> option is given, <i>BUTTON_LIST</i> defaults to <code>&quot;okay:0&quot;</code>. </p>
<pre>
gxmessage -buttons &quot;Foo:42,Bar:63&quot; &quot;Example&quot;
echo $?
gxmessage -buttons &quot;_Foo,_Bar&quot; &quot;Example&quot;
echo $?
gxmessage &quot;Example&quot;
echo $?
gxmessage -buttons &quot;GTK_STOCK_OK:0&quot; &quot;Example&quot;
echo $?
gxmessage -buttons &quot;Hello\, world&quot; &quot;Example&quot;
</pre>
<dt><code>-center</code></p>
<dd>
 Opens the <code>gxmessage</code> window in the middle of the screen.</p>
<dt><code>-default</code> <i>LABEL</i></p>
<dd>
 Opens the <code>gxmessage</code> window with input focused on the specified button. <i>LABEL</i> is one of the <i>LABEL</i>s in <i>BUTTON_LIST</i> (see <code>-buttons</code>, above).</p>
<dt><code>-display</code> <i>DISPLAY</i></p>
<dd>
 Specifies the X display to use.</p>
<dt><code>-encoding</code> <i>CHARSET</i></p>
<dd>
 Specifies the encoding of the message text. By default, the message text is assumed to match the encoding of the current locale. This option is not compatible with <code>xmessage</code>.</p>
<dt><code>-entry</code></p>
<dd>
 Adds a text entry box to the <code>gxmessage</code> window. When the window closes, any text in the entry box will be copied to <i>stdout</i>. This option is not compatible with <code>xmessage</code> and can&#8217;t be used at the same time as the <code>-print</code> option.</p>
<dt><code>-entrytext</code> <i>TEXT</i></p>
<dd>
 Same as <code>-entry</code>, but sets the default entry box contents to <i>TEXT</i>. This option is not compatible with <code>xmessage</code>.</p>
<dt><code>-fg</code> <i>COLOR</i></p>
<dd>
 Sets the message text color to <i>COLOR</i>.</p>
<dt><code>-file</code> <i>FILENAME</i></p>
<dd>
 Causes the named file to be used as the message source. If a dash (-) is used in place of <i>FILENAME</i>, the message will be read from <i>stdin</i>.</p>
<dt><code>-fn</code> | <code>-font</code> <i>FONT</i></p>
<dd>
 Specifies the message font, using GTK2&#8217;s font specification system. For example, <code>-font &quot;serif italic 14&quot;</code>. (GTK2&#8217;s font system is not compatible with <code>xmessage</code>. See the Compatibility section, below, for a workaround.)</p>
<dt><code>-geometry</code> <i>GEOMETRY</i></p>
<dd>
 Sets the window&#8217;s size (position is ignored by <code>gxmessage</code>). Example: <code>-geometry 400&#215;200</code></p>
<dt><code>-help</code></p>
<dd>
 Displays basic usage information then exits.</p>
<dt><code>-iconic</code></p>
<dd>
 Opens the <code>gxmessage</code> window in its iconized (minimized) state.</p>
<dt><code>-name</code> <i>NAME</i></p>
<dd>
 Sets the <code>gxmessage</code> window&#8217;s name to <i>NAME</i>.</p>
<dt><code>-nearmouse</code></p>
<dd>
 Opens the <code>gxmessage</code> window near the mouse pointer.</p>
<dt><code>-nofocus</code></p>
<dd>
 Prevents the <code>gxmessage</code> window from receiving focus when it opens. This option is not compatible with <code>xmessage</code>.</p>
<dt><code>-print</code></p>
<dd>
 Writes the <i>LABEL</i> of the selected button to <i>stdout</i>.</p>
<dt><code>-timeout</code> <i>SECONDS</i></p>
<dd>
 Automatically closes the <code>gxmessage</code> window with an exit code of 0 if no button is pressed within <i>SECONDS</i> seconds. (The <code>-entry</code> and <code>-entrytext</code> options cause <code>-timeout</code> to be ignored.)</p>
<dt><code>-title</code> <i>TITLE</i></p>
<dd>
 Sets the <code>gxmessage</code> window&#8217;s title to <i>TITLE</i>.</p>
<dt><code>-version</code></p>
<dd>
 Displays the program&#8217;s version number and Copyright details, then exits. This option is not compatible with <code>xmessage</code>.</p>
<dt><code>-wrap</code></p>
<dd>
 Causes lines to wrap rather than exceed the width of the window. This option is not compatible with <code>xmessage</code>.</dl>
<h2>GTK DEFAULTS</h2>
<p> The program&#8217;s default appearance can be adjusted using GTK resource files. The main text display widget is named <code>gxmessage-textview</code>. The text entry widget is named <code>gxmessage-entry</code>. </p>
<pre><code>
#Example : ~ /.gtkrc - 2.0
style "gxmsg" {
    text[NORMAL] = "#cc9900" base[NORMAL] = "#660000" text[SELECTED] = "#660000" base[SELECTED] = "#cc9900" font_name = "monospace"} widget "*.gxmessage-textview" style "gxmsg" widget "*.gxmessage-entry" style "gxmsg"
</code></pre>
<h2>EXIT STATUS</h2>
<p> If a button is pressed, the program returns the value assigned to that button. The default &quot;okay&quot; button returns 0. </p>
<p> If a timeout event occurs, the program returns 0. </p>
<p> If an error occurs, or if the window is closed without a button-press or timeout event, the program exits with code 1. Pressing the ESC key also causes the program to exit with code 1.</p>
<h2>COMPATIBILITY WITH XMESSAGE</h2>
<p> Fall back to <code>xmessage</code> if <code>gxmessage</code> isn&#8217;t available: </p>
<pre>
#! /bin/sh
XMESSAGE=$(which gxmessage) || XMESSAGE=xmessage
$XMESSAGE &quot;hello, world&quot;
</pre>
<p> If you specify fonts, check which program you&#8217;re using: </p>
<pre><code>
font = "monospace 14"
    ["$XMESSAGE" = xmessage] &amp;&amp;font = "fixed" $XMESSAGE $
{
font:
    +-fn "$font"
}
"hello, world"
</code></pre>
<p> Don&#8217;t use double-dashed command line options: </p>
<pre>
$XMESSAGE &quot;hello, world&quot; -buttons good
$XMESSAGE &quot;hello, world&quot; --buttons bad
</pre>
<p> Don&#8217;t use the <code>gxmessage</code>-specific options: </p>
<pre>
<code>-entry</code>, <code>-entrytext</code>, <code>-borderless</code>, <code>-wrap</code>,
<code>-encoding</code>, <code>-nofocus</code>, <code>-version</code>, <code>-h</code>, <code>-?</code>
</pre>
<h2>BUGS</h2>
<p> The position component of <code>-geometry</code> values is ignored by <code>gxmessage</code>. </p>
<p> For some reason, opening the gxmessage window with no button set to be the default causes GTK to emit a &quot;beep&quot; sound. </p>
<p> If you discover other bugs in the most recent version of <code>gxmessage</code>, please get in touch.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-xmessage/">xmessage</a></i>(1), <i><a href="/docs/linux/man/1-zenity/">zenity</a></i>(1), <i><a href="/docs/linux/man/1-dialog/">dialog</a></i>(1) </p>
<p> The GNU Info entry for gxmessage contains detailed information and examples.</p>
<h2>AUTHORS</h2>
<p> Timothy Musson &lt;trmusson [at] gmail.com&gt;</p>
<h2>COPYRIGHT NOTICE</h2>
<p> Copyright &#169; 2003, 2004, 2005, 2006, 2007, 2008, 2009 Timothy Richard Musson </p>
<p> Copying and distribution of this file, with or without modification, are permitted provided the copyright notice and this notice are preserved. </p>
<h2>Index</h2>
