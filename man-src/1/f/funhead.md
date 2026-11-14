---
title: "funhead(1)"
name: "funhead"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funhead/"
description: "funhead – display a header in a Funtools file"
---

<h2>NAME</h2>
<p> <code>funhead &#8211; display a header in a Funtools file</code></p>
<h2>SYNOPSIS</h2>
<p> funhead [-a] [-s] [-t] [-L] &lt;iname&gt; [oname ename]</p>
<h2>OPTIONS</h2>
<pre>
  -a    # display all extension headers
  -s    # display 79 chars instead of 80 before the new-line
  -t    # prepend data type char to each line of output
  -L    # output in rdb/starbase list format
</pre>
<h2>DESCRIPTION</h2>
<p> <code>funhead</code> displays the <font SIZE="-1">FITS</font> header parameters in the specified <font SIZE="-1">FITS</font> Extension. </p>
<p> The first argument to the program specifies the Funtools input file to display. If &#8220;stdin&#8221; is specified, data are read from the standard input. Funtools Bracket Notation is used to specify particular <font SIZE="-1">FITS</font> extension to process. Normally, the full 80 characters of each header card is output, followed by a new-line. </p>
<p> If the <code>-a</code> switch is specified, the header from each <font SIZE="-1">FITS</font> extensions in the file is displayed. Note, however, that the <code>-a</code> switch does not work with <font SIZE="-1">FITS</font> files input via stdin. We hope to remove this restriction in a future release. </p>
<p> If the <code>-s</code> switch is specified, only 79 characters are output before the new-line. This helps the display on 80 character terminals. </p>
<p> If the <code>-t</code> switch is specified, the data type of the parameter is output as a one character prefix, followed by 77 characters of the param. The parameter data types are defined as: <font SIZE="-1">FUN_PAR_UNKNOWN</font> (&#8216;u&#8217;), <font SIZE="-1">FUN_PAR_COMMENT</font> (&#8216;c&#8217;), <font SIZE="-1">FUN_PAR_LOGICAL</font> (&#8216;l&#8217;), <font SIZE="-1">FUN_PAR_INTEGER</font> (&#8216;i&#8217;), <font SIZE="-1">FUN_PAR_STRING</font> (&#8216;s&#8217;), <font SIZE="-1">FUN_PAR_REAL</font> (&#8216;r&#8217;), <font SIZE="-1">FUN_PAR_COMPLEX</font> (&#8216;x&#8217;). </p>
<p> If the <code>-L</code> (rdb table) switch is used, the output will conform to starbase/rdb data base list format. </p>
<p> For example to display the <font SIZE="-1">EVENTS</font> extension (binary table): </p>
<pre><code>
  [sh] funhead "foo.fits[EVENTS]"
  XTENSION= 'BINTABLE'            /  FITS 3D BINARY TABLE                      
  BITPIX  =                    8  /  Binary data                               
  NAXIS   =                    2  /  Table is a matrix                         
  NAXIS1  =                   20  /  Width of table in bytes                   
  NAXIS2  =                30760  /  Number of entries in table                
  PCOUNT  =                    0  /  Random parameter count                    
  GCOUNT  =                    1  /  Group count                               
  TFIELDS =                    7  /  Number of fields in each row              
  EXTNAME = 'EVENTS  '            /  Table name                                
  EXTVER  =                    1  /  Version number of table                   
  TFORM1  = '1I      '            /  Data type for field                       
  TTYPE1  = 'X       '            /  Label for field                           
  TUNIT1  = '        '            /  Physical units for field                  
  TFORM2  = '1I      '            /  Data type for field                       
    etc. ...
  END
</code></pre>
<p> To display the third header: </p>
<pre><code>
  [sh] funhead "foo.fits[3]"
  XTENSION= 'BINTABLE'            /  FITS 3D BINARY TABLE                      
  BITPIX  =                    8  /  Binary data                               
  NAXIS   =                    2  /  Table is a matrix                         
  NAXIS1  =                   32  /  Width of table in bytes                   
  NAXIS2  =                   40  /  Number of entries in table                
  PCOUNT  =                    0  /  Random parameter count                    
  GCOUNT  =                    1  /  Group count                               
  TFIELDS =                    7  /  Number of fields in each row              
  EXTNAME = 'TGR     '            /  Table name                                
  EXTVER  =                    1  /  Version number of table                   
  TFORM1  = '1D      '            /  Data type for field                       
    etc. ...
  END
</code></pre>
<p> To display the primary header (i.e., extension 0): </p>
<pre>
  sh&gt; funhead &quot;coma.fits[0]&quot;
  SIMPLE  =                    T /STANDARD FITS FORMAT                         
  BITPIX  =                   16 /2-BYTE TWOS-COMPL INTEGER                    
  NAXIS   =                    2 /NUMBER OF AXES                               
  NAXIS1  =                  800 /                                             
  NAXIS2  =                  800 /                                             
  DATATYPE= 'INTEGER*2'          /SHORT INTEGER                                
  END
</pre>
<p> The funhead program also can edit (i.e. add, delete, or modify) or display individual headers parameters. Edit mode is signalled by the presence of two additional command-line arguments: output file and edit command file, in that order. Edit mode acts as a filter: the output file will contain the entire input <font SIZE="-1">FITS</font> file, including other extensions. The edit command file can be &#8220;stdin&#8221;, in which case edit command are read from the standard input. </p>
<p> The edit command file contains parameter comments (having &#8216;#&#8217; in the first column) and delete and assignment(modify or add) operations. A delete operation is specified by preceding the parameter name with a minus sign &#8220;-&#8221;. A display operation (very useful in interactive sessions, i.e., where the edit commands are taken from stdin) is specified by preceding the parameter name with a question mark &#8220;?&#8221;. In either case, a parameter value need not be specified. An assignment operation is specified in the same two ways that a parameter is specified in a text header (but without the comment character that precedes header params), i.e.:</p>
<dl>
<dt>*</p>
<dd> FITS-style comments have an equal sign &#8220;=&#8221; between the keyword and value and an optional slash &#8220;/&#8221; to signify a comment. The strict <font SIZE="-1">FITS</font> rules on column positions are not enforced.</p>
<dt>*</p>
<dd> Free-form comments can have an optional colon separator between the keyword and value. In the absence of quote, all tokens after the keyword are part of the value, i.e. no comment is allowed.</dl>
<p> For example, the following interactive session checks for the existence of parameters, adds new parameters, modifies them, and modifies and deletes existing parameters: </p>
<pre>
  sh$ ./funhead snr.ev foo.fits -
  # look for FOO1
  ? FOO1
  WARNING: FOO1 not found
  # add new foo1
  FOO1 = 100
  # add foo2
  FOO2 = 200
  # reset foo1 to a different value
  FOO1 -1
  # delete foo2
  -FOO2
  # change existing value
  EXTVER 2
  ? XS-SORT
  XS-SORT = 'EOF     '            /  type of event sort
  # delete existing value
  -XS-SORT
  # exit
  ^D
</pre>
<p> See Column-based Text Files for more information about header parameter format.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
