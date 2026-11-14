---
title: "tk_createimagetype(3)"
name: "tk_createimagetype"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_createimagetype/"
description: "Tk_CreateImageType, Tk_GetImageMasterData, Tk_InitImageArgs – define new kind of image"
---

<p>Tk_CreateImageType, Tk_GetImageMasterData, Tk_InitImageArgs &#8211; define new kind of image </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_CreateImageType</code>(<i>typePtr</i>)
ClientData
<code>Tk_GetImageMasterData</code>(<i>interp, name, typePtrPtr</i>)
<code>Tk_InitImageArgs</code>(<i>interp, argc, argvPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_ImageType <i>*typePtr</i> (in) Structure that defines the new type of image. Must be static: a pointer to this structure is retained by the image code.</p>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which image was created.</p>
<dd>const char <i>*name</i> (in) Name of existing image.</p>
<dd>Tk_ImageType <i>**typePtrPtr</i> (out) Points to word in which to store a pointer to type information for the given image, if it exists.</p>
<dd>int <i>argc</i> (in) Number of arguments</p>
<dd>char <i>***argvPtr</i> (in/out) Pointer to argument list </p>
</dl>
<h2>Description</h2>
<p><code>Tk_CreateImageType</code> is invoked to define a new kind of image. An image type corresponds to a particular value of the <i>type</i> argument for the <code>image create</code> command. There may exist any number of different image types, and new types may be defined dynamically by calling <code>Tk_CreateImageType</code>. For example, there might be one type for 2-color bitmaps, another for multi-color images, another for dithered images, another for video, and so on. </p>
<p> The code that implements a new image type is called an <i>image manager</i>. It consists of a collection of procedures plus three different kinds of data structures. The first data structure is a Tk_ImageType structure, which contains the name of the image type and pointers to five procedures provided by the image manager to deal with images of this type:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tk_ImageType {
 char *<i>name</i>;
 Tk_ImageCreateProc *<i>createProc</i>;
 Tk_ImageGetProc *<i>getProc</i>;
 Tk_ImageDisplayProc *<i>displayProc</i>;
 Tk_ImageFreeProc *<i>freeProc</i>;
 Tk_ImageDeleteProc *<i>deleteProc</i>;
} Tk_ImageType;</pre>
</dl>
<p> The fields of this structure will be described in later subsections of this entry. </p>
<p> The second major data structure manipulated by an image manager is called an <i>image master</i>; it contains overall information about a particular image, such as the values of the configuration options specified in an <code>image create</code> command. There will usually be one of these structures for each invocation of the <code>image create</code> command. </p>
<p> The third data structure related to images is an <i>image instance</i>. There will usually be one of these structures for each usage of an image in a particular widget. It is possible for a single image to appear simultaneously in multiple widgets, or even multiple times in the same widget. Furthermore, different instances may be on different screens or displays. The image instance data structure describes things that may vary from instance to instance, such as colors and graphics contexts for redisplay. There is usually one instance structure for each <code>-image</code> option specified for a widget or canvas item. </p>
<p> The following subsections describe the fields of a Tk_ImageType in more detail. </p>
<h3>Name</h3>
<p><i>typePtr-&gt;name</i> provides a name for the image type. Once <code>Tk_CreateImageType</code> returns, this name may be used in <code>image create</code> commands to create images of the new type. If there already existed an image type by this name then the new image type replaces the old one. </p>
<h3>Createproc</h3>
<p><i>typePtr-&gt;createProc</i> provides the address of a procedure for Tk to call whenever <code>image create</code> is invoked to create an image of the new type. <i>typePtr-&gt;createProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageCreateProc(
 Tcl_Interp *<i>interp</i>,
 char *<i>name</i>,
 int <i>objc</i>,
 Tcl_Obj *const <i>objv</i>[],
 Tk_ImageType *<i>typePtr</i>,
 Tk_ImageMaster <i>master</i>,
 ClientData *<i>masterDataPtr</i>);</pre>
</dl>
<p> The <i>interp</i> argument is the interpreter in which the <code>image</code> command was invoked, and <i>name</i> is the name for the new image, which was either specified explicitly in the <code>image</code> command or generated automatically by the <code>image</code> command. The <i>objc</i> and <i>objv</i> arguments describe all the configuration options for the new image (everything after the name argument to <code>image</code>). The <i>master</i> argument is a token that refers to Tk&#8217;s information about this image; the image manager must return this token to Tk when invoking the <code>Tk_ImageChanged</code> procedure. Typically <i>createProc</i> will parse <i>objc</i> and <i>objv</i> and create an image master data structure for the new image. <i>createProc</i> may store an arbitrary one-word value at *<i>masterDataPtr</i>, which will be passed back to the image manager when other callbacks are invoked. Typically the value is a pointer to the master data structure for the image. </p>
<p> If <i>createProc</i> encounters an error, it should leave an error message in the interpreter result and return <code>TCL_ERROR</code>; otherwise it should return <code>TCL_OK</code>. </p>
<p> <i>createProc</i> should call <code>Tk_ImageChanged</code> in order to set the size of the image and request an initial redisplay. </p>
<h3>Getproc</h3>
<p><i>typePtr-&gt;getProc</i> is invoked by Tk whenever a widget calls <code>Tk_GetImage</code> to use a particular image. This procedure must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef ClientData Tk_ImageGetProc(
 Tk_Window <i>tkwin</i>,
 ClientData <i>masterData</i>);</pre>
</dl>
<p> The <i>tkwin</i> argument identifies the window in which the image will be used and <i>masterData</i> is the value returned by <i>createProc</i> when the image master was created. <i>getProc</i> will usually create a data structure for the new instance, including such things as the resources needed to display the image in the given window. <i>getProc</i> returns a one-word token for the instance, which is typically the address of the instance data structure. Tk will pass this value back to the image manager when invoking its <i>displayProc</i> and <i>freeProc</i> procedures. </p>
<h3>Displayproc</h3>
<p><i>typePtr-&gt;displayProc</i> is invoked by Tk whenever an image needs to be displayed (i.e., whenever a widget calls <code>Tk_RedrawImage</code>). <i>displayProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_ImageDisplayProc(
 ClientData <i>instanceData</i>,
 Display *<i>display</i>,
 Drawable <i>drawable</i>,
 int <i>imageX</i>,
 int <i>imageY</i>,
 int <i>width</i>,
 int <i>height</i>,
 int <i>drawableX</i>,
 int <i>drawableY</i>);</pre>
</dl>
<p> The <i>instanceData</i> will be the same as the value returned by <i>getProc</i> when the instance was created. <i>display</i> and <i>drawable</i> indicate where to display the image; <i>drawable</i> may be a pixmap rather than the window specified to <i>getProc</i> (this is usually the case, since most widgets double-buffer their redisplay to get smoother visual effects). <i>imageX</i>, <i>imageY</i>, <i>width</i>, and <i>height</i> identify the region of the image that must be redisplayed. This region will always be within the size of the image as specified in the most recent call to <code>Tk_ImageChanged</code>. <i>drawableX</i> and <i>drawableY</i> indicate where in <i>drawable</i> the image should be displayed; <i>displayProc</i> should display the given region of the image so that point (<i>imageX</i>, <i>imageY</i>) in the image appears at (<i>drawableX</i>, <i>drawableY</i>) in <i>drawable</i>. </p>
<h3>Freeproc</h3>
<p><i>typePtr-&gt;freeProc</i> contains the address of a procedure that Tk will invoke when an image instance is released (i.e., when <code>Tk_FreeImage</code> is invoked). This can happen, for example, when a widget is deleted or a image item in a canvas is deleted, or when the image displayed in a widget or canvas item is changed. <i>freeProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_ImageFreeProc(
 ClientData <i>instanceData</i>,
 Display *<i>display</i>);</pre>
</dl>
<p> The <i>instanceData</i> will be the same as the value returned by <i>getProc</i> when the instance was created, and <i>display</i> is the display containing the window for the instance. <i>freeProc</i> should release any resources associated with the image instance, since the instance will never be used again. </p>
<h3>Deleteproc</h3>
<p><i>typePtr-&gt;deleteProc</i> is a procedure that Tk invokes when an image is being deleted (i.e. when the <code>image delete</code> command is invoked). Before invoking <i>deleteProc</i> Tk will invoke <i>freeProc</i> for each of the image&#8217;s instances. <i>deleteProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_ImageDeleteProc(
 ClientData <i>masterData</i>);</pre>
</dl>
<p> The <i>masterData</i> argument will be the same as the value stored in <i>*masterDataPtr</i> by <i>createProc</i> when the image was created. <i>deleteProc</i> should release any resources associated with the image. </p>
<h2>Tk_Getimagemasterdata</h2>
<p>The procedure <code>Tk_GetImageMasterData</code> may be invoked to retrieve information about an image. For example, an image manager can use this procedure to locate its image master data for an image. If there exists an image named <i>name</i> in the interpreter given by <i>interp</i>, then <i>*typePtrPtr</i> is filled in with type information for the image (the <i>typePtr</i> value passed to <code>Tk_CreateImageType</code> when the image type was registered) and the return value is the ClientData value returned by the <i>createProc</i> when the image was created (this is typically a pointer to the image master data structure). If no such image exists then NULL is returned and NULL is stored at <i>*typePtrPtr</i>. </p>
<h2>Legacy Interface Support</h2>
<p>In Tk 8.2 and earlier, the definition of <code>Tk_ImageCreateProc</code> was incompatibly different, with the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageCreateProc(
 Tcl_Interp *<i>interp</i>,
 char *<i>name</i>,
 int <i>argc</i>,
 char **<i>argv</i>,
 Tk_ImageType *<i>typePtr</i>,
 Tk_ImageMaster <i>master</i>,
 ClientData *<i>masterDataPtr</i>);</pre>
</dl>
<p> Legacy programs and libraries dating from those days may still contain code that defines extended Tk image types using the old interface. The Tk header file will still support this legacy interface if the code is compiled with the macro <code>USE_OLD_IMAGE</code> defined. </p>
<p> When the <code>USE_OLD_IMAGE</code> legacy support is enabled, you may see the routine <code>Tk_InitImageArgs</code> in use. This was a migration tool used to create stub-enabled extensions that could be loaded into interps containing all versions of Tk 8.1 and later. Tk 8.5 no longer provides this routine, but uses a macro to convert any attempted calls of this routine into an empty comment. Any stub-enabled extension providing an extended image type via the legacy interface that is compiled against Tk 8.5 headers and linked against the Tk 8.5 stub library will produce a file that can be loaded only into interps with Tk 8.5 or later; that is, the normal stub-compatibility rules. If a developer needs to generate from such code a file that is loadable into interps with Tk 8.4 or earlier, they must use Tk 8.4 headers and stub libraries to do so. </p>
<p> Any new code written today should not make use of the legacy interfaces. Expect their support to go away in Tk 9. </p>
<h2>See Also</h2>
<p>Tk_ImageChanged, Tk_GetImage, Tk_FreeImage, Tk_RedrawImage, Tk_SizeOfImage </p>
<h2>Keywords</h2>
<p>image manager, image type, instance, master</p>
