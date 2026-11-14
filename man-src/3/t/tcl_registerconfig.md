---
title: "tcl_registerconfig(3)"
name: "tcl_registerconfig"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_registerconfig/"
description: "Tcl_RegisterConfig – procedures to register embedded configuration information"
---

<p>Tcl_RegisterConfig &#8211; procedures to register embedded configuration information </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_RegisterConfig</code>(<i>interp, pkgName, configuration, valEncoding</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Refers to the interpreter the embedded configuration information is registered for. Must not be NULL.</p>
<dd>const char <i>*pkgName</i> (in) Contains the name of the package registering the embedded configuration as ASCII string. This means that this information is in UTF-8 too. Must not be NULL.</p>
<dd>Tcl_Config <i>*configuration</i> (in) Refers to an array of Tcl_Config entries containing the information embedded in the binary library. Must not be NULL. The end of the array is signaled by either a key identical to NULL, or a key referring to the empty string.</p>
<dd>const char <i>*valEncoding</i> (in) Contains the name of the encoding used to store the configuration values as ASCII string. This means that this information is in UTF-8 too. Must not be NULL. </p>
</dl>
<h2>Description</h2>
<p>The function described here has its base in TIP 59 and provides extensions with support for the embedding of configuration information into their binary library and the generation of a Tcl-level interface for querying this information. </p>
<p> To embed configuration information into their binary library an extension has to define a non-volatile array of Tcl_Config entries in one if its source files and then call <code>Tcl_RegisterConfig</code> to register that information. </p>
<p> <code>Tcl_RegisterConfig</code> takes four arguments; first, a reference to the interpreter we are registering the information with, second, the name of the package registering its configuration information, third, a pointer to an array of structures, and fourth a string declaring the encoding used by the configuration values. </p>
<p> The string <i>valEncoding</i> contains the name of an encoding known to Tcl. All these names are use only characters in the ASCII subset of UTF-8 and are thus implicitly in the UTF-8 encoding. It is expected that keys are legible English text and therefore using the ASCII subset of UTF-8. In other words, they are expected to be in UTF-8 too. The values associated with the keys can be any string however. For these the contents of <i>valEncoding</i> define which encoding was used to represent the characters of the strings. </p>
<p> Each element of the <i>configuration</i> array refers to two strings containing the key and the value associated with that key. The end of the array is signaled by either an empty key or a key identical to NULL. The function makes <code>no</code> copy of the <i>configuration</i> array. This means that the caller has to make sure that the memory holding this array is never released. This is the meaning behind the word <code>non-volatile</code> used earlier. The easiest way to accomplish this is to define a global static array of Tcl_Config entries. See the file &#8220;generic/tclPkgConfig.c&#8221; in the sources of the Tcl core for an example. </p>
<p> When called <code>Tcl_RegisterConfig</code> will</p>
<dl COMPACT>
<dt>(1)</p>
<dd>create a namespace having the provided <i>pkgName</i>, if not yet existing.</p>
<dt>(2)</p>
<dd>create the command <code>pkgconfig</code> in that namespace and link it to the provided information so that the keys from _configuration_ and their associated values can be retrieved through calls to <code>pkgconfig</code>.</dl>
<p> The command <code>pkgconfig</code> will provide two subcommands, <code>list</code> and <code>get</code>:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>::<i>pkgName</i>::<code>pkgconfig</code> list</p>
<dd>Returns a list containing the names of all defined keys.</p>
<dt>::<i>pkgName</i>::<code>pkgconfig</code> get <i>key</i></p>
<dd>Returns the configuration value associated with the specified <i>key</i>.</dl>
</dl>
<h2>Tcl_Config</h2>
<p>The <code>Tcl_Config</code> structure contains the following fields: </p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_Config {
 const char* key;
 const char* value;
} Tcl_Config;</pre>
</dl>
<h2>Keywords</h2>
<p>embedding, configuration, binary library</p>
