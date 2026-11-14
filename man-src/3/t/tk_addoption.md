---
title: "tk_addoption(3)"
name: "tk_addoption"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_addoption/"
description: "Tk_AddOption – Add an option to the option database"
---

<p>Tk_AddOption &#8211; Add an option to the option database </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
void
<code>Tk_AddOption</code>(<i>tkwin, name, value, priority</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>const char <i>*name</i> (in) Multi-element name of option.</p>
<dd>const char <i>*value</i> (in) Value of option.</p>
<dd>int <i>priority</i> (in) Overall priority level to use for option. </p>
</dl>
<h2>Description</h2>
<p>This procedure is invoked to add an option to the database associated with <i>tkwin</i>&#8216;s main window. <i>Name</i> contains the option being specified and consists of names and/or classes separated by asterisks or dots, in the usual X format. <i>Value</i> contains the text string to associate with <i>name</i>; this value will be returned in calls to <code>Tk_GetOption</code>. <i>Priority</i> specifies the priority of the value; when options are queried using <code>Tk_GetOption</code>, the value with the highest priority is returned. <i>Priority</i> must be between 0 and <code>TK_MAX_PRIO</code>. Some common priority values are:</p>
<dl COMPACT>
<dt>20</p>
<dd>Used for default values hard-coded into widgets.</p>
<dt>40</p>
<dd>Used for options specified in application-specific startup files.</p>
<dt>60</p>
<dd>Used for options specified in user-specific defaults files, such as <code>.Xdefaults</code>, resource databases loaded into the X server, or user-specific startup files.</p>
<dt>80</p>
<dd>Used for options specified interactively after the application starts running. </p>
</dl>
<h2>Keywords</h2>
<p>class, name, option, add</p>
