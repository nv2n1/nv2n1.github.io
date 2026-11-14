---
title: "xcursorxcfilesave(3)"
name: "xcursorxcfilesave"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcursorxcfilesave/"
description: "XCURSOR – Cursor management library"
---

<p>XCURSOR &#8211; Cursor management library</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;X11/Xcursor/Xcursor.h&gt;</code></pre>
<h2>Description</h2>
<p><code>Xcursor</code> is a simple library designed to help locate and load cursors. Cursors can be loaded from files or memory. A library of common cursors exists which map to the standard X cursor names. Cursors can exist in several sizes and the library automatically picks the best size. </p>
<h2>Functional Overview</h2>
<p>Xcursor is built in a couple of layers; at the bottom layer is code which can load cursor images from files. Above that is a layer which locates cursor files based on the library path and theme. At the top is a layer which builds cursors either out of an image loaded from a file or one of the standard X cursors. When using images loaded from files, Xcursor prefers to use the Render extension CreateCursor request if supported by the X server. Where not supported, Xcursor maps the cursor image to a standard X cursor and uses the core CreateCursor request. </p>
<h3>Cursor Files</h3>
<p>Xcursor defines a new format for cursors on disk. Each file holds one or more cursor images. Each cursor image is tagged with a nominal size so that the best size can be selected automatically. Multiple cursors of the same nominal size can be loaded together; applications are expected to use them as an animated sequence. </p>
<p> Cursor files are stored as a header containing a table of contents followed by a sequence of chunks. The table of contents indicates the type, subtype and position in the file of each chunk. The file header looks like: </p>
<p> <i>magic</i>: CARD32 &#8216;Xcur&#8217; (0x58, 0x63, 0x75, 0x72)<br />
 <i>header</i>: CARD32 bytes in this header<br />
 <i>version</i>: CARD32 file version number<br />
 <i>ntoc</i>: CARD32 number of toc entries<br />
 <i>toc</i>: LISTofTOC table of contents </p>
<p> Each table of contents entry looks like: </p>
<p> <i>type</i>: CARD32 entry type<br />
 <i>subtype</i>: CARD32 type-specific label &#8211; size for images<br />
 <i>position</i>: CARD32 absolute byte position of table in file </p>
<p> Each chunk in the file has set of common header fields followed by additional type-specific fields: </p>
<p> <i>header</i>: CARD32 bytes in chunk header (including type-specific fields)<br />
 <i>type</i>: CARD32 must match type in TOC for this chunk<br />
 <i>subtype</i>: CARD32 must match subtype in TOC for this chunk<br />
 <i>version</i>: CARD32 version number for this chunk type </p>
<p> There are currently two chunk types defined for cursor files; comments and images. Comments look like: </p>
<p> <i>header</i>: 20 Comment headers are 20 bytes<br />
 <i>type</i>: 0xfffe0001 Comment type is 0xfffe0001<br />
 <i>subtype</i>: { 1 (COPYRIGHT), 2 (LICENSE), 3 (OTHER) }<br />
 <i>version</i>: 1<br />
 <i>length</i>: CARD32 byte length of UTF-8 string<br />
 <i>string</i>: LISTofCARD8 UTF-8 string </p>
<p> Images look like: </p>
<p> <i>header</i>: 36 Image headers are 36 bytes<br />
 <i>type</i>: 0xfffd0002 Image type is 0xfffd0002<br />
 <i>subtype</i>: CARD32 Image subtype is the nominal size<br />
 <i>version</i>: 1<br />
 <i>width</i>: CARD32 Must be less than or equal to 0x7fff<br />
 <i>height</i>: CARD32 Must be less than or equal to 0x7fff<br />
 <i>xhot</i>: CARD32 Must be less than or equal to width<br />
 <i>yhot</i>: CARD32 Must be less than or equal to height<br />
 <i>delay</i>: CARD32 Delay between animation frames in milliseconds<br />
 <i>pixels</i>: LISTofCARD32 Packed ARGB format pixels </p>
<h3>Themes</h3>
<p>Xcursor (mostly) follows the freedesktop.org spec for theming icons. The default search path it uses is ~/.icons, /usr/share/icons, /usr/share/pixmaps. Within each of these directories, it searches for a directory using the theme name. Within the theme directory, it looks for cursor files in the &#8216;cursors&#8217; subdirectory. It uses the first cursor file found along the path. </p>
<p> If necessary, Xcursor also looks for a &quot;index.theme&quot; file in each theme directory to find inherited themes and searches along the path for those themes as well. </p>
<p> If no theme is set, or if no cursor is found for the specified theme, Xcursor checks the &quot;default&quot; theme. </p>
<h2>Datatypes</h2>
<dl COMPACT>
<dt><code>XcursorImage</code></p>
<dd>holds a single cursor image in memory. Each pixel in the cursor is a 32-bit value containing ARGB with A in the high byte. </p>
<pre> typedef struct _XcursorImage {
 XcursorDim size; /* nominal size for matching */
 XcursorDim width; /* actual width */
 XcursorDim height; /* actual height */
 XcursorDim xhot; /* hot spot x (must be inside image) */
 XcursorDim yhot; /* hot spot y (must be inside image) */
 XcursorPixel *pixels; /* pointer to pixels */
 } XcursorImage;</pre>
<dt><code>XcursorImages</code></p>
<dd>holds multiple XcursorImage structures. They&#8217;re all freed when the XcursorImages is freed. </p>
<pre> typedef struct _XcursorImages {
 int nimage; /* number of images */
 XcursorImage **images; /* array of XcursorImage pointers */
 } XcursorImages;</pre>
<dt><code>XcursorCursors</code></p>
<dd>Holds multiple Cursor objects. They&#8217;re all freed when the XcursorCursors is freed. These are reference counted so that multiple XcursorAnimate structures can use the same XcursorCursors. </p>
<pre> typedef struct _XcursorCursors {
 Display *dpy; /* Display holding cursors */
 int ref; /* reference count */
 int ncursor; /* number of cursors */
 Cursor *cursors; /* array of cursors */
 } XcursorCursors;</pre>
<dt><code>XcursorAnimate</code></p>
<dd>References a set of cursors and a sequence within that set. Multiple XcursorAnimate structures may reference the same XcursorCursors; each holds a reference which is removed when the XcursorAnimate is freed. </p>
<pre> typedef struct _XcursorAnimate {
 XcursorCursors *cursors; /* list of cursors to use */
 int sequence; /* which cursor is next */
 } XcursorAnimate;</pre>
<dt><code>XcursorFile</code></p>
<dd>Xcursor provides an abstract API for accessing the file data. Xcursor provides a stdio implementation of this abstract API; applications are free to create additional implementations. These functions parallel the stdio functions in return value and expected argument values; the read and write functions flip the arguments around to match the POSIX versions. </p>
<pre> typedef struct _XcursorFile {
 void *closure;
 int (*read) (XcursorFile *file, unsigned char *buf, int len);
 int (*write) (XcursorFile *file, unsigned char *buf, int len);
 int (*seek) (XcursorFile *file, long offset, int whence);
 };</pre>
</dl>
<h2>Functions</h2>
<h3>Object Management</h3>
<dl COMPACT>
<dt>XcursorImage *XcursorImageCreate (int width, int height)</p>
<dd>
<dd>void XcursorImageDestroy (XcursorImage *image) Allocate and free images. On allocation, the hotspot and the pixels are left uninitialized. The size is set to the maximum of width and height. </p>
<dt>XcursorImages *XcursorImagesCreate (int size)</p>
<dd>
<dd>void XcursorImagesDestroy (XcursorImages *images) Allocate and free arrays to hold multiple cursor images. On allocation, nimage is set to zero. </p>
<dt>XcursorCursors *XcursorCursorsCreate (Display *dpy, int size)</p>
<dd>
<dd>void XcursorCursorsDestroy (XcursorCursors *cursors) Allocate and free arrays to hold multiple cursors. On allocation, ncursor is set to zero, ref is set to one. </p>
</dl>
<h3>Reading and writing images.</h3>
<dl COMPACT>
<dt>XcursorImage *XcursorXcFileLoadImage (XcursorFile *file, int size)</p>
<dd>
<dd>XcursorImages *XcursorXcFileLoadImages (XcursorFile *file, int size) </p>
<dd>XcursorImages *XcursorXcFileLoadAllImages (XcursorFile *file) </p>
<dd>XcursorBool XcursorXcFileLoad (XcursorFile *file, XcursorComments **commentsp, XcursorImages **imagesp) </p>
<dd>XcursorBool XcursorXcFileSave (XcursorFile *file, const XcursorComments *comments, const XcursorImages *images) These read and write cursors from an XcursorFile handle. After reading, the file pointer will be left at some random place in the file. </p>
<dt>XcursorImage *XcursorFileLoadImage (FILE *file, int size)</p>
<dd>
<dd>XcursorImages *XcursorFileLoadImages (FILE *file, int size) </p>
<dd>XcursorImages *XcursorFileLoadAllImages (FILE *file) </p>
<dd>XcursorBool XcursorFileLoad (FILE *file, XcursorComments **commentsp, XcursorImages **imagesp) </p>
<dd>XcursorBool XcursorFileSaveImages (FILE *file, const XcursorImages *images) </p>
<dd>XcursorBool XcursorFileSave (FILE * file, const XcursorComments *comments, const XcursorImages *images) These read and write cursors from a stdio FILE handle. Writing flushes before returning so that any errors should be detected. </p>
<dt>XcursorImage *XcursorFilenameLoadImage (const char *filename, int size)</p>
<dd>
<dd>XcursorImages *XcursorFilenameLoadImages (const char *filename, int size) </p>
<dd>XcursorImages *XcursorFilenameLoadAllImages (FILE *file) </p>
<dd>XcursorBool XcursorFilenameLoad (const char *file, XcursorComments **commentsp, XcursorImages **imagesp) </p>
<dd>XcursorBool XcursorFilenameSaveImages (const char *filename, const XcursorImages *images) </p>
<dd>XcursorBool XcursorFilenameSave (const char *file, const XcursorComments *comments, const XcursorImages *images) These parallel the stdio FILE interfaces above, but take filenames. </p>
</dl>
<h3>Reading library images</h3>
<dl COMPACT>
<dt>XcursorImage *XcursorLibraryLoadImage (const char *name, const char *theme, int size)</p>
<dd>
<dd>XcursorImages *XcursorLibraryLoadImages (const char *name, const char *theme, int size) These search the library path, loading the first file found. If &#8216;theme&#8217; is not NULL, these functions first try appending -theme to name and then name alone. </p>
</dl>
<h3>Cursor APIs</h3>
<dl COMPACT>
<dt>Cursor XcursorFilenameLoadCursor (Display *dpy, const char *file)</p>
<dd>
<dd>XcursorCursors *XcursorFilenameLoadCursors (Display *dpy, const char *file) These load cursors from the specified file. </p>
<dt>Cursor XcursorLibraryLoadCursor (Display *dpy, const char *name)</p>
<dd>
<dd>XcursorCursors *XcursorLibraryLoadCursors (Display *dpy, const char *name) These load cursors using the specified library name. The theme comes from the display. </p>
</dl>
<h3>X Cursor Name APIs</h3>
<dl COMPACT>
<dt>XcursorImage *XcursorShapeLoadImage (unsigned int shape, const char *theme, int size)</p>
<dd>
<dd>XcursorImages *XcursorShapeLoadImages (unsigned int shape, const char *theme, int size) These map &#8216;shape&#8217; to a library name using the standard X cursor names and then load the images. </p>
<dt>Cursor XcursorShapeLoadCursor (Display *dpy, unsigned int shape)</p>
<dd>
<dd>XcursorCursors *XcursorShapeLoadCursors (Display *dpy, unsigned int shape) These map &#8216;shape&#8217; to a library name and then load the cursors. </p>
</dl>
<h3>Display Information APIs</h3>
<dl COMPACT>
<dt>XcursorBool XcursorSupportsARGB (Display *dpy)</p>
<dd>Returns whether the display supports ARGB cursors or whether cursors will be mapped to a core X cursor. </p>
<dt>XcursorBool XcursorSetDefaultSize (Display *dpy, int size)</p>
<dd>Sets the default size for cursors on the specified display. When loading cursors, those whose nominal size is closest to this size will be preferred. </p>
<dt>int XcursorGetDefaultSize (Display *dpy)</p>
<dd>Gets the default cursor size. </p>
<dt>XcursorBool XcursorSetTheme (Display *dpy, const char *theme)</p>
<dd>Sets the current theme name. </p>
<dt>char *XcursorGetTheme (Display *dpy)</p>
<dd>Gets the current theme name. </p>
</dl>
<h2>Environment Variables</h2>
<dl COMPACT>
<dt><code>XCURSOR_PATH</code></p>
<dd>This variable sets the list of paths to look for cursors in. Directories in this path are separated by colons (:). </p>
</dl>
<h2>Restrictions</h2>
<p><code>Xcursor</code> will probably change radically in the future; weak attempts will be made to retain some level of source-file compatibility. </p>
<h2>Author</h2>
<p>Keith Packard</p>
