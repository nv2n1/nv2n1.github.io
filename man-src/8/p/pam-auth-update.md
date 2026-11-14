---
title: "pam-auth-update(8)"
name: "pam-auth-update"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam-auth-update/"
description: "pam-auth-update – manage PAM configuration using packaged profiles"
---

<p>pam-auth-update &#8211; manage PAM configuration using packaged profiles</p>
<h2>Synopsis</h2>
<p><code>pam-auth-update</code> [<code>&#8211;package</code> [<code>&#8211;remove</code> <i>profile</i> [<i>profile</i>&#8230;]]] [<code>&#8211;force</code>]</p>
<h2>Description</h2>
<p><i>pam-auth-update</i> is a utility that permits configuring the central authentication policy for the system using pre-defined profiles as supplied by PAM module packages. Profiles shipped in the <i>/usr/share/pam-configs/</i> directory specify the modules, with options, to enable; the preferred ordering with respect to other profiles; and whether a profile should be enabled by default. Packages providing PAM modules register their profiles at install time by calling <code>pam-auth-update &#8211;package</code>. Selection of profiles is done using the standard debconf interface. The profile selection question will be asked at `medium&#8217; priority when packages are added or removed, so no user interaction is required by default. Users may invoke <code>pam-auth-update</code> directly to change their authentication configuration. </p>
<p> The script makes every effort to respect local changes to <i>/etc/pam.d/common-*.</i> Local modifications to the list of module options will be preserved, and additions of modules within the managed portion of the stack will cause <code>pam-auth-update</code> to treat the config files as locally modified and not make further changes to the config files unless given the <code>&#8211;force</code> option. </p>
<p> If the user specifies that <code>pam-auth-update</code> should override local configuration changes, the locally-modified files will be saved in <i>/etc/pam.d/</i> with a suffix of <i>.pam-old</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;package</code></p>
<dd>Indicate that the caller is a package maintainer script; lowers the priority of debconf questions to `medium&#8217; so that the user is not prompted by default.</p>
<dt><code>&#8211;enable </code><i>profile </i>[<i>profile</i>&#8230;]</p>
<dd>Enable the specified profiles in system configuration. This is used to enable profiles that are not on by default.</p>
<dt><code>&#8211;remove </code><i>profile </i>[<i>profile</i>&#8230;]</p>
<dd>Remove the specified profiles from the system configuration. <code>pam-auth-update &#8211;remove</code> should be used to remove profiles from the configuration before the modules they reference are removed from disk, to ensure that PAM is in a consistent and usable state at all times during package upgrades or removals.</p>
<dt><code>&#8211;force</code></p>
<dd>Overwrite the current PAM configuration, without prompting. This option <code>must not</code> be used by package maintainer scripts; it is intended for use by administrators only.</dl>
<h2>Files</h2>
<p><i>/etc/pam.d/common-*</i></p>
<dl>
<dd>Global configuration of PAM, affecting all installed services.</dl>
<p> <i>/usr/share/pam-configs/</i></p>
<dl>
<dd>Package-supplied authentication profiles.</dl>
<h2>Author</h2>
<p>Steve Langasek &lt;steve.langasek [at] canonical.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2008 Canonical Ltd.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-pam/">PAM</a>(7), <a href="/docs/linux/man/5-pam-d/">pam.d</a>(5), <a href="/docs/linux/man/7-debconf/">debconf</a>(7) </p>
