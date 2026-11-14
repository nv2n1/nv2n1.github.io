---
title: "prerex(5)"
name: "prerex"
section: "5"
letter: "p"
url: "/docs/linux/man/5-prerex/"
description: "prerex_format — a format for prerequisite-chart descriptions"
---

<p>prerex_format &#8212; a format for prerequisite-chart descriptions</p>
<h2>Description</h2>
<p>This manual describes the format of prerequisite-chart descriptions that can be processed by <code>[pdf]latex</code> (normally using a suitable <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7) style file) and edited using the <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) interactive editor (or by any conventional text editor).</p>
<h2>Terminology</h2>
<p>A prerequisite chart consists of a number of <i>course boxes,</i> linked by <i>arrows.</i> Courses are either <i>half</i> or <i>full,</i> and may be <i>required</i> or <i>optional</i> (or neither). Each course box can contain a course <i>code</i> (upper left corner), a course <i>title</i> (lower half), and <i>timetable</i> information (upper right corner). An arrow can be either a <i>prerequisite </i> (solid), a <i>corequisite </i> (dotted), or <i>recommended</i> (dashed). When a conventional arrow would be inappropriate, a <i>mini </i> course just above a target box can be used.</p>
<h2>Structure</h2>
<p>The file should contain exactly one instance of a LaTeX environment </p>
<p> <code>egin{chart}</code><i> instruction &#8230; </i><code>nd{chart}</code> </p>
<p> with at most one <i>instruction</i> per line. Note that a program such as <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) analyzes prerex-format files <i>without </i> using TeX; for example, macro definitions will be ignored and macro calls will not be expanded. </p>
<p> Instructions may be preceded by white space. Lines that start with % are treated as comments and ignored. The order of instructions is not significant except that the instruction for the source and target box o an arrow should <i>precede</i> the instruction for the arrow. The instruction formats are described in the following sections.</p>
<h2>Course Boxes</h2>
<p>The instructions producing course boxes have the following forms:</p>
<dl>
<dt> <code>\halfcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></p>
<dt> <code>ullcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></p>
<dt> <code>eqhalfcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></p>
<dt> <code>eqfullcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></p>
<dt> <code>\opthalfcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></p>
<dt> <code>\optfullcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></dl>
<dd>where <i>x,y</i> are the coordinates of the <i>centerpoint </i> of the box, relative to the origin of the coordinate system at the lower-left corner of the diagram. The <i>code,</i> <i>title,</i> and <i>timetable</i> arguments are arbitrary (well-bracketed) text, possibly with LaTeX markup. </p>
<p> The following are similar but take an additional argument to specify the (non-default) background color of the course box:</p>
<dl>
<dd><code>\halfcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code></p>
<dd><code>ullcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code></p>
<dd><code>eqhalfcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code></p>
<dd><code>eqfullcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code></p>
<dd><code>\opthalfcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code></p>
<dd><code>\optfullcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code></dl>
<h2>Mini Course Boxes And Text</h2>
<p>A mini course is produced by an instruction of the form</p>
<dl>
<dt> <code>\mini</code><i> x,y</i><code>:{</code><i>code</i><code>}</code></p>
<dd>A text line is inserted into the chart by an instruction of the form</p>
<dt> <code>	ext</code><i> x,y</i><code>:{</code><i>line-of-text</i><code>}</code></p>
<dd>The maximum allowed length of a course-code may be smaller that the maximum allowed for a line of text.</dl>
<h2>Arrows</h2>
<p>Arrows between course boxes (or from a mini to a course box) are produced by instructions of the form</p>
<dl>
<dt> <code>\prereq</code><i> x0,y0,x1,y1</i><code>:</code></p>
<dt> <code>
