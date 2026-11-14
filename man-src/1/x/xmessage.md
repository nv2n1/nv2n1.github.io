---
title: "xmessage(1)"
name: "xmessage"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmessage/"
description: "xmessage – display a message or query in a window (X-based /bin/echo)"
---

<h2 class="name">NAME</h2>
<p> xmessage &#8211; display a message or query in a window (X-based /bin/echo) </p>
<h2>SYNOPSIS</h2>
<p> <code>xmessage</code> [ <code>-buttons</code> <i>label1</i>[<code>:</code>value1]<code>,</code>label2[<code>:</code>value2]<code>,</code> &#8230; ] [ <i>options</i> ] <code>-file</code> <i>filename</i><br />
 <code>xmessage</code> [ <code>-buttons</code> <i>label1</i>[<code>:</code>value1]<code>,</code>label2[<code>:</code>value2]<code>,</code> &#8230; ] [ <i>options</i> ] <i>message</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <i>xmessage</i> program displays a window containing a message from the command line, a file, or standard input. Along the lower edge of the message is row of buttons; clicking the left mouse button on any of these buttons will cause <i>xmessage</i> to exit. Which button was pressed is returned in the exit status and, optionally, by writing the label of the button to standard output. </p>
<p> The program is typically used by shell scripts to display information to the user or to ask the user to make a choice. </p>
<p> Unless a size is specified, <i>xmessage</i> sizes itself to fit the message, up to a maximum size. If the message is too big for the window, <i>xmessage</i> will display scroll bars.</p>
<h2>OPTIONS</h2>
<p> These are the command line options that <i>xmessage</i> understands, in addition to the standard ones listed in <code><a href="/docs/linux/man/7-x/">X</a></code>(7).</p>
<dl>
<dt><code>-buttons </code><i>button,button,&#8230;</i></p>
<dd> This option will cause <i>xmessage</i> to create one button for each comma-separated <i>button</i> argument. The corresponding resource is <code>buttons</code>. Each <i>button</i> consists of a label optionally followed by a colon and an exit value. The label is the name of the Command button widget created and will be the default text displayed to the user. Since this is the name of the widget it may be used to change any of the resources associated with that button. The exit value will be returned by <i>xmessage</i> if that button is selected. The default exit value is 100 plus the button number. Buttons are numbered from the left starting with one. The default string if no <code>-buttons</code> option is given is <code>okay:0</code>.</p>
<dt><code>-default </code><i>label</i></p>
<dd> Defines the button with a matching <i>label</i> to be the default. If not specified there is no default. The corresponding resource is <code>defaultButton</code>. Pressing Return anywhere in the <i>xmessage</i> window will activate the default button. The default button has a wider border than the others.</p>
<dt><code>-file </code><i>filename</i></p>
<dd> File to display. The corresponding resource is <code>file</code>. A <i>filename</i> of `<code>&#8211;</code>&#8216; reads from standard input. If this option is not supplied, <i>xmessage</i> will display all non-option arguments in the style of <i>echo</i>. Either <code>-file</code> or a message on the command line should be provided, but not both.</p>
<dt><code>-print</code></p>
<dd> This will cause the program to write the label of the button pressed to standard output. Equivalent to setting the <code>printValue</code> resource to TRUE. This is one way to get feedback as to which button was pressed.</p>
<dt><code>-center</code></p>
<dd> Pop up the window at the center of the screen. Equivalent to setting the <code>center</code> resource to TRUE.</p>
<dt><code>-nearmouse</code></p>
<dd> Pop up the window near the mouse cursor. Equivalent to setting the <code>nearMouse</code> resource to TRUE.</p>
<dt><code>-timeout </code><i>secs</i></p>
<dd> Exit with status 0 after <i>secs</i> seconds if the user has not clicked on a button yet. The corresponding resource is <code>timeout</code>.</dl>
<h2>WIDGET HIERARCHY</h2>
<p> Knowing the name and position in the hierarchy of each widget is useful when specifying resources for them. In the following chart, the class and name of each widget is given. </p>
<pre>
Xmessage (xmessage)
        Form form
                Text message
                Command (label1)
                Command (label2)
                .
                .
                .
</pre>
<h2>RESOURCES</h2>
<p> The program has a few top-level application resources that allow customizations that are specific to <i>xmessage</i>.</p>
<dl>
<dt><code>file</code></p>
<dd> A String specifying the file to display.</p>
<dt><code>buttons</code></p>
<dd> A String specifying the buttons to display. See the <code>-buttons</code> command-line option.</p>
<dt><code>defaultButton</code></p>
<dd> A String specifying a default button by label.</p>
<dt><code>printValue</code></p>
<dd> A Boolean value specifying whether the label of the button pressed to exit the program is written to standard output. The default is FALSE.</p>
<dt><code>center</code></p>
<dd> A Boolean value specifying whether to pop up the window at the center of the screen. The default is FALSE.</p>
<dt><code>nearMouse</code></p>
<dd> A Boolean value specifying whether to pop up the window near the mouse cursor. The default is FALSE.</p>
<dt><code>timeout</code></p>
<dd> The number of seconds after which to exit with status 0. The default is 0, which means never time out.</p>
<dt><code>maxHeight (</code>class<code> Maximum)</code></p>
<dd> The maximum height of the text part of the window in pixels, used if no size was specified in the geometry. The default is 0, which means use 70% of the height of the screen.</p>
<dt><code>maxWidth (</code>class<code> Maximum)</code></p>
<dd> The maximum width of the text part of the window in pixels, used if no size was specified in the geometry. The default is 0, which means use 70% of the width of the screen.</dl>
<h2>ACTIONS</h2>
<dl>
<dt><code>exit(</code><i>value</i>)</p>
<dd> exit immediately with an exit status of <i>value</i> (default 0). This action can be used with translations to provide alternate ways of exiting <i>xmessage</i>.</p>
<dt><code>default-exit()</code></p>
<dd> exit immediately with the exit status specified by the default button. If there is no default button, this action has no effect.</dl>
<h2>EXIT STATUS</h2>
<p> If it detects an error, <i>xmessage</i> returns 1, so this value should not be used with a button.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-x/">X</a></i>(7), <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1), <i><a href="/docs/linux/man/1-cat/">cat</a></i>(1) </p>
<h2>AUTHORS</h2>
<p> Chris Peterson, MIT Project Athena<br />
 Stephen Gildea, X Consortium </p>
<h2>Index</h2>
