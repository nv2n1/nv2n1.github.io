---
title: "po2debconf(1)"
name: "po2debconf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-po2debconf/"
description: "po2debconf – merge master templates file and PO files"
---

<h2 class="name">NAME</h2>
<p> po2debconf &#8211; merge master templates file and PO files </p>
<h2>SYNOPSIS</h2>
<p> <code>po2debconf</code> [<code>-v</code>] [<code>-h</code>] [<code>&#8211;podir=</code><font SIZE="-1">DIR</font>] [<code>-o </code><font SIZE="-1">FILE</font>] [<code>-e </code><font SIZE="-1">STRING</font>] <i>master</i></p>
<h2>DESCRIPTION</h2>
<p> This program reads all <font SIZE="-1">PO</font> files and a single <i>templates</i> file, and produces a Debconf templates file containing all translations, similar to the one produced by <code><a href="/docs/linux/man/1-debconf-mergetemplate/">debconf-mergetemplate</a></code>(1) (from the <tt>&quot;debconf-utils&quot;</tt> package). <font SIZE="-1">PO</font> files are by default searched in the <i>po</i> subdirectory below the location of the master file. </p>
<p> To help the language code transition for Norwegian Bokmål, the <code>no</code> and <code>nb</code> language codes are handled specially. If <i>no.po</i> exists, it should be renamed to <i>nb.po</i>. Using <i>nb.po</i> will make both <tt>&quot;-no&quot;</tt> and <tt>&quot;-nb&quot;</tt> translations available in the templates file. </p>
<p> Lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are comments in templates files. They are useful to give hints to translators, and are discarded by <code>po2debconf</code>. Special comments have been introduced in <tt>&quot;po-debconf&quot;</tt> 1.0. They are in the form <tt>&quot;#flag:</tt>directive<tt>&quot;</tt>. The <tt>&quot;#flag:partial&quot;</tt> is the only directive interpreted by <code>po2debconf</code>. Normally when a field is composed of several paragraphs (like <tt>&quot;__Choices&quot;</tt> and <tt>&quot;_Description&quot;</tt>), it is translated if all paragraphs are translated. When a field contains <tt>&quot;#flag:partial&quot;</tt>, translated strings may be mixed with untranslated strings.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a usage summary and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Process in verbose mode.</p>
<dt><code>&#8211;podir=</code><font SIZE="-1">DIR</font></p>
<dd> Set directory for <font SIZE="-1">PO</font> files. Default is to search <font SIZE="-1">PO</font> files in the <i>po</i> subdirectory below the location of the master file.</p>
<dt><code>-o</code>, <code>&#8211;output=</code><font SIZE="-1">FILE</font></p>
<dd> Set output filename (default is standard output).</p>
<dt><code>-e</code>, <code>&#8211;encoding=</code><font SIZE="-1">STRING</font></p>
<dd> Convert encoding. Argument can take 3 values: <tt>&quot;utf8&quot;</tt> (convert to <font SIZE="-1">UTF-8</font>), <tt>&quot;po&quot;</tt> (do not change encoding) and <tt>&quot;popular&quot;</tt> (convert encoding of input files depending on their language; the <tt>&quot;PODEBCONF_ENCODINGS&quot;</tt> environment variable must point to a name of a file containing the encoding map). </p>
<p> Such a filename looks like: </p>
<pre>
  #
  #   Number is comment sign
  #
  cs       ISO-8859-2
  da       ISO-8859-1
  de       ISO-8859-1
  el       ISO-8859-7
</pre>
<p> etc. </p>
<p> Default encoding used to be <tt>&quot;popular&quot;</tt>, and has been switched to <tt>&quot;utf8&quot;</tt> since po-debconf 0.9.0.</dl>
<h2>OUTPUT FORMAT</h2>
<p> Since debconf 1.2.0, templates format has changed, encoding is part of field names, i.e. they are <tt>&quot;foo-</tt>lang<tt>.</tt>encoding<tt>&quot;</tt>. When older debconf encounter such fields, they are silently ignored, which means that original text is displayed. </p>
<p> If present, a <i>po/output</i> file can override defaults for encoding and output format. It contains a single line with two fields. The first field is the output format (currently valid values are 1 for fields in the form <tt>&quot;foo-</tt>lang<tt>&quot;</tt>, and 2 for <tt>&quot;foo-</tt>lang<tt>.</tt>encoding<tt>&quot;</tt>) and the second field is the encoding, e.g. </p>
<pre>
   echo '2 utf8' &gt; po/output
</pre>
<p> let <code>po2debconf</code> convert text to <font SIZE="-1">UTF-8.</font> </p>
<p> When encoding is set to <tt>&quot;po&quot;</tt> or <tt>&quot;utf8&quot;</tt>, output format is always set to 2, so that older debconf do not try to display text with wrong encodings.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debconf-gettextize/">debconf-gettextize</a></code>(1), <code><a href="/docs/linux/man/1-debconf-updatepo/">debconf-updatepo</a></code>(1), <code><a href="/docs/linux/man/7-po-debconf/">po-debconf</a></code>(7).</p>
<h2>AUTHOR</h2>
<pre>
  Denis Barbier &lt;barbier [at] linuxfr.org&gt;
</pre>
<h2>Index</h2>
