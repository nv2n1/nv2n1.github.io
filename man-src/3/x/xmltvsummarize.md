---
title: "xmltvsummarize(3)"
name: "xmltvsummarize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmltvsummarize/"
---

XMLTV::Summarize - Perl extension to summarize XMLTV data 

<h2>Synopsis</h2><pre> # First get some data from the XMLTV module, eg:
 use XMLTV;
 my $data = XMLTV::parsefile('tv_sorted.xml');
 my ($encoding, $credits, $ch, $progs) = @$data;
 # Now turn the sorted programmes into a printable summary.
 use XMLTV::Summarize qw(summarize);
 foreach (summarize($ch, $progs)) {
 if (not ref) {
 print &quot;\nDay: $_\n\n&quot;;
 }
 else {
 my ($start, $stop, $title, $sub_title, $channel) = @$_;
 print &quot;programme starts at $start, &quot;;
 print &quot;stops at $stop, &quot; if defined $stop;
 print &quot;has title $title &quot;;
 print &quot;and episode title $sub_title&quot; if defined $sub_title;
 print &quot;, on channel $channel.\n&quot;;
 }
 }</pre><h2>Description</h2>This module processes programme and channel data from the <font SIZE="-1">XMLTV</font> module to help produce a human-readable summary or <font SIZE="-1">TV</font> guide. It takes care of choosing the correct language (based on the <font SIZE="-1">LANG</font> environment variable) and of looking up the name of channels from their id. 

 There is one public routine, <tt>&quot;summarize()&quot;</tt>. This takes (references to) a channels hash and a programmes list, the same format as those returned by the <font SIZE="-1">XMLTV</font> module. It returns a list of 'summary' elements where each element is a list of five items: start time, stop time, title, 'sub-title', and channel name. The stop time and sub-title may be undef. 

 The times are formatted as hh:mm, with a timezone appended when the timezone changes in the middle of listings. For the titles and channel name, the shortest string that is in an acceptable language is chosen. 

 The list of acceptable languages normally contains just one element, taken from <font SIZE="-1">LANG,</font> but you can set it manually as <tt>@XMLTV::Summarize::PREF_LANGS</tt> if wished.
<h2>Author</h2>Ed Avis, ed [at] membled.com
<h2>See Also</h2><font SIZE="-1"><i><a HREF="/docs/linux/man/1-xmltv/">XMLTV</a></i></font><i></i>(1).
