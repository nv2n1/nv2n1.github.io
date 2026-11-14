---
title: "strfile(1)"
name: "strfile"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strfile/"
description: "strfile – create a random access file for storing strings unstr – dump strings in pointer order"
---

<h2>NAME</h2>
<p> strfile &#8211; create a random access file for storing strings<br />
 unstr &#8211; dump strings in pointer order</p>
<h2>SYNOPSIS</h2>
<p> <code>strfile</code> [<code>-iorsx</code>] [<code>-c</code> <i>char</i>] <i>sourcefile</i> [<i>outputfile</i>]<br />
 <code>unstr</code> [<code>-c</code> <i>char</i>] <i>datafile</i>[<i>.ext</i>] [<i>outputfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>strfile</code> reads a file containing groups of lines separated by a line containing a single percent `%&#8217; sign (or other specified delimiter character) and creates a data file which contains a header structure and a table of file offsets for each group of lines. This allows random access of the strings. </p>
<p> The output file, if not specified on the command line, is named <i>sourcefile.dat</i>. </p>
<p> The purpose of <code>unstr </code> is to undo the work of <code>strfile</code>. It prints out the strings contained in the sourcefile, which is <i>datafile.ext</i> without its extension, or <i>datafile</i> if no extension is specified (in this case, the extension <i>.dat</i> is added to the name of the datafile) in the order that they are listed in the header file <i>datafile</i>. If no <i>outputfile </i> is specified, it prints to standard output; otherwise it prints to the file specified. <code>unstr</code> can also universally change the delimiter character in a strings file. It is possible to create sorted versions of input files by using <code>strfile -o </code> and then using <code>unstr </code> to dump them out in the table order.</p>
<h3>Options</h3>
<p> The options are as follows:</p>
<dl>
<dt><code>-c </code><i>char</i></p>
<dd> Change the delimiting character from the percent sign to <i>char</i>. This option is available for both <code>strfile</code> and <code>unstr</code>.</p>
<dt><code>-i</code></p>
<dd> Ignore case when ordering the strings.</p>
<dt><code>-o</code></p>
<dd> Order the strings in alphabetical order. The offset table will be sorted in the alphabetical order of the groups of lines referenced. Any initial non-alphanumeric characters are ignored. This option causes the STR_ORDERED bit in the header <i>str_flags </i> field to be set. (It also now really does sort! It didn&#8217;t used to).</p>
<dt><code>-r</code></p>
<dd> Randomize access to the strings. Entries in the offset table will be randomly ordered. This option causes the STR_RANDOM bit in the header <i>str_flags </i> field to be set. (And really does randomize)</p>
<dt><code>-s</code></p>
<dd> Run silently; don&#8217;t give a summary message when finished.</p>
<dt><code>-x</code></p>
<dd> Note that each alphabetic character in the groups of lines is rotated 13 positions in a simple caesar cypher. This option causes the STR_ROTATED bit in the header <i>str_flags </i> field to be set. Note that it <code>does not</code> rotate the strings&#8211;that operation must be performed separately.</dl>
<h3>Header</h3>
<p> The format of the header is: </p>
<p> #define VERSION 1<br />
 unsigned long str_version; /* version number */<br />
 unsigned long str_numstr; /* # of strings in the file */<br />
 unsigned long str_longlen; /* length of longest string */<br />
 unsigned long str_shortlen; /* shortest string length */<br />
 #define STR_RANDOM 0x1 /* randomized pointers */<br />
 #define STR_ORDERED 0x2 /* ordered pointers */<br />
 #define STR_ROTATED 0x4 /* rot-13&#8217;d text */<br />
 unsigned long str_flags; /* bit field for flags */<br />
 char str_delim; /* delimiting character */ </p>
<p> All fields are written in network byte order.</p>
<h2>BUGS</h2>
<p> Fewer now, one hopes. However, fortunes (text strings) beginning with a blank line appear to be sorted between random letters. This includes ASCII art that contains no letters, and first lines that are solely non-alphanumeric, apparently. I&#8217;ve no idea why this should be.</p>
<h2>OTHER USES</h2>
<p> What can you do with this besides printing sarcastic and obscene messages to the screens of lusers at login or logout? </p>
<p> There <code>are</code> some other possibilities. Source code for a sample program, <code>randstr</code>, is included with this distribution: randstr splits the difference between <code>unstr</code> and <code>fortune</code>. It reads a single, specified file, and randomly selects a single text string.</p>
<dl>
<dt>1</p>
<dd> Include <i>strfile.h</i> into a news reading/posting program, to generate random signatures. <code><a href="/docs/linux/man/1-tin/">Tin</a></code>(1) does something similar, in a much more complex manner.</p>
<dt>2</p>
<dd> Include it in a game. While strfile doesn&#8217;t support &#8216;fields&#8217; or &#8216;records&#8217;, there&#8217;s no reason that the text strings can&#8217;t be consistent: first line, a die roll; second line, a score; third and subsequent lines, a text message.</p>
<dt>3</p>
<dd> Use it to store your address book. Hell, some of the guys I know would be as well off using it to decide who to call on Friday nights (and for some, it wouldn&#8217;t matter whether there were phone numbers in it or not).</p>
<dt>4</p>
<dd> Use it in &#8216;lottery&#8217; situations. If you&#8217;re an ISP, write a script to store login names and GECOS from <i>/etc/passwd</i> in strfile format, write another to send &#8216;congratulations, you&#8217;ve won&#8217; to the lucky login selected. The prize might be a month&#8217;s free service, or if you&#8217;re AOL, a month free on a real service provider.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-byteorder/">byteorder</a></code>(3), <code><a href="/docs/linux/man/6-fortune/">fortune</a></code>(6)</p>
<h2>HISTORY</h2>
<p> The <code>strfile</code> utility first appeared in 4.4BSD. This version was heavily modified, much of it in ways peculiar to Linux. Work has since been done to make the code more generic, and has so far been tested to work with SunOS 4.x. More platforms are expected to be supported as work continues. </p>
<h2>Index</h2>
