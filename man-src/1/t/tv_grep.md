---
title: "tv_grep(1)"
name: "tv_grep"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grep/"
description: "tv_grep – Filter programmes and channels from an XMLTV listings file."
---

<h2 class="name">NAME</h2>
<p> tv_grep &#8211; Filter programmes and channels from an XMLTV listings file. </p>
<h2>SYNOPSIS</h2>
<p> <tt>&quot;tv_grep [--help] [--output FILE] [--ignore-case|-i] (EXPR | REGEXP) [FILE...]&quot;</tt></p>
<h2>DESCRIPTION</h2>
<p> Reads <font SIZE="-1">XMLTV</font> listings data and writes out data containing some of the programmes and channels from the original. Which programmes and channels are left in the output is controlled by the regexp or Boolean expression given. </p>
<p> Simple usage is <code>tv_grep </code><font SIZE="-1"><code>REGEXP</code></font><code> [</code><font SIZE="-1"><code>FILE&#8230;</code></font><code>]</code>, where <font SIZE="-1"><code>REGEXP</code></font> is a Perl 5 regular expression (see <i><a href="/docs/linux/man/1-perlre/">perlre</a></i>(1)). This finds all &lt;programme&gt; elements containing text matching the regexp. The channels are left unchanged, that is, all the &lt;channel&gt; elements are output. </p>
<p> For more advanced searches, you can specify a Boolean expression (which loosely follows the style of <i><a href="/docs/linux/man/1-find/">find</a></i>(1)). There are many tests for matching programme content against a regular expression, a few for matching channels and programmes on those channels, and a few special tests.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;ignore-case</code>, <code>-i</code> treat all regular expression matches as case insensitive.</p>
<h2>EXPRESSIONS</h2>
<h3><font SIZE="-1">PROGRAMME CONTENT TESTS</font></h3>
<p> The tests for programme content match against particular attributes or subelements of the &lt;programme&gt; element in the <font SIZE="-1">XML</font> data. Each test is named the same as the attribute or element it matches. Those which take a regexp as an argument match if the programme contains at least one attribute or element of the same name whose content matches the regexp. Those which do not take a regexp match if the programme simply contains one or more attributes or elements of that name. </p>
<p> Some elements may or may not have content &#8211; they may just be empty. The regular expression &#8221; (the empty string) matches any element, even one with empty content, while a nonempty regular expression matches only those with content. </p>
<p> For example, <code>&#8211;desc Racing</code> matches a programme if the programme has at least one &lt;desc&gt; element whose content contains &#8216;Racing&#8217;. <code>&#8211;stop &#8221;</code> (the second argument is the empty string) matches a programme if the programme gives a stop time. </p>
<p> There are some elements where only yes/no matching is possible, where you cannot give a regexp to query the element&#8217;s content. For these the second <code>&#8221;</code> argument is mandatory. For example <code>&#8211;previously-shown &#8221;</code> will match programmes which have that element, but a test of <code>&#8211;previously-shown foo</code> will give an error because querying the content of previously-shown is not implemented. The additional empty-string argument is to leave room for future expansion. </p>
<p> The content tests are generated from the <font SIZE="-1">XMLTV</font> file format. The current set of programme content tests is: </p>
<p> <code>&#8211;audio</code> &#8221; </p>
<p> <code>&#8211;category</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;channel</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;clumpidx</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;country</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;credits</code> &#8221; </p>
<p> <code>&#8211;date</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;desc</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;episode-num</code> &#8221; </p>
<p> <code>&#8211;icon</code> &#8221; </p>
<p> <code>&#8211;keyword</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;language</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;last-chance</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;length</code> &#8221; </p>
<p> <code>&#8211;new</code> </p>
<p> <code>&#8211;orig-language</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;pdc-start</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;premiere</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;previously-shown</code> &#8221; </p>
<p> <code>&#8211;rating</code> &#8221; </p>
<p> <code>&#8211;showview</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;star-rating</code> &#8221; </p>
<p> <code>&#8211;start</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;stop</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;sub-title</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;subtitles</code> &#8221; </p>
<p> <code>&#8211;title</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;url</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;video</code> &#8221; </p>
<p> <code>&#8211;videoplus</code> <font SIZE="-1">REGEXP</font> </p>
<p> <code>&#8211;vps-start</code> <font SIZE="-1">REGEXP</font> </p>
<p> While every attribute and subelement of &lt;programme&gt; elements is included in the above list, for some of them it is normally more convenient to use the special tests described below.</p>
<h3><font SIZE="-1">CHANNEL TESTS</font></h3>
<p> There are two tests for channels. These filter both &lt;programme&gt; and &lt;channel&gt; elements: if a channel is filtered out then all programmes on that channel are too. </p>
<p> <code>&#8211;channel-name </code><font SIZE="-1"><code>REGEXP</code></font> True if the channel has a &lt;name&gt; whose content matches <font SIZE="-1">REGEXP.</font> </p>
<p> <code>&#8211;channel-id </code><font SIZE="-1"><code>CHANNEL_ID</code></font> True if the channel&#8217;s <font SIZE="-1">XMLTV</font> id is exactly equal to <font SIZE="-1">CHANNEL_ID.</font></p>
<h3><font SIZE="-1">TIME TESTS</font></h3>
<p> Normally you don&#8217;t want to test time strings with a regular expression but rather compare them with some other time. There are two tests for this. </p>
<p> <code>&#8211;on-after </code><font SIZE="-1"><code>DATE</code></font> True if the programme will be broadcast at or after <font SIZE="-1">DATE,</font> or will be part of the way through broadcasting at <font SIZE="-1">DATE. </font>(Note: a programme is considered to be broadcasting from its start time, up to but not including its stop time.) <font SIZE="-1">DATE</font> can be given in any sane date format; but if you don&#8217;t specify the timezone then <font SIZE="-1">UTC</font> is assumed. To remove all the programmes you have already missed, try <code>&#8211;on-after now</code>. </p>
<p> <code>&#8211;on-before </code><font SIZE="-1"><code>DATE</code></font> True if the programme will be broadcast wholly before <font SIZE="-1">DATE,</font> or if it will be part of the way through broadcasting at <font SIZE="-1">DATE. </font> To remove all the programmes that haven&#8217;t yet begun broadcasting, try <code>&#8211;on-before now</code>. You can use <code>&#8211;on-before</code> and <code>&#8211;on-after</code> together to find all programmes which are broadcasting at a certain time. </p>
<p> Another way of thinking about these two tests is that <code>&#8211;on-after now</code> gives &#8216;all programmes you could possibly still watch, although perhaps only catching the end&#8217;. <code>&#8211;on-before now</code> gives &#8216;all programmes you could possibly have seen, even if only the start&#8217;. </p>
<p> <code>&#8211;eval </code><font SIZE="-1"><code>CODE</code></font> Evaluate <font SIZE="-1">CODE</font> as Perl code, use the return value to decide whether to keep the programme. The Perl code will be given the programme data in <tt>$_</tt> in <font SIZE="-1">XMLTV</font>.pm hash format (see <font SIZE="-1">XMLTV</font>). The code can actually modify the programme passed in, which can be used for quick fixups. This option is not intended for normal use, but as an escape in case none of the existing tests is what you want. If you develop any useful bits of code, please submit them to be included as new tests.</p>
<h3><font SIZE="-1">LOGICAL OPERATORS</font></h3>
<p> <font SIZE="-1"><code>EXPR1</code></font><code> &#8211;and </code><font SIZE="-1"><code>EXPR2</code></font>, <font SIZE="-1"><code>EXPR1</code></font><code> -and </code><font SIZE="-1"><code>EXPR2</code></font>, <font SIZE="-1"><code>EXPR1 EXPR2</code></font> </p>
<p> <font SIZE="-1"><code>EXPR1</code></font><code> &#8211;or </code><font SIZE="-1"><code>EXPR2</code></font>, <font SIZE="-1"><code>EXPR1</code></font><code> -or </code><font SIZE="-1"><code>EXPR2</code></font> </p>
<p> <code>&#8211;not </code><font SIZE="-1"><code>EXPR</code></font>, <code>-not </code><font SIZE="-1"><code>EXPR</code></font>, <code>! </code><font SIZE="-1"><code>EXPR</code></font> </p>
<p> Of these, &#8216;not&#8217; binds tightest, affecting the following predicate only. &#8216;and&#8217; is next, and &#8216;or&#8217; binds loosest.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5), <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <font SIZE="-1"><i><a href="/docs/linux/man/3-xmltv/">XMLTV</a></i></font><i></i>(3).</p>
<h2>AUTHOR</h2>
<p> Ed Avis, ed [at] membled.com</p>
<h2>BUGS</h2>
<p> The &#8211;on-after test cannot be totally accurate when the input data did not give a stop time for a programme. In this case we assume the stop time is equal to the start time. This filters out more programmes than if the stop time were given. There will be a warning if this happens more than once on any single channel. It could be worthwhile to filter the listings data through <i><a href="/docs/linux/man/1-tv_sort/">tv_sort</a></i>(1) beforehand to add stop times. </p>
<p> Similar remarks apply to &#8211;on-before: if the stop time is missing we assume it is equal to the start time, and this can mean leaving in a programme which, if it had a stop time, would be removed. </p>
<p> The assumption of <font SIZE="-1">UTC</font> for dates without timezones could be considered a bug. Perhaps the user input should be interpreted according to the local timezone. <font SIZE="-1">OTOH,</font> if the data has no timezones and neither does the user input, then things will work as expected. </p>
<p> The simple usage is the only way to match against all a programme&#8217;s content because some things (like &lt;credits&gt;) do not have programme content tests defined. It actually works by stringifying the whole programme and regexp matching that, which means that it could give wrong results for regular expressions containing quote characters or some punctuation symbols. This is not particularly likely to happen in practice. </p>
<p> Some listings sources generate timeslots containing two or more programmes in succession. This is represented in <font SIZE="-1">XMLTV</font> with the &#8216;clumpidx&#8217; attribute. If tv_grep selects only some of the programmes from a clump, then it will alter the clumpidx of those remaining to make it consistent. This is maybe not ideal, perhaps the clumpidx should be left unchanged so it&#8217;s obvious that something is missing, but at least it prevents complaints from other <font SIZE="-1">XMLTV</font> tools about badly formed clumps. The clumpidx handling does mean that tv_grep is not always idempotent. </p>
<h2>Index</h2>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAL">AUTHOR</a></p>
<dd>
<dt><a href="#lbAM">BUGS</a></p>
<dd></dl>
