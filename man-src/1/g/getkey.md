---
title: "getkey(1)"
name: "getkey"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getkey/"
description: "getkey – wait until a key is pressed"
---

<h2 class="name">NAME</h2>
<p> getkey &#8211; wait until a key is pressed</p>
<h2>SYNOPSIS</h2>
<p> <code>getkey</code> [<i>OPTION</i>]&#8230; [<i>KEYS</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>getkey</code> waits until one of <i>KEYS</i> is pressed. If <i>KEYS</i> are not specified, any key is accepted. <i>KEYS</i> are matched case-insensitive. </p>
<h2>EXIT STATUS</h2>
<p> <code>getkey</code> exits with status 0 if one of the expected keys is pressed. If invalid arguments are specified, <code>getkey</code> exits with status 255. If <code>getkey</code> is interrupted or the wait times out, <code>getkey</code> exits with other non-zero status. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;wait</code> <i>SECONDS</i></p>
<dd> Wait only for <i>SECONDS</i> seconds. The default is 0, which means to wait without a time limit. </p>
<dt><code>-i</code>, <code>&#8211;ignore-control-chars</code></p>
<dd> Don&#8217;t treat Ctrl+C and Ctrl+D specially. When this option is not specified, these characters interrupt <code>getkey</code>. </p>
<dt><code>-m</code>, <code>&#8211;message</code> <i>MESSAGE</i></p>
<dd> Display <i>MESSAGE</i> while waiting. The message is used as a format string in <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), with a single argument, the number of seconds left. Typical usage is therefore <code>&quot;Press a key within %d seconds to &#8230;&quot;</code>. If <i>MESSAGE</i> contains other format string directives, the behavior is undefined and <code>getkey</code> may crash. </p>
<p> If there is no time limit specified, the number of seconds left is reported as 0. </p>
</dl>
<h2>Index</h2>
