---
title: "wmc(1)"
name: "wmc"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmc/"
description: "wmc – Wine Message Compiler"
---

<h2>NAME</h2>
<p> wmc &#8211; Wine Message Compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>wmc</code> [<i>options</i>]&nbsp;<wbr>[<i>inputfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>wmc</code> compiles messages from <code>inputfile</code> into FormatMessage[AW] compatible format encapsulated in a resourcescript format. <code>wmc</code> outputs the data either in a standard <i>.bin</i> formatted binary file, or can generated inline resource data. </p>
<p> <code>wmc</code> takes only one <i>inputfile</i> as argument (see <code>BUGS</code>). The <i>inputfile</i> normally has extension <i>.mc</i>. The messages are read from standard input if no inputfile is given. If the outputfile is not specified with <code>-o</code>, then <code>wmc</code> will write the output to <i>inputfile.{rc,h}</i>. The outputfile is named <i>wmc.tab.{rc,h}</i> if no inputfile was given.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-B&nbsp;<wbr></code><i>x</i></dt>
<dd> Set output byte-order x={n[ative], l[ittle], b[ig]}. Default is n[ative].</dd>
<dt><code>-c</code></dt>
<dd> Set &#8216;custom-bit&#8217; in message-code values.</dd>
<dt><code>-d</code></dt>
<dd> NON-FUNCTIONAL; Use decimal values in output</dd>
<dt><code>-D</code></dt>
<dd> Set debug flag. This results is a parser trace and a lot of extra messages.</dd>
<dt><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code></dt>
<dd> Print an informative usage message and exits.</dd>
<dt><code>-H&nbsp;<wbr></code><i>file</i></dt>
<dd> Write headerfile to <i>file</i>. Default is <i>inputfile.h</i>.</dd>
<dt><code>-i</code></dt>
<dd> Inline messagetable(s). This option skips the generation of all <i>.bin</i> files and writes all output into the <i>.rc</i> file. This encoding is parsable with <a href="/docs/linux/man/1-wrc/">wrc</a>(1).</dd>
<dt><code>-o</code>,&nbsp;<wbr><code>&#8211;output</code>=<i>file</i></dt>
<dd> Output to <i>file</i>. Default is <i>inputfile.rc</i>.</dd>
<dt><code>-O</code>,&nbsp;<wbr><code>&#8211;output-format</code>=<i>format</i></dt>
<dd> Set the output format. Supported formats are <code>rc</code> (the default), <code>res</code>, and <code>pot</code>.</dd>
<dt><code>-P</code>,&nbsp;<wbr><code>&#8211;po-dir</code>=<i>directory</i></dt>
<dd> Enable the generation of resource translations based on po files loaded from the specified directory. That directory must follow the gettext convention, in particular in must contain one <i>.po</i> file for each language, and a LINGUAS file listing the available languages.</dd>
<dt><code>-u</code></dt>
<dd> Assume that the inputfile is in unicode.</dd>
<dt><code>-U</code></dt>
<dd> Write resource output in unicode formatted messagetable(s).</dd>
<dt><code>-v</code></dt>
<dd> Show all supported codepages and languages.</dd>
<dt><code>-V</code>,&nbsp;<wbr><code>&#8211;version</code></dt>
<dd> Print version end exit.</dd>
<dt><code>-W</code>,&nbsp;<wbr><code>&#8211;pedantic</code></dt>
<dd> Enable pedantic warnings.</dd></dl>
<h2>EXTENSIONS</h2>
<p> The original syntax is extended to support codepages more smoothly. Normally, codepages are based on the DOS codepage from the language setting. The original syntax only allows the destination codepage to be set. However, this is not enough for non-DOS systems which do not use unicode source-files. </p>
<p> A new keyword <code>Codepages</code> is introduced to set both input and output codepages to anything one wants for each language. The syntax is similar to the other constructs: </p>
<p> Codepages &#8216;=&#8217; &#8216;(&#8216; language &#8216;=&#8217; cpin &#8216;:&#8217; cpout &#8230; &#8216;)&#8217; </p>
<p> The <i>language</i> is the numerical language-ID or the alias set with LanguageNames. The input codepage <i>cpin</i> and output codepage <i>cpout</i> are the numerical codepage IDs. There can be multiple mappings within the definition and the definition may occur more than once.</p>
<h2>AUTHORS</h2>
<p> <code>wmc</code> was written by Bertho A. Stultiens.</p>
<h2>BUGS</h2>
<p> The message compiler should be able to have multiple input files and combine them into one output file. This would enable the splitting of languages into separate files. </p>
<p> Unicode detection of the input is suboptimal, to say the least. It should recognize byte order marks (BOM) and decide what to do. </p>
<p> Decimal output is completely lacking. Don&#8217;t know whether it should be implemented because it is a, well, non-informative format change. It is recognized on the commandline for some form of compatibility. </p>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>wmc</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1), <code><a href="/docs/linux/man/1-wrc/">wrc</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
