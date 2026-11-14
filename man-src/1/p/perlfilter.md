---
title: "perlfilter(1)"
name: "perlfilter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfilter/"
description: "perlfilter – Source Filters"
---

<h2 class="name">NAME</h2>
<p> perlfilter &#8211; Source Filters </p>
<h2>DESCRIPTION</h2>
<p> This article is about a little-known feature of Perl called <i>source filters</i>. Source filters alter the program text of a module before Perl sees it, much as a C preprocessor alters the source text of a C program before the compiler sees it. This article tells you more about what source filters are, how they work, and how to write your own. </p>
<p> The original purpose of source filters was to let you encrypt your program source to prevent casual piracy. This isn&#8217;t all they can do, as you&#8217;ll soon learn. But first, the basics.</p>
<h2>CONCEPTS</h2>
<p> Before the Perl interpreter can execute a Perl script, it must first read it from a file into memory for parsing and compilation. If that script itself includes other scripts with a <tt>&quot;use&quot;</tt> or <tt>&quot;require&quot;</tt> statement, then each of those scripts will have to be read from their respective files as well. </p>
<p> Now think of each logical connection between the Perl parser and an individual file as a <i>source stream</i>. A source stream is created when the Perl parser opens a file, it continues to exist as the source code is read into memory, and it is destroyed when Perl is finished parsing the file. If the parser encounters a <tt>&quot;require&quot;</tt> or <tt>&quot;use&quot;</tt> statement in a source stream, a new and distinct stream is created just for that file. </p>
<p> The diagram below represents a single source stream, with the flow of source from a Perl script file on the left into the Perl parser on the right. This is how Perl normally operates. </p>
<pre><code>
file-- -- ---&gt;parser
</code></pre>
<p> There are two important points to remember:</p>
<dl>
<dt>1.</p>
<dd> Although there can be any number of source streams in existence at any given time, only one will be active.</p>
<dt>2.</p>
<dd> Every source stream is associated with only one file.</dl>
<p> A source filter is a special kind of Perl module that intercepts and modifies a source stream before it reaches the parser. A source filter changes our diagram like this: </p>
<p>file&#8211; &#8212; &gt; filter&#8211; &#8212; &gt; parser</p>
<p> If that doesn&#8217;t make much sense, consider the analogy of a command pipeline. Say you have a shell script stored in the compressed file <i>trial.gz</i>. The simple pipeline command below runs the script without needing to create a temporary file to hold the uncompressed file. </p>
<pre>
    gunzip -c trial.gz | sh
</pre>
<p> In this case, the data flow from the pipeline can be represented as follows: </p>
<p>trial.gz&#8211; &#8212; &gt; gunzip&#8211; &#8212; &gt; sh</p>
<p> With source filters, you can store the text of your script compressed and use a source filter to uncompress it for Perl&#8217;s parser: </p>
<p>compressed gunzip<br />
    Perl program&#8212;&gt;source filter&#8212;&gt;parser</p>
<h2>USING FILTERS</h2>
<p> So how do you use a source filter in a Perl script? Above, I said that a source filter is just a special kind of module. Like all Perl modules, a source filter is invoked with a use statement. </p>
<p> Say you want to pass your Perl source through the C preprocessor before execution. As it happens, the source filters distribution comes with a C preprocessor filter module called Filter::cpp. </p>
<p> Below is an example program, <tt>&quot;cpp_test&quot;</tt>, which makes use of this filter. Line numbers have been added to allow specific lines to be referenced easily. </p>
<p>1 : use Filter::cpp;<br />
2 : #define TRUE 1 3 : $a = TRUE;<br />
4 : print &#8220;a = $a
&#8221;;</p>
<p> When you execute this script, Perl creates a source stream for the file. Before the parser processes any of the lines from the file, the source stream looks like this: </p>
<p>cpp_test&#8211; &#8212; &#8212; &#8212;&gt;parser</p>
<p> Line 1, <tt>&quot;use Filter::cpp&quot;</tt>, includes and installs the <tt>&quot;cpp&quot;</tt> filter module. All source filters work this way. The use statement is compiled and executed at compile time, before any more of the file is read, and it attaches the cpp filter to the source stream behind the scenes. Now the data flow looks like this: </p>
<p>cpp_test&#8211; &#8212; &gt; cpp filter&#8211; &#8212; &gt; parser</p>
<p> As the parser reads the second and subsequent lines from the source stream, it feeds those lines through the <tt>&quot;cpp&quot;</tt> source filter before processing them. The <tt>&quot;cpp&quot;</tt> filter simply passes each line through the real C preprocessor. The output from the C preprocessor is then inserted back into the source stream by the filter. </p>
<p>.-&gt;cpp&#8211;.| |<br />
    | |<br />
    | &lt;-&#8216; cpp_test&#8211; &#8211;&gt; cpp filter&#8211; &#8212; &gt; parser</p>
<p> The parser then sees the following code: </p>
<pre>
    use Filter::cpp;
    $a = 1;
    print &quot;a = $a
&quot;;
</pre>
<p> Let&#8217;s consider what happens when the filtered code includes another module with use: </p>
<p>1 : use Filter::cpp;<br />
2 : #define TRUE 1 3 : use Fred;<br />
4 : $a = TRUE;<br />
5 : print &#8220;a = $a
&#8221;;</p>
<p> The <tt>&quot;cpp&quot;</tt> filter does not apply to the text of the Fred module, only to the text of the file that used it (<tt>&quot;cpp_test&quot;</tt>). Although the use statement on line 3 will pass through the cpp filter, the module that gets included (<tt>&quot;Fred&quot;</tt>) will not. The source streams look like this after line 3 has been parsed and before line 4 is parsed: </p>
<p>cpp_test&#8212;&gt;cpp filter&#8212;&gt;parser(INACTIVE)<br />
        Fred.pm&#8211; &#8212; &gt; parser</p>
<p> As you can see, a new stream has been created for reading the source from <tt>&quot;Fred.pm&quot;</tt>. This stream will remain active until all of <tt>&quot;Fred.pm&quot;</tt> has been parsed. The source stream for <tt>&quot;cpp_test&quot;</tt> will still exist, but is inactive. Once the parser has finished reading Fred.pm, the source stream associated with it will be destroyed. The source stream for <tt>&quot;cpp_test&quot;</tt> then becomes active again and the parser reads line 4 and subsequent lines from <tt>&quot;cpp_test&quot;</tt>. </p>
<p> You can use more than one source filter on a single file. Similarly, you can reuse the same filter in as many files as you like. </p>
<p> For example, if you have a uuencoded and compressed source file, it is possible to stack a uudecode filter and an uncompression filter like this: </p>
<p>use Filter::uudecode;<br />
use Filter::uncompress;<br />
    M&#8217;XL(&#8220;.H&lt;US4&#8221;V9I;F%L&#8217;)Q;<br />
    &gt; 7 / ;<br />
    1I;_&gt;_I3=&amp;E=%:F*I&#8221;T?22Q/<br />
    M6]9*&lt;IQCO*XFT&#8221;0[PL%%&#8217;Y+IG?WN^ZYN-$&#8217;J.[.JE$,20/?K=_[&gt;<br />
    &#8230;</p>
<p> Once the first line has been processed, the flow will look like this: </p>
<p>file&#8212;&gt;uudecode&#8212;&gt;uncompress&#8212;&gt;parser<br />
    filter filter</p>
<p> Data flows through filters in the same order they appear in the source file. The uudecode filter appeared before the uncompress filter, so the source file will be uudecoded before it&#8217;s uncompressed.</p>
<h2>WRITING A SOURCE FILTER</h2>
<p> There are three ways to write your own source filter. You can write it in C, use an external program as a filter, or write the filter in Perl. I won&#8217;t cover the first two in any great detail, so I&#8217;ll get them out of the way first. Writing the filter in Perl is most convenient, so I&#8217;ll devote the most space to it.</p>
<h2>WRITING A SOURCE FILTER IN C</h2>
<p> The first of the three available techniques is to write the filter completely in C. The external module you create interfaces directly with the source filter hooks provided by Perl. </p>
<p> The advantage of this technique is that you have complete control over the implementation of your filter. The big disadvantage is the increased complexity required to write the filter &#8211; not only do you need to understand the source filter hooks, but you also need a reasonable knowledge of Perl guts. One of the few times it is worth going to this trouble is when writing a source scrambler. The <tt>&quot;decrypt&quot;</tt> filter (which unscrambles the source before Perl parses it) included with the source filter distribution is an example of a C source filter (see Decryption Filters, below).</p>
<dl>
<dt><code>Decryption Filters</code></p>
<dd> All decryption filters work on the principle of &#8220;security through obscurity.&#8221; Regardless of how well you write a decryption filter and how strong your encryption algorithm is, anyone determined enough can retrieve the original source code. The reason is quite simple &#8211; once the decryption filter has decrypted the source back to its original form, fragments of it will be stored in the computer&#8217;s memory as Perl parses it. The source might only be in memory for a short period of time, but anyone possessing a debugger, skill, and lots of patience can eventually reconstruct your program. </p>
<p> That said, there are a number of steps that can be taken to make life difficult for the potential cracker. The most important: Write your decryption filter in C and statically link the decryption module into the Perl binary. For further tips to make life difficult for the potential cracker, see the file <i>decrypt.pm</i> in the source filters distribution.</dl>
<h2>CREATING A SOURCE FILTER AS A SEPARATE EXECUTABLE</h2>
<p> An alternative to writing the filter in C is to create a separate executable in the language of your choice. The separate executable reads from standard input, does whatever processing is necessary, and writes the filtered data to standard output. <tt>&quot;Filter::cpp&quot;</tt> is an example of a source filter implemented as a separate executable &#8211; the executable is the C preprocessor bundled with your C compiler. </p>
<p> The source filter distribution includes two modules that simplify this task: <tt>&quot;Filter::exec&quot;</tt> and <tt>&quot;Filter::sh&quot;</tt>. Both allow you to run any external executable. Both use a coprocess to control the flow of data into and out of the external executable. (For details on coprocesses, see Stephens, W.R., &#8220;Advanced Programming in the <font SIZE="-1">UNIX</font> Environment.&#8221; Addison-Wesley, <font SIZE="-1">ISBN 0-210-56317-7,</font> pages 441-445.) The difference between them is that <tt>&quot;Filter::exec&quot;</tt> spawns the external command directly, while <tt>&quot;Filter::sh&quot;</tt> spawns a shell to execute the external command. (Unix uses the Bourne shell; <font SIZE="-1">NT</font> uses the cmd shell.) Spawning a shell allows you to make use of the shell metacharacters and redirection facilities. </p>
<p> Here is an example script that uses <tt>&quot;Filter::sh&quot;</tt>: </p>
<pre>
    use Filter::sh 'tr XYZ PQR';
    $a = 1;
    print &quot;XYZ a = $a
&quot;;
</pre>
<p> The output you&#8217;ll get when the script is executed: </p>
<pre>
    PQR a = 1
</pre>
<p> Writing a source filter as a separate executable works fine, but a small performance penalty is incurred. For example, if you execute the small example above, a separate subprocess will be created to run the Unix <tt>&quot;tr&quot;</tt> command. Each use of the filter requires its own subprocess. If creating subprocesses is expensive on your system, you might want to consider one of the other options for creating source filters.</p>
<h2>WRITING A SOURCE FILTER IN PERL</h2>
<p> The easiest and most portable option available for creating your own source filter is to write it completely in Perl. To distinguish this from the previous two techniques, I&#8217;ll call it a Perl source filter. </p>
<p> To help understand how to write a Perl source filter we need an example to study. Here is a complete source filter that performs rot13 decoding. (Rot13 is a very simple encryption scheme used in Usenet postings to hide the contents of offensive posts. It moves every letter forward thirteen places, so that A becomes N, B becomes O, and Z becomes M.) </p>
<p>package Rot13;<br />
use Filter::Util::Call;<br />
sub import<br />
{<br />
    my($type) = @_;<br />
    my($ref) = [];<br />
    filter_add(bless $ref);<br />
}<br />
sub filter<br />
{<br />
    my($self) = @_;<br />
    my($status);<br />
    tr / n &#8211; za &#8211; mN &#8211; ZA &#8211; M / a &#8211; zA &#8211; Z / if ($status = filter_read()) &gt; 0;<br />
    $status;<br />
}<br />
1;</p>
<p> All Perl source filters are implemented as Perl classes and have the same basic structure as the example above. </p>
<p> First, we include the <tt>&quot;Filter::Util::Call&quot;</tt> module, which exports a number of functions into your filter&#8217;s namespace. The filter shown above uses two of these functions, <tt>&quot;filter_add()&quot;</tt> and <tt>&quot;filter_read()&quot;</tt>. </p>
<p> Next, we create the filter object and associate it with the source stream by defining the <tt>&quot;import&quot;</tt> function. If you know Perl well enough, you know that <tt>&quot;import&quot;</tt> is called automatically every time a module is included with a use statement. This makes <tt>&quot;import&quot;</tt> the ideal place to both create and install a filter object. </p>
<p> In the example filter, the object (<tt>$ref</tt>) is blessed just like any other Perl object. Our example uses an anonymous array, but this isn&#8217;t a requirement. Because this example doesn&#8217;t need to store any context information, we could have used a scalar or hash reference just as well. The next section demonstrates context data. </p>
<p> The association between the filter object and the source stream is made with the <tt>&quot;filter_add()&quot;</tt> function. This takes a filter object as a parameter (<tt>$ref</tt> in this case) and installs it in the source stream. </p>
<p> Finally, there is the code that actually does the filtering. For this type of Perl source filter, all the filtering is done in a method called <tt>&quot;filter()&quot;</tt>. (It is also possible to write a Perl source filter using a closure. See the <tt>&quot;Filter::Util::Call&quot;</tt> manual page for more details.) It&#8217;s called every time the Perl parser needs another line of source to process. The <tt>&quot;filter()&quot;</tt> method, in turn, reads lines from the source stream using the <tt>&quot;filter_read()&quot;</tt> function. </p>
<p> If a line was available from the source stream, <tt>&quot;filter_read()&quot;</tt> returns a status value greater than zero and appends the line to <tt>$_</tt>. A status value of zero indicates end-of-file, less than zero means an error. The filter function itself is expected to return its status in the same way, and put the filtered line it wants written to the source stream in <tt>$_</tt>. The use of <tt>$_</tt> accounts for the brevity of most Perl source filters. </p>
<p> In order to make use of the rot13 filter we need some way of encoding the source file in rot13 format. The script below, <tt>&quot;mkrot13&quot;</tt>, does just that. </p>
<p>die &#8220;usage mkrot13 filename
&#8221; unless @ARGV;<br />
my $in = $ARGV[0];<br />
my $out = &#8220;$in.tmp&#8221;;<br />
open(IN, &#8220;&lt;$in&#8221;) or die &#8220;Cannot open file $in: $!
&#8221;;<br />
open(OUT, &#8220;&gt;$out&#8221;) or die &#8220;Cannot open file $out: $!
&#8221;;<br />
print OUT &#8220;use Rot13;
&#8221;;<br />
while (&lt;IN&gt;) {<br />
    tr / a &#8211; zA &#8211; Z / n &#8211; za &#8211; mN &#8211; ZA &#8211; M / ;<br />
    print OUT;<br />
}<br />
close IN;<br />
close OUT;<br />
unlink $in;<br />
rename $out, $in;</p>
<p> If we encrypt this with <tt>&quot;mkrot13&quot;</tt>: </p>
<pre>
    print &quot; hello fred 
&quot;;
</pre>
<p> the result will be this: </p>
<pre>
    use Rot13;
    cevag &quot;uryyb serq&quot;;
</pre>
<p> Running it produces this output: </p>
<pre>
    hello fred
</pre>
<h2>USING CONTEXT: THE DEBUG FILTER</h2>
<p> The rot13 example was a trivial example. Here&#8217;s another demonstration that shows off a few more features. </p>
<p> Say you wanted to include a lot of debugging code in your Perl script during development, but you didn&#8217;t want it available in the released product. Source filters offer a solution. In order to keep the example simple, let&#8217;s say you wanted the debugging output to be controlled by an environment variable, <tt>&quot;DEBUG&quot;</tt>. Debugging code is enabled if the variable exists, otherwise it is disabled. </p>
<p> Two special marker lines will bracket debugging code, like this: </p>
<p>##DEBUG_BEGIN if ($year &gt; 1999)<br />
{<br />
    warn &#8220;Debug: millennium bug in year $year
&#8221;;<br />
}<br />
##DEBUG_END</p>
<p> The filter ensures that Perl parses the code between the &lt;<font SIZE="-1">DEBUG_BEGIN</font>&gt; and <tt>&quot;DEBUG_END&quot;</tt> markers only when the <tt>&quot;DEBUG&quot;</tt> environment variable exists. That means that when <tt>&quot;DEBUG&quot;</tt> does exist, the code above should be passed through the filter unchanged. The marker lines can also be passed through as-is, because the Perl parser will see them as comment lines. When <tt>&quot;DEBUG&quot;</tt> isn&#8217;t set, we need a way to disable the debug code. A simple way to achieve that is to convert the lines between the two markers into comments: </p>
<p>##DEBUG_BEGIN<br />
#if ($year &gt; 1999) {<br />
#warn &#8220;Debug: millennium bug in year $year
&#8221;;<br />
#}<br />
    ##DEBUG_END</p>
<p> Here is the complete Debug filter: </p>
<p>package Debug;<br />
use strict;<br />
use warnings;<br />
use Filter::Util::Call;<br />
use constant TRUE = &gt; 1;<br />
use constant FALSE = &gt; 0;<br />
sub import<br />
{<br />
    my($type) = @_;<br />
    my(% context) = (Enabled = &gt; defined $ENV{DEBUG},<br />
                     InTraceBlock = &gt; FALSE,<br />
                     Filename = &gt; (caller)[1],<br />
                     LineNo = &gt; 0,<br />
                     LastBegin = &gt; 0, );<br />
    filter_add(bless \% context);<br />
}<br />
sub Die<br />
{<br />
    my($self) = shift;<br />
    my($message) = shift;<br />
    my($line_no) = shift || $self-&gt;{LastBegin};<br />
    die &#8220;$message at $self-&gt;{Filename} line $line_no.
&#8221;<br />
}<br />
sub filter<br />
{<br />
    my($self) = @_;<br />
    my($status);<br />
    $status = filter_read();<br />
    ++$self-&gt;{LineNo};<br />
#deal with EOF / error first<br />
    if ($status &lt;= 0) {<br />
        $self-&gt;Die(&#8220;DEBUG_BEGIN has no DEBUG_END&#8221;) if $self-&gt;{InTraceBlock};<br />
        return $status;<br />
    }<br />
    if ($self-&gt;{InTraceBlock}) {<br />
        if (/ ^\s *##\s * DEBUG_BEGIN /) {<br />
            $self-&gt;Die(&#8220;Nested DEBUG_BEGIN&#8221;, $self-&gt;{LineNo})<br />
        }<br />
        elsif(/ ^\s *##\s *DEBUG_END /)<br />
        {<br />
            $self-&gt;{InTraceBlock} = FALSE;<br />
        }<br />
#comment out the debug lines when the filter is disabled<br />
        s / ^ / # / if !$self-&gt;{<br />
                        Enabled};<br />
    }<br />
    elsif(/ ^\s *##\s *DEBUG_BEGIN /)<br />
    {<br />
        $self-&gt;{InTraceBlock} = TRUE;<br />
        $self-&gt;{LastBegin} = $self-&gt;{LineNo};<br />
    }<br />
    elsif(/ ^\s *##\s *DEBUG_END /)<br />
    {<br />
        $self-&gt;Die(&#8220;DEBUG_END has no DEBUG_BEGIN&#8221;, $self-&gt;{LineNo});<br />
    }<br />
    return $status;<br />
}<br />
1;</p>
<p> The big difference between this filter and the previous example is the use of context data in the filter object. The filter object is based on a hash reference, and is used to keep various pieces of context information between calls to the filter function. All but two of the hash fields are used for error reporting. The first of those two, Enabled, is used by the filter to determine whether the debugging code should be given to the Perl parser. The second, InTraceBlock, is true when the filter has encountered a <tt>&quot;DEBUG_BEGIN&quot;</tt> line, but has not yet encountered the following <tt>&quot;DEBUG_END&quot;</tt> line. </p>
<p> If you ignore all the error checking that most of the code does, the essence of the filter is as follows: </p>
<p>sub filter<br />
{<br />
    my($self) = @_;<br />
    my($status);<br />
    $status = filter_read();<br />
#deal with EOF / error first<br />
    return $status if $status &lt;= 0;<br />
    if ($self-&gt;{InTraceBlock}) {<br />
        if (/ ^\s *##\s * DEBUG_END /) {<br />
            $self-&gt;{InTraceBlock} = FALSE<br />
        }<br />
#comment out debug lines when the filter is disabled<br />
        s / ^ / # / if !$self-&gt;{<br />
                        Enabled};<br />
    }<br />
    elsif(/ ^\s *##\s *DEBUG_BEGIN /)<br />
    {<br />
        $self-&gt;{InTraceBlock} = TRUE;<br />
    }<br />
    return $status;<br />
}</p>
<p> Be warned: just as the C-preprocessor doesn&#8217;t know C, the Debug filter doesn&#8217;t know Perl. It can be fooled quite easily: </p>
<pre>
    print &lt;&lt;EOM;
    ##DEBUG_BEGIN
    EOM
</pre>
<p> Such things aside, you can see that a lot can be achieved with a modest amount of code.</p>
<h2>CONCLUSION</h2>
<p> You now have better understanding of what a source filter is, and you might even have a possible use for them. If you feel like playing with source filters but need a bit of inspiration, here are some extra features you could add to the Debug filter. </p>
<p> First, an easy one. Rather than having debugging code that is all-or-nothing, it would be much more useful to be able to control which specific blocks of debugging code get included. Try extending the syntax for debug blocks to allow each to be identified. The contents of the <tt>&quot;DEBUG&quot;</tt> environment variable can then be used to control which blocks get included. </p>
<p> Once you can identify individual blocks, try allowing them to be nested. That isn&#8217;t difficult either. </p>
<p> Here is an interesting idea that doesn&#8217;t involve the Debug filter. Currently Perl subroutines have fairly limited support for formal parameter lists. You can specify the number of parameters and their type, but you still have to manually take them out of the <tt>@_</tt> array yourself. Write a source filter that allows you to have a named parameter list. Such a filter would turn this: </p>
<pre>
    sub MySub ($first, $second, @rest) { ... }
</pre>
<p> into this: </p>
<pre><code>
sub MySub($$ @)
{
    my($first) = shift;
    my($second) = shift;
    my(@rest) = @_;
    ...
}
</code></pre>
<p> Finally, if you feel like a real challenge, have a go at writing a full-blown Perl macro preprocessor as a source filter. Borrow the useful features from the C preprocessor and any other macro processors you know. The tricky bit will be choosing how much knowledge of Perl&#8217;s syntax you want your filter to have.</p>
<h2>LIMITATIONS</h2>
<p> Source filters only work on the string level, thus are highly limited in its ability to change source code on the fly. It cannot detect comments, quoted strings, heredocs, it is no replacement for a real parser. The only stable usage for source filters are encryption, compression, or the byteloader, to translate binary code back to source code. </p>
<p> See for example the limitations in Switch, which uses source filters, and thus is does not work inside a string eval, the presence of regexes with embedded newlines that are specified with raw <tt>&quot;/.../&quot;</tt> delimiters and don&#8217;t have a modifier <tt>&quot;//x&quot;</tt> are indistinguishable from code chunks beginning with the division operator <tt>&quot;/&quot;</tt>. As a workaround you must use <tt>&quot;m/.../&quot;</tt> or <tt>&quot;m?...?&quot;</tt> for such patterns. Also, the presence of regexes specified with raw <tt>&quot;?...?&quot;</tt> delimiters may cause mysterious errors. The workaround is to use <tt>&quot;m?...?&quot;</tt> instead. See &lt;<a rel="nofollow" href="http://search.cpan.org/perldoc?Switch#LIMITATIONS">http://search.cpan.org/perldoc?Switch#LIMITATIONS</a>&gt; </p>
<p> Currently the content of the <tt>&quot;__DATA__&quot;</tt> block is not filtered. </p>
<p> Currently internal buffer lengths are limited to 32-bit only.</p>
<h2>THINGS TO LOOK OUT FOR</h2>
<dl>
<dt>Some Filters Clobber the &quot;DATA&quot; Handle</p>
<dd> Some source filters use the <tt>&quot;DATA&quot;</tt> handle to read the calling program. When using these source filters you cannot rely on this handle, nor expect any particular kind of behavior when operating on it. Filters based on Filter::Util::Call (and therefore Filter::Simple) do not alter the <tt>&quot;DATA&quot;</tt> filehandle, but on the other hand totally ignore the text after <tt>&quot;__DATA__&quot;</tt>.</dl>
<h2>REQUIREMENTS</h2>
<p> The Source Filters distribution is available on <font SIZE="-1">CPAN,</font> in </p>
<pre>
    CPAN/modules/by-module/Filter
</pre>
<p> Starting from Perl 5.8 Filter::Util::Call (the core part of the Source Filters distribution) is part of the standard Perl distribution. Also included is a friendlier interface called Filter::Simple, by Damian Conway.</p>
<h2>AUTHOR</h2>
<p> Paul Marquess &lt;Paul.Marquess [at] btinternet.com&gt; </p>
<p> Reini Urban &lt;rurban [at] cpan.org&gt;</p>
<h2>Copyrights</h2>
<p> The first version of this article originally appeared in The Perl Journal #11, and is copyright 1998 The Perl Journal. It appears courtesy of Jon Orwant and The Perl Journal. This document may be distributed under the same terms as Perl itself. </p>
<h2>Index</h2>
