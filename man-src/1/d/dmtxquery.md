---
title: "dmtxquery(1)"
name: "dmtxquery"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmtxquery/"
description: "dmtxquery – extract information from dmtxread output"
---

<h2>NAME</h2>
<p> dmtxquery &#8211; extract information from dmtxread output</p>
<h2>SYNOPSIS</h2>
<p> <code>dmtxquery</code> <i>PROPERTY</i> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> dmtxquery extracts information from the XML output from dmtxread for individual or grouped barcode scan results.</p>
<h2>PROPERTY</h2>
<p> barcode.count count of all barcodes found in image </p>
<p> barcode.<code>N</code>.<code>BPROP</code> print BPROP property of Nth barcode </p>
<p> message.count count of all messages found in image </p>
<p> message.<code>N</code>.<code>MPROP</code> print MPROP property of Nth message </p>
<p> message.<code>N</code>.barcode.count count of all barcodes in Nth message </p>
<p> message.<code>N</code>.barcode.<code>M</code> Mth barcode of Nth message, print all </p>
<p> message.<code>N</code>.barcode.<code>M</code>.<code>BPROP</code> Mth barcode of Nth message, print BPROP </p>
<p> <code>BPROP</code> barcode properties:<br />
message&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>message_number&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>message_position<br />
matrix_size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data_codewords&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>error_codewords<br />
rotation&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data_regions_count&nbsp;<wbr>&nbsp;<wbr>interleaved_blocks </p>
<p> <code>MPROP</code> message properties:<br />
message&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data_codeword&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>error_codeword</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print program version information.</p>
<dt><code>&#8211;help</code></p>
<dd> Display this help message and quit.</dl>
<h2>STANDARDS</h2>
<p> ISO/IEC 16022:2000 </p>
<p> ANSI/AIM BC11 ISS</p>
<h2>BUGS</h2>
<p> Email bug reports to <i>mike [at] dragonflylogic.com</i></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2008, 2009 Mike Laughton </p>
<h2>Index</h2>
