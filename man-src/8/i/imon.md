---
title: "imon(8)"
name: "imon"
section: "8"
letter: "i"
url: "/docs/linux/man/8-imon/"
description: "imon – watch ISDN activities"
---

<p>imon &#8211; watch ISDN activities</p>
<h2>Synopsis</h2>
<p><code>imon [ -q] [-p </code><i>phonebook</i><code>]</code></p>
<h2>Description</h2>
<p><i>imon</i> is a ncurses based utility for watching ISDN activity. </p>
<h2>Options</h2>
<dl>
<dt><code>-q </code></p>
<dd>If this option is given, the facility of terminatig the program by pressing &#8216;Q&#8217; is disabled and the signals SIGHUP and SIGINT are caught. This option is intended for starting imon from within an rc script with redirecting input/output to some otherwise unused virtual console at boot time.</dl>
<dl>
<dt><code>-p</code><i> phonebook</i></p>
<dd>is used to supply imon with a <i>phonebook</i> file. The format of a <i>phonebook</i> file is very simple: Every line has two elements separated by a <code>TAB</code>. The first element is a phone number which can contain wildcards. The second element is a descriptive string. For each active connection, this string is shown instead the phone number. Pressing &#8216;S&#8217; toggles between display of strings and phone numbers. Pressing &#8216;R&#8217; rereads the phonebook file in case of changes during program execution.</dl>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/4-ttyi/">ttyI</a></i>(4), <i><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></i>(8), <i><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></i>(4). </p>
