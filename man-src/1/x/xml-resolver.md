---
title: "xml-resolver(1)"
name: "xml-resolver"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml-resolver/"
description: "xml-resolver – A simple command-line resolver"
---

<h2 class="name">NAME</h2>
<p> xml-resolver &#8211; A simple command-line resolver</p>
<h2>SYNOPSIS</h2>
<p> <code>xml-resolver</code> [options] keyword </p>
<h2>DESCRIPTION</h2>
<p> <code>xml-resolver</code> is a simple command-line resolver. It takes some parameters and passes them through the resolver, printing the result. </p>
<p> The process ends with error-level 1, if there were errors. </p>
<h2>OPTIONS</h2>
<p> Command-line options are described below. </p>
<p> <code>-c</code> catalogfile</p>
<dl>
<dt>
<dd> Load a particular catalog file</dl>
<p> <code>-n</code> name</p>
<dl>
<dt>
<dd> Sets the name</dl>
<p> <code>-p</code> publicId</p>
<dl>
<dt>
<dd> Sets the public identifier</dl>
<p> <code>-s</code> systemId</p>
<dl>
<dt>
<dd> Sets the system identifier</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Absolute system URI</dl>
<p> <code>-u</code> uri</p>
<dl>
<dt>
<dd> Sets the URI</dl>
<p> <code>-d</code> integer</p>
<dl>
<dt>
<dd> Set the debug level</dl>
<p> And keyword is one of: doctype, document, entity, notation, public, system, or uri. </p>
<h2>Index</h2>
