---
title: "acl_to_any_text(3)"
name: "acl_to_any_text"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_to_any_text/"
description: "acl_to_any_text – convert an ACL to text"
---

<h2 class="name">NAME</h2>
<p> <code>acl_to_any_text</code> &#8211; convert an ACL to text </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft char * Fo acl_to_any_text Fa acl_t acl Fa const char *prefix Fa char separator Fa int options Fc</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_to_any_text function translates the ACL pointed to by the argument <i>acl</i> into a <code>NULL</code> terminated character string. This character string is composed of the ACL entries contained in <i>acl</i> in the entry text format described on <a href="/docs/linux/man/5-acl/">acl</a>(5). Entries are separated from each other by the <i>separator</i> character. If the argument <i>prefix</i> is not <code>(const char *)NULL</code> each entry is prefixed by this character string. </p>
<p> If the argument <i>options</i> is <code>0</code> ACL entries are converted using the entry tag type keywords <code>user , group , mask</code> and <code>other</code> User IDs and group IDs of ACL entries that contain such qualifiers are converted to their corresponding names; if an identifier has no corresponding name, a decimal number string is produced. The ACL text representation contains no additional comments. A bitwise combinations of the following <i>options</i> can be used to modify the result:</p>
<dl>
<dt><code>TEXT_ABBREVIATE</code></p>
<dd> Instead of the full tag type keywords, single letter abbreviations are used. The abbreviation for <code>user</code> is <code>u</code> the abbreviation for <code>group</code> is <code>g</code> the abbreviation for <code>mask</code> is <code>m</code> and the abbreviation for <code>other</code> is <code>o</code></p>
<dt><code>TEXT_NUMERIC_IDS</code></p>
<dd> User IDs and group IDs are included as decimal numbers instead of names.</p>
<dt><code>TEXT_SOME_EFFECTIVE</code></p>
<dd> A comment containing the effective permissions of the ACL entry is included after ACL entries that contain permissions which are ineffective because they are masked by an ACL_MASK entry. The ACL entry and the comment are separated by a tab character.</p>
<dt><code>TEXT_ALL_EFFECTIVE</code></p>
<dd> A comment containing the effective permissions of the ACL entry is included after all ACL entries that are affected by an ACL_MASK entry. The comment is included even if the permissions contained in the ACL entry equal the effective permissions. The ACL entry and the comment are separated by a tab character.</p>
<dt><code>TEXT_SMART_INDENT</code></p>
<dd> This option is used in combination with the TEXT_SOME_EFFECTIVE or TEXT_ALL_EFFECTIVE option. The number of tab characters inserted between the ACL entry and the comment is increased so that the comment is aligned to the fourth tab stop position. A tab width of 8 characters is assumed.</dl>
<p> The ACL referred to by <i>acl</i> is not changed. </p>
<p> This function allocates any memory necessary to contain the string and returns a pointer to the string. The caller should free any releasable memory, when the new string is no longer required, by calling Fn acl_free with the <i>(void*)char</i> returned by Fn acl_to_any_text as an argument.</p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns a pointer to the text representation of the ACL. On error, a value of <code>(char *)NULL</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_to_any_text function returns a value of <code>(char *)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL. </p>
<p> The ACL referenced by <i>acl</i> contains one or more improperly formed ACL entries, or for some other reason cannot be translated into the text form of an ACL.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The character string to be returned requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> acl_from_text3, acl_to_text3, acl_free3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
