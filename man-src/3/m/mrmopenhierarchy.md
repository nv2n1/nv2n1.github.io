---
title: "mrmopenhierarchy(3)"
name: "mrmopenhierarchy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmopenhierarchy/"
description: "MrmOpenHierarchy — Allocates a hierarchy ID and opens all the UID files in the hierarchy"
---

<p><code>MrmOpenHierarchy</code> &#8212; Allocates a hierarchy ID and opens all the UID files in the hierarchy</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmOpenHierarchy</code>(
<code>MrmCount num_files</code>,
<code>String file_names_list</code>[],
<code>MrmOsOpenParamPtr *ancillary_structures_list</code>,
<code>MrmHierarchy *hierarchy_id</code>);</pre>
<h2>Description</h2>
<p>This routine is obsolete and exists for compatibility with previous releases. It is replaced by <code>MrmOpenHierarchyPerDisplay</code>. <code>MrmOpenHierarchy</code> is identical to <code>MrmOpenHierarchyPerDisplay</code> except that <code>MrmOpenHierarchy</code> does not take a <i>display</i> argument.</p>
<dl COMPACT>
<dt><i>num_files</i></dt>
<dd>Specifies the number of files in the name list.</dd>
<dt><i>file_names_list</i></dt>
<dd>Specifies an array of character strings that identify the UID files.</dd>
<dt><i>ancillary_structures_list</i></dt>
<dd>A list of operating-system-dependent ancillary structures corresponding to items such as filenames, clobber flags, and so forth. This argument should be NULL for most operations. If you need to reference this structure, see the definition of <code>MrmOsOpenParamPtr</code> in the <code>MrmPublic.h</code> header file for more information.</dd>
<dt><i>hierarchy_id</i></dt>
<dd>Returns the search hierarchy ID. The search hierarchy ID identifies the list of UID files that MRM searches (in order) when performing subsequent fetch calls.</dd></dl>
<p> Each UID file string in <i>file_names_list</i> can specify either a full pathname or a filename. If a UID file string has a leading slash (/), it specifies a full pathname, and MRM opens the file as specified. Otherwise, the UID file string specifies a filename. In this case, MRM looks for the file along a search path specified by the <code>UIDPATH</code> environment variable or by a default search path, which varies depending on whether or not the <code>XAPPLRESDIR</code> environment variable is set. </p>
<p> The <code>UIDPATH</code> environment variable specifies a search path and naming conventions associated with UID files. It can contain the substitution field <code>%U</code>, where the UID file string from the <i>file_names_list</i> argument to <code>MrmOpenHierarchyPerDisplay</code> is substituted for <code>%U</code>. It can also contain the substitution fields accepted by <code>XtResolvePathname</code>. The substitution field <code>%T</code> is always mapped to <i>uid</i>. The entire path is first searched with <code>%S</code> mapped to <code>.uid</code>. If no file is found, it is searched again with <code>%S</code> mapped to NULL. </p>
<p> If no display is set prior to calling this function, the result of this function&#8217;s call to <code>XtResolvePathname</code> is undefined. </p>
<p> For example, the following <code>UIDPATH</code> value and <code>MrmOpenHierarchy</code> call cause MRM to open two separate UID files: </p>
<pre><tt>UIDPATH=/uidlib/%L/%U.uid:/uidlib/%U/%L
 static char *uid_files[] = {&quot;/usr/users/me/test.uid&quot;, &quot;test2&quot;};
 MrmHierarchy *Hierarchy_id;
 MrmOpenHierarchy((MrmCount)2,uid_files, NULL, Hierarchy_id)</tt></pre>
<p>MRM opens the first file, <code>/usr/users/me/test.uid</code>, as specified in the <i>file_names_list</i> argument to <code>MrmOpenHierarchy</code>, because the UID file string in the <i>file_names_list</i> argument specifies a full pathname. MRM looks for the second file, <code>test2</code>, first as <code>/uidlib/%L/test2.uid</code> and second as <code>/uidlib/test2/%L</code>, where the display&#8217;s language string is substituted for <code>%L</code>. </p>
<p> After <code>MrmOpenHierarchy</code> opens the UID hierarchy, you should not delete or modify the UID files until you close the UID hierarchy by calling <code>MrmCloseHierarchy</code>. </p>
<p> If <code>UIDPATH</code> is not set but the environment variable <code>XAPPLRESDIR</code> is set, MRM searches the following pathnames:</p>
<dl COMPACT>
<dt> &bull;</dt>
<dd><code>%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$XAPPLRESDIR/%L/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$XAPPLRESDIR/%l/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$XAPPLRESDIR/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$XAPPLRESDIR/%L/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$XAPPLRESDIR/%l/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$XAPPLRESDIR/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$HOME/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$HOME/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%L/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%l/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%L/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%l/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/include/X11/uid/%U%S</code></dd></dl>
<p> If neither <code>UIDPATH</code> nor <code>XAPPLRESDIR</code> is set, MRM searches the following pathnames:</p>
<dl COMPACT>
<dt> &bull;</dt>
<dd><code>%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>HOME/%L/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>HOME/%l/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$HOME/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$HOME/%L/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$HOME/%l/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$HOME/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>$HOME/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%L/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%l/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/uid/%N/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%L/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/%l/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/lib/X11/uid/%U%S</code></dd>
<dt> &bull;</dt>
<dd><code>/usr/include/X11/uid/%U%S</code></dd></dl>
<p> These paths are defaults that vendors may change. For example, a vendor may use different directories for <code>/usr/lib/X11</code> and <code>/usr/include/X11</code>. </p>
<p> The following substitutions are used in these paths:</p>
<dl COMPACT>
<dt><code>%U</code></dt>
<dd>The UID file string, from the <i>file_names_list</i> argument.</dd>
<dt><code>%N</code></dt>
<dd>The class name of the application.</dd>
<dt><code>%L</code></dt>
<dd>The display&#8217;s language string. This string is influenced by <code>XtSetLanguageProc</code>. The default string is determined by calling setlocale(<code>LC_ALL, NULL</code>).</dd>
<dt><code>%l</code></dt>
<dd>The language component of the display&#8217;s language string.</dd>
<dt><code>%S</code></dt>
<dd>The suffix to the filename. The entire path is first searched with a suffix of <code>.uid</code>. If no file is found, it is searched again with a NULL suffix.</dd></dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></dt>
<dd>The function executed successfully.</dd>
<dt><code>MrmNOT_FOUND</code></dt>
<dd>File not found.</dd>
<dt><code>MrmFAILURE</code></dt>
<dd>The function failed.</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3) and <code><a href="/docs/linux/man/3-mrmclosehierarchy/">MrmCloseHierarchy</a></code>(3).</p>
