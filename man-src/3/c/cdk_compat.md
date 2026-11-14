---
title: "cdk_compat(3)"
name: "cdk_compat"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_compat/"
description: "cdk_compat – Cdk4 compatibility functions"
---

<h2>NAME</h2>
<p> cdk_compat &#8211; Cdk4 compatibility functions</p>
<h2>SYNOPSIS</h2>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk/cdk_compat.h&gt; </p>
<pre><code>

int getDirectoryContents(
    char *directory,
    char **list,
    int maxListSize);
int readFile(
    char *filename,
    char **info,
    int maxlines);
int splitString(
    char *string,
    char **items,
    char splitChar);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> These functions and macros make it simpler to port applications from the older Cdk4 library to Cdk5. </p>
<p> A few functions are deprecated in Cdk5, because they rely upon the caller to know in advance the size of data which will be returned by the function. </p>
<p> Additionally, some macros are deprecated because they serve no realistic purpose: they have direct (standard) equivalents in all modern curses implementations. </p>
<p> Finally, a few macro definitions are added to iron out naming inconsistencies across the Cdk4 header files.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>getDirectoryContents </code></p>
<dd> This opens the current directory and reads the contents. Use <code>CDKgetDirectoryContents()</code> in new code.</p>
<dt><code>readFile</code></p>
<dd> This reads a file and sticks it into the <code>char&nbsp;<wbr>**</code> provided. Use <code>CDKreadFile()</code> for new code.</p>
<dt><code>splitString</code></p>
<dd> This splits a string into one or more parts given the split character. Use <code>CDKsplitString()</code> for new code.</dl>
<h2>EXAMPLE</h2>
<p> Start the porting process by changing the <code>#include</code>&#8216;s to use</p>
<dl>
<dt>
<dd> #include &lt;cdk/cdk_compat.h&gt;</dl>
<p> rather than</p>
<dl>
<dt>
<dd> #include &lt;cdk.h&gt;</dl>
<p> Some adjustments of course are needed to make your compiler see the compatibility header file. A separate name was chosen so that it in turn can (by adjusting the include path) include either the old Cdk4 <code>cdk.h</code> or the new. If the old is included, you should link your program against the old library. Likewise, including the new requires that you link against the new library. </p>
<p> That is the first step: making your program compile using the compatibility header file using the old headers and library. </p>
<p> The next step is to get it to compile against the new headers and library. Most of the changes will require modifying bare references to certain pointers to wrap them with the <code>ObjOf()</code> and <code>ScreenOf()</code> macros. New Cdk uses these to provide functions which are easily shared among the different widget types. Your compiler should be able to tell you where the changes should be made. See the example programs which are included with Cdk as a guide. </p>
<p> That is the hard part of porting. But even for a large program, the changes can be made simply: there are not that many types of change to make. At the end of this step, you should still be able to build and run your program against the old headers and library. It is reasonably likely that you can do the same with the new headers and library. By using the same source for old/new versions of Cdk, you can test and verify that your program still works properly after these modifications. </p>
<p> Finally, unless this is a purely academic exercise, you will want to remove references to the deprecated functions and macros.</p>
<h2>SEE ALSO</h2>
<p> cdk_objs (3), cdk_util (3) </p>
<h2>Index</h2>
