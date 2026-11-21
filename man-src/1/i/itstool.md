---
title: "itstool(1)"
name: "itstool"
section: "1"
letter: "i"
url: "/docs/linux/man/1-itstool/"
description: "itstool – convert between XML and PO using ITS"
---

<h2>SYNOPSIS</h2>
<p> itstool [OPTIONS] XMLFILES&#8230;<br />
 itstool <code>-m</code> &lt;MOFILE&gt; [OPTIONS] XMLFILES&#8230;<br />
 itstool <code>-j</code> &lt;XMLFILE&gt; [OPTIONS] MOFILES&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>itstool </code> extracts messages from XML files and outputs PO template files, then merges translations from MO files to create translated XML files. It determines what to translate and how to chunk it into messages using the W3C Internationalization Tag Set (ITS). </p>
<p> To extract messages from XML files <code>XMLFILES</code> and output them to <code>OUT.pot</code>: </p>
<p> <code>itstool -o OUT.pot XMLFILES</code> </p>
<p> After merging with existing translations or translating strings, generate an MO file with <code><a href="/docs/linux/man/1-msgfmt/">msgfmt</a>(1)</code>, then output translated files to the directory <code>DIR</code>: </p>
<p> <code>itstool -m OUT.mo -o DIR XMLFILES</code> </p>
<p> You can also create a single multilingual XML output file using an input XML file and a set of MO files: </p>
<p> <code>itstool -j FILE.xml -o OUT.xml MOFILES</code> </p>
<p> ITS definitions are loaded from the built-in rules, rules embedded in the source XML files, files passed with the <code>-i</code> option, and ITS attributes in the source XML files. Later definitions take precedence. You can disable built-in rules by passing the <code>-n</code> option. </p>
<h2>OPTIONS</h2>
<h3>Extracting</h3>
<dl>
<dt><code>-o </code><i>OUT.pot</i></dt>
<dd>
</dd><dt><code>&#8211;out </code><i>OUT.pot</i></dt>
<dd> output PO template to the file <code>OUT.pot</code> </dd>
</dl>
<h3>Merging</h3>
<dl>
<dt><code>-m </code><i>MOFILE</i> <i>XMLFILES</i></dt>
<dd>
</dd><dt><code>&#8211;merge </code><i>MOFILE</i> <i>XMLFILES</i></dt>
<dd> merge from an MO file <code>MOFILE</code> and output translated XML files for source <code>XMLFILES</code> </dd>
<dt><code>-l </code><i>LANG</i></dt>
<dd>
</dd><dt><code>&#8211;lang </code><i>LANG </i></dt>
<dd> explicitly set the language code output to XML </dd>
<dt><code>-o </code><i>OUT</i></dt>
<dd>
</dd><dt><code>&#8211;out </code><i>OUT </i></dt>
<dd> output XML files in the directory <code>OUT</code> </dd>
</dl>
<h3>Joining</h3>
<dl>
<dt><code>-j </code>MLIFILE <i>MOFILES</i></dt>
<dd>
</dd><dt><code>&#8211;join </code><i>XMLFILE</i> <i>MOFILES</i></dt>
<dd> join translations from <code>MOFILES</code> into a multilingual file based on source <code>XMLFILE</code> </dd>
<dt><code>-o </code><i>OUT.xml</i></dt>
<dd>
</dd><dt><code>&#8211;out </code><i>OUT.xml</i></dt>
<dd> output to the XML file <code>OUT.xml</code> </dd>
</dl>
<h3>Common</h3>
<dl>
<dt><code>-i </code><i>ITS</i></dt>
<dd>
</dd><dt><code>&#8211;its </code><i>ITS</i></dt>
<dd> load the ITS rules in the file <code>ITS</code> (can specify multiple times) </dd>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>&#8211;no-builtins</code></dt>
<dd> do not apply the built-in ITS rules that ship with itstool </dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;strict</code></dt>
<dd> exit with error when PO files contain broken XML </dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;load-dtd</code></dt>
<dd> load external DTDs used by input XML files </dd>
<dt><code>-k</code></dt>
<dd>
</dd><dt><code>&#8211;keep-entities</code></dt>
<dd> keep entity references unexpanded in PO files </dd>
<dt><code>-p </code><i>NAME VALUE</i></dt>
<dd>
</dd><dt><code>&#8211;param </code><i>NAME VALUE</i></dt>
<dd> define ITS parameter <code>NAME</code> to the value <code>VALUE</code> (can specify multiple times) </dd>
</dl>
<h2>AUTHOR</h2>
<p> Shaun McCance &lt;shaunm [at] gnome.org&gt; </p>
<h2>SEE ALSO</h2>
<p> More documentation for <code>itstool</code> is maintained online. For more information, see: </p>
<p> <code><a rel="nofollow" href="http://itstool.org/documentation/">http://itstool.org/documentation/</a></code> </p>
