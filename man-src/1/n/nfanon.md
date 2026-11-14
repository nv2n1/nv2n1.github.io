---
title: "nfanon(1)"
name: "nfanon"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfanon/"
description: "nfanon – netflow anonymisation"
---

<h2>NAME</h2>
<p> nfanon &#8211; netflow anonymisation</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nfanon [options]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>nfanon</code></p>
<dd>is used to anonymise all IP addresses ( src, dst, next hop, router IP etc. ) in the netflow records using the CryptoPAn (Cryptography-based Prefix-preserving Anonymization) module. The key <i>-K</i> is used to initialize the Rijndael cipher. The key is either a 32 character string, or a 64 hex digit string starting with 0x. </p>
<dl>
<dt>
<dd> See <a rel="nofollow" href="http://www.cc.gatech.edu/computing/Telecomm/cryptopan/">http://www.cc.gatech.edu/computing/Telecomm/cryptopan/</a> for more information about CryptoPAn.</dl>
<p> nfanon has several modes of operation. </p>
<p> <code>o</code> nfanon reads a sequence of input files, specified by -r, -R and -M and anonymises the flows in the given files. The input file arguments have the same syntax and meaning as <a href="/docs/linux/man/1-nfdump/">nfdump</a>(1). </p>
<p> <code>o</code> nfanon reads a sequence of input files, specified by -r, -R and -M. All anonymised flows are written to a single file specified by -w. </p>
<p> <code>o</code> nfanon works as filter and reads flows from stding and writes the anonymised flows to stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r </code><i>inputfile</i></p>
<dd> Read input data from <i>inputfile</i>. Default is read from stdin.</p>
<dt><code>-R </code><i>expr</i></p>
<dd> Read input from a sequence of files in the same directory. <i>expr</i> may be one of:</p>
<dl>
<dt>
<dd> /any/<i>dir</i> Read recursively all files in directory <i>dir</i>. </p>
<p> /dir/<i>file</i> Read all files beginning with <i>file</i>. </p>
<p> /dir/<i>file1:file2</i> Read all files from <i>file1</i> to <i>file2</i>. </p>
<p> Note: files are read in alphabetical sequence.</dl>
<dt><code>-M </code><i>expr</i></p>
<dd> Read input from multiple directories. <i>expr</i> looks like: <i>/any/path/to/dir1:dir2:dir3</i> etc. and will be expanded to the directories: <i>/any/path/to/dir1</i>, <i>/any/path/to/dir2</i> and <i>/any/path/to/dir3</i> Any number of colon separated directories may be given. The files to read are specified by -r or -R and are expected to exist in all the given directories. The options -r and -R must not contain any directory part when used in conjunction with -M.</p>
<dt><code>-w </code><i>outputfile</i></p>
<dd> If specified writes anonymised netflow records to <i>outputfile</i>.</p>
<dt><code>-K </code><i>key</i></p>
<dd> The key is used to initialize the Rijndael cipher. <i>key</i> is either a 32 character string, or a 64 hex digit string starting with 0x.</dl>
<h2>RETURN VALUE</h2>
<p> Returns</p>
<dl>
<dt>
<dd>
<p> 0 No error. </p>
<p> 255 Initialization failed. </p>
<p> 250 Internal error.</dl>
<h2>NOTES</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nfdump/">nfdump</a>(1)</p>
<h2>BUGS</h2>
<h2>Index</h2>
