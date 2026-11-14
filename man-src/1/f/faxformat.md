---
title: "faxformat(1)"
name: "faxformat"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faxformat/"
---

<h2>SYNOPSIS</h2>
<p> This page, part of the <code>Netpbm</code>user&#8217;s<code><a href="/docs/linux/man/1-guide/">guide</a></code>(1) , describes FAX formats in relation to Netpbm facilities. </p>
<h2>DESCRIPTION</h2>
<p> The ITU (formerly CCITT) publishes standards for operation of fax machines (the idea is to provide a way to be sure that a fax machine is able to receive a fax sent by another). These standards incidentally specify graphics file formats &#8212; a protocol for representing a visual image in sequences of bits. </p>
<p> The two relevant standards are called Group 3 (G3) and Group 4 (G4) (Groups 1 and 2 are analog standards no longer in use). Virtually every fax machine in existence conforms at least generally to at least one of these standards. </p>
<p> The standard for Group 3 fax is defined in ITU Recommendation T.4. In the U.S., that is implemented by EIA standards EIA-465 and EIA-466. These standards cover more than the file format as well, including how to transmit bits over a telephone line and procedures for handling document transmissions. </p>
<p> G3 faxes are 204 dots per inch (dpi) horizontally and 98 dpi (196 dpi optionally, in fine-detail mode) vertically. </p>
<p> The standards specify three file formats (also called coding methods and compression schemes &#8212; remember the standard doesn&#8217;t mention computer files; it talks about the format of a stream of bits travelling over a telephone line): </p>
<dl>
<dt>MH</p>
<dd> This compresses in one dimension: it compresses individual raster lines but makes no attempt to compress redundancy between lines. </p>
<p> One dimensional compression is traditionally the best a fax machine could handle because G3 neither assumes error free transmission not retransmits when errors occur, and receiving fax machines traditionally could not afford to buffer much of a page. It&#8217;s important that when there is an error in a raster line, its impact not spread to many lines after it. </p>
<p> All Group 3 and Group 4 fax machines must be able to send and receive MH. </p>
<p> MH is sometimes called &#8216;G3,&#8217; but that is a poor name because while the Group 3 standard does specify MH, it has always specified other formats too. </p>
<p> MH is sometimes called &#8216;T4&#8217; based on the name of the document that specifies it, ITU T.4. But this is a poor name because T.4 also specifies MR. </p>
<dt>MR</p>
<dd> This compresses in two dimensions, horizontally and vertically. </p>
<p> MR has always been part of the Group 3 standard, but is optional (a Group 3 fax machine may or may not be able to send and receive it). </p>
<dt>MMR</p>
<dd> This is a more advanced format than the others. It is even more two-dimensional than MR. It is optional in the Group 3 standard, and didn&#8217;t even exist in earlier versions of it. It was developed specifically for the Group 4 standard, but then added to an extended Group 3 standard as well. </p>
<p> MMR is sometimes called Group 4, but that is a poor name because of the fact that it is also part of the current Group 3 standard. </p>
<p> MMR is sometimes called &#8216;T6&#8217; based on the name of the document<br />
&nbsp;<wbr>that specifies it, ITU T.6. </p>
</dl>
<p> <code>g3topbm</code> converts the MH format to PBM. <code>pbmtog3</code> converts PBM to MH. </p>
<p> There is no Netpbm program to convert to or from other fax formats. </p>
<h2>TIFF</h2>
<p> The TIFF format is flexible enough to allow lots of different coding methods, within it. There are TIFF subformats for MH, MR, and MMR, among others. These are particularly useful when you receive a fax as a TIFF file. </p>
<p> <code>tifftopnm</code> recognizes and can convert from any of these. </p>
<p> <code>pamtotiff</code> can convert to any of these; you use command options to choose which. </p>
<h2>Index</h2>
