---
title: "sechecker(1)"
name: "sechecker"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sechecker/"
description: "sechecker – SELinux policy checking tool"
---

<h2>NAME</h2>
<p> sechecker &#8211; SELinux policy checking tool</p>
<h2>SYNOPSIS</h2>
<p> <code>sechecker</code> [OPTIONS] -p profile [POLICY &#8230;]<br />
 <code>sechecker</code> [OPTIONS] -m module [POLICY &#8230;]<br />
 <code>sechecker</code> [OPTIONS] -p profile -m module [POLICY &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>sechecker</code> allows the user to perform predefined modular checks on a SELinux policy. Profiles exist to group modules together and allow modification of module settings (see below).</p>
<h2>POLICY</h2>
<p> <code>sechecker</code> supports loading a SELinux policy in one of four formats.</p>
<dl>
<dt>source</p>
<dd> A single text file containing policy source for versions 12 through 21. This file is usually named policy.conf.</p>
<dt>binary</p>
<dd> A single file containing a monolithic kernel binary policy for versions 15 through 21. This file is usually named by version &#8211; for example, policy.20.</p>
<dt>modular</p>
<dd> A list of policy packages each containing a loadable policy module. The first module listed must be a base module.</p>
<dt>policy list</p>
<dd> A single text file containing all the information needed to load a policy, usually exported by SETools graphical utilities.</dl>
<p> If no policy file is provided, <code>sechecker</code> will search for the system default policy: checking first for a source policy, next for a binary policy matching the running kernel&#8217;s preferred version, and finally for the highest version that can be found. In the latter case, the policy will be downgraded to match the running system. If no policy can be found, <code>sechecker</code> will print an error message and exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-p PROFILE, &#8211;profile=PROFILE</p>
<dd> Load module settings from a module profile. The settings in the profile will override the default settings for all specified modules. If specified without -m, run all modules in the profile. PROFILE may either be the name of a known profile (see &#8211;list) or the path to a user created profile. see PROFILE OPTIONS below for more information about creating profiles.</p>
<dt>-m MODULE, &#8211;module=MODULE</p>
<dd> Run only the module named MODULE (see &#8211;list).</p>
<dt>&#8211;min-sev=SEVERITY</p>
<dd> Report only results with the minimum severity of SEVERITY. SEVERITY must have one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt>low</p>
<dd> The module&#8217;s results indicate a flaw in the policy that does not affect the manner in which the policy is enforced, but is considered to be improper.</p>
<dt>med</p>
<dd> The module&#8217;s results indicate a flaw in the policy that changes the manner in which the policy is enforced; however, it does not present an identifiable security risk.</p>
<dt>high</p>
<dd> The module&#8217;s results indicate a flaw in the policy that presents an identifiable security risk.</dl>
</dl>
<dt>&#8211;fcfile=FILE</p>
<dd> Use FILE for the file_contexts file instead of the system default. This flag is only applicable if sechecker was configured with the <code>&#8211;enable-sefs</code> flag.</p>
<dt>-l, &#8211;list</p>
<dd> Print a list of the name and a brief description of all known profiles and modules and exit.</p>
<dt>-h[MODULE], &#8211;help[=MODULE]</p>
<dd> Print general help information and exit. If MODULE is provided, print help information for the module named MODULE and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print version information and exit.</dl>
<h3>REPORT GENERATION OPTIONS</h3>
<p> Only one of the following may be provided to specify the length of the report for all modules. If provided, this option overrides both profile and module default output settings.</p>
<dl>
<dt>-q, &#8211;quiet</p>
<dd> suppress output</p>
<dt>-s, &#8211;short</p>
<dd> print short output</p>
<dt>-v, &#8211;verbose</p>
<dd> print verbose output</dl>
<h2>PROFILE OPTIONS</h2>
<p> Profiles are used to group modules together, to specify the output format for each module in the report, and to provide the ability to override the modules&#8217; default options. Each profile is a well-formed XML document, as specified by the DTD installed with sechecker. An example profile follows: </p>
<p> &lt;sechecker version=&quot;1.1&quot;&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;profile&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;module name=&quot;find_domains&quot;&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;output value=&quot;quiet&quot;/&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;option name=&quot;domain_attribute&quot;&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;item value=&quot;domain&quot;/&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;item value=&quot;user_domain&quot;/&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;/option&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;/module&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;/profile&gt;</p>
<p> &lt;/sechecker&gt; </p>
<p> The example profile specifies the output property for the find_domains module. The example profile also overrides the default value for the &quot;domain_attribute&quot; option in the find_domains module.</p>
<h3>PROFILE OUTPUT OPTIONS</h3>
<p> The valid output values for each module are specified below:</p>
<dl>
<dt>verbose</p>
<dd> Print each result in the report with accompanying proof(s).</p>
<dt>short</p>
<dd> Print a list of results with no accompanying proof.</p>
<dt>none</p>
<dd> Do not print output from this module in the report; however, module errors will still be printed.</p>
<dt>quiet</p>
<dd> Do not print output from this module in the report and do not print errors. This is useful for utility modules for which the calling module handles any errors.</dl>
<h3>PROFILE MODULE OPTIONS</h3>
<p> Several modules provide one or more options that can be set from a profile. Each option has one or more items. To check what options are available for a module use &#8211;help=MODULE, where MODULE is the name of the module as printed by &#8211;list.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Jeremy A. Mowery &lt;jmowery [at] tresys.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright(C) 2005-2008 Tresys Technology, LLC</p>
<h2>BUGS</h2>
<p> Please report bugs via an email to setools-bugs [at] tresys.com.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-apol/">apol</a>(1) </p>
<h2>Index</h2>
