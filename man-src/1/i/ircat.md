---
title: "ircat(1)"
name: "ircat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ircat/"
description: "ircat – print strings when pressing buttons"
---

<h2>NAME</h2>
<p> ircat &#8211; print strings when pressing buttons</p>
<h2>SYNOPSIS</h2>
<p> <code>ircat</code> [<i>options</i>] <i>&lt;prog&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> This program prints config strings to standard output. It can be used to provide remote control input to scripts and to debug your .lircrc file. </p>
<p> The argument to the program is the program name, as it appears in the prog entries in .lircrc.</p>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display usage summary</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>-c</code> <code>&#8211;config=</code>&lt;file&gt;</p>
<dd> set config file</dl>
<h2>EXAMPLES</h2>
<p> If .lircrc contains: </p>
<pre>
begin
        prog = myprog
        button = KEY_CHANNELUP
        config = next_file
end
</pre>
<p> then </p>
<pre>
$ ircat myprog
</pre>
<p> will print &quot;next_file&quot; (followed by newline) every time the button bound to KEY_CHANNELUP is pressed.</p>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<h2>Index</h2>
