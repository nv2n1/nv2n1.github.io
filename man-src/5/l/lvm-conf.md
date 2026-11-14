---
title: "lvm-conf(5)"
name: "lvm-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lvm-conf/"
description: "lvm.conf — Configuration file for LVM2"
---

<p>lvm.conf &#8212; Configuration file for LVM2</p>
<h2>Synopsis</h2>
<p><code>/etc/lvm/lvm.conf</code></p>
<h2>Description</h2>
<p><code>lvm.conf</code> is loaded during the initialisation phase of <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8). This file can in turn lead to other files being loaded &#8211; settings read in later override earlier settings. File timestamps are checked between commands and if any have changed, all the files are reloaded. For a description of each lvm.conf setting, run: <code>lvmconfig &#8211;typeconfig default &#8211;withcomments &#8211;withspaces</code> The settings defined in lvm.conf can be overridden by any of these extended configuration methods:</p>
<dl>
<dt><code>direct config override on command line</code></p>
<dd>The <code>&#8211;config ConfigurationString</code> command line option takes the ConfigurationString as direct string representation of the configuration to override the existing configuration. The ConfigurationString is of exactly the same format as used in any LVM configuration file.</p>
<dt><code>profile config</code></p>
<dd>A profile is a set of selected customizable configuration settings that are aimed to achieve a certain characteristics in various environments or uses. It&#8217;s used to override existing configuration. Normally, the name of the profile should reflect that environment or use. There are two groups of profiles recognised: <code>command profiles</code> and <code>metadata profiles</code>. The <code>command profile</code> is used to override selected configuration settings at global LVM command level &#8211; it is applied at the very beginning of LVM command execution and it is used throughout the whole time of LVM command execution. The command profile is applied by using the <code>&#8211;commandprofile ProfileName</code> command line option that is recognised by all LVM2 commands. The <code>metadata profile</code> is used to override selected configuration settings at Volume Group/Logical Volume level &#8211; it is applied independently for each Volume Group/Logical Volume that is being processed. As such, each Volume Group/Logical Volume can store the profile name used in its metadata so next time the Volume Group/Logical Volume is processed, the profile is applied automatically. If Volume Group and any of its Logical Volumes have different profiles defined, the profile defined for the Logical Volume is preferred. The metadata profile can be attached/detached by using the <code>lvchange</code> and <code>vgchange</code> commands and their <code>&#8211;metadataprofile ProfileName</code> and <code>&#8211;detachprofile</code> options or the <code>&#8211;metadataprofile</code> option during creation when using <code>vgcreate</code> or <code>lvcreate</code> command. The <code>vgs</code> and <code>lvs</code> reporting commands provide <code>-o vg_profile</code> and <code>-o lv_profile</code> output options to show the metadata profile currently attached to a Volume Group or a Logical Volume. The set of options allowed for command profiles is mutually exclusive when compared to the set of options allowed for metadata profiles. The settings that belong to either of these two sets can&#8217;t be mixed together and LVM tools will reject such profiles. LVM itself provides a few predefined configuration profiles. Users are allowed to add more profiles with different values if needed. For this purpose, there&#8217;s the <code>command_profile_template.profile</code> (for command profiles) and <code>metadata_profile_template.profile</code> (for metadata profiles) which contain all settings that are customizable by profiles of certain type. Users are encouraged to copy these template profiles and edit them as needed. Alternatively, the <code>lvmconfig &#8211;file &lt;ProfileName.profile&gt; &#8211;type profilable-command &lt;section&gt;</code> or <code>lvmconfig &#8211;file &lt;ProfileName.profile&gt; &#8211;type profilable-metadata &lt;section&gt;</code> can be used to generate a configuration with profilable settings in either of the type for given section and save it to new ProfileName.profile (if the section is not specified, all profilable settings are reported). The profiles are stored in /etc/lvm/profile directory by default. This location can be changed by using the <code>config/profile_dir</code> setting. Each profile configuration is stored in <code>ProfileName.profile</code> file in the profile directory. When referencing the profile, the <code>.profile</code> suffix is left out.</p>
<dt><code>tag config</code></p>
<dd>See <code>tags</code> configuration setting description below.  When several configuration methods are used at the same time and when LVM looks for the value of a particular setting, it traverses this <code>config cascade</code> from left to right: <code>direct config override on command line</code>-&gt; <code>command profile config</code>-&gt; <code>metadata profile config</code>-&gt; <code>tag config</code>-&gt; <code>lvmlocal.conf-&gt; lvm.conf</code> No part of this cascade is compulsory. If there&#8217;s no setting value found at the end of the cascade, a default value is used for that setting. Use <code>lvmconfig</code> to check what settings are in use and what the default values are.</p>
<h2>Syntax</h2>
<p>This section describes the configuration file syntax. </p>
<p> Whitespace is not significant unless it is within quotes. This provides a wide choice of acceptable indentation styles. Comments begin with # and continue to the end of the line. They are treated as whitespace. </p>
<p> Here is an informal grammar:</p>
<dl>
<dt><code>file</code> = <code>value</code>*</p>
<dd>A configuration file consists of a set of values.</p>
<dt><code>value</code> = <code>section</code> | <code>assignment</code></p>
<dd>A value can either be a new section, or an assignment.</p>
<dt><code>section</code> = <code>identifier</code> &#8216;<code>{</code>&#8216; <code>value</code>* &#8216;<code>}</code>&#8216;</p>
<dd>A section groups associated values together. If the same section is encountered multiple times, the contents of all instances are concatenated together in the order of appearance.<br />
 It is denoted by a name and delimited by curly brackets.<br />
 e.g.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>backup {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>}</p>
<dt><code>assignment</code> = <code>identifier</code> &#8216;<code>=</code>&#8216; ( <code>array</code> | <code>type</code> )</p>
<dd>An assignment associates a type with an identifier. If the identifier contains forward slashes, those are interpreted as path delimiters. The statement <code>section/key = value</code> is equivalent to <code>section { key = value }</code>. If multiple instances of the same key are encountered, only the last value is used (and a warning is issued).<br />
 e.g.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><code>level = 7</code></p>
<dt><code>array</code> = &#8216;<code>[</code>&#8216; ( <code>type</code> &#8216;<code>,</code>&#8216;)* <code>type</code> &#8216;<code>]</code>&#8216; | &#8216;<code>[</code>&#8216; &#8216;<code>]</code>&#8216;</p>
<dd>Inhomogeneous arrays are supported.<br />
 Elements must be separated by commas.<br />
 An empty array is acceptable.</p>
<dt><code>type</code> = <code>integer</code> | <code>float</code> | <code>string</code></p>
<dd><code>integer</code> = [0-9]*<br />
 <code>float</code> = [0-9]*&#8217;<code>.</code>&#8216;[0-9]*<br />
 <code>string </code>= &#8221;.*&#8221;</p>
<dd>Strings with spaces must be enclosed in double quotes, single words that start with a letter can be left unquoted. </p>
</dl>
<h2>Settings</h2>
<p>The <code>lvmconfig</code> command prints the LVM configuration settings in various ways. See the man page <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8). </p>
<p> Command to print a list of all possible config settings, with their default values:<br />
 <code>lvmconfig &#8211;type default</code> </p>
<p> Command to print a list of all possible config settings, with their default values, and a full description of each as a comment:<br />
 <code>lvmconfig &#8211;type default &#8211;withcomments</code> </p>
<p> Command to print a list of all possible config settings, with their current values (configured, non-default values are shown):<br />
 <code>lvmconfig &#8211;type current</code> </p>
<p> Command to print all config settings that have been configured with a different value than the default (configured, non-default values are shown):<br />
 <code>lvmconfig &#8211;type diff</code> </p>
<p> Command to print a single config setting, with its default value, and a full description, where &quot;Section&quot; refers to the config section, e.g. global, and &quot;Setting&quot; refers to the name of the specific setting, e.g. umask:<br />
 <code>lvmconfig &#8211;type default &#8211;withcomments Section/Setting</code></p>
<h2>Files</h2>
<p><i>/etc/lvm/lvm.conf</i><br />
 <i>/etc/lvm/lvmlocal.conf</i><br />
 <i>/etc/lvm/archive</i><br />
 <i>/etc/lvm/backup</i><br />
 <i>/etc/lvm/cache/.cache</i><br />
 <i>/run/lock/lvm</i><br />
 <i>/etc/lvm/profile</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) </p>
