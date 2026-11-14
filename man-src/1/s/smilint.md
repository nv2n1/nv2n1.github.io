---
title: "smilint(1)"
name: "smilint"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smilint/"
description: "smilint – syntax and semantic checks of SMIv1/v2 and SPPI modules"
---

<h2>NAME</h2>
<p> smilint &#8211; syntax and semantic checks of SMIv1/v2 and SPPI modules</p>
<h2>SYNOPSIS</h2>
<p> <code>smilint</code> [ <code>-Vhersm</code> ] [ <code>-c </code><i>file</i> ] [ <code>-p </code><i>module</i> ] [ <code>-l </code><i>level</i> ] [ <code>-i </code><i>error-pattern</i> ] <i>module(s)</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>smilint</code> program is used to check MIB or PIB modules for syntax errors and semantics at some degree. SMIv1/v2 style MIB modules as well as SPPI PIB modules are supported. </p>
<p> The rules that <code>smilint</code> is based on are taken from RFC 1155, RFC 1212 and RFC 1215 for SMIv1, RFCs 2578-2580 for SMIv2, RFC 3159 for SPPI.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Show the smilint version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a help text and exit.</p>
<dt><code>-e, &#8211;error-list</code></p>
<dd> Show a list of all known error messages and exit. Error messages can have associated tags, shown in braces at the end of each line. The tags can be used with the -i option to ignore certain error messages.</p>
<dt><code>-r, &#8211;recursive</code></p>
<dd> Report errors and warnings also for recursively imported modules.</p>
<dt><code>-s, &#8211;severity</code></p>
<dd> Show the error severity in brackets before error messages.</p>
<dt><code>-m, &#8211;error-names</code></p>
<dd> Show the error names in braces before error messages.</p>
<dt><code>-c </code><i>file</i><code>, &#8211;config=</code><i>file</i></p>
<dd> Read <i>file</i> instead of any other (global and user) configuration file.</p>
<dt><code>-p </code><i>module</i><code>, &#8211;preload=</code><i>module</i></p>
<dd> Preload the module <i>module</i> before reading the main module(s). This may be helpful if an incomplete main module misses to import some definitions.</p>
<dt><code>-l </code><i>level</i><code>, &#8211;level=</code><i>level</i></p>
<dd> Report errors and warnings up to the given severity <i>level</i>. See below for a description of the error levels. The default error level is 3.</p>
<dt><code>-i </code><i>prefix</i><code>, &#8211;ignore=</code><i>prefix</i></p>
<dd> Ignore all errors that have a tag which matches <i>prefix</i>. A list of error tags can be retrieved by calling smilint with the -e option.</p>
<dt><i>module(s)</i></p>
<dd> These are the modules to be checked. If a module argument represents a path name (identified by containing at least one dot or slash character), this is assumed to be the exact file to read. Otherwise, if a module is identified by its plain module name, it is searched according to libsmi internal rules. See <code><a href="/docs/linux/man/3-smi_config/">smi_config</a>(3)</code> for more details.</dl>
<h2>ERROR AND WARNING LEVELS</h2>
<p> All generated error and warning messages have an associated severity level. The actual severity levels are:</p>
<dl>
<dt>0</p>
<dd> Internal error, no recovery possible. Examples are memory allocation failures. Errors of this level usually cause the application to abort.</p>
<dt>1</p>
<dd> Major SMI/SPPI error, recovery somehow possible but may lead to severe problems. Examples are lexically unexpected characters or unknown keywords. Errors of this kind usually lead to follow-on errors.</p>
<dt>2</p>
<dd> SMI/SPPI error which is probably tolerated by some implementations. Examples are MIB/PIB modules which mix constructs from different SMI/SPPI versions.</p>
<dt>3</p>
<dd> SMI/SPPI error which is likely tolerated by many implementations. Examples are misplaced SMIv2 MODULE-IDENTITY invocations or SMIv2 textual conventions derived from other textual conventions.</p>
<dt>4</p>
<dd> Something which is not strictly an error but which is recommended to be changed. Warnings of this level are usually considered during MIB reviews.</p>
<dt>5</p>
<dd> Something that is basically correct but might be problematic in certain environments or usage scenarios. Examples are warnings that identifiers only differ in case or that type definitions are not used within the defining module.</p>
<dt>6</p>
<dd> Messages of this level are auxiliary notices. Examples are messages that point to a previous definition in case of a redefinition.</dl>
<p> Higher levels are currently not used and lead to the same effects as level 6 does. Note that errors up to level 3 are errors violating the specifications and must be fixed by the responsible author. The warnings generated with level 4 should be considered during normal MIB/PIB reviews.</p>
<h2>EXAMPLE</h2>
<p> This example checks the file RMON2-MIB in the current directory (note that the `./&#8217; prefix ensures this). The error level is raised to 6 and warnings that claim about identifier names that exceed a length of 32 characters are suppressed. </p>
<pre>
  $ smilint -l 6 -i namelength-32 ./RMON2-MIB
  ./RMON2-MIB:3935: unexpected type restriction
  ./RMON2-MIB:3936: unexpected type restriction
  ./RMON2-MIB:3937: unexpected type restriction
  ./RMON2-MIB:3938: unexpected type restriction
  ./RMON2-MIB:3939: unexpected type restriction
  ./RMON2-MIB:3940: unexpected type restriction
  ./RMON2-MIB:4164: scalar object must not have a `read-create' access value
</pre>
<h2>SEE ALSO</h2>
<p> The <code><a href="/docs/linux/man/3-libsmi/">libsmi</a></code>(3) project is documented at <code><a rel="nofollow" href="http://www.ibr.cs.tu-bs.de/projects/libsmi/">http://www.ibr.cs.tu-bs.de/projects/libsmi/</a></code>. Other commonly used MIB checkers are <code><a href="/docs/linux/man/1-mosy/">mosy</a></code>(1) and <code><a href="/docs/linux/man/1-smicng/">smicng</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> (C) 1999-2004 F. Strauss, TU Braunschweig, Germany &lt;strauss [at] ibr.cs.tu-bs.de&gt;<br />
 (C) 1999-2002 J. Schoenwaelder, TU Braunschweig, Germany &lt;schoenw [at] ibr.cs.tu-bs.de&gt;<br />
 (C) 2002-2003 J. Schoenwaelder, University of Osnabrueck, Germany<br />
 (C) 2003-2004 J. Schoenwaelder, International University Bremen, Germany<br />
 (C) 2001-2002 T. Klie, TU Braunschweig, Germany &lt;tklie [at] ibr.cs.tu-bs.de&gt;<br />
 (C) 2002 M. Bunkus, TU Braunschweig, Germany &lt;bunkus [at] ibr.cs.tu-bs.de&gt;<br />
 and contributions by many other people. </p>
<h2>Index</h2>
