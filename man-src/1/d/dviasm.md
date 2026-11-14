---
title: "dviasm(1)"
name: "dviasm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dviasm/"
description: "DVIasm – a TeX utility program for editing DVI files directly"
---

<h2 class="name">NAME</h2>
<p> DVIasm &#8211; a TeX utility program for editing DVI files directly </p>
<h2>SYNOPSIS</h2>
<p> <code>dviasm</code> [&lt;<i>options</i>&gt;] &lt;<i>dvi_file</i>&gt;|&lt;<i>dvi_dump_file</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>DVIasm</code> is a TeX utility program which is designed for editing DeVice-Independent (DVI) files directly. It consists of a single Python script, dviasm.py, in a human readable text format. It runs on any platform in which Python 3 is installed.</p>
<dl>
<dt>Features of <code>DVIasm</code> includes:</p>
<dd>
<dt>
<dd> 1) Disassemble a DVI file (or XeTeX XDV file) into a human-readable text file, the contents of which are easy to modify.</p>
<dt>
<dd> 2) Assembles the output text file back to the binary format.</p>
<dt>There are several alternatives for dumping and editing DVI files:</p>
<dd>
<dt>
<dd> 1) <code>DVItype</code> developed by Donald E. Knuth supports one-way conversion from DVI to a text format. There are also some derivatives: <code>pDVItype</code> for pTeX, <code>upDVItype</code> for upTeX, <code>ODVItype</code> for Omega.</p>
<dt>
<dd> 2) The programs <code>dv2dt</code> and <code>dt2dv</code> can be used in pairs to allow two-way conversion between DVI and the DVI Text Language (DTL).</p>
<dt>
<dd> 3) The program <code>dvispc</code> (part of DVIOUT previewer) also has an ability to convert between DVI and text.</dl>
<p> Among those, <code>DVIasm</code> is designed to allow users to edit DVI files easily, for example by unifying &#8220;right1&#8221;-&#8220;right4&#8221; to a single command &#8220;right&#8221; which can be used regardless of the amount of move.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this help message and exit.</p>
<dt><code>-u</code> &lt;<i>STR</i>&gt;, <code>&#8211;unit=</code>&lt;<i>STR</i>&gt;</p>
<dd> Set unit [default: `pt&#8217;]. Allowed values are: `sp&#8217;, `pt&#8217;, `bp&#8217;, `mm&#8217;, `cm&#8217; and `in&#8217;.</p>
<dt><code>-o</code> &lt;<i>FILE</i>&gt;, <code>&#8211;output=</code>&lt;<i>FILE</i>&gt;</p>
<dd> Set filename for output instead of stdout.</p>
<dt><code>-e</code> &lt;<i>STR</i>&gt;, <code>&#8211;encoding=</code>&lt;<i>STR</i>&gt;</p>
<dd> Set encoding for input/output of dumped text [default: `utf8&#8242;]. Allowed values are: `ascii&#8217;, `latin1&#8242;, `utf8&#8242;, `sjis&#8217; and `eucjp&#8217;. When used with the option <code>-p</code> (or <code>&#8211;ptex</code>), allowed values are only `utf8&#8242;, `sjis&#8217; and `eucjp&#8217;.</p>
<dl>
<dt>
<dd> # NOTE: This feature does not support dumping through stdout.</dl>
<dt><code>-x</code> &lt;<i>STR</i>&gt;, <code>&#8211;xxx-encoding=</code>&lt;<i>STR</i>&gt;</p>
<dd> Set encoding for interpreting `xxx:&#8217; strings [default: `none&#8217;]. Allowed values are: `none&#8217;, `utf8&#8242;, `sjis&#8217; and `eucjp&#8217;.</p>
<dl>
<dt>
<dd> This option allows users to specify the correct encoding for dumping/compiling the contents of \special.</p>
<dl>
<dt>Typical usages are as follows:</p>
<dd>
<dt>
<dd> 1) By default, the contents of \special are dumped/compiled as byte-to-byte escape sequences in `
