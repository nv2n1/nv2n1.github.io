---
title: "mag(5)"
name: "mag"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mag/"
description: "magic – format of .mag files read/written by Magic"
---

<p>magic &#8211; format of <code>.mag</code> files read/written by Magic</p>
<h2>Description</h2>
<p>Magic uses its own internal ASCII format for storing cells in disk files. Each cell <i>name</i> is stored in its own file, named <i>name</i><code>.mag</code>. The first line in a <code>.mag</code> file is the string </p>
<pre><code>magic</code></pre>
<p>to identify this as a Magic file. The next line is optional and is used to identify the technology in which a cell was designed. If present, it should be of the form </p>
<pre><code>tech</code> <i>techname</i></pre>
<p>If absent, the technology defaults to a system-wide standard, currently <code>nmos</code>. The next line is also optional and gives a timestamp for the cell. The line is of the format </p>
<pre><code>timestamp</code> <i>stamp</i></pre>
<p>where <i>stamp</i> is a number of seconds since 00:00 GMT January 1, 1970 (i.e, the Unix time returned by the library function <i>time()</i>). It should be the last time this cell or any of its children changed. The timestamp is used to detect when a child is edited outside the context of its parent (the parent stores the last timestamp it saw for each of its children; see below). When this occurs, the design-rule checker must recheck the entire area of the child for subcell interaction errors. If this field is omitted in a cell, Magic supplies a default value that forces the rechecks. Next come lines describing the contents of the cell. There are three kinds of groups of lines, describing mask rectangles, subcell uses, and labels. Each group must appear contiguously in the file, but the order between groups is arbitrary. Each group of mask rectangles is headed with a line of the format </p>
<pre><code>&lt;&lt;&nbsp;<wbr></code><i>layer</i><code>&nbsp;<wbr>&gt;&gt;</code></pre>
<p>where <i>layer</i> is a layername known in the current technology (see the <code>tech</code> line above). Each line after this header has the format </p>
<pre><code>rect</code><i> xbot ybot xtop ytop</i></pre>
<p>where <i>(xbot, ybot)</i> is the lower-left corner of the rectangle in Magic (lambda) coordinates, and <i>(xtop, ytop)</i> is the upper-right corner. Degenerate rectangles are not allowed; <i>xbot</i> must be strictly less than <i>xtop</i>, and <i>ybot</i> strictly less than <i>ytop</i>. The smallest legal value of <i>xbot</i> or <i>ybot</i> is <code>-67108858</code>, and the largest legal value for <i>xtop</i> or <i>ytop</i> is <code>67108858</code>. Values that approach these limits (within a factor of 100 or 1000) may cause numerical overflows in Magic even though they are not strictly illegal. We recommend using coordinates around zero as much as possible. Rectangles should be non-overlapping, although this is not essential. They should also already have been merged into maximal horizontal strips (the neighbor to the right or left of a rectangle should not be of the same type), but this is also not essential. The second kind of line group describes a single cell use. Each cell use group is of the following form: </p>
<pre><code>use</code><i> filename use-id</i>
<code>array</code><i> xlo xhi xsep ylo yhi ysep</i>
<code>timestamp</code><i> stamp</i>
<code>transform</code><i> a b c d e f</i>
<code>box</code><i> xbot ybot xtop ytop</i></pre>
<p>A group specifies a single instance of the cell named <i>filename</i>, with instance-identifier <i>use-id</i>. The instance-identifier <i>use-id</i> must be unique among all cells used by this <code>.mag</code> file. If <i>use-id</i> is not specified, a unique one is generated automatically. The <code>array</code> line need only be present if the cell is an array. If so, the X indices run from <i>xlo</i> to <i>xhi</i> inclusive, with elements being separated from each other in the X dimension by <i>xsep</i> lambda. The Y indices run from <i>ylo</i> to <i>yhi</i> inclusive, with elements being separated from each other in the Y dimension by <i>ysep</i> lambda. If <i>xlo</i> and <i>xhi</i> are equal, <i>xsep</i> is ignored; similarly if <i>ylo</i> and <i>yhi</i> are equal, <i>ysep</i> is ignored. The <code>timestamp</code> line is optional; if present, it gives the last time this cell was aware that the child <i>filename</i> changed. If there is no <code>timestamp</code> line, a timestamp of 0 is assumed. When the subcell is read in, this value is compared to the actual value at the beginning of the child cell. If there is a difference, the &#8220;timestamp mismatch&#8221; message is printed, and Magic rechecks design-rules around the child. The <code>transform</code> line gives the geometric transform from coordinates of the child <i>filename</i> into coordinates of the cell being read. The six integers <i>a</i>, <i>b</i>, <i>c</i>, <i>d</i>, <i>e</i>, and <i>f</i> are part of the following transformation matrix, which is used to postmultiply all coordinates in the child <i>filename</i> whenever their coordinates in the parent are required: </p>
<pre><i>a</i> <i>d</i> 0
<i>b</i> <i>e</i> 0
<i>c</i> <i>f</i> 1</pre>
<p>Finally, <code>box</code> gives an estimate of the bounding box of cell <i>filename</i> (covering all the elements of the array if an <code>array</code> line was present), in coordinates of the cell being read. The third kind of line group in a <code>.mag</code> file is a list of labels. It begins with the line </p>
<pre><code>&lt;&lt;&nbsp;<wbr>labels&nbsp;<wbr>&gt;&gt;</code></pre>
<p>and is followed by zero or more lines of the following form: </p>
<pre><code>rlabel</code><i> layer xbot ybot xtop ytop position text</i></pre>
<p>Here <i>layer</i> is the name of one of the layers specified in the technology file for this cell. The label is attached to material of this type. <i>Layer</i> may be <code>space</code>, in which case the label is not considered to be attached to any layer. Labels are rectangular. The lower-left corner of the label (the part attached to any geometry if <i>layer</i> is non-<code>space</code>) is at <i>(xbot, ybot)</i>, and the upper-right corner at <i>(xtop, ytop)</i>. The width of the rectangle or its height may be zero. In fact, most labels in Magic have a lower-left equal to their upper right. The text of the label, <i>text</i>, may be any sequence of characters not including a newline. This text is located at one of nine possible orientations relative to the center of the label&#8217;s rectangle. <i>Position</i> is an integer between 0 and 8, each of which corresponds to a different orientation: </p>
<pre><code>0</code> center
<code>1</code> north
<code>2</code> northeast
<code>3</code> east
<code>4</code> southeast
<code>5</code> south
<code>6</code> southwest
<code>7</code> west
<code>8</code> northwest</pre>
<p>A <code>.mag</code> file is terminated by the line </p>
<pre><code>&lt;&lt;&nbsp;<wbr>end&nbsp;<wbr>&gt;&gt;</code></pre>
<p>Everything following this line is ignored. Any line beginning with a pound sigh (&#8220;<code>#</code>&#8221;) is considered to be a comment and ignored. Beware, however, that these comments are discarded by Magic when it reads a cell, so if that cell is written again by Magic, the comments will be lost. </p>
<h2>Note For Programs That Generate Magic Files</h2>
<p>Magic&#8217;s incremental design rule checker expects that every cell is either completely checked, or contains information to tell the checker which areas of the cell have yet to be examined for design-rule violations. To make sure that the design-rule checker verifies all the material that has been generated for a cell, programs that generate <code>.mag</code> files should place the following rectangle in each file: </p>
<pre><code>&lt;&lt; checkpaint &gt;&gt;</code>
<code>rect </code><i>xbot ybot xtop ytop</i></pre>
<p>This rectangle may appear anywhere a list of rectangles is allowed; immediately following the <code>timestamp</code> line at the beginning of a <code>.mag</code> file is a good place. The coordinates <i>xbot</i> etc. should be large enough to completely cover anything in the cell, and must surround all this material by at least one lambda. Be careful, however, not to make this area too ridiculously large. For example, if you use the maximum and minimum legal tile coordinates, it will take the design-rule checker an extremely long time to recheck the area.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-magic/">magic</a>(1) </p>
