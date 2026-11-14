---
title: "tk_getoption(3)"
name: "tk_getoption"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getoption/"
description: "Tk_GetOption – retrieve an option from the option database"
---

<p>Tk_GetOption &#8211; retrieve an option from the option database </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Uid
<code>Tk_GetOption</code>(<i>tkwin, name, class</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>const char <i>*name</i> (in) Name of desired option.</p>
<dd>const char <i>*class</i> (in) Class of desired option. Null means there is no class for this option; do lookup based on name only. </p>
</dl>
<h2>Description</h2>
<p>This procedure is invoked to retrieve an option from the database associated with <i>tkwin</i>&#8216;s main window. If there is an option for <i>tkwin</i> that matches the given <i>name</i> or <i>class</i>, then it is returned in the form of a Tk_Uid. If multiple options match <i>name</i> and <i>class</i>, then the highest-priority one is returned. If no option matches, then NULL is returned. </p>
<p> <code>Tk_GetOption</code> caches options related to <i>tkwin</i> so that successive calls for the same <i>tkwin</i> will execute much more quickly than successive calls for different windows. </p>
<h2>Keywords</h2>
<p>class, name, option, retrieve</p>
