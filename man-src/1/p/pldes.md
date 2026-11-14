---
title: "pldes(1)"
name: "pldes"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pldes/"
---

<h2>NAME</h2>

 pl, pldes, plser, plmerge, plparse, pl2link<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>- property list tools

<h2>SYNOPSIS</h2>

 <pre><code>
pldes filename(s)
plget key[morekeys] plser filename(s)
    plmerge[destination - file][input - file(s)] plparse filename(s)
pl2link input - file[destination - file] pl - input[input - file] - output[destination - file]
</code></pre>

<h2>DESCRIPTION</h2>

 

 Property lists in GNUstep are hierarchical lists of values or attribute-value pairs. Programmatically they are represented by instances of the NSString, NSData, NSArray, or NSDictionary (most common) class (which may contain other instances of such classes). These instances can be serialized as binary objects to form a persistent representation. In addition, there are two alternative human-readable representations. The first, utilized in NeXTstep and OpenStep, utilizes a text format with equals signs expressing attribute-value bindings and set braces expressing hierarchical organization. The second, often (uninformatively) referred to as &quot;plist&quot; format, is in XML and is used by Mac OS X. The tools described here are utilities for manipulating the various persistent property list representations as files.
<dl>
<dt><b>pldes</b> <i>filename(s)</i>
<dd> Converts a binary serialised property list (class instance) to a text representation.
<dt><b>plget</b> <i>key</i>
<dd> Reads a text representation of a dictionary in property list format as standard input, extracts the string value held in that dictionary with the specified key, and writes the result to standard output. Multiple keys may be used to extract values from nested dictionaries.
<dt><b>plser</b> <i>filename(s)</i>
<dd> Converts a text representation of a property list to a binary serialized representation.
<dt><b>plmerge</b> [ <i>destination-file</i> ] [ <i>input-file(s)</i> ]
<dd> Merges text property lists into a single property list
<dt><b>plparse</b> <i>filename(s)</i>
<dd> Checks that each file contains a valid text representation of a property list.
<dt><b>pl2link</b> <i>input-file</i> [ <i>destination-file</i> ]
<dd> Produces a desktop link file for KDE and Gnome for the given text representation of a property list.
<dt><b>pl</b> <i>-input</i> [ <i>input-file</i> ]
<dd> Takes the serialized plist represented by input-file and outputs it to standard output.
<dt><b>pl</b> <i>-output</i> [ <i>destination-file</i> ]
<dd> Takes a plist from standard input and serializes it into destination-file.</dl>
 

 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-defaults/">defaults</a>(1) 

<h2>HISTORY</h2>

 Written 1999-2000. 

 This manual page first appeared in gnustep-base 1.9.2 (March 2004). 

<h2>AUTHORS</h2>

 <b>pldes, plget, plparse, plser</b> were written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt;. 

 <b>plmerge</b> was written by Jonathan Gapen &lt;jagapen [at] whitewater.chem.wisc.edu&gt;. 

 <b>pl2link</b> was written by Fred Kiefer &lt;FredKiefer [at] gmx.de&gt;. 

 <b>pl</b> was written by Gregory Casamento &lt;greg_casamento [at] yahoo.com&gt;. 

<h2>Index</h2>


