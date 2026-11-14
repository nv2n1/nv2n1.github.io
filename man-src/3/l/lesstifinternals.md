---
title: "lesstifinternals(3)"
name: "lesstifinternals"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lesstifinternals/"
description: "_Xm* – LessTif Internal Functions"
---

<p>_Xm* &#8211; LessTif Internal Functions</p>
<h2>Description</h2>
<p>When the LessTif project began some discussion was undertaken about the use of the previously undocumented internal _Xm.. functions in Motif 1.2. Apparently many of those functions have been transformed to Xme.. functions in OSF/Motif&#174; 2.x and are also documented. As many people use these functions in their code (especially widget writers) the implementation of the _Xm.. functions is important to the LessTif project. </p>
<p> Below is a (outdated!) list of functions currently taken from the LessTif header files.</p>
<h2>Convenience Functions</h2>
<p><code>void _XmCalcLabelDimensions(Widget w);</code> </p>
<p> Sets the core width and height values to the values needed to display the current label contents. It takes into account the label type as well as all of the margin resources. </p>
<p> <code>Boolean _XmGetInDragMode(Widget w);</code> </p>
<p> returns True, if the widget (e.g. push button,&#8230;) resides in a menu and the user is currently dragging the mouse with button 1 pressed over the menu items. This way a widget can figure out, whether it must redraw itself in the armed state if the widget gets a PrimitiveEnter action. </p>
<p> <code>Boolean _XmIsEventUnique(XEvent *event);</code> </p>
<p> Unknown Function </p>
<p> <code>Widget _XmGetRC_PopupPosted(Widget w);</code> </p>
<p> Returns the widget id of the parent of the menu that is currently posted by any of the children of w. In other words the id of the shell that is cascaded from menu w. </p>
<p> <code>void _XmRecordEvent(XEvent *event); </code> </p>
<p> Unknown Function </p>
<p> <code>void _XmSetInDragMode(Widget w, Boolean flag);</code> </p>
<p> this is used to enter or leave the dragging mode within the menu system. </p>
<p> <code>XmFontListEntry _XmFontListEntryFromTag(XmFontList fontlist, char *tag);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmCreateVisibilityRect(Widget w, XRectangle *rectPtr);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmCvtStringToXmNavigation(Display *, XrmValue *, Cardinal *, XrmValue *, XrmValue *, XtPointer *);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmCvtStringToXmString(Display *, XrmValue *, Cardinal *, XrmValue *, XrmValue *, XtPointer *);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmFocusIsHere(Widget w);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmFocusIsInShell(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmGrabTheFocus(Widget w, XEvent *event);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmIsNavigable(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmNavigSetValues(Widget current, Widget request, Widget new_wid, ArgList args, Cardinal *num_args);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmSearchColorCache(unsigned int which, XmColorData *values, XmColorData **ret);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmShellIsExclusive(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>Boolean _XmStringsAreEqual() </code> </p>
<p> Unknown Function </p>
<p> <code>Pixel _XmAccessColorData(XmColorData *cd, unsigned char which);</code> </p>
<p> Unknown Function </p>
<p> <code>Pixel _XmBlackPixel(Screen *screen, Colormap colormap, XColor blackcolor);</code> </p>
<p> Unknown Function </p>
<p> <code>Pixel _XmWhitePixel(Screen *screen, Colormap colormap, XColor whitecolor);</code> </p>
<p> Unknown Function </p>
<p> <code>Pixmap _XmGetPixmap();</code> </p>
<p> Unknown Function </p>
<p> <code>String _XmGetDefaultBackgroundColorSpec(Screen *screen);</code> </p>
<p> Unknown Function </p>
<p> <code>Time __XmGetDefaultTime(Widget w, XEvent *event);</code> </p>
<p> Unknown Function </p>
<p> <code>Widget _XmFindNextTabGroup(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>Widget _XmFindPrevTabGroup(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>Widget _XmFindTopMostShell(Widget w);</code> </p>
<p> Unknown Function </p>
<p> <code>Widget _XmGetActiveItem(Widget w);</code> </p>
<p> Unknown Function </p>
<p> <code>Widget _XmGetFirstFocus(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>Widget _XmNavigate(Widget wid, XmTraversalDirection direction);</code> </p>
<p> Unknown Function </p>
<p> <code>XmColorData *_XmAddToColorCache(XmColorData *new_rec);</code> </p>
<p> Unknown Function </p>
<p> <code>XmColorData *_XmGetColors(Screen *screen, Colormap color_map, Pixel background);</code> </p>
<p> Unknown Function </p>
<p> <code>XmColorData *_XmGetDefaultColors(Screen *screen, Colormap color_map);</code> </p>
<p> Unknown Function </p>
<p> <code>XmFocusData _XmCreateFocusData();</code> </p>
<p> Unknown Function </p>
<p> <code>XmFocusData _XmGetFocusData(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>XmFontList _XmGetDefaultFontList(Widget w, unsigned char fontListType);</code> </p>
<p> Unknown Function </p>
<p> <code>XmGadget _XmInputForGadget(Widget cw, int x, int y);</code> </p>
<p> Unknown Function </p>
<p> <code>XmGadget _XmInputInGadget(Widget cw, int x, int y);</code> </p>
<p> Unknown Function </p>
<p> <code>char * _XmGetBGPixmapName();</code> </p>
<p> Unknown Function </p>
<p> <code>char *_XmConvertCSToString(XmString cs);</code> </p>
<p> Unknown Function </p>
<p> <code>int _XmEmptyRect(XRectangle *r);</code> </p>
<p> Unknown Function </p>
<p> <code>int _XmIntersectRect(XRectangle *srcRectA, Widget widget, XRectangle *dstRect);</code> </p>
<p> Unknown Function </p>
<p> <code>unsigned char _XmGetFocusPolicy(Widget w);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmBackgroundColorDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmBottomShadowColorDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmCallFocusMoved(Widget old, Widget new_wid, XEvent *event);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmClearBGPixmap();</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmClearFocusPath(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmClearRect(XRectangle *r);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmConfigureObject(Widget g, Position x, Position y, Dimension width, Dimension height, Dimension border_width);</code> </p>
<p> _XmConfigureObject is a wrapper around <code><a href="/docs/linux/man/3-xtconfigurewidget/">XtConfigureWidget</a></code>(3) which insulates a widget writer from the burden of checking whether an object is a widget or a gadget. The way for a manager widget (any subclass of XmManager; they&#8217;re supposed to do geometry management for their children) to set the layout of a child is to use this function. In the case of a widget, XtConfigureWidget is called. For a gadget, the geometry fields are manipulated directly. </p>
<p> <code>void _XmDestroyFocusData(XmFocusData focusData);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDispatchGadgetInput(Widget g, XEvent *event, Mask mask);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmFocusModelChanged(Widget wid, XtPointer client_data, XtPointer call_data);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmForegroundColorDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmGetDefaultThresholdsForScreen(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmHighlightColorDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmManagerHighlightPixmapDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmManagerTopShadowPixmapDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmMgrTraversal(Widget wid, XmTraversalDirection direction);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmMoveObject(Widget g, Position x, Position y);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmNavigChangeManaged(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmNavigDestroy(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmNavigInitialize(Widget request, Widget new_wid, ArgList args, Cardinal num_args);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmNavigResize(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmPrimitiveEnter(Widget w, XEvent *event, String *params, Cardinal num_params);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmPrimitiveHighlightPixmapDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmPrimitiveLeave(Widget w, XEvent *event, String *params, Cardinal num_params);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmPrimitiveTopShadowPixmapDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmProcessTraversal(Widget w, XmTraversalDirection dir, Boolean check);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRedisplayGadgets(Widget w, XEvent *event, Region region);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRegisterConverters();</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRegisterPixmapConverters();</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmResetTravGraph(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmResizeObject(Widget g, Dimension width, Dimension height, Dimension border_width);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmSetActiveTabGroup(XmFocusData focusData, Widget tabGroup);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmSetDefaultBackgroundColorSpec(Screen *screen, String new_color_spec);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmSetInitialOfTabGroup(Widget tab_group, Widget init_focus);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmSetRect(XRectangle *rect, Widget w);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmTopShadowColorDefault(Widget widget, int offset, XrmValue *value);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmValidateFocus(Widget wid);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmWarning(Widget w, char *message);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmWidgetFocusChange(Widget wid, XmFocusChange change);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmCascadePixmapDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmClearBorder(Display *display, Window win, int x, int y, Dimension width, Dimension height, Dimension shadow_thickness)</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDefaultButtonShadowThickness(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDefaultMultiClick(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDrawArrow(Display *display, Window win, GC bottomGC, GC topGC, GC fillGC, Position x, Position y, Dimension width, Dimension height, Dimension shadow_thickness, unsigned char direction);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDrawDiamond(Display *display, Window win, GC bottomGC, GC topGC, GC selectGC, Position x, Position y, Dimension width, Dimension height, Dimension shadowThickness, Dimension fill);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDrawSeparator(Display *display, Window win, GC top_gc, GC bottom_gc, separator_GC, Position wx, Position wy, Dimension wwidth, Dimension wheight, Dimension shadowThickness, Dimension margin, unsigned char orientation, unsigned char separator_type);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDrawShadowDisplay *display, Drawable d, GC top_gc, GC bottom_gc, Dimension shad_thick, Position x, Position y, Dimension width, Dimension height);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmDrawShadows(Display *display, Window win, GC topShadowGC, GC bottomShadowGC, Position x, Position y, Dimension width, Dimension height, Dimension shadowThickness, unsigned int shadowType);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmFontListGetDefaultFont(XmFontList fontlist, XFontStruct **font_struct);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmFrameHorizSpaceDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmFrameShadowThicknessDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmFrameShadowTypeDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmInitializeWidgetSet();</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRowColumnEntryClassDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRowColumnIsHomogeneousDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRowColumnMarginDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRowColumnMenuAcceleratorDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRowColumnPackingDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmRowColumnSpacingDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmScrollBarMaximumDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmScrollBarProcessingDirectionDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmScrollBarSliderSizeDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmScrollBarTroughColorDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmScrollBarValueDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmSelectColorDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmToggleButtonIndicatorTypeDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmVendorShellVirtualBindingsDefault(Widget w, int offset, XrmValue *val);</code> </p>
<p> Unknown Function </p>
<p> <code>String _XmOSGetHomeDirName(void);</code> </p>
<p> Unknown Function </p>
<p> <code>XmString _XmOSGetLocalizedString(char *reserved, </code> </p>
<p> Unknown Function </p>
<p> <code>int _XmMicroSleep(long secs);</code> </p>
<p> Unknown Function </p>
<p> <code>void _XmInternAtomAndName(Display *display, Atom atom, String name);</code> </p>
<p> Associates an atom name with an atom id (and vice versa) without the need to query the X server first for the atom id. This way any name to id mapping (as well as the id to name mapping) can be set on a given display. </p>
<p> <code>void _XmVirtualToActualKeysym(Display *Dsp, KeySym VirtualKeysym, KeySym *RealKeysymReturn, Modifiers *ModifierReturn);</code> </p>
<p> For the given virtual keysym (which must be one of the = osfXK_xxx keysyms) returns the real keysym as well as the modifiers which make up that particular virtual keysym. If asked for an invalid virtual keysym, _XmVirtualToActualKeysym returns NoSymbol for the real keysym. </p>
<p> <code>int _XmVirtKeysLoadFallbackBindings(Display *Dsp, String *Bindings);</code> </p>
<p> Installs the default key bindings for a specific display. If th= ere are any vendor specific default bindings available, then the appropiate one= will be installed instead of the fallback key bindings. Additionally, the bindings installed are returned in Bindings. The caller is responsible for freeing the space occupied by this key binding description string. The return code seems to be always zero. At least LessTif will always retur= n a zero&#8230; </p>
<p> <code>Boolean _XmVirtKeysLoadFileBindings(String filename, String *binding= );</code> </p>
<p> Reads in a file containing a description of the virtual key bindings. If succesful, returns True and the description string. The caller= is responsible for freeing the memory lateron. </p>
<p> <code>void _XmVirtKeysInitialize(Widget w);</code> </p>
<p> Sets up the virtual key bindings for a display. The widget specified must be a XmDisplay widget, otherwise _XmVirtKeysInitialize will deny the attempt to set up the key bindings. The function first checks several places in order to catch up key binding description. If all fails, it will install fallback key bindings. This internal function is called during when initializing a XmDisplay widget. </p>
<p> <code>void _XmVirtKeysDestroy(Widget w);</code> </p>
<p> Cleanup any leftovers from the virtual binding mechanism when destroying a XmDisplay widget. </p>
<p> <code>void _XmVirtKeysHandler(Widget w, XtPointer Data, XEvent *Event, Boolean *ContDispatch);</code> </p>
<p> This handler is installed on every widget. It just records the current key press event in an widget instance field private to a XmDisplay widget.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/1x-lesstif/">lesstif</a></code>(1x)</p>
