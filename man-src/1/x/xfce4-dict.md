---

title: "xfce4-dict(1)"
name: "xfce4-dict"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfce4-dict/"
description: "xfce4-dict — a client program to query different dictionaries"
---

<p> <code>xfce4-dict</code> [<code>option</code>] [<code>text &#8230;</code>]</p>
<p> xfce4-dict allows you to search different kinds of dictionary services for words or phrases and shows you the result. Currently you can query a &quot;Dict&quot; server(RFC 2229), any online dictionary service by opening a web browser or search for words using a spell check program like aspell, ispell or enchant. </p>
<p> Homepage: <a rel="nofollow" href="http://goodies.xfce.org/projects/applications/xfce4-dict">http://goodies.xfce.org/projects/applications/xfce4-dict</a></p>
<h2>OPTIONS</h2>
<p> If called without any arguments, the xfce4-dict main window is shown. Any passed text argument(s) are used as search text.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;dict</code></dt>
<dd> Search the given text using a Dict server(RFC 2229).</dd>
<dt><code>-w</code>, <code>&#8211;web</code></dt>
<dd> Search the given text using a web-based search engine.</dd>
<dt><code>-t</code>, <code>&#8211;text-field</code></dt>
<dd> Grab the focus on the text field in the panel (has no effect if panel plugin is not loaded).</dd>
<dt><code>-s</code>, <code>&#8211;spell</code></dt>
<dd> Check the given text with a spellchecker.</dd>
<dt><code>-i</code>, <code>&#8211;ignore-plugin</code></dt>
<dd> Start stand-alone application even if the panel plugin is loaded.</dd>
<dt><code>-c</code>, <code>&#8211;clipboard</code></dt>
<dd> Grabs the PRIMARY selection content (X selection clipboard), uses it as search text and performs a search. This is useful when you want to create keyboard shortcuts for this command. The search method can be specified with the -d, -w and -s options, if not specified the default search method is used. If the PRIMARY clipboard doesn&#8217;t contain any text, the normal clipboard is used.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Be verbose (print useful status messages).</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Show version information.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Show help information and exit.</dd></dl>
<p> xfce4-dict supports all generic GTK options, a list is available on the help screen.</p>
<h2>BUGS</h2>
<p> There is a limitation of max. 12 characters in passing a search term to xfce4-dict when the panel plugin is loaded. That is, if you pass a search term as command line argument(s) to xfce4-dict which is longer than 12 characters, it is truncated. To be exact, the limit is 12 bytes so if the search term contains any non-ASCII characters it might be even less than 12 characters. To work around this limitation, you can add the command line &#8216;-i&#8217; so that xfce4-dict will start a single stand-alone application. Then all passed text is used as search term.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Enrico Troeger. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2, or (at your option) any later version. </p>
