---
title: "pdfroff(1)"
name: "pdfroff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfroff/"
description: "pdfroff – create PDF documents using groff"
---

<h2 class="name">NAME</h2>
<p> pdfroff &#8211; create PDF documents using groff </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-abcegilpstzCEGNRSUVXZ</code> ] [ <code>-d </code><i>cs</i> ] [ <code>-f </code><i>fam</i> ] [ <code>-F </code><i>dir</i> ] [ <code>-I </code><i>dir</i> ] [ <code>-L </code><i>arg</i> ] [ <code>-m </code><i>name</i> ] [ <code>-M </code><i>dir</i> ] [ <code>-n </code><i>num</i> ] [ <code>-o </code><i>list</i> ] [ <code>-P </code><i>arg</i> ] [ <code>-r </code><i>cn</i> ] [ <code>-T </code><i>dev</i> ] [ <code>-w </code><i>name</i> ] [ <code>-W </code><i>name</i> ] [ <code>&#8211;emit-ps</code> ] [ <code>&#8211;no-toc-relocation</code> ] [ <code>&#8211;no-kill-null-pages</code> ] [<code>&#8211;stylesheet=</code><i>name</i>] [ <code>&#8211;no-pdf-output</code> ] [<code>&#8211;pdf-output=</code><i>name</i>] [ <code>&#8211;no-reference-dictionary</code> ] [<code>&#8211;reference-dictionary=</code><i>name</i>] [ <code>&#8211;report-progress</code> ] [ <code>&#8211;keep-temporary-files</code> ] [<i>file</i> &#8230;] <code>-h</code> <code>&#8211;help</code> <code>-v</code> [<i>groff-option</i> &#8230;] <code>&#8211;version</code> [<i>groff-option</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pdfroff</code> is a wrapper program for the GNU text processing system, <code>groff</code>. It transparently handles the mechanics of multiple pass <code>groff</code> processing, when applied to suitably marked up <code>groff</code> source files, such that tables of contents and body text are formatted separately, and are subsequently combined in the correct order, for final publication as a single PDF document. A further optional &#8220;style sheet&#8221; capability is provided; this allows for the definition of content which is required to precede the table of contents, in the published document. </p>
<p> For each invocation of <code>pdfroff</code>, the ultimate <code>groff</code> output stream is post-processed by the GhostScript interpreter, to produce a finished PDF document. </p>
<p> <code>pdfroff</code> makes no assumptions about, and imposes no restrictions on, the use of any <code>groff</code> macro packages which the user may choose to employ, in order to achieve a desired document format; however, it <i>does</i> include specific built in support for the <code>pdfmark</code> macro package, should the user choose to employ it. Specifically, if the <i>pdfhref</i> macro, defined in the <i>pdfmark.tmac</i> package, is used to define public reference marks, or dynamic links to such reference marks, then <code>pdfroff</code> performs as many preformatting <code>groff</code> passes as required, up to a maximum limit of <i>four</i>, in order to compile a document reference dictionary, to resolve references, and to expand the dynamically defined content of links.</p>
<h2>USAGE</h2>
<p> The command line is parsed in accordance with normal GNU conventions, but with one exception &#8212; when specifying any short form option (i.e., a single character option introduced by a single hyphen), and if that option expects an argument, then it <i>must</i> be specified independently (i.e., it may <i>not</i> be appended to any group of other single character short form options). </p>
<p> Long form option names (i.e., those introduced by a double hyphen) may be abbreviated to their minimum length unambiguous initial substring. </p>
<p> Otherwise, <code>pdfroff</code> usage closely mirrors that of <code>groff</code> itself. Indeed, with the exception of the <code>-h</code>, <code>-v</code>, and <code>-T</code><i>&nbsp;dev</i> short form options, and all long form options, which are parsed internally by <code>pdfroff</code>, all options and file name arguments specified on the command line are passed on to <code>groff</code>, to control the formatting of the PDF document. Consequently, <code>pdfroff</code> accepts all options and arguments, as specified in <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), which may also be considered as the definitive reference for all standard <code>pdfroff</code> options and argument usage.</p>
<h2>OPTIONS</h2>
<p> <code>pdfroff</code> accepts all of the short form options (i.e., those introduced by a single hyphen), which are available with <code>groff</code> itself. In most cases, these are simply passed transparently to <code>groff</code>; the following, however, are handled specially by <code>pdfroff</code>.</p>
<dl>
<dt><code>-h</code></p>
<dd> Same as <code>&#8211;help</code>; see below.</p>
<dt><code>-i</code></p>
<dd> Process standard input, after all other specified input files. This is passed transparently to <code>groff</code>, but, if grouped with other options, it <i>must</i> be the first in the group. Hiding it within a group breaks standard input processing, in the multiple pass <code>groff</code> processing context of <code>pdfroff</code>.</p>
<dt><code>-T</code><i>&nbsp;dev</i></p>
<dd> Only <code>-T ps</code> is supported by <code>pdfroff</code>. Attempting to specify any other device causes <code>pdfroff</code> to abort.</p>
<dt><code>-v</code></p>
<dd> Same as <code>&#8211;version</code>; see below.</dl>
<p> See <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) for a description of all other short form options, which are transparently passed through <code>pdfroff</code> to <code>groff</code>. </p>
<p> All long form options (i.e., those introduced by a double hyphen) are interpreted locally by <code>pdfroff</code>; they are <code>not</code> passed on to <code>groff</code>, unless otherwise stated below.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Causes <code>pdfroff</code> to display a summary of the its usage syntax, and supported options, and then exit.</p>
<dt><code>&#8211;emit-ps</code></p>
<dd> Suppresses the final output conversion step, causing <code>pdfroff</code> to emit PostScript output instead of PDF. This may be useful, to capture intermediate PostScript output, when using a specialised postprocessor, such as <i>gpresent</i> for example, in place of the default <i>GhostScript</i> PDF writer.</p>
<dt><code>&#8211;keep-temporary-files</code></p>
<dd> Suppresses the deletion of temporary files, which normally occurs after <code>pdfroff</code> has completed PDF document formatting; this may be useful, when debugging formatting problems.</p>
<dt>
<dd> See section &#8220;Files&#8221; below for a description of the temporary files used by <code>pdfroff</code>.</p>
<dt><code>&#8211;no-pdf-output</code></p>
<dd> May be used with the <code>&#8211;reference-dictionary=</code><i>name</i> option (described below) to eliminate the overhead of PDF formatting, when running <code>pdfroff</code> to create a reference dictionary, for use in a different document.</p>
<dt><code>&#8211;no-reference-dictionary</code></p>
<dd> May be used to eliminate the overhead of creating a reference dictionary, when it is known that the target PDF document contains no public references, created by the <i>pdfhref</i> macro.</p>
<dt><code>&#8211;no-toc-relocation</code></p>
<dd> May be used to eliminate the extra <code>groff</code> processing pass, which is required to generate a table of contents, and relocate it to the start of the PDF document, when processing any document which lacks an automatically generated table of contents.</p>
<dt><code>&#8211;no-kill-null-pages</code></p>
<dd> While preparing for simulation of the manual collation step, which is traditionally required to relocate a <i>table of contents</i> to the start of a document, <code>pdfroff</code> accumulates a number of empty page descriptions into the intermediate <i>PostScript</i> output stream. During the final collation step, these empty pages are normally discarded from the finished document; this option forces <code>pdfroff</code> to leave them in place.</p>
<dt><code>&#8211;pdf-output=</code><i>name</i></p>
<dd> Specifies the name to be used for the resultant PDF document; if unspecified, the PDF output is written to standard output. A future version of <code>pdfroff</code> may use this option, to encode the document name in a generated reference dictionary.</p>
<dt><code>&#8211;reference-dictionary=</code><i>name</i></p>
<dd> Specifies the name to be used for the generated reference dictionary file; if unspecified, the reference dictionary is created in a temporary file, which is deleted when <code>pdfroff</code> completes processing of the current document. This option <i>must</i> be specified, if it is desired to save the reference dictionary, for use in references placed in other PDF documents.</p>
<dt><code>&#8211;report-progress</code></p>
<dd> Causes <code>pdfroff</code> to display an informational message on standard error, at the start of each <code>groff</code> processing pass.</p>
<dt><code>&#8211;stylesheet=</code><i>name</i></p>
<dd> Specifies the name of an <i>input file</i>, to be used as a style sheet for formatting of content, which is to be placed <i>before</i> the table of contents, in the formatted PDF document.</p>
<dt><code>&#8211;version</code></p>
<dd> Causes <code>pdfroff</code> to display a version identification message. The entire command line is then passed transparently to <code>groff</code>, in a <i>one</i> pass operation <i>only</i>, in order to display the associated <code>groff</code> version information, before exiting.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables may be set, and exported, to modify the behaviour of <code>pdfroff</code>.</p>
<dl>
<dt><i>PDFROFF_COLLATE</i></p>
<dd> Specifies the program to be used for collation of the finished PDF document.</p>
<dt>
<dd> This collation step may be required to move <i>tables of contents</i> to the start of the finished PDF document, when formatting with traditional macro packages, which print them at the end. However, users should not normally need to specify <i>PDFROFF_COLLATE</i>, (and indeed, are not encouraged to do so). If unspecified, <code>pdfroff</code> uses <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) by default, which normally suffices.</p>
<dt>
<dd> If <i>PDFROFF_COLLATE</i> <i>is</i> specified, then it must act as a filter, accepting a list of file name arguments, and write its output to the <i>stdout</i> stream, whence it is piped to the <i>PDFROFF_POSTPROCESSOR_COMMAND</i>, to produce the finished PDF output.</p>
<dt>
<dd> When specifying <i>PDFROFF_COLLATE</i>, it is normally necessary to also specify <i>PDFROFF_KILL_NULL_PAGES</i>.</p>
<dt>
<dd> <i>PDFROFF_COLLATE</i> is ignored, if <code>pdfroff</code> is invoked with the <i>&#8211;no-kill-null-pages</i> option.</p>
<dt><i>PDFROFF_KILL_NULL_PAGES</i></p>
<dd> Specifies options to be passed to the <i>PDFROFF_COLLATE</i> program.</p>
<dt>
<dd> It should not normally be necessary to specify <i>PDFROFF_KILL_NULL_PAGES</i>. The internal default is a <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) script, which is intended to remove completely blank pages from the collated output stream, and which should be appropriate in most applications of <code>pdfroff</code>. However, if any alternative to <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1) is specified for <i>PDFROFF_COLLATE</i>, then it is likely that a corresponding alternative specification for <i>PDFROFF_KILL_NULL_PAGES</i> is required.</p>
<dt>
<dd> As in the case of <i>PDFROFF_COLLATE</i>, <i>PDFROFF_KILL_NULL_PAGES</i> is ignored, if <code>pdfroff</code> is invoked with the <i>&#8211;no-kill-null-pages</i> option.</p>
<dt><i>PDFROFF_POSTPROCESSOR_COMMAND</i></p>
<dd> Specifies the command to be used for the final document conversion from PostScript intermediate output to PDF. It must behave as a filter, writing its output to the <i>stdout</i> stream, and must accept an arbitrary number of <i>files &#8230;</i> arguments, with the special case of <i>&#8211;</i> representing the <i>stdin</i> stream.</p>
<dt>
<dd> If unspecified, <i>PDFROFF_POSTPROCESSOR_COMMAND</i> defaults to</p>
<dl>
<dt>
<dd> gs -dBATCH -dQUIET -dNOPAUSE -dSAFER -sDEVICE=pdfwrite \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-sOutputFile=-
</dl>
<dt><i>GROFF_TMPDIR</i></p>
<dd> Identifies the directory in which <code>pdfroff</code> should create temporary files. If <i>GROFF_TMPDIR</i> is <i>not</i> specified, then the variables <i>TMPDIR</i>, <i>TMP</i> and <i>TEMP</i> are considered in turn, as possible temporary file repositories. If none of these are set, then temporary files are created in the current directory.</p>
<dt><i>GROFF_GHOSTSCRIPT_INTERPRETER</i></p>
<dd> Specifies the program to be invoked, when <code>pdfroff</code> converts <code>groff</code> PostScript output to PDF. If <i>PDFROFF_POSTPROCESSOR_COMMAND</i> is specified, then the command name it specifies is <i>implicitly</i> assigned to <i>GROFF_GHOSTSCRIPT_INTERPRETER</i>, overriding any explicit setting specified in the environment. If <i>GROFF_GHOSTSCRIPT_INTERPRETER</i> is not specified, then <code>pdfroff</code> searches the process <i>PATH</i>, looking for a program with any of the well known names for the GhostScript interpreter; if no GhostScript interpreter can be found, <code>pdfroff</code> aborts.</p>
<dt><i>GROFF_AWK_INTERPRETER</i></p>
<dd> Specifies the program to be invoked, when <code>pdfroff</code> is extracting reference dictionary entries from a <code>groff</code> intermediate message stream. If <i>GROFF_AWK_INTERPRETER</i> is not specified, then <code>pdfroff</code> searches the process <i>PATH</i>, looking for any of the preferred programs, &#8216;gawk&#8217;, &#8216;mawk&#8217;, &#8216;nawk&#8217;, and &#8216;awk&#8217;, in this order; if none of these are found, <code>pdfroff</code> issues a warning message, and continue processing; however, in this case, no reference dictionary is created.</p>
<dt><i>OSTYPE</i></p>
<dd> Typically defined automatically by the operating system, <i>OSTYPE</i> is used on Microsoft Win32/MS-DOS platforms <i>only</i>, to infer the default <i>PATH_SEPARATOR</i> character, which is used when parsing the process <i>PATH</i> to search for external helper programs.</p>
<dt><i>PATH_SEPARATOR</i></p>
<dd> If set, <i>PATH_SEPARATOR</i> overrides the default separator character, (&#8216;:&#8217; on POSIX/Unix systems, inferred from <i>OSTYPE</i> on Microsoft Win32/MS-DOS), which is used when parsing the process <i>PATH</i> to search for external helper programs.</p>
<dt><i>SHOW_PROGRESS</i></p>
<dd> If this is set to a non-empty value, then <code>pdfroff</code> always behaves as if the <code>&#8211;report-progress</code> option is specified, on the command line.</dl>
<h2>FILES</h2>
<p> Input and output files for <code>pdfroff</code> may be named according to any convention of the user&#8217;s choice. Typically, input files may be named according to the choice of the principal formatting macro package, e.g., file<i>.ms</i> might be an input file for formatting using the <code>ms</code> macros (<i>s.tmac</i>); normally, the final output file should be named file<i>.pdf</i>. </p>
<p> Temporary files, created by <code>pdfroff</code>, are placed in the file system hierarchy, in or below the directory specified by environment variables (see section &#8220;Environment&#8221; above). If <code><a href="/docs/linux/man/1-mktemp/">mktemp</a></code>(1) is available, it is invoked to create a private subdirectory of the nominated temporary files directory, (with subdirectory name derived from the template <i>pdfroff-XXXXXXXXXX</i>); if this subdirectory is successfully created, the temporary files will be placed within it, otherwise they will be placed directly in the directory nominated in the environment. </p>
<p> All temporary files themselves are named according to the convention <i>pdf</i>$$<i>.</i>*, where <i>$$</i> is the standard shell variable representing the process ID of the <code>pdfroff</code> process itself, and <i>*</i> represents any of the extensions used by <code>pdfroff</code> to identify the following temporary and intermediate files.</p>
<dl>
<dt><i>pdf</i>$$<i>.tmp</i></p>
<dd> A scratch pad file, used to capture reference data emitted by <code>groff</code>, during the <i>reference dictionary</i> compilation phase.</p>
<dt><i>pdf</i>$$<i>.ref</i></p>
<dd> The <i>reference dictionary</i>, as compiled in the last but one pass of the <i>reference dictionary</i> compilation phase; (at the start of the first pass, this file is created empty; in successive passes, it contains the <i>reference dictionary</i> entries, as collected in the preceding pass).</p>
<dt>
<dd> If the <code>&#8211;reference-dictionary</code>=<i>name</i> option is specified, this intermediate file becomes permanent, and is named <i>name</i>, rather than <i>pdf</i>$$<i>.ref</i>.</p>
<dt><i>pdf</i>$$<i>.cmp</i></p>
<dd> Used to collect <i>reference dictionary</i> entries during the active pass of the <i>reference dictionary</i> compilation phase. At the end of any pass, when the content of <i>pdf</i>$$<i>.cmp</i> compares as identical to <i>pdf</i>$$<i>.ref</i>, (or the corresponding file named by the <code>&#8211;reference-dictionary</code>=<i>name</i> option), then <i>reference dictionary</i> compilation is terminated, and the <i>document reference map</i> is appended to this intermediate file, for inclusion in the final formatting passes.</p>
<dt><i>pdf</i>$$<i>.tc</i></p>
<dd> An intermediate <i>PostScript</i> file, in which &#8220;Table of Contents&#8221; entries are collected, to facilitate relocation before the body text, on ultimate output to the <i>GhostScript</i> postprocessor.</p>
<dt><i>pdf</i>$$<i>.ps</i></p>
<dd> An intermediate <i>PostScript</i> file, in which the body text is collected prior to ultimate output to the <i>GhostScript</i> postprocessor, in the proper sequence, <i>after</i> <i>pdf</i>$$<i>.tc</i>.</dl>
<h2>AUTHORS</h2>
<p> <code>pdfroff</code> was written by Keith Marshall</p>
<h2>SEE ALSO</h2>
<p> See <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) for the definitive reference to document formatting with <code>groff</code>. Since <code>pdfroff</code> provides a superset of all <code>groff</code> capabilities, <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) may also be considered to be the definitive reference to all <i>standard</i> capabilities of <code>pdfroff</code>, with this document providing the reference to <code>pdfroff</code>&#8216;s extended features. </p>
<p> While <code>pdfroff</code> imposes neither any restriction on, nor any requirement for, the use of any specific <code>groff</code> macro package, a number of supplied macro packages, and in particular those associated with the package <i>pdfmark.tmac</i>, are best suited for use with <code>pdfroff</code> as the preferred formatter. Detailed documentation on the use of these packages may be found, in PDF format, in the reference guide <code>&#8220;Portable Document Format Publishing with GNU Troff&#8221;</code>, included in the installed documentation set as <i>/usr/:share/:doc/:groff-base/:pdf/pdfmark.pdf.gz</i>. </p>
<h2>Index</h2>
