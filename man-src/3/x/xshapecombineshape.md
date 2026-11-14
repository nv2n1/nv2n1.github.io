---
title: "xshapecombineshape(3)"
name: "xshapecombineshape"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xshapecombineshape/"
---

XShapeQueryExtension, XShapeQueryVersion, XShapeCombineRegion, XShapeCombineRectangles, XShapeCombineMask, XShapeCombineShape, XShapeOffsetShape, XShapeQueryExtents, XShapeSelectInput, XShapeInputSelected, XShapeGetRectangles - X nonrectangular shape functions 

<h2>Syntax</h2><pre>#include &lt;X11/extensions/shape.h&gt;
Bool XShapeQueryExtension (
 Display *dpy,
 int *event_basep,
 int *error_basep);
Status XShapeQueryVersion (
 Display *dpy,
 int *major_versionp,
 int *minor_versionp);
void XShapeCombineRegion (
 Display *dpy,
 Window dest,
 int destKind,
 int xOff,
 int yOff,
 struct _XRegion *r,
 int op);
void XShapeCombineRectangles (
 Display *dpy,
 XID dest,
 int destKind,
 int xOff,
 int yOff,
 XRectangle *rects,
 int n_rects,
 int op,
 int ordering);
void XShapeCombineMask (
 Display *dpy,
 XID dest,
 int destKind,
 int xOff,
 int yOff,
 Pixmap src,
 int op);
void XShapeCombineShape (
 Display *dpy,
 XID dest,
 int destKind,
 int xOff,
 int yOff,
 Pixmap src,
 int srcKind,
 int op);
void XShapeOffsetShape (
 Display *dpy,
 XID dest,
 int destKind,
 int xOff,
 int yOff);
Status XShapeQueryExtents (
 Display *dpy,
 Window window,
 int *bShaped,
 int *xbs,
 int *ybs,
 unsigned int *wbs,
 unsigned int *hbs,
 int *cShaped,
 int *xcs,
 int *ycs,
 unsigned int *wcs,
 unsigned int *hcs);
void XShapeSelectInput (
 Display *dpy,
 Window window,
 unsigned longmask);
unsigned long XShapeInputSelected (
 Display *dpy,
 Window window);
XRectangle *XShapeGetRectangles (
 Display *dpy,
 Window window,
 int kind,
 int *count,
 int *ordering);</pre><h2>Structures</h2><pre>typedef struct {
 int type; /* of event */
 unsigned long serial; /* # of last request processed by server */
 Bool send_event; /* true if this came from a SendEvent request */
 Display *display; /* Display the event was read from */
 Window window; /* window of event */
 int kind; /* ShapeBounding or ShapeClip */
 int x, y; /* extents of new region */
 unsigned width, height;
 Time time; /* server timestamp when region changed */
 Bool shaped; /* true if the region exists */
} XShapeEvent;</pre><h2>Description</h2>The <i>X11 Nonrectangular Window Shape Extension</i> adds nonrectangular windows to the X Window System.
<h2>Predefined Values</h2>Operations:
<dl COMPACT><dd><pre><i>ShapeSet</i>
<i>ShapeUnion</i>
<i>ShapeIntersect</i>
<i>ShapeSubtract</i>
<i>ShapeInvert</i></pre></dl>
 

 Shape Kinds:
<dl COMPACT><dd><pre><i>ShapeBounding</i>
<i>ShapeClip</i></pre></dl>
 

 Event defines:
<dl COMPACT><dd><pre><i>ShapeNotifyMask</i>
<i>ShapeNotify</i></pre></dl><h2>Bugs</h2>This manual page needs a lot more work.
<h2>See Also</h2><i>X11 Nonrectangular Window Shape Extension</i>
