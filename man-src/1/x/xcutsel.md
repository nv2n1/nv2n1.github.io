---
title: "xcutsel(1)"
name: "xcutsel"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcutsel/"
description: "xcutsel – interchange between cut buffer and selection"
---

<h2 class="name">NAME</h2>
<p> xcutsel &#8211; interchange between cut buffer and selection </p>
<h2>SYNOPSIS</h2>
<p> <code>xcutsel</code> [ <i>-toolkitoption</i> &#8230;] [-selection <i>selection</i>] [-cutbuffer <i>number</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xcutsel</i> program is used to copy the current selection into a cut buffer and to make a selection that contains the current contents of the cut buffer. It acts as a bridge between applications that don&#8217;t support selections and those that do. </p>
<p> By default, <i>xcutsel</i> will use the selection named PRIMARY and the cut buffer CUT_BUFFER0. Either or both of these can be overridden by command line arguments or by resources. </p>
<p> An <i>xcutsel</i> window has the following buttons:</p>
<dl>
<dt><i> quit</i></p>
<dd> When this button is pressed, <i>xcutsel</i> exits. Any selections held by <i>xcutsel</i> are automatically released.</p>
<dt><i> copy PRIMARY to 0</i></p>
<dd> When this button is pressed, <i>xcutsel</i> copies the current selection into the cut buffer.</p>
<dt><i> copy 0 to PRIMARY</i></p>
<dd> When this button is pressed, <i>xcutsel</i> converts the current contents of the cut buffer into the selection.</dl>
<p> The button labels reflect the selection and cutbuffer selected by command line options or through the resource database. </p>
<p> When the &#8220;copy 0 to PRIMARY&#8221; button is activated, the button will remain inverted as long as <i>xcutsel</i> remains the owner of the selection. This serves to remind you which client owns the current selection. Note that the value of the selection remains constant; if the cutbuffer is changed, you must again activate the copy button to retrieve the new value when desired.</p>
<h2>OPTIONS</h2>
<p> <i>Xcutsel</i> accepts all of the standard X Toolkit command line options as well as the following:</p>
<dl>
<dt><code>-selection </code><i>name</i></p>
<dd> This option specifies the name of the selection to use. The default is PRIMARY. The only supported abbreviations for this option are &#8220;-select&#8221;, &#8220;-sel&#8221; and &#8220;-s&#8221;, as the standard toolkit option &#8220;-selectionTimeout&#8221; has a similar name.</p>
<dt><code>-cutbuffer </code><i>number</i></p>
<dd> This option specifies the cut buffer to use. The default is cut buffer 0.</dl>
<h2>X DEFAULTS</h2>
<p> This program accepts all of the standard X Toolkit resource names and classes as well as:</p>
<dl>
<dt><code>selection (</code>class<code> Selection)</code></p>
<dd> This resource specifies the name of the selection to use. The default is PRIMARY.</p>
<dt><code>cutBuffer (</code>class<code> CutBuffer)</code></p>
<dd> This resource specifies the number of the cut buffer to use. The default is 0.</dl>
<h2>WIDGET NAMES</h2>
<p> The following instance names may be used when user configuration of the labels in them is desired:</p>
<dl>
<dt><code>sel-cut (</code>class<code> Command)</code></p>
<dd> This is the &#8220;copy SELECTION to BUFFER&#8221; button.</p>
<dt><code>cut-sel (</code>class<code> Command)</code></p>
<dd> This is the &#8220;copy BUFFER to SELECTION&#8221; button.</p>
<dt><code>quit (</code>class<code> Command)</code></p>
<dd> This is the &#8220;quit&#8221; button.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xclipboard/">xclipboard</a>(1), <a href="/docs/linux/man/1-xterm/">xterm</a>(1), text widget documentation, individual client documentation for how to make a selection.</p>
<h2>BUGS</h2>
<p> There is no way to change the name of the selection or the number of the cut buffer while the program is running.</p>
<h2>AUTHOR</h2>
<p> Ralph R. Swick, DEC/MIT Project Athena </p>
<h2>Index</h2>
