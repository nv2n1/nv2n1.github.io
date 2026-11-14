---
title: "xmltvgrab_xml(3)"
name: "xmltvgrab_xml"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmltvgrab_xml/"
description: "XMLTV::Grab_XML – Perl extension to fetch raw XMLTV data from a site"
---

<p>XMLTV::Grab_XML &#8211; Perl extension to fetch raw XMLTV data from a site </p>
<h2>Synopsis</h2>
<pre> package Grab_XML_rur;
 use base 'XMLTV::Grab_XML';
 sub urls_by_date( $ ) { my $pkg = shift; ... }
 sub country( $ ) { my $pkg = shift; return 'Ruritania' }
 # Maybe override a couple of other methods as described below...
 Grab_XML_rur-&gt;go();</pre>
<h2>Description</h2>
<p>This module helps to write grabbers which fetch pages in <font SIZE="-1">XMLTV</font> format from some website and output the data. It is not used for grabbers which scrape human-readable sites. </p>
<p> It consists of several class methods (package methods). The way to use it is to subclass it and override some of these.</p>
<h2>Methods</h2>
<dl COMPACT>
<dt>XMLTV::Grab_XML-&gt;<i>date_init()</i></p>
<dd>Called at the start of the program to set up Date::Manip. You might want to override this with a method that sets the timezone.</p>
<dt>XMLTV::Grab_XML-&gt;<i>urls_by_date()</i></p>
<dd>Returns a hash mapping <font SIZE="-1">YYYYMMDD</font> dates to a <font SIZE="-1">URL</font> where listings for that date can be downloaded. This method is abstract, you must override it. </p>
<p> Arguments: the command line options for &#8211;config-file and &#8211;quiet.</p>
<dt>XMLTV::Grab_XML-&gt;xml_from_data(data)</p>
<dd>Given page data for a particular day, turn it into <font SIZE="-1">XML. </font> The default implementation just returns the data unchanged, but you might override it if you need to decompress the data or patch it up.</p>
<dt>XMLTV::Grab_XML-&gt;<i>configure()</i></p>
<dd>Configure the grabber if needed. Arguments are &#8211;config-file option (or undef) and &#8211;quiet flag (or undef). </p>
<p> This method is not provided in the base class; if you don&#8217;t provide it then attempts to &#8211;configure will give a message that configuration is not necessary.</p>
<dt>XMLTV::Grab_XML-&gt;nextday(day)</p>
<dd>Bump a <font SIZE="-1">YYYYMMDD</font> date by one. You probably shouldn&#8217;t override this.</p>
<dt>XMLTV::Grab_XML-&gt;<i>country()</i></p>
<dd>Return the name of the country you&#8217;re grabbing for, used in usage messages. Abstract.</p>
<dt>XMLTV::Grab_XML-&gt;<i>usage_msg()</i></p>
<dd>Return a command-line usage message. This calls <tt>&quot;country()&quot;</tt>, so you probably need to override only that method.</p>
<dt>XMLTV::Grab_XML-&gt;<i>get()</i></p>
<dd>Given a <font SIZE="-1">URL,</font> fetch the content at that <font SIZE="-1">URL. </font> The default implementation calls <i>XMLTV::Get_nice::get_nice()</i> but you might want to override it if you need to do wacky things with http requests, like cookies. </p>
<p> Note that while this method fetches a page, <tt>&quot;xml_from_data()&quot;</tt> does any further processing of the result to turn it into <font SIZE="-1">XML.</font></p>
<dt>XMLTV::Grab_XML-&gt;<i>go()</i></p>
<dd>The main program. Parse command line options, fetch and write data. </p>
<p> Most of the options are fairly self-explanatory but this routine also calls the XMLTV::Memoize module to look for a <code>&#8211;cache</code> argument. The functions memoized are those given by the <tt>&quot;cachables()&quot;</tt> method.</p>
<dt>XMLTV::Grab_XML-&gt;<i>cachables()</i></p>
<dd>Returns a list of names of functions which could reasonably be memoized between runs. This will normally be whatever function fetches the web pages &#8211; you memoize that to save on repeated downloads. A subclass might want to add things to this list if it has its own way of fetching web pages.</p>
<dt>XMLTV::Grab_XML-&gt;<i>remove_early_stop_times()</i></p>
<dd>Checks each stop time and removes it if it&#8217;s before the start time. </p>
<p> Argument: the <font SIZE="-1">XML</font> to correct Returns: the corrected <font SIZE="-1">XML</font></dl>
<h2>Author</h2>
<p>Ed Avis, ed [at] membled.com</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <font SIZE="-1"><i><a href="/docs/linux/man/3-xmltv/">XMLTV</a></i></font><i></i>(3).</p>
