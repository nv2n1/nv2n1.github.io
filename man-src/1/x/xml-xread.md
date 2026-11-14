---
title: "xml-xread(1)"
name: "xml-xread"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml-xread/"
description: "xml-xread – A simple command-line XML parsing application"
---

<h2 class="name">NAME</h2>
<p> xml-xread &#8211; A simple command-line XML parsing application</p>
<h2>SYNOPSIS</h2>
<p> <code>xml-xread</code> [options] document.xml </p>
<h2>DESCRIPTION</h2>
<p> <code>xml-xread</code> is a simple command-line XML Parser. It&#8217;s just a little wrapper around the JAXP XMLReader with support for catalogs. </p>
<p> The process ends with error-level 1, if there were errors. </p>
<h2>OPTIONS</h2>
<p> Command-line options are described below. </p>
<p> <code>-c</code> catalogfile</p>
<dl>
<dt>
<dd> Load a particular catalog file</dl>
<p> <code>-w</code></p>
<dl>
<dt>
<dd> Perform a well-formed parse, not a validating parse</dl>
<p> <code>-v</code> (default)</p>
<dl>
<dt>
<dd> Perform a validating parse</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Enable W3C XML Schema validation</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Perform a namespace-ignorant parse</dl>
<p> <code>-N</code> (default)</p>
<dl>
<dt>
<dd> Perform a namespace-aware parse</dl>
<p> <code>-d</code> integer</p>
<dl>
<dt>
<dd> Set the debug level. Warnings are shown if the debug level is &gt; 2</dl>
<p> <code>-E</code> integer</p>
<dl>
<dt>
<dd> Set the maximum number of errors to display</dl>
<h2>Index</h2>
