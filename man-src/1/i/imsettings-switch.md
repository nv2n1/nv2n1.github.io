---

title: "imsettings-switch(1)"
name: "imsettings-switch"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imsettings-switch/"
description: "imsettings-switch – Switch Input Method"
---

<p> imsettings-switch &#8211; Switch Input Method</p>
<h2>SYNOPSIS</h2>
<p> <code>imsettings-switch</code> [ <code>-hnqrx</code> ] [ <code>&#8211;no-update</code> ] [ <code>&#8211;quiet</code> ] [ <code>&#8211;restart</code> ] [ <code>&#8211;read-xinputrc</code> ] [ <code>&#8211;help</code> ] [Input Method name | configuration filename]</p>
<h2>DESCRIPTION</h2>
<p> <code>imsettings-switch</code> switches Input Method which is managed under imsettings. Either <i>Input Method name</i> or <i>configuration filename</i> are required unless <code>&#8211;read-xinputrc</code> option is specified to determine the target from <i>$HOME/.config/imsettings/xinputrc</i> or <i>$xinputrcdir/xinputrc</i>.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-n</code> <code>&#8211;no-update</code></dt>
<dd> Do not update <i>$HOME/imsettings/xinputrc</i>. without this option, <code>imsettings-switch</code> will updates it with the targeted Input Method.</dd>
<dt><code>-q</code> <code>&#8211;quiet</code></dt>
<dd> Do not show any messages except errors.</dd>
<dt><code>-r</code> <code>&#8211;restart</code></dt>
<dd> Restart the given Input Method or one which is determined from xinputrc by <code>&#8211;read-xinputrc</code> option.</dd>
<dt><code>-x</code> <code>&#8211;read-xinputrc</code></dt>
<dd> Determine the targeted Input Method from <i>$HOME/imsettings/xinputrc</i> or <i>$xinputrcdir/xinputrc</i> if not available.</dd>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> Show summary of options</dd>
<dt><i>Input Method name</i></dt>
<dd> Switch Input Method to <i>Input Method name</i>.</dd>
<dt><i>configuration filename</i></dt>
<dd> Switch Input Method to <i>configuration filename</i>.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-imsettings-list/">imsettings-list</a></code>(1) <code><a href="/docs/linux/man/1-imsettings-reload/">imsettings-reload</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Akira TAGOH &lt;akira [at] tagoh.org&gt; </p>
