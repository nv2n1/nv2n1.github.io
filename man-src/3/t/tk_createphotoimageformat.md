---
title: "tk_createphotoimageformat(3)"
name: "tk_createphotoimageformat"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_createphotoimageformat/"
description: "formatPtr->name provides a name for the image type. Once Tk_CreatePhotoImageFormat returns, this name may be used in the -format photo image configuration and subcommand option. The manual page for..."
---

<p>Tk_CreatePhotoImageFormat &#8211; define new file format for photo images </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_CreatePhotoImageFormat</code>(<i>formatPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_PhotoImageFormat <i>*formatPtr</i> (in) Structure that defines the new file format. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_CreatePhotoImageFormat</code> is invoked to define a new file format for image data for use with photo images. The code that implements an image file format is called an image file format handler, or handler for short. The photo image code maintains a list of handlers that can be used to read and write data to or from a file. Some handlers may also support reading image data from a string or converting image data to a string format. The user can specify which handler to use with the <code>-format</code> image configuration option or the <code>-format</code> option to the <code>read</code> and <code>write</code> photo image subcommands. </p>
<p> An image file format handler consists of a collection of procedures plus a Tk_PhotoImageFormat structure, which contains the name of the image file format and pointers to six procedures provided by the handler to deal with files and strings in this format. The Tk_PhotoImageFormat structure contains the following fields:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tk_PhotoImageFormat {
 char *<i>name</i>;
 Tk_ImageFileMatchProc *<i>fileMatchProc</i>;
 Tk_ImageStringMatchProc *<i>stringMatchProc</i>;
 Tk_ImageFileReadProc *<i>fileReadProc</i>;
 Tk_ImageStringReadProc *<i>stringReadProc</i>;
 Tk_ImageFileWriteProc *<i>fileWriteProc</i>;
 Tk_ImageStringWriteProc *<i>stringWriteProc</i>;
} Tk_PhotoImageFormat;</pre>
</dl>
<p> The handler need not provide implementations of all six procedures. For example, the procedures that handle string data would not be provided for a format in which the image data are stored in binary, and could therefore contain null characters. If any procedure is not implemented, the corresponding pointer in the Tk_PhotoImageFormat structure should be set to NULL. The handler must provide the <i>fileMatchProc</i> procedure if it provides the <i>fileReadProc</i> procedure, and the <i>stringMatchProc</i> procedure if it provides the <i>stringReadProc</i> procedure. </p>
<h2>Name</h2>
<p><i>formatPtr-&gt;name</i> provides a name for the image type. Once <code>Tk_CreatePhotoImageFormat</code> returns, this name may be used in the <code>-format</code> photo image configuration and subcommand option. The manual page for the photo image (</p>
<p> <a href="/docs/linux/man/n-photo/">photo</a>(n)) describes how image file formats are chosen based on their names and the value given to the <code>-format</code> option. The first character of <i>formatPtr-&gt;name</i> must not be an uppercase character from the ASCII character set (that is, one of the characters <code>A</code>&#8211;<code>Z</code>). Such names are used only for legacy interface support (see below). </p>
<h2>Filematchproc</h2>
<p><i>formatPtr-&gt;fileMatchProc</i> provides the address of a procedure for Tk to call when it is searching for an image file format handler suitable for reading data in a given file. <i>formatPtr-&gt;fileMatchProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageFileMatchProc(
 Tcl_Channel <i>chan</i>,
 const char *<i>fileName</i>,
 Tcl_Obj *<i>format</i>,
 int *<i>widthPtr</i>,
 int *<i>heightPtr</i>,
 Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> The <i>fileName</i> argument is the name of the file containing the image data, which is open for reading as <i>chan</i>. The <i>format</i> argument contains the value given for the <code>-format</code> option, or NULL if the option was not specified. If the data in the file appears to be in the format supported by this handler, the <i>formatPtr-&gt;fileMatchProc</i> procedure should store the width and height of the image in *<i>widthPtr</i> and *<i>heightPtr</i> respectively, and return 1. Otherwise it should return 0. </p>
<h2>Stringmatchproc</h2>
<p><i>formatPtr-&gt;stringMatchProc</i> provides the address of a procedure for Tk to call when it is searching for an image file format handler for suitable for reading data from a given string. <i>formatPtr-&gt;stringMatchProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageStringMatchProc(
 Tcl_Obj *<i>data</i>,
 Tcl_Obj *<i>format</i>,
 int *<i>widthPtr</i>,
 int *<i>heightPtr</i>,
 Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> The <i>data</i> argument points to the object containing the image data. The <i>format</i> argument contains the value given for the <code>-format</code> option, or NULL if the option was not specified. If the data in the string appears to be in the format supported by this handler, the <i>formatPtr-&gt;stringMatchProc</i> procedure should store the width and height of the image in *<i>widthPtr</i> and *<i>heightPtr</i> respectively, and return 1. Otherwise it should return 0. </p>
<h2>Filereadproc</h2>
<p><i>formatPtr-&gt;fileReadProc</i> provides the address of a procedure for Tk to call to read data from an image file into a photo image. <i>formatPtr-&gt;fileReadProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageFileReadProc(
 Tcl_Interp *<i>interp</i>,
 Tcl_Channel <i>chan</i>,
 const char *<i>fileName</i>,
 Tcl_Obj *<i>format</i>,
 PhotoHandle <i>imageHandle</i>,
 int <i>destX</i>, int <i>destY</i>,
 int <i>width</i>, int <i>height</i>,
 int <i>srcX</i>, int <i>srcY</i>);</pre>
</dl>
<p> The <i>interp</i> argument is the interpreter in which the command was invoked to read the image; it should be used for reporting errors. The image data is in the file named <i>fileName</i>, which is open for reading as <i>chan</i>. The <i>format</i> argument contains the value given for the <code>-format</code> option, or NULL if the option was not specified. The image data in the file, or a subimage of it, is to be read into the photo image identified by the handle <i>imageHandle</i>. The subimage of the data in the file is of dimensions <i>width</i> x <i>height</i> and has its top-left corner at coordinates (<i>srcX</i>,<i>srcY</i>). It is to be stored in the photo image with its top-left corner at coordinates (<i>destX</i>,<i>destY</i>) using the <code>Tk_PhotoPutBlock</code> procedure. The return value is a standard Tcl return value. </p>
<h2>Stringreadproc</h2>
<p><i>formatPtr-&gt;stringReadProc</i> provides the address of a procedure for Tk to call to read data from a string into a photo image. <i>formatPtr-&gt;stringReadProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageStringReadProc(
 Tcl_Interp *<i>interp</i>,
 Tcl_Obj *<i>data</i>,
 Tcl_Obj *<i>format</i>,
 PhotoHandle <i>imageHandle</i>,
 int <i>destX</i>, int <i>destY</i>,
 int <i>width</i>, int <i>height</i>,
 int <i>srcX</i>, int <i>srcY</i>);</pre>
</dl>
<p> The <i>interp</i> argument is the interpreter in which the command was invoked to read the image; it should be used for reporting errors. The <i>data</i> argument points to the image data in object form. The <i>format</i> argument contains the value given for the <code>-format</code> option, or NULL if the option was not specified. The image data in the string, or a subimage of it, is to be read into the photo image identified by the handle <i>imageHandle</i>. The subimage of the data in the string is of dimensions <i>width</i> x <i>height</i> and has its top-left corner at coordinates (<i>srcX</i>,<i>srcY</i>). It is to be stored in the photo image with its top-left corner at coordinates (<i>destX</i>,<i>destY</i>) using the <code>Tk_PhotoPutBlock</code> procedure. The return value is a standard Tcl return value. </p>
<h2>Filewriteproc</h2>
<p><i>formatPtr-&gt;fileWriteProc</i> provides the address of a procedure for Tk to call to write data from a photo image to a file. <i>formatPtr-&gt;fileWriteProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageFileWriteProc(
 Tcl_Interp *<i>interp</i>,
 const char *<i>fileName</i>,
 Tcl_Obj *<i>format</i>,
 Tk_PhotoImageBlock *<i>blockPtr</i>);</pre>
</dl>
<p> The <i>interp</i> argument is the interpreter in which the command was invoked to write the image; it should be used for reporting errors. The image data to be written are in memory and are described by the Tk_PhotoImageBlock structure pointed to by <i>blockPtr</i>; see the manual page <a href="/docs/linux/man/3-findphoto/">FindPhoto</a>(3) for details. The <i>fileName</i> argument points to the string giving the name of the file in which to write the image data. The <i>format</i> argument contains the value given for the <code>-format</code> option, or NULL if the option was not specified. The format string can contain extra characters after the name of the format. If appropriate, the <i>formatPtr-&gt;fileWriteProc</i> procedure may interpret these characters to specify further details about the image file. The return value is a standard Tcl return value. </p>
<h2>Stringwriteproc</h2>
<p><i>formatPtr-&gt;stringWriteProc</i> provides the address of a procedure for Tk to call to translate image data from a photo image into a string. <i>formatPtr-&gt;stringWriteProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_ImageStringWriteProc(
 Tcl_Interp *<i>interp</i>,
 Tcl_Obj *<i>format</i>,
 Tk_PhotoImageBlock *<i>blockPtr</i>);</pre>
</dl>
<p> The <i>interp</i> argument is the interpreter in which the command was invoked to convert the image; it should be used for reporting errors. The image data to be converted are in memory and are described by the Tk_PhotoImageBlock structure pointed to by <i>blockPtr</i>; see the manual page <a href="/docs/linux/man/3-findphoto/">FindPhoto</a>(3) for details. The data for the string should be put in the interpreter <i>interp</i> result. The <i>format</i> argument contains the value given for the <code>-format</code> option, or NULL if the option was not specified. The format string can contain extra characters after the name of the format. If appropriate, the <i>formatPtr-&gt;stringWriteProc</i> procedure may interpret these characters to specify further details about the image file. The return value is a standard Tcl return value. </p>
<h2>Legacy Interface Support</h2>
<p>In Tk 8.2 and earlier, the definition of all the function pointer types stored in fields of a <code>Tk_PhotoImageFormat</code> struct were incompatibly different. Legacy programs and libraries dating from those days may still contain code that defines extended Tk photo image formats using the old interface. The Tk header file will still support this legacy interface if the code is compiled with the macro <code>USE_OLD_IMAGE</code> defined. Alternatively, the legacy interfaces are used if the first character of <i>formatPtr-&gt;name</i> is an uppercase ASCII character (<code>A</code>&#8211;<code>Z</code>), and explicit casts are used to forgive the type mismatch. For example,</p>
<dl COMPACT>
<dd>
<pre>static Tk_PhotoImageFormat myFormat = {
 &quot;MyFormat&quot;,
 (Tk_ImageFileMatchProc *) FileMatch,
 NULL,
 (Tk_ImageFileReadProc *) FileRead,
 NULL,
 NULL,
 NULL
};</pre>
</dl>
<p> would define a minimal <code>Tk_PhotoImageFormat</code> that operates provide only file reading capability, where <code>FileMatch</code> and <code>FileRead</code> are written according to the legacy interfaces of Tk 8.2 or earlier. </p>
<p> Any stub-enabled extension providing an extended photo image format via the legacy interface enabled by the <code>USE_OLD_IMAGE</code> macro that is compiled against Tk 8.5 headers and linked against the Tk 8.5 stub library will produce a file that can be loaded only into interps with Tk 8.5 or later; that is, the normal stub-compatibility rules. If a developer needs to generate from such code a file that is loadable into interps with Tk 8.4 or earlier, they must use Tk 8.4 headers and stub libraries to do so. </p>
<p> Any new code written today should not make use of the legacy interfaces. Expect their support to go away in Tk 9. </p>
<h2>See Also</h2>
<p>Tk_FindPhoto, Tk_PhotoPutBlock </p>
<h2>Keywords</h2>
<p>photo image, image file</p>
