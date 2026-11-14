---
title: "fd2pascal(1)"
name: "fd2pascal"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fd2pascal/"
description: "fd2pascal – Free Pascal forms description to pascal program converter"
---

<h2>NAME</h2>
<p> fd2pascal &#8211; Free Pascal forms description to pascal program converter </p>
<h2>SYNOPSIS</h2>
<p> <code>fd2pascal [-compensate] [-altformat] [-main] [-callback] filename</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>fd2pascal</code> reads a XForms designer file ( <i>.fd</i> ) and creates pascal code to create the form described in the file. The pascal code is written to a file with the same name as the input file, but with extension <i>.pp</i> if a file with that name already exists, then it will be renamed to a file with the extension <i>.bak</i> appended. </p>
<h2>OPTIONS</h2>
<p> fd2pascal has a small number of options to control its behaviour: </p>
<dl>
<dt><code>-altformat</code></p>
<dd> By default, a record type is emitted for the form definition, with a field for each widget (object) on the form. The alternate form declares a global variable for the form and each widget on the form.</p>
<dt><code>-compensate</code></p>
<dd> If this option is given then a call to fl_adjust_form_size is emitted after the form is created.</p>
<dt><code>-callback</code></p>
<dd> If this option is given, then a callback procedure is generated for each widget on the form.</p>
<dt><code>-main</code></p>
<dd> By default, a unit is created which can be included in the uses clause of a program. If this option is specified, a program file is emitted instead. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) </p>
</dl>
<h2>Index</h2>
