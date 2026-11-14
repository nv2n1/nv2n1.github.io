---
title: "xclipboard(1)"
name: "xclipboard"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xclipboard/"
description: "xclipboard – X clipboard client"
---

<h2 class="name">NAME</h2>
<p> xclipboard &#8211; X clipboard client </p>
<h2>SYNOPSIS</h2>
<p> <code>xclipboard</code> [ <i>-toolkitoption</i> &#8230; ] [ <code>-w</code> ] [ <code>-nw</code> ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xclipboard</i> program is used to collect and display text selections that are sent to the CLIPBOARD by other clients. It is typically used to save CLIPBOARD selections for later use. It stores each CLIPBOARD selection as a separate string, each of which can be selected. Each time CLIPBOARD is asserted by another application, <i>xclipboard</i> transfers the contents of that selection to a new buffer and displays it in the text window. Buffers are never automatically deleted, so you&#8217;ll want to use the delete button to get rid of useless items. </p>
<p> Since <i>xclipboard</i> uses a Text Widget to display the contents of the clipboard, text sent to the CLIPBOARD may be re-selected for use in other applications. <i>xclipboard</i> also responds to requests for the CLIPBOARD selection from other clients by sending the entire contents of the currently displayed buffer. </p>
<p> An <i>xclipboard</i> window has the following buttons across the top:</p>
<dl>
<dt><i>quit</i></p>
<dd> When this button is pressed, <i>xclipboard</i> exits.</p>
<dt><i>delete</i></p>
<dd> When this button is pressed, the current buffer is deleted and the next one displayed.</p>
<dt><i>new</i></p>
<dd> Creates a new buffer with no contents. Useful in constructing a new CLIPBOARD selection by hand.</p>
<dt><i>save</i></p>
<dd> Displays a File Save dialog box. Pressing the Accept button saves the currently displayed buffer to the file specified in the text field.</p>
<dt><i>next</i></p>
<dd> Displays the next buffer in the list.</p>
<dt><i>previous</i></p>
<dd> Displays the previous buffer.</dl>
<h2>OPTIONS</h2>
<p> The <i>xclipboard</i> program accepts all of the standard X Toolkit command line options as well as the following:</p>
<dl>
<dt><code>-w</code></p>
<dd> This option indicates that lines of text that are too long to be displayed on one line in the clipboard should wrap around to the following lines.</p>
<dt><code>-nw</code></p>
<dd> This option indicates that long lines of text should not wrap around. This is the default behavior.</dl>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xclipboard</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
XClipboard  xclipboard
        Form  form
                Command  Quit
                Command  delete
                Command  new
                Command  Save
                Command  next
                Command  prev
                Label  index
                Text  text
        TransientShell  fileDialogShell
                Dialog  fileDialog
                        Label  label
                        Command  accept
                        Command  cancel
                        Text value
        TransientShell  failDialogShell
                Dialog  failDialog
                        Label  label
                        Command  continue
</pre>
<h2>SENDING/RETRIEVING CLIPBOARD CONTENTS</h2>
<p> Text is copied to the clipboard whenever a client asserts ownership of the <code>CLIPBOARD</code> selection. Text is copied from the clipboard whenever a client requests the contents of the <code>CLIPBOARD</code> selection. Examples of event bindings that a user may wish to include in a resource configuration file to use the clipboard are: </p>
<pre>
*VT100.Translations: #override \
        &lt;Btn3Up&gt;:       select-end(CLIPBOARD) 
\
        &lt;Btn2Up&gt;:       insert-selection(PRIMARY,CLIPBOARD) 
\
        &lt;Btn2Down&gt;:     ignore ()
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xcutsel/">xcutsel</a>(1), <a href="/docs/linux/man/1-xterm/">xterm</a>(1), individual client documentation for how to make a selection and send it to the CLIPBOARD.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/X11/app-defaults/XClipboard</i></p>
<dd> specifies required resources</dl>
<h2>AUTHOR</h2>
<p> Ralph R. Swick, DEC/MIT Project Athena<br />
 Chris D. Peterson, MIT X Consortium<br />
 Keith Packard, MIT X Consortium </p>
<h2>Index</h2>
