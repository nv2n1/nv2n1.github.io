---
title: "vdcomp(1)"
name: "vdcomp"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdcomp/"
---

<h2>Name</h2>

 <i>vdcomp</i> - decompress a compressed PDS image

<h2>Synopsis</h2>

 <i>vdcomp</i> [ infile ] [ outfile ] [ format-code ]

<h2>Description</h2>

 The <i>vdcomp</i> program reads a variable length compressed PDS image and outputs a fixed length uncompressed image file in PDS format with labels, image histogram, engineering table, line header table and an image with PDS, FITS, VICAR or no labels. 

 If used on a non-byte-swapped machine the image histogram is un-swapped.

<h2>Options</h2>

 <i>Vdcomp</i> will prompt for any options that are not supplied on the command-line. 

 <i>infile</i> 

<dl>
<dt>
<dd> The name of compressed image file.</dl>
 

 <i>outfile</i> 

<dl>
<dt>
<dd> The name of uncompressed image file.</dl>
 

 <i>format-code</i> 

<dl>
<dt>
<dd> Select from the following list: 

<dl>
<dt>
<dd> <i>1</i> - SFDU/PDS format [default] 
 <i>2</i> - FITS format 
 <i>3</i> - VICAR format 
 <i>4</i> - unlabelled binary array</dl>
</dl>

<h2>Limitations</h2>

 This program has been tested on a VAX 780 (VMS 4.6), SUN Workstation (UNIX 4.2, release 3.4), an IBM PC (MICROSOFT 5.1 compiler) and Macintosh IIx using Lightspeed C version 3.0. When converting to other systems, check for portability conflicts.

<h2>Credits</h2>

 This program uses Kris Becker's subroutine DECOMP.C (which is included in this program in a shortened version).

<h2>History</h2>

 bradley [at] cis.upenn.edu 06-23-94 ansi-fied program 

 datri [at] convex.com, 11-15-91 added recognition of - as stdout for output filename; disabled various messages; directed messages to stderr; added exit status 

 DEC89 Modified program to handle both Voyager and Viking images. 

 OCT89 Converted Voyager decompression program to handle Viking compressed images. Changed obuf to 'unsigned' to simplify computation of checksum. 

 AUG89 Added code to get command line arguments for filenames and output format; routines to free memory used by the Huffman tree); fixed the SFDU label output length; and modified the I/O routines so that the open for Host type 2 uses binary I/O. 

 JUN89 Fixed READVAR, to get length on 16-bit unswapped hosts. 

 JUL88 C driver to decompress standard Voyager Compressed images by Mike Martin 1989/12/02. 

<h2>Index</h2>


