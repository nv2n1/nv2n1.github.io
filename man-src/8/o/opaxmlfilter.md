---
title: "opaxmlfilter(8)"
name: "opaxmlfilter"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaxmlfilter/"
---

opaxmlfilter 

 

 

 Processes an XML file and removes all specified XML tags. The remaining tags are output and indentation can also be reformatted. opaxmlfilter is the opposite of opaxmlextract.

<h2>Syntax</h2>

opaxmlfilter [-t|-k] [-l] [-i <i>indent</i>] [-s <i>element</i>] [-P <i>param_file</i>] [ <i>input_file</i>]

<h2>Options</h2>

<dl><dt>-t
<dd>Trims leading and trailing whitespace in tag contents. 

<dt>-k
<dd>In tags with purely whitespace that contain newlines, keep newlines as-is. Default is to format as an empty list. 

<dt>-l
<dd>Adds comments with line numbers after each end tag. This can make comparison of resulting files easier since original line numbers are available. 

<dt>-i <i>indent</i>
<dd>Sets indentation to use per level. Default is 4. 

<dt>-s <i>element</i>
<dd>Name of the XML element to suppress. Can be used multiple times (in any order). 

<dt>-P <i>param_file</i>
<dd>Uses input command line options (parameters) from param_file. 

<dt>
&nbsp;<wbr><i>input_file</i>&nbsp;<wbr>
<dd>XML file to read. Default is stdin. 

</dl>
