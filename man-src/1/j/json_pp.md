---
title: "json_pp(1)"
name: "json_pp"
section: "1"
letter: "j"
url: "/docs/linux/man/1-json_pp/"
---

<h2 class="name">NAME</h2>
 

 json_pp - JSON::PP command utility 

<h2>SYNOPSIS</h2>

 <pre><code>
json_pp[-v][-f from_format][-t to_format][-json_opt options_to_json1[, options_to_json2[, ...]]]
</code></pre>

<h2>DESCRIPTION</h2>

 json_pp converts between some input and output formats (one of them is <font SIZE="-1">JSON</font>). This program was copied from json_xs and modified. 

 The default input format is json and the default output format is json with pretty option.

<h2>OPTIONS</h2>

<h3>-f</h3>

 <pre>
    -f from_format
</pre> 

 Reads a data in the given format from <font SIZE="-1">STDIN.</font> 

 Format types:
<dl>
<dt>json
<dd> as <font SIZE="-1">JSON</font>
<dt>eval
<dd> as Perl code</dl>

<h3>-t</h3>

 Writes a data in the given format to <font SIZE="-1">STDOUT.</font>
<dl>
<dt>null
<dd> no action.
<dt>json
<dd> as <font SIZE="-1">JSON</font>
<dt>dumper
<dd> as Data::Dumper</dl>

<h3>-json_opt</h3>

 options to <font SIZE="-1">JSON::PP</font> 

 Acceptable options are: 

 <pre>
    ascii latin1 utf8 pretty indent space_before space_after relaxed canonical allow_nonref
    allow_singlequote allow_barekey allow_bignum loose escape_slash indent_length
</pre> 

 Multiple options must be separated by commas: 

 <pre>
    Right: -json_opt pretty,canonical
    Wrong: -json_opt pretty -json_opt canonical
</pre>

<h3>-v</h3>

 Verbose option, but currently no action in fact.

<h3>-V</h3>

 Prints version and exits.

<h2>EXAMPLES</h2>

 <pre><code>
$ perl - e 'print q|{"foo":"あい","bar":1234567890000000000000000}|' |
    json_pp - f json - t dumper - json_opt pretty,
    utf8, allow_bignum

              $VAR1 = {'bar' = &gt; bless({'value' = &gt; [
                                            '0000000',
                                            '0000000',
                                            '5678900',
                                            '1234'
                                        ],
                                        'sign' = &gt; '+'},
                                       'Math::BigInt'),
                       'foo' = &gt; "\x{3042}\x{3044}"};
$ perl - e 'print q|{"foo":"あい","bar":1234567890000000000000000}|' |
    json_pp - f json - t dumper - json_opt pretty

                                      $VAR1 = {
    'bar' = &gt; '1234567890000000000000000',
    'foo' = &gt; "\x{e3}\x{81}\x{82}\x{e3}\x{81}\x{84}"};
</code></pre>

<h2>SEE ALSO</h2>

 <font SIZE="-1">JSON::PP</font>, json_xs

<h2>AUTHOR</h2>

 Makamaka Hannyaharamitu, &lt;makamaka[at]cpan.org&gt;

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 2010 by Makamaka Hannyaharamitu 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


