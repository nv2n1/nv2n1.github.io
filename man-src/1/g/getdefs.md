---
title: "getdefs(1)"
name: "getdefs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getdefs/"
description: "getdefs – AutoGen Definition Extraction Tool"
---

<h2 class="name">NAME</h2>
<p> getdefs &#8211; AutoGen Definition Extraction Tool </p>
<h2>SYNOPSIS</h2>
<p> <code>getdefs</code> [<i>opt-name</i>[<code>=</code><i>value</i>]]&#8230; </p>
<p> All arguments are named options. </p>
<p> If no <code>input</code> argument is provided or is set to simply &quot;-&quot;, and if <code>stdin</code> is not a <code>tty</code>, then the list of input files will be read from <code>stdin</code>.</p>
<h2>DESCRIPTION</h2>
<p> This program extracts AutoGen definitions from a list of source files. Definitions are delimited by <code>/*=&lt;entry-type&gt; &lt;entry-name&gt;fP and =*/fP. </code></p>
<h2>OPTIONS</h2>
<h3>Specify which definitions are of interest and what to say about them</h3>
<dl>
<dt><code>defs-to-get</code>=<i>reg-ex</i></p>
<dd> Regexp to look for after the &quot;/*=&quot;. </p>
<p> If you want definitions only from a particular category, or even with names matching particular patterns, then specify this regular expression for the text that must follow the <code>/*=</code>.</p>
<dt><code>subblock</code>=<i>sub-def</i></p>
<dd> subblock definition names. This option may appear an unlimited number of times. </p>
<p> This option is used to create shorthand entries for nested definitions. For example, with: </p>
<p> <i>using subblock thus</i> <code>&#8211;subblock=arg=argname,type,null</code> </p>
<p> <i>and defining an </i><code>arg</code> thus <code>arg: this, char *</code> </p>
<p> <i>will then expand to:</i> <code>arg = { argname = this; type = &quot;char *&quot;; @</code>;}<br />
 The &quot;this, char *&quot; string is separated at the commas, with the white space removed. You may use characters other than commas by starting the value string with a punctuation character other than a single or double quote character. You may also omit intermediate values by placing the commas next to each other with no intervening white space. For example, &quot;+mumble++yes+&quot; will expand to:<br />
 <code>arg = { argname = mumble; null = &quot;yes&quot;; @</code>;}.</p>
<dt><code>listattr</code>=<i>def</i></p>
<dd> attribute with list of values. This option may appear an unlimited number of times. </p>
<p> This option is used to create shorthand entries for definitions that generally appear several times. That is, they tend to be a list of values. For example, with:<br />
 <code>listattr=foo</code> defined, the text:<br />
 <code>foo: this, is, a, multi-list</code> will then expand to:<br />
 <code>foo = &#8216;this&#8217;, &#8216;is&#8217;, &#8216;a&#8217;, &#8216;multi-list&#8217;;</code><br />
 The texts are separated by the commas, with the white space removed. You may use characters other than commas by starting the value string with a punctuation character other than a single or double quote character.</dl>
<h3>specify how to number the definitions</h3>
<dl>
<dt><code>ordering</code>[<code>=</code><i>file-name</i>], <code>no-ordering</code></p>
<dd> Alphabetize or use named file. The <i>no-ordering</i> form will disable the option. This option is enabled by default. </p>
<p> By default, ordering is alphabetical by the entry name. Use, <code>no-ordering</code> if order is unimportant. Use <code>ordering</code> with no argument to order without case sensitivity. Use <code>ordering=&lt;file-name&gt;</code> if chronological order is important. getdefs will maintain the text content of <code>file-name</code>. <code>file-name</code> need not exist.</p>
<dt><code>first-index</code>=<i>first-index</i></p>
<dd> The first index to apply to groups. This option takes an integer number as its argument. The default <i>first-index</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>0 </p>
<p> By default, the first occurrence of a named definition will have an index of zero. Sometimes, that needs to be a reserved value. Provide this option to specify a different starting point.</dl>
<h3>Definition insertion options</h3>
<dl>
<dt><code>filelist</code>[<code>=</code><i>file</i>]</p>
<dd> Insert source file names into defs. </p>
<p> Inserts the name of each input file into the output definitions. If no argument is supplied, the format will be: </p>
<pre>
    infile = '%s';
</pre>
<p> If an argument is supplied, that string will be used for the entry name instead of <code>infile</code>.</p>
<dt><code>assign</code>=<i>ag-def</i></p>
<dd> Global assignments. This option may appear an unlimited number of times. </p>
<p> The argument to each copy of this option will be inserted into the output definitions, with only a semicolon attached.</p>
<dt><code>common-assign</code>=<i>ag-def</i></p>
<dd> Assignments common to all blocks. This option may appear an unlimited number of times. </p>
<p> The argument to each copy of this option will be inserted into each output definition, with only a semicolon attached.</p>
<dt><code>copy</code>=<i>file</i></p>
<dd> File(s) to copy into definitions. This option may appear an unlimited number of times. </p>
<p> The content of each file named by these options will be inserted into the output definitions.</p>
<dt><code>srcfile</code>[<code>=</code><i>file</i>]</p>
<dd> Insert source file name into each def. </p>
<p> Inserts the name of the input file where a definition was found into the output definition. If no argument is supplied, the format will be: </p>
<pre>
    srcfile = '%s';
</pre>
<p> If an argument is supplied, that string will be used for the entry name instead of <code>srcfile</code>.</p>
<dt><code>linenum</code>[<code>=</code><i>def-name</i>]</p>
<dd> Insert source line number into each def. </p>
<p> Inserts the line number in the input file where a definition was found into the output definition. If no argument is supplied, the format will be: </p>
<pre>
    linenum = '%s';
</pre>
<p> If an argument is supplied, that string will be used for the entry name instead of <code>linenum</code>.</dl>
<h3>specify which files to search for markers</h3>
<dl>
<dt><code>input</code>=<i>src-file</i></p>
<dd> Input file to search for defs. This option may appear an unlimited number of times. This option is the default option. </p>
<p> All files that are to be searched for definitions must be named on the command line or read from <code>stdin</code>. If there is only one <code>input</code> option and it is the string, &quot;-&quot;, then the input file list is read from <code>stdin</code>. If a command line argument is not an option name and does not contain an assignment operator (<code>=</code>), then it defaults to being an input file name. At least one input file must be specified.</dl>
<h3>Definition output disposition options:</h3>
<dl>
<dt><code>output</code>=<i>file</i></p>
<dd> Output file to open. This option is a member of the autogen class of options. </p>
<p> If you are not sending the output to an AutoGen process, you may name an output file instead.</p>
<dt><code>autogen</code>[<code>=</code><i>ag-cmd</i>], <code>no-autogen</code></p>
<dd> Invoke AutoGen with defs. The <i>no-autogen</i> form will disable the option. This option is enabled by default. This option is a member of the autogen class of options. </p>
<p> This is the default output mode. Specifying <code>no-autogen</code> is equivalent to <code>output=-</code>. If you supply an argument to this option, that program will be started as if it were AutoGen and its standard in will be set to the output definitions of this program.</p>
<dt><code>template</code>=<i>file</i></p>
<dd> Template Name. </p>
<p> Specifies the template name to be used for generating the final output.</p>
<dt><code>agarg</code>=<i>ag-opt</i></p>
<dd> AutoGen Argument. This option may appear an unlimited number of times. This option must not appear in combination with any of the following options: output. </p>
<p> This is a pass-through argument. It allows you to specify any arbitrary argument to be passed to AutoGen.</p>
<dt><code>base-name</code>=<i>name</i></p>
<dd> Base name for output file(s). This option must not appear in combination with any of the following options: output. </p>
<p> When output is going to AutoGen, a base name must either be supplied or derived. If this option is not supplied, then it is taken from the <code>template</code> option. If that is not provided either, then it is set to the base name of the current directory.</p>
<dt><code>help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>more-help</code></p>
<dd> Pass the extended usage information through a pager.</p>
<dt><code>save-opts</code>[=<i>cfgfile</i>]</p>
<dd> Save the option state to <i>cfgfile</i>. The default is the <i>last</i> configuration file listed in the <code>OPTION PRESETS</code> section, below. The command will exit after updating the config file.</p>
<dt><code>load-opts</code>=<i>cfgfile</i>,<code> no-load-opts</code></p>
<dd> Load options from <i>cfgfile</i>. The <i>no-load-opts</i> form will disable the loading of earlier config/rc/ini files. <i>&#8211;no-load-opts</i> is handled early, out of order.</p>
<dt><code>version</code>[={<i>v|c|n</i>}]</p>
<dd> Output version of program and exit. The default mode is `v&#8217;, a simple version. The `c&#8217; mode will print copyright information and `n&#8217; will print the full copyright notice.</dl>
<h2>OPTION PRESETS</h2>
<p> Any option that is not marked as <i>not presettable</i> may be preset by loading values from configuration (&quot;RC&quot; or &quot;.INI&quot;) file(s). The <i>homerc</i> file is &quot;<i>/dev/null</i>&quot;, unless that is a directory. In that case, the file &quot;<i>.getdefsrc</i>&quot; is searched for within that directory.</p>
<h2>FILES</h2>
<p> See <code>OPTION PRESETS</code> for configuration files.</p>
<h2>EXIT STATUS</h2>
<p> One of the following exit values will be returned:</p>
<dl>
<dt><code>0</code> (EXIT_SUCCESS)</p>
<dd> Successful program execution.</p>
<dt><code>1</code> (EXIT_FAILURE)</p>
<dd> The operation failed or the command syntax was not valid.</p>
<dt><code>66</code> (EX_NOINPUT)</p>
<dd> A specified configuration file could not be loaded.</p>
<dt><code>70</code> (EX_SOFTWARE)</p>
<dd> libopts had an internal operational error. Please report it to autogen-users [at] lists.sourceforge.net. Thank you.</dl>
<h2>SEE ALSO</h2>
<p> This program is documented more fully in the Getdefs section of the Add-On chapter in the <code>AutoGen</code> Info system documentation.</p>
<h2>AUTHORS</h2>
<p> Bruce Korb</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1999-2012 Bruce Korb all rights reserved. This program is released under the terms of the GNU General Public License, version 3 or later.</p>
<h2>BUGS</h2>
<p> Please send bug reports to: autogen-users [at] lists.sourceforge.net</p>
<h2>NOTES</h2>
<p> This manual page was <i>AutoGen</i>-erated from the <code>getdefs</code> option definitions. </p>
<h2>Index</h2>
