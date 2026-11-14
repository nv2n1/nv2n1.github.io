---
title: "perlopentut(1)"
name: "perlopentut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlopentut/"
---

<h2 class="name">NAME</h2>
 

 perlopentut - simple recipes for opening files and pipes in Perl 

<h2>DESCRIPTION</h2>

 Whenever you do I/O on a file in Perl, you do so through what in Perl is called a <b>filehandle</b>. A filehandle is an internal name for an external file. It is the job of the <tt>&quot;open&quot;</tt> function to make the association between the internal name and the external name, and it is the job of the <tt>&quot;close&quot;</tt> function to break that association. 

 For your convenience, Perl sets up a few special filehandles that are already open when you run. These include <tt>&quot;STDIN&quot;</tt>, <tt>&quot;STDOUT&quot;</tt>, <tt>&quot;STDERR&quot;</tt>, and <tt>&quot;ARGV&quot;</tt>. Since those are pre-opened, you can use them right away without having to go to the trouble of opening them yourself: 

 <pre><code>
print STDERR "This is a debugging message.\n";
print STDOUT "Please enter something: ";
$response = &lt;STDIN&gt; // die "how come no input?";
    print STDOUT "Thank you!\n";
while (&lt;ARGV&gt;) {
    ...
}
</code></pre> 

 As you see from those examples, <tt>&quot;STDOUT&quot;</tt> and <tt>&quot;STDERR&quot;</tt> are output handles, and <tt>&quot;STDIN&quot;</tt> and <tt>&quot;ARGV&quot;</tt> are input handles. They are in all capital letters because they are reserved to Perl, much like the <tt>@ARGV</tt> array and the <tt>%ENV</tt> hash are. Their external associations were set up by your shell. 

 You will need to open every other filehandle on your own. Although there are many variants, the most common way to call Perl's <b>open()</b> function is with three arguments and one return value: 

 <tt>&quot; </tt>OK<tt> = open(</tt>HANDLE<tt>, </tt>MODE<tt>, </tt>PATHNAME<tt>)&quot;</tt> 

 Where:
<dl>
<dt><i></i><font SIZE="-1"><i>OK</i></font><i></i>
<dd> will be some defined value if the open succeeds, but <tt>&quot;undef&quot;</tt> if it fails;
<dt><i></i><font SIZE="-1"><i>HANDLE</i></font><i></i>
<dd> should be an undefined scalar variable to be filled in by the <tt>&quot;open&quot;</tt> function if it succeeds;
<dt><i></i><font SIZE="-1"><i>MODE</i></font><i></i>
<dd> is the access mode and the encoding format to open the file with;
<dt><i></i><font SIZE="-1"><i>PATHNAME</i></font><i></i>
<dd> is the external name of the file you want opened.</dl>
 

 Most of the complexity of the <tt>&quot;open&quot;</tt> function lies in the many possible values that the <i></i><font SIZE="-1"><i>MODE</i></font><i></i> parameter can take on. 

 One last thing before we show you how to open files: opening files does not (usually) automatically lock them in Perl. See perlfaq5 for how to lock.

<h2>Opening Text Files</h2>

<h3>Opening Text Files for Reading</h3>

 If you want to read from a text file, first open it in read-only mode like this: 

 
my $filename = "/some/path/to/a/textfile/goes/here";
my $encoding = ":encoding(UTF-8)";
my $handle = undef;
#this will be filled in on success
        open($handle, "&lt; $encoding", $filename) ||
    die "$0: can't open $filename for reading: $!";
 

 As with the shell, in Perl the <tt>&quot;&lt;&quot;</tt> is used to open the file in read-only mode. If it succeeds, Perl allocates a brand new filehandle for you and fills in your previously undefined <tt>$handle</tt> argument with a reference to that handle. 

 Now you may use functions like <tt>&quot;readline&quot;</tt>, <tt>&quot;read&quot;</tt>, <tt>&quot;getc&quot;</tt>, and <tt>&quot;sysread&quot;</tt> on that handle. Probably the most common input function is the one that looks like an operator: 

 
$line = readline($handle);
$line = &lt;$handle&gt;;
#same thing
 

 Because the <tt>&quot;readline&quot;</tt> function returns <tt>&quot;undef&quot;</tt> at end of file or upon error, you will sometimes see it used this way: 

 
$line = &lt;$handle&gt;;
if (defined $line) {
#do something with $line
} else {
#$line is not valid, so skip it
}
 

 You can also just quickly <tt>&quot;die&quot;</tt> on an undefined value this way: 

 <pre>
    $line = &lt;$handle&gt; // die &quot;no input found&quot;;
</pre> 

 However, if hitting <font SIZE="-1">EOF</font> is an expected and normal event, you do not want to exit simply because you have run out of input. Instead, you probably just want to exit an input loop. You can then test to see if an actual error has caused the loop to terminate, and act accordingly: 

 
while (&lt;$handle&gt;) {
#do something with data in $_
}
if ($ !) {
    die "unexpected error while reading from $filename: $!";
}
 

 <b>A Note on Encodings</b>: Having to specify the text encoding every time might seem a bit of a bother. To set up a default encoding for <tt>&quot;open&quot;</tt> so that you don't have to supply it each time, you can use the <tt>&quot;open&quot;</tt> pragma: 

 <pre>
    use open qw&lt; :encoding(UTF-8) &gt;;
</pre> 

 Once you've done that, you can safely omit the encoding part of the open mode: 

 <pre>
    open($handle, &quot;&lt;&quot;, $filename)
        || die &quot;$0: can't open $filename for reading: $!&quot;;
</pre> 

 But never use the bare <tt>&quot;&lt;&quot;</tt> without having set up a default encoding first. Otherwise, Perl cannot know which of the many, many, many possible flavors of text file you have, and Perl will have no idea how to correctly map the data in your file into actual characters it can work with. Other common encoding formats including <tt>&quot;ASCII&quot;</tt>, <tt>&quot;ISO-8859-1&quot;</tt>, <tt>&quot;ISO-8859-15&quot;</tt>, <tt>&quot;Windows-1252&quot;</tt>, <tt>&quot;MacRoman&quot;</tt>, and even <tt>&quot;UTF-16LE&quot;</tt>. See perlunitut for more about encodings.

<h3>Opening Text Files for Writing</h3>

 When you want to write to a file, you first have to decide what to do about any existing contents of that file. You have two basic choices here: to preserve or to clobber. 

 If you want to preserve any existing contents, then you want to open the file in append mode. As in the shell, in Perl you use <tt>&quot;&gt;&gt;&quot;</tt> to open an existing file in append mode. <tt>&quot;&gt;&gt;&quot;</tt> creates the file if it does not already exist. 

 
my $handle = undef;
my $filename = "/some/path/to/a/textfile/goes/here";
my $encoding = ":encoding(UTF-8)";
open($handle, "&gt;&gt; $encoding", $filename) || die "$0: can't open $filename for appending: $!";
 

 Now you can write to that filehandle using any of <tt>&quot;print&quot;</tt>, <tt>&quot;printf&quot;</tt>, <tt>&quot;say&quot;</tt>, <tt>&quot;write&quot;</tt>, or <tt>&quot;syswrite&quot;</tt>. 

 As noted above, if the file does not already exist, then the append-mode open will create it for you. But if the file does already exist, its contents are safe from harm because you will be adding your new text past the end of the old text. 

 On the other hand, sometimes you want to clobber whatever might already be there. To empty out a file before you start writing to it, you can open it in write-only mode: 

 
my $handle = undef;
my $filename = "/some/path/to/a/textfile/goes/here";
my $encoding = ":encoding(UTF-8)";
open($handle, "&gt; $encoding", $filename) || die "$0: can't open $filename in write-open mode: $!";
 

 Here again Perl works just like the shell in that the <tt>&quot;&gt;&quot;</tt> clobbers an existing file. 

 As with the append mode, when you open a file in write-only mode, you can now write to that filehandle using any of <tt>&quot;print&quot;</tt>, <tt>&quot;printf&quot;</tt>, <tt>&quot;say&quot;</tt>, <tt>&quot;write&quot;</tt>, or <tt>&quot;syswrite&quot;</tt>. 

 What about read-write mode? You should probably pretend it doesn't exist, because opening text files in read-write mode is unlikely to do what you would like. See perlfaq5 for details.

<h2>Opening Binary Files</h2>

 If the file to be opened contains binary data instead of text characters, then the <tt>&quot;MODE&quot;</tt> argument to <tt>&quot;open&quot;</tt> is a little different. Instead of specifying the encoding, you tell Perl that your data are in raw bytes. 

 <pre>
    my $filename = &quot;/some/path/to/a/binary/file/goes/here&quot;;
    my $encoding = &quot;:raw :bytes&quot;
    my $handle   = undef;     # this will be filled in on success
</pre> 

 And then open as before, choosing <tt>&quot;&lt;&quot;</tt>, <tt>&quot;&gt;&gt;&quot;</tt>, or <tt>&quot;&gt;&quot;</tt> as needed: 

 
open($handle, "&lt; $encoding", $filename) || die "$0: can't open $filename for reading: $!";
open($handle, "&gt;&gt; $encoding", $filename) || die "$0: can't open $filename for appending: $!";
open($handle, "&gt; $encoding", $filename) || die "$0: can't open $filename in write-open mode: $!";
 

 Alternately, you can change to binary mode on an existing handle this way: 

 <pre>
    binmode($handle)    || die &quot;cannot binmode handle&quot;;
</pre> 

 This is especially handy for the handles that Perl has already opened for you. 

 
binmode(STDIN) || die "cannot binmode STDIN";
binmode(STDOUT) || die "cannot binmode STDOUT";
 

 You can also pass <tt>&quot;binmode&quot;</tt> an explicit encoding to change it on the fly. This isn't exactly ``binary'' mode, but we still use <tt>&quot;binmode&quot;</tt> to do it: 

 
binmode(STDIN, ":encoding(MacRoman)") || die "cannot binmode STDIN";
binmode(STDOUT, ":encoding(UTF-8)") || die "cannot binmode STDOUT";
 

 Once you have your binary file properly opened in the right mode, you can use all the same Perl I/O functions as you used on text files. However, you may wish to use the fixed-size <tt>&quot;read&quot;</tt> instead of the variable-sized <tt>&quot;readline&quot;</tt> for your input. 

 Here's an example of how to copy a binary file: 

 <pre><code>
my $BUFSIZ = 64 * (2 * *10);
my $name_in = "/some/input/file";
my $name_out = "/some/output/flie";
my($in_fh, $out_fh, $buffer);
open($in_fh, "&lt;", $name_in) || die "$0: cannot open $name_in for reading: $!";
open($out_fh, "&gt;", $name_out) || die "$0: cannot open $name_out for writing: $!";
    for
        my $fh($in_fh, $out_fh)
        {
            binmode($fh) || die "binmode failed";
        }
    while (read($in_fh, $buffer, $BUFSIZ)) {
        unless(print $out_fh $buffer)
        {
            die "couldn't write to $name_out: $!";
        }
    }
    close($in_fh) || die "couldn't close $name_in: $!";
    close($out_fh) || die "couldn't close $name_out: $!";
</code></pre>

<h2>Opening Pipes</h2>

 To be announced.

<h2>Low-level File Opens via sysopen</h2>

 To be announced. Or deleted.

<h2>SEE ALSO</h2>

 To be announced.

<h2>AUTHOR and COPYRIGHT</h2>

 Copyright 2013 Tom Christiansen. 

 This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


