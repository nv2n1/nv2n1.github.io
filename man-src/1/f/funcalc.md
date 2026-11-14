---
title: "funcalc(1)"
name: "funcalc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funcalc/"
description: "funcalc – Funtools calculator (for binary tables)"
---

<h2>NAME</h2>
<p> <code>funcalc &#8211; Funtools calculator (for binary tables)</code></p>
<h2>SYNOPSIS</h2>
<p> funcalc [-n] [-a argstr] [-e expr] [-f file] [-l link] [-p prog] &lt;iname&gt; [oname [columns]]</p>
<h2>OPTIONS</h2>
<pre>
  -a argstr    # user arguments to pass to the compiled program
  -e expr      # funcalc expression
  -f file      # file containing funcalc expression
  -l libs      # libs to add to link command  
  -n           # output generated code instead of compiling and executing
  -p prog      # generate named program, no execution
  -u           # die if any variable is undeclared (don't auto-declare)
</pre>
<h2>DESCRIPTION</h2>
<p> <code>funcalc</code> is a calculator program that allows arbitrary expressions to be constructed, compiled, and executed on columns in a Funtools table (<font SIZE="-1">FITS</font> binary table or raw event file). It works by integrating user-supplied expression(s) into a template C program, then compiling and executing the program. <code>funcalc</code> expressions are C statements, although some important simplifications (such as automatic declaration of variables) are supported. </p>
<p> <code>funcalc</code> expressions can be specified in three ways: on the command line using the <code>-e [expression]</code> switch, in a file using the <code>-f [file]</code> switch, or from stdin (if neither <code>-e</code> nor <code>-f</code> is specified). Of course a file containing <code>funcalc</code> expressions can be read from stdin. </p>
<p> Each invocation of <code>funcalc</code> requires an input Funtools table file to be specified as the first command line argument. The output Funtools table file is the second optional argument. It is needed only if an output <font SIZE="-1">FITS</font> file is being created (i.e., in cases where the <code>funcalc</code> expression only prints values, no output file is needed). If input and output file are both specified, a third optional argument can specify the list of columns to activate (using <i>FunColumnActivate()</i>). Note that <code>funcalc</code> determines whether or not to generate code for writing an output file based on the presence or absence of an output file argument. </p>
<p> A <code>funcalc</code> expression executes on each row of a table and consists of one or more C statements that operate on the columns of that row (possibly using temporary variables). Within an expression, reference is made to a column of the <code>current</code> row using the C struct syntax <code>cur-</code>[colname]&gt;, e.g. cur-&gt;x, cur-&gt;pha, etc. Local scalar variables can be defined using C declarations at very the beginning of the expression, or else they can be defined automatically by <code>funcalc</code> (to be of type double). Thus, for example, a swap of columns x and y in a table can be performed using either of the following equivalent <code>funcalc</code> expressions: </p>
<pre><code>
double temp;
temp = cur-&gt;x;
cur-&gt;x = cur-&gt;y;
cur-&gt;y = temp;
</code></pre>
<p> or: </p>
<p>temp = cur-&gt;x;<br />
cur-&gt;x = cur-&gt;y;<br />
cur-&gt;y = temp;</p>
<p> When this expression is executed using a command such as: </p>
<pre>
  funcalc -f swap.expr itest.ev otest.ev
</pre>
<p> the resulting file will have values of the x and y columns swapped. </p>
<p> By default, the data type of the variable for a column is the same as the data type of the column as stored in the file. This can be changed by appending &#8220;:[dtype]&#8221; to the first reference to that column. In the example above, to force x and y to be output as doubles, specify the type &#8216;D&#8217; explicitly: </p>
<p>temp = cur-&gt;x : D;<br />
cur-&gt;x = cur-&gt;y : D;<br />
cur-&gt;y = temp;</p>
<p> Data type specifiers follow standard <font SIZE="-1">FITS</font> table syntax for defining columns using <font SIZE="-1">TFORM:</font></p>
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
<dd> D: 64-bit float</p>
<dt>*</p>
<dd> X: bits (treated as an array of chars)</dl>
<p> Note that only the first reference to a column should contain the explicit data type specifier. </p>
<p> Of course, it is important to handle the data type of the columns correctly. One of the most frequent cause of error in <code>funcalc</code> programming is the implicit use of the wrong data type for a column in expression. For example, the calculation: </p>
<pre>
  dx = (cur-&gt;x - cur-&gt;y)/(cur-&gt;x + cur-&gt;y);
</pre>
<p> usually needs to be performed using floating point arithmetic. In cases where the x and y columns are integers, this can be done by reading the columns as doubles using an explicit type specification: </p>
<pre>
  dx = (cur-&gt;x:D - cur-&gt;y:D)/(cur-&gt;x + cur-&gt;y);
</pre>
<p> Alternatively, it can be done using C type-casting in the expression: </p>
<p>dx = ((double)cur-&gt;x &#8211; (double)cur-&gt;y) / ((double)cur-&gt;x + (double)cur-&gt;y);</p>
<p> In addition to accessing columns in the current row, reference also can be made to the <code>previous</code> row using <code>prev-</code>[colname]&gt;, and to the <code>next</code> row using <code>next-</code>[colname]&gt;. Note that if <code>prev-</code>[colname]&gt; is specified in the <code>funcalc</code> expression, the very first row is not processed. If <code>next-</code>[colname]&gt; is specified in the <code>funcalc</code> expression, the very last row is not processed. In this way, <code>prev</code> and <code>next</code> are guaranteed always to point to valid rows. For example, to print out the values of the current x column and the previous y column, use the C fprintf function in a <code>funcalc</code> expression: </p>
<pre>
  fprintf(stdout, &quot;%d %d
&quot;, cur-&gt;x, prev-&gt;y);
</pre>
<p> New columns can be specified using the same <code>cur-</code>[colname]&gt; syntax by appending the column type (and optional tlmin/tlmax/binsiz specifiers), separated by colons. For example, cur-&gt;avg:D will define a new column of type double. Type specifiers are the same those used above to specify new data types for existing columns. </p>
<p> For example, to create and output a new column that is the average value of the x and y columns, a new &#8220;avg&#8221; column can be defined: </p>
<pre>
  cur-&gt;avg:D = (cur-&gt;x + cur-&gt;y)/2.0
</pre>
<p> Note that the final &#8216;;&#8217; is not required for single-line expressions. </p>
<p> As with <font SIZE="-1">FITS</font> <font SIZE="-1">TFORM</font> data type specification, the column data type specifier can be preceded by a numeric count to define an array, e.g., &#8220;10I&#8221; means a vector of 10 short ints, &#8220;2E&#8221; means two single precision floats, etc. A new column only needs to be defined once in a <code>funcalc</code> expression, after which it can be used without re-specifying the type. This includes reference to elements of a column array: </p>
<p>cur-&gt;avg[0] : 2D = (cur-&gt;x + cur-&gt;y) / 2.0;<br />
cur-&gt;avg[1] = (cur-&gt;x &#8211; cur-&gt;y) / 2.0;</p>
<p> The &#8216;X&#8217; (bits) data type is treated as a char array of dimension (numeric_count/8), i.e., 16X is processed as a 2-byte char array. Each 8-bit array element is accessed separately: </p>
<p>cur-&gt;stat[0] : 16X = 1;<br />
cur-&gt;stat[1] = 2;</p>
<p> Here, a 16-bit column is created with the <font SIZE="-1">MSB</font> is set to 1 and the <font SIZE="-1">LSB</font> set to 2. </p>
<p> By default, all processed rows are written to the specified output file. If you want to skip writing certain rows, simply execute the C &#8220;continue&#8221; statement at the end of the <code>funcalc</code> expression, since the writing of the row is performed immediately after the expression is executed. For example, to skip writing rows whose average is the same as the current x value: </p>
<p>cur-&gt;avg[0] : 2D = (cur-&gt;x + cur-&gt;y) / 2.0;<br />
cur-&gt;avg[1] = (cur-&gt;x &#8211; cur-&gt;y) / 2.0;<br />
if (cur-&gt;avg[0] == cur-&gt;x)<br />
    continue;</p>
<p> If no output file argument is specified on the <code>funcalc</code> command line, no output file is opened and no rows are written. This is useful in expressions that simply print output results instead of generating a new file: </p>
<p>fpv = (cur-&gt;av3<br />
       : D &#8211; cur-&gt;av1<br />
       : D) /<br />
      (cur-&gt;av1 + cur-&gt;av2<br />
       : D + cur-&gt;av3);<br />
fbv = cur-&gt;av2 / (cur-&gt;av1 + cur-&gt;av2 + cur-&gt;av3);<br />
fpu = ((double)cur-&gt;au3 &#8211; cur-&gt;au1) / ((double)cur-&gt;au1 + cur-&gt;au2 + cur-&gt;au3);<br />
fbu = cur-&gt;au2 / (double)(cur-&gt;au1 + cur-&gt;au2 + cur-&gt;au3);<br />
fprintf(stdout, &#8220;%f	%f	%f	%f
&#8221;, fpv, fbv, fpu, fbu);</p>
<p> In the above example, we use both explicit type specification (for &#8220;av&#8221; columns) and type casting (for &#8220;au&#8221; columns) to ensure that all operations are performed in double precision. </p>
<p> When an output file is specified, the selected input table is processed and output rows are copied to the output file. Note that the output file can be specified as &#8220;stdout&#8221; in order to write the output rows to the standard output. If the output file argument is passed, an optional third argument also can be passed to specify which columns to process. </p>
<p> In a <font SIZE="-1">FITS</font> binary table, it sometimes is desirable to copy all of the other <font SIZE="-1">FITS</font> extensions to the output file as well. This can be done by appending a &#8216;+&#8217; sign to the name of the extension in the input file name. See <code>funtable</code> for a related example. </p>
<p> <code>funcalc</code> works by integrating the user-specified expression into a template C program called tabcalc.c. The completed program then is compiled and executed. Variable declarations that begin the <code>funcalc</code> expression are placed in the local declaration section of the template main program. All other lines are placed in the template main program&#8217;s inner processing loop. Other details of program generation are handled automatically. For example, column specifiers are analyzed to build a C struct for processing rows, which is passed to <i>FunColumnSelect()</i> and used in <i>FunTableRowGet()</i>. If an unknown variable is used in the expression, resulting in a compilation error, the program build is retried after defining the unknown variable to be of type double. </p>
<p> Normally, <code>funcalc</code> expression code is added to <code>funcalc</code> row processing loop. It is possible to add code to other parts of the program by placing this code inside special directives of the form: </p>
<pre>
  [directive name]
    ... code goes here ...
  end
</pre>
<p> The directives are:</p>
<dl>
<dt>*</p>
<dd> <code>global</code> add code and declarations in global space, before the main routine.</p>
<dt>*</p>
<dd> <code>local</code> add declarations (and code) just after the local declarations in main</p>
<dt>*</p>
<dd> <code>before</code> add code just before entering the main row processing loop</p>
<dt>*</p>
<dd> <code>after</code> add code just after exiting the main row processing loop</dl>
<p> Thus, the following <code>funcalc</code> expression will declare global variables and make subroutine calls just before and just after the main processing loop: </p>
<p>global double v1, v2;<br />
double init(void);<br />
double finish(double v);<br />
end<br />
    before<br />
        v1 = init();<br />
end&#8230; process rows, with calculations using v1&#8230; after<br />
                         v2 = finish(v1);<br />
if (v2 &lt; 0.0) {<br />
    fprintf(stderr, &#8220;processing failed %g -&gt; %g
&#8221;, v1, v2);<br />
    exit(1);<br />
}<br />
end</p>
<p> Routines such as <i>init()</i> and <i>finish()</i> above are passed to the generated program for linking using the <code>-l [link directives &#8230;]</code> switch. The string specified by this switch will be added to the link line used to build the program (before the funtools library). For example, assuming that <i>init()</i> and <i>finish()</i> are in the library libmysubs.a in the /opt/special/lib directory, use: </p>
<pre>
  funcalc  -l &quot;-L/opt/special/lib -lmysubs&quot; ...
</pre>
<p> User arguments can be passed to a compiled funcalc program using a string argument to the &#8220;-a&#8221; switch. The string should contain all of the user arguments. For example, to pass the integers 1 and 2, use: </p>
<pre>
  funcalc -a &quot;1 2&quot; ...
</pre>
<p> The arguments are stored in an internal array and are accessed as strings via the <font SIZE="-1"><a href="/docs/linux/man/n-argv/">ARGV</a></font>(n) macro. For example, consider the following expression: </p>
<pre>
  local
    int pmin, pmax;
  end
</pre>
<p>before<br />
    pmin = atoi(ARGV(0));<br />
pmax = atoi(ARGV(1));<br />
end</p>
<p>if ((cur-&gt;pha &gt;= pmin) &amp;&amp; (cur-&gt;pha &lt;= pmax))<br />
    fprintf(stderr, &#8220;%d %d %d
&#8221;, cur-&gt;x, cur-&gt;y, cur-&gt;pha);</p>
<p> This expression will print out x, y, and pha values for all rows in which the pha value is between the two user-input values: </p>
<pre>
  funcalc -a '1 12' -f foo snr.ev'[cir 512 512 .1]'
  512 512 6
  512 512 8
  512 512 5
  512 512 5
  512 512 8
</pre>
<pre>
  funcalc -a '5 6' -f foo snr.ev'[cir 512 512 .1]'
  512 512 6
  512 512 5
  512 512 5
</pre>
<p> Note that it is the user&#8217;s responsibility to ensure that the correct number of arguments are passed. The <font SIZE="-1"><a href="/docs/linux/man/n-argv/">ARGV</a></font>(n) macro returns a <font SIZE="-1">NULL</font> if a requested argument is outside the limits of the actual number of args, usually resulting in a <font SIZE="-1">SEGV</font> if processed blindly. To check the argument count, use the <font SIZE="-1">ARGC</font> macro: </p>
<p>local long int seed = 1;<br />
double limit = 0.8;<br />
end</p>
<p>before if (ARGC &gt;= 1) seed = atol(ARGV(0));<br />
if (ARGC &gt;= 2)<br />
    limit = atof(ARGV(1));<br />
srand48(seed);<br />
end</p>
<p>if (drand48() &gt; limit)<br />
    continue;</p>
<p> The macro <font SIZE="-1">WRITE_ROW</font> expands to the <i>FunTableRowPut()</i> call that writes the current row. It can be used to write the row more than once. In addition, the macro <font SIZE="-1">NROW</font> expands to the row number currently being processed. Use of these two macros is shown in the following example: </p>
<p>if (cur-&gt;pha<br />
    : I == cur-&gt;pi<br />
    : I)<br />
    continue;<br />
a = cur-&gt;pha;<br />
cur-&gt;pha = cur-&gt;pi;<br />
cur-&gt;pi = a;<br />
cur-&gt;AVG : E = (cur-&gt;pha + cur-&gt;pi) / 2.0;<br />
cur-&gt;NR : I = NROW;<br />
if (NROW &lt; 10)<br />
    WRITE_ROW;</p>
<p> If the <code>-p [prog]</code> switch is specified, the expression is not executed. Rather, the generated executable is saved with the specified program name for later use. </p>
<p> If the <code>-n</code> switch is specified, the expression is not executed. Rather, the generated code is written to stdout. This is especially useful if you want to generate a skeleton file and add your own code, or if you need to check compilation errors. Note that the comment at the start of the output gives the compiler command needed to build the program on that platform. (The command can change from platform to platform because of the use of different libraries, compiler switches, etc.) </p>
<p> As mentioned previously, <code>funcalc</code> will declare a scalar variable automatically (as a double) if that variable has been used but not declared. This facility is implemented using a sed script named funcalc.sed, which processes the compiler output to sense an undeclared variable error. This script has been seeded with the appropriate error information for gcc, and for cc on Solaris, DecAlpha, and <font SIZE="-1">SGI</font> platforms. If you find that automatic declaration of scalars is not working on your platform, check this sed script; it might be necessary to add to or edit some of the error messages it senses. </p>
<p> In order to keep the lexical analysis of <code>funcalc</code> expressions (reasonably) simple, we chose to accept some limitations on how accurately C comments, spaces, and new-lines are placed in the generated program. In particular, comments associated with local variables declared at the beginning of an expression (i.e., not in a <code>local&#8230;end</code> block) will usually end up in the inner loop, not with the local declarations: </p>
<p>/* this comment will end up in the wrong place (i.e, inner loop) */<br />
double a; /* also in wrong place */<br />
/* this will be in the the right place (inner loop) */<br />
if (cur-&gt;x<br />
    : D == cur-&gt;y<br />
    : D)<br />
    continue; /* also in right place */<br />
a = cur-&gt;x;<br />
cur-&gt;x = cur-&gt;y;<br />
cur-&gt;y = a;<br />
cur-&gt;avg : E = (cur-&gt;x + cur-&gt;y) / 2.0;</p>
<p> Similarly, spaces and new-lines sometimes are omitted or added in a seemingly arbitrary manner. Of course, none of these stylistic blemishes affect the correctness of the generated code. </p>
<p> Because <code>funcalc</code> must analyze the user expression using the data file(s) passed on the command line, the input file(s) must be opened and read twice: once during program generation and once during execution. As a result, it is not possible to use stdin for the input file: <code>funcalc</code> cannot be used as a filter. We will consider removing this restriction at a later time. </p>
<p> Along with C comments, <code>funcalc</code> expressions can have one-line internal comments that are not passed on to the generated C program. These internal comment start with the <code>#</code> character and continue up to the new-line: </p>
<pre><code>
double a;
#this is not passed to the generated C file
#nor is this
    a = cur-&gt;x;
cur-&gt;x = cur-&gt;y;
cur-&gt;y = a;
/* this comment is passed to the C file */
cur-&gt;avg : E = (cur-&gt;x + cur-&gt;y) / 2.0;
</code></pre>
<p> As previously mentioned, input columns normally are identified by their being used within the inner event loop. There are rare cases where you might want to read a column and process it outside the main loop. For example, qsort might use a column in its sort comparison routine that is not processed inside the inner loop (and therefore not implicitly specified as a column to be read). To ensure that such a column is read by the event loop, use the <code>explicit</code> keyword. The arguments to this keyword specify columns that should be read into the input record structure even though they are not mentioned in the inner loop. For example: </p>
<pre>
  explicit pi pha
</pre>
<p> will ensure that the pi and pha columns are read for each row, even if they are not processed in the inner event loop. The <code>explicit</code> statement can be placed anywhere. </p>
<p> Finally, note that <code>funcalc</code> currently works on expressions involving <font SIZE="-1">FITS</font> binary tables and raw event files. We will consider adding support for image expressions at a later point, if there is demand for such support from the community.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
