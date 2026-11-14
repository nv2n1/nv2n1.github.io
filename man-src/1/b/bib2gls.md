---
title: "bib2gls(1)"
name: "bib2gls"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bib2gls/"
---

<h2>SYNOPSIS</h2>
<p> <code>bib2gls</code> [<i>option</i>]+ <i>auxfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bib2gls</code> is designed to work with the <code>glossaries-extra</code> LaTeX package. (The <code>record</code> package option is required.) The application performs two functions in one: (1) selects entries from .bib files according to information found in the <i>auxfile</i> (similar to <code>bibtex</code>); (2) hierarchically sorts entries and collates location lists (similar to <code>makeindex</code> and <code>xindy</code>). The .aux extension may be omitted from <i>auxfile</i>. </p>
<p> The <i>auxfile</i> (and corresponding .log file) should either be in the current directory or in the directory specified by <code>&#8211;dir</code>. Bib files can either be relative to the directory the <i>auxfile</i> is in or in a location that can be found by kpsewhich.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code> or <code>-h</code></p>
<dd> Display help message and exit.</p>
<dt><code>&#8211;version</code> or <code>-v</code></p>
<dd> Display version information and exit.</p>
<dt><code>&#8211;debug</code> [<i>level</i>]</p>
<dd> Switch on the debug mode (optionally at the given <i>level</i>, which should be a non-negative integer). If <i>level</i> is <code>0</code> then the debug mode is switched off.</p>
<dt><code>&#8211;no-debug</code> (or <code>&#8211;nodebug</code>)</p>
<dd> Switch off debug mode. (Equivalent to <code>&#8211;debug</code> <code>0</code>)</p>
<dt><code>&#8211;verbose</code></p>
<dd> Switch on verbose mode.</p>
<dt><code>&#8211;no-verbose</code> (or <code>&#8211;noverbose</code>)</p>
<dd> Switch off verbose mode. (Some messages will still be written to <font SIZE="-1">STDOUT.</font>)</p>
<dt><code>&#8211;silent</code></p>
<dd> Only display error messages. All other messages are just written to the transcript file.</p>
<dt><code>&#8211;locale</code> <i>lang</i> (or <code>-l</code> <i>lang</i>)</p>
<dd> Use language resource file for <i>lang</i> (which should be an <font SIZE="-1">IETF</font> locale tag).</p>
<dt><code>&#8211;log-file</code> <i>file</i> (or <code>-t</code> &lt;file&gt;)</p>
<dd> Set the transcript file.</p>
<dt><code>&#8211;dir</code> <i>directory</i> (or <code>-d</code> &lt;directory&gt;)</p>
<dd> Files are relative to <i>directory</i>. (This doesn&#8217;t change the current working directory.)</p>
<dt><code>&#8211;tex-encoding</code> <i>name</i></p>
<dd> Set the character encoding for the output files. This overrides the setting given in <i>auxfile</i>.</p>
<dt><code>&#8211;interpret</code></p>
<dd> Use the TeX parser library to interpret known (La)TeX commands (default).</p>
<dt><code>&#8211;no-interpret</code></p>
<dd> Don&#8217;t try interpreting (La)TeX commands.</p>
<dt><code>&#8211;break-space</code></p>
<dd> Interpret <tt>&quot;~&quot;</tt> (tilde) character and <tt>&quot;
obreakspace&quot;</tt> as a normal space.</p>
<dt><code>&#8211;no-break-space</code></p>
<dd> Interpret <tt>&quot;~&quot;</tt> (tilde) and <tt>&quot;
obreakspace&quot;</tt> as a non-breaking space (default).</p>
<dt><code>&#8211;cite-as-record</code></p>
<dd> Treat <tt>&quot;
