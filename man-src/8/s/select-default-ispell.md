---
title: "select-default-ispell(8)"
name: "select-default-ispell"
section: "8"
letter: "s"
url: "/docs/linux/man/8-select-default-ispell/"
---

<pre> select-default-ispell - select default ispell dictionary</pre>
<h2>Synopsis</h2>
<pre> select-default-ispell [options]
 Options (all long only options):
 --set-default='regexp' Try 'regexp' to get a single match and set
 it as default. Fail otherwise.
 --show-choices Show available choices to STDERR and exit.
 --debug Enable debug mode</pre>
<h2>Description</h2>
<p>This program is responsible for selecting default ispell dictionary. </p>
<p> If <code>&#8211;show-choices</code> is used will just output a list of available choices to <font SIZE="-1">STDERR</font> and exit. <font SIZE="-1">STDOUT</font> cannot be used, this program loads <code>debconf</code> and <code>debconf</code> captures <font SIZE="-1">STDOUT.</font> </p>
<p> If <code>&#8211;set-default</code> is used, program will try to get a single regexp match from available choices, failing if not. Will try case dependent match first, then case independent. </p>
<p> If <code>&#8211;set-default</code> is not used this program will make debconf always ask the shared question about the default ispell dictionary to be used in your system according to the installed ones. </p>
<p> In both cases, will do the appropriate settings if needed. </p>
<p> Calls internally <code>update-default-ispell</code>.</p>
<h2>See Also</h2>
<p>The dictionaries-common policy document</p>
<h2>Authors</h2>
<p>Rafael Laboissiere, Agustin Martin</p>
