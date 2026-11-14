---
title: "perlunifaq(1)"
name: "perlunifaq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlunifaq/"
---

<h2 class="name">NAME</h2>
 

 perlunifaq - Perl Unicode FAQ 

<h2>Q and A</h2>

 This is a list of questions and answers about Unicode in Perl, intended to be read after perlunitut.

<h3>perlunitut isn't really a Unicode tutorial, is it?</h3>

 No, and this isn't really a Unicode <font SIZE="-1">FAQ.</font> 

 Perl has an abstracted interface for all supported character encodings, so this is actually a generic <tt>&quot;Encode&quot;</tt> tutorial and <tt>&quot;Encode&quot;</tt> <font SIZE="-1">FAQ.</font> But many people think that Unicode is special and magical, and I didn't want to disappoint them, so I decided to call the document a Unicode tutorial.

<h3>What character encodings does Perl support?</h3>

 To find out which character encodings your Perl supports, run: 

 <pre>
    perl -MEncode -le &quot;print for Encode-&gt;encodings(':all')&quot;
</pre>

<h3>Which version of perl should I use?</h3>

 Well, if you can, upgrade to the most recent, but certainly <tt>5.8.1</tt> or newer. The tutorial and <font SIZE="-1">FAQ</font> assume the latest release. 

 You should also check your modules, and upgrade them if necessary. For example, HTML::Entities requires version &gt;= 1.32 to function correctly, even though the changelog is silent about this.

<h3>What about binary data, like images?</h3>

 Well, apart from a bare <tt>&quot;binmode $fh&quot;</tt>, you shouldn't treat them specially. (The binmode is needed because otherwise Perl may convert line endings on Win32 systems.) 

 Be careful, though, to never combine text strings with binary strings. If you need text in a binary stream, encode your text strings first using the appropriate encoding, then join them with binary strings. See also: ``What if I don't encode?''.

<h3>When should I decode or encode?</h3>

 Whenever you're communicating text with anything that is external to your perl process, like a database, a text file, a socket, or another program. Even if the thing you're communicating with is also written in Perl.

<h3>What if I don't decode?</h3>

 Whenever your encoded, binary string is used together with a text string, Perl will assume that your binary string was encoded with <font SIZE="-1">ISO-8859-1,</font> also known as latin-1. If it wasn't latin-1, then your data is unpleasantly converted. For example, if it was <font SIZE="-1">UTF-8,</font> the individual bytes of multibyte characters are seen as separate characters, and then again converted to <font SIZE="-1">UTF-8.</font> Such double encoding can be compared to double <font SIZE="-1">HTML</font> encoding (<tt>&quot;&amp;amp;gt;&quot;</tt>), or double <font SIZE="-1">URI</font> encoding (<tt>%253E</tt>). 

 This silent implicit decoding is known as ``upgrading''. That may sound positive, but it's best to avoid it.

<h3>What if I don't encode?</h3>

 Your text string will be sent using the bytes in Perl's internal format. In some cases, Perl will warn you that you're doing something wrong, with a friendly warning: 

 <pre>
    Wide character in print at example.pl line 2.
</pre> 

 Because the internal format is often <font SIZE="-1">UTF-8,</font> these bugs are hard to spot, because <font SIZE="-1">UTF-8</font> is usually the encoding you wanted! But don't be lazy, and don't use the fact that Perl's internal format is <font SIZE="-1">UTF-8</font> to your advantage. Encode explicitly to avoid weird bugs, and to show to maintenance programmers that you thought this through.

<h3>Is there a way to automatically decode or encode?</h3>

 If all data that comes from a certain handle is encoded in exactly the same way, you can tell the PerlIO system to automatically decode everything, with the <tt>&quot;encoding&quot;</tt> layer. If you do this, you can't accidentally forget to decode or encode anymore, on things that use the layered handle. 

 You can provide this layer when <tt>&quot;open&quot;</tt>ing the file: 

 <pre><code>
open my $fh, '&gt;:encoding(UTF-8)', $filename;
#auto encoding on write
    open my $fh,
    '&lt;:encoding(UTF-8)', $filename;
#auto decoding on read
</code></pre> 

 Or if you already have an open filehandle: 

 <pre>
  binmode $fh, ':encoding(UTF-8)';
</pre> 

 Some database drivers for <font SIZE="-1">DBI</font> can also automatically encode and decode, but that is sometimes limited to the <font SIZE="-1">UTF-8</font> encoding.

<h3>What if I don't know which encoding was used?</h3>

 Do whatever you can to find out, and if you have to: guess. (Don't forget to document your guess with a comment.) 

 You could open the document in a web browser, and change the character set or character encoding until you can visually confirm that all characters look the way they should. 

 There is no way to reliably detect the encoding automatically, so if people keep sending you data without charset indication, you may have to educate them.

<h3>Can I use Unicode in my Perl sources?</h3>

 Yes, you can! If your sources are <font SIZE="-1">UTF-8</font> encoded, you can indicate that with the <tt>&quot;use utf8&quot;</tt> pragma. 

 <pre>
    use utf8;
</pre> 

 This doesn't do anything to your input, or to your output. It only influences the way your sources are read. You can use Unicode in string literals, in identifiers (but they still have to be ``word characters'' according to <tt>&quot;\w&quot;</tt>), and even in custom delimiters.

<h3>Data::Dumper doesn't restore the <font SIZE="-1">UTF8</font> flag; is it broken?</h3>

 No, Data::Dumper's Unicode abilities are as they should be. There have been some complaints that it should restore the <font SIZE="-1">UTF8</font> flag when the data is read again with <tt>&quot;eval&quot;</tt>. However, you should really not look at the flag, and nothing indicates that Data::Dumper should break this rule. 

 Here's what happens: when Perl reads in a string literal, it sticks to 8 bit encoding as long as it can. (But perhaps originally it was internally encoded as <font SIZE="-1">UTF-8,</font> when you dumped it.) When it has to give that up because other characters are added to the text string, it silently upgrades the string to <font SIZE="-1">UTF-8.</font> 

 If you properly encode your strings for output, none of this is of your concern, and you can just <tt>&quot;eval&quot;</tt> dumped data as always.

<h3>Why do regex character classes sometimes match only in the <font SIZE="-1">ASCII</font> range?</h3>

 Starting in Perl 5.14 (and partially in Perl 5.12), just put a <tt>&quot;use feature 'unicode_strings'&quot;</tt> near the beginning of your program. Within its lexical scope you shouldn't have this problem. It also is automatically enabled under <tt>&quot;use feature ':5.12'&quot;</tt> or <tt>&quot;use v5.12&quot;</tt> or using <tt>&quot;-E&quot;</tt> on the command line for Perl 5.12 or higher. 

 The rationale for requiring this is to not break older programs that rely on the way things worked before Unicode came along. Those older programs knew only about the <font SIZE="-1">ASCII</font> character set, and so may not work properly for additional characters. When a string is encoded in <font SIZE="-1">UTF-8,</font> Perl assumes that the program is prepared to deal with Unicode, but when the string isn't, Perl assumes that only <font SIZE="-1">ASCII</font> is wanted, and so those characters that are not <font SIZE="-1">ASCII</font> characters aren't recognized as to what they would be in Unicode. <tt>&quot;use feature 'unicode_strings'&quot;</tt> tells Perl to treat all characters as Unicode, whether the string is encoded in <font SIZE="-1">UTF-8</font> or not, thus avoiding the problem. 

 However, on earlier Perls, or if you pass strings to subroutines outside the feature's scope, you can force Unicode rules by changing the encoding to <font SIZE="-1">UTF-8</font> by doing <tt>&quot;utf8::upgrade($string)&quot;</tt>. This can be used safely on any string, as it checks and does not change strings that have already been upgraded. 

 For a more detailed discussion, see Unicode::Semantics on <font SIZE="-1">CPAN.</font>

<h3>Why do some characters not uppercase or lowercase correctly?</h3>

 See the answer to the previous question.

<h3>How can I determine if a string is a text string or a binary string?</h3>

 You can't. Some use the <font SIZE="-1">UTF8</font> flag for this, but that's misuse, and makes well behaved modules like Data::Dumper look bad. The flag is useless for this purpose, because it's off when an 8 bit encoding (by default <font SIZE="-1">ISO-8859-1</font>) is used to store the string. 

 This is something you, the programmer, has to keep track of; sorry. You could consider adopting a kind of ``Hungarian notation'' to help with this.

<h3>How do I convert from encoding <font SIZE="-1">FOO</font> to encoding <font SIZE="-1">BAR</font>?</h3>

 By first converting the FOO-encoded byte string to a text string, and then the text string to a BAR-encoded byte string: 

 
my $text_string = decode('FOO', $foo_string);
my $bar_string = encode('BAR', $text_string);
 

 or by skipping the text string part, and going directly from one binary encoding to the other: 

 
use Encode qw(from_to);
from_to($string, 'FOO', 'BAR');
#changes contents of $string
 

 or by letting automatic decoding and encoding do all the work: 

 <pre><code>
open my $foofh, '&lt;:encoding(FOO)', 'example.foo.txt';
open my $barfh, '&gt;:encoding(BAR)', 'example.bar.txt';
print{$barfh} $_ while&lt;$foofh&gt;;
</code></pre>

<h3>What are decode_utf8 and encode_utf8?</h3>

 These are alternate syntaxes for <tt>&quot;decode('utf8', ...)&quot;</tt> and <tt>&quot;encode('utf8', ...)&quot;</tt>. Do not use these functions for data exchange. Instead use <tt>&quot;decode('UTF-8', ...)&quot;</tt> and <tt>&quot;encode('UTF-8', ...)&quot;</tt>; see ``What's the difference between <font SIZE="-1">UTF-8</font> and utf8?'' below.

<h3>What is a wide character?</h3>

 This is a term used for characters occupying more than one byte. 

 The Perl warning ``Wide character in ...'' is caused by such a character. With no specified encoding layer, Perl tries to fit things into a single byte. When it can't, it emits this warning (if warnings are enabled), and uses <font SIZE="-1">UTF-8</font> encoded data instead. 

 To avoid this warning and to avoid having different output encodings in a single stream, always specify an encoding explicitly, for example with a PerlIO layer: 

 <pre>
    binmode STDOUT, &quot;:encoding(UTF-8)&quot;;
</pre>

<h2>INTERNALS</h2>

<h3>What is the <font SIZE="-1">UTF8</font> flag?</h3>

 Please, unless you're hacking the internals, or debugging weirdness, don't think about the <font SIZE="-1">UTF8</font> flag at all. That means that you very probably shouldn't use <tt>&quot;is_utf8&quot;</tt>, <tt>&quot;_utf8_on&quot;</tt> or <tt>&quot;_utf8_off&quot;</tt> at all. 

 The <font SIZE="-1">UTF8</font> flag, also called SvUTF8, is an internal flag that indicates that the current internal representation is <font SIZE="-1">UTF-8.</font> Without the flag, it is assumed to be <font SIZE="-1">ISO-8859-1.</font> Perl converts between these automatically. (Actually Perl usually assumes the representation is <font SIZE="-1">ASCII</font>; see ``Why do regex character classes sometimes match only in the <font SIZE="-1">ASCII</font> range?'' above.) 

 One of Perl's internal formats happens to be <font SIZE="-1">UTF-8.</font> Unfortunately, Perl can't keep a secret, so everyone knows about this. That is the source of much confusion. It's better to pretend that the internal format is some unknown encoding, and that you always have to encode and decode explicitly.

<h3>What about the use bytes pragma?</h3>

 Don't use it. It makes no sense to deal with bytes in a text string, and it makes no sense to deal with characters in a byte string. Do the proper conversions (by decoding/encoding), and things will work out well: you get character counts for decoded data, and byte counts for encoded data. 

 <tt>&quot;use bytes&quot;</tt> is usually a failed attempt to do something useful. Just forget about it.

<h3>What about the use encoding pragma?</h3>

 Don't use it. Unfortunately, it assumes that the programmer's environment and that of the user will use the same encoding. It will use the same encoding for the source code and for <font SIZE="-1">STDIN</font> and <font SIZE="-1">STDOUT.</font> When a program is copied to another machine, the source code does not change, but the <font SIZE="-1">STDIO</font> environment might. 

 If you need non-ASCII characters in your source code, make it a <font SIZE="-1">UTF-8</font> encoded file and <tt>&quot;use utf8&quot;</tt>. 

 If you need to set the encoding for <font SIZE="-1">STDIN, STDOUT,</font> and <font SIZE="-1">STDERR,</font> for example based on the user's locale, <tt>&quot;use open&quot;</tt>.

<h3>What is the difference between :encoding and :utf8?</h3>

 Because <font SIZE="-1">UTF-8</font> is one of Perl's internal formats, you can often just skip the encoding or decoding step, and manipulate the <font SIZE="-1">UTF8</font> flag directly. 

 Instead of <tt>&quot;:encoding(UTF-8)&quot;</tt>, you can simply use <tt>&quot;:utf8&quot;</tt>, which skips the encoding step if the data was already represented as <font SIZE="-1">UTF8</font> internally. This is widely accepted as good behavior when you're writing, but it can be dangerous when reading, because it causes internal inconsistency when you have invalid byte sequences. Using <tt>&quot;:utf8&quot;</tt> for input can sometimes result in security breaches, so please use <tt>&quot;:encoding(UTF-8)&quot;</tt> instead. 

 Instead of <tt>&quot;decode&quot;</tt> and <tt>&quot;encode&quot;</tt>, you could use <tt>&quot;_utf8_on&quot;</tt> and <tt>&quot;_utf8_off&quot;</tt>, but this is considered bad style. Especially <tt>&quot;_utf8_on&quot;</tt> can be dangerous, for the same reason that <tt>&quot;:utf8&quot;</tt> can. 

 There are some shortcuts for oneliners; see -C in perlrun.

<h3>What's the difference between UTF-8 and utf8?</h3>

 <tt>&quot;UTF-8&quot;</tt> is the official standard. <tt>&quot;utf8&quot;</tt> is Perl's way of being liberal in what it accepts. If you have to communicate with things that aren't so liberal, you may want to consider using <tt>&quot;UTF-8&quot;</tt>. If you have to communicate with things that are too liberal, you may have to use <tt>&quot;utf8&quot;</tt>. The full explanation is in ``<font SIZE="-1">UTF-8</font> vs. utf8 vs. <font SIZE="-1">UTF8''</font> in Encode. 

 <tt>&quot;UTF-8&quot;</tt> is internally known as <tt>&quot;utf-8-strict&quot;</tt>. The tutorial uses <font SIZE="-1">UTF-8</font> consistently, even where utf8 is actually used internally, because the distinction can be hard to make, and is mostly irrelevant. 

 For example, utf8 can be used for code points that don't exist in Unicode, like 9999999, but if you encode that to <font SIZE="-1">UTF-8,</font> you get a substitution character (by default; see ``Handling Malformed Data'' in Encode for more ways of dealing with this.) 

 Okay, if you insist: the ``internal format'' is utf8, not <font SIZE="-1">UTF-8.</font> (When it's not some other encoding.)

<h3>I lost track; what encoding is the internal format really?</h3>

 It's good that you lost track, because you shouldn't depend on the internal format being any specific encoding. But since you asked: by default, the internal format is either <font SIZE="-1">ISO-8859-1</font> (latin-1), or utf8, depending on the history of the string. On <font SIZE="-1">EBCDIC</font> platforms, this may be different even. 

 Perl knows how it stored the string internally, and will use that knowledge when you <tt>&quot;encode&quot;</tt>. In other words: don't try to find out what the internal encoding for a certain string is, but instead just encode it into the encoding that you want.

<h2>AUTHOR</h2>

 Juerd Waalboer &lt;#####@juerd.nl&gt;

<h2>SEE ALSO</h2>

 perlunicode, perluniintro, Encode 

<h2>Index</h2>



<dt><a HREF="#lbAU">INTERNALS</a>
<dd>


<dt><a HREF="#lbBB">AUTHOR</a>
<dd>
<dt><a HREF="#lbBC">SEE ALSO</a>
<dd></dl>
