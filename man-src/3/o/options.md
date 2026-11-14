---
title: "options(3)"
name: "options"
section: "3"
letter: "o"
url: "/docs/linux/man/3-options/"
description: "XMLTV::Options – Command-line parsing for XMLTV grabbers"
---

<p>XMLTV::Options &#8211; Command-line parsing for XMLTV grabbers </p>
<h2>Description</h2>
<p>Utility library that implements command-line parsing and handles a lot of functionality that is common to all <font SIZE="-1">XMLTV</font> grabbers.</p>
<h2>Exported Functions</h2>
<p>All these functions are exported on demand.</p>
<h2>Usage</h2>
<dl COMPACT>
<dt><code>ParseOptions</code></p>
<dd>ParseOptions shall be called by a grabber to parse the command-line options supplied by the user. It takes a single hashref as a parameter. The entries in the hash configure the behaviour of ParseOptions. </p>
<pre> my( $opt, $conf ) = ParseOptions( {
 grabber_name =&gt; 'tv_grab_test',
 version =&gt; '$Id: Options.pm,v 1.28 2014/01/30 14:41:09 bilbo_uk Exp $',
 description =&gt; 'Sweden (tv.swedb.se)',
 capabilities =&gt; [qw/baseline manualconfig apiconfig lineups/],
 stage_sub =&gt; \&amp;config_stage,
 listchannels_sub =&gt; \&amp;list_channels,
 list_lineups_sub =&gt; \&amp;list_lineups,
 get_lineup_sub =&gt; \&amp;get_lineup,
 } );</pre>
<p>ParseOptions returns two hashrefs:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>A hashref with the values for all command-line options in the format returned by Getopt::Long (See &#8220;Storing options in a hash&#8221; in Getopt::Long). This includes both options that the grabber must handle as well as options that ParseOptions handles for the grabber.</p>
<dt>&bull;</p>
<dd>A hashref to the data loaded from the configuration file. See XMLTV::Configure for the format of <tt>$conf</tt>.</dl>
</dl>
<dl COMPACT>
<dd>ParseOptions handles the following options automatically without returning:</p>
<dl COMPACT>
<dt>&#8211;help</p>
<dd>
<dt>&#8211;info (or &#8211;man)</p>
<dd>
<dt>&#8211;capabilities</p>
<dd>
<dt>&#8211;version</p>
<dd>
<dt>&#8211;description</p>
<dd>
<dt>&#8211;preferredmethod</p>
<dd>Handled automatically if the preferredmethod capability has been set and the preferredmethod option has been specified in the call to ParseOptions.</dl>
</dl>
<dl COMPACT>
<dd>ParseOptions also takes care of the following options without returning, by calling the stage_sub, listchannels_sub, list_lineups_sub and get_lineup_sub callbacks supplied by the grabber:</p>
<dl COMPACT>
<dt>&#8211;configure</p>
<dd>
<dt>&#8211;configure-api</p>
<dd>
<dt>&#8211;stage</p>
<dd>
<dt>&#8211;list-channels</p>
<dd>
<dt>&#8211;list-lineups</p>
<dd>
<dt>&#8211;get-lineup</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd>ParseOptions will thus only return to the grabber when the grabber shall actually grab data. </p>
<p> If the &#8211;output option is specified, <font SIZE="-1">STDOUT</font> will be redirected to the specified file. </p>
<p> The grabber must check the following options on its own:</p>
<dl COMPACT>
<dt>&#8211;days</p>
<dd>
<dt>&#8211;offset</p>
<dd>
<dt>&#8211;quiet</p>
<dd>
<dt>&#8211;debug</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd>and any other options that are grabber specific. This can be done by reading <tt>$opt</tt>-&gt;{days} etc.</dl>
<dt><code>Changing the behaviour of ParseOptions</code></p>
<dd>The behaviour of ParseOptions can be influenced by passing named arguments in the hashref. The following arguments are supported:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>grabber_name</p>
<dd>Required. The name of the grabber (e.g. tv_grab_se_swedb). This is used when printing the synopsis.</p>
<dt>description</p>
<dd>Required. The description for the grabber. This is returned in response to the &#8211;description option and shall say which region the grabber returns data for. Examples: &#8220;Sweden&#8221;, or &#8220;Sweden (tv.swedb.se)&#8221; if there are several grabbers for a region or country).</p>
<dt>version</p>
<dd>Required. This shall be a cvs Id field.</p>
<dt>capabilities</p>
<dd>Required. The capabilities that the grabber shall support. Only capabilities that XMLTV::Options knows how to handle can be specified. Example: </p>
<pre> capabilities =&gt; [qw/baseline manualconfig apiconfig/],</pre>
<p>Note that XMLTV::Options guarantees that the grabber supports the manualconfig and apiconfig capabilities. The capabilities share and cache can be specified if the grabber supports them. XMLTV::Options will then automatically accept the command-line parameters &#8211;share and &#8211;cache respectively.</p>
<dt>stage_sub</p>
<dd>Required. A coderef that takes a stage-name and a configuration hashref as a parameter and returns an xml-string that describes the configuration necessary for that stage. The xml-string shall follow the xmltv-configuration.dtd.</p>
<dt>listchannels_sub</p>
<dd>Required. A coderef that takes a configuration hash as returned by XMLTV::Configure::LoadConfig as the first parameter and an option hash as returned by ParseOptions as the second parameter, and returns an xml-string containing a list of all the channels that the grabber can deliver data for using the supplied configuration. Note that the listsub shall not use any channel-configuration from the hashref.</p>
<dt>load_old_config_sub</p>
<dd>Optional. Default undef. A coderef that takes a filename as a parameter and returns a configuration hash in the same format as returned by XMLTV::Configure::LoadConfig. load_old_config_sub is called if XMLTV::Configure::LoadConfig fails to parse the configuration file. This allows the grabber to load configuration files created with an older version of the grabber.</p>
<dt>list_lineups_sub</p>
<dd>Optional. A coderef that takes an option hash as returned by ParseOptions as a parameter, and returns an xml-string containing a list of all the channel lineups for which the grabber can deliver data. The xml-string shall follow the xmltv-lineups.xsd schema.</p>
<dt>get_lineup_sub</p>
<dd>Optional. A coderef that returns an xml-string describing the configured lineup. The xml-string shall follow the xmltv-lineups.xsd schema.</p>
<dt>preferredmethod</p>
<dd>Optional. A value to return when the grabber is called with the &#8211;preferredmethod parameter. Example: </p>
<pre> my( $opt, $conf ) = ParseOptions( {
 grabber_name =&gt; 'tv_grab_test',
 version =&gt; '$Id: Options.pm,v 1.28 2014/01/30 14:41:09 bilbo_uk Exp $',
 description =&gt; 'Sweden (tv.swedb.se)',
 capabilities =&gt; [qw/baseline manualconfig apiconfig preferredmethod/],
 stage_sub =&gt; \&amp;config_stage,
 listchannels_sub =&gt; \&amp;list_channels,
 preferredmethod =&gt; 'allatonce',
 list_lineups_sub =&gt; \&amp;list_lineups,
 get_lineup_sub =&gt; \&amp;get_lineup,
 } );</pre>
<dt>defaults</p>
<dd>Optional. Default {}. A hashref that contains default values for the command-line options. It shall be in the same format as returned by Getopt::Long (See &#8220;Storing options in a hash&#8221; in Getopt::Long).</p>
<dt>extra_options</p>
<dd>Optional. Default []. An arrayref containing option definitions in the format accepted by Getopt::Long. This can be used to support grabber-specific options. The use of grabber-specific options is discouraged.</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h2>Copyright</h2>
<p>Copyright (C) 2005,2006 Mattias Holmlund. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301, USA.</font></p>
