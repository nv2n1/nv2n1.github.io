---

title: "derb(1)"
name: "derb"
section: "1"
letter: "d"
url: "/docs/linux/man/1-derb/"
description: "derb – disassemble a resource bundle"
---

<p> <code>derb</code> &#8211; disassemble a resource bundle </p>
<p> <code>derb</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-e</code>, <code>&#8211;encoding</code><i> encoding</i> ] [ <code>&#8211;bom</code> ] [ <code>-t</code>, <code>&#8211;truncate</code><i> </i>[ size ] ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] [ <code>-c</code>, <code>&#8211;to-stdout</code> ] <i>bundle</i> &#8230;</p>
<p> <code>derb</code> reads the compiled resource <i>bundle</i> files passed on the command line and write them back in text form. The resulting text files have a <code>.txt</code> extension while compiled resource bundle source files typically have a <code>.res</code> extension. </p>
<p> It is customary to name the resource bundles by their locale name, i.e. to use a local identifier for the <i>bundle</i> filename, e.g. <code>ja_JP.res</code> for Japanese (Japan) data, or <code>root.res</code> for the root bundle. This is especially important for <code>derb</code> since the locale name is not accessible directly from the compiled resource bundle, and to know which locale to ask for when opening the bundle. <code>derb</code> will produce a file whose base name is the base name of the compiled resource file itself. If the <code>&#8211;to-stdout</code>, <code>-c</code> option is used, however, the text will be written on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></dt>
<dd> Print help about usage and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version of <code>derb</code> and exit.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display extra informative messages during execution.</dd>
<dt><code>-A</code>, <code>&#8211;suppressAliases</code></dt>
<dd> Don&#8217;t follow aliases when producing output.</dd>
<dt><code>-e</code>, <code>&#8211;encoding</code><i> encoding</i></dt>
<dd> Set the encoding used to write output files to <i>encoding</i>. The default encoding is the invariant (subset of ASCII or EBCDIC) codepage for the system (see section <code>INVARIANT CHARACTERS</code>). The choice of the encoding does not affect the data, just their representation. Characters that cannot be represented in the <i>encoding</i> will be represented using <code></code> <code>\u</code><i>hhhh</i> escape sequences.  </dd>
<dt><code>--bom</code> </dt>
<dd>  Write a byte order mark (BOM) at the beginning of the file.  </dd>
<dt><code>-l</code>, <code>--locale</code><i> locale</i> </dt>
<dd>  Set the <i>locale</i> for the resource bundle, which is used both in the generated text and as the base name of the output file.  </dd>
<dt><code>-t</code>, <code>--truncate</code><i> </i>[ size ] </dt>
<dd>  Truncate individual resources (strings or binary data) to <i>size</i> bytes. The default if <i>size</i> is not specified is <code>80</code> bytes.  </dd>
<dt><code>-s</code>, <code>--sourcedir</code><i> source</i> </dt>
<dd>  Set the source directory to <i>source</i>. The default source directory is the current directory. If <code>-</code> is passed for <i>source</i>, then the <i>bundle</i> will be looked for in its default location, specified by the <code>ICU_DATA</code> environment variable (or defaulting to the location set when ICU was built if <code>ICU_DATA</code> is not set).  </dd>
<dt><code>-d</code>, <code>--destdir</code><i> destination</i> </dt>
<dd>  Set the destination directory to <i>destination</i>. The default destination directory is specified by the environment variable <code>ICU_DATA</code> or is the location set when ICU was built if <code>ICU_DATA</code> is not set.  </dd>
<dt><code>-i</code>, <code>--icudatadir</code><i> directory</i> </dt>
<dd>  Look for any necessary ICU data files in <i>directory</i>. For example, when processing collation overrides, the file <code>ucadata.dat</code> must be located. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>.  </dd>
<dt><code>-c</code>, <code>--to-stdout</code> </dt>
<dd>  Write the disassembled <i>bundle</i> on standard output instead of into a file.  </dd></dl>
  <h2>CAVEATS</h2>
 When the option <code>--bom</code> is used, the character <code>U+FEFF</code> is written in the destination <i>encoding</i> regardless of whether it is a Unicode transformation format (UTF) or not. This option should only be used with an UTF encoding, as byte order marks are not meaningful for other encodings.  <h2>INVARIANT CHARACTERS</h2>
 The <code>invariant character set</code> consists of the following set of characters, expressed as a standard POSIX regular expression: <code>[a-z]|[A-Z]|[0-9]|_| |+|-|*|/</code>. This is the set which is guaranteed to be available regardless of code page.  <h2>ENVIRONMENT</h2>
 <dl>
 <dt><code>ICU_DATA</code> </dt>
<dd>  Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.  </dd></dl>
  <h2>AUTHORS</h2>
 Vladimir Weinstein <br />
 Yves Arrouye  <h2>VERSION</h2>
 1.0  <h2>COPYRIGHT</h2>
 Copyright (C) 2002 IBM, Inc. and others.  <h2>SEE ALSO</h2>
 <code><a href="/docs/linux/man/1-genrb/">genrb</a></code>(1) 
