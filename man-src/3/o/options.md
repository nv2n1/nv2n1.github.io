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
<p>Utility library that implements command-line parsing and handles a lot of functionality that is common to all XMLTV grabbers.</p>
<h2>Exported Functions</h2>
<p>All these functions are exported on demand.</p>
<h2>Usage</h2>
<dl COMPACT>
<dt><code>ParseOptions</code></dt>
<dd>ParseOptions shall be called by a grabber to parse the command-line options supplied by the user. It takes a single hashref as a parameter. The entries in the hash configure the behaviour of ParseOptions. </dd>
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
</dd><dl COMPACT>
<dt>&bull;</dt>
<dd>A hashref with the values for all command-line options in the format returned by Getopt::Long (See &#8220;Storing options in a hash&#8221; in Getopt::Long). This includes both options that the grabber must handle as well as options that ParseOptions handles for the grabber.</dd>
<dt>&bull;</dt>
<dd>A hashref to the data loaded from the configuration file. See XMLTV::Configure for the format of <tt>$conf</tt>.</dd></dl>
</dl>
<dl COMPACT>
<dd>ParseOptions handles the following options automatically without returning:</dd>
<dl COMPACT>
<dt>&#8211;help</dt>
<dd>
</dd><dt>&#8211;info (or &#8211;man)</dt>
<dd>
</dd><dt>&#8211;capabilities</dt>
<dd>
</dd><dt>&#8211;version</dt>
<dd>
</dd><dt>&#8211;description</dt>
<dd>
</dd><dt>&#8211;preferredmethod</dt>
<dd>Handled automatically if the preferredmethod capability has been set and the preferredmethod option has been specified in the call to ParseOptions.</dd></dl>
</dl>
<dl COMPACT>
<dd>ParseOptions also takes care of the following options without returning, by calling the stage_sub, listchannels_sub, list_lineups_sub and get_lineup_sub callbacks supplied by the grabber:</dd>
<dl COMPACT>
<dt>&#8211;configure</dt>
<dd>
</dd><dt>&#8211;configure-api</dt>
<dd>
</dd><dt>&#8211;stage</dt>
<dd>
</dd><dt>&#8211;list-channels</dt>
<dd>
</dd><dt>&#8211;list-lineups</dt>
<dd>
</dd><dt>&#8211;get-lineup</dt>
<dd></dd></dl>
</dl>
<dl COMPACT>
<dd>ParseOptions will thus only return to the grabber when the grabber shall actually grab data. </dd>
<p> If the &#8211;output option is specified, STDOUT will be redirected to the specified file. </p>
<p> The grabber must check the following options on its own:</p>
<dl COMPACT>
<dt>&#8211;days</dt>
<dd>
</dd><dt>&#8211;offset</dt>
<dd>
</dd><dt>&#8211;quiet</dt>
<dd>
</dd><dt>&#8211;debug</dt>
<dd></dd></dl>
</dl>
<dl COMPACT>
<dd>and any other options that are grabber specific. This can be done by reading <tt>$opt</tt>-&gt;{days} etc.</dd></dl>
<dt><code>Changing the behaviour of ParseOptions</code></dt>
<dd>The behaviour of ParseOptions can be influenced by passing named arguments in the hashref. The following arguments are supported:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>grabber_name</dt>
<dd>Required. The name of the grabber (e.g. tv_grab_se_swedb). This is used when printing the synopsis.</dd>
<dt>description</dt>
<dd>Required. The description for the grabber. This is returned in response to the &#8211;description option and shall say which region the grabber returns data for. Examples: &#8220;Sweden&#8221;, or &#8220;Sweden (tv.swedb.se)&#8221; if there are several grabbers for a region or country).</dd>
<dt>version</dt>
<dd>Required. This shall be a cvs Id field.</dd>
<dt>capabilities</dt>
<dd>Required. The capabilities that the grabber shall support. Only capabilities that XMLTV::Options knows how to handle can be specified. Example: </dd>
<pre> capabilities =&gt; [qw/baseline manualconfig apiconfig/],</pre>
<p>Note that XMLTV::Options guarantees that the grabber supports the manualconfig and apiconfig capabilities. The capabilities share and cache can be specified if the grabber supports them. XMLTV::Options will then automatically accept the command-line parameters &#8211;share and &#8211;cache respectively.</p>
<dt>stage_sub</dt>
<dd>Required. A coderef that takes a stage-name and a configuration hashref as a parameter and returns an xml-string that describes the configuration necessary for that stage. The xml-string shall follow the xmltv-configuration.dtd.</dd>
<dt>listchannels_sub</dt>
<dd>Required. A coderef that takes a configuration hash as returned by XMLTV::Configure::LoadConfig as the first parameter and an option hash as returned by ParseOptions as the second parameter, and returns an xml-string containing a list of all the channels that the grabber can deliver data for using the supplied configuration. Note that the listsub shall not use any channel-configuration from the hashref.</dd>
<dt>load_old_config_sub</dt>
<dd>Optional. Default undef. A coderef that takes a filename as a parameter and returns a configuration hash in the same format as returned by XMLTV::Configure::LoadConfig. load_old_config_sub is called if XMLTV::Configure::LoadConfig fails to parse the configuration file. This allows the grabber to load configuration files created with an older version of the grabber.</dd>
<dt>list_lineups_sub</dt>
<dd>Optional. A coderef that takes an option hash as returned by ParseOptions as a parameter, and returns an xml-string containing a list of all the channel lineups for which the grabber can deliver data. The xml-string shall follow the xmltv-lineups.xsd schema.</dd>
<dt>get_lineup_sub</dt>
<dd>Optional. A coderef that returns an xml-string describing the configured lineup. The xml-string shall follow the xmltv-lineups.xsd schema.</dd>
<dt>preferredmethod</dt>
<dd>Optional. A value to return when the grabber is called with the &#8211;preferredmethod parameter. Example: </dd>
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
<dt>defaults</dt>
<dd>Optional. Default {}. A hashref that contains default values for the command-line options. It shall be in the same format as returned by Getopt::Long (See &#8220;Storing options in a hash&#8221; in Getopt::Long).</dd>
<dt>extra_options</dt>
<dd>Optional. Default []. An arrayref containing option definitions in the format accepted by Getopt::Long. This can be used to support grabber-specific options. The use of grabber-specific options is discouraged.</dd></dl>
</dl>
<dl COMPACT>
<dd></dd></dl>
</dl>
<h2>Copyright</h2>
<p>Copyright (C) 2005,2006 Mattias Holmlund. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.</p>
