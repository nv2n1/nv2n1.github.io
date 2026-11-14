---
title: "xfce4-dict(1)"
name: "xfce4-dict"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfce4-dict/"
description: "xfce4-dict — a client program to query different dictionaries"
---

<h2 class="name">NAME</h2>
<p> xfce4-dict &#8212; a client program to query different dictionaries </p>
<h2>SYNOPSIS</h2>
<p> <code>xfce4-dict</code> [<code>option</code>] [<code>text &#8230;</code>]</p>
<h2>DESCRIPTION</h2>
<p> xfce4-dict allows you to search different kinds of dictionary services for words or phrases and shows you the result. Currently you can query a &quot;Dict&quot; server(RFC 2229), any online dictionary service by opening a web browser or search for words using a spell check program like aspell, ispell or enchant. </p>
<p> Homepage: <a rel="nofollow" href="http://goodies.xfce.org/projects/applications/xfce4-dict">http://goodies.xfce.org/projects/applications/xfce4-dict</a></p>
<h2>OPTIONS</h2>
<p> If called without any arguments, the xfce4-dict main window is shown. Any passed text argument(s) are used as search text.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;dict</code></p>
<dd> Search the given text using a Dict server(RFC 2229).</p>
<dt><code>-w</code>, <code>&#8211;web</code></p>
<dd> Search the given text using a web-based search engine.</p>
<dt><code>-t</code>, <code>&#8211;text-field</code></p>
<dd> Grab the focus on the text field in the panel (has no effect if panel plugin is not loaded).</p>
<dt><code>-s</code>, <code>&#8211;spell</code></p>
<dd> Check the given text with a spellchecker.</p>
<dt><code>-i</code>, <code>&#8211;ignore-plugin</code></p>
<dd> Start stand-alone application even if the panel plugin is loaded.</p>
<dt><code>-c</code>, <code>&#8211;clipboard</code></p>
<dd> Grabs the PRIMARY selection content (X selection clipboard), uses it as search text and performs a search. This is useful when you want to create keyboard shortcuts for this command. The search method can be specified with the -d, -w and -s options, if not specified the default search method is used. If the PRIMARY clipboard doesn&#8217;t contain any text, the normal clipboard is used.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose (print useful status messages).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show help information and exit.</dl>
<p> xfce4-dict supports all generic GTK options, a list is available on the help screen.</p>
<h2>BUGS</h2>
<p> There is a limitation of max. 12 characters in passing a search term to xfce4-dict when the panel plugin is loaded. That is, if you pass a search term as command line argument(s) to xfce4-dict which is longer than 12 characters, it is truncated. To be exact, the limit is 12 bytes so if the search term contains any non-ASCII characters it might be even less than 12 characters. To work around this limitation, you can add the command line &#8216;-i&#8217; so that xfce4-dict will start a single stand-alone application. Then all passed text is used as search term.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Enrico Troeger. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2, or (at your option) any later version. </p>
<h2>Index</h2>
