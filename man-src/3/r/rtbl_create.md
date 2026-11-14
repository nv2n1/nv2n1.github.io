---
title: "rtbl_create(3)"
name: "rtbl_create"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rtbl_create/"
description: "rtbl_create rtbl_destroy rtbl_set_flags rtbl_get_flags rtbl_set_prefix rtbl_set_separator rtbl_set_column_prefix rtbl_set_column_affix_by_id rtbl_add_column rtbl_add_column_by_id rtbl_add_column_en..."
---

<p><code>rtbl_create</code> <code>rtbl_destroy</code> <code>rtbl_set_flags</code> <code>rtbl_get_flags</code> <code>rtbl_set_prefix</code> <code>rtbl_set_separator</code> <code>rtbl_set_column_prefix</code> <code>rtbl_set_column_affix_by_id</code> <code>rtbl_add_column</code> <code>rtbl_add_column_by_id</code> <code>rtbl_add_column_entry</code> <code>rtbl_add_column_entry_by_id</code> <code>rtbl_new_row</code> <code>rtbl_format</code> &#8211; format data in simple tables</p>
<h2>Library</h2>
<p>The roken library (libroken, -lroken)</p>
<h2>Synopsis</h2>
<p>In rtbl.h Ft int Fn rtbl_add_column rtbl_t table const char *column_name unsigned int flags Ft int Fn rtbl_add_column_by_id rtbl_t table unsigned int column_id const char *column_header unsigned int flags Ft int Fn rtbl_add_column_entry rtbl_t table const char *column_name const char *cell_entry Ft int Fn rtbl_add_column_entry_by_id rtbl_t table unsigned int column_id const char *cell_entry Ft rtbl_t Fn rtbl_create void Ft void Fn rtbl_destroy rtbl_t table Ft int Fn rtbl_new_row rtbl_t table Ft int Fn rtbl_set_column_affix_by_id rtbl_t table unsigned int column_id const char *prefix const char *suffix Ft int Fn rtbl_set_column_prefix rtbl_t table const char *column_name const char *prefix Ft unsigned int Fn rtbl_get_flags rtbl_t table Ft void Fn rtbl_set_flags rtbl_t table unsigned int flags Ft int Fn rtbl_set_prefix rtbl_t table const char *prefix Ft int Fn rtbl_set_separator rtbl_t table const char *separator Ft int Fn rtbl_format rtbl_t table FILE *file</p>
<h2>Description</h2>
<p>This set of functions assemble a simple table consisting of rows and columns, allowing it to be printed with certain options. Typical use would be output from tools such as <a href="/docs/linux/man/1-ls/">ls</a>(1) or <a href="/docs/linux/man/1-netstat/">netstat</a>(1), where you have a fixed number of columns, but don&#8217;t know the column widths before hand. </p>
<p> A table is created with Fn rtbl_create and destroyed with Fn rtbl_destroy . </p>
<p> Global flags on the table are set with Fa rtbl_set_flags and retrieved with Fa rtbl_get_flags . At present the only defined flag is <code>RTBL_HEADER_STYLE_NONE</code> which suppresses printing the header. </p>
<p> Before adding data to the table, one or more columns need to be created. This would normally be done with Fn rtbl_add_column_by_id , Fa column_id is any number of your choice (it&#8217;s used only to identify columns), Fa column_header is the header to print at the top of the column, and Fa flags are flags specific to this column. Currently the only defined flag is <code>RTBL_ALIGN_RIGHT</code> aligning column entries to the right. Columns are printed in the order they are added. </p>
<p> There&#8217;s also a way to add columns by column name with Fn rtbl_add_column , but this is less flexible (you need unique header names), and is considered deprecated. </p>
<p> To add data to a column you use Fn rtbl_add_column_entry_by_id , where the Fa column_id is the same as when the column was added (adding data to a non-existent column is undefined), and Fa cell_entry is whatever string you wish to include in that cell. It should not include newlines. For columns added with Fn rtbl_add_column you must use Fn rtbl_add_column_entry instead. </p>
<p> Fn rtbl_new_row fills all columns with blank entries until they all have the same number of rows. </p>
<p> Each column can have a separate prefix and suffix, set with Fa rtbl_set_column_affix_by_id ; Fa rtbl_set_column_prefix allows setting the prefix only by column name. In addition to this, columns may be separated by a string set with Fa rtbl_set_separator ( Ns by default columns are not seprated by anything). </p>
<p> The finished table is printed to Fa file with Fa rtbl_format .</p>
<h2>Examples</h2>
<p>This program: </p>
<pre>#include &lt;stdio.h&gt;
#include &lt;rtbl.h&gt;
int
main(int argc, char **argv)
{
 rtbl_t table;
 table = rtbl_create();
 rtbl_set_separator(table, &quot; &quot;);
 rtbl_add_column_by_id(table, 0, &quot;Column A&quot;, 0);
 rtbl_add_column_by_id(table, 1, &quot;Column B&quot;, RTBL_ALIGN_RIGHT);
 rtbl_add_column_by_id(table, 2, &quot;Column C&quot;, 0);
 rtbl_add_column_entry_by_id(table, 0, &quot;A-1&quot;);
 rtbl_add_column_entry_by_id(table, 0, &quot;A-2&quot;);
 rtbl_add_column_entry_by_id(table, 0, &quot;A-3&quot;);
 rtbl_add_column_entry_by_id(table, 1, &quot;B-1&quot;);
 rtbl_add_column_entry_by_id(table, 2, &quot;C-1&quot;);
 rtbl_add_column_entry_by_id(table, 2, &quot;C-2&quot;);
 rtbl_add_column_entry_by_id(table, 1, &quot;B-2&quot;);
 rtbl_add_column_entry_by_id(table, 1, &quot;B-3&quot;);
 rtbl_add_column_entry_by_id(table, 2, &quot;C-3&quot;);
 rtbl_add_column_entry_by_id(table, 0, &quot;A-4&quot;);
 rtbl_new_row(table);
 rtbl_add_column_entry_by_id(table, 1, &quot;B-4&quot;);
 rtbl_new_row(table);
 rtbl_add_column_entry_by_id(table, 2, &quot;C-4&quot;);
 rtbl_new_row(table);
 rtbl_format(table, stdout);
 rtbl_destroy(table);
 return 0;
}</pre>
<p>will output the following: </p>
<pre>Column A Column B Column C
A-1 B-1 C-1
A-2 B-2 C-2
A-3 B-3 C-3
A-4
 B-4
 C-4</pre>
