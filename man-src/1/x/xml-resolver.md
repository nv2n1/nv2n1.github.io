---

title: "xml-resolver(1)"
name: "xml-resolver"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml-resolver/"
description: "xml-resolver – A simple command-line resolver"
---

<p> <code>xml-resolver</code> [options] keyword </p>
<p> <code>xml-resolver</code> is a simple command-line resolver. It takes some parameters and passes them through the resolver, printing the result. </p>
<p> The process ends with error-level 1, if there were errors. </p>
<h2>OPTIONS</h2>
<p> Command-line options are described below. </p>
<p> <code>-c</code> catalogfile</p>
<dl>
<dt>
</dt><dd> Load a particular catalog file</dd></dl>
<p> <code>-n</code> name</p>
<dl>
<dt>
</dt><dd> Sets the name</dd></dl>
<p> <code>-p</code> publicId</p>
<dl>
<dt>
</dt><dd> Sets the public identifier</dd></dl>
<p> <code>-s</code> systemId</p>
<dl>
<dt>
</dt><dd> Sets the system identifier</dd></dl>
<p> <code>-a</code></p>
<dl>
<dt>
</dt><dd> Absolute system URI</dd></dl>
<p> <code>-u</code> uri</p>
<dl>
<dt>
</dt><dd> Sets the URI</dd></dl>
<p> <code>-d</code> integer</p>
<dl>
<dt>
</dt><dd> Set the debug level</dd></dl>
<p> And keyword is one of: doctype, document, entity, notation, public, system, or uri. </p>
