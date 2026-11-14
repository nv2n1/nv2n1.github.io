---
title: "smokeping_extend(7)"
name: "smokeping_extend"
section: "7"
letter: "s"
url: "/docs/linux/man/7-smokeping_extend/"
description: "smokeping_extend – Notes on extending Smokeping"
---

<p>smokeping_extend &#8211; Notes on extending Smokeping</p>
<h2>Overview</h2>
<p>This document is intended to guide prospective authors in writing new Smokeping probes. It mostly describes the interface between Smokeping and its probe modules. If it seems too complicated to understand, look at the existing modules for examples. </p>
<p> Comments and proposed changes or additions are welcome. Please send them to the smokeping-users mailing list. Patches against the <font SIZE="-1">POD</font> source of this document are most appreciated.</p>
<h2>Choosing A Base Class</h2>
<p>The first thing you should decide is which base class you should use for your probe. For most (if not all) uses it&#8217;s a choice between Smokeping::probes::base and Smokeping::probes::basefork. The former is intended for probes that can measure their targets all in one go, while the latter is for probing them one at a time, possibly in several concurrent subprocesses. </p>
<p> At the moment, the only probes that use <tt>&quot;Smokeping::probes::base&quot;</tt> are the FPing derivatives. All the others use <tt>&quot;Smokeping::probes::basefork&quot;</tt>, and chances are you should too. This document will thus concentrate on the latter case.</p>
<h2>Skeleton File</h2>
<p>The Smokeping::probes::skel module is a non-functional probe that is intended to make a good basis for a new probe module. Copy the file, <tt>&quot;lib/probes/skel.pm&quot;</tt>, to a new name and just fill out the blanks :) Note that the names of real probe modules must start with a capital letter.</p>
<h2>Probe Documentation</h2>
<p>The probe documentation is generated from the source code with the smokeping arguments <tt>&quot;--man&quot;</tt> or <tt>&quot;--makepod&quot;</tt>. The embedded <font SIZE="-1">POD</font> documentation should point to this real documentation, so that curious users of the <tt>&quot;perldoc&quot;</tt> command see what&#8217;s going on. All the current probes do this. </p>
<p> You should provide the method <tt>&quot;pod_hash&quot;</tt> that returns a reference to a hash with keys corresponding to the section names you want in the manpage. The supported section names are <tt>&quot;name&quot;</tt>, <tt>&quot;overview&quot;</tt>, <tt>&quot;description&quot;</tt>, <tt>&quot;authors&quot;</tt>, <tt>&quot;notes&quot;</tt>, <tt>&quot;bugs&quot;</tt>, and <tt>&quot;see_also&quot;</tt>. If you don&#8217;t need a particular section, just leave it out. </p>
<p> The special sections <tt>&quot;synopsis&quot;</tt> and <tt>&quot;variables&quot;</tt> are automatically generated from the description of your variables. See below. </p>
<p> Note that if you use &#8216;here documents&#8217; (&#8216;&lt;&lt;&#8216;) that have <font SIZE="-1">POD</font> markup inside, you should escape the markup so that it doesn&#8217;t show up in the embedded <font SIZE="-1">POD</font> documentation. Most probes do it like this: </p>
<pre> my $e = &quot;=&quot;;
 my $doc = &lt;&lt;DOC;
 ${e}head1 SECTION TITLE
 DOC</pre>
<h2>Probe Description</h2>
<p>The probe should offer the <tt>&quot;ProbeDesc&quot;</tt> method that returns a short description of what it does. This will be used in the graphs produced by the web frontend.</p>
<h2>Variables</h2>
<p>All Smokeping probes must define their variables by implementing a <tt>&quot;probevars&quot;</tt> method for probe-specific variables and a <tt>&quot;targetvars&quot;</tt> method for target-specific variables. If you don&#8217;t know the difference between these yet, see smokeping_examples. </p>
<p> (The probes that are derived from <tt>&quot;Smokeping::probes::base&quot;</tt> don&#8217;t support target-specific variables, so they only use the <tt>&quot;probevars&quot;</tt> method.) </p>
<p> The base classes offer these methods too to provide the variables that are common to all the probes (eg. the probe-specific <tt>&quot;step&quot;</tt> variable and the target-specific <tt>&quot;pings&quot;</tt> variable. If you don&#8217;t want to add anything to the base class variables (perhaps because all your variables are of a target-specific nature, so you don&#8217;t need new probe-specific variables at all), you can leave the corresponding method out and it will be inherited from the base class. </p>
<p> When you do supply your own <tt>&quot;probevars&quot;</tt> or <tt>&quot;targetvars&quot;</tt> method, you should combine your variables with those coming from the superclass. There is a convenience method called <tt>&quot;_makevars&quot;</tt> that does this, and the common idiom is </p>
<pre> sub probevars {
 my $class = shift;
 return $class-&gt;_makevars($class-&gt;SUPER::probevars, {
 # your variables go here
 }
 }</pre>
<p>The variables are declared in a syntax that comes from the module used for parsing the configuration file, <tt>&quot;Config::Grammar&quot;</tt>. Each variable should be a hash that uses the &#8220;special variable keys&#8221; documented in Config::Grammar. See <tt>&quot;Smokeping::probes::skel&quot;</tt> and the other probes for examples. </p>
<p> For reference, here are the keys the hash should have. Much of this is taken straight from the <tt>&quot;Config::Grammar&quot;</tt> manual.</p>
<dl>
<dt>Keys you <code>must</code> provide</p>
<dd>
<dl>
<dd>
<dl>
<dt>_doc</p>
<dd>Description of the variable.</p>
<dt>_example</p>
<dd>An example value. This will be used in the <font SIZE="-1">SYNOPSIS</font> section in the probe manual.</dl>
</dl>
<dl>
<dd></dl>
<dt>Optional keys</p>
<dd>
<dl>
<dd>
<dl>
<dt>_default</p>
<dd>A default value that will be assigned to the variable if none is specified or inherited.</p>
<dt>_re</p>
<dd>Regular expression upon which the value will be checked.</p>
<dt>_re_error</p>
<dd>String containing the returned error in case the regular expression doesn&#8217;t match (if not specified, a generic &#8216;syntax error&#8217; message will be returned).</p>
<dt>_sub</p>
<dd>A function pointer. It is called for every value, with the value passed as its first argument. If the function returns a defined value it is assumed that the test was not successful and an error is generated with the returned string as content.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<p> The <tt>&quot;probevars&quot;</tt> and <tt>&quot;targetvars&quot;</tt> methods should return hash references that contain the variable names as keys and the hashes described above as values. In addition the <tt>&quot;Config::Grammar&quot;</tt> special section key <tt>&quot;_mandatory&quot;</tt> is supported and should contain a reference to a list of mandatory variables. The <tt>&quot;_makevars&quot;</tt> method is aware of this special key and merges the mandatory lists in its arguments. Note that no other <tt>&quot;Config::Grammar&quot;</tt> special section keys are supported.</p>
<h2>Initialization</h2>
<p>If you must do something at probe initialization time, like check that the external program you&#8217;re going to use behaves as you expect, you should do it in the <tt>&quot;new&quot;</tt> method. You should probably also take care that you don&#8217;t run the tests needlessly while in <font SIZE="-1">CGI</font> mode. The usual way to do this is to test for <tt>$ENV</tt>{<font SIZE="-1">SERVER_SOFTWARE</font>}. See the <tt>&quot;Smokeping::probes::skel&quot;</tt> module for an example.</p>
<h2>Pinging</h2>
<p>All the real action happens in the <tt>&quot;pingone&quot;</tt> method (or, for <tt>&quot;Smokeping::probes::base&quot;</tt>-derived probes, in the <tt>&quot;ping&quot;</tt> method.) The arguments for <tt>&quot;pingone&quot;</tt> are <tt>$self</tt>, the module instance (since this is a method) and <tt>$target</tt>, the target to be probed. </p>
<p> You can access the probe-specific variables here via the <tt>&quot;$self-&gt;{properties}&quot;</tt> hash and the target-specific ones via the <tt>&quot;$target-&gt;{vars}&quot;</tt> hash. You get the number of pings needed for the target via the <tt>&quot;pings&quot;</tt> method: <tt>&quot;my $count = $self-&gt;pings($target)&quot;</tt>. </p>
<p> You should return a sorted array of the latency times measured. If a ping fails, don&#8217;t put anything in the array. </p>
<p> That&#8217;s it, you&#8217;re done!</p>
<h2>Example Configurations</h2>
<p>If you would like to provide a documented example configuration for your probe (in addition to the automatically generated <font SIZE="-1">SYNOPSIS</font> section in the probe manual), you can do so by adding it to the Smokeping::Examples module. Look for the &#8216;examples&#8217; subroutine and add your example there. </p>
<p> Future versions of Smokeping might provide a way to embed examples in the probe modules too. The author&#8217;s motivation for implementing this would be greatly increased by even a single demand for it, so please speak up if you think you&#8217;d use it.</p>
<h2>Timeout Handling</h2>
<p>If you deal with timeouts (for example because your program offers a parameter for specifying the timeout for the pings), you should know a few things. </p>
<p> First, there&#8217;s timeout logic in <tt>&quot;Smokeping::probes::basefork&quot;</tt> that kills the probe when the timeout is reached. By default the timeout is (# of pings * 5 seconds) + 1 second. If you expect that your pings can take longer, you should modify the default value of the probe-specific variable <tt>&quot;timeout&quot;</tt>. This would be done like this: </p>
<pre> sub probevars {
 my $class = shift;
 my $h = $class-&gt;SUPER::probevars;
 $h-&gt;{timeout}{_default} = 10; # override the superclass default
 return $class-&gt;_makevars($h, {
 # your variables go here
 }
 }</pre>
<p>If you want to provide a target-specific <tt>&quot;timeout&quot;</tt> setting, you should delete the probe-specific variable and be sure to provide a default for your target-specific one. See eg. <tt>&quot;Smokeping::probes::AnotherDNS&quot;</tt> for an example of how this is done. </p>
<p> Providing a target-specific <tt>&quot;timeout&quot;</tt> will make the timeout in <tt>&quot;Smokeping::probes::basefork&quot;</tt> be (# of pings * the maximum timeout of all targets) + 1 second. The 1 second is added so that the own timeout logic of the probe has time to kick in even in the worst case (ie. all pings are lost) before <tt>&quot;Smokeping::probes::basefork&quot;</tt> starts killing the processes.</p>
<h2>Copyright</h2>
<p>Copyright 2005 by Niko Tyni.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>Author</h2>
<p>Niko Tyni &lt;ntyni [at] iki.fi&gt;</p>
<h2>Bugs</h2>
<p>This document makes writing new probes look much harder than it really is.</p>
<h2>See Also</h2>
<p>The other Smokeping documents, especially smokeping_config. </p>
