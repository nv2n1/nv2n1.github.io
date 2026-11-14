---
title: "datarecursiveencode(3)"
name: "datarecursiveencode"
section: "3"
letter: "d"
url: "/docs/linux/man/3-datarecursiveencode/"
---

Data::Recursive::Encode - Encode/Decode Values In A Structure 

<h2>Synopsis</h2><pre> use Data::Recursive::Encode;
 Data::Recursive::Encode-&gt;decode('euc-jp', $data);
 Data::Recursive::Encode-&gt;encode('euc-jp', $data);
 Data::Recursive::Encode-&gt;decode_utf8($data);
 Data::Recursive::Encode-&gt;encode_utf8($data);
 Data::Recursive::Encode-&gt;from_to($data, $from_enc, $to_enc[, $check]);</pre><h2>Description</h2>Data::Recursive::Encode visits each node of a structure, and returns a new structure with each node's encoding (or similar action). If you ever wished to do a bulk encode/decode of the contents of a structure, then this module may help you.
<h2>Methods</h2><dl COMPACT><dt>decode
<dd><pre> my $ret = Data::Recursive::Encode-&gt;decode($encoding, $data, [CHECK]);</pre>Returns a structure containing nodes which are decoded from the specified encoding.
<dt>encode
<dd><pre> my $ret = Data::Recursive::Encode-&gt;encode($encoding, $data, [CHECK]);</pre>Returns a structure containing nodes which are encoded to the specified encoding.
<dt>decode_utf8
<dd><pre> my $ret = Data::Recursive::Encode-&gt;decode_utf8($data, [CHECK]);</pre>Returns a structure containing nodes which have been processed through decode_utf8.
<dt>encode_utf8
<dd><pre> my $ret = Data::Recursive::Encode-&gt;encode_utf8($data);</pre>Returns a structure containing nodes which have been processed through encode_utf8.
<dt>from_to
<dd><pre> my $ret = Data::Recursive::Encode-&gt;from_to($data, FROM_ENC, TO_ENC[, CHECK]);</pre>Returns a structure containing nodes which have been processed through from_to.</dl><h2>Author</h2>Tokuhiro Matsuno &lt;tokuhirom <font SIZE="-1">AAJKLFJEF GMAIL COM</font>&gt; 

 gfx
<h2>See Also</h2>This module is inspired from Data::Visitor::Encode, but this module depended to too much modules. I want to use this module in pure-perl, but Data::Visitor::Encode depend to <font SIZE="-1">XS</font> modules. 

 Unicode::RecursiveDowngrade does not supports perl5's Unicode way correctly.
<h2>License</h2>Copyright (C) 2010 Tokuhiro Matsuno All rights reserved. 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.
