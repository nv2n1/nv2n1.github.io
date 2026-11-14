---
title: "objcmdwrite(3)"
name: "objcmdwrite"
section: "3"
letter: "o"
url: "/docs/linux/man/3-objcmdwrite/"
description: "TclCommandWriting – Writing C language extensions to Tcl."
---

<p>TclCommandWriting &#8211; Writing C language extensions to Tcl. </p>
<h2>Overview</h2>
<p>This document is intended to help the programmer who wishes to extend Tcl with C language routines. It should also be useful to someone wishing to add Tcl to an existing editor, communications program, window manager, etc. Experienced extension writers may find this manual helpful in rewriting their applications to use the new Tcl object system. We assume you are already fluent in the C programming language and that you have built and installed Tcl on your machine. </p>
<p> Information on the available C interface routines to Tcl can be found in the <i>*.3</i> manual pages in the <i>doc</i> directory of the baseline Tcl distribution, and in the <i>*.3</i> manpages in the <i>doc</i> directory of Extended Tcl.</p>
<h2>Tcl Object System</h2>
<p>With the release of Tcl version 8, Tcl has a new system for managing Tcl values internally. To the Tcl programmer, the new objects look and act like strings, as before. But at the C level, these objects can now also hold cached internal representations of the strings in various native datatypes. For example, an object containing a string consisting of an integer, will now maintain a machine-code integer representation, if an integer representation has been needed. Using these objects is much more efficient than using the older-style Tcl strings, although the older style is still (currently) supported. </p>
<p> Although the object system has almost no effect at all on how the Tcl programmer uses Tcl, the object system&#8217;s C interfaces to strings, integers, lists, etc., have changed considerably. While converting a package to use the new system can be a lot of work, the combination of the object system, which saves Tcl from having to constantly convert strings to integers and back, etc., and the on-the-fly bytecode compiler (which keeps Tcl from having to continually reparse code it is to execute) yield Tcl programs that routinely execute several times more quickly than with previous versions (Tcl 7 and before), and in some cases run as much as 2500 (!) times faster than before. </p>
<p> We have chosen, then, to rewrite the Command Writer&#8217;s manpage, which has been shipping with Extended Tcl for a number of years, to produce this new version based on the new object system. The old manpage, based on the older string-oriented routines, will still be included in TclX releases for now, as it is still relevant to Tcl releases through version 7, and may be of use to those modifying/upgrading packages written for the old model. The old manual will be dropped from the release once we deem it unneeded; the old interfaces should now be considered legacy interfaces, and all new development should be done using the new object interfaces, unless backwards compatibility to pre-Tcl-8 releases is needed. </p>
<h2>A Simple C Extension</h2>
<p>All C-based Tcl commands are called with four arguments: a client data pointer, an interpreter pointer, an argument count and a pointer to an array of Tcl objects containing the arguments to the command. </p>
<p> A simple C extension to Tcl is now presented, and described below: </p>
<pre> #include &quot;tcl.h&quot;
 int App_DumpArgsObjCmd(clientData, interp, objc, objv)
 void *clientData;
 Tcl_Interp *interp;
 int objc;
 Tcl_Obj **objv;
 {
 int i;
 int stringLen;
 char *stringPtr;
 for (i = 1; i &lt; objc; i++) {
 stringPtr = Tcl_GetStringFromObj (objv [i], &amp;stringLen);
 printf(&quot;%s&quot;, stringPtr);
 if (i &lt; objc - 1) printf(&quot; &quot;);
 }
 printf(&quot;
&quot;);
 return TCL_OK;
 }</pre>
<p>The client data pointer will be described later.</p>
<h2>Interpreters</h2>
<p>The interpreter pointer is the &#8220;key&#8221; to an interpreter. It is returned by <code>Tcl_CreateInterp</code> and is used extensively within Tcl, and will be used by your C extensions. The data structure pointed to by the interpreter pointer, and all of the subordinate structures that branch off of it, make up a Tcl interpreter, which includes all of the currently defined procedures, commands, variables, arrays and the execution state of that interpreter. (For more information on creating and deleting interpreters, please examine the <code><a href="/docs/linux/man/3-crtinterp/">CrtInterp</a></code>(3) manpage in the core Tcl distribution. For information on creating interpreters that include the commands provided by Extended Tcl, check out the <code><a href="/docs/linux/man/3-tclx_init/">TclX_Init</a></code>(3) manpage of Extended Tcl. For a manual page describing the user-visible fields of a Tcl interpreter, please look at <code><a href="/docs/linux/man/3-interp/">Interp</a></code>(3) in core Tcl.)</p>
<h2>Object Count And Arguments</h2>
<p>The argument count, or object count (objc), and pointer to an array of pointers to Tcl objects of the command&#8217;s arguments (objv) is handled by your C code, in a manner similar to the one you would use in writing a C <i>main</i> function &#8212; an argument count and array of pointers works the same as in a C <i>main</i> call; pointers to the arguments to the function are contained in the <i>objv</i> array. Similar to a C main, the first argument (<i>objv[0]</i>) is an object containing the name the routine was called as (in a C main, the name the program was invoked as). </p>
<p> In Tcl, however, the array of pointers are not pointers to character strings (although they were in all version of Tcl before 8.0). </p>
<p> In the above example, all of the arguments are output with a space between each one by looping through elements of the <i>objv</i> array from one to the argument count, <i>objc</i>, and a newline is output to terminate the line &#8212; a simple &#8220;echo&#8221; command. This example uses printf for simplicity. Of course in production code you would want to use the Tcl filesystem interfaces. See <code><a href="/docs/linux/man/3-getfile/">GetFile</a></code>(3) and friends for more information. </p>
<p> All arguments from a Tcl call to a Tcl C extension are passed as Tcl Objects. If your C routine wants to look at one of those arguments as an integer, you need to make a call to a routine to fetch the representation of the object that you need. In the earlier example, for instance, <code>Tcl_GetStringFromObj</code> is called to obtain a textual representation of an object. Additional routines are available to fetch the representation of a data element as other data types. Tcl_GetBooleanFromObj, Tcl_GetDoubleFromObj, Tcl_GetIntFromObj, Tcl_GetLongFromObj, and Tcl_GetIndexFromObj, fetch object representations of Tcl strings as booleans, double-precision floating point, integer, long integer, and lists, among others. </p>
<p> These routines automatically leave an appropriate error message in the Tcl interpreter&#8217;s result object and return <code>TCL_ERROR</code> if a conversion error occurs. (For more information on these routines, please look at the <code><a href="/docs/linux/man/3-object/">Object</a></code>(3) manpage in the core Tcl distribution.)</p>
<h2>Returning Results</h2>
<p>As you might expect, the API for setting results from C extensions has changed significantly under the object system. The old technique of writing small results directory into the interpreter&#8217;s result buffer is no longer used, for example. The notion of having to tell Tcl whether a result is static or dynamic is also a thing of the past. Under the object system, results are objects that are set up by your code, and objects are freed when their reference counts say they should be. More on this later. </p>
<p> If you program produces a numeric result, it should set the result object to contain that numeric value. A common way of doing this is something like&#8230; </p>
<pre> Tcl_Obj *obj;
 obj = Tcl_GetObjResult (interp);
 Tcl_SetIntObj (obj, value);</pre>
<p>The above code obtains a pointer to the result object (an object made available to your routine that you&#8217;re supposed to store your results into) and sets the integer value <i>value</i> into it. </p>
<p> Another way to do it would be to set up a new object and tell Tcl that this object contains the result&#8230; </p>
<pre> Tcl_Obj *resultObj;
 /* create a new object for use as a result */
 resultObj = Tcl_NewObj ();
 Tcl_SetIntObj (obj, value);
 Tcl_SetObjResult (interp, resultObj);</pre>
<p>Understanding how results are passed back to Tcl is essential to the C extension writer. Please study the <code><a href="/docs/linux/man/3-setobjresult/">SetObjResult</a></code>(3) manual page in the Tcl distribution for more information.</p>
<h2>Validating Arguments</h2>
<p>It is a design goal of Tcl that no Tcl program be able to cause Tcl to dump core. It is important that the extension writers, likewise, use the avaiable methods and tools to make sure that their extensions do not allow unchecked input, for example, to cause the code to get some kind of runtime exception. </p>
<p> The object system has simplified, to some degree, the task of validating arguments, in that the object system automatically attempts type conversions as needed, and will return an error when a type conversion fails. </p>
<p> A simple, but important, check that every C extension should do is verify that it has the right number of arguments. </p>
<p> The act of trying to use, say, a string as an integer, implicitly performs the type conversion of the string and, if it doesn&#8217;t work as an integer, returns TCL_ERROR. The developer should check for the TCL_ERROR return from all of the GetXxxFromObj commands, and handle them as appropriate. Usually this will mean propagating the error on back to the user, or to an intevening catch, as the case may be. </p>
<p> You should also check that values are in range (when their ranges are known), and so forth. When C data structures need to be handled in Tcl in some form or another, yet the contents of the data must remain opaque to Tcl, as is usually the case with binary data (although futures releases of Tcl are expected to have native abilities to read, write and manipulate binary data instrinsically), <i>handles</i> need to be used. Handles will be described and examples presented, later in this doc.</p>
<h2>Another C Extension &#8211; The Max Command</h2>
<p>In the command below, two or more arguments are compared, and the one with the maximum value is returned, if all goes well. It is an error if there are fewer than two arguments (the pointer to the &#8220;max&#8221; command text itself, <i>objv[0]</i>, and a pointer to at least one object to compare the values of). </p>
<pre> int
 Tcl_MaxCmd (clientData, interp, objc, objv)
 char *clientData;
 Tcl_Interp *interp;
 int objc;
 Tcl_Obj **objv;
 {
 int maxVal = MININT;
 int value, idx;
 if (objc &lt; 3)
 return TclX_WrongArgs (interp, objv[0], 
 &quot; num1 num2 [..numN]&quot;);
 for (idx = 1; idx &lt; objc; idx++) {
 if (Tcl_GetIntFromObj (interp, objv[idx], &amp;value) != TCL_OK)
 return TCL_ERROR;
 if (value &gt; maxVal) {
 maxVal = value;
 }
 }
 Tcl_SetIntObj (Tcl_GetObjResult (interp), value);
 return TCL_OK;
 }</pre>
<p>Here we introduce the Extended Tcl helper function <code>TclX_WrongArgs</code>. This routine makes it easy to create an error message and error return in response to the common mistake of being called with a wrong number. </p>
<p> <code>Tcl_GetIntFromObj</code> is used to fetch the integer values of the remaining arguments. If any fail to be converted, we return a Tcl error. If an interpreter is specified in the call to <code>Tcl_GetIntFromObj</code>, an appropriate error message about the conversion failure will be left in the result, so we do that here. </p>
<p> After examining all of the arguments to find the largest value, we set the result object to contain that value, and return <code>TCL_OK</code>.</p>
<h2>Returning Results</h2>
<p>When Tcl-callable functions complete, they should normally return <code>TCL_OK</code> or <code>TCL_ERROR</code>. <code>TCL_OK</code> is returned when the command succeeded, and <code>TCL_ERROR</code> is returned when the command has failed in some abnormal way. <code>TCL_ERROR</code> should be returned for all syntax errors, non-numeric values when numeric ones were expected, and so forth. Less clear in some cases is whether Tcl errors should be returned or whether a function should just return a status value. For example, end-of-file during a <i>gets</i> returns a status, but <i>open</i> returns an error if it fails. Errors can be caught from Tcl programs using the <i>catch</i> command. (See Tcl&#8217;s <code><a href="/docs/linux/man/n-catch/">catch</a></code>(n) and <code><a href="/docs/linux/man/n-error/">error</a></code>(n) manual pages.) </p>
<p> Less common return values are <code>TCL_RETURN</code>, <code>TCL_BREAK</code> and <code>TCL_CONTINUE</code>. These are used if you are adding new control and/or looping structures to Tcl. To see these values in action, examine the source code to Extended Tcl&#8217;s <i>loop</i> commands. Tcl&#8217;s <i>while</i>, <i>for</i> and <i>if</i> commands used to work in the just same manner, but are now compiled into bytecode by the bytecode for performance. </p>
<h2>Another C Extension &#8211; The Lreverse Command</h2>
<p>In the command below, a list is passed as an argument, and a list containing all of the elements of the list in reverse order is returned. It is an error if anything other than two arguments are passed (the pointer to the &#8220;lreverse&#8221; command text itself, <i>objv[0]</i>, and a pointer to the list to reverse. </p>
<p> Once <i>lreverse</i> has determined that it has received the correct number of arguments, <code>Tcl_ListObjGetElements</code> is called to split the list into its own <i>objc</i> count of elements and <i>objv</i> array of pointers to the list&#8217;s elements. </p>
<p> <i>lreverse</i> then operates on the array of pointers, swapping them from lowest to highest, second-lowest to second-highest, and so forth. </p>
<p> <code>Tcl_ListObjAppendElement</code> is called on successive list elements to build up the new list, which is finally returned as result of the command. </p>
<pre>int
Tcl_LreverseObjCmd(notUsed, interp, objc, objv)
 ClientData notUsed; /* Not used. */
 Tcl_Interp *interp; /* Current interpreter. */
 int objc; /* Number of arguments. */
 Tcl_Obj **obj; /* Argument strings. */
{
 int listObjc, lowListIndex, hiListIndex;
 Tcl_Obj **listObjv;
 char *temp, *resultList;
 Tcl_Obj **newListObjv;
 /* Verify argument count. Since we take only one argument, argument
 * count must be 2 (command plus one argument).
 */
 if (objc != 2)
 return TclX_WrongArgs (interp, objv [0], &quot;list&quot;);
 /* Create an object to handle the new list we're creating */
 newListObjv = Tcl_NewObj();
 /* Crack the list at objv[1] into its own count and array of object
 * pointers.
 */
 if (Tcl_ListObjGetElements (interp, objv[1], &amp;listObjc, &amp;listObjv) != TCL_OK) {
 return TCL_ERROR;
 }
 /* For each element in the source list from last to first, append an
 * element to the new list.
 */
 for (listIndex = listObjc - 1; listIndex &gt;= 0; listIndex--) {
 Tcl_ListObjAppendElement (interp, newListObjv, listObjv[listIndex]);
 }
FIX: NEED TO RETURN THE LIST.
 return TCL_OK;
}</pre>
<h2>Installing Your Command</h2>
<p>To install your command into Tcl you must call <code>Tcl_CreateObjCommand</code>, passing it the pointer to the interpreter you want to install the command into, the name of the command, a pointer to the C function that implements the command, a client data pointer, and a pointer to an optional callback routine. </p>
<p> The client data pointer and the callback routine will be described later. </p>
<p> For example, for the max function above (which, incidentally, comes from TclX&#8217;s tclXmath.c in the <i>TclX7.4/src</i> directory): </p>
<pre> Tcl_CreateCommand (interp, &quot;max&quot;, Tcl_MaxCmd, (ClientData)NULL, 
 (void (*)())NULL);</pre>
<p>In the above example, the max function is added to the specified interpreter. The client data pointer and callback function pointer are NULL. (For complete information on <code>Tcl_CreateCommand</code> and its companion routine, <code>Tcl_CommandInfo</code>, please examine the <code><a href="/docs/linux/man/3-crtcommand/">CrtCommand</a></code>(3) command page in the core Tcl distribution.) </p>
<h2>Dynamic Strings</h2>
<p><i>Dynamic strings</i> are an important abstraction that first became available with Tcl 7.0. Dynamic strings, or <i>DStrings</i>, provide a way to build up arbitrarily long strings through a repeated process of appending information to them. DStrings reduce the amount of allocating and copying required to add information to a string. Further, they simplify the process of doing so. </p>
<p> At first glance, it may seem that the object system supersedes DStrings. It does not, in that the performance improvements made possible by the lazy conversion of an object&#8217;s representation from one datatype to another does not come into play much while constructing strings as the string representation is always available either without any type conversion or where type conversion would be necessary in any case as a string representation of the object is required when strings are being constructed by concatenation, etc. </p>
<p> It should be noted, however, that the C level string manipulation capabilites of objects, such as <code>Tcl_AppendToObj</code> and <code>Tcl_AppendStringsToObj</code>, are often plenty enough for what you need to do. For complete information on dynamic strings, please examine the <code><a href="/docs/linux/man/3-dstring/">DString</a></code>(3) manual page in the core Tcl distribution. For more on Tcl object&#8217;s string-oriented calls, seek <code><a href="/docs/linux/man/3-tcl_stringobj/">Tcl_StringObj</a></code>(3) in the same location. </p>
<h2>Client Data</h2>
<p>The client data pointer provides a means for Tcl commands to have data associated with them that is not global to the C program nor included in the Tcl core. Client data is essential in a multi-interpreter environment (where a single program has created and is making use of multiple Tcl interpreters) for the C routines to maintain any permanent data they need on a per-interpreter basis. If needed static data was simply declared static in C, you will probably have reentrancy problems when you work with multiple interpreters. </p>
<p> Tcl solves this through the client data mechanism. When you are about to call <code>Tcl_CreateObjCommand</code> to add a new command to an interpreter, if your command needs to keep some read/write data across invocations, you should allocate the space, preferably using <code>Tcl_Alloc</code> instead of <code>malloc</code>, then pass the address of that space as the ClientData pointer to <code>Tcl_CreateObjCommand</code>. </p>
<p> When your command is called from Tcl, the ClientData pointer you passed to <code>Tcl_CreateObjCommand</code> will be passed to your C routine through the ClientData pointer calling argument. </p>
<p> Commands that need to share this data with one another can do so by using the same ClientData pointer when the commands are added. </p>
<p> It is important to note that the Tcl extensions in the <i>tclX8.0.0</i> directory have had all of their data set up in this way. Since release 6.2, Extended Tcl has supported multiple interpreters within one invocation of Tcl.</p>
<h2>Theory Of Handles</h2>
<p>Sometimes you need to have a data element that isn&#8217;t readily representable as a string within Tcl, for example a pointer to a complex C data structure. It is not a good idea to try to pass pointers around within Tcl as strings by converting them to and from hex or integer representations, for example. It is too easy to mess one up, and the likely outcome of doing that is a core dump. </p>
<p> Instead we have developed and made use of the concept of <i>handles</i>. Handles are identifiers a C extension can pass to, and accept from, Tcl to make the transition between what your C code knows something as and what name Tcl knows it by to be as safe and painless as possible. For example, the I/O system included in Tcl uses file handles. When you open a file from Tcl, a handle is returned of the form <code>file</code><i>n</i> where <i>n</i> is a file number. When you pass the file handle back to <i>puts</i>, <i>gets</i>, <i>seek</i>, <i>flush</i> and so forth, they validate the file handle by checking the the <code>file</code> text is present, then converting the file number to an integer that they use to look into a data structure of pointers to Tcl open file structures, which contain a Unix file descriptor, flags indicating whether or not the file is currently open, whether the file is a file or a pipe and so forth. </p>
<p> Handles have proven so useful that, since TclX release 6.1a, general support has been available to help create and manipulate them. Many of these capabilities have migrated into baseline Tcl. If you have a similar need, you might like to use the handle routines documented in <code><a href="/docs/linux/man/3-handles/">Handles</a></code>(3) in Extended Tcl. We recommend that you use a unique-to-your-package textual handle coupled with a specific identifier and let the handle management routines validate it when it&#8217;s passed back. It is much easier to track down a bug with an implicated handle named something like <code>file4</code> or <code>bitmap6</code> than just <code>6</code>. </p>
<p> Note that Tcl&#8217;s object offers another way for complex data structures to exist in parallel with and underneath Tcl strings. As of this writing (May 30, 1997) this is fairly new territory, but things are looking good for the prospects of using the Tcl object system in this manner, and for enhancements to the object system that allow even Tcl objects to have methods in a very straightforward and simple way.</p>
<h2>Using Commands To Do The Same Thing, And More</h2>
<p>Another handle-like technique, first popularized in the Tk toolkit, offers handle-like capabilities as well as some neat additional capabilities. That is to create a new Tcl command, from C, that uses ClientData to keep a &quot;handle&quot; on its complex underlying data structure. Then by having that command look at its second argument for what it is to do (its sub-functions), you get these nice methods, where you have several additional sub-commands that don&#8217;t pollute the global namespace and only work on (and are available with) the objects (new commands) they are relevant to. For example, in Tk, creating a checkbutton (<code>checkbutton .b) creates a new Tcl command (.b), that has methods to configure the button, select, deselect, toggle and flash it. </p>
<p> A lot of people think this is really the way to go, and I am pretty much leaning that way myself. If you use the incr tcl</code> script-level object system for Tcl, objects that you define in Tcl will be highly compatible in terms of their command interfaces and configuration management with objects you create in C using the the command-and-ClientData technique described here. I believe <code>Tk</code> has some nice facilities for making this easy for the Tcl programmer. <code>Itcl</code> certainly does. </p>
<h2>Tracking Memory Corruption Problems</h2>
<p>Occasionally you may write code that scribbles past the end of an allocated piece of memory. This will usually result in a core dump or memory allocation failure sometime later in the program, often implicating code that is not actually responsible for the problem (as you start looking from the point where the error is detected, which is usually where the later routine has failed). </p>
<p> The memory debugging routines included in Tcl can help find these problems. Developed by Mark and Karl, the memory debugging routines are now part of baseline Tcl, and is to our knowledge the largest piece of TclX to drop into the core without being reengineered first. (You see, summer back in &#8217;91, John was sitting in his office in the CS building at UC Berkeley trying to find a memory leak somewhere in Tcl, when he was paid a visit by two long-haired-yet-polite programmers bearing gifts in the form of the technology grab-bag known as Extended Tcl. He saw that, using TclX&#8217;s malloc routines, Tcl could be prompted to print the filename and line number of every single memory allocation that did not have a corresponding free. It was just what the doctor ordered ;-) See <i>Memory(TCL)</i> for details. </p>
<h2>Installing Your Extensions Into Tcl</h2>
<p>To add your extensions to Tcl, you used to have to statically link them, together with any other extensions, into a single binary executable image. Today, although the statically linked executable is still an option, most operating systems, even Microsoft Windows, support shared libraries, and in most cases, Tcl can now make use of those shared libraries such that you extensions, and most others, can now be built a shared libraries that can be loaded in (using <code>package require</code>) by scripts that need them. Shared libraries can simplify a Tcl installation, because only one copy of Tcl is required, rather than a hodepodge of combinations of applications that you might have found at a big Tcl site in the previous era.</p>
<h2>Gnu Autoconf</h2>
<p>While the build procedure for shared libraries varies from system to system, most Unix and Unix workalike systems will figure out the nuances of the compiler and linker arguments automatically when the <i>configure</i> script is run. If you are building a package that you plan to make generally available, we strongly recommend that you use <code>GNU autoconf</code> (<a href="ftp://prep.ai.mit.edu/pub/gnu)">ftp://prep.ai.mit.edu/pub/gnu)</a> to set up an automatic <i>configure</i> script for it. Be forewarned that <i>autoconf</i> uses some pretty heavy duty shell and sed script magic to get the job done, and the learning curve can be pretty steep. Once done and shaken out, though, it&#8217;s rewarding to know that your package can build and run on everything from a notebook to a Cray to a RISC SMP server. </p>
<p> Application-specific startup is accomplished by creating or editing the <i>Tcl_AppInit</i> function. In <i>Tcl_AppInit</i> you should add a call to an application-specific init function which you create. This function should take the address of the interpreter it should install its commands into, and it should install those commands with <code>Tcl_CreateCommand</code> and do any other application-specific startup that is necessary. </p>
<p> The naming convention for application startup routines is <code>App_Init</code>, where <i>App</i> is the name of your application. For example, to add an application named <i>cute</i> one would create a <i>Cute_Init</i> routine that expected a <code>Tcl_Interp</code> pointer as an argument, and add the following code to <i>Tcl_AppInit</i>: </p>
<pre> if (Cute_Init (interp) == TCL_ERROR) {
 return TCL_ERROR;
 }</pre>
<p>As you can guess from the above example, if your init routine is unable to initialize, it should use <code>Tcl_AppendResult</code> to provide some kind of useful error message back to TclX, then return <code>TCL_ERROR</code> to indicate that an error occurred. If the routine executed successfully, it should return <code>TCL_OK</code>. </p>
<p> When you examine <i>Tcl_AppInit</i>, note that there is one call already there to install an application &#8212; the call to <i>TclX_Init</i> installs Extended Tcl into the Tcl core. </p>
<h2>Making Application Information Visible From Extended Tcl</h2>
<p>TclX&#8217;s <code>infox</code> command can return several pieces of information relevant to Extended Tcl, including the application&#8217;s name, descriptive name, patch level and version. Your application&#8217;s startup can set these variables to application-specific values. If it doesn&#8217;t, they are given default values for Extended Tcl. </p>
<p> To set these values, first be sure that you include either <code>tclExtend.h</code> or <code>tclExtdInt.h</code> from the source file that defines your init routine. This will create external declarations for the variables. Then, set the variables in your init route, for example: </p>
<pre> tclAppName = &quot;cute&quot;;
 tclAppLongName = &quot;Call Unix/Tcl Environment&quot;;
 tclAppVersion = &quot;2.1&quot;;</pre>
<p>Note that the default values are set by <i>TclX_Init</i>, so if you wish to override them, you must call your init routine in <i>Tcl_AppInit</i> after its call to <i>TclX_Init</i>. </p>
<h2>Extended Tcl Exit</h2>
<p>When Extended Tcl exits, <code>Tcl_DeleteInterp</code> may be called to free memory used by Tcl &#8212; normally, this is only called if <code>TCL_MEM_DEBUG</code> was defined, since Unix will return all of the allocated memory back to the system, anyway. If <code>TCL_MEM_DEBUG</code> was defined, it is called so that any memory that was allocated without ever being freed can be detected. This greatly reduces the amount of work to detect and track down memory leaks, a situation where some piece of your code allocates memory repeatedly without ever freeing it, or at least without always freeing it. </p>
<p> It is often necessary for an application to perform special cleanup functions upon the deletion of an interpreter as well. To facilitate this activity, Tcl provides the ability to perform a function callback when an interpreter is deleted. To arrange for a C function to be called when the interpreter is deleted, call <code>Tcl_CallWhenDeleted</code> from your application initialization routine. For details on how to use this function, read the <code><a href="/docs/linux/man/3-calldel/">CallDel</a></code>(3) manual page that ships with core Tcl. </p>
<h2>Executing Tcl Code From Your C Extension</h2>
<p>Suppose you are in the middle of coding a C extension and you realize that you need some operation performed, one that would be simple from Tcl, but possibly excruciating to do directly in C. Tcl provides a number of C-level interfaces whereby you can cause Tcl code to be executeed. The old-style calls are <code>Tcl_Eval</code>, <code>Tcl_VarEval</code>, <code>Tcl_EvalFile</code> and <code>Tcl_GlobalEval</code>. The results of these calls can be dug out of the interpreter using <code>Tcl_GetStringResult</code>, if you want a string representation of the result, or <code>Tcl_GetObjResult</code> if you want the object. (The use of <code>interp-&gt;result</code> to access the result string has been deprecated.) </p>
<p> The Tcl object system adds <code>Tcl_EvalObj</code> and <code>Tcl_GlobalEvalObj</code>. The difference here is that we are evaluating an object, not just a string, and using these routines in preference to the aforementioned ones can result in a major performance improvement in your code, when the code is executed repeatedly (even if it only executes once but loops several times within itself), as these routines make it possible for the bytecode compiler to compile the code being evaluated and save the compiled code with the data structure, in an implementation-dependent manner. </p>
<p> For more information please consult the <code><a href="/docs/linux/man/3-evalobj/">EvalObj</a></code>(3) and <code><a href="/docs/linux/man/3-eval/">Eval</a></code>(3) manual pages within the Tcl distribution. </p>
<h2>Accessing Tcl Variables And Arrays From Your C Extensions</h2>
<p>In addition to the non-object-system ways of reading from and storing to Tcl variables, using routines such as <code>Tcl_SetVar2</code> and <code>Tcl_GetVar2</code>, Tcl variables and arrays can be read from a C extension as Tcl objects by using the <code>Tcl_ObjGetVar2</code> function, and set from C extensions through the <code>Tcl_ObjSetVar2</code> function. </p>
<p> Please note that the object versions do not carry forward analogues to the one-variable-name-argument <code>Tcl_GetVar</code>, <code>Tcl_SetVar</code>, and <code>Tcl_UnsetVar</code>. If you know you have a scalar, call the object variable get and set functions with a NULL second argument. If your variable name might contain an array reference via a self-contained embedded array index (i.e., I&#8217;m asking <code>Tcl_ObjGetVar2</code> for <code>&quot;<a href="/docs/linux/man/5-foo/">foo</a>(5)&quot;</code> instead of <code>&quot;foo&quot; &quot;5&quot;</code>), add the <code>TCL_PARSE_PART1</code> to the flags in your call. </p>
<p> While the fact that <code>Tcl_ObjGetVar2</code> retrieves Tcl objects, rather than strings, is critical for the object system to be able to provide the performance boosts from &quot;lazy&quot; type conversion and the binary data capabilities, the arguments containing the variable name, or the array name and element name if they&#8217;ve been split out, also must be specified as Tcl objects rather than strings. While this is useful on occasion, those writing C extensions for Tcl in the post-object-system era usually have the names available as plain old <i>char *</i> variables, requiring conversion of the strings to objects before use and account for their possible destruction afterwards. </p>
<p> To simplify the task in those cases, TclX adds the <code>TclX_ObjGetVar2S</code> subroutine. It works just like <code>Tcl_ObjGetVar2</code>, except the one or two variable name arguments are specified as strings, and the routine takes care of making and disposing of object equivalents. </p>
<p> Tcl variables can be unset from C via the <code>Tcl_UnsetVar</code> and <code>Tcl_UnsetVar2</code> functions. There are currently (as of 8.0) no object-system equivalents, so in the rare case where you have the name of the variable you want unset as an object instead of a string, you can call <code>Tcl_GetStringFromObj</code> to obtain the string representation first. </p>
<p> For complete information on these functions, please refer to the <code><a href="/docs/linux/man/3-objsetvar/">ObjSetVar</a></code>(3) and <code><a href="/docs/linux/man/3-setvar/">SetVar</a></code>(3) manual pages in the <i>doc</i> directory of the core Tcl distribution. </p>
<h2>Linking Tcl Variables To C Variables</h2>
<p><code>Tcl_LinkVar</code> and <code>Tcl_UnlinkVar</code> can be used to automatically keep Tcl variables synchronized with corresponding C variables. Once a Tcl variable has been linked to a C variable with <code>Tcl_LinkVar</code>, anytime the Tcl variable is read, the value of the C variable is converted (if necessary) and returned, and when the Tcl variable is written, the C variable will be updated with the new value. </p>
<p> <code>Tcl_LinkVar</code> uses variable traces to keep the Tcl variable named by <i>varName</i> in sync with the C variable at the address given by <i>addr</i>. </p>
<p> <i>Int</i>, <i>double</i>, <i>boolean</i> and <i>char *</i> variables are supported. You can make your linked variables read only from the Tcl side, as well. Please note that the C variables must continually exist while they are linked, in other words, linking &quot;automatic&quot; C variables, those created on the stack while a routine is being executed and destroyed afterwards, will result in a malfunctioning program at best and a coredump or more at worst. </p>
<p> For more information, please examine the <code><a href="/docs/linux/man/3-linkvar/">LinkVar</a></code>(3) manual page in the core Tcl distribution. </p>
<h2>Adding New Math Functions To Tcl</h2>
<p>As of Tcl version 7.0, math functions such as <i>sin</i>, <i>cos</i>, etc, are directly supported within Tcl expressions. These obsolete the Extended Tcl commands that provided explicit commands for these functions for many, many releases, although procs equivalencing the old TclX commands to the new math functions are still provided for backwards compatibility. </p>
<p> New math functions can be added to Tcl, or existing math functions can be replaced, by calling <code>Tcl_CreateMathFunc</code>. </p>
<h2>Accessing And Manipulating The Random Number Generator</h2>
<p>Prior to Tcl version 8.0, the Tcl core did not provide access to a random number generator, but TclX did, through its <i>random</i> command. As of Tcl version 8.0, access to a random number generator is provided by baseline Tcl through the new math functions, <i>rand</i> and <i>srand</i>. </p>
<p> The TclX <i>random</i> command is still available &#8212; it has some useful capabilities not directly provided by the new baseline functions. </p>
<p> For more information on adding your own math functions to Tcl, please study the <code><a href="/docs/linux/man/3-crtmathfnc/">CrtMathFnc</a></code>(3) manual page in the core Tcl distribution. </p>
<h2>Converting Filenames To Native Form And Performing Tilde Substitutions</h2>
<p>The <code>Tcl_TranslateFileName</code> function is available to C extension writers to translate filenames to a form suitable for use by the local operating system. It converts network names to their native form, and if the name starts with a &#8220;~&#8221; character, the function returns a new string where the name is replaced with the home directory of the given user. </p>
<p> For more information please consult the <code><a href="/docs/linux/man/3-translate/">Translate</a></code>(3) manual page in the core Tcl distribution. </p>
<h2>Setting The Recursion Limit</h2>
<p>Tcl has a preset recursion limit that limits the maximum allowable nesting depth of calls within an interpreter. This is useful for detecting infinite recursions before other limits such as the process memory limit or, worse, available swap space on the system, run out. </p>
<p> The default limit is just a guess, however, and applications that make heavy use of recursion may need to call <code>Tcl_SetRecursionLimit</code> to raise this limit. For more information, please consult the <code><a href="/docs/linux/man/3-setreclmt/">SetRecLmt</a></code>(3) manual page in the core Tcl distribution. </p>
<h2>Handling Signals From Tcl Extensions</h2>
<p>If an event such as a signal occurs while a Tcl script is being executed, it isn&#8217;t safe to do much in the signal handling routine &#8212; the Tcl environment cannot be safely manipulated at this point because it could be in the middle of some operation, such as updating pointers, leaving the interpreter in an unreliable state. </p>
<p> The only safe approach is to set a flag indicating that the event occurred, then handle the event later when the interpreter has returned to a safe state, such as after the current Tcl command completes. </p>
<p> The <code>Tcl_AsyncCreate</code>, <code>Tcl_AsyncMark</code>, <code>Tcl_AsyncInvoke</code>, and <code>Tcl_AsyncDelete</code> functions provide a safe mechanism for dealing with signals and other asynchronous events. For more information on how to use this capability, please refer to the <code><a href="/docs/linux/man/3-async/">Async</a></code>(3) manual page in the core Tcl distribution. </p>
<p> Note that Extended Tcl provides built-in support for managing signals in numerous ways, including generating them with <i><a href="/docs/linux/man/2-alarm/">alarm</a></i>(2) and <i><a href="/docs/linux/man/2-kill/">kill</a></i>(2), ignoring them, trapping them, getting, setting, blocking and unblocking them. You can cause specific code to execute at a safe point after a signal occurs, or cause a Tcl error backtrace on one&#8217;s occurrence. For more information, please examine the TclX documentation. </p>
<h2>Parsing Backslash Sequences</h2>
<p>The <code>Tcl_Backslash</code> function is called to parse Tcl backslash sequences. These backslash sequences are the usual sort that you see in the C programming language, such as <code>
</code> for newline, <code></code> for return, and so forth. <code>Tcl_Backslash</code> parses a single backslash sequence and returns a single character corresponding to the backslash sequence. </p>
<p> For more info on this call, look at the <code><a href="/docs/linux/man/3-backslash/">Backslash</a></code>(3) manual page in the core Tcl distribution. For information on the valid backslash sequences, consult the summary of Tcl language syntax, <code><a href="/docs/linux/man/n-tcl/">Tcl</a></code>(n) in the same distribution. </p>
<h2>Hash Tables</h2>
<p><i>Hash tables</i> provide Tcl with a high-performance facility for looking up and managing key-value pairs located and maintained in memory. Tcl uses hash tables internally to locate procedure definitions, Tcl variables, array elements, file handles and so forth. Tcl makes the hash table functions accessible to C extension writers as well. </p>
<p> Hash tables grow automatically to maintain efficiency, rather than exposing the table size to the programmer at allocation time, which would needlessly add complexity to Tcl and would be prone to inefficiency due to the need to guess the number of items that will go into the table, and the seemingly inevitable growth in amount of data processed per run over the useful life of the program. </p>
<p> For more information on hash tables, please consult the <code><a href="/docs/linux/man/3-hash/">Hash</a></code>(3) manual page in the core Tcl distribution. </p>
<h2>Tracing Variable Accesses</h2>
<p>The C extension writer can arrange to have a C routine called whenever a Tcl variable is read, written, or unset. Variable traces are the mechanism by which Tk toolkit widgets such as radio and checkbuttons, messages and so forth update without Tcl programmer intervention when their data variables are changed. They are also used by the routine that links Tcl and C variables, <code>Tcl_LinkVar</code>, described above. </p>
<p> <code>Tcl_TraceVar</code> is called to establish a variable trace. Entire arrays and individual array elements can be traced as well. If the programmer already has an array name in one string and a variable name in another, <code>Tcl_TraceVar2</code> can be called. Calls are also available to request information about traces and to delete them. </p>
<p> For more information on variable traces, consult the <code><a href="/docs/linux/man/3-tracevar/">TraceVar</a></code>(3) manual page in the core Tcl distribution. </p>
<h2>Tracing Tcl Execution</h2>
<p>Tcl has the ability to call C routines each time it executes a Tcl command, up to a specified depth of nesting levels. The command <code>Tcl_CreateTrace</code> creates an execution trace; <code>Tcl_DeleteTrace</code> deletes it. </p>
<p> Command tracing is used in Extended Tcl to implement the <i>cmdtrace</i> Tcl command, a useful command for debugging Tcl applications. </p>
<p> For complete information on execution tracing, please look at the <code><a href="/docs/linux/man/3-crttrace/">CrtTrace</a></code>(3) manual pages in the core Tcl distribution. </p>
<h2>Evaluating Tcl Expressions From C</h2>
<p><code>Tcl_ExprLong</code>, <code>Tcl_ExprDouble</code>, <code>Tcl_ExprBool</code>, and <code>Tcl_ExprString</code> all take string arguments and, when called, evaluate those strings as Tcl expressions. Depending on the routine called, the result is either a C <i>long</i>, a <i>double</i>, a boolean (<i>int</i> with a value of <code>0</code> or <i>1</i>), or a <i>char *</i> (obtainable through <code>Tcl_GetResult</code>). </p>
<p> To take advantage of the performance gains available through the bytecode compiler, <code>Tcl_ExprLongObj</code>, <code>Tcl_ExprDoubleObj</code>, <code>Tcl_ExprBoolObj</code>, and <code>Tcl_ExprObj</code> all take an object containing an expression to be evaluated (rather than a string.) The result is that bytecode-compiled version of the expression will be kept in the object, alongside the string representation. If the expression is evaluated again, without being changed, it does not have to be recompiled&#8230; a major performance win. </p>
<p> For complete information on evaluating Tcl expressions from C, you are invited to examine the <code><a href="/docs/linux/man/3-exprlong/">ExprLong</a></code>(3) and <code><a href="/docs/linux/man/3-exprlongobj/">ExprLongObj</a></code>(3) manpages in the core Tcl distribution. </p>
<h2>Pattern Matching</h2>
<p>The <code>Tcl_StringMatch</code> function can be called to see if a string matches a specified pattern. <code>Tcl_StringMatch</code> is called by the Tcl <i>string match</i> command, so the format for patterns is identical. The pattern format is similar to the one used by the C-shell; <code><a href="/docs/linux/man/n-string/">string</a></code>(n) describes this format. </p>
<p> More information about <code>Tcl_StringMatch</code> is available in the <code><a href="/docs/linux/man/3-strmatch/">StrMatch</a></code>(3) manpage in the core Tcl distribution. </p>
<h2>Regular Expression Pattern Matching</h2>
<p><code>Tcl_RegExpMatch</code> can be called to determine whether a string matches a regular expression. <code>Tcl_RegExpMatch</code> is used internally by the <i>regexp</i> Tcl command. </p>
<p> As regular expressions are typically &quot;compiled&quot; before use, a fairly involved process, Tcl also supports routines that separate the compilation of an expression from its use: <code>Tcl_RegExpCompile</code>, <code>Tcl_RegExpExec</code>, and <code>Tcl_RegExpRange</code>. If an expression is going to be matched many times, doing the compile once and caching the compiled regular expression result, then reusing the cached version by using <code>Tcl_RegExpExec</code>, can be a significant performance win. </p>
<p> For more information on this function, please consult the <code><a href="/docs/linux/man/3-regexp/">RegExp</a></code>(3) manpage in the core Tcl distribution. </p>
<h2>Manipulating Tcl Lists From C Extensions</h2>
<p>The C extension writer often needs to create, manipulate and decompose Tcl lists. <code>Tcl_SplitList</code> and <code>Tcl_Merge</code> used to be the only way to parse strings into lists and vice versa. As of Tcl 8, lists can be parsed and assembled, object-style, using <code>Tcl_ListObjGetElements</code> and <code>Tcl_SetListObj</code>, and friends. Once again the &quot;win&quot; of using object-system-based list manipulation, instead of the previous string based routines, is that the parsing of a string in an object to a list is cached in the object structure, the same as with integers and floating point numbers, compiled procedures, etc. The next time this string needs to be looked at as a list, if the contents of the string have not changed, the string does not have to be parsed. </p>
<p> In the author&#8217;s experience, working with an admittedly degenerate test whereby we iterated rather inefficiently across a 6,000-element list, a speedup factor of more than 2500 was obtained over the previous non-object-based version of Tcl. </p>
<p> For more information on these commands, please consult the <code><a href="/docs/linux/man/3-listobj/">ListObj</a></code>(3) manual page in the core Tcl distribution. </p>
<h2>Concatenating Strings</h2>
<p><code>Tcl_ConcatObj</code> concatenates the string representation of zero or more objects into a single new object. The elements of the new string are space-separated. <code>Tcl_Concat</code> does the same thing for strings, as <code>Tcl_ConcatObj</code> does for objects. </p>
<p> Concatenating strings is similar to constructing lists from them, except that <code>Tcl_ConcatObj</code> and <code>Tcl_Concat</code> do not attempt to make the resulting string into a valid Tcl list. </p>
<p> <code>Tcl_Concat</code> is documented in the <code><a href="/docs/linux/man/3-concat/">Concat</a></code>(3) manpage, and <code>Tcl_ConcatObj</code> in the <code>tringObj</code> manpage, both in the core Tcl distribution. </p>
<h2>Detecting Whether Or Not You Have A Complete Command</h2>
<p>C routines that collect data to form a command to be passed to <i>Tcl_Eval</i> often need a way to tell whether they have a complete command already or whether they need more data. (Programs that read typed-in Tcl input such as Tcl shells need this capability, for instance.) <code>Tcl_CommandComplete</code> can be used to tell whether or not you have a complete command. </p>
<p> For more information examine <code><a href="/docs/linux/man/3-cmdcmplt/">CmdCmplt</a></code>(3) in the core Tcl distribution. </p>
<h2>Recording Commands For Command History</h2>
<p>Tcl has a history mechanism that is accessed from Tcl through the <i>history</i> command. If you want your extension to propagate commands into the command history, you should call <i>Tcl_RecordAndEvalObj</i> (object system) or <i>Tcl_RecordAndEval</i> (old system), </p>
<p> These commands work like <i>Tcl_EvalObj</i> and <i>Tcl_Eval</i>, respectively, except that these versions record the command as well as executing it. </p>
<p> <i>Tcl_RecordAndEval</i> and <i>Tcl_RecordAndEvlObj</i> should only be called with user-entered top-level commands, since the history mechanism exists to allow the user to easily access, edit and reissue previously issued commands. </p>
<p> For complete information on these functions, please examine the <code>RecordEval</code>.3 and <code>RecEvalObj</code>.3 manual pages in the core Tcl distribution. </p>
<h2>Converting Floating Point Values To Strings</h2>
<p>The Tcl object system&#8217;s <code>Tcl_GetDoubleFromObj</code> and <code>Tcl_SetDoubleObj</code> use Tcl objects, rather than the strings used by <code>Tcl_PrintDouble</code>, and convert, when necessary, an ASCII string to a <i>double</i> and back again. </p>
<p> These routines ensure that the string output will continue to be interpretable as a floating point number, rather than an integer, by always putting a &#8220;.&#8221; or &#8220;e&#8221; into the string representing the number. </p>
<p> The precision of the output string is controlled by the Tcl <code>tcl_precision</code> variable. </p>
<p> For complete information on these routines, please examine <code><a href="/docs/linux/man/3-doubleobj/">DoubleObj</a></code>(3) and <code><a href="/docs/linux/man/3-printdbl/">PrintDbl</a></code>(3) in the core Tcl distribution. </p>
<h2>Creating Child Processes And Pipelines From C</h2>
<p><code>Tcl_OpenCommandChannel</code> provides a C-level interface to the <code>exec</code> and <code>open</code> commands. The child (or pipeline of children) can have its standard input, output and error redirected from files, variables or pipes. To understand the meaning of the redirection symbols understood by this function, look at the <code><a href="/docs/linux/man/n-exec/">exec</a></code>(n) Tcl command. For complete information on <code>Tcl_OpenCommandChannel</code>, please examine <code><a href="/docs/linux/man/3-openfilechnl/">OpenFileChnl</a></code>(3). </p>
<h2>Accessing Tcl Filehandles From C</h2>
<p>On Posix/Unix systems, Tcl filehandles passed to your C extension can be translated to a Posix <i>FILE *</i> structure using the <code>Tcl_GetOpenFile</code> function, documented in <code>GetOpnFl</code>.3. </p>
<h2>Managing Background Process Termination And Cleanup</h2>
<p>When a Posix system does a <i>fork</i> to create a new process, the process ID of the child is returned to the caller. After the child process exits, its process table entry (and some other data associated with the process) cannot be reclaimed by the operating system until a call to <i>waitpid</i>, or one of a couple of other, similar system calls, has been made by the parent process. </p>
<p> The C extension writer who has created a subprocess, by whatever mechanism, can turn over responsibility for detecting the processes&#8217; termination and calling <i>waitpid</i> to obtain its exit status, by calling <code>Tcl_DetachPids</code> on it. </p>
<p> <code>Tcl_ReapDetachedProcs</code> is the C routine that will detect the termination of any processes turned over to Tcl, permitting the processes to be fully reclaimed by the operating system. It is usually not necessary to call <code>Tcl_ReapDetachedProcs</code>, as it is called automatically every time <code>exec</code> is performed. </p>
<p> For complete information on these routines, please look at <i><a href="/docs/linux/man/3-detachpids/">DetachPids</a>(3)</i> in the core Tcl distribution. </p>
<h2>For More Information</h2>
<p>In addition to the documentation referenced above, you can learn a lot by studying the source code of the commands added by Tcl, Tk and Extended Tcl, etc. The <i>comp.lang.tcl</i> Usenet newsgroup is read by hundreds of thousands of Tcl people. A number of Frequently Asked Questions (FAQs) about Tcl are posted there periodically. The newsgroup is a good place to ask questions (after you&#8217;ve made sure they&#8217;re not already answered in the FAQ ;-) </p>
<p> Finally, if you have interactive Internet access, you can ftp to <i><a href="ftp://ftp.neosoft.com/pub/tcl">ftp://ftp.neosoft.com/pub/tcl</a></i>, the site for contributed Tcl sources. This site contains quite a few extensions, applications, and so forth, including several object-oriented extension packages. </p>
<p> If you have access via the world-wide web, check out the Sun Microsystems site (<i><a rel="nofollow" href="http://sunscript.sun.com">http://sunscript.sun.com</a></i>), the contributed sources archive website (<i><a rel="nofollow" href="http://www.neosoft.com/tcl">http://www.neosoft.com/tcl</a></i>), and the homepage for Extended Tcl (<i><a rel="nofollow" href="http://www.neosoft.com/tclx">http://www.neosoft.com/tclx</a></i>). </p>
<h2>Authors</h2>
<p>Extended Tcl was created by Karl Lehenbauer (karl [at] neosoft.com) and Mark Diekhans (markd [at] grizzly.com).</p>
