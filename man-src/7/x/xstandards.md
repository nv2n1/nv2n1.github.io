---
title: "xstandards(7)"
name: "xstandards"
section: "7"
letter: "x"
url: "/docs/linux/man/7-xstandards/"
---

XStandards - X Window System Standards and Specifications

<h2>Description</h2>

The major goal of the X Consortium was to promote cooperation within the computer industry in the creation of standard software interfaces at all layers in the X Window System environment. The X Consortium produced standards - documents which defined network protocols, programming interfaces, and other aspects of the X environment. These standards continue to exist in the X.Org Foundation releases. The X.Org Foundation also produces specifications. Like X Window System Standards, these are documents which define network protocols, programming interfaces, and other aspects of the X environment. Under the aegis of The Open Group, X Window System standards, X.Org Foundation specifications, and other specifications are the basis for portions of The Open Group's various CAE specifications. 

 The status of various standards, specifications, and the software in the X11R7.0 distribution, is explained below.

<h2>Standards</h2>

The following documents are X Window System standards: <pre>X Window System Protocol
X Version 11, Release 7.0
Robert W. Scheifler
Xlib - C Language X Interface
X Version 11, Release 7.0
James Gettys, Robert W. Scheifler, Ron Newman
X Toolkit Intrinsics - C Language Interface
X Version 11, Release 7.0
Joel McCormack, Paul Asente, Ralph R. Swick, Donna Converse
Bitmap Distribution Format
Version 2.1
X Version 11, Release 7.0
Inter-Client Communication Conventions Manual
Version 2.0
X Version 11, Release 7.0
David Rosenthal, Stuart W. Marks
Compound Text Encoding
Version 1.1
X Version 11, Release 7.0
Robert W. Scheifler
X Logical Font Description Conventions
Version 1.5
X Version 11, Release 7.0
Jim Flowers, Stephen Gildea
X Display Manager Control Protocol
Version 1.1
X Version 11, Release 7.0
Keith Packard
X11 Nonrectangular Window Shape Extension
Version 1.0.1
X Version 11, Release 7.0
Keith Packard
X11 Input Extension Protocol Specification
Version 1.0
X Version 11, Release 7.0
George Sachs, Mark Patrick
X11 Input Extension Library Specification
X Version 11, Release 7.0
Mark Patrick, George Sachs
The X Font Service Protocol
Version 2.0
X Version 11, Release 7.0
Jim Fulton
Inter-Client Exchange (ICE) Protocol
Version 1.0
X Version 11, Release 7.0
Robert Scheifler, Jordan Brown
Inter-Client Exchange (ICE) Library
Version 1.0
X Version 11, Release 7.0
Ralph Mor
X Session Management Protocol
Version 1.0
X Version 11, Release 7.0
Mike Wexler
X Session Management Library
Version 1.0
X Version 11, Release 7.0
Ralph Mor
The Input Method Protocol
Version 1.0
X Version 11, Release 7.0
Masahiko Narita, Hideki Hiura
X Synchronization Extension
Version 3.0
X Version 11, Release 7.0
Tim Glauert, Dave Carver, Jim Gettys, David P. Wiggins
XTEST Extension
Version 2.2
Kieron Drake
Big Requests Extension
Version 2.0
X Version 11, Release 7.0
Bob Scheifler
XC-MISC Extension
Version 1.1
X Version 11, Release 7.0
Bob Scheifler, Dave Wiggins
Double Buffer Extension
Version 1.0
Ian Elliott, David P. Wiggins
Record Extension Protocol
Version 1.13
Martha Zimet, Stephen Gildea
Record Extension Library
Version 1.13
Martha Zimet, Stephen Gildea
X Keyboard Extension Protocol
X Version 11, Release 7.0
Erik Fortune
X Keyboard Extension Library
X Version 11, Release 7.0
Amber J. Benson, Gary Aitken, Erik Fortune, Donna Converse,
George Sachs, and Will Walker
X Print Extension Protocol
X Version 11, Release 7.0
X Print Extension Library
X Version 11, Release 7.0
X Application Group Extension Protocol and Library
Version 1.0
X Version 11, Release 7.0
Kaleb Keithley
X Security Extension Protocol and Library
Version 4.0
X Version 11, Release 7.0
Dave Wiggins
X Proxy Manager Protocol
X Version 11, Release 7.0
Ralph Swick
LBX Extension Protocol and Library
X Version 11, Release 7.0
Keith Packard, Dave Lemke, Donna Converse, Ralph Mor, Ray Tice
Remote Execution MIME Type
Version 1.0
X Version 11, Release 7.0
Arnaud Le Hors</pre>

<h2>Specifications</h2>

The following documents are X Project Team specifications: <pre>Colormap Utilization Policy and Extension
Version 1.0
Kaleb Keithley
Extended Visual Information Extension
Version 1.0
Peter Daifuku
X Display Power Management (DPMS) Extension Protocol and Library
Version 1.0
Rob Lembree</pre>

<h2>Include Files</h2>

The following include files are part of the Xlib standard. 

 <pre>&lt;X11/cursorfont.h&gt;
&lt;X11/keysym.h&gt;
&lt;X11/keysymdef.h&gt;
&lt;X11/X.h&gt;
&lt;X11/Xatom.h&gt;
&lt;X11/Xcms.h&gt;
&lt;X11/Xlib.h&gt;
&lt;X11/Xlibint.h&gt;
&lt;X11/Xproto.h&gt;
&lt;X11/Xprotostr.h&gt;
&lt;X11/Xresource.h&gt;
&lt;X11/Xutil.h&gt;
&lt;X11/X10.h&gt;</pre>The following include files are part of the X Toolkit Intrinsics standard. 

 <pre>&lt;X11/Composite.h&gt;
&lt;X11/CompositeP.h&gt;
&lt;X11/Constraint.h&gt;
&lt;X11/ConstrainP.h&gt;
&lt;X11/Core.h&gt;
&lt;X11/CoreP.h&gt;
&lt;X11/Intrinsic.h&gt;
&lt;X11/IntrinsicP.h&gt;
&lt;X11/Object.h&gt;
&lt;X11/ObjectP.h&gt;
&lt;X11/RectObj.h&gt;
&lt;X11/RectObjP.h&gt;
&lt;X11/Shell.h&gt;
&lt;X11/ShellP.h&gt;
&lt;X11/StringDefs.h&gt;
&lt;X11/Vendor.h&gt;
&lt;X11/VendorP.h&gt;</pre>The following include file is part of the Nonrectangular Window Shape Extension standard. 

 <pre>&lt;X11/extensions/shape.h&gt;</pre>The following include files are part of the X Input Extension standard. 

 <pre>&lt;X11/extensions/XI.h&gt;
&lt;X11/extensions/XInput.h&gt;
&lt;X11/extensions/XIproto.h&gt;</pre>The following include files are part of the ICElib standard. 

 <pre>&lt;X11/ICE/ICE.h&gt;
&lt;X11/ICE/ICEconn.h&gt;
&lt;X11/ICE/ICElib.h&gt;
&lt;X11/ICE/ICEmsg.h&gt;
&lt;X11/ICE/ICEproto.h&gt;
&lt;X11/ICE/ICEutil.h&gt;</pre>The following include files are part of the SMlib standard. 

 <pre>&lt;X11/SM/SM.h&gt;
&lt;X11/SM/SMlib.h&gt;
&lt;X11/SM/SMproto.h&gt;</pre>The following include file is part of the Synchronization standard. 

 <pre>&lt;X11/extensions/sync.h&gt;</pre>The following include file is part of the XTEST standard. 

 <pre>&lt;X11/extensions/XTest.h&gt;</pre>The following include file is part of the Double Buffer Extension standard. 

 <pre>&lt;X11/extensions/Xdbe.h&gt;</pre>The following include file is part of the Record Library standard. 

 <pre>&lt;X11/extensions/record.h&gt;</pre>The following include files are part of the X Keyboard Extension Library standard. 

 <pre>&lt;X11/XKBlib.h&gt;
&lt;X11/extensions/XKB.h&gt;
&lt;X11/extensions/XKBproto.h&gt;
&lt;X11/extensions/XKBstr.h&gt;
&lt;X11/extensions/XKBgeom.h&gt;</pre>The following include files are part of the X Print Extension Library standard. 

 <pre>&lt;X11/extensions/Print.h&gt;
&lt;X11/extensions/Printstr.h&gt;</pre>The following include files are part of the X Application Group Extension Library standard. 

 <pre>&lt;X11/extensions/Xag.h&gt;
&lt;X11/extensions/Xagstr.h&gt;</pre>The following include files are part of the X Security Extension Library standard. 

 <pre>&lt;X11/extensions/security.h&gt;
&lt;X11/extensions/securstr.h&gt;</pre>The following include files are part of the LBX Extension library standard. 

 <pre>&lt;X11/extensions/XLbx.h&gt;
&lt;X11/extensions/lbxbuf.h&gt;
&lt;X11/extensions/lbxbufstr.h&gt;
&lt;X11/extensions/lbxdeltastr.h&gt;
&lt;X11/extensions/lbximage.h&gt;
&lt;X11/extensions/lbxopts.h&gt;
&lt;X11/extensions/lbxstr.h&gt;
&lt;X11/extensions/lbxzlib.h&gt;</pre>The following include files are part of the Colormap Utilization Policy and Extension specification. 

 <pre>&lt;X11/extensions/Xcup.h&gt;
&lt;X11/extensions/Xcupstr.h&gt;</pre>The following include files are part of the Extended Visual Information specification. 

 <pre>&lt;X11/extensions/XEVI.h&gt;
&lt;X11/extensions/XEVIstr.h&gt;</pre>The following include files are part of the X Display Management Signaling Extension specification. 

 <pre>&lt;X11/extensions/dpms.h&gt;
&lt;X11/extensions/dpmsstr.h&gt;</pre>

<h2>Non Standards</h2>

The X11R7.0 distribution contains <i>sample</i> implementations, not <i>reference</i> implementations. Although much of the code is believed to be correct, the code should be assumed to be in error wherever it conflicts with the specification. 

 The only X Window System standards are the ones listed above. No other documents, include files, or software in X11R7.0 carry special status within the X Window System. For example, none of the following are standards: internal interfaces of the sample server; the MIT-SHM extension; the Athena Widget Set; the Xmu library; the Xau library; the RGB database; the X Locale database; the fonts distributed with X11R7.0; the applications distributed with X11R7.0; the include files &lt;X11/XWDFile.h&gt;, &lt;X11/Xfuncproto.h&gt;, &lt;X11/Xfuncs.h&gt;, &lt;X11/Xosdefs.h&gt;, &lt;X11/Xos.h&gt;, &lt;X11/Xos_r.h&gt;, &lt;X11/Xwinsock.h&gt;, and &lt;X11/Xthreads.h&gt;; the bitmap files in &lt;X11/bitmaps&gt;. 

 The Multi-Buffering extension was a draft standard of the X Consortium but has been superseded by DBE as a standard.

<h2>X Registry</h2>

The X.Org Foundation maintains a registry of certain X-related items, to aid in avoiding conflicts and to aid in sharing of such items. 

 The registry is published as part of the X Window System software release. The latest version may also be found at <pre> <a HREF="ftp://ftp.x.org/pub/DOCS/registry">ftp://ftp.x.org/pub/DOCS/registry</a></pre>The X Registry and the names in it are not X Window System standards.
