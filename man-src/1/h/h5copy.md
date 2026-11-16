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
</dt><dd> OBJECTS</dd>
<dt><code>-i</code>, <code>&#8211;input</code></dt>
<dd> input file name</dd>
<dt><code>-o</code>, <code>&#8211;output</code></dt>
<dd> output file name</dd>
<dt><code>-s</code>, <code>&#8211;source</code></dt>
<dd> source object name</dd>
<dt><code>-d</code>, <code>&#8211;destination</code></dt>
<dd> destination object name</dd>
<dt>
</dt><dd> OPTIONS</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print a usage message and exit</dd>
<dt><code>-p</code>, <code>&#8211;parents</code></dt>
<dd> No error if existing, make parent groups as needed</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print information about OBJECTS and OPTIONS</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version number and exit</dd>
<dt><code>-f</code>, <code>&#8211;flag</code></dt>
<dd> Flag type</dd>
<dt>
</dt><dd> Flag type is one of the following strings:</dd>
<dt>shallow</dt>
<dd> Copy only immediate members for groups</dd>
<dt>soft</dt>
<dd> Expand soft links into new objects</dd>
<dt>ext</dt>
<dd> Expand external links into new objects</dd>
<dt>ref</dt>
<dd> Copy references and any referenced objects, i.e., objects that the references point to.</dd>
<dt>
</dt><dd> Referenced objects are copied in addition to the objects</dd>
<dt>
</dt><dd> specified on the command line and reference datasets are populated with correct reference values. Copies of referenced datasets outside the copy range specified on the command line will normally have a different name from the original.</dd>
<dt>
</dt><dd> (Default:Without this option, reference value(s) in any</dd>
<dt>
</dt><dd> reference datasets are set to NULL and referenced objects are not copied unless they are otherwise within the copy range specified on the command line.)</dd>
<dt>noattr</dt>
<dd> Copy object without copying attributes</dd>
<dt>allflags</dt>
<dd> Switches all flags from the default to the non-default setting</dd>
<dt>
</dt><dd> These flag types correspond to the following API symbols</dd>
<dt>
</dt><dd> H5O_COPY_SHALLOW_HIERARCHY_FLAG H5O_COPY_EXPAND_SOFT_LINK_FLAG H5O_COPY_EXPAND_EXT_LINK_FLAG H5O_COPY_EXPAND_REFERENCE_FLAG H5O_COPY_WITHOUT_ATTR_FLAG H5O_COPY_ALL</dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>h5copy:</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>h5copy:</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info h5copy:</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
