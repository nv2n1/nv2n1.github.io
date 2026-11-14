---
title: "mrmopenhierarchyperdisplay(3)"
name: "mrmopenhierarchyperdisplay"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmopenhierarchyperdisplay/"
description: "MrmOpenHierarchyPerDisplay — Allocates a hierarchy ID and opens all the UID files in the hierarchy"
---

<p><code>MrmOpenHierarchyPerDisplay</code> &#8212; Allocates a hierarchy ID and opens all the UID files in the hierarchy</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmOpenHierarchyPerDisplay</code>(
<code>Display *display</code>,
<code>MrmCount num_files</code>,
<code>String file_names_list</code>[],
<code>MrmOsOpenParamPtr *ancillary_structures_list</code>,
<code>MrmHierarchy *hierarchy_id</code>);</pre>
<h2>Description</h2>
<p><code>MrmOpenHierarchyPerDisplay</code> allows you to specify the list of UID files that MRM searches in subsequent fetch operations. All subsequent fetch operations return the first occurrence of the named item encountered while traversing the UID hierarchy from the first list element (UID file specification) to the last list element. This function also allocates a hierarchy ID and opens all the UID files in the hierarchy. It initializes the optimized search lists in the hierarchy. If <code>MrmOpenHierarchyPerDisplay</code> encounters any errors during its execution, any files that were opened are closed. </p>
<p> The application must call <code>XtAppInitialize</code> before calling <code>MrmOpenHierarchyPerDisplay</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server and the value to pass to <code>XtResolvePathname</code>. For more information on the <code>Display</code> structure, see the Xlib function <code>XOpenDisplay</code>.</p>
<dt><i>num_files</i></p>
<dd>Specifies the number of files in the name list.</p>
<dt><i>file_names_list</i></p>
<dd>Specifies an array of character strings that identify the UID files.</p>
<dt><i>ancillary_structures_list</i></p>
<dd>A list of operating-system-dependent ancillary structures corresponding to items such as filenames, clobber flags, and so forth. This argument should be NULL for most operations. If you need to reference this structure, see the definition of <code>MrmOsOpenParamPtr</code> in the <code>MrmPublic.h</code> header file for more information.</p>
<dt><i>hierarchy_id</i></p>
<dd>Returns the search hierarchy ID. The search hierarchy ID identifies the list of UID files that MRM searches (in order) when performing subsequent fetch calls.</dl>
<p> Each UID file string in <i>file_names_list</i> can specify either a full pathname or a filename. If a UID file string has a leading / (slash), it specifies a full pathname, and MRM opens the file as specified. Otherwise, the UID file string specifies a filename. In this case MRM looks for the file along a search path specified by the <code>UIDPATH</code> environment variable or by a default search path, which varies depending on whether or not the <code>XAPPLRESDIR</code> environment variable is set. </p>
<p> The <code>UIDPATH</code> environment variable specifies a search path and naming conventions associated with UID files. It can contain the substitution field <code>%U</code>, where the UID file string from the <i>file_names_list</i> argument to <code>MrmOpenHierarchyPerDisplay</code> is substituted for <code>%U</code>. It can also contain the substitution fields accepted by <code>XtResolvePathname</code>. The substitution field <code>%T</code> is always mapped to <i>uid</i>. The entire path is searched first with <code>%S</code> mapped to <code>.uid</code>. If no file is found, it is searched again with <code>%S</code> mapped to NULL. For example, the following <code>UIDPATH</code> value and <code>MrmOpenHierarchyPerDisplay</code> call cause MRM to open two separate UID files: </p>
<pre><tt>UIDPATH=/uidlib/%L/%U.uid:/uidlib/%U/%L
 static char *uid_files[] = {&quot;/usr/users/me/test.uid&quot;, &quot;test2&quot;};
 MrmHierarchy *Hierarchy_id;
 MrmOpenHierarchyPerDisplay((MrmCount)2,uid_files, NULL, Hierarchy_id)</tt></pre>
<p>MRM opens the first file, <code>/usr/users/me/test.uid</code>, as specified in the <i>file_names_list</i> argument to <code>MrmOpenHierarchyPerDisplay</code>, because the UID file string in the <i>file_names_list</i> argument specifies a full pathname. MRM looks for the second file, <code>test2</code>, first as <code>/uidlib/%L/test2.uid</code> and second as <code>/uidlib/test2/%L</code>, where the display&#8217;s language string is substituted for <code>%L</code>. </p>
<p> After <code>MrmOpenHierarchyPerDisplay</code> opens the UID hierarchy, you should not delete or modify the UID files until you close the UID hierarchy by calling <code>MrmCloseHierarchy</code>. </p>
<p> If <code>UIDPATH</code> is not set, but the environment variable <code>XAPPLRESDIR</code> is set, MRM searches the following pathnames:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>%U%S</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%L/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%l/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%L/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/%l/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$XAPPLRESDIR/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/include/X11/uid/%U%S</code></dl>
<p> If neither <code>UIDPATH</code> nor <code>XAPPLRESDIR</code> is set, MRM searches the following pathnames:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%L/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%l/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%L/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%l/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>$HOME/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/uid/%N/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%L/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/%l/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/lib/X11/uid/%U%S</code></p>
<dt> &bull;</p>
<dd><code>/usr/include/X11/uid/%U%S</code></dl>
<p> These paths are defaults that vendors may change. For example, a vendor may use different directories for <code>/usr/lib/X11</code> and <code>/usr/include/X11</code>. </p>
<p> The following substitutions are used in these paths:</p>
<dl COMPACT>
<dt><code>%U</code></p>
<dd>The UID file string, from the <i>file_names_list</i> argument.</p>
<dt><code>%N</code></p>
<dd>The class name of the application.</p>
<dt><code>%L</code></p>
<dd>The display&#8217;s language string. This string is influenced by <code>XtSetLanguageProc</code>. The default string is determined by calling setlocale(<code>LC_ALL, NULL</code>).</p>
<dt><code>%l</code></p>
<dd>The language component of the display&#8217;s language string.</p>
<dt><code>%S</code></p>
<dd>The suffix to the filename. The entire path is first searched with a suffix of <code>.uid</code>. If no file is found, it is searched again with a NULL suffix.</dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmNOT_FOUND</code></p>
<dd>File not found.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmclosehierarchy/">MrmCloseHierarchy</a></code>(3).</p>
