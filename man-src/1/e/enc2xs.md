---

title: "enc2xs(1)"
name: "enc2xs"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enc2xs/"
description: "enc2xs — Perl Encode Module Generator"
---

<pre><code>  enc2xs -[options]
  enc2xs -M ModName mapfiles...
  enc2xs -C
</code></pre>
<p> <i>enc2xs</i> builds a Perl extension for use by Encode from either Unicode Character Mapping files (.ucm) or Tcl Encoding Files (.enc). Besides being used internally during the build process of the Encode module, you can use <i>enc2xs</i> to add your own encoding to perl. No knowledge of <font SIZE="-1">XS</font> is necessary.  </p>
<h2>Quick Guide</h2>
<p> If you want to know as little about Perl as possible but need to add a new encoding, just read this chapter and forget the rest. </p>
<dl>
<dt>0.</dt>
<dd> <p> Have a .ucm file ready. You can get it from somewhere or you can write your own from scratch or you can grab one from the Encode distribution and customize it. For the <font SIZE="-1">UCM</font> format, see the next Chapter. In the example below, I&#8217;ll call my theoretical encoding myascii, defined in <i>my.ucm</i>. <code>&quot;$&quot;</code> is a shell prompt. </p>
<pre><code>  $ ls -F
  my.ucm
</code></pre>
 </dd>
<dt>1.</dt>
<dd> <p> Issue a command as follows; </p>
<pre><code>  $ enc2xs -M My my.ucm
  generating Makefile.PL
  generating My.pm
  generating README
  generating Changes
</code></pre>
<p> Now take a look at your current directory. It should look like this. </p>
<pre><code>  $ ls -F
  Makefile.PL My.pm my.ucm t/
</code></pre>
<p> The following files were created. </p>
<pre><code>  Makefile.PL - MakeMaker script
  My.pm - Encode submodule
  t/My.t - test file
</code></pre>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>1.1.</dt>
<dd> <p> If you want *.ucm installed together with the modules, do as follows; </p>
<pre><code>  $ mkdir Encode
  $ mv *.ucm Encode
  $ enc2xs -M My Encode/*ucm
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>2.</dt>
<dd> <p> Edit the files generated. You don&#8217;t have to if you have no time <font SIZE="-1">AND</font> no intention to give it to someone else. But it is a good idea to edit the pod and to add more tests. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Now issue a command all Perl Mongers love: </p>
<pre><code>  $ perl Makefile.PL
  Writing Makefile for Encode::My
</code></pre>
 </dd>
<dt>4.</dt>
<dd> <p> Now all you have to do is make. </p>
<pre><code>  $ make
  cp My.pm blib/lib/Encode/My.pm
  /usr/local/bin/perl /usr/local/bin/enc2xs -Q -O \
    -o encode_t.c -f encode_t.fnm
  Reading myascii (myascii)
  Writing compiled form
  128 bytes in string tables
  384 bytes (75%) saved spotting duplicates
  1 bytes (0.775%) saved using substrings
  ....
  chmod 644 blib/arch/auto/Encode/My/My.bs
  $
</code></pre>
<p> The time it takes varies depending on how fast your machine is and how large your encoding is. Unless you are working on something big like euc-tw, it won&#8217;t take too long. </p>
 </dd>
<dt>5.</dt>
<dd> <p> You can ``make install&#8217;&#8216; already but you should test first. </p>
<pre><code>  $ make test
  PERL_DL_NONLAZY=1 /usr/local/bin/perl -Iblib/arch -Iblib/lib \
    -e 'use Test::Harness qw(&amp;runtests $verbose); \
    $verbose=0; runtests @ARGV;' t/*.t
  t/My....ok
  All tests successful.
  Files=1, Tests=2, 0 wallclock secs
   ( 0.09 cusr + 0.01 csys = 0.09 CPU)
</code></pre>
 </dd>
<dt>6.</dt>
<dd> <p> If you are content with the test result, just ``make install&#8217;&#8216; </p>
 </dd>
<dt>7.</dt>
<dd> <p> If you want to add your encoding to Encode&#8217;s demand-loading list (so you don&#8217;t have to ``use Encode::YourEncoding&#8217;&#8216;), run </p>
<pre><code>  enc2xs -C
</code></pre>
<p> to update Encode::ConfigLocal, a module that controls local settings. After that, ``use Encode;&#8216;&#8216; is enough to load your encodings on demand. </p>
 </dd></dl>
<h2>The Unicode Character Map</h2>
<p> Encode uses the Unicode Character Map (<font SIZE="-1">UCM</font>) format for source character mappings. This format is used by <font SIZE="-1">IBM</font>&#8216;s <font SIZE="-1">ICU</font> package and was adopted by Nick Ing-Simmons for use with the Encode module. Since <font SIZE="-1">UCM</font> is more flexible than Tcl&#8217;s Encoding Map and far more user-friendly, this is the recommended format for Encode now. </p>
<p> A <font SIZE="-1">UCM</font> file looks like this. </p>
<pre><code>  #
  # Comments
  #
  &lt;code_set_name&gt; &quot;US-ascii&quot; # Required
  &lt;code_set_alias&gt; &quot;ascii&quot; # Optional
  &lt;mb_cur_min&gt; 1 # Required; usually 1
  &lt;mb_cur_max&gt; 1 # Max. # of bytes/char
  &lt;subchar&gt; \x3F # Substitution char
  #
  CHARMAP
  &lt;U0000&gt; \x00 |0 # &lt;control&gt;
  &lt;U0001&gt; \x01 |0 # &lt;control&gt;
  &lt;U0002&gt; \x02 |0 # &lt;control&gt;
  ....
  &lt;U007C&gt; \x7C |0 # VERTICAL LINE
  &lt;U007D&gt; \x7D |0 # RIGHT CURLY BRACKET
  &lt;U007E&gt; \x7E |0 # TILDE
  &lt;U007F&gt; \x7F |0 # &lt;control&gt;
  END CHARMAP
</code></pre>
<dl>
<dt>&bull;</dt>
<dd> <p> Anything that follows <code>&quot;#&quot;</code> is treated as a comment. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The header section continues until a line containing the word <font SIZE="-1">CHARMAP.</font> This section has a form of <i>&lt;keyword&gt; value</i>, one pair per line. Strings used as values must be quoted. Barewords are treated as numbers. <i>\xXX</i> represents a byte. </p>
<p> Most of the keywords are self-explanatory. <i>subchar</i> means substitution character, not subcharacter. When you decode a Unicode sequence to this encoding but no matching character is found, the byte sequence defined here will be used. For most cases, the value here is \x3F; in <font SIZE="-1">ASCII,</font> this is a question mark. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CHARMAP</font> starts the character map section. Each line has a form as follows: </p>
<pre><code>  &lt;UXXXX&gt; \xXX.. |0 # comment
    ^ ^ ^
    | | +- Fallback flag
    | +-------- Encoded byte sequence
    +-------------- Unicode Character ID in hex
</code></pre>
<p> The format is roughly the same as a header section except for the fallback flag: | followed by 0..3. The meaning of the possible values is as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>|0</dt>
<dd> <p> Round trip safe. A character decoded to Unicode encodes back to the same byte sequence. Most characters have this flag. </p>
 </dd>
<dt>|1</dt>
<dd> <p> Fallback for unicode -&gt; encoding. When seen, enc2xs adds this character for the encode map only. </p>
 </dd>
<dt>|2</dt>
<dd> <p> Skip sub-char mapping should there be no code point. </p>
 </dd>
<dt>|3</dt>
<dd> <p> Fallback for encoding -&gt; unicode. When seen, enc2xs adds this character for the decode map only. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> And finally, <font SIZE="-1">END OF CHARMAP</font> ends the section. </p>
 </dd></dl>
<p> When you are manually creating a <font SIZE="-1">UCM</font> file, you should copy ascii.ucm or an existing encoding which is close to yours, rather than write your own from scratch. </p>
<p> When you do so, make sure you leave at least <code>U0000</code> to <code>U0020</code> as is, unless your environment is <font SIZE="-1">EBCDIC.</font> </p>
<p> <font SIZE="-1"><code>CAVEAT</code></font>: not all features in <font SIZE="-1">UCM</font> are implemented. For example, icu:state is not used. Because of that, you need to write a perl module if you want to support algorithmical encodings, notably the <font SIZE="-1">ISO-2022</font> series. Such modules include Encode::JP::2022_JP, Encode::KR::2022_KR, and Encode::TW::HZ.  </p>
<h3>Coping with duplicate mappings</h3>
<p> When you create a map, you <font SIZE="-1">SHOULD</font> make your mappings round-trip safe. That is, <code>&quot;encode(&#8216;your-encoding&#8217;, decode(&#8216;your-encoding&#8217;, $data)) eq $data&quot;</code> stands for all characters that are marked as <code>&quot;|0&quot;</code>. Here is how to make sure: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Sort your map in Unicode order. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When you have a duplicate entry, mark either one with &#8216;|1&#8217; or &#8216;|3&#8217;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> And make sure the &#8216;|1&#8217; or &#8216;|3&#8217; entry <font SIZE="-1">FOLLOWS</font> the &#8216;|0&#8217; entry. </p>
 </dd></dl>
<p> Here is an example from big5-eten. </p>
<pre><code>  &lt;U2550&gt; \xF9\xF9 |0
  &lt;U2550&gt; \xA2\xA4 |3
</code></pre>
<p> Internally Encoding -&gt; Unicode and Unicode -&gt; Encoding Map looks like this; </p>
<pre><code>  E to U U to E
  --------------------------------------
  \xF9\xF9 =&gt; U2550 U2550 =&gt; \xF9\xF9
  \xA2\xA4 =&gt; U2550
</code></pre>
<p> So it is round-trip safe for \xF9\xF9. But if the line above is upside down, here is what happens. </p>
<pre><code>  E to U U to E
  --------------------------------------
  \xA2\xA4 =&gt; U2550 U2550 =&gt; \xF9\xF9
  (\xF9\xF9 =&gt; U2550 is now overwritten!)
</code></pre>
<p> The Encode package comes with <i>ucmlint</i>, a crude but sufficient utility to check the integrity of a <font SIZE="-1">UCM</font> file. Check under the Encode/bin directory for this. </p>
<p> When in doubt, you can use <i>ucmsort</i>, yet another utility under Encode/bin directory.  </p>
<h2>Bookmarks</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">ICU</font> Home Page &lt;<a rel="nofollow" href="http://www.icu-project.org/">http://www.icu-project.org/</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">ICU</font> Character Mapping Tables &lt;<a rel="nofollow" href="http://site.icu-project.org/charts/charset">http://site.icu-project.org/charts/charset</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ICU:Conversion Data &lt;<a rel="nofollow" href="http://www.icu-project.org/userguide/conversion-data.html">http://www.icu-project.org/userguide/conversion-data.html</a>&gt; </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> Encode, perlmod, perlpod </p>
