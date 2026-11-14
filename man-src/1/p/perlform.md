---
title: "perlform(1)"
name: "perlform"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlform/"
description: "perlform – Perl formats"
---

<h2 class="name">NAME</h2>
<p> perlform &#8211; Perl formats </p>
<h2>DESCRIPTION</h2>
<p> Perl has a mechanism to help you generate simple reports and charts. To facilitate this, Perl helps you code up your output page close to how it will look when it&#8217;s printed. It can keep track of things like how many lines are on a page, what page you&#8217;re on, when to print page headers, etc. Keywords are borrowed from <font SIZE="-1">FORTRAN:</font> <code>format()</code> to declare and <code>write()</code> to execute; see their entries in perlfunc. Fortunately, the layout is much more legible, more like <font SIZE="-1">BASIC</font>&#8216;s <font SIZE="-1">PRINT USING</font> statement. Think of it as a poor man&#8217;s <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1). </p>
<p> Formats, like packages and subroutines, are declared rather than executed, so they may occur at any point in your program. (Usually it&#8217;s best to keep them all together though.) They have their own namespace apart from all the other &#8220;types&#8221; in Perl. This means that if you have a function named &#8220;Foo&#8221;, it is not the same thing as having a format named &#8220;Foo&#8221;. However, the default name for the format associated with a given filehandle is the same as the name of the filehandle. Thus, the default format for <font SIZE="-1">STDOUT</font> is named &#8220;<font SIZE="-1">STDOUT&#8221;,</font> and the default format for filehandle <font SIZE="-1">TEMP</font> is named &#8220;<font SIZE="-1">TEMP&#8221;.</font> They just look the same. They aren&#8217;t. </p>
<p> Output record formats are declared as follows: </p>
<pre>
    format NAME =
    FORMLIST
    .
</pre>
<p> If the name is omitted, format &#8220;<font SIZE="-1">STDOUT&#8221;</font> is defined. A single &#8220;.&#8221; in column 1 is used to terminate a format. <font SIZE="-1">FORMLIST</font> consists of a sequence of lines, each of which may be one of three types:</p>
<dl>
<dt>1.</p>
<dd> A comment, indicated by putting a &#8216;#&#8217; in the first column.</p>
<dt>2.</p>
<dd> A &#8220;picture&#8221; line giving the format for one output line.</p>
<dt>3.</p>
<dd> An argument line supplying values to plug into the previous picture line.</dl>
<p> Picture lines contain output field definitions, intermingled with literal text. These lines do not undergo any kind of variable interpolation. Field definitions are made up from a set of characters, for starting and extending a field to its desired width. This is the complete set of characters for field definitions: </p>
<pre><code>
   @    start of regular field
   ^    start of special field
   &lt;    pad character for left justification
   |    pad character for centering
   &gt;    pad character for right justification
#pad character for a right - justified numeric field
   0    instead of first #: pad number with leading zeroes
   .    decimal point within a numeric field
   ...  terminate a text field, show "..." as truncation evidence
   @*   variable width field for a multi-line value
   ^*   variable width field for next line of a multi-line value
   ~    suppress line with all fields empty
   ~~   repeat line until all fields are exhausted
</code></pre>
<p> Each field in a picture line starts with either &#8220;@&#8221; (at) or &#8220;^&#8221; (caret), indicating what we&#8217;ll call, respectively, a &#8220;regular&#8221; or &#8220;special&#8221; field. The choice of pad characters determines whether a field is textual or numeric. The tilde operators are not part of a field. Let&#8217;s look at the various possibilities in detail.</p>
<h3>Text Fields</h3>
<p> The length of the field is supplied by padding out the field with multiple &#8220;&lt;&#8221;, &#8220;&gt;&#8221;, or &#8220;|&#8221; characters to specify a non-numeric field with, respectively, left justification, right justification, or centering. For a regular field, the value (up to the first newline) is taken and printed according to the selected justification, truncating excess characters. If you terminate a text field with &#8220;&#8230;&#8221;, three dots will be shown if the value is truncated. A special text field may be used to do rudimentary multi-line text block filling; see &#8220;Using Fill Mode&#8221; for details. </p>
<pre>
   Example:
      format STDOUT =
      @&lt;&lt;&lt;&lt;&lt;&lt;   @||||||   @&gt;&gt;&gt;&gt;&gt;&gt;
      &quot;left&quot;,   &quot;middle&quot;, &quot;right&quot;
      .
   Output:
      left      middle    right
</pre>
<h3>Numeric Fields</h3>
<p> Using &#8220;#&#8221; as a padding character specifies a numeric field, with right justification. An optional &#8220;.&#8221; defines the position of the decimal point. With a &#8220;0&#8221; (zero) instead of the first &#8220;#&#8221;, the formatted number will be padded with leading zeroes if necessary. A special numeric field is blanked out if the value is undefined. If the resulting value would exceed the width specified the field is filled with &#8220;#&#8221; as overflow evidence. </p>
<pre>
   Example:
      format STDOUT =
      @###   @.###   @##.###  @###   @###   ^####
       42,   3.1415,  undef,    0, 10000,   undef
      .
   Output:
        42   3.142     0.000     0   ####
</pre>
<h3>The Field @* for Variable-Width Multi-Line Text</h3>
<p> The field &#8220;@*&#8221; can be used for printing multi-line, nontruncated values; it should (but need not) appear by itself on a line. A final line feed is chomped off, but all other characters are emitted verbatim.</p>
<h3>The Field ^* for Variable-Width One-line-at-a-time Text</h3>
<p> Like &#8220;@*&#8221;, this is a variable-width field. The value supplied must be a scalar variable. Perl puts the first line (up to the first &#8220;
&#8221;) of the text into the field, and then chops off the front of the string so that the next time the variable is referenced, more of the text can be printed. The variable will <i>not</i> be restored. </p>
<pre>
   Example:
      $text = &quot;line 1
line 2
line 3&quot;;
      format STDOUT =
      Text: ^*
            $text
      ~~    ^*
            $text
      .
   Output:
      Text: line 1
            line 2
            line 3
</pre>
<h3>Specifying Values</h3>
<p> The values are specified on the following format line in the same order as the picture fields. The expressions providing the values must be separated by commas. They are all evaluated in a list context before the line is processed, so a single list expression could produce multiple list elements. The expressions may be spread out to more than one line if enclosed in braces. If so, the opening brace must be the first token on the first line. If an expression evaluates to a number with a decimal part, and if the corresponding picture specifies that the decimal part should appear in the output (that is, any picture except multiple &#8220;#&#8221; characters <code>without</code> an embedded &#8220;.&#8221;), the character used for the decimal point is determined by the current <font SIZE="-1">LC_NUMERIC</font> locale if <tt>&quot;use locale&quot;</tt> is in effect. This means that, if, for example, the run-time environment happens to specify a German locale, &#8220;,&#8221; will be used instead of the default &#8220;.&#8221;. See perllocale and &#8220;<font SIZE="-1">WARNINGS&#8221;</font> for more information.</p>
<h3>Using Fill Mode</h3>
<p> On text fields the caret enables a kind of fill mode. Instead of an arbitrary expression, the value supplied must be a scalar variable that contains a text string. Perl puts the next portion of the text into the field, and then chops off the front of the string so that the next time the variable is referenced, more of the text can be printed. (Yes, this means that the variable itself is altered during execution of the <code>write()</code> call, and is not restored.) The next portion of text is determined by a crude line-breaking algorithm. You may use the carriage return character (<tt>&quot;&quot;</tt>) to force a line break. You can change which characters are legal to break on by changing the variable <tt>$:</tt> (that&#8217;s <tt>$FORMAT_LINE_BREAK_CHARACTERS</tt> if you&#8217;re using the English module) to a list of the desired characters. </p>
<p> Normally you would use a sequence of fields in a vertical stack associated with the same scalar variable to print out a block of text. You might wish to end the final field with the text &#8220;&#8230;&#8221;, which will appear in the output if the text was too long to appear in its entirety.</p>
<h3>Suppressing Lines Where All Fields Are Void</h3>
<p> Using caret fields can produce lines where all fields are blank. You can suppress such lines by putting a &#8220;~&#8221; (tilde) character anywhere in the line. The tilde will be translated to a space upon output.</p>
<h3>Repeating Format Lines</h3>
<p> If you put two contiguous tilde characters &#8220;~~&#8221; anywhere into a line, the line will be repeated until all the fields on the line are exhausted, i.e. undefined. For special (caret) text fields this will occur sooner or later, but if you use a text field of the at variety, the expression you supply had better not give the same value every time forever! (<tt>&quot;shift(@f)&quot;</tt> is a simple example that would work.) Don&#8217;t use a regular (at) numeric field in such lines, because it will never go blank.</p>
<h3>Top of Form Processing</h3>
<p> Top-of-form processing is by default handled by a format with the same name as the current filehandle with &#8220;_TOP&#8221; concatenated to it. It&#8217;s triggered at the top of each page. See &#8220;write&#8221; in perlfunc. </p>
<p> Examples: </p>
<p>#a report on the / etc / passwd file<br />
format STDOUT_TOP =<br />
    Passwd File<br />
        Name Login Office Uid Gid Home&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;.format STDOUT =<br />
        @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt;&lt;@ || || || | @&lt;&lt;&lt;&lt;&lt;&lt;@&gt;&gt;&gt;&gt; @&gt;&gt;&gt;&gt; @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt;<br />
        $name,<br />
       $login, $office, $uid, $gid, $home.<br />
#a report from a bug report form<br />
                                    format STDOUT_TOP = Bug Reports @&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;@ || | @&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;<br />
                                        $system,<br />
       $ %, $date&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;.format STDOUT = Subject : @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $subject Index : @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; ^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $index, $description Priority : @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; Date : @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; ^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $priority, $date, $description From : @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; ^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $from, $description Assigned to : @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; ^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $programmer, $description ~^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $description ~^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $description ~^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $description ~^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; $description ~^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &#8230; $description.</p>
<p> It is possible to intermix <code>print()</code>s with <code>write()</code>s on the same output channel, but you&#8217;ll have to handle <tt>&quot;$-&quot;</tt> (<tt>$FORMAT_LINES_LEFT</tt>) yourself.</p>
<h3>Format Variables</h3>
<p> The current format name is stored in the variable <tt>$~</tt> (<tt>$FORMAT_NAME</tt>), and the current top of form format name is in <tt>$^</tt> (<tt>$FORMAT_TOP_NAME</tt>). The current output page number is stored in <tt>$%</tt> (<tt>$FORMAT_PAGE_NUMBER</tt>), and the number of lines on the page is in <tt>$=</tt> (<tt>$FORMAT_LINES_PER_PAGE</tt>). Whether to autoflush output on this handle is stored in <tt>$|</tt> (<tt>$OUTPUT_AUTOFLUSH</tt>). The string output before each top of page (except the first) is stored in <tt>$^L</tt> (<tt>$FORMAT_FORMFEED</tt>). These variables are set on a per-filehandle basis, so you&#8217;ll need to <code>select()</code> into a different one to affect them: </p>
<pre>
    select((select(OUTF),
            $~ = &quot;My_Other_Format&quot;,
            $^ = &quot;My_Top_Format&quot;
           )[0]);
</pre>
<p> Pretty ugly, eh? It&#8217;s a common idiom though, so don&#8217;t be too surprised when you see it. You can at least use a temporary variable to hold the previous filehandle: (this is a much better approach in general, because not only does legibility improve, you now have an intermediary stage in the expression to single-step the debugger through): </p>
<p>$ofh = select(OUTF);<br />
$ ~ = &#8220;My_Other_Format&#8221;;<br />
$ ^ = &#8220;My_Top_Format&#8221;;<br />
select($ofh);</p>
<p> If you use the English module, you can even read the variable names: </p>
<p>use English;<br />
$ofh = select(OUTF);<br />
$FORMAT_NAME = &#8220;My_Other_Format&#8221;;<br />
$FORMAT_TOP_NAME = &#8220;My_Top_Format&#8221;;<br />
select($ofh);</p>
<p> But you still have those funny <code>select()</code>s. So just use the FileHandle module. Now, you can access these special variables using lowercase method names instead: </p>
<pre>
    use FileHandle;
    format_name     OUTF &quot;My_Other_Format&quot;;
    format_top_name OUTF &quot;My_Top_Format&quot;;
</pre>
<p> Much better!</p>
<h2>NOTES</h2>
<p> Because the values line may contain arbitrary expressions (for at fields, not caret fields), you can farm out more sophisticated processing to other functions, like <code>sprintf()</code> or one of your own. For example: </p>
<pre>
    format Ident =
        @&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;
        &amp;commify($n)
    .
</pre>
<p> To get a real at or caret into the field, do this: </p>
<pre>
    format Ident =
    I have an @ here.
            &quot;@&quot;
    .
</pre>
<p> To center a whole line of text, do something like this: </p>
<p>format Ident =<br />
    @ || || || || || || || || || || || || || || || || || || || || || || || |<br />
                                                                               &#8220;Some text line&#8221;<br />
                                                                                   .</p>
<p> There is no builtin way to say &#8220;float this to the right hand side of the page, however wide it is.&#8221; You have to specify where it goes. The truly desperate can generate their own format on the fly, based on the current number of columns, and then <code>eval()</code> it: </p>
<p>$format = &#8220;format STDOUT = 
&#8221;<br />
              .&#8217;^&#8217;.'&lt;&#8216; x $cols.&#8221;
&#8221;<br />
              .&#8217;$entry&#8217;.&#8221;
&#8221;<br />
              .&#8221;	^&#8221;.&#8221;&lt;&#8221; x($cols &#8211; 8)<br />
              .&#8221;~~
&#8221;<br />
              .&#8217;$entry&#8217;.&#8221;
&#8221;<br />
              .&#8221;.
&#8221;;<br />
print $format if $Debugging;<br />
eval $format;<br />
die $ @ if $ @;</p>
<p> Which would generate a format looking something like this: </p>
<pre>
 format STDOUT =
 ^&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;
 $entry
         ^&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;~~
 $entry
 .
</pre>
<p> Here&#8217;s a little program that&#8217;s somewhat like <code><a href="/docs/linux/man/1-fmt/">fmt</a></code>(1): </p>
<p>format =<br />
    ^ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; ~~$_<br />
                                                                                                          .$ /<br />
    = &#8221;;<br />
while (&lt;&gt;) {<br />
    s /\s *
\s * / / g;<br />
    write;<br />
}</p>
<h3>Footers</h3>
<p> While <tt>$FORMAT_TOP_NAME</tt> contains the name of the current header format, there is no corresponding mechanism to automatically do the same thing for a footer. Not knowing how big a format is going to be until you evaluate it is one of the major problems. It&#8217;s on the <font SIZE="-1">TODO</font> list. </p>
<p> Here&#8217;s one strategy: If you have a fixed-size footer, you can get footers by checking <tt>$FORMAT_LINES_LEFT</tt> before each <code>write()</code> and print the footer yourself if necessary. </p>
<p> Here&#8217;s another strategy: Open a pipe to yourself, using <tt>&quot;open(MYSELF, &quot;|-&quot;)&quot;</tt> (see &#8220;open&#8221; in perlfunc) and always <code>write()</code> to <font SIZE="-1">MYSELF</font> instead of <font SIZE="-1">STDOUT.</font> Have your child process massage its <font SIZE="-1">STDIN</font> to rearrange headers and footers however you like. Not very convenient, but doable.</p>
<h3>Accessing Formatting Internals</h3>
<p> For low-level access to the formatting mechanism, you may use <code>formline()</code> and access <tt>$^A</tt> (the <tt>$ACCUMULATOR</tt> variable) directly. </p>
<p> For example: </p>
<pre>
    $str = formline &lt;&lt;'END', 1,2,3;
    @&lt;&lt;&lt;  @|||  @&gt;&gt;&gt;
    END
    print &quot;Wow, I just stored '$^A' in the accumulator!
&quot;;
</pre>
<p> Or to make an <code>swrite()</code> subroutine, which is to <code>write()</code> what <code>sprintf()</code> is to <code>printf()</code>, do this: </p>
<pre><code>
use Carp;
sub swrite
{
    croak "usage: swrite PICTURE ARGS" unless @_;
    my $format = shift;
    $ ^ A = "";
    formline($format, @_);
    return $ ^ A;
}
$string = swrite(&lt;&lt; 'END', 1, 2, 3);
Check me out
    @&lt;&lt;&lt;@ || | @&gt;&gt;&gt;
        END
            print $string;
</code></pre>
<h2>WARNINGS</h2>
<p> The lone dot that ends a format can also prematurely end a mail message passing through a misconfigured Internet mailer (and based on experience, such misconfiguration is the rule, not the exception). So when sending format code through mail, you should indent it so that the format-ending dot is not on the left margin; this will prevent <font SIZE="-1">SMTP</font> cutoff. </p>
<p> Lexical variables (declared with &#8220;my&#8221;) are not visible within a format unless the format is declared within the scope of the lexical variable. </p>
<p> If a program&#8217;s environment specifies an <font SIZE="-1">LC_NUMERIC</font> locale and <tt>&quot;use locale&quot;</tt> is in effect when the format is declared, the locale is used to specify the decimal point character in formatted output. Formatted output cannot be controlled by <tt>&quot;use locale&quot;</tt> at the time when <code>write()</code> is called. See perllocale for further discussion of locale handling. </p>
<p> Within strings that are to be displayed in a fixed-length text field, each control character is substituted by a space. (But remember the special meaning of <tt>&quot;&quot;</tt> when using fill mode.) This is done to avoid misalignment when control characters &#8220;disappear&#8221; on some output media. </p>
<h2>Index</h2>
