---
title: "funcolumnselect(3)"
name: "funcolumnselect"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funcolumnselect/"
description: "FunColumnSelect – select Funtools columns"
---

<h2>NAME</h2>
<p> <code>FunColumnSelect &#8211; select Funtools columns</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<p>int FunColumnSelect(Fun fun, int size, char *plist,<br />
                    char *name1, char *type1, char *mode1, int offset1,<br />
                    char *name2, char *type2, char *mode2, int offset2,<br />
                    &#8230;,<br />
                    NULL)</p>
<p>int FunColumnSelectArr(Fun fun, int size, char *plist,<br />
                       char **names, char **types, char **modes,<br />
                       int *offsets, int nargs);</p>
<h2>DESCRIPTION</h2>
<p> The FunColumnSelect() routine is used to select the columns from a Funtools binary table extension or raw event file for processing. This routine allows you to specify how columns in a file are to be read into a user record structure or written from a user record structure to an output <font SIZE="-1">FITS</font> file. </p>
<p> The first argument is the Fun handle associated with this set of columns. The second argument specifies the size of the user record structure into which columns will be read. Typically, the <i>sizeof()</i> macro is used to specify the size of a record structure. The third argument allows you to specify keyword directives for the selection and is described in more detail below. </p>
<p> Following the first three required arguments is a variable length list of column specifications. Each column specification will consist of four arguments:</p>
<dl>
<dt>*</p>
<dd> <code>name</code>: the name of the column</p>
<dt>*</p>
<dd> <code>type</code>: the data type of the column as it will be stored in the user record struct (not the data type of the input file). The following basic data types are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> A: <font SIZE="-1">ASCII</font> characters</p>
<dt>*</p>
<dd> B: unsigned 8-bit char</p>
<dt>*</p>
<dd> I: signed 16-bit int</p>
<dt>*</p>
<dd> U: unsigned 16-bit int (not standard <font SIZE="-1">FITS</font>)</p>
<dt>*</p>
<dd> J: signed 32-bit int</p>
<dt>*</p>
<dd> V: unsigned 32-bit int (not standard <font SIZE="-1">FITS</font>)</p>
<dt>*</p>
<dd> E: 32-bit float</p>
<dt>*</p>
<dd> D: 64-bit float</dl>
</dl>
<dl>
<dt>
<dd>
<p> The syntax used is similar to that which defines the <font SIZE="-1">TFORM</font> parameter in <font SIZE="-1">FITS</font> binary tables. That is, a numeric repeat value can precede the type character, so that &#8220;10I&#8221; means a vector of 10 short ints, &#8220;E&#8221; means a single precision float, etc. Note that the column value from the input file will be converted to the specified data type as the data is read by <i>FunTableRowGet()</i>. </p>
<p> [ A short digression regarding bit-fields: Special attention is required when reading or writing the <font SIZE="-1">FITS</font> bit-field type (&#8220;X&#8221;). Bit-fields almost always have a numeric repeat character preceding the &#8216;X&#8217; specification. Usually this value is a multiple of 8 so that bit-fields fit into an integral number of bytes. For all cases, the byte size of the bit-field B is (N+7)/8, where N is the numeric repeat character. </p>
<p> A bit-field is most easily declared in the user struct as an array of type char of size B as defined above. In this case, bytes are simply moved from the file to the user space. If, instead, a short or int scalar or array is used, then the algorithm for reading the bit-field into the user space depends on the size of the data type used along with the value of the repeat character. That is, if the user data size is equal to the byte size of the bit-field, then the data is simply moved (possibly with endian-based byte-swapping) from one to the other. If, on the other hand, the data storage is larger than the bit-field size, then a data type cast conversion is performed to move parts of the bit-field into elements of the array. Examples will help make this clear:</p>
<dl>
<dt>*</p>
<dd> If the file contains a 16X bit-field and user space specifies a 2B char array[2], then the bit-field is moved directly into the char array.</p>
<dt>*</p>
<dd> If the file contains a 16X bit-field and user space specifies a 1I scalar short int, then the bit-field is moved directly into the short int.</p>
<dt>*</p>
<dd> If the file contains a 16X bit-field and user space specifies a 1J scalar int, then the bit-field is type-cast to unsigned int before being moved (use of unsigned avoids possible sign extension).</p>
<dt>*</p>
<dd> If the file contains a 16X bit-field and user space specifies a 2J int array[2], then the bit-field is handled as 2 chars, each of which are type-cast to unsigned int before being moved (use of unsigned avoids possible sign extension).</p>
<dt>*</p>
<dd> If the file contains a 16X bit-field and user space specifies a 1B char, then the bit-field is treated as a char, i.e., truncation will occur.</p>
<dt>*</p>
<dd> If the file contains a 16X bit-field and user space specifies a 4J int array[4], then the results are undetermined.</dl>
</dl>
<dl>
<dt>
<dd>
<p> For all user data types larger than char, the bit-field is byte-swapped as necessary to convert to native format, so that bits in the resulting data in user space can be tested, masked, etc. in the same way regardless of platform.] </p>
<p> In addition to setting data type and size, the <code>type</code> specification allows a few ancillary parameters to be set, using the full syntax for <code>type</code>: </p>
<p>[@][n]&lt;type&gt;[[[&#8216;B&#8217;] poff]][:[tlmin[:tlmax[:binsiz]]]]</p>
<p> The special character &#8220;@&#8221; can be prepended to this specification to indicated that the data element is a pointer in the user record, rather than an array stored within the record. </p>
<p> The [n] value is an integer that specifies the number of elements that are in this column (default is 1). <font SIZE="-1">TLMIN</font>, <font SIZE="-1">TLMAX</font>, and <font SIZE="-1">BINSIZ</font> values also can be specified for this column after the type, separated by colons. If only one such number is specified, it is assumed to be <font SIZE="-1">TLMAX</font>, and <font SIZE="-1">TLMIN</font> and <font SIZE="-1">BINSIZ</font> are set to 1. </p>
<p> The [poff] value can be used to specify the offset into an array. By default, this offset value is set to zero and the data specified starts at the beginning of the array. The offset usually is specified in terms of the data type of the column. Thus an offset specification of [5] means a 20-byte offset if the data type is a 32-bit integer, and a 40-byte offset for a double. If you want to specify a byte offset instead of an offset tied to the column data type, precede the offset value with &#8216;B&#8217;, e.g. [B6] means a 6-bye offset, regardless of the column data type. </p>
<p> The [poff] is especially useful in conjunction with the pointer @ specification, since it allows the data element to anywhere stored anywhere in the allocated array. For example, a specification such as &#8220;@I[2]&#8221; specifies the third (i.e., starting from 0) element in the array pointed to by the pointer value. A value of &#8220;@2I[4]&#8221; specifies the fifth and sixth values in the array. For example, consider the following specification: </p>
<p>typedef struct EvStruct {<br />
    short x[4], *atp;<br />
} * Event, EventRec;<br />
/* set up the (hardwired) columns */<br />
FunColumnSelect(fun, sizeof(EventRec), NULL,<br />
                &#8220;2i&#8221;, &#8220;2I  &#8220;, &#8220;w&#8221;, FUN_OFFSET(Event, x),<br />
                &#8220;2i2&#8221;, &#8220;2I[2]&#8221;, &#8220;w&#8221;, FUN_OFFSET(Event, x),<br />
                &#8220;at2p&#8221;, &#8220;@2I&#8221;, &#8220;w&#8221;, FUN_OFFSET(Event, atp),<br />
                &#8220;at2p4&#8221;, &#8220;@2I[4]&#8221;, &#8220;w&#8221;, FUN_OFFSET(Event, atp),<br />
                &#8220;atp9&#8221;, &#8220;@I[9]&#8221;, &#8220;w&#8221;, FUN_OFFSET(Event, atp),<br />
                &#8220;atb20&#8221;, &#8220;@I[B20]&#8221;, &#8220;w&#8221;, FUN_OFFSET(Event, atb),<br />
                NULL);</p>
<p> Here we have specified the following columns:</p>
<dl>
<dt>*</p>
<dd> 2i: two short ints in an array which is stored as part the record</p>
<dt>*</p>
<dd> 2i2: the 3rd and 4th elements of an array which is stored as part of the record</p>
<dt>*</p>
<dd> an array of at least 10 elements, not stored in the record but allocated elsewhere, and used by three different columns:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> at2p: 2 short ints which are the first 2 elements of the allocated array</p>
<dt>*</p>
<dd> at2p4: 2 short ints which are the 5th and 6th elements of the allocated array</p>
<dt>*</p>
<dd> atp9: a short int which is the 10th element of the allocated array</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>*</p>
<dd> atb20: a short int which is at byte offset 20 of another allocated array</dl>
</dl>
<dl>
<dt>
<dd>
<p> In this way, several columns can be specified, all of which are in a single array. <font SIZE="-1"><code>NB</code></font>: it is the programmer&#8217;s responsibility to ensure that specification of a positive value for poff does not point past the end of valid data.</dl>
<dt>*</p>
<dd> <code>read/write mode</code>: &#8220;r&#8221; means that the column is read from an input file into user space by <i>FunTableRowGet()</i>, &#8220;w&#8221; means that the column is written to an output file. Both can specified at the same time.</p>
<dt>*</p>
<dd> <code>offset</code>: the offset into the user data to store this column. Typically, the macro <font SIZE="-1">FUN_OFFSET</font>(recname, colname) is used to define the offset into a record structure.</dl>
<p> When all column arguments have been specified, a final <font SIZE="-1">NULL</font> argument must added to signal the column selection list. </p>
<p> As an alternative to the varargs <i>FunColumnSelect()</i> routine, a non-varargs routine called <i>FunColumnSelectArr()</i> also is available. The first three arguments (fun, size, plist) of this routine are the same as in <i>FunColumnSelect()</i>. Instead of a variable argument list, however, <i>FunColumnSelectArr()</i> takes 5 additional arguments. The first 4 arrays arguments contain the names, types, modes, and offsets, respectively, of the columns being selected. The final argument is the number of columns that are contained in these arrays. It is the user&#8217;s responsibility to free string space allocated in these arrays. </p>
<p> Consider the following example: </p>
<p>typedef struct evstruct {<br />
    int status;<br />
    float pi, pha, *phas;<br />
    double energy;<br />
} * Ev, EvRec;</p>
<p>FunColumnSelect(fun, sizeof(EvRec), NULL,<br />
                &#8220;status&#8221;, &#8220;J&#8221;, &#8220;r&#8221;, FUN_OFFSET(Ev, status),<br />
                &#8220;pi&#8221;, &#8220;E&#8221;, &#8220;r&#8221;, FUN_OFFSET(Ev, pi),<br />
                &#8220;pha&#8221;, &#8220;E&#8221;, &#8220;r&#8221;, FUN_OFFSET(Ev, pha),<br />
                &#8220;phas&#8221;, &#8220;@9E&#8221;, &#8220;r&#8221;, FUN_OFFSET(Ev, phas),<br />
                NULL);</p>
<p> Each time a row is read into the Ev struct, the &#8220;status&#8221; column is converted to an int data type (regardless of its data type in the file) and stored in the status value of the struct. Similarly, &#8220;pi&#8221; and &#8220;pha&#8221;, and the phas vector are all stored as floats. Note that the &#8220;@&#8221; sign indicates that the &#8220;phas&#8221; vector is a pointer to a 9 element array, rather than an array allocated in the struct itself. The row record can then be processed as required: </p>
<p>/* get rows &#8212; let routine allocate the row array */<br />
while ((ebuf = (Ev)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got))) {<br />
    /* process all rows */<br />
    for (i = 0; i &lt; got; i++) {<br />
        /* point to the i&#8217;th row */<br />
        ev = ebuf + i;<br />
        ev-&gt;pi = (ev-&gt;pi + .5);<br />
        ev-&gt;pha = (ev-&gt;pi &#8211; .5);<br />
    }</p>
<p> <i>FunColumnSelect()</i> can also be called to define &#8220;writable&#8221; columns in order to generate a <font SIZE="-1">FITS</font> Binary Table, without reference to any input columns. For example, the following will generate a 4-column <font SIZE="-1">FITS</font> binary table when <i>FunTableRowPut()</i> is used to write Ev records: </p>
<p>typedef struct evstruct {<br />
    int status;<br />
    float pi, pha double energy;<br />
} * Ev, EvRec;</p>
<p>FunColumnSelect(fun, sizeof(EvRec), NULL,<br />
                &#8220;status&#8221;, &#8220;J&#8221;, &#8220;w&#8221;, FUN_OFFSET(Ev, status),<br />
                &#8220;pi&#8221;, &#8220;E&#8221;, &#8220;w&#8221;, FUN_OFFSET(Ev, pi),<br />
                &#8220;pha&#8221;, &#8220;E&#8221;, &#8220;w&#8221;, FUN_OFFSET(Ev, pha),<br />
                &#8220;energy&#8221;, &#8220;D&#8221;, &#8220;w&#8221;, FUN_OFFSET(Ev, energy),<br />
                NULL);</p>
<p> All columns are declared to be write-only, so presumably the column data is being generated or read from some other source. </p>
<p> In addition, <i>FunColumnSelect()</i> can be called to define <code>both</code> &#8220;readable&#8221; and &#8220;writable&#8221; columns. In this case, the &#8220;read&#8221; columns are associated with an input file, while the &#8220;write&#8221; columns are associated with the output file. Of course, columns can be specified as both &#8220;readable&#8221; and &#8220;writable&#8221;, in which case they are read from input and (possibly modified data values are) written to the output. The <i>FunColumnSelect()</i> call itself is made by passing the input Funtools handle, and it is assumed that the output file has been opened using this input handle as its Funtools reference handle. </p>
<p> Consider the following example: </p>
<p>typedef struct evstruct {<br />
    int status;<br />
    float pi, pha, *phas;<br />
    double energy;<br />
} * Ev, EvRec;</p>
<p>FunColumnSelect(fun, sizeof(EvRec), NULL,<br />
                &#8220;status&#8221;, &#8220;J&#8221;, &#8220;r&#8221;, FUN_OFFSET(Ev, status),<br />
                &#8220;pi&#8221;, &#8220;E&#8221;, &#8220;rw&#8221;, FUN_OFFSET(Ev, pi),<br />
                &#8220;pha&#8221;, &#8220;E&#8221;, &#8220;rw&#8221;, FUN_OFFSET(Ev, pha),<br />
                &#8220;phas&#8221;, &#8220;@9E&#8221;, &#8220;rw&#8221;, FUN_OFFSET(Ev, phas),<br />
                &#8220;energy&#8221;, &#8220;D&#8221;, &#8220;w&#8221;, FUN_OFFSET(Ev, energy),<br />
                NULL);</p>
<p> As in the &#8220;read&#8221; example above, each time an row is read into the Ev struct, the &#8220;status&#8221; column is converted to an int data type (regardless of its data type in the file) and stored in the status value of the struct. Similarly, &#8220;pi&#8221; and &#8220;pha&#8221;, and the phas vector are all stored as floats. Since the &#8220;pi&#8221;, &#8220;pha&#8221;, and &#8220;phas&#8221; variables are declared as &#8220;writable&#8221; as well as &#8220;readable&#8221;, they also will be written to the output file. Note, however, that the &#8220;status&#8221; variable is declared as &#8220;readable&#8221; only, and hence it will not be written to an output file. Finally, the &#8220;energy&#8221; column is declared as &#8220;writable&#8221; only, meaning it will not be read from the input file. In this case, it can be assumed that &#8220;energy&#8221; will be calculated in the program before being output along with the other values. </p>
<p> In these simple cases, only the columns specified as &#8220;writable&#8221; will be output using <i>FunTableRowPut()</i>. However, it often is the case that you want to merge the user columns back in with the input columns, even in cases where not all of the input column names are explicitly read or even known. For this important case, the <code>merge=[type]</code> keyword is provided in the plist string. </p>
<p> The <code>merge=[type]</code> keyword tells Funtools to merge the columns from the input file with user columns on output. It is normally used when an input and output file are opened and the input file provides the Funtools reference handle for the output file. In this case, each time <i>FunTableRowGet()</i> is called, the raw input rows are saved in a special buffer. If <i>FunTableRowPut()</i> then is called (before another call to <i>FunTableRowGet()</i>), the contents of the raw input rows are merged with the user rows according to the value of <code>type</code> as follows:</p>
<dl>
<dt>*</p>
<dd> <code>update</code>: add new user columns, and update value of existing ones (maintaining the input data type)</p>
<dt>*</p>
<dd> <code>replace</code>: add new user columns, and replace the data type and value of existing ones. (Note that if tlmin/tlmax values are not specified in the replacing column, but are specified in the original column being replaced, then the original tlmin/tlmax values are used in the replacing column.)</p>
<dt>*</p>
<dd> <code>append</code>: only add new columns, do not &#8220;replace&#8221; or &#8220;update&#8221; existing ones</dl>
<p> Consider the example above. If <code>merge=update</code> is specified in the plist string, then &#8220;energy&#8221; will be added to the input columns, and the values of &#8220;pi&#8221;, &#8220;pha&#8221;, and &#8220;phas&#8221; will be taken from the user space (i.e., the values will be updated from the original values, if they were changed by the program). The data type for &#8220;pi&#8221;, &#8220;pha&#8221;, and &#8220;phas&#8221; will be the same as in the original file. If <code>merge=replace</code> is specified, both the data type and value of these three input columns will be changed to the data type and value in the user structure. If <code>merge=append</code> is specified, none of these three columns will be updated, and only the &#8220;energy&#8221; column will be added. Note that in all cases, &#8220;status&#8221; will be written from the input data, not from the user record, since it was specified as read-only. </p>
<p> Standard applications will call <i>FunColumnSelect()</i> to define user columns. However, if this routine is not called, the default behavior is to transfer all input columns into user space. For this purpose a default record structure is defined such that each data element is properly aligned on a valid data type boundary. This mechanism is used by programs such as fundisp and funtable to process columns without needing to know the specific names of those columns. It is not anticipated that users will need such capabilities (contact us if you do!) </p>
<p> By default, <i>FunColumnSelect()</i> reads/writes rows to/from an &#8220;array of structs&#8221;, where each struct contains the column values for a single row of the table. This means that the returned values for a given column are not contiguous. You can set up the <font SIZE="-1">IO</font> to return a &#8220;struct of arrays&#8221; so that each of the returned columns are contiguous by specifying <code>org=structofarrays</code> (abbreviation: <code>org=soa</code>) in the plist. (The default case is <code>org=arrayofstructs</code> or <code>org=aos</code>.) </p>
<p> For example, the default setup to retrieve rows from a table would be to define a record structure for a single event and then call<br />
&nbsp;<wbr><i>FunColumnSelect()</i> as follows: </p>
<p>typedef struct evstruct {<br />
    short region;<br />
    double x, y;<br />
    int pi, pha;<br />
    double time;<br />
} * Ev, EvRec;</p>
<p>got = FunColumnSelect(fun, sizeof(EvRec), NULL,<br />
                      &#8220;x&#8221;, &#8220;D:10:10&#8221;, mode, FUN_OFFSET(Ev, x),<br />
                      &#8220;y&#8221;, &#8220;D:10:10&#8221;, mode, FUN_OFFSET(Ev, y),<br />
                      &#8220;pi&#8221;, &#8220;J&#8221;, mode, FUN_OFFSET(Ev, pi),<br />
                      &#8220;pha&#8221;, &#8220;J&#8221;, mode, FUN_OFFSET(Ev, pha),<br />
                      &#8220;time&#8221;, &#8220;1D&#8221;, mode, FUN_OFFSET(Ev, time),<br />
                      NULL);</p>
<p> Subsequently, each call to <i>FunTableRowGet()</i> will return an array of structs, one for each returned row. If instead you wanted to read columns into contiguous arrays, you specify <code>org=soa</code>: </p>
<p>typedef struct aevstruct {<br />
    short region[MAXROW];<br />
    double x[MAXROW], y[MAXROW];<br />
    int pi[MAXROW], pha[MAXROW];<br />
    double time[MAXROW];<br />
} * AEv, AEvRec;</p>
<pre>
  got = FunColumnSelect(fun, sizeof(AEvRec), &quot;org=soa&quot;,
                      &quot;x&quot;,       &quot;D:10:10&quot;, mode, FUN_OFFSET(AEv, x),
                      &quot;y&quot;,       &quot;D:10:10&quot;, mode, FUN_OFFSET(AEv, y),
                      &quot;pi&quot;,      &quot;J&quot;,       mode, FUN_OFFSET(AEv, pi),
                      &quot;pha&quot;,     &quot;J&quot;,       mode, FUN_OFFSET(AEv, pha),
                      &quot;time&quot;,    &quot;1D&quot;,      mode, FUN_OFFSET(AEv, time),
                      NULL);
</pre>
<p> Note that the only modification to the call is in the plist string. </p>
<p> Of course, instead of using staticly allocated arrays, you also can specify dynamically allocated pointers: </p>
<p>/* pointers to arrays of columns (used in struct of arrays) */<br />
typedef struct pevstruct {<br />
    short *region;<br />
    double *x, *y;<br />
    int *pi, *pha;<br />
    double *time;<br />
} * PEv, PEvRec;</p>
<pre>
  got = FunColumnSelect(fun, sizeof(PEvRec), &quot;org=structofarrays&quot;,
                      &quot;$region&quot;, &quot;@I&quot;,       mode, FUN_OFFSET(PEv, region),
                      &quot;x&quot;,       &quot;@D:10:10&quot;, mode, FUN_OFFSET(PEv, x),
                      &quot;y&quot;,       &quot;@D:10:10&quot;, mode, FUN_OFFSET(PEv, y),
                      &quot;pi&quot;,      &quot;@J&quot;,       mode, FUN_OFFSET(PEv, pi),
                      &quot;pha&quot;,     &quot;@J&quot;,       mode, FUN_OFFSET(PEv, pha),
                      &quot;time&quot;,    &quot;@1D&quot;,      mode, FUN_OFFSET(PEv, time),
                      NULL);
</pre>
<p> Here, the actual storage space is either allocated by the user or by the <i>FunColumnSelect()</i> call). </p>
<p> In all of the above cases, the same call is made to retrieve rows, e.g.: </p>
<p>buf = (void *)FunTableRowGet(fun, NULL, MAXROW, NULL, &amp;got);</p>
<p> However, the individual data elements are accessed differently. For the default case of an &#8220;array of structs&#8221;, the individual row records are accessed using: </p>
<p>for (i = 0; i &lt; got; i++) {<br />
    ev = (Ev)buf + i;<br />
    fprintf(stdout, &#8220;%.2f	%.2f	%d	%d	%.4f	%.4f	%21.8f
&#8221;,<br />
            ev-&gt;x, ev-&gt;y, ev-&gt;pi, ev-&gt;pha, ev-&gt;dx, ev-&gt;dy, ev-&gt;time);<br />
}</p>
<p> For a struct of arrays or a struct of array pointers, we have a single struct through which we access individual columns and rows using: </p>
<pre><code>
aev = (AEv)buf;
for (i = 0; i &lt; got; i++) {
    fprintf(stdout, "%.2f	%.2f	%d	%d	%.4f	%.4f	%21.8f
",
            aev-&gt;x[i], aev-&gt;y[i], aev-&gt;pi[i], aev-&gt;pha[i],
            aev-&gt;dx[i], aev-&gt;dy[i], aev-&gt;time[i]);
}
</code></pre>
<p> Support for struct of arrays in the <i>FunTableRowPut()</i> call is handled analogously. </p>
<p> See the evread example code and evmerge example code for working examples of how <i>FunColumnSelect()</i> is used.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
