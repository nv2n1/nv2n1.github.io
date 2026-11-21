---

title: "prerex(5)"
name: "prerex"
section: "5"
letter: "p"
url: "/docs/linux/man/5-prerex/"
description: "prerex_format — a format for prerequisite-chart descriptions"
---

<p>prerex_format -- a format for prerequisite-chart descriptions </p>
<p> This manual describes the format of prerequisite-chart descriptions that can be processed by <code>[pdf]latex</code> (normally using a suitable <code>prerex.sty</code>(7) style file) and edited using the <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) interactive editor (or by any conventional text editor).  </p>
<h2>TERMINOLOGY</h2>
<p> A prerequisite chart consists of a number of <i>course boxes,</i> linked by <i>arrows.</i> Courses are either <i>half</i> or <i>full,</i> and may be <i>required</i> or <i>optional</i> (or neither). Each course box can contain a course <i>code</i> (upper left corner), a course <i>title</i> (lower half), and <i>timetable</i> information (upper right corner). An arrow can be either a <i>prerequisite </i> (solid), a <i>corequisite </i> (dotted), or <i>recommended</i> (dashed). When a conventional arrow would be inappropriate, a <i>mini </i> course just above a target box can be used.  </p>
<h2>STRUCTURE</h2>
<p> The file should contain exactly one instance of a LaTeX environment </p>
<p> <code>\begin{chart}</code><i> instruction ... </i><code>\end{chart}</code> </p>
<p>with at most one <i>instruction</i> per line. Note that a program such as <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) analyzes prerex-format files <i>without </i> using TeX; for example, macro definitions will be ignored and macro calls will not be expanded. </p>
<p>Instructions may be preceded by white space. Lines that start with % are treated as comments and ignored. The order of instructions is not significant except that the instruction for the source and target box o an arrow should <i>precede</i> the instruction for the arrow. The instruction formats are described in the following sections.  </p>
<h2>COURSE BOXES</h2>
<p> The instructions producing course boxes have the following forms: </p>
<dl>
<dt><code>\halfcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></dt>
<dt><code>\fullcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></dt>
<dt><code>\reqhalfcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></dt>
<dt><code>\reqfullcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></dt>
<dt><code>\opthalfcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></dt>
<dt><code>\optfullcourse</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}</code></dt>
</dl>
<dd> <p> where <i>x,y</i> are the coordinates of the <i>centerpoint </i> of the box, relative to the origin of the coordinate system at the lower-left corner of the diagram. The <i>code,</i> <i>title,</i> and <i>timetable</i> arguments are arbitrary (well-bracketed) text, possibly with LaTeX markup. </p>
<p>The following are similar but take an additional argument to specify the (non-default) background color of the course box: </p>
 </dd>
<dl>
<dd> <p> <code>\halfcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code> </p>
 </dd>
<dd> <p> <code>\fullcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code> </p>
 </dd>
<dd> <p> <code>\reqhalfcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code> </p>
 </dd>
<dd> <p> <code>\reqfullcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code> </p>
 </dd>
<dd> <p> <code>\opthalfcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code> </p>
 </dd>
<dd> <p> <code>\optfullcoursec</code><i> x,y</i><code>:{</code><i>code</i><code>}{</code><i>title</i><code>}{</code><i>timetable</i><code>}{</code><i>color</i><code>}</code> </p>
 </dd></dl>
<h2>MINI COURSE BOXES AND TEXT</h2>
<p> A mini course is produced by an instruction of the form </p>
<dl>
<dt><code>\mini</code><i> x,y</i><code>:{</code><i>code</i><code>}</code></dt>
<dd> <p> A text line is inserted into the chart by an instruction of the form </p>
 </dd>
<dt><code>\text</code><i> x,y</i><code>:{</code><i>line-of-text</i><code>}</code></dt>
<dd> <p> The maximum allowed length of a course-code may be smaller that the maximum allowed for a line of text. </p>
 </dd></dl>
<h2>ARROWS</h2>
<p> Arrows between course boxes (or from a mini to a course box) are produced by instructions of the form </p>
<dl>
<dt><code>\prereq</code><i> x0,y0,x1,y1</i><code>:</code></dt>
<dt><code>\coreq</code><i> x0,y0,x1,y1</i><code>:</code></dt>
<dt><code>\recomm</code><i> x0,y0,x1,y1</i><code>:</code></dt>
</dl>
<dd> <p> These produce, respectively, solid, dotted, and dashed arrows from the course box (or mini) centered at coordinates <i>x0,y0</i> to the course box centered at coordinates <i>x1,y1.</i> </p>
<p>In some implementations, certain arrows by default have a non-zero curvature. It is possible to override the default curvature for a particular arrow by using the instructions </p>
 </dd>
<dl>
<dt><code>\prereqc</code><i> x0,y0,x1,y1;c</i><code>:</code></dt>
<dt><code>\coreqc</code><i> x0,y0,x1,y1;c</i><code>:</code></dt>
<dt><code>\recommc</code><i> x0,y0,x1,y1;c</i><code>:</code></dt>
</dl>
<dd> <p> where <i>c</i> is an integer in the range -100:100 specifying the desired curvature; for example, <i>c=</i>0 will produce a <i>straight </i> arrow. To change the default curvature, the user program may redefine the <code>\DefaultCurvature</code> command.  </p>
<h2>COORDINATE GRID</h2>
<p> The following instruction produces a coordinate grid, which is useful for editing a diagram: </p>
 </dd>
<dl>
<dt><code>\grid </code></dt>
</dl>
<dd> <p> This is normally placed before all the other instructions so that grid lines are in the background, covered by course boxes, minis, and arrows.  </p>
<h2>WEB LINKS</h2>
<p> Course boxes may be linked to web addresses. The URL for course boxes may be set by the user by redefining the <code>\CourseURL </code> command; when called for a course box, it is supplied with three arguments, the <i>x</i> and <i>y</i> coordinates of the box, mini, or textline, and the <i>code</i> argument of the course box. For example, </p>
 </dd>
<dl>
<dt><code>\renewcommand{\CourseURL}[3]{<a rel="nofollow" href="http://www.cs.queensu.ca/undergraduate/courses/#3.html}">http://www.cs.queensu.ca/undergraduate/courses/#3.html}</a></code></dt>
</dl>
<dd> <p> is appropriate for courses at the School of Computing, Queen&#8217;s University. The first two arguments can be used to display the coordinates of a box, mini, or textline in some PDF viewers while the mouse hovers over it when the source file is being edited.  </p>
<h2>AUTHOR</h2>
<p> R. D. Tennent (rdt [at] cs.queensu.ca)  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1), <code>prerex.sty</code>(7). </p>
