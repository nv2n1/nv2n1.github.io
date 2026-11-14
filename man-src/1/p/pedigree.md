---
title: "pedigree(1)"
name: "pedigree"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pedigree/"
description: "pedigree – create a TeX file for pedigree from a csv file"
---

<h2 class="name">NAME</h2>
<p> pedigree &#8211; create a TeX file for pedigree from a csv file </p>
<h2>SYNOPSIS</h2>
<p> <code>pedigree</code> [-c <i>configuration_file</i>] [-d] [-o <i>output_file</i>] [-s <i>start_id</i>] <i>input_file</i> </p>
<p> <code>pedigree</code> -v</p>
<h2>DESCRIPTION</h2>
<p> The program converts a comma separated <i>input_file</i> into a TeX file with pst-pdgr macros.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>configuration_file</i></p>
<dd> The configuration file to read along with the system-wide and user&#8217;s configuration files</p>
<dt><code>-d</code></p>
<dd> Debug mode on</p>
<dt><code>-o</code> &#8211;<i>output_file</i></p>
<dd> The ouput file instead of <i>input_file.tex</i></p>
<dt><code>-s</code> &#8211;<i>start_id</i></p>
<dd> If this option is selected, the pedigree is constructed starting from the node with the Id i&lt;start_id&gt;. Otherwise it is started from the proband node. </p>
<p> This option allows to create pedigrees with multiple probands or absent probands, or show people who are not proband&#8217;s relatives.</p>
<dt><code>-v</code></p>
<dd> Print version information</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pedigree.cfg</code></p>
<dd> Global configuration file</p>
<dt>$HOME<code>/.pedigreerc</code></p>
<dd> User configuration file</dl>
<h2>SEE ALSO</h2>
<p> The manual distributed with this program describes the format of the configuration file and the input file. </p>
<p> The library functions are described in <code><a href="/docs/linux/man/3-pedigree--language/">Pedigree::Language</a></code>(3), <code><a href="/docs/linux/man/3-pedigree--parser/">Pedigree::Parser</a></code>(3), <code><a href="/docs/linux/man/3-pedigree--node/">Pedigree::Node</a></code>(3), <code><a href="/docs/linux/man/3-pedigree--personnode/">Pedigree::PersonNode</a></code>(3), <code><a href="/docs/linux/man/3-pedigree--marriagenode/">Pedigree::MarriageNode</a></code>(3), <code><a href="/docs/linux/man/3-pedigree--area/">Pedigree::Area</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> Boris Veytsman, Leila Akhmadeeva, 2006-2021 </p>
<h2>Index</h2>
