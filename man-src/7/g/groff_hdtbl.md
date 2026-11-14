---
title: "groff_hdtbl(7)"
name: "groff_hdtbl"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_hdtbl/"
description: "groff_hdtbl – Heidelberger table macros for GNU roff"
---

<p>groff_hdtbl &#8211; Heidelberger table macros for GNU roff</p>
<h2>Description</h2>
<p>The <code>hdtbl</code> macros consist of four base and three optional macros, controlled by about twenty arguments. The syntax is simple and similar to the <code>HTML</code> table model and nearly as flexible: You can write sequences of tokens (macro calls with their arguments and content data), separated by blanks and beginning with a macro call, into the same line to get compact and cleanly arrranged input. An advantage of <code>hdtbl</code> is that the tables are constructed without calling a preprocessor; this means that <code>groff</code>&#8216;s full macro capabilities are available. On the other hand, table processing with <code>hdtbl</code> is much slower than using the <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1) preprocessor. A further advantage is that the HTML-like syntax of <code>hdtbl</code> will be easily converted to HTML; this is not implemented yet.</p>
<h2>Usage</h2>
<p>In this and the next section, we present examples to help users understand the basic workflow of <code>hdtbl</code>. First of all, you must load the <i>hdtbl.tmac</i> file. As with nearly all other groff macro packages, there are two possibilities to do so: Either add the line </p>
<pre><dl><dt><dd></pre>
</dl>
<p> to your <i>roff</i> file before using any macros of the <code>hdtbl</code> package, or add the option </p>
<pre><dl><dt><dd></pre>
</dl>
<p> to the command line of groff (before the document file which contains <code>hdtbl</code> macros). Then you can include on or more tables in your document, where each one must be started and ended with the and macros, respectively. </p>
<p> In this man page, we approximate the result of each example in the <i>tty</i> format to be as generic as possible since <code>hdtbl</code> currently only supports the PS and PDF output devices. </p>
<p> The simplest well-formed table consists of just single calls to the four base table macros in the right order. Here we construct a table with only one cell. </p>
<dl>
<dd></dl>
<p> A <i>tty</i> representation is </p>
<pre><dl><dt><dd>+------------------------------------------------------+
| contents-of-the-table-cell |
+------------------------------------------------------+
</dl></pre>
<p>Equivalent to the above is the following notation. </p>
<dl>
<dd></dl>
<p> By default, the formatted table is inserted into the surrounding text at the place of its definition. If the vertical space isn&#8217;t sufficient, it is placed at the top of the next page. Tables can also be stored for later insertion. </p>
<p> Using as the data for the table cells, a table with two rows and two columns can be written as </p>
<dl>
<dd></dl>
<p> A <i>tty</i> representation is </p>
<pre><dl><dt><dd>+--------------------------+---------------------------+
| 1*1 | 1*2 |
+--------------------------+---------------------------+
| 2*1 | 2*2 |
+--------------------------+---------------------------+
</dl></pre>
<p>Here we see a difference from HTML tables: The number of columns must be explicitly specified using the argument (or indirectly via the argument, see below). </p>
<p> The contents of a table cell is arbitrary; for example, it can be another table, without restriction to the nesting depth. A given table layout can be either constructed with suitably nested tables or with proper arguments to and , controlling column and row spanning. Note, however, that this table </p>
<dl>
<dd></dl>
<p> and this table </p>
<dl>
<dd></dl>
<p> are similar but not identical (the use of is purely cosmetic to get proper indentation). </p>
<p> The first table looks like </p>
<pre><dl><dt><dd>+------------------------------------------------------+
| 1*1 1*2 |
+------------------------------------------------------+
| |
| 2*1 2*2 |
| |
+------------------------------------------------------+
</dl></pre>
<p>and the second one like </p>
<pre><dl><dt><dd>+------------------------------------------------------+
| 1*1 1*2 |
+---------------------------+--------------------------+
| 2*1 | 2*2 |
+---------------------------+--------------------------+
</dl></pre>
<p>Here the latter table in a more compact form. </p>
<dl>
<dd></dl>
<p> If a macro has one or more arguments (see below), and it is not starting a line, everything belonging to this macro including the macro itself must be enclosed in double quotes.</p>
<h2>Macros And Arguments</h2>
<p>The order of macro calls and other tokens follows the HTML model. In the following list, valid predecessors and successors of all <code>hdtbl</code> macros are given, together with the possible arguments. </p>
<p> Macro arguments are separated by blanks. The order of arguments is arbitrary; they are of the form </p>
<dl>
<dd></dl>
<p> or </p>
<dl>
<dd></dl>
<p> with the only exception of the optional argument of the macro , which is the string . Another possible form is </p>
<dl>
<dd></dl>
<p> However, this is limited to the case where the macro is the first one in the line and not already enclosed in double quotes. </p>
<p> Argument values specified below as~ are colors predefined by <code>groff</code> or colors defined by the user with the request. Argument values~ are decimal numbers with or without decimal point. Argument values~ are natural numbers. Argument values~ are numerical values with the usual <code>groff</code> scaling indicators. Some of the arguments are specific to one or two macros, but most of them can be specified with , , , and These common arguments are explained in the next subsection. </p>
<p> Most of the argument default values can be changed by the user by setting corresponding default registers or strings, as listed below.</p>
<dl>
<dd>Begin a new table.</p>
<dd>
<dl>
<dd><code>predecessor:</code><br />
 <code>successor:</code><br />
 <code>arguments:</code> </p>
<dl>
<dd>Thickness of the surrounding box border. (no value) means neither a surrounding box border nor any horizontal or vertical separator lines between the table rows and cells. suppresses the surrounding box border, but still allows separator lines between cells and rows.<br />
 <code>Default:</code> Border color.<br />
 <code>Default:</code> Number of table columns. This argument is necessary if more than one column is in the table and no arguments are present.<br />
 <code>Default:</code> Cell padding, i.e., the extra space between the cell space border and the cell contents.<br />
 <code>Default:</code> Cell spacing, i.e., the extra space between the table border or vertical or horizontal lines between cells and the cellspace.<br />
 <code>Default:</code> Horizontal alignment of the table, if it is smaller than the line width. : left alignment. : centered alignment. : right alignment.<br />
 <code>Default:</code> Widths of table cells. ,<i></i> ,<i></i> ll are either numbers of type~ or natural numbers with the pseudo-scaling indicator , with the meaning &#8220;percent of the actual line length (or column length for inner tables, respectively)&#8221;. If there are less width values than table columns, the last width value is used for the remaining cells. The argument</p>
<dl>
<dd>
<dl>
<dd></dl>
</dl>
<dl>
<dd>for example indicates that the first column is 1.5~inches wide; the remaining columns take 1/10 of the column length each.<br />
 <code>Default:</code> The table width equals the outer line length or column length; the columns have equal widths. Height of the table. If the table with its contents is lower than~ ,<i></i> the last row is stretched to this value.</dl>
</dl>
</dl>
<dd>Text of caption.</p>
<dd>The (optionally numbered) table caption. is optional.</p>
<dd>
<dl>
<dd><code>predecessor:</code><br />
 <code>successor:</code><br />
 <code>arguments:</code> </p>
<dl>
<dd>Vertical alignment of the table caption. : The caption is placed above the table. : The caption is placed below the table.<br />
 <code>Default:</code></dl>
</dl>
<dd>Begin a new table row.</p>
<dd>
<dl>
<dd><code>predecessor:</code><br />
 <code>successor:</code><br />
 <code>arguments:</code> </p>
<dl>
<dd>The height of the row. If a cell in the row is higher than~ ,<i></i> this value is ignored; otherwise the row height is stretched to~ .<i></i></dl>
</dl>
<dd>Begin a table data cell. Begin a table header cell.</p>
<dd>Arguments and cell contents can be mixed. The macro is not really necessary and differs from only in three default settings, similar to the and HTML tags: The contents of is horizontally and vertically centered and typeset in boldface.</p>
<dd>
<dl>
<dd><code>predecessor:</code><br />
 <code>successor:</code><br />
 <code>arguments:</code> </p>
<dl>
<dd>The width of this cell is the sum of the widths of the~ cells above and below this row. The height of this cell is the sum of the heights of the cells left and right of this column.</p>
<dl>
<dd><code>Remark:</code> Overlapping of column and row spanning, as in the following table fragment (the overlapping happens in the second cell in the second row), is invalid and causes incorrect results.</p>
<dl>
<dd>
<dl>
<dd></dl>
</dl>
</dl>
<p> A working example for headers and cells with <code>colspan</code> is </p>
<dl>
<dd></dl>
<p> This looks like </p>
<dl>
<dd>
<pre>+------------------------------+---------------+
| header1+2 | header3 |
+--------------+---------------+---------------+
| 1*1 | 1*2 | 1*3 |
+--------------+---------------+---------------+
| 2*1 | 2*2+3 |
+--------------+-------------------------------+
</dl></pre>
<p>A working example with <code>rowspan</code> is </p>
<dl>
<dd></dl>
<p> which looks like </p>
<dl>
<dd>
<pre>+--------------+---------------+---------------+
| 1*1 | 1+2*2 | 1*3 |
+--------------+ +---------------+
| 2*1 | | 2*3 |
+--------------+---------------+---------------+</pre>
</dl>
</dl>
</dl>
<dd>End of the table.</p>
<dd>This macro finishes a table. It causes one of the following actions.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the argument is given, the table is held until it is freed by calling the macro , which in turn prints the table immediately, either at the current position or at the top of the next page if its height is larger than the remaining space on the page.</p>
<dt>&bull;</p>
<dd>Otherwise, if the table is higher than the remaining space on the page, it is printed at the top of the next page.</p>
<dt>&bull;</p>
<dd>If neither of the two above constraints hold, the table is printed immediately at the place of its definition.</dl>
</dl>
<dd>
<dl>
<dd><code>predecessor:</code><br />
 <code>successor:</code><br />
 <code>arguments:</code> </p>
<dl>
<dd>Prevent the table from being printed until it is freed by calling the macro . This argument is ignored for inner (nested) tables.</dl>
</dl>
<dd>Free the next held table or held<i></i> tables. Call this utility macro to print tables which are held by using the argument of the macro.</dl>
<h3>Arguments common to .TBL, .TR, .TD, and .TH</h3>
<p>The arguments described in this section can be specified with the and macros, but they are eventually passed on to the table cells. If omitted, the defaults take place, which the user can change by setting the corresponding default registers or strings, as documented below. Setting an argument with the macro has the same effect as setting it for all rows in the table. Setting an argument with a macro has the same effect as setting it for all the or macro in this row.</p>
<dl>
<dd>The background color of the table cells. This includes the area specified with the argument. The argument (no value) suppresses a background color; this makes the background transparent.<br />
 <code>Default:</code> The foreground color of the cell contents.<br />
 <code>Default:</code> The font family for the table. is one of the groff font families, for example for the AvantGarde fonts or for Helvetica-Narrow.<br />
 <code>Default:</code> The font family found before the table (string ). The font style for the table. One of , , , or for roman, <code>bold</code>, <i>italic</i>, or bold italic, respectively. As with <code>roff</code>&#8216;s request the argument can be used to specify the font family and font style together, for example instead of and .<br />
 <code>Default:</code> The font style in use right before the table (string ). A decimal or fractional factor ,<i></i> by which the point size for the table is changed, and ,<i></i> by which the vertical line spacing is changed. If is omitted, value is taken for both.<br />
 <code>Default:</code> Horizontal alignment of the cell contents in the table. : left alignment. : centered alignment. : both (left and right) alignment. : right alignment.<br />
 <code>Default:</code> Vertical alignment of the cell contents in the table for cells lower than the current row. : alignment below the top of the cell. : alignment in the middle of the cell. : alignment above the cell bottom.<br />
 <code>Default:</code> Horizontal line between the rows. If specified with or this is a separator line to the cell below. (no value): no separator line. : a single separator line between the rows. : a double separator line.</p>
<dd>The thickness of the separator lines is the half of the border thickness, but at least 0.1~inches. The distance between the double lines is equal to the line thickness.</p>
<dd><code>Remark:</code> Together with for proper formatting the value of must be at least .05~inches for single separator lines and .15~inches for double separator lines.<br />
 <code>Default:</code> Vertical separator line between the cells. If specified with or this is a separator line to the cell on the right. : a single separator line between the cells. : a double separator line. (no value): no vertical cell separator lines. For more information see the documentation of the argument above.<br />
 <code>Default:</code></dl>
<h2>Hdtbl Customization</h2>
<p>Before creating the first table, you should configure default values to minimize the markup needed in each table. The following example sets up defaults suitable for typical papers: </p>
<dl>
<dd></dl>
<p> The file <code>examples/common.roff</code> provides another example setup in the &#8220;minimal Page setup&#8221; section. </p>
<p> A table which does not fit on a partially filled page is printed automatically on the top of the next page if you append the little utility macro to the page header macro of your document&#8217;s main macro package. For example, say </p>
<dl>
<dd></dl>
<p> if you use the <code>ms</code> macro package. </p>
<p> The macro checks for held or kept tables, and for missing macros (table not closed). You can append this macro to the &#8220;end&#8221; macro of your document&#8217;s main macro package. For example: </p>
<dl>
<dd></dl>
<p> If you use the <code>ms</code> macro package.</p>
<h2>Bugs And Suggestions</h2>
<p>Please send your commments to the groff mailing list or directly to the author.</p>
<h2>Authors</h2>
<p>The <code>hdtbl</code> macro package was written by Joachim Walsdorff</p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1)</p>
<dd>provides an overview of GNU <i>roff</i> and details how to invoke <i>groff</i> at the command line.</p>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dd>summarizes the <i>roff</i> language and GNU extensions to it.</p>
<dt><code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1)</p>
<dd>describes the traditional <i>roff</i> preprocessor for tables. </p>
