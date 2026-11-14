---
title: "spi_modifytuple(3)"
name: "spi_modifytuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spi_modifytuple/"
description: "SPI_modifytuple – create a row by replacing selected fields of a given row"
---

<p>SPI_modifytuple &#8211; create a row by replacing selected fields of a given row </p>
<h2>Synopsis</h2>
<pre>HeapTuple SPI_modifytuple(Relation <i>rel</i>, HeapTuple <i>row</i>, int <i>ncols</i>,
 int * <i>colnum</i>, Datum * <i>values</i>, const char * <i>nulls</i>)</pre>
<h2>Description</h2>
<p><code>SPI_modifytuple</code> creates a new row by substituting new values for selected columns, copying the original row&#8217;s columns at other positions. The input row is not modified.</p>
<h2>Arguments</h2>
<p>Relation <i>rel</i></p>
<dl COMPACT>
<dd>Used only as the source of the row descriptor for the row. (Passing a relation rather than a row descriptor is a misfeature.)</dl>
<p> HeapTuple <i>row</i></p>
<dl COMPACT>
<dd>row to be modified</dl>
<p> int <i>ncols</i></p>
<dl COMPACT>
<dd>number of column numbers in the array <i>colnum</i></dl>
<p> int * <i>colnum</i></p>
<dl COMPACT>
<dd>array of the numbers of the columns that are to be changed (column numbers start at 1)</dl>
<p> Datum * <i>values</i></p>
<dl COMPACT>
<dd>new values for the specified columns</dl>
<p> const char * <i>Nulls</i></p>
<dl COMPACT>
<dd>which new values are null, if any (see <code>SPI_execute_plan</code> for the format)</dl>
<h2>Return Value</h2>
<p>new row with modifications, allocated in the upper executor context; NULL only if <i>row</i> is NULL </p>
<p> On error, <i>SPI_result</i> is set as follows: </p>
<p> SPI_ERROR_ARGUMENT</p>
<dl COMPACT>
<dd>if <i>rel</i> is NULL, or if <i>row</i> is NULL, or if <i>ncols</i> is less than or equal to 0, or if <i>colnum</i> is NULL, or if <i>values</i> is NULL.</dl>
<p> SPI_ERROR_NOATTRIBUTE</p>
<dl COMPACT>
<dd>if <i>colnum</i> contains an invalid column number (less than or equal to 0 or greater than the number of column in <i>row</i>)</dl>
