---
title: "perluniintro(1)"
name: "perluniintro"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perluniintro/"
description: "perluniintro – Perl Unicode introduction"
---
<h2>DESCRIPTION</h2>
<p> This document gives a general idea of Unicode and how to use Unicode in Perl. See ``Further Resources&#8217;&#8216; for references to more in-depth treatments of Unicode.  </p>
<h3>Unicode</h3>
<p> Unicode is a character set standard which plans to codify all of the writing systems of the world, plus many other symbols. </p>
<p> Unicode and <font SIZE="-1">ISO/IEC 10646</font> are coordinated standards that unify almost all other modern character set standards, covering more than 80 writing systems and hundreds of languages, including all commercially-important modern languages. All characters in the largest Chinese, Japanese, and Korean dictionaries are also encoded. The standards will eventually cover almost all characters in more than 250 writing systems and thousands of languages. Unicode 1.0 was released in October 1991, and 6.0 in October 2010. </p>
<p> A Unicode <i>character</i> is an abstract entity. It is not bound to any particular integer width, especially not to the C language <code>&quot;char&quot;</code>. Unicode is language-neutral and display-neutral: it does not encode the language of the text, and it does not generally define fonts or other graphical layout details. Unicode operates on characters and on text built from those characters. </p>
<p> Unicode defines characters like <code>&quot;LATIN CAPITAL LETTER A&quot;</code> or <code>&quot;GREEK SMALL LETTER ALPHA&quot;</code> and unique numbers for the characters, in this case 0x0041 and 0x03B1, respectively. These unique numbers are called <i>code points</i>. A code point is essentially the position of the character within the set of all possible Unicode characters, and thus in Perl, the term <i>ordinal</i> is often used interchangeably with it. </p>
<p> The Unicode standard prefers using hexadecimal notation for the code points. If numbers like <code>0x0041</code> are unfamiliar to you, take a peek at a later section, ``Hexadecimal Notation&#8217;&#8216;. The Unicode standard uses the notation <code>&quot;U+0041 LATIN CAPITAL LETTER A&quot;</code>, to give the hexadecimal code point and the normative name of the character. </p>
<p> Unicode also defines various <i>properties</i> for the characters, like ``uppercase&#8217;&#8216; or ``lowercase&#8217;&#8216;, ``decimal digit&#8217;&#8216;, or ``punctuation&#8217;&#8216;; these properties are independent of the names of the characters. Furthermore, various operations on the characters like uppercasing, lowercasing, and collating (sorting) are defined. </p>
<p> A Unicode <i>logical</i> ``character&#8217;&#8216; can actually consist of more than one internal <i>actual</i> ``character&#8217;&#8216; or code point. For Western languages, this is adequately modelled by a <i>base character</i> (like <code>&quot;LATIN CAPITAL LETTER A&quot;</code>) followed by one or more <i>modifiers</i> (like <code>&quot;COMBINING ACUTE ACCENT&quot;</code>). This sequence of base character and modifiers is called a <i>combining character sequence</i>. Some non-western languages require more complicated models, so Unicode created the <i>grapheme cluster</i> concept, which was later further refined into the <i>extended grapheme cluster</i>. For example, a Korean Hangul syllable is considered a single logical character, but most often consists of three actual Unicode characters: a leading consonant followed by an interior vowel followed by a trailing consonant. </p>
<p> Whether to call these extended grapheme clusters ``characters&#8217;&#8216; depends on your point of view. If you are a programmer, you probably would tend towards seeing each element in the sequences as one unit, or ``character&#8217;&#8216;. However from the user&#8217;s point of view, the whole sequence could be seen as one ``character&#8217;&#8216; since that&#8217;s probably what it looks like in the context of the user&#8217;s language. In this document, we take the programmer&#8217;s point of view: one ``character&#8217;&#8216; is one Unicode code point. </p>
<p> For some combinations of base character and modifiers, there are <i>precomposed</i> characters. There is a single character equivalent, for example, for the sequence <code>&quot;LATIN CAPITAL LETTER A&quot;</code> followed by <code>&quot;COMBINING ACUTE ACCENT&quot;</code>. It is called <code>&quot;LATIN CAPITAL LETTER A WITH ACUTE&quot;</code>. These precomposed characters are, however, only available for some combinations, and are mainly meant to support round-trip conversions between Unicode and legacy standards (like <font SIZE="-1">ISO 8859</font>). Using sequences, as Unicode does, allows for needing fewer basic building blocks (code points) to express many more potential grapheme clusters. To support conversion between equivalent forms, various <i>normalization forms</i> are also defined. Thus, <code>&quot;LATIN CAPITAL LETTER A WITH ACUTE&quot;</code> is in <i>Normalization Form Composed</i>, (abbreviated <font SIZE="-1">NFC</font>), and the sequence <code>&quot;LATIN CAPITAL LETTER A&quot;</code> followed by <code>&quot;COMBINING ACUTE ACCENT&quot;</code> represents the same character in <i>Normalization Form Decomposed</i> (<font SIZE="-1">NFD</font>). </p>
<p> Because of backward compatibility with legacy encodings, the ``a unique number for every character&#8217;&#8216; idea breaks down a bit: instead, there is ``at least one number for every character&#8217;&#8216;. The same character could be represented differently in several legacy encodings. The converse is not true: some code points do not have an assigned character. Firstly, there are unallocated code points within otherwise used blocks. Secondly, there are special Unicode control characters that do not represent true characters. </p>
<p> When Unicode was first conceived, it was thought that all the world&#8217;s characters could be represented using a 16-bit word; that is a maximum of <code>0x10000</code> (or 65,536) characters would be needed, from <code>0x0000</code> to <code>0xFFFF</code>. This soon proved to be wrong, and since Unicode 2.0 (July 1996), Unicode has been defined all the way up to 21 bits (<code>0x10FFFF</code>), and Unicode 3.1 (March 2001) defined the first characters above <code>0xFFFF</code>. The first <code>0x10000</code> characters are called the <i>Plane 0</i>, or the <i>Basic Multilingual Plane</i> (<font SIZE="-1">BMP</font>). With Unicode 3.1, 17 (yes, seventeen) planes in all were defined---but they are nowhere near full of defined characters, yet. </p>
<p> When a new language is being encoded, Unicode generally will choose a <code>&quot;block&quot;</code> of consecutive unallocated code points for its characters. So far, the number of code points in these blocks has always been evenly divisible by 16. Extras in a block, not currently needed, are left unallocated, for future growth. But there have been occasions when a later release needed more code points than the available extras, and a new block had to allocated somewhere else, not contiguous to the initial one, to handle the overflow. Thus, it became apparent early on that ``block&#8217;&#8216; wasn&#8217;t an adequate organizing principle, and so the <code>&quot;Script&quot;</code> property was created. (Later an improved script property was added as well, the <code>&quot;Script_Extensions&quot;</code> property.) Those code points that are in overflow blocks can still have the same script as the original ones. The script concept fits more closely with natural language: there is <code>&quot;Latin&quot;</code> script, <code>&quot;Greek&quot;</code> script, and so on; and there are several artificial scripts, like <code>&quot;Common&quot;</code> for characters that are used in multiple scripts, such as mathematical symbols. Scripts usually span varied parts of several blocks. For more information about scripts, see ``Scripts&#8217;&#8216; in perlunicode. The division into blocks exists, but it is almost completely accidental---an artifact of how the characters have been and still are allocated. (Note that this paragraph has oversimplified things for the sake of this being an introduction. Unicode doesn&#8217;t really encode languages, but the writing systems for them---their scripts; and one script can be used by many languages. Unicode also encodes things that aren&#8217;t really about languages, such as symbols like <code>&quot;BAGGAGE CLAIM&quot;</code>.) </p>
<p> The Unicode code points are just abstract numbers. To input and output these abstract numbers, the numbers must be <i>encoded</i> or <i>serialised</i> somehow. Unicode defines several <i>character encoding forms</i>, of which <i></i><font SIZE="-1"><i>UTF-8</i></font><i></i> is the most popular. <font SIZE="-1">UTF-8</font> is a variable length encoding that encodes Unicode characters as 1 to 4 bytes. Other encodings include <font SIZE="-1">UTF-16</font> and <font SIZE="-1">UTF-32</font> and their big- and little-endian variants (<font SIZE="-1">UTF-8</font> is byte-order independent). The <font SIZE="-1">ISO/IEC 10646</font> defines the <font SIZE="-1">UCS-2</font> and <font SIZE="-1">UCS-4</font> encoding forms. </p>
<p> For more information about encodings---for instance, to learn what <i>surrogates</i> and <i>byte order marks</i> (BOMs) are---see perlunicode.  </p>
<h3>Perl's Unicode Support</h3>
<p> Starting from Perl v5.6.0, Perl has had the capacity to handle Unicode natively. Perl v5.8.0, however, is the first recommended release for serious Unicode work. The maintenance release 5.6.1 fixed many of the problems of the initial Unicode implementation, but for example regular expressions still do not work with Unicode in 5.6.1. Perl v5.14.0 is the first release where Unicode support is (almost) seamlessly integrable without some gotchas. (There are a few exceptions. Firstly, some differences in quotemeta were fixed starting in Perl 5.16.0. Secondly, some differences in the range operator were fixed starting in Perl 5.26.0. Thirdly, some differences in split were fixed started in Perl 5.28.0.) </p>
<p> To enable this seamless support, you should <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code> (which is automatically selected if you <code>&quot;use 5.012&quot;</code> or higher). See feature. (5.14 also fixes a number of bugs and departures from the Unicode standard.) </p>
<p> Before Perl v5.8.0, the use of <code>&quot;use utf8&quot;</code> was used to declare that operations in the current block or file would be Unicode-aware. This model was found to be wrong, or at least clumsy: the ``Unicodeness&#8217;&#8216; is now carried with the data, instead of being attached to the operations. Starting with Perl v5.8.0, only one case remains where an explicit <code>&quot;use utf8&quot;</code> is needed: if your Perl script itself is encoded in <font SIZE="-1">UTF-8,</font> you can use <font SIZE="-1">UTF-8</font> in your identifier names, and in string and regular expression literals, by saying <code>&quot;use utf8&quot;</code>. This is not the default because scripts with legacy 8-bit data in them would break. See utf8.  </p>
<h3>Perl's Unicode Model</h3>
<p> Perl supports both pre-5.6 strings of eight-bit native bytes, and strings of Unicode characters. The general principle is that Perl tries to keep its data as eight-bit bytes for as long as possible, but as soon as Unicodeness cannot be avoided, the data is transparently upgraded to Unicode. Prior to Perl v5.14.0, the upgrade was not completely transparent (see ``The &#8216;&#8216;Unicode Bug&quot;&quot; in perlunicode), and for backwards compatibility, full transparency is not gained unless <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code> (see feature) or <code>&quot;use 5.012&quot;</code> (or higher) is selected. </p>
<p> Internally, Perl currently uses either whatever the native eight-bit character set of the platform (for example Latin-1) is, defaulting to <font SIZE="-1">UTF-8,</font> to encode Unicode strings. Specifically, if all code points in the string are <code>0xFF</code> or less, Perl uses the native eight-bit character set. Otherwise, it uses <font SIZE="-1">UTF-8.</font> </p>
<p> A user of Perl does not normally need to know nor care how Perl happens to encode its internal strings, but it becomes relevant when outputting Unicode strings to a stream without a PerlIO layer (one with the ``default&#8217;&#8216; encoding). In such a case, the raw bytes used internally (the native character set or <font SIZE="-1">UTF-8,</font> as appropriate for each string) will be used, and a ``Wide character&#8217;&#8216; warning will be issued if those strings contain a character beyond 0x00FF. </p>
<p> For example, </p>
<pre><code>      perl -e 'print &quot;\x{DF}\n&quot;, &quot;\x{0100}\x{DF}\n&quot;'
</code></pre>
<p> produces a fairly useless mixture of native bytes and <font SIZE="-1">UTF-8,</font> as well as a warning: </p>
<pre><code>     Wide character in print at ...
</code></pre>
<p> To output <font SIZE="-1">UTF-8,</font> use the <code>&quot;:encoding&quot;</code> or <code>&quot;:utf8&quot;</code> output layer. Prepending </p>
<pre><code>      binmode(STDOUT, &quot;:utf8&quot;);
</code></pre>
<p> to this sample program ensures that the output is completely <font SIZE="-1">UTF-8,</font> and removes the program&#8217;s warning. </p>
<p> You can enable automatic UTF-8-ification of your standard file handles, default <code>&quot;open()&quot;</code> layer, and <code>@ARGV</code> by using either the <code>&quot;-C&quot;</code> command line switch or the <code>&quot;PERL_UNICODE&quot;</code> environment variable, see perlrun for the documentation of the <code>&quot;-C&quot;</code> switch. </p>
<p> Note that this means that Perl expects other software to work the same way: if Perl has been led to believe that <font SIZE="-1">STDIN</font> should be <font SIZE="-1">UTF-8,</font> but then <font SIZE="-1">STDIN</font> coming in from another command is not <font SIZE="-1">UTF-8,</font> Perl will likely complain about the malformed <font SIZE="-1">UTF-8.</font> </p>
<p> All features that combine Unicode and I/O also require using the new PerlIO feature. Almost all Perl 5.8 platforms do use PerlIO, though: you can see whether yours is by running ``perl -V&#8217;&#8216; and looking for <code>&quot;useperlio=define&quot;</code>.  </p>
<font SIZE="-1"></font><h3>Unicode and EBCDIC</h3>
<p> Perl 5.8.0 added support for Unicode on <font SIZE="-1">EBCDIC</font> platforms. This support was allowed to lapse in later releases, but was revived in 5.22. Unicode support is somewhat more complex to implement since additional conversions are needed. See perlebcdic for more information. </p>
<p> On <font SIZE="-1">EBCDIC</font> platforms, the internal Unicode encoding form is UTF-EBCDIC instead of <font SIZE="-1">UTF-8.</font> The difference is that as <font SIZE="-1">UTF-8</font> is ``ASCII-safe&#8217;&#8216; in that <font SIZE="-1">ASCII</font> characters encode to <font SIZE="-1">UTF-8</font> as-is, while UTF-EBCDIC is ``EBCDIC-safe&#8217;&#8216;, in that all the basic characters (which includes all those that have <font SIZE="-1">ASCII</font> equivalents (like <code>&quot;A&quot;</code>, <code>&quot;0&quot;</code>, <code>&quot;%&quot;</code>, <i>etc.</i>) are the same in both <font SIZE="-1">EBCDIC</font> and UTF-EBCDIC. Often, documentation will use the term ``<font SIZE="-1">UTF-8&#8217;&#8216;</font> to mean UTF-EBCDIC as well. This is the case in this document.  </p>
<h3>Creating Unicode</h3>
<p> This section applies fully to Perls starting with v5.22. Various caveats for earlier releases are in the ``Earlier releases caveats&#8217;&#8216; subsection below. </p>
<p> To create Unicode characters in literals, use the <code>&quot;\N{...}&quot;</code> notation in double-quoted strings: </p>
<pre><code> my $smiley_from_name = &quot;\N{WHITE SMILING FACE}&quot;;
 my $smiley_from_code_point = &quot;\N{U+263a}&quot;;
</code></pre>
<p> Similarly, they can be used in regular expression literals </p>
<pre><code> $smiley =~ /\N{WHITE SMILING FACE}/;
 $smiley =~ /\N{U+263a}/;
</code></pre>
<p> At run-time you can use: </p>
<pre><code> use charnames ();
 my $hebrew_alef_from_name
                      = charnames::string_vianame(&quot;HEBREW LETTER ALEF&quot;);
 my $hebrew_alef_from_code_point = charnames::string_vianame(&quot;U+05D0&quot;);
</code></pre>
<p> Naturally, <code>&quot;ord()&quot;</code> will do the reverse: it turns a character into a code point. </p>
<p> There are other runtime options as well. You can use <code>&quot;pack()&quot;</code>: </p>
<pre><code> my $hebrew_alef_from_code_point = pack(&quot;U&quot;, 0x05d0);
</code></pre>
<p> Or you can use <code>&quot;chr()&quot;</code>, though it is less convenient in the general case: </p>
<pre><code> $hebrew_alef_from_code_point = chr(utf8::unicode_to_native(0x05d0));
 utf8::upgrade($hebrew_alef_from_code_point);
</code></pre>
<p> The <code>&quot;utf8::unicode_to_native()&quot;</code> and <code>&quot;utf8::upgrade()&quot;</code> aren&#8217;t needed if the argument is above 0xFF, so the above could have been written as </p>
<pre><code> $hebrew_alef_from_code_point = chr(0x05d0);
</code></pre>
<p> since 0x5d0 is above 255. </p>
<p> <code>&quot;\x{}&quot;</code> and <code>&quot;\o{}&quot;</code> can also be used to specify code points at compile time in double-quotish strings, but, for backward compatibility with older Perls, the same rules apply as with <code>&quot;chr()&quot;</code> for code points less than 256. </p>
<p> <code>&quot;utf8::unicode_to_native()&quot;</code> is used so that the Perl code is portable to <font SIZE="-1">EBCDIC</font> platforms. You can omit it if you&#8217;re <i>really</i> sure no one will ever want to use your code on a non-ASCII platform. Starting in Perl v5.22, calls to it on <font SIZE="-1">ASCII</font> platforms are optimized out, so there&#8217;s no performance penalty at all in adding it. Or you can simply use the other constructs that don&#8217;t require it. </p>
<p> See ``Further Resources&#8217;&#8216; for how to find all these names and numeric codes. </p>
<p> <i>Earlier releases caveats</i> </p>
<p> On <font SIZE="-1">EBCDIC</font> platforms, prior to v5.22, using <code>&quot;\N{U+...}&quot;</code> doesn&#8217;t work properly. </p>
<p> Prior to v5.16, using <code>&quot;\N{...}&quot;</code> with a character name (as opposed to a <code>&quot;U+...&quot;</code> code point) required a <code>&quot;use charnames :full&quot;</code>. </p>
<p> Prior to v5.14, there were some bugs in <code>&quot;\N{...}&quot;</code> with a character name (as opposed to a <code>&quot;U+...&quot;</code> code point). </p>
<p> <code>&quot;charnames::string_vianame()&quot;</code> was introduced in v5.14. Prior to that, <code>&quot;charnames::vianame()&quot;</code> should work, but only if the argument is of the form <code>&quot;U+...&quot;</code>. Your best bet there for runtime Unicode by character name is probably: </p>
<pre><code> use charnames ();
 my $hebrew_alef_from_name
                  = pack(&quot;U&quot;, charnames::vianame(&quot;HEBREW LETTER ALEF&quot;));
</code></pre>
<h3>Handling Unicode</h3>
<p> Handling Unicode is for the most part transparent: just use the strings as usual. Functions like <code>&quot;index()&quot;</code>, <code>&quot;length()&quot;</code>, and <code>&quot;substr()&quot;</code> will work on the Unicode characters; regular expressions will work on the Unicode characters (see perlunicode and perlretut). </p>
<p> Note that Perl considers grapheme clusters to be separate characters, so for example </p>
<pre><code> print length(&quot;\N{LATIN CAPITAL LETTER A}\N{COMBINING ACUTE ACCENT}&quot;),
       &quot;\n&quot;;
</code></pre>
<p> will print 2, not 1. The only exception is that regular expressions have <code>&quot;\X&quot;</code> for matching an extended grapheme cluster. (Thus <code>&quot;\X&quot;</code> in a regular expression would match the entire sequence of both the example characters.) </p>
<p> Life is not quite so transparent, however, when working with legacy encodings, I/O, and certain special cases:  </p>
<h3>Legacy Encodings</h3>
<p> When you combine legacy data and Unicode, the legacy data needs to be upgraded to Unicode. Normally the legacy data is assumed to be <font SIZE="-1">ISO 8859-1</font> (or <font SIZE="-1">EBCDIC,</font> if applicable). </p>
<p> The <code>&quot;Encode&quot;</code> module knows about many encodings and has interfaces for doing conversions between those encodings: </p>
<pre><code>    use Encode 'decode';
    $data = decode(&quot;iso-8859-3&quot;, $data); # convert from legacy
</code></pre>
<h3>Unicode I/O</h3>
<p> Normally, writing out Unicode data </p>
<pre><code>    print FH $some_string_with_unicode, &quot;\n&quot;;
</code></pre>
<p> produces raw bytes that Perl happens to use to internally encode the Unicode string. Perl&#8217;s internal encoding depends on the system as well as what characters happen to be in the string at the time. If any of the characters are at code points <code>0x100</code> or above, you will get a warning. To ensure that the output is explicitly rendered in the encoding you desire---and to avoid the warning---open the stream with the desired encoding. Some examples: </p>
<pre><code>    open FH, &quot;&gt;:utf8&quot;, &quot;file&quot;;
    open FH, &quot;&gt;:encoding(ucs2)&quot;, &quot;file&quot;;
    open FH, &quot;&gt;:encoding(UTF-8)&quot;, &quot;file&quot;;
    open FH, &quot;&gt;:encoding(shift_jis)&quot;, &quot;file&quot;;
</code></pre>
<p> and on already open streams, use <code>&quot;binmode()&quot;</code>: </p>
<pre><code>    binmode(STDOUT, &quot;:utf8&quot;);
    binmode(STDOUT, &quot;:encoding(ucs2)&quot;);
    binmode(STDOUT, &quot;:encoding(UTF-8)&quot;);
    binmode(STDOUT, &quot;:encoding(shift_jis)&quot;);
</code></pre>
<p> The matching of encoding names is loose: case does not matter, and many encodings have several aliases. Note that the <code>&quot;:utf8&quot;</code> layer must always be specified exactly like that; it is <i>not</i> subject to the loose matching of encoding names. Also note that currently <code>&quot;:utf8&quot;</code> is unsafe for input, because it accepts the data without validating that it is indeed valid <font SIZE="-1">UTF-8</font>; you should instead use <code>&quot;:encoding(UTF-8)&quot;</code> (with or without a hyphen). </p>
<p> See PerlIO for the <code>&quot;:utf8&quot;</code> layer, PerlIO::encoding and Encode::PerlIO for the <code>&quot;:encoding()&quot;</code> layer, and Encode::Supported for many encodings supported by the <code>&quot;Encode&quot;</code> module. </p>
<p> Reading in a file that you know happens to be encoded in one of the Unicode or legacy encodings does not magically turn the data into Unicode in Perl&#8217;s eyes. To do that, specify the appropriate layer when opening files </p>
<pre><code>    open(my $fh,'&lt;:encoding(UTF-8)', 'anything');
    my $line_of_unicode = &lt;$fh&gt;;
    open(my $fh,'&lt;:encoding(Big5)', 'anything');
    my $line_of_unicode = &lt;$fh&gt;;
</code></pre>
<p> The I/O layers can also be specified more flexibly with the <code>&quot;open&quot;</code> pragma. See open, or look at the following example. </p>
<pre><code>    use open ':encoding(UTF-8)'; # input/output default encoding will be
                                 # UTF-8
    open X, &quot;&gt;file&quot;;
    print X chr(0x100), &quot;\n&quot;;
    close X;
    open Y, &quot;&lt;file&quot;;
    printf &quot;%#x\n&quot;, ord(&lt;Y&gt;); # this should print 0x100
    close Y;
</code></pre>
<p> With the <code>&quot;open&quot;</code> pragma you can use the <code>&quot;:locale&quot;</code> layer </p>
<pre><code>    BEGIN { $ENV{LC_ALL} = $ENV{LANG} = 'ru_RU.KOI8-R' }
    # the :locale will probe the locale environment variables like
    # LC_ALL
    use open OUT =&gt; ':locale'; # russki parusski
    open(O, &quot;&gt;koi8&quot;);
    print O chr(0x430); # Unicode CYRILLIC SMALL LETTER A = KOI8-R 0xc1
    close O;
    open(I, &quot;&lt;koi8&quot;);
    printf &quot;%#x\n&quot;, ord(&lt;I&gt;), &quot;\n&quot;; # this should print 0xc1
    close I;
</code></pre>
<p> These methods install a transparent filter on the I/O stream that converts data from the specified encoding when it is read in from the stream. The result is always Unicode. </p>
<p> The open pragma affects all the <code>&quot;open()&quot;</code> calls after the pragma by setting default layers. If you want to affect only certain streams, use explicit layers directly in the <code>&quot;open()&quot;</code> call. </p>
<p> You can switch encodings on an already opened stream by using <code>&quot;binmode()&quot;</code>; see ``binmode&#8217;&#8216; in perlfunc. </p>
<p> The <code>&quot;:locale&quot;</code> does not currently work with <code>&quot;open()&quot;</code> and <code>&quot;binmode()&quot;</code>, only with the <code>&quot;open&quot;</code> pragma. The <code>&quot;:utf8&quot;</code> and <code>&quot;:encoding(...)&quot;</code> methods do work with all of <code>&quot;open()&quot;</code>, <code>&quot;binmode()&quot;</code>, and the <code>&quot;open&quot;</code> pragma. </p>
<p> Similarly, you may use these I/O layers on output streams to automatically convert Unicode to the specified encoding when it is written to the stream. For example, the following snippet copies the contents of the file ``text.jis&#8217;&#8216; (encoded as <font SIZE="-1">ISO-2022-JP,</font> aka <font SIZE="-1">JIS</font>) to the file ``text.utf8&#8217;&#8216;, encoded as <font SIZE="-1">UTF-8:</font> </p>
<pre><code>    open(my $nihongo, '&lt;:encoding(iso-2022-jp)', 'text.jis');
    open(my $unicode, '&gt;:utf8', 'text.utf8');
    while (&lt;$nihongo&gt;) { print $unicode $_ }
</code></pre>
<p> The naming of encodings, both by the <code>&quot;open()&quot;</code> and by the <code>&quot;open&quot;</code> pragma allows for flexible names: <code>&quot;koi8-r&quot;</code> and <code>&quot;KOI8R&quot;</code> will both be understood. </p>
<p> Common encodings recognized by <font SIZE="-1">ISO, MIME, IANA,</font> and various other standardisation organisations are recognised; for a more detailed list see Encode::Supported. </p>
<p> <code>&quot;read()&quot;</code> reads characters and returns the number of characters. <code>&quot;seek()&quot;</code> and <code>&quot;tell()&quot;</code> operate on byte counts, as does <code>&quot;sysseek()&quot;</code>. </p>
<p> <code>&quot;sysread()&quot;</code> and <code>&quot;syswrite()&quot;</code> should not be used on file handles with character encoding layers, they behave badly, and that behaviour has been deprecated since perl 5.24. </p>
<p> Notice that because of the default behaviour of not doing any conversion upon input if there is no default layer, it is easy to mistakenly write code that keeps on expanding a file by repeatedly encoding the data: </p>
<pre><code>    # BAD CODE WARNING
    open F, &quot;file&quot;;
    local $/; ## read in the whole file of 8-bit characters
    $t = &lt;F&gt;;
    close F;
    open F, &quot;&gt;:encoding(UTF-8)&quot;, &quot;file&quot;;
    print F $t; ## convert to UTF-8 on output
    close F;
</code></pre>
<p> If you run this code twice, the contents of the <i>file</i> will be twice <font SIZE="-1">UTF-8</font> encoded. A <code>&quot;use open &#8216;:encoding(UTF-8)&#8216;&quot;</code> would have avoided the bug, or explicitly opening also the <i>file</i> for input as <font SIZE="-1">UTF-8.</font> </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: the <code>&quot;:utf8&quot;</code> and <code>&quot;:encoding&quot;</code> features work only if your Perl has been built with PerlIO, which is the default on most systems.  </p>
<h3>Displaying Unicode As Text</h3>
<p> Sometimes you might want to display Perl scalars containing Unicode as simple <font SIZE="-1">ASCII</font> (or <font SIZE="-1">EBCDIC</font>) text. The following subroutine converts its argument so that Unicode characters with code points greater than 255 are displayed as <code>&quot;\x{...}&quot;</code>, control characters (like <code>&quot;\n&quot;</code>) are displayed as <code>&quot;\x..&quot;</code>, and the rest of the characters as themselves: </p>
<pre><code> sub nice_string {
        join(&quot;&quot;,
        map { $_ &gt; 255 # if wide character...
              ? sprintf(&quot;\\x{%04X}&quot;, $_) # \x{...}
              : chr($_) =~ /[[:cntrl:]]/ # else if control character...
                ? sprintf(&quot;\\x%02X&quot;, $_) # \x..
                : quotemeta(chr($_)) # else quoted or as themselves
        } unpack(&quot;W*&quot;, $_[0])); # unpack Unicode characters
   }
</code></pre>
<p> For example, </p>
<pre><code>   nice_string(&quot;foo\x{100}bar\n&quot;)
</code></pre>
<p> returns the string </p>
<pre><code>   'foo\x{0100}bar\x0A'
</code></pre>
<p> which is ready to be printed. </p>
<p> (<code>&quot;\\x{}&quot;</code> is used here instead of <code>&quot;\\N{}&quot;</code>, since it&#8217;s most likely that you want to see what the native values are.)  </p>
<h3>Special Cases</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Starting in Perl 5.28, it is illegal for bit operators, like <code>&quot;~&quot;</code>, to operate on strings containing code points above 255. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>vec()</code> function may produce surprising results if used on strings containing characters with ordinal values above 255. In such a case, the results are consistent with the internal encoding of the characters, but not with much else. So don&#8217;t do that, and starting in Perl 5.28, a deprecation message is issued if you do so, becoming illegal in Perl 5.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Peeking At Perl&#8217;s Internal Encoding </p>
<p> Normal users of Perl should never care how Perl encodes any particular Unicode string (because the normal ways to get at the contents of a string with Unicode---via input and output---should always be via explicitly-defined I/O layers). But if you must, there are two ways of looking behind the scenes. </p>
<p> One way of peeking inside the internal encoding of Unicode characters is to use <code>&quot;unpack(&quot;C*&quot;, ...&quot;</code> to get the bytes of whatever the string encoding happens to be, or <code>&quot;unpack(&quot;U0..&quot;, ...)&quot;</code> to get the bytes of the <font SIZE="-1">UTF-8</font> encoding: </p>
<pre><code>    # this prints c4 80 for the UTF-8 bytes 0xc4 0x80
    print join(&quot; &quot;, unpack(&quot;U0(H2)*&quot;, pack(&quot;U&quot;, 0x100))), &quot;\n&quot;;
</code></pre>
<p> Yet another way would be to use the Devel::Peek module: </p>
<pre><code>    perl -MDevel::Peek -e 'Dump(chr(0x100))'
</code></pre>
<p> That shows the <code>&quot;UTF8&quot;</code> flag in <font SIZE="-1">FLAGS</font> and both the <font SIZE="-1">UTF-8</font> bytes and Unicode characters in <code>&quot;PV&quot;</code>. See also later in this document the discussion about the <code>&quot;utf8::is_utf8()&quot;</code> function. </p>
 </dd></dl>
<h3>Advanced Topics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> String Equivalence </p>
<p> The question of string equivalence turns somewhat complicated in Unicode: what do you mean by ``equal&#8217;&#8216;? </p>
<p> (Is <code>&quot;LATIN CAPITAL LETTER A WITH ACUTE&quot;</code> equal to <code>&quot;LATIN CAPITAL LETTER A&quot;</code>?) </p>
<p> The short answer is that by default Perl compares equivalence (<code>&quot;eq&quot;</code>, <code>&quot;ne&quot;</code>) based only on code points of the characters. In the above case, the answer is no (because 0x00C1 != 0x0041). But sometimes, any <font SIZE="-1">CAPITAL LETTER A</font>&#8216;s should be considered equal, or even A&#8217;s of any case. </p>
<p> The long answer is that you need to consider character normalization and casing issues: see Unicode::Normalize, Unicode Technical Report #15, Unicode Normalization Forms &lt;<a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr15">http://www.unicode.org/unicode/reports/tr15</a>&gt; and sections on case mapping in the Unicode Standard &lt;<a rel="nofollow" href="http://www.unicode.org">http://www.unicode.org</a>&gt;. </p>
<p> As of Perl 5.8.0, the ``Full&#8217;&#8216; case-folding of <i>Case Mappings/SpecialCasing</i> is implemented, but bugs remain in <code>&quot;qr//i&quot;</code> with them, mostly fixed by 5.14, and essentially entirely by 5.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String Collation </p>
<p> People like to see their strings nicely sorted---or as Unicode parlance goes, collated. But again, what do you mean by collate? </p>
<p> (Does <code>&quot;LATIN CAPITAL LETTER A WITH ACUTE&quot;</code> come before or after <code>&quot;LATIN CAPITAL LETTER A WITH GRAVE&quot;</code>?) </p>
<p> The short answer is that by default, Perl compares strings (<code>&quot;lt&quot;</code>, <code>&quot;le&quot;</code>, <code>&quot;cmp&quot;</code>, <code>&quot;ge&quot;</code>, <code>&quot;gt&quot;</code>) based only on the code points of the characters. In the above case, the answer is ``after&#8217;&#8216;, since <code>0x00C1</code> &gt; <code>0x00C0</code>. </p>
<p> The long answer is that ``it depends&#8217;&#8216;, and a good answer cannot be given without knowing (at the very least) the language context. See Unicode::Collate, and <i>Unicode Collation Algorithm</i> &lt;<a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr10/">http://www.unicode.org/unicode/reports/tr10/</a>&gt; </p>
 </dd></dl>
<h3>Miscellaneous</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Character Ranges and Classes </p>
<p> Character ranges in regular expression bracketed character classes ( e.g., <code>&quot;/[a-z]/&quot;</code>) and in the <code>&quot;tr///&quot;</code> (also known as <code>&quot;y///&quot;</code>) operator are not magically Unicode-aware. What this means is that <code>&quot;[A-Za-z]&quot;</code> will not magically start to mean ``all alphabetic letters&#8217;&#8216; (not that it does mean that even for 8-bit characters; for those, if you are using locales (perllocale), use <code>&quot;/[[:alpha:]]/&quot;</code>; and if not, use the 8-bit-aware property <code>&quot;\p{alpha}&quot;</code>). </p>
<p> All the properties that begin with <code>&quot;\p&quot;</code> (and its inverse <code>&quot;\P&quot;</code>) are actually character classes that are Unicode-aware. There are dozens of them, see perluniprops. </p>
<p> Starting in v5.22, you can use Unicode code points as the end points of regular expression pattern character ranges, and the range will include all Unicode code points that lie between those end points, inclusive. </p>
<pre><code> qr/ [ \N{U+03} - \N{U+20} ] /xx
</code></pre>
<p> includes the code points <code>&quot;\N{U+03}&quot;</code>, <code>&quot;\N{U+04}&quot;</code>, ..., <code>&quot;\N{U+20}&quot;</code>. </p>
<p> This also works for ranges in <code>&quot;tr///&quot;</code> starting in Perl v5.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String-To-Number Conversions </p>
<p> Unicode does define several other decimal---and numeric---characters besides the familiar 0 to 9, such as the Arabic and Indic digits. Perl does not support string-to-number conversion for digits other than <font SIZE="-1">ASCII</font> <code>0</code> to <code>9</code> (and <font SIZE="-1">ASCII</font> <code>&quot;a&quot;</code> to <code>&quot;f&quot;</code> for hexadecimal). To get safe conversions from any Unicode string, use ``<code>num()</code>&#8216;&#8216; in Unicode::UCD. </p>
 </dd></dl>
<h3>Questions With Answers</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Will My Old Scripts Break? </p>
<p> Very probably not. Unless you are generating Unicode characters somehow, old behaviour should be preserved. About the only behaviour that has changed and which could start generating Unicode is the old behaviour of <code>&quot;chr()&quot;</code> where supplying an argument more than 255 produced a character modulo 255. <code>&quot;chr(300)&quot;</code>, for example, was equal to <code>&quot;chr(45)&quot;</code> or ``-&#8216;&#8216; (in <font SIZE="-1">ASCII</font>), now it is <font SIZE="-1">LATIN CAPITAL LETTER I WITH BREVE.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> How Do I Make My Scripts Work With Unicode? </p>
<p> Very little work should be needed since nothing changes until you generate Unicode data. The most important thing is getting input as Unicode; for that, see the earlier I/O discussion. To get full seamless Unicode support, add <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code> (or <code>&quot;use 5.012&quot;</code> or higher) to your script. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> How Do I Know Whether My String Is In Unicode? </p>
<p> You shouldn&#8217;t have to care. But you may if your Perl is before 5.14.0 or you haven&#8217;t specified <code>&quot;use feature &#8216;unicode_strings&#8217;&quot;</code> or <code>&quot;use 5.012&quot;</code> (or higher) because otherwise the rules for the code points in the range 128 to 255 are different depending on whether the string they are contained within is in Unicode or not. (See ``When Unicode Does Not Happen&#8217;&#8216; in perlunicode.) </p>
<p> To determine if a string is in Unicode, use: </p>
<pre><code>    print utf8::is_utf8($string) ? 1 : 0, &quot;\n&quot;;
</code></pre>
<p> But note that this doesn&#8217;t mean that any of the characters in the string are necessary <font SIZE="-1">UTF-8</font> encoded, or that any of the characters have code points greater than 0xFF (255) or even 0x80 (128), or that the string has any characters at all. All the <code>&quot;is_utf8()&quot;</code> does is to return the value of the internal ``utf8ness&#8217;&#8216; flag attached to the <code>$string</code>. If the flag is off, the bytes in the scalar are interpreted as a single byte encoding. If the flag is on, the bytes in the scalar are interpreted as the (variable-length, potentially multi-byte) <font SIZE="-1">UTF-8</font> encoded code points of the characters. Bytes added to a <font SIZE="-1">UTF-8</font> encoded string are automatically upgraded to <font SIZE="-1">UTF-8.</font> If mixed non-UTF-8 and <font SIZE="-1">UTF-8</font> scalars are merged (double-quoted interpolation, explicit concatenation, or printf/sprintf parameter substitution), the result will be <font SIZE="-1">UTF-8</font> encoded as if copies of the byte strings were upgraded to <font SIZE="-1">UTF-8:</font> for example, </p>
<pre><code>    $a = &quot;ab\x80c&quot;;
    $b = &quot;\x{100}&quot;;
    print &quot;$a = $b\n&quot;;
</code></pre>
<p> the output string will be UTF-8-encoded <code>&quot;ab\x80c = \x{100}\n&quot;</code>, but <code>$a</code> will stay byte-encoded. </p>
<p> Sometimes you might really need to know the byte length of a string instead of the character length. For that use the <code>&quot;bytes&quot;</code> pragma and the <code>&quot;length()&quot;</code> function: </p>
<pre><code>    my $unicode = chr(0x100);
    print length($unicode), &quot;\n&quot;; # will print 1
    use bytes;
    print length($unicode), &quot;\n&quot;; # will print 2
                                  # (the 0xC4 0x80 of the UTF-8)
    no bytes;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> How Do I Find Out What Encoding a File Has? </p>
<p> You might try Encode::Guess, but it has a number of limitations. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> How Do I Detect Data That&#8217;s Not Valid In a Particular Encoding? </p>
<p> Use the <code>&quot;Encode&quot;</code> package to try converting it. For example, </p>
<pre><code>    use Encode 'decode';
    if (eval { decode('UTF-8', $string, Encode::FB_CROAK); 1 }) {
        # $string is valid UTF-8
    } else {
        # $string is not valid UTF-8
    }
</code></pre>
<p> Or use <code>&quot;unpack&quot;</code> to try decoding it: </p>
<pre><code>    use warnings;
    @chars = unpack(&quot;C0U*&quot;, $string_of_bytes_that_I_think_is_utf8);
</code></pre>
<p> If invalid, a <code>&quot;Malformed UTF-8 character&quot;</code> warning is produced. The ``C0&#8217;&#8216; means ``process the string character per character&#8217;&#8216;. Without that, the <code>&quot;unpack(&quot;U*&quot;, ...)&quot;</code> would work in <code>&quot;U0&quot;</code> mode (the default if the format string starts with <code>&quot;U&quot;</code>) and it would return the bytes making up the <font SIZE="-1">UTF-8</font> encoding of the target string, something that will always work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> How Do I Convert Binary Data Into a Particular Encoding, Or Vice Versa? </p>
<p> This probably isn&#8217;t as useful as you might think. Normally, you shouldn&#8217;t need to. </p>
<p> In one sense, what you are asking doesn&#8217;t make much sense: encodings are for characters, and binary data are not ``characters&#8217;&#8216;, so converting ``data&#8217;&#8216; into some encoding isn&#8217;t meaningful unless you know in what character set and encoding the binary data is in, in which case it&#8217;s not just binary data, now is it? </p>
<p> If you have a raw sequence of bytes that you know should be interpreted via a particular encoding, you can use <code>&quot;Encode&quot;</code>: </p>
<pre><code>    use Encode 'from_to';
    from_to($data, &quot;iso-8859-1&quot;, &quot;UTF-8&quot;); # from latin-1 to UTF-8
</code></pre>
<p> The call to <code>&quot;from_to()&quot;</code> changes the bytes in <code>$data</code>, but nothing material about the nature of the string has changed as far as Perl is concerned. Both before and after the call, the string <code>$data</code> contains just a bunch of 8-bit bytes. As far as Perl is concerned, the encoding of the string remains as ``system-native 8-bit bytes&#8217;&#8216;. </p>
<p> You might relate this to a fictional &#8216;Translate&#8217; module: </p>
<pre><code>   use Translate;
   my $phrase = &quot;Yes&quot;;
   Translate::from_to($phrase, 'english', 'deutsch');
   ## phrase now contains &quot;Ja&quot;
</code></pre>
<p> The contents of the string changes, but not the nature of the string. Perl doesn&#8217;t know any more after the call than before that the contents of the string indicates the affirmative. </p>
<p> Back to converting data. If you have (or want) data in your system&#8217;s native 8-bit encoding (e.g. Latin-1, <font SIZE="-1">EBCDIC,</font> etc.), you can use pack/unpack to convert to/from Unicode. </p>
<pre><code>    $native_string = pack(&quot;W*&quot;, unpack(&quot;U*&quot;, $Unicode_string));
    $Unicode_string = pack(&quot;U*&quot;, unpack(&quot;W*&quot;, $native_string));
</code></pre>
<p> If you have a sequence of bytes you <code>know</code> is valid <font SIZE="-1">UTF-8,</font> but Perl doesn&#8217;t know it yet, you can make Perl a believer, too: </p>
<pre><code>    $Unicode = $bytes;
    utf8::decode($Unicode);
</code></pre>
<p> or: </p>
<pre><code>    $Unicode = pack(&quot;U0a*&quot;, $bytes);
</code></pre>
<p> You can find the bytes that make up a <font SIZE="-1">UTF-8</font> sequence with </p>
<pre><code>    @bytes = unpack(&quot;C*&quot;, $Unicode_string)
</code></pre>
<p> and you can create well-formed Unicode with </p>
<pre><code>    $Unicode_string = pack(&quot;U*&quot;, 0xff, ...)
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> How Do I Display Unicode? How Do I Input Unicode? </p>
<p> See &lt;<a rel="nofollow" href="http://www.alanwood.net/unicode/">http://www.alanwood.net/unicode/</a>&gt; and &lt;<a rel="nofollow" href="http://www.cl.cam.ac.uk/~mgk25/unicode.html">http://www.cl.cam.ac.uk/~mgk25/unicode.html</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> How Does Unicode Work With Traditional Locales? </p>
<p> If your locale is a <font SIZE="-1">UTF-8</font> locale, starting in Perl v5.26, Perl works well for all categories; before this, starting with Perl v5.20, it works for all categories but <code>&quot;LC_COLLATE&quot;</code>, which deals with sorting and the <code>&quot;cmp&quot;</code> operator. But note that the standard <code>&quot;Unicode::Collate&quot;</code> and <code>&quot;Unicode::Collate::Locale&quot;</code> modules offer much more powerful solutions to collation issues, and work on earlier releases. </p>
<p> For other locales, starting in Perl 5.16, you can specify </p>
<pre><code>    use locale ':not_characters';
</code></pre>
<p> to get Perl to work well with them. The catch is that you have to translate from the locale character set to/from Unicode yourself. See ``Unicode I/O&#8217;&#8216; above for how to </p>
<pre><code>    use open ':locale';
</code></pre>
<p> to accomplish this, but full details are in ``Unicode and <font SIZE="-1">UTF-8&#8217;&#8216;</font> in perllocale, including gotchas that happen if you don&#8217;t specify <code>&quot;:not_characters&quot;</code>. </p>
 </dd></dl>
<h3>Hexadecimal Notation</h3>
<p> The Unicode standard prefers using hexadecimal notation because that more clearly shows the division of Unicode into blocks of 256 characters. Hexadecimal is also simply shorter than decimal. You can use decimal notation, too, but learning to use hexadecimal just makes life easier with the Unicode standard. The <code>&quot;U+HHHH&quot;</code> notation uses hexadecimal, for example. </p>
<p> The <code>&quot;0x&quot;</code> prefix means a hexadecimal number, the digits are 0-9 <i>and</i> a-f (or A-F, case doesn&#8217;t matter). Each hexadecimal digit represents four bits, or half a byte. <code>&quot;print 0x..., &quot;\n&quot;&quot;</code> will show a hexadecimal number in decimal, and <code>&quot;printf &quot;%x\n&quot;, $decimal&quot;</code> will show a decimal number in hexadecimal. If you have just the ``hex digits&#8217;&#8216; of a hexadecimal number, you can use the <code>&quot;hex()&quot;</code> function. </p>
<pre><code>    print 0x0009, &quot;\n&quot;; # 9
    print 0x000a, &quot;\n&quot;; # 10
    print 0x000f, &quot;\n&quot;; # 15
    print 0x0010, &quot;\n&quot;; # 16
    print 0x0011, &quot;\n&quot;; # 17
    print 0x0100, &quot;\n&quot;; # 256
    print 0x0041, &quot;\n&quot;; # 65
    printf &quot;%x\n&quot;, 65; # 41
    printf &quot;%#x\n&quot;, 65; # 0x41
    print hex(&quot;41&quot;), &quot;\n&quot;; # 65
</code></pre>
<h3>Further Resources</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Unicode Consortium </p>
<p> &lt;<a rel="nofollow" href="http://www.unicode.org/">http://www.unicode.org/</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode <font SIZE="-1">FAQ</font> </p>
<p> &lt;<a rel="nofollow" href="http://www.unicode.org/unicode/faq/">http://www.unicode.org/unicode/faq/</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode Glossary </p>
<p> &lt;<a rel="nofollow" href="http://www.unicode.org/glossary/">http://www.unicode.org/glossary/</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode Recommended Reading List </p>
<p> The Unicode Consortium has a list of articles and books, some of which give a much more in depth treatment of Unicode: &lt;<a rel="nofollow" href="http://unicode.org/resources/readinglist.html">http://unicode.org/resources/readinglist.html</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode Useful Resources </p>
<p> &lt;<a rel="nofollow" href="http://www.unicode.org/unicode/onlinedat/resources.html">http://www.unicode.org/unicode/onlinedat/resources.html</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode and Multilingual Support in <font SIZE="-1">HTML,</font> Fonts, Web Browsers and Other Applications </p>
<p> &lt;<a rel="nofollow" href="http://www.alanwood.net/unicode/">http://www.alanwood.net/unicode/</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">UTF-8</font> and Unicode <font SIZE="-1">FAQ</font> for Unix/Linux </p>
<p> &lt;<a rel="nofollow" href="http://www.cl.cam.ac.uk/~mgk25/unicode.html">http://www.cl.cam.ac.uk/~mgk25/unicode.html</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Legacy Character Sets </p>
<p> &lt;<a rel="nofollow" href="http://www.czyborra.com/">http://www.czyborra.com/</a>&gt; &lt;<a rel="nofollow" href="http://www.eki.ee/letter/">http://www.eki.ee/letter/</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can explore various information from the Unicode data files using the <code>&quot;Unicode::UCD&quot;</code> module. </p>
 </dd></dl>
<h2>UNICODE IN OLDER PERLS</h2>
<p> If you cannot upgrade your Perl to 5.8.0 or later, you can still do some Unicode processing by using the modules <code>&quot;Unicode::String&quot;</code>, <code>&quot;Unicode::Map8&quot;</code>, and <code>&quot;Unicode::Map&quot;</code>, available from <font SIZE="-1">CPAN.</font> If you have the <font SIZE="-1">GNU</font> recode installed, you can also use the Perl front-end <code>&quot;Convert::Recode&quot;</code> for character conversions. </p>
<p> The following are fast conversions from <font SIZE="-1">ISO 8859-1</font> (Latin-1) bytes to <font SIZE="-1">UTF-8</font> bytes and back, the code works even with older Perl 5 versions. </p>
<pre><code>    # ISO 8859-1 to UTF-8
    s/([\x80-\xFF])/chr(0xC0|ord($1)&gt;&gt;6).chr(0x80|ord($1)&amp;0x3F)/eg;
    # UTF-8 to ISO 8859-1
    s/([\xC2\xC3])([\x80-\xBF])/chr(ord($1)&lt;&lt;6&amp;0xC0|ord($2)&amp;0x3F)/eg;
</code></pre>
<h2>SEE ALSO</h2>
<p> perlunitut, perlunicode, Encode, open, utf8, bytes, perlretut, perlrun, Unicode::Collate, Unicode::Normalize, Unicode::UCD  </p>
<h2>ACKNOWLEDGMENTS</h2>
<p> Thanks to the kind readers of the perl5-porters [at] perl.org, perl-unicode [at] perl.org, linux-utf8 [at] nl.linux.org, and unicore [at] unicode.org mailing lists for their valuable feedback.  </p>
<h2>AUTHOR, COPYRIGHT, AND LICENSE</h2>
<p> Copyright 2001-2011 Jarkko Hietaniemi &lt;jhi [at] iki.fi&gt;. Now maintained by Perl 5 Porters. </p>
<p> This document may be distributed under the same terms as Perl itself. </p>
