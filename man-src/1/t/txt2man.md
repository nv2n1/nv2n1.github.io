---

title: "txt2man(1)"
name: "txt2man"
section: "1"
letter: "t"
url: "/docs/linux/man/1-txt2man/"
description: "txt2man – convert flat ASCII text to man page format"
---

<p> <code>txt2man </code>&#8211; convert flat ASCII text to man page format</p>
<h2>SYNOPSIS</h2>
<pre><code>
txt2man[-hpTX][-t mytitle][-P pname][-r rel][-s sect]
       [-v vol][-I txt][-B txt][-d date][ifile]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>txt2man</code> converts the input text into nroff/troff standard <code><a href="/docs/linux/man/7-man/">man</a></code>(7) macros used to format Unix manual pages. Nice pages can be generated specially for commands (section 1 or 8) or for C functions reference (sections 2, 3), with the ability to recognize and format command and function names, flags, types and arguments. </p>
<p> <code>txt2man</code> is also able to recognize and format sections, paragraphs, lists (standard, numbered, description, nested), cross references and literal display blocks. </p>
<p> If input file <i>ifile</i> is omitted, standard input is used. Result is displayed on standard output. </p>
<p> Here is how text patterns are recognized and processed:</p>
<dl>
<dt><code>Sections</code></dt>
<dd> These headers are defined by a line in upper case, starting column 1. If there is one or more leading spaces, a sub-section will be generated instead.</dd>
<dt><code>Paragraphs</code></dt>
<dd> They must be separated by a blank line, and left aligned.</dd>
<dt><code>Tag list</code></dt>
<dd> The item definition is separated from the item description by at least 2 blank spaces, even before a new line, if definition is too long. Definition will be emphasized by default.</dd>
<dt><code>Bullet list</code></dt>
<dd> Bullet list items are defined by the first word being &quot;-&quot; or &quot;*&quot; or &quot;o&quot;.</dd>
<dt><code>Enumerated list</code></dt>
<dd> The first word must be a number followed by a dot.</dd>
<dt><code>Literal display blocks</code></dt>
<dd> This paragraph type is used to display unmodified text, for example source code. It must be separated by a blank line, and be indented. It is primarily used to format unmodified source code. It will be printed using fixed font whenever possible (troff).</dd>
<dt><code>Cross references</code></dt>
<dd> A cross reference (another man page) is defined by a word followed by a number in parenthesis.</dd></dl>
<p> Special sections:</p>
<dl>
<dt><code>NAME</code></dt>
<dd> The function or command name and short description are set in this section.</dd>
<dt><code>SYNOPSIS</code></dt>
<dd> This section receives a special treatment to identify command name, flags and arguments, and propagate corresponding attributes later in the text. If a C like function is recognized (word immediately followed by an open parenthesis), <code>txt2man</code> will print function name in bold font, types in normal font, and variables in italic font. The whole section will be printed using a fixed font family (courier) whenever possible (troff).</dd></dl>
<p> It is a good practice to embed documentation into source code, by using comments or constant text variables. <code>txt2man</code> allows to do that, keeping the document source readable, usable even without further formatting (i.e. for online help) and easy to write. The result is high quality and standard complying document.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> The option <code>-h</code> displays help.</dd>
<dt><code>-d</code> <i>date</i></dt>
<dd> Set <i>date</i> in header. Defaults to current <i>date</i>.</dd>
<dt><code>-P</code> <i>pname</i></dt>
<dd> Set <i>pname</i> as project name in header. Default to uname <code>-s</code>.</dd>
<dt><code>-p</code></dt>
<dd> Probe title, section name and volume.</dd>
<dt><code>-t</code> <i>mytitle</i></dt>
<dd> Set <i>mytitle</i> as title of generated man page.</dd>
<dt><code>-r</code> <i>rel</i></dt>
<dd> Set <i>rel</i> as project name and release.</dd>
<dt><code>-s</code> <i>sect</i></dt>
<dd> Set <i>sect</i> as section in heading, ususally a value from 1 to 8.</dd>
<dt><code>-v</code> <i>vol</i></dt>
<dd> Set <i>vol</i> as volume name, i.e. &quot;Unix user &#8216;s manual&quot;.</dd>
<dt><code>-I</code> <i>txt</i></dt>
<dd> Italicize <i>txt</i> in output. Can be specified more than once.</dd>
<dt><code>-B</code> <i>txt</i></dt>
<dd> Emphasize (bold) <i>txt</i> in output. Can be specified more than once.</dd>
<dt><code>-T</code></dt>
<dd> Text result previewing using PAGER, usually <code><a href="/docs/linux/man/1-more/">more</a></code>(1).</dd>
<dt><code>-X</code></dt>
<dd> X11 result previewing using <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1).</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>PAGER</code></dt>
<dd> name of paging command, usually <code><a href="/docs/linux/man/1-more/">more</a></code>(1), or <code><a href="/docs/linux/man/1-less/">less</a></code>(1). If not set falls back to <code><a href="/docs/linux/man/1-more/">more</a></code>(1).</dd></dl>
<h2>EXAMPLE</h2>
<p> Try this command to format this text itself: </p>
<pre>
      $ txt2man -h 2&gt;&amp;1 | txt2man -T
</pre>
<h2>HINTS</h2>
<p> To obtain an overall good formating of output document, keep paragraphs indented correctly. If you have unwanted bold sections, search for multiple spaces between words, which are used to identify a tag list (term followed by a description). Choose also carefully the name of command line or function parameters, as they will be emphasized each time they are encountered in the document.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code>mandoc</code>(7), <code>rman</code>(1), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-more/">more</a></code>(1), <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1).</p>
<h2>BUGS</h2>
<dl>
<dt>&bull;</dt>
<dd> Automatic probe (<code>-p</code> option) works only if input is a regular file (i.e. not stdin).</dd></dl>
<h2>AUTHOR</h2>
<p> Marc Vertes &lt;mvertes [at] free.fr&gt; </p>
