---
title: "lintianprofile(3)"
name: "lintianprofile"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprofile/"
description: "Lintian::Profile – Profile parser for Lintian"
---

<p>Lintian::Profile &#8211; Profile parser for Lintian </p>
<h2>Synopsis</h2>
<pre> my $profile = Lintian::Profile-&gt;new ('debian');</pre>
<h2>Description</h2>
<p>Lintian::Profile handles finding, parsing and implementation of Lintian Profiles as well as loading the relevant Lintian checks.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>$prof-&gt;<code>known_aliases()</code></p>
<dd>Returns a hash with old names that have new names.</p>
<dt>$prof-&gt;profile_list</p>
<dd>Returns a list ref of the (normalized) names of the profile and its parents. The last element of the list is the name of the profile itself, the second last is its parent and so on. </p>
<p> Note: This list reference and its contents should not be modified.</p>
<dt>$prof-&gt;name</p>
<dd>Returns the name of the profile, which may differ from the name used to create this instance of the profile (e.g. due to symlinks).</p>
<dt>load ([$profname[, $ipath[, $extra]]])</p>
<dd>Loads a new profile. <tt>$profname</tt> is the name of the profile and <tt>$ipath</tt> is a list reference containing the path to one (or more) Lintian &#8220;roots&#8221;. </p>
<p> If <tt>$profname</tt> is <tt>&quot;undef&quot;</tt>, the default vendor will be loaded based on Dpkg::Vendor::get_current_vendor. </p>
<p> If <tt>$ipath</tt> is not given, a default one will be used.</p>
<dt>$prof-&gt;known_tags</p>
<dd>
<dt>$prof-&gt;enabled_tags</p>
<dd>
<dt>$prof-&gt;get_taginfo ($name)</p>
<dd>Returns the Lintian::Tag::Info for <tt>$tag</tt> if known. Otherwise it returns undef.</p>
<dt>$prof-&gt;is_overridable ($tag)</p>
<dd>Returns a false value if the tag has been marked as &#8220;non-overridable&#8221;. Otherwise it returns a truth value.</p>
<dt>$prof-&gt;known_checks</p>
<dd>
<dt>$prof-&gt;enabled_checks</p>
<dd>
<dt>$prof-&gt;get_checkinfo ($name)</p>
<dd>Returns the Lintian::Check::Info for <tt>$name</tt>. Otherwise it returns undef.</p>
<dt>$prof-&gt;enable_tag ($name)</p>
<dd>Enables a tag.</p>
<dt>$prof-&gt;disable_tag ($name)</p>
<dd>Disable a tag.</p>
<dt>$prof-&gt;include_path ([$path])</p>
<dd>Returns an array of paths to the (partial) Lintian roots, which are used by this profile. The paths are ordered from &#8220;highest&#8221; to &#8220;lowest&#8221; priority (i.e. items in the earlier paths should shadow those in later ones). </p>
<p> If <tt>$path</tt> is given, the array will contain the paths to the path in these roots denoted by <tt>$path</tt>. </p>
<p> Paths returned are not guaranteed to exists.</p>
<dt>display_level_for_tag</p>
<dd>
<dt>tag_is_enabled(<font SIZE="-1">TAG</font>)</p>
<dd>
<dt>display(<font SIZE="-1">OPERATION, RELATION, SEVERITY</font>)</p>
<dd>Configure which tags are displayed by severity. <font SIZE="-1">OPERATION</font> is <tt>&quot;+&quot;</tt> to display the indicated tags, <tt>&quot;-&quot;</tt> to not display the indicated tags, or <tt>&quot;=&quot;</tt> to not display any tags except the indicated ones. <font SIZE="-1">RELATION</font> is one of <tt>&quot;&lt;&quot;</tt>, <tt>&quot;&lt;=&quot;</tt>, <tt>&quot;=&quot;</tt>, <tt>&quot;&gt;=&quot;</tt>, or <tt>&quot;&gt;&quot;</tt>. The <font SIZE="-1">OPERATION</font> will be applied to all values of severity that match the given <font SIZE="-1">RELATION</font> on the <font SIZE="-1">SEVERITY</font> argument. If either of those arguments are undefined, the action applies to any value for that variable. For example: </p>
<pre> $tags-&gt;display('=', '&gt;=', 'error');</pre>
<p>turns off display of all tags and then enables display of any tag of severity error or higher. </p>
<pre> $tags-&gt;display('+', '&gt;', 'warning');</pre>
<p>adds to the current configuration display of all tags with a severity higher than warning. </p>
<pre> $tags-&gt;display('-', '=', 'info');</pre>
<p>turns off display of tags of severity info. </p>
<p> This method throws an exception on errors, such as an unknown severity or an impossible constraint (like <tt>&quot;&gt; serious&quot;</tt>).</dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
