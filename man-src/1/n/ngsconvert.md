---
title: "ngsconvert(1)"
name: "ngsconvert"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ngsconvert/"
description: "sconvert – convert spice formats"
---

<h2 class="name">NAME</h2>
<p> sconvert &#8211; convert spice formats </p>
<h2>SYNOPSIS</h2>
<p> <code>sconvert fromtype fromfile totype tofile</code><br />
 <code>sconvert fromtype totype</code><br />
 <code>sconvert</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Sconvert</code> translates spice output files among three formats: the old binary format, a new binary format, and a new ascii format. The formats are specified by the <code>fromtype</code> and <code>totype</code> arguments: `o&#8217; for the old format, `b&#8217; for the new binary format, and `a&#8217; for the new ascii format. <code>Fromtype</code> specifies the format to be read, and <code>totype</code> specifies the format to be written. If <code>fromfile</code> and <code>tofile</code> are given, then they are used as the input and output, otherwise standard input and output are used. (Note that this second option is only available on <font SIZE="-2">UNIX</font> systems &#8211; on VMS and other systems you must supply the filenames.) If no arguments are given, the parameters are prompted for. </p>
<p> Binary format is the preferred format for general use, as it is the most economical in terms of space and speed of access, and ascii is provided to make it easy to modify data files and transfer them between machines with different floating-point formats. The old format is provided only for backward compatibility. The three formats are as follows: </p>
<pre><code>
Old : What Size in Bytes
          title 80 date 8 time 8 numoutputs 2 the integer 4 2 variable names-- char[numoutputs][8] numoutputs *
      8 types of output numoutputs * 2 node index numoutputs * 2 plot title numoutputs * 24 the actual data numpoints *numoutputs * 8 Ascii : Title : Title Card String Date : Date [Plotname:Plot Name
                                                                                                                                                                                        Flags:complex or real No.
                                                                                                                                                                                    Variables:numoutputs No.
                                                                                                                                                                                       Points:numpoints
                                                                                                                                                                                      Command:nutmeg command
                                                                                                                                                                                    Variables:0 varname1 typename1 1 varname2 typename2 etc...
                                                                                                                                                                                       Values:0 n n n n... 1 n n n n... And so forth...] repeated one or
    more times
        If one of the flags is complex,
    the points look like r, i where r and i are floating point(in % e format).Otherwise they are in % e format.Only one of real and complex should appear.The lines are guaranteed to be less than 80 columns wide(unless the plot title or variable names are very long), so this format is safe to mail between systems like CMS.Any number of Command : lines may appear between the No.Points : and the Variables : lines, and whenever the plot is loaded into nutmeg they will be executed.Binary : Title Card(a NULL terminated string) Date, Time(a NULL terminated string)[Plot title(a NULL terminated string) Number of variables(an int) Number of data points(an int) flags(a short) variable header struct(repeated numoutputs times) variable name(a NULL terminated string) variable type(an int) set of outputs(repeated numpoints times)] repeated one or more times.A set of outputs is a vector of doubles of length numoutputs, or
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         a vector of real - imaginary pairs of doubles if the data is complex.
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nutmeg/">nutmeg</a>(1), <a href="/docs/linux/man/1-spice/">spice</a>(1), <a href="/docs/linux/man/3-writedata/">writedata</a>(3)</p>
<h2>AUTHOR</h2>
<p> Wayne Christopher (faustus [at] cad.berkeley.edu)</p>
<h2>BUGS</h2>
<p> If variable names and the title and plotname strings have trailing blanks in them they will be stripped off when the file is read, if it is in ascii format. </p>
<p> If a plot title begins with &quot;Title:&quot; <code>nutmeg</code> will be fooled into thinking that this is an ascii format file. <code>Sconvert</code> always requires the type to be specified, however. </p>
<h2>Index</h2>
