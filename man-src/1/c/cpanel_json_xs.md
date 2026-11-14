---
title: "cpanel_json_xs(1)"
name: "cpanel_json_xs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpanel_json_xs/"
---

<h2 class="name">NAME</h2>
 

 cpanel_json_xs - Cpanel::JSON::XS commandline utility 

<h2>SYNOPSIS</h2>

 <pre><code>
cpanel_json_xs[-v][-f inputformat][-t outputformat]
</code></pre>

<h2>DESCRIPTION</h2>

 <i>cpanel_json_xs</i> converts between some input and output formats (one of them is <font SIZE="-1">JSON</font>). 

 The default input format is <tt>&quot;json&quot;</tt> and the default output format is <tt>&quot;json-pretty&quot;</tt>.

<h2>OPTIONS</h2>

<dl>
<dt>-v
<dd> Be slightly more verbose.
<dt>-f fromformat
<dd> Read a file in the given format from <font SIZE="-1">STDIN.</font> 

 <tt>&quot;fromformat&quot;</tt> can be one of:
<dl>
<dt>
<dd>
<dl>
<dt>json - a json text encoded, either utf-8, utf16-be/le, utf32-be/le
<dd>
<dt>storable - a Storable frozen value
<dd>
<dt>storable-file - a Storable file (Storable has two incompatible formats)
<dd>
<dt>bencode - use Convert::Bencode, if available (used by torrent files, among others)
<dd>
<dt>clzf - Compress::LZF format (requires that module to be installed)
<dd>
<dt>eval - evaluate the given code as (non-utf-8) Perl, basically the reverse of &quot;-t dump&quot;
<dd>
<dt>yaml - <font SIZE="-1">YAML </font>(avoid at all costs, requires the <font SIZE="-1">YAML</font> module :)
<dd>
<dt>string - do not attempt to decode the file data
<dd>
<dt>none - nothing is read, creates an &quot;undef&quot; scalar - mainly useful with &quot;-e&quot;
<dd></dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>-t toformat
<dd> Write the file in the given format to <font SIZE="-1">STDOUT.</font> 

 <tt>&quot;toformat&quot;</tt> can be one of:
<dl>
<dt>
<dd>
<dl>
<dt>json, json-utf-8 - json, utf-8 encoded
<dd>
<dt>json-pretty - as above, but pretty-printed
<dd>
<dt>json-utf-16le, json-utf-16be - little endian/big endian utf-16
<dd>
<dt>json-utf-32le, json-utf-32be - little endian/big endian utf-32
<dd>
<dt>storable - a Storable frozen value in network format
<dd>
<dt>storable-file - a Storable file in network format (Storable has two incompatible formats)
<dd>
<dt>bencode - use Convert::Bencode, if available (used by torrent files, among others)
<dd>
<dt>clzf - Compress::LZF format
<dd>
<dt>yaml - <font SIZE="-1">YAML</font>
<dd>
<dt>dump - Data::Dump
<dd>
<dt>dumper - Data::Dumper
<dd>
<dt>string - writes the data out as if it were a string
<dd>
<dt>none - nothing gets written, mainly useful together with &quot;-e&quot;
<dd> Note that Data::Dumper doesn't handle self-referential data structures correctly - use ``dump'' instead.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>-e code
<dd> Evaluate perl code after reading the data and before writing it out again - can be used to filter, create or extract data. The data that has been written is in <tt>$_</tt>, and whatever is in there is written out afterwards.</dl>

<h2>EXAMPLES</h2>

 <pre>
   cpanel_json_xs -t none &lt;isitreally.json
</pre> 

 ``<font SIZE="-1">JSON</font> Lint'' - tries to parse the file <i>isitreally.json</i> as <font SIZE="-1">JSON -</font> if it is valid <font SIZE="-1">JSON,</font> the command outputs nothing, otherwise it will print an error message and exit with non-zero exit status. 

 <pre>
   &lt;src.json cpanel_json_xs &gt;pretty.json
</pre> 

 Prettify the <font SIZE="-1">JSON</font> file <i>src.json</i> to <i>dst.json</i>. 

 <pre>
   cpanel_json_xs -f storable-file &lt;file
</pre> 

 Read the serialised Storable file <i>file</i> and print a human-readable <font SIZE="-1">JSON</font> version of it to <font SIZE="-1">STDOUT.</font> 

 <pre>
   cpanel_json_xs -f storable-file -t yaml &lt;file
</pre> 

 Same as above, but write <font SIZE="-1">YAML</font> instead (not using <font SIZE="-1">JSON</font> at all :) 

 <pre>
   cpanel_json_xs -f none -e '$_ = [1, 2, 3]'
</pre> 

 Dump the perl array as <font SIZE="-1">UTF-8</font> encoded <font SIZE="-1">JSON</font> text. 

 <pre><code>
   &lt;torrentfile cpanel_json_xs -f bencode -e '$_ = join "\n", map @$_, @{$_-&gt;{"announce-list"}}' -t string
</code></pre> 

 Print the tracker list inside a torrent file. 

 <pre>
   lwp-request <a rel="nofollow" HREF="http://cpantesters.perl.org/show/JSON-XS.json">http://cpantesters.perl.org/show/JSON-XS.json</a> | cpanel_json_xs
</pre> 

 Fetch the cpan-testers result summary <tt>&quot;Cpanel::JSON::XS&quot;</tt> and pretty-print it.

<h2>AUTHOR</h2>

 Copyright (C) 2008 Marc Lehmann &lt;json [at] schmorp.de&gt; 

<h2>Index</h2>


