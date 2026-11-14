---
title: "h5copy(1)"
name: "h5copy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5copy/"
description: "h5copy: – Copies HDF5 objects from a file to a new file"
---

<h2>NAME</h2>
<p> h5copy: &#8211; Copies HDF5 objects from a file to a new file</p>
<h2>DESCRIPTION</h2>
<p> usage: h5copy [OPTIONS] [OBJECTS&#8230;]</p>
<dl>
<dt>
<dd> OBJECTS</p>
<dt><code>-i</code>, <code>&#8211;input</code></p>
<dd> input file name</p>
<dt><code>-o</code>, <code>&#8211;output</code></p>
<dd> output file name</p>
<dt><code>-s</code>, <code>&#8211;source</code></p>
<dd> source object name</p>
<dt><code>-d</code>, <code>&#8211;destination</code></p>
<dd> destination object name</p>
<dt>
<dd> OPTIONS</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a usage message and exit</p>
<dt><code>-p</code>, <code>&#8211;parents</code></p>
<dd> No error if existing, make parent groups as needed</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print information about OBJECTS and OPTIONS</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version number and exit</p>
<dt><code>-f</code>, <code>&#8211;flag</code></p>
<dd> Flag type</p>
<dt>
<dd> Flag type is one of the following strings:</p>
<dt>shallow</p>
<dd> Copy only immediate members for groups</p>
<dt>soft</p>
<dd> Expand soft links into new objects</p>
<dt>ext</p>
<dd> Expand external links into new objects</p>
<dt>ref</p>
<dd> Copy references and any referenced objects, i.e., objects that the references point to.</p>
<dt>
<dd> Referenced objects are copied in addition to the objects</p>
<dt>
<dd> specified on the command line and reference datasets are populated with correct reference values. Copies of referenced datasets outside the copy range specified on the command line will normally have a different name from the original.</p>
<dt>
<dd> (Default:Without this option, reference value(s) in any</p>
<dt>
<dd> reference datasets are set to NULL and referenced objects are not copied unless they are otherwise within the copy range specified on the command line.)</p>
<dt>noattr</p>
<dd> Copy object without copying attributes</p>
<dt>allflags</p>
<dd> Switches all flags from the default to the non-default setting</p>
<dt>
<dd> These flag types correspond to the following API symbols</p>
<dt>
<dd> H5O_COPY_SHALLOW_HIERARCHY_FLAG H5O_COPY_EXPAND_SOFT_LINK_FLAG H5O_COPY_EXPAND_EXT_LINK_FLAG H5O_COPY_EXPAND_REFERENCE_FLAG H5O_COPY_WITHOUT_ATTR_FLAG H5O_COPY_ALL</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>h5copy:</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>h5copy:</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info h5copy:</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
