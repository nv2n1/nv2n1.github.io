---
title: "funtablerowget(3)"
name: "funtablerowget"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funtablerowget/"
description: "FunTableRowGet – get Funtools rows"
---

<h2>NAME</h2>
<p> <code>FunTableRowGet &#8211; get Funtools rows</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>void *FunTableRowGet(Fun fun, void *rows, int maxrow, char *plist,<br />
                     int *nrow)</p>
<h2>DESCRIPTION</h2>
<p> The FunTableRowGet() routine retrieves rows from a Funtools binary table or raw event file, and places the values of columns selected by <i>FunColumnSelect()</i> into an array of user structs. Selected column values are automatically converted to the specified user data type (and to native data format) as necessary. </p>
<p> The first argument is the Fun handle associated with this row data. The second <code>rows</code> argument is the array of user structs into which the selected columns will be stored. If <font SIZE="-1">NULL</font> is passed, the routine will automatically allocate space for this array. (This includes proper allocation of pointers within each struct, if the &#8220;@&#8221; pointer type is used in the selection of columns. Note that if you pass <font SIZE="-1">NULL</font> in the second argument, you should free this space using the standard <i>free()</i> system call when you are finished with the array of rows.) The third <code>maxrow</code> argument specifies the maximum number of rows to be returned. Thus, if <code>rows</code> is allocated by the user, it should be at least of size maxrow*sizeof(evstruct). </p>
<p> The fourth <code>plist</code> argument is a param list string. Currently, the keyword/value pair &#8220;mask=transparent&#8221; is supported in the plist argument. If this string is passed in the call&#8217;s plist argument, then all rows are passed back to the user (instead of just rows passing the filter). This is only useful when <i>FunColumnSelect()</i> also is used to specify &#8220;$region&#8221; as a column to return for each row. In such a case, rows found within a region have a returned region value greater than 0 (corresponding to the region id of the region in which they are located), rows passing the filter but not in a region have region value of -1, and rows not passing any filter have region value of 0. Thus, using &#8220;mask=transparent&#8221; and the returned region value, a program can process all rows and decide on an action based on whether a given row passed the filter or not. </p>
<p> The final argument is a pointer to an int variable that will return the actual number of rows returned. The routine returns a pointer to the array of stored rows, or <font SIZE="-1">NULL</font> if there was an error. (This pointer will be the same as the second argument, if the latter is non-NULL). </p>
<pre><code>
/* get rows -- let routine allocate the row array */
while ((buf = (Ev)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got))) {
    /* process all rows */
    for (i = 0; i &lt; got; i++) {
        /* point to the i'th row */
        ev = buf + i;
        /* rearrange some values. etc. */
        ev-&gt;energy = (ev-&gt;pi + ev-&gt;pha) / 2.0;
        ev-&gt;pha = -ev-&gt;pha;
        ev-&gt;pi = -ev-&gt;pi;
    }
    /* write out this batch of rows */
    FunTableRowPut(fun2, buf, got, 0, NULL);
    /* free row data */
    if (buf)
        free(buf);
}
</code></pre>
<p> As shown above, successive calls to <i>FunTableRowGet()</i> will return the next set of rows from the input file until all rows have been read, i.e., the routine behaves like sequential Unix I/O calls such as <i>fread()</i>. See evmerge example code for a more complete example. </p>
<p> Note that <i>FunTableRowGet()</i> also can be called as <i>FunEventsGet()</i>, for backward compatibility.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
