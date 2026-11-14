---
title: "prerex(1)"
name: "prerex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prerex/"
description: "prerex – interactive editor of prerequisite-chart descriptions"
---

<h2 class="name">NAME</h2>
<p> prerex &#8211; interactive editor of prerequisite-chart descriptions </p>
<h2>SYNOPSIS</h2>
<p> <code>prerex</code> [ <i>options</i> ] [ <i>basefile</i>[<i>.tex</i>] [ <i>chartfile</i>[<i>.tex</i>] ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>prerex</code> is an interactive program for editing prerequisite-chart descriptions in the <code><a href="/docs/linux/man/5-prerex/">prerex</a></code>(5) format. The user does not normally have to be familiar with details of the format. The editor supports add, remove, cut-and-paste, and edit operations on diagram elements, and vertical or horizontal shifts of a list of specified elements, all the elements in a rectangular region, or the entire diagram. The edited diagram may be saved, re-processed, and viewed in a PDF viewer, without exiting the editor. Alternatively, <code><a href="/docs/linux/man/1-vprerex/">vprerex</a></code>(1) will open a <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) window and display the corresponding PDF file alongside.</p>
<h2>TERMINOLOGY</h2>
<p> A prerequisite chart consists of several <i>course boxes,</i> linked by <i>arrows.</i> Courses are either <i>half</i> or <i>full,</i> and may be <i>required </i> or <i>optional </i> (or neither). Each course box contains a course <i>code</i> (upper left corner), a course <i>title</i> (lower half), and <i>timetable</i> information (upper right corner). An arrow is either a <i>prerequisite </i> (solid), a <i>corequisite </i> (dotted), or <i>recommended </i> (dashed). When a conventional arrow would be inappropriate, a <i>mini </i> course just above a target box may be used. A line of text may have been placed anywhere in the chart. </p>
<p> In some implementations of the <code><a href="/docs/linux/man/5-prerex/">prerex</a></code>(5) format, (some) arrows may be curved and by default have non-zero curvature. The curvature of individual arrows may be edited using the <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) editor. Negative curvatures are supported. To modify the default curvature (or set it to zero), see <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7).</p>
<h2>COORDINATE SYSTEM</h2>
<p> A conventional two-dimensional coordinate system is used to specify the locations of diagram elements; the origin (where <i>x = 0</i> and <i>y = 0</i>) is at the lower-left corner of the diagram. For convenience, a coordinate grid is normally displayed in the background while a diagram is being edited. </p>
<p> The coordinates of a <i>box,</i> <i>mini,</i> or <i>text-line</i> are those of its centre point. An <i>arrow </i> is described by the coordinates of the centre points of its source and target boxes/minis/text-lines. </p>
<p> The notation <i>x0,y0</i><code>:</code><i>x1,y1</i> denotes all the nodes (course boxes, minis, texts) in the rectangle whose northwest and southeast corners are at coordinates <i>x0,y0 </i>and<i> x1,y1.</i></p>
<h2>USAGE</h2>
<p> If <code>prerex</code> is invoked on one existing file, a back-up copy is made of it, the <i>x,y</i> coordinate grid is turned on, the file is processed by using a system call to <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1), and then the user gets a command summary and an interactive prompt of the form</p>
<dl>
<dt>
<dd> <i>file.tex&gt;</i></dl>
<p> If no file argument is given on the command line, the user is prompted to supply a file name. In either case, if the file name provided does not have a <i>.tex </i> extension, <i>.tex</i> is appended to it. </p>
<p> If the <i>file.tex </i> file named does <i>not </i> already exist, a new &quot;empty&quot; chart file with that name is created, and then it is processed as above. </p>
<p> If a <i>second </i> filename is provided, the first filename is treated as the base file of a LaTeX document and the second as an included file that contains the <i>chart </i> environment to be edited. This allows more than one document to share an included chart file and allows more than one chart to be included in a single document. </p>
<p> The user may enter commands at the interactive command prompt as follows:</p>
<dl>
<dt><code>box</code><i> x,y</i></p>
<dd> edit a course box at <i>x,y, </i> if necessary, creating a new course box there</p>
<dt><code>mini</code><i> x,y</i></p>
<dd> edit a mini at <i>x,y,</i> if necessary, creating a new mini there</p>
<dt><code>text</code><i> x,y</i></p>
<dd> edit a text-line at <i>x,y,</i> if necessary, creating a new text-line there</p>
<dt><code>arrow</code><i> x0,y0,x1,y1</i></p>
<dd> edit an arrow from <i>x0,y0 </i> to <i>x1,y1,</i> if necessary, creating a new such arrow</p>
<dt><code>cut</code><i> xi,yi &#8230; </i></p>
<dd> (temporarily) remove the box, mini, or text at <i>xi,yi </i> (including arrows into/out of the box/mini/text)</p>
<dt><code>paste [</code><i>x,y</i><code>]</code></p>
<dd> re-insert most recently cut but not yet pasted box, mini, or text at <i>x,y </i> (including arrows into/out of the box/mini/text), or at the original coordinates if <i> x,y</i> omitted</p>
<dt><code>xchange</code><i> x0,y0 x1,y1</i></p>
<dd> exchange the box, mini or text at <i>x0,y0</i> with that at <i>x1,y1.</i> This is implemented as a sequence of two cuts followed by two pastes to the same points.</p>
<dt><code>delete [ </code><i>x,y</i><code> | </code><i>x0,y0,x1,y1</i><code> | </code><i>x0,y0</i><code>:</code><i>x1,y1</i><code> ] </code><i>&#8230;</i></p>
<dd> remove the specified boxes, minis, texts, or arrows (including automatically all arrows into/out of each box/mini/text)</p>
<dt><code>undo</code></p>
<dd> undo the most recent editing command (not already undone)</p>
<dt><code>shift [-]</code><i>s</i><code> [ </code><i>x,y</i><code> | </code><i>x0,y0</i><code>:</code><i>x1,y1</i><code> ] </code><i>&#8230;</i></p>
<dd> move specified diagram elements <i>x </i> units right [left]; if no elements are specified, the whole diagram is shifted</p>
<dt><code>raise [-]</code><i>r</i><code> [ </code><i>x,y</i><code> | </code><i>x0,y0</i><code>:</code><i>x1,y1</i><code> ] </code><i>&#8230;</i></p>
<dd> move specified diagram elements <i>y </i> units up [down]; if no elements are specified, the whole diagram is raised</p>
<dt><code>write, ! </code></p>
<dd> save to the current <i>chartfile.tex</i> and process the chart by calling <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1) on the base file.</p>
<dt><code>quit, exit, x, ^D </code></p>
<dd> turn off the coordinate grid, restore write-access, save to the current <i>chartfile.tex,</i> process the base file and exit.</p>
<dt><code>!</code><i>cmd</i></p>
<dd> restore write access to <i>chartfile.tex, </i> execute shell command <i>cmd,</i> re-load and re-process the base file (in case the command changed anything), and remove write-access.</p>
<dt><code>Backup</code></p>
<dd> copy the current <i>chartfile.tex</i> to the back-up file <i>.chartfile.tex;</i> equivalent to <code>!cp</code><i> chartfile.tex .chartfile.tex</i></p>
<dt><code>Restore</code></p>
<dd> delete the current <i>chartfile.tex </i> and editing buffer, and replace them using the current back-up in <i>.chartfile.tex.</i></p>
<dt><code>grid</code> [y/n]</p>
<dd> turn on/off coordinate-grid background</p>
<dt><code>help, ?</code></p>
<dd> print a command summary</dl>
<p> After most editing commands, the editing buffer is automatically saved to <i>chartfile.tex</i> and the basefile is processed; the <code>cut</code> and <code>paste</code> commands are exceptions: saving and processing take place only when all outstanding cuts have been pasted. Saving and processing can be <i>forced </i> by using the <code>write </code> (or <code>!</code>) command, or <i>suppressed </i> for all commands (except <code>write</code> and <code>!</code>) by appending a &quot;;&quot; to the command immediately prior to entering it. To exit the editor <i>without</i> saving to the current <i>chartfile.tex</i>, use <code>quit; </code> (.i.e., <code>quit</code> followed by a semi-colon) or a similar combination. Starting in Version 3.8, <code>^C</code> and other interrupts result in the editing buffer being saved to <i>chartfile.tex</i> before the editor is exited.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> output program name and version number, and quit</p>
<dt><code>-h</code></p>
<dd> output usage summary and quit</dl>
<h2>NOTES</h2>
<p> The main difference between <code>mini </code> and <code>text </code> is in the maximum lengths for the text displayed; the latter allows a full line of text, not merely a course code. Also a text-line does not have an associated URI (when the grid is off). The text &quot;line&quot; may actually be displayed as a paragraph by using a LaTeX \parbox. </p>
<p> To save the current state of <i>chartfile.tex, </i> use <code>Backup</code> or a comparable shell command. A history list of interpreted commands is maintained and is accessible using the up-arrow key. </p>
<p> If processing of the chart fails, <code>prerex</code> will attempt to display the LaTeX error message from the log file. The chart file can be fixed using a conventional text editor or LaTeX-oriented editor. LaTeX processing should fail only if there is an initial problem or if ill-formed LaTeX markup has been inserted into a text field. </p>
<p> Any (non-empty) prefix of a command suffices; for example, <code>q</code>, <code>qu</code>, or <code>qui </code> may be used instead of <code>quit</code>. Some of the commands will begin a dialogue with the user in order to fill in or modify properties; the prompts should be self-explanatory. </p>
<p> Since version 5.5, <code>prerex</code> no longer automatically calls a PDF viewer (because it may be embedded in an instance of <code><a href="/docs/linux/man/1-vprerex/">vprerex</a></code>(1) which already provides a PDF display). If <code>prerex </code> is being used by itself, a PDF viewer may be invoked using the <code>!</code><i>cmd</i> shell-escape mechanism. Also, <code>prerex</code> no longer interacts with the user until a PDF file is available; this is for use with <code><a href="/docs/linux/man/1-vprerex/">vprerex</a></code>(1). For example, if the .tex file is initially read-only, <code>prerex</code> aborts.</p>
<h2>FILES</h2>
<p> A LaTeX style file <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7) that implements the macro calls defined by the <code><a href="/docs/linux/man/5-prerex/">prerex</a></code>(5) format must be available to <code>[pdf]<a href="/docs/linux/man/1-latex/">latex</a></code>(1) to process the chart file. Before any editing is allowed, <i>chartfile.tex</i> is copied to <i>.chartfile.tex</i> as a backup.</p>
<h2>ENVIRONMENT</h2>
<p> The most convenient viewing program to use with <code>prerex</code> is one like <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1), <code><a href="/docs/linux/man/1-gsview/">gsview</a></code>(1), <code><a href="/docs/linux/man/1-kghostview/">kghostview</a>(1),</code> <code><a href="/docs/linux/man/1-kpdf/">kpdf</a></code>(1) or <code><a href="/docs/linux/man/1-okular/">okular</a></code>(1) that may be configured to &quot;watch&quot; the pdf file and re-load the display automatically when the file changes. <code><a href="/docs/linux/man/1-evince/">evince</a></code>(1) has a Reload button and <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1) supports re-loading using the keystroke &quot;R&quot;, but re-loading is much less convenient with <code><a href="/docs/linux/man/1-acroread/">acroread</a></code>(1) and <code><a href="/docs/linux/man/1-gpdf/">gpdf</a></code>(1), which may have to be re-started. </p>
<p> Recent versions of some PDF viewers show the URIs of hyperlinks in a tooltip or in the status bar; this mechanism is used by some implementations of <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7) to allow display of the coordinates of a box, mini, text-line, or arrow when the mouse hovers over it (while the coordinate grid is on and the relevant chart file is presumably being edited). </p>
<p> The <code>prerex</code> package at <code><a rel="nofollow" href="http://www.ctan.org/tex-archive/graphics/prerex/">http://www.ctan.org/tex-archive/graphics/prerex/</a></code> has source code for <code><a href="/docs/linux/man/1-vprerex/">vprerex</a></code>(1), a GUI front-end for <code>prerex</code> which is prerex-enabled.</p>
<h2>BUGS</h2>
<p> <code>prerex </code> analyzes chart files without using TeX; thus, macro calls are <i>not</i> expanded, and anything in the chart file before or after the (first) <code>egin{chart} &#8230; nd{chart} </code> environment is ignored (but preserved) by the editor. Lines that begin with &quot;%&quot; within the chart environment are preserved but other comments within the chart environment are <i>not</i> preserved and may interfere with command parsing. </p>
<p> From version 5.6, <code>prerex</code> no longer supports the latex -&gt; dvips -&gt; ps2pdf toolchain as an option.</p>
<h2>AUTHOR</h2>
<p> R. D. Tennent (rdt [at] cs.queensu.ca)</p>
<h2>DEPENDENCIES</h2>
<p> <code>prerex</code> uses the <code><a href="/docs/linux/man/3-editline/">editline</a></code>(3) library if available and the GNU <code><a href="/docs/linux/man/3-readline/">readline</a></code>(3) and <code><a href="/docs/linux/man/3-history/">history</a></code>(3) libraries otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-acroread/">acroread</a></code>(1), <code><a href="/docs/linux/man/1-evince/">evince</a></code>(1), <code><a href="/docs/linux/man/1-gpdf/">gpdf</a></code>(1), <code><a href="/docs/linux/man/1-gsview/">gsview</a></code>(1), <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1), <code><a href="/docs/linux/man/1-kghostview/">kghostview</a></code>(1), <code><a href="/docs/linux/man/1-kpdf/">kpdf</a></code>(1), <code><a href="/docs/linux/man/1-okular/">okular</a></code>(1), <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1), <code><a href="/docs/linux/man/5-prerex/">prerex</a></code>(5), <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7), <code><a href="/docs/linux/man/1-previewer/">previewer</a></code>(1), <code><a href="/docs/linux/man/1-vprerex/">vprerex</a></code>(1), <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1). </p>
<h2>Index</h2>
