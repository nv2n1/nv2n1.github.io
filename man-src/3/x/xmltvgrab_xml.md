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
<p>This module helps to write grabbers which fetch pages in XMLTV format from some website and output the data. It is not used for grabbers which scrape human-readable sites. </p>
<p> It consists of several class methods (package methods). The way to use it is to subclass it and override some of these.</p>
<h2>Methods</h2>
<dl COMPACT>
<dt>XMLTV::Grab_XML-&gt;<i>date_init()</i></dt>
<dd>Called at the start of the program to set up Date::Manip. You might want to override this with a method that sets the timezone.</dd>
<dt>XMLTV::Grab_XML-&gt;<i>urls_by_date()</i></dt>
<dd>Returns a hash mapping YYYYMMDD dates to a URL where listings for that date can be downloaded. This method is abstract, you must override it. </dd>
<p> Arguments: the command line options for &#8211;config-file and &#8211;quiet.</p>
<dt>XMLTV::Grab_XML-&gt;xml_from_data(data)</dt>
<dd>Given page data for a particular day, turn it into XML.  The default implementation just returns the data unchanged, but you might override it if you need to decompress the data or patch it up.</dd>
<dt>XMLTV::Grab_XML-&gt;<i>configure()</i></dt>
<dd>Configure the grabber if needed. Arguments are &#8211;config-file option (or undef) and &#8211;quiet flag (or undef). </dd>
<p> This method is not provided in the base class; if you don&#8217;t provide it then attempts to &#8211;configure will give a message that configuration is not necessary.</p>
<dt>XMLTV::Grab_XML-&gt;nextday(day)</dt>
<dd>Bump a YYYYMMDD date by one. You probably shouldn&#8217;t override this.</dd>
<dt>XMLTV::Grab_XML-&gt;<i>country()</i></dt>
<dd>Return the name of the country you&#8217;re grabbing for, used in usage messages. Abstract.</dd>
<dt>XMLTV::Grab_XML-&gt;<i>usage_msg()</i></dt>
<dd>Return a command-line usage message. This calls <tt>&quot;country()&quot;</tt>, so you probably need to override only that method.</dd>
<dt>XMLTV::Grab_XML-&gt;<i>get()</i></dt>
<dd>Given a URL, fetch the content at that URL.  The default implementation calls <i>XMLTV::Get_nice::get_nice()</i> but you might want to override it if you need to do wacky things with http requests, like cookies. </dd>
<p> Note that while this method fetches a page, <tt>&quot;xml_from_data()&quot;</tt> does any further processing of the result to turn it into XML.</p>
<dt>XMLTV::Grab_XML-&gt;<i>go()</i></dt>
<dd>The main program. Parse command line options, fetch and write data. </dd>
<p> Most of the options are fairly self-explanatory but this routine also calls the XMLTV::Memoize module to look for a <code>&#8211;cache</code> argument. The functions memoized are those given by the <tt>&quot;cachables()&quot;</tt> method.</p>
<dt>XMLTV::Grab_XML-&gt;<i>cachables()</i></dt>
<dd>Returns a list of names of functions which could reasonably be memoized between runs. This will normally be whatever function fetches the web pages &#8211; you memoize that to save on repeated downloads. A subclass might want to add things to this list if it has its own way of fetching web pages.</dd>
<dt>XMLTV::Grab_XML-&gt;<i>remove_early_stop_times()</i></dt>
<dd>Checks each stop time and removes it if it&#8217;s before the start time. </dd>
<p> Argument: the XML to correct Returns: the corrected XML</dl>
<h2>Author</h2>
<p>Ed Avis, ed [at] membled.com</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="/docs/linux/man/3-xmltv/">XMLTV</a></i><i></i>(3).</p>
</p>