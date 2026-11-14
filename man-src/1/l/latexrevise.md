---
title: "latexrevise(1)"
name: "latexrevise"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latexrevise/"
description: "latexrevise – selectively remove markup and text from latexdiff output"
---

<h2 class="name">NAME</h2>
<p> latexrevise &#8211; selectively remove markup and text from latexdiff output </p>
<h2>SYNOPSIS</h2>
<p> <code>latexrevise</code> [ <font SIZE="-1"><code>OPTIONS</code></font> ] [ <i>diff.tex</i> ] &gt; <i>revised.tex</i></p>
<h2>DESCRIPTION</h2>
<p> <i>latexrevise</i> reads a file <tt>&quot;diff.tex&quot;</tt> (output of <i>latexdiff</i>), and remove the markup commands. If no filename is given the input is read from standard input. The command can be used in <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i>, <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i>, or <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode, or can be used to remove user-defined latex commands from the input (see <code>-c</code>, <code>-e</code>, <code>-m</code>, and <code>-n</code> below). In <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i> mode, all appended text fragments (or preamble lines) are kept, and all discarded text fragments (or preamble lines) are deleted. In <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i> mode, all discarded text fragments are kept, and all appended text fragments are deleted. If you wish to keep some changes, edit the diff.tex file in advance, and manually remove those tokens which would otherwise be deleted. Note that <i>latexrevise</i> only pays attention to the <tt>&quot;\DIFaddbegin&quot;</tt>, <tt>&quot;\DIFaddend&quot;</tt>, <tt>&quot;\DIFdelbegin&quot;</tt>, and <tt>&quot;\DIFdelend&quot;</tt> tokens and corresponding <font SIZE="-1">FL</font> varieties. All <tt>&quot;\DIFadd&quot;</tt> and <tt>&quot;\DIFdel&quot;</tt> commands (but not their contents) are simply deleted. The commands added by latexdiff to the preamble are also removed. In <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode, <tt>&quot;\DIFaddbegin, \DIFaddend, \DIFdelbegin, \DIFdelend&quot;</tt> tokens and their corresponding <tt>&quot;FL&quot;</tt> varieties are kept but all other markup (e.g. <tt>&quot;DIFadd&quot;</tt> and &lt;\DIFdel&gt;) is removed. The result will not in general be valid latex-code but it will be easier to read and edit in preparation for a subsequent run in <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i> or <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i> mode. In <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode the preamble is left unmodified.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> or <code>&#8211;accept</code></p>
<dd> Run in <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i> mode (delete all blocks marked by <tt>&quot;\DIFdelbegin&quot;</tt> and <tt>&quot;\DIFdelend&quot;</tt>).</p>
<dt><code>-d</code> or <code>&#8211;decline</code></p>
<dd> Run in <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i> mode (delete all blocks marked by <tt>&quot;\DIFaddbegin&quot;</tt> and <tt>&quot;\DIFaddend&quot;</tt>).</p>
<dt><code>-s</code> or <code>&#8211;simplify</code></p>
<dd> Run in <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode (Keep all <tt>&quot;\DIFaddbegin&quot;</tt>, <tt>&quot;\DIFaddend&quot;</tt>, <tt>&quot;\DIFdelbegin&quot;</tt>, <tt>&quot;\DIFdelend&quot;</tt> tokens, but remove all other latexdiff markup from body).</dl>
<p> Note that the three mode options are mutually exclusive. If no mode option is given, <i>latexrevise</i> simply removes user annotations and markup according to the following four options.</p>
<dl>
<dt><code>-c cmd</code> or <code>&#8211;comment=cmd</code></p>
<dd> Remove <tt>&quot;
