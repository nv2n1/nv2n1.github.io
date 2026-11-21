---

title: "ico(1)"
name: "ico"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ico/"
description: "ico – animate an icosahedron or other polyhedron"
---

<p> <code>ico</code> [-display display] [-geometry geometry] [-r] [-d pattern] [-i] [-dbl] [-faces] [-noedges] [-sleep n] [-obj object] [-colors color-list] </p>
<p> <code>ico</code> -objhelp </p>
<p> <code>ico</code> -version</p>
<p> <i>Ico</i> displays a wire-frame rotating polyhedron, with hidden lines removed, or a solid-fill polyhedron with hidden faces removed. There are a number of different polyhedra available; adding a new polyhedron to the program is quite simple.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></dt>
<dd> Display on the root window instead of creating a new window.</dd>
<dt><code>-d pattern</code></dt>
<dd> Specify a bit pattern for drawing dashed lines for wire frames.</dd>
<dt><code>-i</code></dt>
<dd> Use inverted colors for wire frames.</dd>
<dt><code>-dbl</code></dt>
<dd> Use double buffering on the display. This works for either wire frame or solid fill drawings. For solid fill drawings, using this switch results in substantially smoother movement. Note that this requires twice as many bit planes as without double buffering. Since some colors are typically allocated by other programs, most eight-bit-plane displays will probably be limited to eight colors when using double buffering.</dd>
<dt><code>-faces</code></dt>
<dd> Draw filled faces instead of wire frames.</dd>
<dt><code>-noedges</code></dt>
<dd> Don&#8217;t draw the wire frames. Typically used only when -faces is used.</dd>
<dt><code>-sleep </code><i>n</i></dt>
<dd> Sleep n seconds between each move of the object.</dd>
<dt><code>-obj </code><i>object</i></dt>
<dd> Specify what object to draw. If no object is specified, an icosahedron is drawn.</dd>
<dt><code>-objhelp</code></dt>
<dd> Print out a list of the available objects, along with information about each object.</dd>
<dt><code>-colors </code><i>color color &#8230;</i></dt>
<dd> Specify what colors should be used to draw the filled faces of the object. If less colors than faces are given, the colors are reused.</dd>
<dt><code>-version</code></dt>
<dd> Print program version information and exit.</dd></dl>
<h2>PROGRAM TERMINATION</h2>
<p> Pressing &quot;q&quot; will close a window. If compiled with threads support, the program will stop only when all threads terminate. You can also close an animation window using the ICCCM <i>delete</i> message (depending on your window manager, you will have a decoration button or menu to send such message).</p>
<h2>ADDING POLYHEDRA</h2>
<p> If you have the source to ico, it is very easy to add more polyhedra. Each polyhedron is defined in an include file by the name of objXXX.h, where XXX is something related to the name of the polyhedron. The format of the include file is defined in the file polyinfo.h. Look at the file objcube.h to see what the exact format of an objXXX.h file should be, then create your objXXX.h file in that format. </p>
<p> After making the new objXXX.h file (or copying in a new one from elsewhere), simply do a &#8216;make depend&#8217;. This will recreate the file allobjs.h, which lists all of the objXXX.h files. Doing a &#8216;make&#8217; after this will rebuild ico with the new object information.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>BUGS</h2>
<p> Pyramids and tetrahedrons with filled faces do not display correctly. </p>
<p> A separate color cell is allocated for each name in the -colors list, even when the same name may be specified twice. Color allocation fails in TrueColor displays and option <i>-faces</i> does not work well.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1994 X Consortium<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions. </p>
