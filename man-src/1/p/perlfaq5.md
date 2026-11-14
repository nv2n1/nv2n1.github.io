---
title: "perlfaq5(1)"
name: "perlfaq5"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq5/"
description: "perlfaq5 – Files and Formats"
---

<h2 class="name">NAME</h2>
<p> perlfaq5 &#8211; Files and Formats </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> This section deals with I/O and the &#8220;f&#8221; issues: filehandles, flushing, formats, and footers.</p>
<h3>How do I flush/unbuffer an output filehandle? Why must I do this?</h3>
<p> (contributed by brian d foy) </p>
<p> You might like to read Mark Jason Dominus&#8217;s &#8220;Suffering From Buffering&#8221; at &lt;<a rel="nofollow" href="http://perl.plover.com/FAQs/Buffering.html">http://perl.plover.com/FAQs/Buffering.html</a>&gt; . </p>
<p> Perl normally buffers output so it doesn&#8217;t make a system call for every bit of output. By saving up output, it makes fewer expensive system calls. For instance, in this little bit of code, you want to print a dot to the screen for every line you process to watch the progress of your program. Instead of seeing a dot for every line, Perl buffers the output and you have a long wait before you see a row of 50 dots all at once: </p>
<pre><code>
#long wait, then row of dots all at once
while (&lt;&gt;) {
    print ".";
    print "
" unless++ $count % 50;
#... expensive line processing operations
}
</code></pre>
<p> To get around this, you have to unbuffer the output filehandle, in this case, <tt>&quot;STDOUT&quot;</tt>. You can set the special variable <tt>$|</tt> to a true value (mnemonic: making your filehandles &#8220;piping hot&#8221;): </p>
<p>$ | ++;<br />
#dot shown immediately<br />
while (&lt;&gt;) {<br />
    print &#8220;.&#8221;;<br />
    print &#8220;
&#8221; unless++ $count % 50;<br />
#&#8230; expensive line processing operations<br />
}</p>
<p> The <tt>$|</tt> is one of the per-filehandle special variables, so each filehandle has its own copy of its value. If you want to merge standard output and standard error for instance, you have to unbuffer each (although <font SIZE="-1">STDERR</font> might be unbuffered by default): </p>
<p>{<br />
    my $previous_default = select(STDOUT);<br />
#save previous default $ | ++;<br />
#autoflush STDOUT<br />
        select(STDERR);<br />
    $ | ++;<br />
#autoflush STDERR, to be sure<br />
                           select($previous_default);<br />
#restore previous default<br />
}<br />
#now should alternate.and +<br />
while (1) {<br />
    sleep 1;<br />
    print STDOUT &#8220;.&#8221;;<br />
    print STDERR &#8220;+&#8221;;<br />
    print STDOUT &#8220;
&#8221; unless++ $count % 25;<br />
}</p>
<p> Besides the <tt>$|</tt> special variable, you can use <tt>&quot;binmode&quot;</tt> to give your filehandle a <tt>&quot;:unix&quot;</tt> layer, which is unbuffered: </p>
<p>binmode(STDOUT, &#8220;:unix&#8221;);<br />
while (1) {<br />
    sleep 1;<br />
    print &#8220;.&#8221;;<br />
    print &#8220;
&#8221; unless++ $count % 50;<br />
}</p>
<p> For more information on output layers, see the entries for <tt>&quot;binmode&quot;</tt> and open in perlfunc, and the PerlIO module documentation. </p>
<p> If you are using IO::Handle or one of its subclasses, you can call the <tt>&quot;autoflush&quot;</tt> method to change the settings of the filehandle: </p>
<p>use IO::Handle;<br />
open my($io_fh), &#8220;&gt;&#8221;, &#8220;output.txt&#8221;;<br />
$io_fh-&gt;autoflush(1);</p>
<p> The IO::Handle objects also have a <tt>&quot;flush&quot;</tt> method. You can flush the buffer any time you want without auto-buffering </p>
<pre>
    $io_fh-&gt;flush;
</pre>
<h3>How do I change, delete, or insert a line in a file, or append to the beginning of a file?</h3>
<p> (contributed by brian d foy) </p>
<p> The basic idea of inserting, changing, or deleting a line from a text file involves reading and printing the file to the point you want to make the change, making the change, then reading and printing the rest of the file. Perl doesn&#8217;t provide random access to lines (especially since the record input separator, <tt>$/</tt>, is mutable), although modules such as Tie::File can fake it. </p>
<p> A Perl program to do these tasks takes the basic form of opening a file, printing its lines, then closing the file: </p>
<p>open my $in, &#8216;&lt;&#8216;, $file or die &#8220;Can&#8217;t read old file: $!&#8221;;<br />
open my $out, &#8216;&gt;&#8217;, &#8220;$file.new&#8221; or die &#8220;Can&#8217;t write new file: $!&#8221;;<br />
while (&lt;$in&gt;) {<br />
    print $out $_;<br />
}<br />
close $out;</p>
<p> Within that basic form, add the parts that you need to insert, change, or delete lines. </p>
<p> To prepend lines to the beginning, print those lines before you enter the loop that prints the existing lines. </p>
<p>open my $in, &#8216;&lt;&#8216;, $file or die &#8220;Can&#8217;t read old file: $!&#8221;;<br />
open my $out, &#8216;&gt;&#8217;, &#8220;$file.new&#8221; or die &#8220;Can&#8217;t write new file: $!&#8221;;<br />
print $out &#8220;# Add this line to the top
&#8221;;<br />
# &lt;&#8211; &#8211; HERE&#8217;S THE MAGIC while (&lt;$in&gt;)<br />
{<br />
    print $out $_;<br />
}<br />
close $out;</p>
<p> To change existing lines, insert the code to modify the lines inside the <tt>&quot;while&quot;</tt> loop. In this case, the code finds all lowercased versions of &#8220;perl&#8221; and uppercases them. The happens for every line, so be sure that you&#8217;re supposed to do that on every line! </p>
<p>open my $in, &#8216;&lt;&#8216;, $file or die &#8220;Can&#8217;t read old file: $!&#8221;;<br />
open my $out, &#8216;&gt;&#8217;, &#8220;$file.new&#8221; or die &#8220;Can&#8217;t write new file: $!&#8221;;<br />
print $out &#8220;# Add this line to the top
&#8221;;<br />
while (&lt;$in&gt;) {<br />
    s /(perl) / Perl / g;<br />
    print $out $_;<br />
}<br />
close $out;</p>
<p> To change only a particular line, the input line number, <tt>$.</tt>, is useful. First read and print the lines up to the one you want to change. Next, read the single line you want to change, change it, and print it. After that, read the rest of the lines and print those: </p>
<p>while (&lt;$in&gt;) {<br />
#print the lines before the change<br />
        print $out $_;<br />
    last if $.== 4;<br />
#line number before change<br />
}<br />
my $line = &lt;$in&gt;;<br />
$line = ~s /(perl) / Perl / g;<br />
print $out $line;<br />
while (&lt;$in&gt;) {<br />
#print the rest of the lines<br />
        print $out $_;<br />
}</p>
<p> To skip lines, use the looping controls. The <tt>&quot;next&quot;</tt> in this example skips comment lines, and the <tt>&quot;last&quot;</tt> stops all processing once it encounters either <tt>&quot;__END__&quot;</tt> or <tt>&quot;__DATA__&quot;</tt>. </p>
<p>while (&lt;$in&gt;) {<br />
    next if / ^\s + # / ;<br />
#skip comment lines<br />
            last if /<br />
        ^__(END | DATA) __$ /<br />
        ;<br />
#stop at end of code marker<br />
        print $out $_;<br />
}</p>
<p> Do the same sort of thing to delete a particular line by using <tt>&quot;next&quot;</tt> to skip the lines you don&#8217;t want to show up in the output. This example skips every fifth line: </p>
<p>while (&lt;$in&gt;) {<br />
    next unless $.% 5;<br />
    print $out $_;<br />
}</p>
<p> If, for some odd reason, you really want to see the whole file at once rather than processing line-by-line, you can slurp it in (as long as you can fit the whole thing in memory!): </p>
<p>open my $in, &#8216;&lt;&#8216;, $file or die &#8220;Can&#8217;t read old file: $!&#8221; open my $out, &#8216;&gt;&#8217;, &#8220;$file.new&#8221; or die &#8220;Can&#8217;t write new file: $!&#8221;;<br />
my $content = do<br />
{<br />
    local $ / ;<br />
&lt;$in&gt;<br />
};<br />
#slurp !<br />
#do your magic here<br />
    print $out $content;</p>
<p> Modules such as Path::Tiny and Tie::File can help with that too. If you can, however, avoid reading the entire file at once. Perl won&#8217;t give that memory back to the operating system until the process finishes. </p>
<p> You can also use Perl one-liners to modify a file in-place. The following changes all &#8216;Fred&#8217; to &#8216;Barney&#8217; in <i>inFile.txt</i>, overwriting the file with the new contents. With the <tt>&quot;-p&quot;</tt> switch, Perl wraps a <tt>&quot;while&quot;</tt> loop around the code you specify with <tt>&quot;-e&quot;</tt>, and <tt>&quot;-i&quot;</tt> turns on in-place editing. The current line is in <tt>$_</tt>. With <tt>&quot;-p&quot;</tt>, Perl automatically prints the value of <tt>$_</tt> at the end of the loop. See perlrun for more details. </p>
<pre>
    perl -pi -e 's/Fred/Barney/' inFile.txt
</pre>
<p> To make a backup of <tt>&quot;inFile.txt&quot;</tt>, give <tt>&quot;-i&quot;</tt> a file extension to add: </p>
<pre>
    perl -pi.bak -e 's/Fred/Barney/' inFile.txt
</pre>
<p> To change only the fifth line, you can add a test checking <tt>$.</tt>, the input line number, then only perform the operation when the test passes: </p>
<pre>
    perl -pi -e 's/Fred/Barney/ if $. == 5' inFile.txt
</pre>
<p> To add lines before a certain line, you can add a line (or lines!) before Perl prints <tt>$_</tt>: </p>
<pre>
    perl -pi -e 'print &quot;Put before third line
&quot; if $. == 3' inFile.txt
</pre>
<p> You can even add a line to the beginning of a file, since the current line prints at the end of the loop: </p>
<pre>
    perl -pi -e 'print &quot;Put before first line
&quot; if $. == 1' inFile.txt
</pre>
<p> To insert a line after one already in the file, use the <tt>&quot;-n&quot;</tt> switch. It&#8217;s just like <tt>&quot;-p&quot;</tt> except that it doesn&#8217;t print <tt>$_</tt> at the end of the loop, so you have to do that yourself. In this case, print <tt>$_</tt> first, then print the line that you want to add. </p>
<pre>
    perl -ni -e 'print; print &quot;Put after fifth line
&quot; if $. == 5' inFile.txt
</pre>
<p> To delete lines, only print the ones that you want. </p>
<pre>
    perl -ni -e 'print if /d/' inFile.txt
</pre>
<h3>How do I count the number of lines in a file?</h3>
<p> (contributed by brian d foy) </p>
<p> Conceptually, the easiest way to count the lines in a file is to simply read them and count them: </p>
<p>my $count = 0;<br />
while (&lt;$fh&gt;) {<br />
    $count++;<br />
}</p>
<p> You don&#8217;t really have to count them yourself, though, since Perl already does that with the <tt>$.</tt> variable, which is the current line number from the last filehandle read: </p>
<p>1 while (&lt;$fh&gt;);<br />
my $count = $.;</p>
<p> If you want to use <tt>$.</tt>, you can reduce it to a simple one-liner, like one of these: </p>
<p>% perl &#8211; lne &#8216;} print $.; {&#8216; file % perl &#8211; lne &#8216;END { print $. }&#8217; file</p>
<p> Those can be rather inefficient though. If they aren&#8217;t fast enough for you, you might just read chunks of data and count the number of newlines: </p>
<p>my $lines = 0;<br />
open my($fh), &#8216;&lt;:raw&#8217;, $filename or die &#8220;Can&#8217;t open $filename: $!&#8221;;<br />
while (sysread $fh, $buffer, 4096) {<br />
        $lines += ( $buffer =~ tr/
// );<br />
}<br />
close $fh;</p>
<p> However, that doesn&#8217;t work if the line ending isn&#8217;t a newline. You might change that <tt>&quot;tr///&quot;</tt> to a <tt>&quot;s///&quot;</tt> so you can count the number of times the input record separator, <tt>$/</tt>, shows up: </p>
<p>my $lines = 0;<br />
open my($fh), &#8216;&lt;:raw&#8217;, $filename or die &#8220;Can&#8217;t open $filename: $!&#8221;;<br />
while (sysread $fh, $buffer, 4096) {<br />
    $lines += ($buffer = ~s | $ / || g;);<br />
}<br />
close $fh;</p>
<p> If you don&#8217;t mind shelling out, the <tt>&quot;wc&quot;</tt> command is usually the fastest, even with the extra interprocess overhead. Ensure that you have an untainted filename though: </p>
<p>#!perl &#8211; T<br />
$ENV{PATH} = undef;<br />
my $lines;<br />
if ($filename = ~ / ^([0 &#8211; 9a &#8211; z_.] +)\z /) {<br />
    $lines = `/ usr / bin / wc &#8211; l $1` chomp $lines;<br />
}</p>
<h3>How do I delete the last N lines from a file?</h3>
<p> (contributed by brian d foy) </p>
<p> The easiest conceptual solution is to count the lines in the file then start at the beginning and print the number of lines (minus the last N) to a new file. </p>
<p> Most often, the real question is how you can delete the last N lines without making more than one pass over the file, or how to do it without a lot of copying. The easy concept is the hard reality when you might have millions of lines in your file. </p>
<p> One trick is to use File::ReadBackwards, which starts at the end of the file. That module provides an object that wraps the real filehandle to make it easy for you to move around the file. Once you get to the spot you need, you can get the actual filehandle and work with it as normal. In this case, you get the file position at the end of the last line you want to keep and truncate the file to that point: </p>
<p>use File::ReadBackwards;<br />
my $filename = &#8216;test.txt&#8217;;<br />
my $Lines_to_truncate = 2;<br />
my $bw = File::ReadBackwards-&gt;new ($filename) or die &#8220;Could not read backwards in [$filename]: $!&#8221;;<br />
my $lines_from_end = 0;<br />
until($bw-&gt;eof or $lines_from_end == $Lines_to_truncate)<br />
{<br />
    print &#8220;Got: &#8220;, $bw-&gt;readline;<br />
    $lines_from_end++;<br />
}<br />
truncate($filename, $bw-&gt;tell);</p>
<p> The File::ReadBackwards module also has the advantage of setting the input record separator to a regular expression. </p>
<p> You can also use the Tie::File module which lets you access the lines through a tied array. You can use normal array operations to modify your file, including setting the last index and using <tt>&quot;splice&quot;</tt>.</p>
<h3>How can I use Perl&#8217;s -i option from within a program?</h3>
<p> <tt>&quot;-i&quot;</tt> sets the value of Perl&#8217;s <tt>$^I</tt> variable, which in turn affects the behavior of <tt>&quot;&lt;&gt;&quot;</tt>; see perlrun for more details. By modifying the appropriate variables directly, you can get the same behavior within a larger program. For example: </p>
<p>#&#8230;<br />
{<br />
    local($ ^ I, @ARGV) = (&#8216;.orig&#8217;, glob(&#8220;*.c&#8221;));<br />
    while (&lt;&gt;) {<br />
        if ($.== 1) {<br />
            print &#8220;This line should appear at the top of each file
&#8221;;<br />
        }<br />
        s /(p) earl / ${1} erl / i;<br />
#Correct typos, preserving case print;<br />
        close ARGV if eof;<br />
#Reset $.<br />
    }<br />
}<br />
#$ ^ I and@ARGV return to their old values here</p>
<p> This block modifies all the <tt>&quot;.c&quot;</tt> files in the current directory, leaving a backup of the original data from each file in a new <tt>&quot;.c.orig&quot;</tt> file.</p>
<h3>How can I copy a file?</h3>
<p> (contributed by brian d foy) </p>
<p> Use the File::Copy module. It comes with Perl and can do a true copy across file systems, and it does its magic in a portable fashion. </p>
<pre>
    use File::Copy;
    copy( $original, $new_copy ) or die &quot;Copy failed: $!&quot;;
</pre>
<p> If you can&#8217;t use File::Copy, you&#8217;ll have to do the work yourself: open the original file, open the destination file, then print to the destination file as you read the original. You also have to remember to copy the permissions, owner, and group to the new file.</p>
<h3>How do I make a temporary file name?</h3>
<p> If you don&#8217;t need to know the name of the file, you can use <tt>&quot;open()&quot;</tt> with <tt>&quot;undef&quot;</tt> in place of the file name. In Perl 5.8 or later, the <tt>&quot;open()&quot;</tt> function creates an anonymous temporary file: </p>
<pre>
    open my $tmp, '+&gt;', undef or die $!;
</pre>
<p> Otherwise, you can use the File::Temp module. </p>
<p>use File::Temp qw / tempfile tempdir / ;<br />
my $dir = tempdir(CLEANUP = &gt; 1);<br />
($fh, $filename) = tempfile(DIR = &gt; $dir);<br />
# or if you don&#8217;t need to know the filename<br />
my $fh = tempfile(DIR = &gt; $dir);</p>
<p> The File::Temp has been a standard module since Perl 5.6.1. If you don&#8217;t have a modern enough Perl installed, use the <tt>&quot;new_tmpfile&quot;</tt> class method from the IO::File module to get a filehandle opened for reading and writing. Use it if you don&#8217;t need to know the file&#8217;s name: </p>
<pre>
    use IO::File;
    my $fh = IO::File-&gt;new_tmpfile()
        or die &quot;Unable to make new temporary file: $!&quot;;
</pre>
<p> If you&#8217;re committed to creating a temporary file by hand, use the process <font SIZE="-1">ID</font> and/or the current time-value. If you need to have many temporary files in one process, use a counter: </p>
<p>BEGIN<br />
{<br />
    use Fcntl;<br />
    use File::Spec;<br />
    my $temp_dir = File::Spec-&gt;tmpdir();<br />
    my $file_base = sprintf &#8220;%d-%d-0000&#8221;, $$, time;<br />
    my $base_name = File::Spec-&gt;catfile($temp_dir, $file_base);<br />
    sub temp_file<br />
    {<br />
        my $fh;<br />
        my $count = 0;<br />
        until(defined(fileno($fh)) || $count++ &gt; 100)<br />
        {<br />
            $base_name = ~s / -(\d +) $ / &#8220;-&#8220;.(1 + $1) / e;<br />
#O_EXCL is required for security reasons.<br />
            sysopen $fh, $base_name, O_WRONLY | O_EXCL | O_CREAT;<br />
        }<br />
        if (defined fileno($fh)) {<br />
            return ($fh, $base_name);<br />
        } else {<br />
            return ();<br />
        }<br />
    }<br />
}</p>
<h3>How can I manipulate fixed-record-length files?</h3>
<p> The most efficient way is using <code>pack()</code> and <code>unpack()</code>. This is faster than using <code>substr()</code> when taking many, many strings. It is slower for just a few. </p>
<p> Here is a sample chunk of code to break up and put back together again some fixed-format input lines, in this case from the output of a normal, Berkeley-style ps: </p>
<p>#sample input line:<br />
# 15158 p5 T 0 : 00 perl / home / tchrist / scripts / now &#8211; what<br />
my $PS_T = &#8216;A6 A4 A7 A5 A*&#8217;;<br />
open my $ps, &#8216;-|&#8217;, &#8216;ps&#8217;;<br />
print scalar&lt;$ps&gt;;<br />
my @fields = qw(pid tt stat time command);<br />
while (&lt;$ps&gt;) {<br />
    my % process;<br />
    @process<br />
    {<br />
        @fields<br />
    }<br />
    = unpack($PS_T, $_);<br />
        for<br />
            my $field(@fields)<br />
            {<br />
                print &#8220;$field: &lt;$process{$field}&gt;
&#8221;;<br />
            }<br />
        print &#8216;line=&#8217;, pack(<br />
                           $PS_T, @process { @fields }),<br />
            &#8220;
&#8221;;<br />
}</p>
<p> We&#8217;ve used a hash slice in order to easily handle the fields of each row. Storing the keys in an array makes it easy to operate on them as a group or loop over them with <tt>&quot;for&quot;</tt>. It also avoids polluting the program with global variables and using symbolic references.</p>
<h3>How can I make a filehandle local to a subroutine? How do I pass filehandles between subroutines? How do I make an array of filehandles?</h3>
<p> As of perl5.6, <code>open()</code> autovivifies file and directory handles as references if you pass it an uninitialized scalar variable. You can then pass these references just like any other scalar, and use them in the place of named handles. </p>
<p>open my $fh, $file_name;<br />
open local $fh, $file_name;<br />
print $fh &#8220;Hello World!
&#8221;;<br />
process_file($fh);</p>
<p> If you like, you can store these filehandles in an array or a hash. If you access them directly, they aren&#8217;t simple scalars and you need to give <tt>&quot;print&quot;</tt> a little help by placing the filehandle reference in braces. Perl can only figure it out on its own when the filehandle reference is a simple scalar. </p>
<p>my @fhs = ($fh1, $fh2, $fh3);<br />
for ($i = 0; $i &lt;= $ #fhs; $i++) {<br />
    print<br />
    {<br />
        $fhs[$i]<br />
    }<br />
    &#8220;just another Perl answer, 
&#8221;;<br />
}</p>
<p> Before perl5.6, you had to deal with various typeglob idioms which you may see in older code. </p>
<p>open FILE, &#8220;&gt; $filename&#8221;;<br />
process_typeglob(*FILE);<br />
process_reference( \*FILE);<br />
sub process_typeglob<br />
{<br />
    local *FH = shift;<br />
    print FH &#8220;Typeglob!&#8221;<br />
}<br />
sub process_reference<br />
{<br />
    local $fh = shift;<br />
    print $fh &#8220;Reference!&#8221;<br />
}</p>
<p> If you want to create many anonymous handles, you should check out the Symbol or IO::Handle modules.</p>
<h3>How can I use a filehandle indirectly?</h3>
<p> An indirect filehandle is the use of something other than a symbol in a place that a filehandle is expected. Here are ways to get indirect filehandles: </p>
<p>$fh = SOME_FH;<br />
#bareword is strict &#8211; subs hostile<br />
                          $fh = &#8220;SOME_FH&#8221;;<br />
#strict &#8211; refs hostile;<br />
same package only<br />
    $fh = *SOME_FH;<br />
#typeglob $fh = \* SOME_FH;<br />
#ref to typeglob(bless &#8211; able)<br />
    $fh = *SOME_FH{IO };<br />
#blessed IO::Handle from *SOME_FH typeglob</p>
<p> Or, you can use the <tt>&quot;new&quot;</tt> method from one of the IO::* modules to create an anonymous filehandle and store that in a scalar variable. </p>
<p>use IO::Handle;<br />
# 5.004 or higher my $fh = IO::Handle-&gt;new ();</p>
<p> Then use any of those as you would a normal filehandle. Anywhere that Perl is expecting a filehandle, an indirect filehandle may be used instead. An indirect filehandle is just a scalar variable that contains a filehandle. Functions like <tt>&quot;print&quot;</tt>, <tt>&quot;open&quot;</tt>, <tt>&quot;seek&quot;</tt>, or the <tt>&quot;&lt;FH&gt;&quot;</tt> diamond operator will accept either a named filehandle or a scalar variable containing one: </p>
<p>($ifh, $ofh, $efh) = (*STDIN, *STDOUT, *STDERR);<br />
print $ofh &#8220;Type it: &#8220;;<br />
my $got = &lt;$ifh&gt;<br />
    print $efh &#8220;What was that: $got&#8221;;</p>
<p> If you&#8217;re passing a filehandle to a function, you can write the function in two ways: </p>
<p>sub accept_fh<br />
{<br />
    my $fh = shift;<br />
    print $fh &#8220;Sending to indirect filehandle
&#8221;;<br />
}</p>
<p> Or it can localize a typeglob and use the filehandle directly: </p>
<p>sub accept_fh<br />
{<br />
    local *FH = shift;<br />
    print FH &#8220;Sending to localized filehandle
&#8221;;<br />
}</p>
<p> Both styles work with either objects or typeglobs of real filehandles. (They might also work with strings under some circumstances, but this is risky.) </p>
<p>accept_fh(*STDOUT);<br />
accept_fh($handle);</p>
<p> In the examples above, we assigned the filehandle to a scalar variable before using it. That is because only simple scalar variables, not expressions or subscripts of hashes or arrays, can be used with built-ins like <tt>&quot;print&quot;</tt>, <tt>&quot;printf&quot;</tt>, or the diamond operator. Using something other than a simple scalar variable as a filehandle is illegal and won&#8217;t even compile: </p>
<p>my @fd = (*STDIN, *STDOUT, *STDERR);<br />
print $fd[1] &#8220;Type it: &#8220;;<br />
#WRONG my $got = &lt; $fd[0]&gt; #WRONG print $fd[2] &#8220;What was that: $got&#8221;;<br />
#WRONG</p>
<p> With <tt>&quot;print&quot;</tt> and <tt>&quot;printf&quot;</tt>, you get around this by using a block and an expression where you would place the filehandle: </p>
<p>print<br />
{<br />
    $fd[1]<br />
}<br />
&#8220;funny stuff
&#8221;;<br />
printf<br />
{<br />
    $fd[1]<br />
}<br />
&#8220;Pity the poor %x.
&#8221;, 3_735_928_559;<br />
#Pity the poor deadbeef.</p>
<p> That block is a proper block like any other, so you can put more complicated code there. This sends the message out to one of two places: </p>
<p>my $ok = -x &#8220;/bin/cat&#8221;;<br />
print<br />
{<br />
    $ok ? $fd[1] : $fd[2]<br />
}<br />
&#8220;cat stat $ok
&#8221;;<br />
print<br />
{<br />
    $fd[1 + ($ok || 0)]<br />
}<br />
&#8220;cat stat $ok
&#8221;;</p>
<p> This approach of treating <tt>&quot;print&quot;</tt> and <tt>&quot;printf&quot;</tt> like object methods calls doesn&#8217;t work for the diamond operator. That&#8217;s because it&#8217;s a real operator, not just a function with a comma-less argument. Assuming you&#8217;ve been storing typeglobs in your structure as we did above, you can use the built-in function named <tt>&quot;readline&quot;</tt> to read a record just as <tt>&quot;&lt;&gt;&quot;</tt> does. Given the initialization shown above for <tt>@fd</tt>, this would work, but only because <code>readline()</code> requires a typeglob. It doesn&#8217;t work with objects or strings, which might be a bug we haven&#8217;t fixed yet. </p>
<pre>
    $got = readline($fd[0]);
</pre>
<p> Let it be noted that the flakiness of indirect filehandles is not related to whether they&#8217;re strings, typeglobs, objects, or anything else. It&#8217;s the syntax of the fundamental operators. Playing the object game doesn&#8217;t help you at all here.</p>
<h3>How can I open a filehandle to a string?</h3>
<p> (contributed by Peter J. Holzer, hjp-usenet2 [at] hjp.at) </p>
<p> Since Perl 5.8.0 a file handle referring to a string can be created by calling open with a reference to that string instead of the filename. This file handle can then be used to read from or write to the string: </p>
<p>open(my $fh, &#8216;&gt;&#8217;, \$string) or die &#8220;Could not open string for writing&#8221;;<br />
print $fh &#8220;foo
&#8221;;<br />
print $fh &#8220;bar
&#8221;;<br />
#$string now contains &#8220;foo
bar
&#8221; open(my $fh, &#8216;&lt;&#8216;, \$string) or die &#8220;Could not open string for reading&#8221;;<br />
my $x = &lt;$fh&gt;;<br />
#$x now contains &#8220;foo
&#8221;</p>
<p> With older versions of Perl, the IO::String module provides similar functionality.</p>
<h3>How can I set up a footer format to be used with <code>write()</code>?</h3>
<p> There&#8217;s no builtin way to do this, but perlform has a couple of techniques to make it possible for the intrepid hacker.</p>
<h3>How can I <code>write()</code> into a string?</h3>
<p> (contributed by brian d foy) </p>
<p> If you want to <tt>&quot;write&quot;</tt> into a string, you just have to &lt;open&gt; a filehandle to a string, which Perl has been able to do since Perl 5.6: </p>
<p>open FH, &#8216;&gt;&#8217;, \my $string;<br />
write(FH);</p>
<p> Since you want to be a good programmer, you probably want to use a lexical filehandle, even though formats are designed to work with bareword filehandles since the default format names take the filehandle name. However, you can control this with some Perl special per-filehandle variables: <tt>$^</tt>, which names the top-of-page format, and <tt>$~</tt> which shows the line format. You have to change the default filehandle to set these variables: </p>
<p>open my($fh), &#8216;&gt;&#8217;, \my $string;<br />
{<br />
#set per &#8211; filehandle variables<br />
                   my $old_fh = select($fh);<br />
    $ ~ = &#8216;ANIMAL&#8217;;<br />
    $ ^ = &#8216;ANIMAL_TOP&#8217;;<br />
    select($old_fh);<br />
}<br />
format ANIMAL_TOP =<br />
    ID Type Name<br />
        .format ANIMAL =<br />
        @##@ &lt; &lt; &lt; @ &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt; &lt;<br />
        $id,<br />
       $type, $name.</p>
<p> Although write can work with lexical or package variables, whatever variables you use have to scope in the format. That most likely means you&#8217;ll want to localize some package variables: </p>
<p>{<br />
    local($id, $type, $name) = qw(12 cat Buster);<br />
    write($fh);<br />
}<br />
print $string;</p>
<p> There are also some tricks that you can play with <tt>&quot;formline&quot;</tt> and the accumulator variable <tt>$^A</tt>, but you lose a lot of the value of formats since <tt>&quot;formline&quot;</tt> won&#8217;t handle paging and so on. You end up reimplementing formats when you use them.</p>
<h3>How can I output my numbers with commas added?</h3>
<p> (contributed by brian d foy and Benjamin Goldberg) </p>
<p> You can use Number::Format to separate places in a number. It handles locale information for those of you who want to insert full stops instead (or anything else that they want to use, really). </p>
<p> This subroutine will add commas to your number: </p>
<p>sub commify<br />
{<br />
    local $_ = shift;<br />
        1 while s/^([-+]?\d+)(\d{3})/$1,$2/;<br />
        return $_;<br />
}</p>
<p> This regex from Benjamin Goldberg will add commas to numbers: </p>
<pre>
    s/(^[-+]?\d+?(?=(?&gt;(?:\d{3})+)(?!\d))|\G\d{3}(?=\d))/$1,/g;
</pre>
<p> It is easier to see with comments: </p>
<p>    s/(<br />
        ^[-+]?             # beginning of number.<br />
        \d+?               # first digits before first comma<br />
        (?=                # followed by, (but not included in the match) :<br />
            (?&gt;(?:\d{3})+) # some positive multiple of three digits.<br />
            (?!\d)         # an *exact* multiple, not x * 3 + 1 or whatever.<br />
        )<br />
        |                  # or:<br />
        \G\d{3}            # after the last group, get three digits<br />
        (?=\d)             # but they have to have more digits after them.<br />
    )/$1,/xg;</p>
<h3>How can I translate tildes (~) in a filename?</h3>
<p> Use the &lt;&gt; (<tt>&quot;glob()&quot;</tt>) operator, documented in perlfunc. Versions of Perl older than 5.6 require that you have a shell installed that groks tildes. Later versions of Perl have this feature built in. The File::KGlob module (available from <font SIZE="-1">CPAN</font>) gives more portable glob functionality. </p>
<p> Within Perl, you may use this directly: </p>
<p>$filename = ~s{<br />
    ^~#find a leading tilde(#save this in $1<br />
                                    [^ / ] #a non &#8211;<br />
                                slash character * #repeated 0 or<br />
                            more times(0 means me))} {$1 ? (getpwnam($1))[7] : ($ENV{HOME} || $ENV{LOGDIR})} ex;</p>
<h3>How come when I open a file read-write it wipes it out?</h3>
<p> Because you&#8217;re using something like this, which truncates the file <i>then</i> gives you read-write access: </p>
<pre>
    open my $fh, '+&gt;', '/path/name'; # WRONG (almost always)
</pre>
<p> Whoops. You should instead use this, which will fail if the file doesn&#8217;t exist: </p>
<pre>
    open my $fh, '+&lt;', '/path/name'; # open for update
</pre>
<p> Using &#8220;&gt;&#8221; always clobbers or creates. Using &#8220;&lt;&#8221; never does either. The &#8220;+&#8221; doesn&#8217;t change this. </p>
<p> Here are examples of many kinds of file opens. Those using <tt>&quot;sysopen&quot;</tt> all assume that you&#8217;ve pulled in the constants from Fcntl: </p>
<pre>
    use Fcntl;
</pre>
<p> To open file for reading: </p>
<pre>
    open my $fh, '&lt;', $path                               or die $!;
    sysopen my $fh, $path, O_RDONLY                       or die $!;
</pre>
<p> To open file for writing, create new file if needed or else truncate old file: </p>
<pre>
    open my $fh, '&gt;', $path                               or die $!;
    sysopen my $fh, $path, O_WRONLY|O_TRUNC|O_CREAT       or die $!;
    sysopen my $fh, $path, O_WRONLY|O_TRUNC|O_CREAT, 0666 or die $!;
</pre>
<p> To open file for writing, create new file, file must not exist: </p>
<pre>
    sysopen my $fh, $path, O_WRONLY|O_EXCL|O_CREAT        or die $!;
    sysopen my $fh, $path, O_WRONLY|O_EXCL|O_CREAT, 0666  or die $!;
</pre>
<p> To open file for appending, create if necessary: </p>
<pre>
    open my $fh, '&gt;&gt;', $path                              or die $!;
    sysopen my $fh, $path, O_WRONLY|O_APPEND|O_CREAT      or die $!;
    sysopen my $fh, $path, O_WRONLY|O_APPEND|O_CREAT, 0666 or die $!;
</pre>
<p> To open file for appending, file must exist: </p>
<pre>
    sysopen my $fh, $path, O_WRONLY|O_APPEND              or die $!;
</pre>
<p> To open file for update, file must exist: </p>
<pre>
    open my $fh, '+&lt;', $path                              or die $!;
    sysopen my $fh, $path, O_RDWR                         or die $!;
</pre>
<p> To open file for update, create file if necessary: </p>
<pre>
    sysopen my $fh, $path, O_RDWR|O_CREAT                 or die $!;
    sysopen my $fh, $path, O_RDWR|O_CREAT, 0666           or die $!;
</pre>
<p> To open file for update, file must not exist: </p>
<pre>
    sysopen my $fh, $path, O_RDWR|O_EXCL|O_CREAT          or die $!;
    sysopen my $fh, $path, O_RDWR|O_EXCL|O_CREAT, 0666    or die $!;
</pre>
<p> To open a file without blocking, creating if necessary: </p>
<pre>
    sysopen my $fh, '/foo/somefile', O_WRONLY|O_NDELAY|O_CREAT
        or die &quot;can't open /foo/somefile: $!&quot;:
</pre>
<p> Be warned that neither creation nor deletion of files is guaranteed to be an atomic operation over <font SIZE="-1">NFS.</font> That is, two processes might both successfully create or unlink the same file! Therefore O_EXCL isn&#8217;t as exclusive as you might wish. </p>
<p> See also perlopentut.</p>
<h3>Why do I sometimes get an Argument list too long when I use &lt;*&gt;?</h3>
<p> The <tt>&quot;&lt;&gt;&quot;</tt> operator performs a globbing operation (see above). In Perl versions earlier than v5.6.0, the internal <code>glob()</code> operator forks <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1) to do the actual glob expansion, but csh can&#8217;t handle more than 127 items and so gives the error message <tt>&quot;Argument list too long&quot;</tt>. People who installed tcsh as csh won&#8217;t have this problem, but their users may be surprised by it. </p>
<p> To get around this, either upgrade to Perl v5.6.0 or later, do the glob yourself with <code>readdir()</code> and patterns, or use a module like File::Glob, one that doesn&#8217;t use the shell to do globbing.</p>
<h3>How can I open a file named with a leading &gt; or trailing blanks?</h3>
<p> (contributed by Brian McCauley) </p>
<p> The special two-argument form of Perl&#8217;s <code>open()</code> function ignores trailing blanks in filenames and infers the mode from certain leading characters (or a trailing &#8220;|&#8221;). In older versions of Perl this was the only version of <code>open()</code> and so it is prevalent in old code and books. </p>
<p> Unless you have a particular reason to use the two-argument form you should use the three-argument form of <code>open()</code> which does not treat any characters in the filename as special. </p>
<pre>
    open my $fh, &quot;&lt;&quot;, &quot;  file  &quot;;  # filename is &quot;   file   &quot;
    open my $fh, &quot;&gt;&quot;, &quot;&gt;file&quot;;     # filename is &quot;&gt;file&quot;
</pre>
<h3>How can I reliably rename a file?</h3>
<p> If your operating system supports a proper <code><a href="/docs/linux/man/1-mv/">mv</a></code>(1) utility or its functional equivalent, this works: </p>
<pre>
    rename($old, $new) or system(&quot;mv&quot;, $old, $new);
</pre>
<p> It may be more portable to use the File::Copy module instead. You just copy to the new file to the new name (checking return values), then delete the old one. This isn&#8217;t really the same semantically as a <tt>&quot;rename()&quot;</tt>, which preserves meta-information like permissions, timestamps, inode info, etc.</p>
<h3>How can I lock a file?</h3>
<p> Perl&#8217;s builtin <code>flock()</code> function (see perlfunc for details) will call <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) if that exists, <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) if it doesn&#8217;t (on perl version 5.004 and later), and <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3) if neither of the two previous system calls exists. On some systems, it may even use a different form of native locking. Here are some gotchas with Perl&#8217;s <code>flock()</code>:</p>
<dl>
<dt>1.</p>
<dd> Produces a fatal error if none of the three system calls (or their close equivalent) exists.</p>
<dt>2.</p>
<dd> <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3) does not provide shared locking, and requires that the filehandle be open for writing (or appending, or read/writing).</p>
<dt>3.</p>
<dd> Some versions of <code>flock()</code> can&#8217;t lock files over a network (e.g. on <font SIZE="-1">NFS</font> file systems), so you&#8217;d need to force the use of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) when you build Perl. But even this is dubious at best. See the flock entry of perlfunc and the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file in the source distribution for information on building Perl to do this. </p>
<p> Two potentially non-obvious but traditional flock semantics are that it waits indefinitely until the lock is granted, and that its locks are <i>merely advisory</i>. Such discretionary locks are more flexible, but offer fewer guarantees. This means that files locked with <code>flock()</code> may be modified by programs that do not also use <code>flock()</code>. Cars that stop for red lights get on well with each other, but not with cars that don&#8217;t stop for red lights. See the perlport manpage, your port&#8217;s specific documentation, or your system-specific local manpages for details. It&#8217;s best to assume traditional behavior if you&#8217;re writing portable programs. (If you&#8217;re not, you should as always feel perfectly free to write for your own system&#8217;s idiosyncrasies (sometimes called &#8220;features&#8221;). Slavish adherence to portability concerns shouldn&#8217;t get in the way of your getting your job done.) </p>
<p> For more information on file locking, see also &#8220;File Locking&#8221; in perlopentut if you have it (new for 5.6).</dl>
<h3>Why can&#8217;t I just open(<font SIZE="-1">FH, </font>&gt;file.lock)?</h3>
<p> A common bit of code <font SIZE="-1"><code>NOT TO USE</code></font> is this: </p>
<p>sleep(3) while &#8211; e &#8216;file.lock&#8217;;<br />
#PLEASE DO NOT USE<br />
    open my $lock,<br />
    &#8216;&gt;&#8217;, &#8216;file.lock&#8217;;<br />
#THIS BROKEN CODE</p>
<p> This is a classic race condition: you take two steps to do something which must be done in one. That&#8217;s why computer hardware provides an atomic test-and-set instruction. In theory, this &#8220;ought&#8221; to work: </p>
<pre>
    sysopen my $fh, &quot;file.lock&quot;, O_WRONLY|O_EXCL|O_CREAT
        or die &quot;can't open  file.lock: $!&quot;;
</pre>
<p> except that lamentably, file creation (and deletion) is not atomic over <font SIZE="-1">NFS,</font> so this won&#8217;t work (at least, not every time) over the net. Various schemes involving <code>link()</code> have been suggested, but these tend to involve busy-wait, which is also less than desirable.</p>
<h3>I still don&#8217;t get locking. I just want to increment the number in the file. How can I do this?</h3>
<p> Didn&#8217;t anyone ever tell you web-page hit counters were useless? They don&#8217;t count number of hits, they&#8217;re a waste of time, and they serve only to stroke the writer&#8217;s vanity. It&#8217;s better to pick a random number; they&#8217;re more realistic. </p>
<p> Anyway, this is what you can do if you can&#8217;t help yourself. </p>
<p>use Fcntl qw(<br />
    : DEFAULT<br />
    : flock);<br />
sysopen my $fh, &#8220;numfile&#8221;, O_RDWR | O_CREAT or die &#8220;can&#8217;t open numfile: $!&#8221;;<br />
flock $fh, LOCK_EX or die &#8220;can&#8217;t flock numfile: $!&#8221;;<br />
my $num = &lt;$fh&gt; || 0;<br />
seek $fh, 0, 0 or die &#8220;can&#8217;t rewind numfile: $!&#8221;;<br />
truncate $fh, 0 or die &#8220;can&#8217;t truncate numfile: $!&#8221;;<br />
(print $fh $num + 1, &#8220;
&#8221;) or die &#8220;can&#8217;t write numfile: $!&#8221;;<br />
close $fh or die &#8220;can&#8217;t close numfile: $!&#8221;;</p>
<p> Here&#8217;s a much better web-page hit counter: </p>
<pre>
    $hits = int( (time() - 850_000_000) / rand(1_000) );
</pre>
<p> If the count doesn&#8217;t impress your friends, then the code might. :-)</p>
<h3>All I want to do is append a small amount of text to the end of a file. Do I still have to use locking?</h3>
<p> If you are on a system that correctly implements <tt>&quot;flock&quot;</tt> and you use the example appending code from &#8220;perldoc -f flock&#8221; everything will be <font SIZE="-1">OK</font> even if the <font SIZE="-1">OS</font> you are on doesn&#8217;t implement append mode correctly (if such a system exists). So if you are happy to restrict yourself to OSs that implement <tt>&quot;flock&quot;</tt> (and that&#8217;s not really much of a restriction) then that is what you should do. </p>
<p> If you know you are only going to use a system that does correctly implement appending (i.e. not Win32) then you can omit the <tt>&quot;seek&quot;</tt> from the code in the previous answer. </p>
<p> If you know you are only writing code to run on an <font SIZE="-1">OS</font> and filesystem that does implement append mode correctly (a local filesystem on a modern Unix for example), and you keep the file in block-buffered mode and you write less than one buffer-full of output between each manual flushing of the buffer then each bufferload is almost guaranteed to be written to the end of the file in one chunk without getting intermingled with anyone else&#8217;s output. You can also use the <tt>&quot;syswrite&quot;</tt> function which is simply a wrapper around your system&#8217;s <tt><a href="/docs/linux/man/2-write/">write</a>(2)</tt> system call. </p>
<p> There is still a small theoretical chance that a signal will interrupt the system-level <tt>&quot;write()&quot;</tt> operation before completion. There is also a possibility that some <font SIZE="-1">STDIO</font> implementations may call multiple system level <tt>&quot;write()&quot;</tt>s even if the buffer was empty to start. There may be some systems where this probability is reduced to zero, and this is not a concern when using <tt>&quot;:perlio&quot;</tt> instead of your system&#8217;s <font SIZE="-1">STDIO.</font></p>
<h3>How do I randomly update a binary file?</h3>
<p> If you&#8217;re just trying to patch a binary, in many cases something as simple as this works: </p>
<p>perl &#8211; i &#8211; pe &#8216;s{window manager}{window mangler}g&#8217; / usr / bin / emacs</p>
<p> However, if you have fixed sized records, then you might do something more like this: </p>
<p>my $RECSIZE = 220;<br />
#size of record, in bytes<br />
                     my $recno = 37;<br />
#which record to update<br />
    open my $fh,<br />
    &#8216;+&lt;&#8216;, &#8216;somewhere&#8217; or die &#8220;can&#8217;t update somewhere: $!&#8221;;<br />
seek $fh, $recno *$RECSIZE, 0;<br />
read $fh, $record, $RECSIZE == $RECSIZE or die &#8220;can&#8217;t read record $recno: $!&#8221;;<br />
#munge the record<br />
seek $fh, -$RECSIZE, 1;<br />
print $fh $record;<br />
close $fh;</p>
<p> Locking and error checking are left as an exercise for the reader. Don&#8217;t forget them or you&#8217;ll be quite sorry.</p>
<h3>How do I get a file&#8217;s timestamp in perl?</h3>
<p> If you want to retrieve the time at which the file was last read, written, or had its meta-data (owner, etc) changed, you use the <code>-A</code>, <code>-M</code>, or <code>-C</code> file test operations as documented in perlfunc. These retrieve the age of the file (measured against the start-time of your program) in days as a floating point number. Some platforms may not have all of these times. See perlport for details. To retrieve the &#8220;raw&#8221; time in seconds since the epoch, you would call the stat function, then use <tt>&quot;localtime()&quot;</tt>, <tt>&quot;gmtime()&quot;</tt>, or <tt>&quot;POSIX::strftime()&quot;</tt> to convert this into human-readable form. </p>
<p> Here&#8217;s an example: </p>
<p>my $write_secs = (stat($file))[9];<br />
printf &#8220;file %s updated at %s
&#8221;, $file,<br />
    scalar localtime($write_secs);</p>
<p> If you prefer something more legible, use the File::stat module (part of the standard distribution in version 5.004 and later): </p>
<p>#error checking left as an exercise for reader.<br />
use File::stat;<br />
use Time::localtime;<br />
my $date_string = ctime(stat($file)-&gt;mtime);<br />
print &#8220;file $file updated at $date_string
&#8221;;</p>
<p> The <code>POSIX::strftime()</code> approach has the benefit of being, in theory, independent of the current locale. See perllocale for details.</p>
<h3>How do I set a file&#8217;s timestamp in perl?</h3>
<p> You use the <code>utime()</code> function documented in &#8220;utime&#8221; in perlfunc. By way of example, here&#8217;s a little program that copies the read and write times from its first argument to all the rest of them. </p>
<p>if (@ARGV &lt; 2) {<br />
    die &#8220;usage: cptimes timestamp_file other_files &#8230;
&#8221;;<br />
}<br />
my $timestamp = shift;<br />
my($atime, $mtime) = (stat($timestamp))[8, 9];<br />
utime $atime, $mtime, @ARGV;</p>
<p> Error checking is, as usual, left as an exercise for the reader. </p>
<p> The perldoc for utime also has an example that has the same effect as <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) on files that <i>already exist</i>. </p>
<p> Certain file systems have a limited ability to store the times on a file at the expected level of precision. For example, the <font SIZE="-1">FAT</font> and <font SIZE="-1">HPFS</font> filesystem are unable to create dates on files with a finer granularity than two seconds. This is a limitation of the filesystems, not of <code>utime()</code>.</p>
<h3>How do I print to more than one file at once?</h3>
<p> To connect one filehandle to several output filehandles, you can use the IO::Tee or Tie::FileHandle::Multiplex modules. </p>
<p> If you only have to do this once, you can print individually to each filehandle. </p>
<pre>
    for my $fh ($fh1, $fh2, $fh3) { print $fh &quot;whatever
&quot; }
</pre>
<h3>How can I read in an entire file all at once?</h3>
<p> The customary Perl approach for processing all the lines in a file is to do so one line at a time: </p>
<p>open my $input, &#8216;&lt;&#8216;, $file or die &#8220;can&#8217;t open $file: $!&#8221;;<br />
while (&lt;$input&gt;) {<br />
    chomp;<br />
#do something with $_<br />
}<br />
close $input or die &#8220;can&#8217;t close $file: $!&#8221;;</p>
<p> This is tremendously more efficient than reading the entire file into memory as an array of lines and then processing it one element at a time, which is often&#8212;if not almost always&#8212;the wrong approach. Whenever you see someone do this: </p>
<pre>
    my @lines = &lt;INPUT&gt;;
</pre>
<p> You should think long and hard about why you need everything loaded at once. It&#8217;s just not a scalable solution. </p>
<p> If you &#8220;mmap&#8221; the file with the File::Map module from <font SIZE="-1">CPAN,</font> you can virtually load the entire file into a string without actually storing it in memory: </p>
<p>use File::Map qw(map_file);<br />
map_file my $string, $filename;</p>
<p> Once mapped, you can treat <tt>$string</tt> as you would any other string. Since you don&#8217;t necessarily have to load the data, mmap-ing can be very fast and may not increase your memory footprint. </p>
<p> You might also find it more fun to use the standard Tie::File module, or the DB_File module&#8217;s <tt>$DB_RECNO</tt> bindings, which allow you to tie an array to a file so that accessing an element of the array actually accesses the corresponding line in the file. </p>
<p> If you want to load the entire file, you can use the Path::Tiny module to do it in one simple and efficient step: </p>
<p>use Path::Tiny;<br />
my $all_of_it = path($filename)-&gt;slurp;<br />
#entire file in scalar<br />
    my @all_lines = path($filename)-&gt;lines;<br />
#one line per element</p>
<p> Or you can read the entire file contents into a scalar like this: </p>
<p>my $var;<br />
{<br />
    local $ / ;<br />
    open my $fh, &#8216;&lt;&#8216;, $file or die &#8220;can&#8217;t open $file: $!&#8221;;<br />
    $var = &lt;$fh&gt;;<br />
}</p>
<p> That temporarily undefs your record separator, and will automatically close the file at block exit. If the file is already open, just use this: </p>
<p>my $var = do<br />
{<br />
    local $ / ;<br />
&lt;$fh&gt;<br />
};</p>
<p> You can also use a localized <tt>@ARGV</tt> to eliminate the <tt>&quot;open&quot;</tt>: </p>
<p>my $var = do<br />
{<br />
    local(@ARGV, $ /) = $file;<br />
&lt;&gt;<br />
};</p>
<p> For ordinary files you can also use the <tt>&quot;read&quot;</tt> function. </p>
<pre>
    read( $fh, $var, -s $fh );
</pre>
<p> That third argument tests the byte size of the data on the <tt>$fh</tt> filehandle and reads that many bytes into the buffer <tt>$var</tt>.</p>
<h3>How can I read in a file by paragraphs?</h3>
<p> Use the <tt>$/</tt> variable (see perlvar for details). You can either set it to <tt>&quot;&quot;</tt> to eliminate empty paragraphs (<tt>&quot;abc



def&quot;</tt>, for instance, gets treated as two paragraphs and not three), or <tt>&quot;

&quot;</tt> to accept empty paragraphs. </p>
<p> Note that a blank line must have no blanks in it. Thus <tt>&quot;fred
 
stuff

&quot;</tt> is one paragraph, but <tt>&quot;fred

stuff

&quot;</tt> is two.</p>
<h3>How can I read a single character from a file? From the keyboard?</h3>
<p> You can use the builtin <tt>&quot;getc()&quot;</tt> function for most filehandles, but it won&#8217;t (easily) work on a terminal device. For <font SIZE="-1">STDIN,</font> either use the Term::ReadKey module from <font SIZE="-1">CPAN</font> or use the sample code in &#8220;getc&#8221; in perlfunc. </p>
<p> If your system supports the portable operating system programming interface (<font SIZE="-1">POSIX</font>), you can use the following code, which you&#8217;ll note turns off echo processing as well. </p>
<p>#!/ usr / bin / perl &#8211; w<br />
use strict;<br />
$ | = 1;<br />
for (1..4) {<br />
    print &#8220;gimme: &#8220;;<br />
    my $got = getone();<br />
    print &#8220;&#8211;&gt; $got
&#8221;;<br />
}<br />
exit;<br />
BEGIN<br />
{<br />
    use POSIX qw(<br />
        : termios_h);<br />
    my($term, $oterm, $echo, $noecho, $fd_stdin);<br />
    my $fd_stdin = fileno(STDIN);<br />
    $term = POSIX::Termios-&gt;new ();<br />
    $term-&gt;getattr($fd_stdin);<br />
    $oterm = $term-&gt;getlflag();<br />
    $echo = ECHO | ECHOK | ICANON;<br />
    $noecho = $oterm &amp; ~$echo;<br />
    sub cbreak<br />
    {<br />
        $term-&gt;setlflag($noecho);<br />
        $term-&gt;setcc(VTIME, 1);<br />
        $term-&gt;setattr($fd_stdin, TCSANOW);<br />
    }<br />
    sub cooked<br />
    {<br />
        $term-&gt;setlflag($oterm);<br />
        $term-&gt;setcc(VTIME, 0);<br />
        $term-&gt;setattr($fd_stdin, TCSANOW);<br />
    }<br />
    sub getone<br />
    {<br />
        my $key = &#8221;;<br />
        cbreak();<br />
        sysread(STDIN, $key, 1);<br />
        cooked();<br />
        return $key;<br />
    }<br />
}<br />
END<br />
{<br />
    cooked()<br />
}</p>
<p> The Term::ReadKey module from <font SIZE="-1">CPAN</font> may be easier to use. Recent versions include also support for non-portable systems as well. </p>
<p>use Term::ReadKey;<br />
open my $tty, &#8216;&lt;&#8216;, &#8216;/dev/tty&#8217;;<br />
print &#8220;Gimme a char: &#8220;;<br />
ReadMode &#8220;raw&#8221;;<br />
my $key = ReadKey 0, $tty;<br />
ReadMode &#8220;normal&#8221;;<br />
printf &#8220;
You said %s, char number %03d
&#8221;,<br />
    $key, ord $key;</p>
<h3>How can I tell whether there&#8217;s a character waiting on a filehandle?</h3>
<p> The very first thing you should do is look into getting the Term::ReadKey extension from <font SIZE="-1">CPAN.</font> As we mentioned earlier, it now even has limited support for non-portable (read: not open systems, closed, proprietary, not <font SIZE="-1">POSIX,</font> not Unix, etc.) systems. </p>
<p> You should also check out the Frequently Asked Questions list in comp.unix.* for things like this: the answer is essentially the same. It&#8217;s very system-dependent. Here&#8217;s one solution that works on <font SIZE="-1">BSD</font> systems: </p>
<p>sub key_ready<br />
{<br />
    my($rin, $nfd);<br />
    vec($rin, fileno(STDIN), 1) = 1;<br />
    return $nfd = select($rin, undef, undef, 0);<br />
}</p>
<p> If you want to find out how many characters are waiting, there&#8217;s also the <font SIZE="-1">FIONREAD</font> ioctl call to be looked at. The <i>h2ph</i> tool that comes with Perl tries to convert C include files to Perl code, which can be <tt>&quot;require&quot;</tt>d. <font SIZE="-1">FIONREAD</font> ends up defined as a function in the <i>sys/ioctl.ph</i> file: </p>
<p>require &#8216;./sys/ioctl.ph&#8217;;<br />
$size = pack(&#8220;L&#8221;, 0);<br />
ioctl(FH, FIONREAD(), $size) or die &#8220;Couldn&#8217;t call ioctl: $!
&#8221;;<br />
$size = unpack(&#8220;L&#8221;, $size);</p>
<p> If <i>h2ph</i> wasn&#8217;t installed or doesn&#8217;t work for you, you can <i>grep</i> the include files by hand: </p>
<p>% grep FIONREAD / usr / include /*/*<br />
    /usr/include/asm/ioctls.h:#define FIONREAD      0x541B</p>
<p> Or write a small C program using the editor of champions: </p>
<p>% cat &gt; fionread.c<br />
#include &lt;sys/ioctl.h&gt;<br />
        main()<br />
{<br />
    printf(&#8220;%#08x
&#8221;, FIONREAD);<br />
}<br />
^D % cc &#8211; o fionread fionread.c %./ fionread 0x4004667f</p>
<p> And then hard-code it, leaving porting as an exercise to your successor. </p>
<p>$FIONREAD = 0x4004667f;<br />
#XXX : opsys dependent<br />
    $size = pack(&#8220;L&#8221;, 0);<br />
ioctl(FH, $FIONREAD, $size) or die &#8220;Couldn&#8217;t call ioctl: $!
&#8221;;<br />
$size = unpack(&#8220;L&#8221;, $size);</p>
<p> <font SIZE="-1">FIONREAD</font> requires a filehandle connected to a stream, meaning that sockets, pipes, and tty devices work, but <i>not</i> files.</p>
<h3>How do I do a tail -f in perl?</h3>
<p> First try </p>
<pre>
    seek($gw_fh, 0, 1);
</pre>
<p> The statement <tt>&quot;seek($gw_fh, 0, 1)&quot;</tt> doesn&#8217;t change the current position, but it does clear the end-of-file condition on the handle, so that the next <tt>&quot;&lt;$gw_fh&gt;&quot;</tt> makes Perl try again to read something. </p>
<p> If that doesn&#8217;t work (it relies on features of your stdio implementation), then you need something more like this: </p>
<p>for (;;) {<br />
    for ($curpos = tell($gw_fh);&lt;$gw_fh&gt;; $curpos = tell($gw_fh)) {<br />
#search for some stuff and put it into files<br />
    }<br />
#sleep for a while<br />
    seek($gw_fh, $curpos, 0);<br />
#seek to where we had been<br />
}</p>
<p> If this still doesn&#8217;t work, look into the <tt>&quot;clearerr&quot;</tt> method from IO::Handle, which resets the error and end-of-file states on the handle. </p>
<p> There&#8217;s also a File::Tail module from <font SIZE="-1">CPAN.</font></p>
<h3>How do I <code>dup()</code> a filehandle in Perl?</h3>
<p> If you check &#8220;open&#8221; in perlfunc, you&#8217;ll see that several of the ways to call <code>open()</code> should do the trick. For example: </p>
<pre>
    open my $log, '&gt;&gt;', '/foo/logfile';
    open STDERR, '&gt;&amp;', $log;
</pre>
<p> Or even with a literal numeric descriptor: </p>
<p>my $fd = $ENV{MHCONTEXTFD};<br />
open $mhcontext, &#8220;&lt;&amp;=$fd&#8221;;<br />
#like fdopen(3S)</p>
<p> Note that &#8220;&lt;&amp;STDIN&#8221; makes a copy, but &#8220;&lt;&amp;=STDIN&#8221; makes an alias. That means if you close an aliased handle, all aliases become inaccessible. This is not true with a copied one. </p>
<p> Error checking, as always, has been left as an exercise for the reader.</p>
<h3>How do I close a file descriptor by number?</h3>
<p> If, for some reason, you have a file descriptor instead of a filehandle (perhaps you used <tt>&quot;POSIX::open&quot;</tt>), you can use the <tt>&quot;close()&quot;</tt> function from the <font SIZE="-1">POSIX</font> module: </p>
<p>use POSIX();<br />
POSIX::close($fd);</p>
<p> This should rarely be necessary, as the Perl <tt>&quot;close()&quot;</tt> function is to be used for things that Perl opened itself, even if it was a dup of a numeric descriptor as with <tt>&quot;MHCONTEXT&quot;</tt> above. But if you really have to, you may be able to do this: </p>
<p>require &#8216;./sys/syscall.ph&#8217;;<br />
my $rc = syscall(SYS_close(), $fd + 0);<br />
#must force numeric<br />
        die &#8220;can&#8217;t sysclose $fd: $!&#8221; unless $rc == -1;</p>
<p> Or, just use the <a href="//www.systutorials.com/docs/linux/man/3S-fdopen/">fdopen</a>(3S) feature of <tt>&quot;open()&quot;</tt>: </p>
<p>{<br />
    open my $fh, &#8220;&lt;&amp;=$fd&#8221; or die &#8220;Cannot reopen fd=$fd: $!&#8221;;<br />
    close $fh;<br />
}</p>
<h3>Why can&#8217;t I use C:	empoo in <font SIZE="-1">DOS</font> paths? Why doesn&#8217;t `C:	empoo.exe` work?</h3>
<p> Whoops! You just put a tab and a formfeed into that filename! Remember that within double quoted strings (&#8220;like	his&#8221;), the backslash is an escape character. The full list of these is in &#8220;Quote and Quote-like Operators&#8221; in perlop. Unsurprisingly, you don&#8217;t have a file called &#8220;c:(tab)emp(formfeed)oo&#8221; or &#8220;c:(tab)emp(formfeed)oo.exe&#8221; on your legacy <font SIZE="-1">DOS</font> filesystem. </p>
<p> Either single-quote your strings, or (preferably) use forward slashes. Since all <font SIZE="-1">DOS</font> and Windows versions since something like MS-DOS 2.0 or so have treated <tt>&quot;/&quot;</tt> and <tt>&quot;\&quot;</tt> the same in a path, you might as well use the one that doesn&#8217;t clash with Perl&#8212;or the <font SIZE="-1">POSIX</font> shell, <font SIZE="-1">ANSI C</font> and C<font SIZE="-2">++</font>, awk, Tcl, Java, or Python, just to mention a few. <font SIZE="-1">POSIX</font> paths are more portable, too.</p>
<h3>Why doesn&#8217;t glob(*.*) get all the files?</h3>
<p> Because even on non-Unix ports, Perl&#8217;s glob function follows standard Unix globbing semantics. You&#8217;ll need <tt>&quot;glob(&quot;*&quot;)&quot;</tt> to get all (non-hidden) files. This makes <code>glob()</code> portable even to legacy systems. Your port may include proprietary globbing functions as well. Check its documentation for details.</p>
<h3>Why does Perl let me delete read-only files? Why does -i clobber protected files? Isn&#8217;t this a bug in Perl?</h3>
<p> This is elaborately and painstakingly described in the <i>file-dir-perms</i> article in the &#8220;Far More Than You Ever Wanted To Know&#8221; collection in &lt;<a rel="nofollow" href="http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz">http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz</a>&gt; . </p>
<p> The executive summary: learn how your filesystem works. The permissions on a file say what can happen to the data in that file. The permissions on a directory say what can happen to the list of files in that directory. If you delete a file, you&#8217;re removing its name from the directory (so the operation depends on the permissions of the directory, not of the file). If you try to write to the file, the permissions of the file govern whether you&#8217;re allowed to.</p>
<h3>How do I select a random line from a file?</h3>
<p> Short of loading the file into a database or pre-indexing the lines in the file, there are a couple of things that you can do. </p>
<p> Here&#8217;s a reservoir-sampling algorithm from the Camel Book: </p>
<p>srand;<br />
rand($.) &lt; 1 &amp;&amp; ($line = $_) while&lt;&gt;;</p>
<p> This has a significant advantage in space over reading the whole file in. You can find a proof of this method in <i>The Art of Computer Programming</i>, Volume 2, Section 3.4.2, by Donald E. Knuth. </p>
<p> You can use the File::Random module which provides a function for that algorithm: </p>
<p>use File::Random qw / random_line / ;<br />
my $line = random_line($filename);</p>
<p> Another way is to use the Tie::File module, which treats the entire file as an array. Simply access a random array element.</p>
<h3>Why do I get weird spaces when I print an array of lines?</h3>
<p> (contributed by brian d foy) </p>
<p> If you are seeing spaces between the elements of your array when you print the array, you are probably interpolating the array in double quotes: </p>
<p>my @animals = qw(camel llama alpaca vicuna);<br />
print &#8220;animals are: @animals
&#8221;;</p>
<p> It&#8217;s the double quotes, not the <tt>&quot;print&quot;</tt>, doing this. Whenever you interpolate an array in a double quote context, Perl joins the elements with spaces (or whatever is in <tt>$&quot;</tt>, which is a space by default): </p>
<pre>
    animals are: camel llama alpaca vicuna
</pre>
<p> This is different than printing the array without the interpolation: </p>
<p>my @animals = qw(camel llama alpaca vicuna);<br />
print &#8220;animals are: &#8220;, @animals, &#8220;
&#8221;;</p>
<p> Now the output doesn&#8217;t have the spaces between the elements because the elements of <tt>@animals</tt> simply become part of the list to <tt>&quot;print&quot;</tt>: </p>
<pre>
    animals are: camelllamaalpacavicuna
</pre>
<p> You might notice this when each of the elements of <tt>@array</tt> end with a newline. You expect to print one element per line, but notice that every line after the first is indented: </p>
<pre>
    this is a line
     this is another line
     this is the third line
</pre>
<p> That extra space comes from the interpolation of the array. If you don&#8217;t want to put anything between your array elements, don&#8217;t use the array in double quotes. You can send it to print without them: </p>
<pre>
    print @lines;
</pre>
<h3>How do I traverse a directory tree?</h3>
<p> (contributed by brian d foy) </p>
<p> The File::Find module, which comes with Perl, does all of the hard work to traverse a directory structure. It comes with Perl. You simply call the <tt>&quot;find&quot;</tt> subroutine with a callback subroutine and the directories you want to traverse: </p>
<p>use File::Find;<br />
find( \&amp;wanted, @directories);<br />
sub wanted<br />
{<br />
#full path in $File::Find::name<br />
#just filename in $_<br />
    &#8230; do whatever you want to do&#8230;<br />
}</p>
<p> The File::Find::Closures, which you can download from <font SIZE="-1">CPAN,</font> provides many ready-to-use subroutines that you can use with File::Find. </p>
<p> The File::Finder, which you can download from <font SIZE="-1">CPAN,</font> can help you create the callback subroutine using something closer to the syntax of the <tt>&quot;find&quot;</tt> command-line utility: </p>
<p>use File::Find;<br />
use File::Finder;<br />
my $deep_dirs = File::Finder-&gt;depth-&gt;type(&#8216;d&#8217;)-&gt;ls-&gt;exec(&#8216;rmdir&#8217;, &#8216;{}&#8217;);<br />
find($deep_dirs-&gt;as_options, @places);</p>
<p> The File::Find::Rule module, which you can download from <font SIZE="-1">CPAN,</font> has a similar interface, but does the traversal for you too: </p>
<p>use File::Find::Rule;<br />
my @files = File::Find::Rule-&gt;file()<br />
                -&gt;name(&#8216;*.pm&#8217;)<br />
                -&gt;in(@INC);</p>
<h3>How do I delete a directory tree?</h3>
<p> (contributed by brian d foy) </p>
<p> If you have an empty directory, you can use Perl&#8217;s built-in <tt>&quot;rmdir&quot;</tt>. If the directory is not empty (so, with files or subdirectories), you either have to empty it yourself (a lot of work) or use a module to help you. </p>
<p> The File::Path module, which comes with Perl, has a <tt>&quot;remove_tree&quot;</tt> which can take care of all of the hard work for you: </p>
<pre><code>
use File::Path qw(remove_tree);
remove_tree(@directories);
</code></pre>
<p> The File::Path module also has a legacy interface to the older <tt>&quot;rmtree&quot;</tt> subroutine.</p>
<h3>How do I copy an entire directory?</h3>
<p> (contributed by Shlomi Fish) </p>
<p> To do the equivalent of <tt>&quot;cp -R&quot;</tt> (i.e. copy an entire directory tree recursively) in portable Perl, you&#8217;ll either need to write something yourself or find a good <font SIZE="-1">CPAN</font> module such as File::Copy::Recursive.</p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 1997-2010 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples here are in the public domain. You are permitted and encouraged to use this code and any derivatives thereof in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit to the <font SIZE="-1">FAQ</font> would be courteous but is not required. </p>
<h2>Index</h2>
<dt><a href="#lbBU">AUTHOR AND COPYRIGHT</a></p>
<dd></dl>
