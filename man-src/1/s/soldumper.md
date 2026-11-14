---
title: "soldumper(1)"
name: "soldumper"
section: "1"
letter: "s"
url: "/docs/linux/man/1-soldumper/"
---

<h2>NAME</h2>

 soldumper - Gnash Local Shared Object (LSO) File Dumper

<h2>Synopsis</h2>

 <pre>
soldumper (options)... (file)...
</pre>

<h2>DESCRIPTION</h2>

 Dump information about the .sol files used by the SharedObject ActionScript class. 

 When a SWF player, including Gnash, plays a SWF &quot;movie&quot;, the movie can contain scripts. These scripts can call ActionScript classes. One such class is SharedObject. SharedObject creates shared objects, which end up stored in your computer's file system. For example, a SWF game might store its score file in a SharedObject; or a privacy-invading SWF movie might store &quot;cookies&quot; in a SharedObject. Before soldumper was written, these bits of stored information were hard for users to notice or investigate. Soldumper prints these files, which are comprised of a header, and a collection of SWF AMF Objects that the movie has written in the shared object file.
<dl>
<dt>-h
<dd> Print usage info.
<dt>-l
<dd> List all the .sol files in the default path.
<dt>-f
<dd> Ignore the global setting, use the current directory for files.
<dt>-v
<dd> Verbose output. 

</dl>

<h2>Index</h2>


