---
title: "xmltv(3)"
name: "xmltv"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmltv/"
description: "XMLTV – Perl extension to read and write TV listings in XMLTV format"
---

<p>XMLTV &#8211; Perl extension to read and write TV listings in XMLTV format </p>
<h2>Synopsis</h2>
<pre> use XMLTV;
 my $data = XMLTV::parsefile('tv.xml');
 my ($encoding, $credits, $ch, $progs) = @$data;
 my $langs = [ 'en', 'fr' ];
 print 'source of listings is: ', $credits-&gt;{'source-info-name'}, &quot;
&quot;
 if defined $credits-&gt;{'source-info-name'};
 foreach (values %$ch) {
 my ($text, $lang) = @{XMLTV::best_name($langs, $_-&gt;{'display-name'})};
 print &quot;channel $_-&gt;{id} has name $text
&quot;;
 print &quot;...in language $lang
&quot; if defined $lang;
 }
 foreach (@$progs) {
 print &quot;programme on channel $_-&gt;{channel} at time $_-&gt;{start}
&quot;;
 next if not defined $_-&gt;{desc};
 foreach (@{$_-&gt;{desc}}) {
 my ($text, $lang) = @$_;
 print &quot;has description $text
&quot;;
 print &quot;...in language $lang
&quot; if defined $lang;
 }
 }</pre>
<p>The value of <tt>$data</tt> will be something a bit like: </p>
<pre> [ 'UTF-8',
 { 'source-info-name' =&gt; 'Ananova', 'generator-info-name' =&gt; 'XMLTV' },
 { 'radio-4.bbc.co.uk' =&gt; { 'display-name' =&gt; [ [ 'en', 'BBC Radio 4' ],
 [ 'en', 'Radio 4' ],
 [ undef, '4' ] ],
 'id' =&gt; 'radio-4.bbc.co.uk' },
 ... },
 [ { start =&gt; '200111121800', title =&gt; [ [ 'Simpsons', 'en' ] ],
 channel =&gt; 'radio-4.bbc.co.uk' },
 ... ] ]</pre>
<h2>Description</h2>
<p>This module provides an interface to read and write files in <font SIZE="-1">XMLTV</font> format (a <font SIZE="-1">TV</font> listings format defined by xmltv.dtd). In general element names in the <font SIZE="-1">XML</font> correspond to hash keys in the Perl data structure. You can think of this module as a bit like <code>XML::Simple</code>, but specialized to the <font SIZE="-1">XMLTV</font> file format. </p>
<p> The Perl data structure corresponding to an <font SIZE="-1">XMLTV</font> file has four elements. The first gives the character encoding used for text data, typically <font SIZE="-1">UTF-8</font> or <font SIZE="-1">ISO-8859-1. </font>(The encoding value could also be undef meaning &#8216;unknown&#8217;, when the library can&#8217;t work out what it is.) The second element gives the attributes of the root &lt;tv&gt; element, which give information about the source of the <font SIZE="-1">TV</font> listings. The third element is a list of channels, each list element being a hash corresponding to one &lt;channel&gt; element. The fourth element is similarly a list of programmes. More details about the data structure are given later. The easiest way to find out what it looks like is to load some small <font SIZE="-1">XMLTV</font> files and use <code>Data::Dumper</code> to print out the resulting structure.</p>
<h2>Usage</h2>
<dl COMPACT>
<dt>parse(document)</p>
<dd>Takes an <font SIZE="-1">XMLTV</font> document (a string) and returns the Perl data structure. It is assumed that the document is valid <font SIZE="-1">XMLTV</font>; if not the routine may <i>die()</i> with an error (although the current implementation just warns and continues for most small errors). </p>
<p> The first element of the listref returned, the encoding, may vary according to the encoding of the input document, the versions of perl and <tt>&quot;XML::Parser&quot;</tt> installed, the configuration of the <font SIZE="-1">XMLTV</font> library and other factors including, but not limited to, the phase of the moon. With luck it should always be either the encoding of the input file or <font SIZE="-1">UTF-8.</font> </p>
<p> Attributes and elements in the <font SIZE="-1">XML</font> file whose names begin with &#8216;x-&#8216; are skipped silently. You can use these to include information which is not currently handled by the <font SIZE="-1">XMLTV</font> format, or by this module.</p>
<dt>parsefiles(filename&#8230;)</p>
<dd>Like <tt>&quot;parse()&quot;</tt> but takes one or more filenames instead of a string document. The data returned is the merging of those file contents: the programmes will be concatenated in their original order, the channels just put together in arbitrary order (ordering of channels should not matter). </p>
<p> It is necessary that each file have the same character encoding, if not, an exception is thrown. Ideally the credits information would also be the same between all the files, since there is no obvious way to merge it &#8211; but if the credits information differs from one file to the next, one file is picked arbitrarily to provide credits and a warning is printed. If two files give differing channel definitions for the same <font SIZE="-1">XMLTV</font> channel id, then one is picked arbitrarily and a warning is printed. </p>
<p> In the simple case, with just one file, you needn&#8217;t worry about mismatching of encodings, credits or channels. </p>
<p> The deprecated function <tt>&quot;parsefile()&quot;</tt> is a wrapper allowing just one filename.</p>
<dt>parse_callback(document, encoding_callback, credits_callback, channel_callback, programme_callback)</p>
<dd>An alternative interface. Whereas <tt>&quot;parse()&quot;</tt> reads the whole document and then returns a finished data structure, with this routine you specify a subroutine to be called as each &lt;channel&gt; element is read and another for each &lt;programme&gt; element. </p>
<p> The first argument is the document to parse. The remaining arguments are code references, one for each part of the document. </p>
<p> The callback for encoding will be called once with a string giving the encoding. In present releases of this module, it is also possible for the value to be undefined meaning &#8216;unknown&#8217;, but it&#8217;s hoped that future releases will always be able to figure out the encoding used. </p>
<p> The callback for credits will be called once with a hash reference. For channels and programmes, the appropriate function will be called zero or more times depending on how many channels / programmes are found in the file. </p>
<p> The four subroutines will be called in order, that is, the encoding and credits will be done before the channel handler is called and all the channels will be dealt with before the first programme handler is called. </p>
<p> If any of the code references is undef, nothing is called for that part of the file. </p>
<p> For backwards compatibility, if the value for &#8216;encoding callback&#8217; is not a code reference but a scalar reference, then the encoding found will be stored in that scalar. Similarly if the &#8216;credits callback&#8217; is a scalar reference, the scalar it points to will be set to point to the hash of credits. This style of interface is deprecated: new code should just use four callbacks. </p>
<p> For example: </p>
<pre> my $document = '&lt;tv&gt;...&lt;/tv&gt;';
 my $encoding;
 sub encoding_cb( $ ) { $encoding = shift }
 my $credits;
 sub credits_cb( $ ) { $credits = shift }
 # The callback for each channel populates this hash.
 my %channels;
 sub channel_cb( $ ) {
 my $c = shift;
 $channels{$c-&gt;{id}} = $c;
 }
 # The callback for each programme. We know that channels are
 # always read before programmes, so the %channels hash will be
 # fully populated.
 #
 sub programme_cb( $ ) {
 my $p = shift;
 print &quot;got programme: $p-&gt;{title}-&gt;[0]-&gt;[0]
&quot;;
 my $c = $channels{$p-&gt;{channel}};
 print 'channel name is: ', $c-&gt;{'display-name'}-&gt;[0]-&gt;[0], &quot;
&quot;;
 }
 # Let's go.
 XMLTV::parse_callback($document, \&amp;encoding_cb, \&amp;credits_cb,
 \&amp;channel_cb, \&amp;programme_cb);</pre>
<dt>parsefiles_callback(encoding_callback, credits_callback, channel_callback, programme_callback, filenames&#8230;)</p>
<dd>As <tt>&quot;parse_callback()&quot;</tt> but takes one or more filenames to open, merging their contents in the same manner as <tt>&quot;parsefiles()&quot;</tt>. Note that the reading is still gradual &#8211; you get the channels and programmes one at a time, as they are read. </p>
<p> Note that the same &lt;channel&gt; may be present in more than one file, so the channel callback will get called more than once. It&#8217;s your responsibility to weed out duplicate channel elements (since writing them out again requires that each have a unique id). </p>
<p> For compatibility, there is an alias <tt>&quot;parsefile_callback()&quot;</tt> which is the same but takes only a single filename, <code>before</code> the callback arguments. This is deprecated.</p>
<dt>write_data(data, options&#8230;)</p>
<dd>Takes a data structure and writes it as <font SIZE="-1">XML</font> to standard output. Any extra arguments are passed on to XML::Writer&#8217;s constructor, for example </p>
<pre> my $f = new IO::File '&gt;out.xml'; die if not $f;
 write_data($data, OUTPUT =&gt; $f);</pre>
<p>The encoding used for the output is given by the first element of the data. </p>
<p> Normally, there will be a warning for any Perl data which is not understood and cannot be written as <font SIZE="-1">XMLTV,</font> such as strange keys in hashes. But as an exception, any hash key beginning with an underscore will be skipped over silently. You can store &#8216;internal use only&#8217; data this way. </p>
<p> If a programme or channel hash contains a key beginning with &#8216;debug&#8217;, this key and its value will be written out as a comment inside the &lt;programme&gt; or &lt;channel&gt; element. This lets you include small debugging messages in the <font SIZE="-1">XML</font> output.</p>
<dt>best_name(languages, pairs [, comparator])</p>
<dd>The <font SIZE="-1">XMLTV</font> format contains many places where human-readable text is given an optional &#8216;lang&#8217; attribute, to allow mixed languages. This is represented in Perl as a pair [ text, lang ], although the second element may be missing or undef if the language is unknown. When several alernatives for an element (such as &lt;title&gt;) can be given, the representation is a list of [ text, lang ] pairs. Given such a list, what is the best text to use? It depends on the user&#8217;s preferred language. </p>
<p> This function takes a list of acceptable languages and a list of [string, language] pairs, and finds the best one to use. This means first finding the appropriate language and then picking the &#8216;best&#8217; string in that language. </p>
<p> The best is normally defined as the first one found in a usable language, since the <font SIZE="-1">XMLTV</font> format puts the most canonical versions first. But you can pass in your own comparison function, for example if you want to choose the shortest piece of text that is in an acceptable language. </p>
<p> The acceptable languages should be a reference to a list of language codes looking like &#8216;ru&#8217;, or like &#8216;de_DE&#8217;. The text pairs should be a reference to a list of pairs [ string, language ]. (As a special case if this list is empty or undef, that means no text is present, and the result is undef.) The third argument if present should be a cmp-style function that compares two strings of text and returns 1 if the first argument is better, -1 if the second better, 0 if they&#8217;re equally good. </p>
<p> Returns: [s, l] pair, where s is the best of the strings to use and l is its language. This pair is &#8216;live&#8217; &#8211; it is one of those from the list passed in. So you can use <tt>&quot;best_name()&quot;</tt> to find the best pair from a list and then modify the content of that pair. </p>
<p> (This routine depends on the <tt>&quot;Lingua::Preferred&quot;</tt> module being installed; if that module is missing then the first available language is always chosen.) </p>
<p> Example: </p>
<pre> my $langs = [ 'de', 'fr' ]; # German or French, please
 # Say we found the following under $p-&gt;{title} for a programme $p.
 my $pairs = [ [ 'La CitE des enfants perdus', 'fr' ],
 [ 'The City of Lost Children', 'en_US' ] ];
 my $best = best_name($langs, $pairs);
 print &quot;chose title $best-&gt;[0]
&quot;;</pre>
<dt><i>list_channel_keys()</i>, <i>list_programme_keys()</i></p>
<dd>Some users of this module may wish to enquire at runtime about which keys a programme or channel hash can contain. The data in the hash comes from the attributes and subelements of the corresponding element in the <font SIZE="-1">XML. </font> The values of attributes are simply stored as strings, while subelements are processed with a handler which may return a complex data structure. These subroutines returns a hash mapping key to handler name and multiplicity. This lets you know what data types can be expected under each key. For keys which come from attributes rather than subelements, the handler is set to &#8216;scalar&#8217;, just as for subelements which give a simple string. See &#8220;<font SIZE="-1">DATA STRUCTURE&#8221;</font> for details on what the different handler names mean. </p>
<p> It is not possible to find out which keys are mandatory and which optional, only a list of all those which might possibly be present. An example use of these routines is the tv_grep program, which creates its allowed command line arguments from the names of programme subelements.</p>
<dt>catfiles(w_args, filename&#8230;)</p>
<dd>Concatenate several listings files, writing the output to somewhere specified by <tt>&quot;w_args&quot;</tt>. Programmes are catenated together, channels are merged, for credits we just take the first and warn if the others differ. </p>
<p> The first argument is a hash reference giving information to pass to <tt>&quot;XMLTV::Writer&quot;</tt>&#8216;s constructor. But do not specify encoding, this will be taken from the input files. <tt>&quot;catfiles()&quot;</tt> will abort if the input files have different encodings, unless the &#8216;<font SIZE="-1">UTF8</font>&#8216;=1 argument is passed in.</p>
<dt>cat(data, &#8230;)</p>
<dd>Concatenate (and merge) listings data. Programmes are catenated together, channels are merged, for credits we just take the first and warn if the others differ (except that the &#8216;date&#8217; of the result is the latest date of all the inputs). </p>
<p> Whereas <tt>&quot;catfiles()&quot;</tt> reads and writes files, this function takes already-parsed listings data and returns some more listings data. It is much more memory-hungry.</p>
<dt>cat_noprogrammes</p>
<dd>Like <tt>&quot;cat()&quot;</tt> but ignores the programme data and just returns encoding, credits and channels. This is in case for scalability reasons you want to handle programmes individually, but still merge the smaller data.</dl>
<h2>Data Structure</h2>
<p>For completeness, we describe more precisely how channels and programmes are represented in Perl. Each element of the channels list is a hashref corresponding to one &lt;channel&gt; element, and likewise for programmes. The possible keys of a channel (programme) hash are the names of attributes or subelements of &lt;channel&gt; (&lt;programme&gt;). </p>
<p> The values for attributes are not processed in any way; an attribute <tt>&quot;fred=&quot;jim&quot;&quot;</tt> in the <font SIZE="-1">XML</font> will become a hash element with key <tt>'fred'</tt>, value <tt>'jim'</tt>. </p>
<p> But for subelements, there is further processing needed to turn the <font SIZE="-1">XML</font> content of a subelement into Perl data. What is done depends on what type of data is stored under that subelement. Also, if a certain element can appear several times then the hash key for that element points to a list of values rather than just one. </p>
<p> The conversion of a subelement&#8217;s content to and from Perl data is done by a handler. The most common handler is <i>with-lang</i>, used for human-readable text content plus an optional &#8216;lang&#8217; attribute. There are other handlers for other data structures in the file format. Often two subelements will share the same handler, since they hold the same type of data. The handlers defined are as follows; note that many of them will silently strip leading and trailing whitespace in element content. Look at the <font SIZE="-1">DTD</font> itself for an explanation of the whole file format. </p>
<p> Unless specified otherwise, it is not allowed for an element expected to contain text to have empty content, nor for the text to contain newline characters.</p>
<dl COMPACT>
<dt><i>credits</i></p>
<dd>Turns a list of credits (for director, actor, writer, etc.) into a hash mapping &#8216;role&#8217; to a list of names. The names in each role are kept in the same order.</p>
<dt><i>scalar</i></p>
<dd>Reads and writes a simple string as the content of the <font SIZE="-1">XML</font> element.</p>
<dt><i>length</i></p>
<dd>Converts the content of a &lt;length&gt; element into a number of seconds (so &lt;length units=&#8220;minutes&#8221;&gt;5&lt;/minutes&gt; would be returned as 300). On writing out again tries to convert a number of seconds to a time in minutes or hours if that would look better.</p>
<dt><i>episode-num</i></p>
<dd>The representation in Perl of <font SIZE="-1">XMLTV</font>&#8216;s odd episode numbers is as a pair of [ content, system ]. As specified by the <font SIZE="-1">DTD,</font> if the system is not given in the file then &#8216;onscreen&#8217; is assumed. Whitespace in the &#8216;xmltv_ns&#8217; system is unimportant, so on reading it is normalized to a single space on either side of each dot.</p>
<dt><i>video</i></p>
<dd>The &lt;video&gt; section is converted to a hash. The &lt;present&gt; subelement corresponds to the key &#8216;present&#8217; of this hash, &#8216;yes&#8217; and &#8216;no&#8217; are converted to Booleans. The same applies to &lt;colour&gt;. The content of the &lt;aspect&gt; subelement is stored under the key &#8216;aspect&#8217;. These keys can be missing in the hash just as the subelements can be missing in the <font SIZE="-1">XML.</font></p>
<dt><i>audio</i></p>
<dd>This is similar to <i>video</i>. &lt;present&gt; is a Boolean value, while the content of &lt;stereo&gt; is stored unchanged.</p>
<dt><i>previously-shown</i></p>
<dd>The &#8216;start&#8217; and &#8216;channel&#8217; attributes are converted to keys in a hash.</p>
<dt><i>presence</i></p>
<dd>The content of the element is ignored: it signfies something by its very presence. So the conversion from <font SIZE="-1">XML</font> to Perl is a constant true value whenever the element is found; the conversion from Perl to <font SIZE="-1">XML</font> is to write out the element if true, don&#8217;t write anything if false.</p>
<dt><i>subtitles</i></p>
<dd>The &#8216;type&#8217; attribute and the &#8216;language&#8217; subelement (both optional) become keys in a hash. But see <i>language</i> for what to pass as the value of that element.</p>
<dt><i>rating</i></p>
<dd>The rating is represented as a tuple of [ rating, system, icons ]. The last element is itself a listref of structures returned by the <i>icon</i> handler.</p>
<dt><i>star-rating</i></p>
<dd>In <font SIZE="-1">XML</font> this is a string &#8216;X/Y&#8217; plus a list of icons. In Perl represented as a pair [ rating, icons ] similar to <i>rating</i>. </p>
<p> Multiple star ratings are now supported. For backward compatability, you may specify a single [rating,icon] or the preferred double array [[rating,system,icon],[rating2,system2,icon2]] (like &#8216;ratings&#8217;)</p>
<dt><i>icon</i></p>
<dd>An icon in <font SIZE="-1">XMLTV</font> files is like the &lt;img&gt; element in <font SIZE="-1">HTML. </font> It is represented in Perl as a hashref with &#8216;src&#8217; and optionally &#8216;width&#8217; and &#8216;height&#8217; keys.</p>
<dt><i>with-lang</i></p>
<dd>In <font SIZE="-1">XML</font> something like title can be either &lt;title&gt;Foo&lt;/title&gt; or &lt;title lang=&#8220;en&#8221;&gt;Foo&lt;/title&gt;. In Perl these are stored as [ &#8216;Foo&#8217; ] and [ &#8216;Foo&#8217;, &#8216;en&#8217; ]. For the former [ &#8216;Foo&#8217;, undef ] would also be okay. </p>
<p> This handler also has two modifiers which may be added to the name after &#8216;/&#8217;. <i>/e</i> means that empty text is allowed, and will be returned as the empty tuple [], to mean that the element is present but has no text. When writing with <i>/e</i>, undef will also be understood as present-but-empty. You cannot however specify a language if the text is empty. </p>
<p> The modifier <i>/m</i> means that the text is allowed to span multiple lines. </p>
<p> So for example <i>with-lang/em</i> is a handler for text with language, where the text may be empty and may contain newlines. Note that the <i>with-lang-or-empty</i> of earlier releases has been replaced by <i>with-lang/e</i>.</dl>
<p> Now, which handlers are used for which subelements (keys) of channels and programmes? And what is the multiplicity (should you expect a single value or a list of values)? </p>
<p> The following tables map subelements of &lt;channel&gt; and of &lt;programme&gt; to the handlers used to read and write them. Many elements have their own handler with the same name, and most of the others use <i>with-lang</i>. The third column specifies the multiplicity of the element: <code>*</code> (any number) will give a list of values in Perl, <code>+</code> (one or more) will give a nonempty list, <code>?</code> (maybe one) will give a scalar, and <code>1</code> (exactly one) will give a scalar which is not undef.</p>
<h3>Handlers for &lt;channel&gt;</h3>
<dl COMPACT>
<dt>display-name, <i>with-lang</i>, <code>+</code></p>
<dd>
<dt>icon, <i>icon</i>, <code>*</code></p>
<dd>
<dt>url, <i>scalar</i>, <code>*</code></p>
<dd></dl>
<h3>Handlers for &lt;programme&gt;</h3>
<dl COMPACT>
<dt>title, <i>with-lang</i>, <code>+</code></p>
<dd>
<dt>sub-title, <i>with-lang</i>, <code>*</code></p>
<dd>
<dt>desc, <i>with-lang/m</i>, <code>*</code></p>
<dd>
<dt>credits, <i>credits</i>, <code>?</code></p>
<dd>
<dt>date, <i>scalar</i>, <code>?</code></p>
<dd>
<dt>category, <i>with-lang</i>, <code>*</code></p>
<dd>
<dt>keyword, <i>with-lang</i>, <code>*</code></p>
<dd>
<dt>language, <i>with-lang</i>, <code>?</code></p>
<dd>
<dt>orig-language, <i>with-lang</i>, <code>?</code></p>
<dd>
<dt>length, <i>length</i>, <code>?</code></p>
<dd>
<dt>icon, <i>icon</i>, <code>*</code></p>
<dd>
<dt>url, <i>scalar</i>, <code>*</code></p>
<dd>
<dt>country, <i>with-lang</i>, <code>*</code></p>
<dd>
<dt>episode-num, <i>episode-num</i>, <code>*</code></p>
<dd>
<dt>video, <i>video</i>, <code>?</code></p>
<dd>
<dt>audio, <i>audio</i>, <code>?</code></p>
<dd>
<dt>previously-shown, <i>previously-shown</i>, <code>?</code></p>
<dd>
<dt>premiere, <i>with-lang/em</i>, <code>?</code></p>
<dd>
<dt>last-chance, <i>with-lang/em</i>, <code>?</code></p>
<dd>
<dt>new, <i>presence</i>, <code>?</code></p>
<dd>
<dt>subtitles, <i>subtitles</i>, <code>*</code></p>
<dd>
<dt>rating, <i>rating</i>, <code>*</code></p>
<dd>
<dt>star-rating, <i>star-rating</i>, <code>*</code></p>
<dd></dl>
<p> At present, no parsing or validation on dates is done because dates may be partially specified in <font SIZE="-1">XMLTV. </font> For example &#8216;2001&#8217; means that the year is known but not the month, day or time of day. Maybe in the future dates will be automatically converted to and from <code>Date::Manip</code> objects. For now they just use the <i>scalar</i> handler. Similar remarks apply to URLs.</p>
<h2>Writing</h2>
<p>When reading a file you have the choice of using <tt>&quot;parse()&quot;</tt> to gulp the whole file and return a data structure, or using <tt>&quot;parse_callback()&quot;</tt> to get the programmes one at a time, although channels and other data are still read all at once. </p>
<p> There is a similar choice when writing data: the <tt>&quot;write_data()&quot;</tt> routine prints a whole <font SIZE="-1">XMLTV</font> document at once, but if you want to write an <font SIZE="-1">XMLTV</font> document incrementally you can manually create an <tt>&quot;XMLTV::Writer&quot;</tt> object and call methods on it. Synopsis: </p>
<pre> use XMLTV;
 my $w = new XMLTV::Writer();
 $w-&gt;comment(&quot;Hello from XML::Writer's comment() method&quot;);
 $w-&gt;start({ 'generator-info-name' =&gt; 'Example code in pod' });
 my %ch = (id =&gt; 'test-channel', 'display-name' =&gt; [ [ 'Test', 'en' ] ]);
 $w-&gt;write_channel(\%ch);
 my %prog = (channel =&gt; 'test-channel', start =&gt; '200203161500',
 title =&gt; [ [ 'News', 'en' ] ]);
 $w-&gt;write_programme(\%prog);
 $w-&gt;end();</pre>
<p>XMLTV::Writer inherits from XML::Writer, and provides the following extra or overridden methods:</p>
<dl COMPACT>
<dt><i>new()</i>, the constructor</p>
<dd>Creates an XMLTV::Writer object and starts writing an <font SIZE="-1">XMLTV</font> file, printing the <font SIZE="-1">DOCTYPE</font> line. Arguments are passed on to XML::Writer&#8217;s constructor, except for the following: </p>
<p> the &#8216;encoding&#8217; key if present gives the <font SIZE="-1">XML</font> character encoding. For example: </p>
<pre> my $w = new XMLTV::Writer(encoding =&gt; 'ISO-8859-1');</pre>
<p>If encoding is not specified, XML::Writer&#8217;s default is used (currently <font SIZE="-1">UTF-8</font>). </p>
<p> XMLTW::Writer can also filter out specific days from the data. This is useful if the datasource provides data for periods of time that does not match the days that the user has asked for. The filtering is controlled with the days, offset and cutoff arguments: </p>
<pre> my $w = new XMLTV::Writer(
 offset =&gt; 1,
 days =&gt; 2,
 cutoff =&gt; &quot;050000&quot; );</pre>
<p>In this example, XMLTV::Writer will discard all entries that do not have starttimes larger than or equal to 05:00 tomorrow and less than 05:00 two days after tomorrow. The time offset is stripped off the starttime before the comparison is made.</p>
<dt><i>start()</i></p>
<dd>Write the start of the &lt;tv&gt; element. Parameter is a hashref which gives the attributes of this element.</p>
<dt><i>write_channels()</i></p>
<dd>Write several channels at once. Parameter is a reference to a hash mapping channel id to channel details. They will be written sorted by id, which is reasonable since the order of channels in an <font SIZE="-1">XMLTV</font> file isn&#8217;t significant.</p>
<dt><i>write_channel()</i></p>
<dd>Write a single channel. You can call this routine if you want, but most of the time <tt>&quot;write_channels()&quot;</tt> is a better interface.</p>
<dt><i>write_programme()</i></p>
<dd>Write details for a single programme as <font SIZE="-1">XML.</font></p>
<dt><i>end()</i></p>
<dd>Say you&#8217;ve finished writing programmes. This ends the &lt;tv&gt; element and the file.</dl>
<h2>Author</h2>
<p>Ed Avis, ed [at] membled.com</p>
<h2>See Also</h2>
<p>The file format is defined by the <font SIZE="-1">DTD</font> xmltv.dtd, which is included in the xmltv package along with this module. It should be installed in your system&#8217;s standard place for <font SIZE="-1">SGML</font> and <font SIZE="-1">XML</font> DTDs. </p>
<p> The xmltv package has a web page at &lt;<a rel="nofollow" href="http://xmltv.org/">http://xmltv.org/</a>&gt; which carries information about the file format and the various tools and apps which are distributed with this module.</p>
