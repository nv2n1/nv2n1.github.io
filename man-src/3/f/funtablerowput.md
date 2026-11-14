---
title: "funtablerowput(3)"
name: "funtablerowput"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funtablerowput/"
description: "FunTableRowPut – put Funtools rows"
---

<h2>NAME</h2>
<p> <code>FunTableRowPut &#8211; put Funtools rows</code></p>
<h2>SYNOPSIS</h2>
<p> int FunTableRowPut(Fun fun, void *rows, int nev, int idx, char *plist)</p>
<h2>DESCRIPTION</h2>
<p> The FunTableRowPut() routine writes rows to a <font SIZE="-1">FITS</font> binary table, taking its input from an array of user structs that contain column values selected by a previous call to <i>FunColumnSelect()</i>. Selected column values are automatically converted from native data format to <font SIZE="-1">FITS</font> data format as necessary. </p>
<p> The first argument is the Fun handle associated with this row data. The second <code>rows</code> argument is the array of user structs to output. The third <code>nrow</code> argument specifies the number number of rows to write. The routine will write <code>nrow</code> records, starting from the location specified by <code>rows</code>. </p>
<p> The fourth <code>idx</code> argument is the index of the first raw input row to write, in the case where rows from the user buffer are being merged with their raw input row counterparts (see below). Note that this <code>idx</code> value is has nothing to do with the row buffer specified in argument 1. It merely matches the row being written with its corresponding (hidden) raw row. Thus, if you read a number of rows, process them, and then write them out all at once starting from the first user row, the value of <code>idx</code> should be 0: </p>
<pre><code>
Ev ebuf, ev;
/* get rows -- let routine allocate the row array */
while ((ebuf = (Ev)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got))) {
    /* process all rows */
    for (i = 0; i &lt; got; i++) {
        /* point to the i'th row */
        ev = ebuf + i;
        ...
    }
    /* write out this batch of rows, starting with the first */
    FunTableRowPut(fun2, (char *)ebuf, got, 0, NULL);
    /* free row data */
    if (ebuf)
        free(ebuf);
}
</code></pre>
<p> On the other hand, if you write out the rows one at a time (possibly skipping rows), then, when writing the i&#8217;th row from the input array of rows, set <code>idx</code> to the value of i: </p>
<p>Ev ebuf, ev;<br />
/* get rows &#8212; let routine allocate the row array */<br />
while ((ebuf = (Ev)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got))) {<br />
    /* process all rows */<br />
    for (i = 0; i &lt; got; i++) {<br />
        /* point to the i&#8217;th row */<br />
        ev = ebuf + i;<br />
        &#8230;<br />
            /* write out the current (i.e., i&#8217;th) row */<br />
            FunTableRowPut(fun2, (char *)ev, 1, i, NULL);<br />
    }<br />
    /* free row data */<br />
    if (ebuf)<br />
        free(ebuf);<br />
}</p>
<p> The final argument is a param list string that is not currently used. The routine returns the number of rows output. This should be equal to the value passed in the third nrow&lt;/B argument. </p>
<p> When <i>FunTableRowPut()</i> is first called for a given binary table, Funtools checks to see of the primary header has already been written (either by writing a previous row table or by writing an image.) If not, a dummy primary header is written to the file specifying that an extension should be expected. After this, a binary table header is automatically written containing information about the columns that will populate this table. In addition, if a Funtools reference handle was specified when this table was opened, the parameters from this Funtools reference handle are merged into the new binary table header. </p>
<p> In a typical Funtools row loop, you read rows using <i>FunTableRowGet()</i>() and write rows using <i>FunTableRowPut()</i>. The columns written by <i>FunTableRowPut()</i>() are those defined as writable by a previous call to <i>FunColumnSelect()</i>. If that call to FunColumnSelect also specified <code>merge=[update|replace|append]</code>, then the entire corresponding raw input row record will be merged with the output row according to the <code>merge</code> specification (see <i>FunColumnSelect()</i> above). </p>
<p> A call to write rows can either be done once, after all rows in the input batch have been processed, or it can be done (slightly less efficiently) one row at a time (or anything in between). We do recommend that you write all rows associated with a given batch of input rows before reading new rows. This is <code>required</code> if you are merging the output rows with the raw input rows (since the raw rows are destroyed with each successive call to get new rows). </p>
<p> For example: </p>
<p>Ev buf, ev;<br />
&#8230;<br />
    /* get rows &#8212; let routine allocate the row array */<br />
    while ((buf = (Ev)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got)))<br />
{<br />
    /* point to the i&#8217;th row */<br />
    ev = buf + i;<br />
    &#8230;.process<br />
}<br />
/* write out this batch of rows */<br />
FunTableRowPut(fun2, buf, got, 0, NULL);<br />
/* free row data */<br />
if (buf)<br />
    free(buf);<br />
}</p>
<p> or </p>
<pre><code>
Ev buf, ev;
...
    /* get rows -- let routine allocate the row array */
    while ((buf = (Ev)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got)))
{
    /* process all rows */
    for (i = 0; i &lt; got; i++) {
        /* point to the i'th row */
        ev = buf + i;
        ... process
            /* write out this batch of rows with the new column */
            if (dowrite)
                FunTableRowPut(fun2, buf, 1, i, NULL);
    }
    /* free row data */
    if (buf)
        free(buf);
}
</code></pre>
<p> Note that the difference between these calls is that the first one outputs <code>got</code> rows all at once and therefore passes <code>idx=0</code> in argument four, so that merging starts at the first raw input row. In the second case, a check it made on each row to see if it needs to be output. If so, the value of <code>idx</code> is passed as the value of the <code>i</code> variable which points to the current row being processed in the batch of input rows. </p>
<p> As shown above, successive calls to <i>FunTableRowPut()</i> will write rows sequentially. When you are finished writing all rows in a table, you should call <i>FunFlush()</i> to write out the <font SIZE="-1">FITS</font> binary table padding. However, this is not necessary if you subsequently call <i>FunClose()</i> without doing any other I/O to the <font SIZE="-1">FITS</font> file. </p>
<p> Note that <i>FunTableRowPut()</i> also can be called as <i>FunEventsPut()</i>, for backward compatibility.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
