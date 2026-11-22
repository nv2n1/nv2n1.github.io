---

title: "json_xs(1)"
name: "json_xs"
section: "1"
letter: "j"
url: "/docs/linux/man/1-json_xs/"
---

json_xs - JSON::XS commandline utility 

<h2>SYNOPSIS</h2>

 <pre><code>
json_xs[-v][-f inputformat][-t outputformat]
</code></pre>

<h2>DESCRIPTION</h2>

 <i>json_xs</i> converts between some input and output formats (one of them is JSON). 

 The default input format is <tt>&quot;json&quot;</tt> and the default output format is <tt>&quot;json-pretty&quot;</tt>.

<h2>OPTIONS</h2>

<dl>
<dt>-v
</dt><dd> Be slightly more verbose.
</dd><dt>-f fromformat
</dt><dd> Read a file in the given format from STDIN. 
 <tt>&quot;fromformat&quot;</tt> can be one of:
</dd><dl>
<dl>
<dt>json - a json text encoded, either utf-8, utf16-be/le, utf32-be/le
</dt><dd>
</dd><dt>cbor - CBOR (RFC 7049, CBOR::XS), a kind of binary JSON
</dt><dd>
</dd><dt>storable - a Storable frozen value
</dt><dd>
</dd><dt>storable-file - a Storable file (Storable has two incompatible formats)
</dt><dd>
</dd><dt>bencode - use Convert::Bencode, if available (used by torrent files, among others)
</dt><dd>
</dd><dt>clzf - Compress::LZF format (requires that module to be installed)
</dt><dd>
</dd><dt>eval - evaluate the given code as (non-utf-8) Perl, basically the reverse of &quot;-t dump&quot;
</dt><dd>
</dd><dt>yaml - YAML (avoid at all costs, requires the YAML module :)
</dt><dd>
</dd><dt>string - do not attempt to decode the file data
</dt><dd>
</dd><dt>none - nothing is read, creates an &quot;undef&quot; scalar - mainly useful with &quot;-e&quot;
</dt><dd></dd></dl>
</dl>

<dl>
</dl>

<dt>-t toformat
</dt><dd> Write the file in the given format to STDOUT. 

 <tt>&quot;toformat&quot;</tt> can be one of:
</dd><dl>
<dl>
<dt>json, json-utf-8 - json, utf-8 encoded
</dt><dd>
</dd><dt>json-pretty - as above, but pretty-printed
</dt><dd>
</dd><dt>json-utf-16le, json-utf-16be - little endian/big endian utf-16
</dt><dd>
</dd><dt>json-utf-32le, json-utf-32be - little endian/big endian utf-32
</dt><dd>
</dd><dt>cbor - CBOR (RFC 7049, CBOR::XS), a kind of binary JSON
</dt><dd>
</dd><dt>storable - a Storable frozen value in network format
</dt><dd>
</dd><dt>storable-file - a Storable file in network format (Storable has two incompatible formats)
</dt><dd>
</dd><dt>bencode - use Convert::Bencode, if available (used by torrent files, among others)
</dt><dd>
</dd><dt>clzf - Compress::LZF format
</dt><dd>
</dd><dt>yaml - YAML
</dt><dd>
</dd><dt>dump - Data::Dump
</dt><dd>
</dd><dt>dumper - Data::Dumper
</dt><dd>
</dd><dt>string - writes the data out as if it were a string
</dt><dd>
</dd><dt>none - nothing gets written, mainly useful together with &quot;-e&quot;
</dt><dd> Note that Data::Dumper doesn't handle self-referential data structures correctly - use ``dump'' instead.</dd></dl>
</dl>

<dl>
</dl>

<dt>-e code
</dt><dd> Evaluate perl code after reading the data and before writing it out again - can be used to filter, create or extract data. The data that has been written is in <tt>$_</tt>, and whatever is in there is written out afterwards.</dd></dl>

<h2>EXAMPLES</h2>

 <pre>
   json_xs -t none &lt;isitreally.json
</pre> 

 ``JSON Lint'' - tries to parse the file <i>isitreally.json</i> as JSON - if it is valid JSON, the command outputs nothing, otherwise it will print an error message and exit with non-zero exit status. 

 <pre>
   &lt;src.json json_xs &gt;pretty.json
</pre> 

 Prettify the JSON file <i>src.json</i> to <i>dst.json</i>. 

 <pre>
   json_xs -f storable-file &lt;file
</pre> 

 Read the serialised Storable file <i>file</i> and print a human-readable JSON version of it to STDOUT. 

 <pre>
   json_xs -f storable-file -t yaml &lt;file
</pre> 

 Same as above, but write YAML instead (not using JSON at all :) 

 <pre>
   json_xs -f none -e '$_ = [1, 2, 3]'
</pre> 

 Dump the perl array as UTF-8 encoded JSON text. 

 <pre><code>
   &lt;torrentfile json_xs -f bencode -e '$_ = join "\n", map @$_, @{$_-&gt;{"announce-list"}}' -t string
</code></pre> 

 Print the tracker list inside a torrent file. 

 <pre>
   lwp-request <a rel="nofollow" HREF="http://cpantesters.perl.org/show/JSON-XS.json">http://cpantesters.perl.org/show/JSON-XS.json</a> | json_xs
</pre> 

 Fetch the cpan-testers result summary <tt>&quot;JSON::XS&quot;</tt> and pretty-print it.

<h2>AUTHOR</h2>

 Copyright (C) 2008 Marc Lehmann &lt;json [at] schmorp.de&gt;
