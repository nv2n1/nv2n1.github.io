---
title: "xmnotebook(3)"
name: "xmnotebook"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmnotebook/"
description: "XmNotebook — The Notebook widget class"
---

<p><code>XmNotebook</code> &#8212; The Notebook widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Notebook.h&gt;</pre>
<h2>Description</h2>
<p>Notebook is a manager widget that organizes its children into pages, tabs, status areas, and page scrollers to simulate a real notebook. It stacks its page children so that all page children occupy the same area like real book pages. Notebook displays visuals that look like the binding of a book and the edges of other pages around the page that is shown. Tab children simulate notebook tabs. Major tabs divide Notebook into several sections, and minor tabs subdivide these sections. Status area children provide additional information about pages such as page numbers. The page scroller child allows the user to move from page to page. Notebook also provides tab scrollers for scrolling major and minor tabs if it cannot display all tabs within its edges. </p>
<p> The application creates pages, tabs, status areas, and page scroller as children of the Notebook widget. Notebook creates tab scrollers when the Notebook is created. </p>
<p> The <code>XmNnotebookChildType</code> constraint resource of Notebook determines whether a child widget is a page, tab, status area, or page scroller. Any Motif widget can be a page of the Notebook. When the application creates a child of the Notebook widget without setting the child type constraint, the child becomes a page by default, unless it has the <code>XmQTactivatable</code>, <code>XmQTaccessTextual</code>, or <code>XmQTnavigator</code> trait. Children with the <code>XmQTactivatable</code>, <code>XmQTaccessTextual</code>, or <code>XmQTnavigator</code> trait become major tabs, status areas, and page scrollers, respectively. </p>
<p> Notebook uses the <code>XmQTaccessTextual</code>, <code>XmQTactivatable</code>, <code>XmQTjoinSide</code>, and <code>XmQTnavigator</code> traits, and installs the <code>XmQTscrollFrame</code> trait. </p>
<p> The application attaches a tab to a page by creating a tab child of the Notebook and setting the <code>XmNpageNumber</code> constraint to the page number of the targeted page. By the same method, a status area widget can be attached to a page. The page scroller child, on the other hand, is associated with the Notebook, not with a specific page. Therefore, there is only one valid page scroller for each Notebook.</p>
<h3>Pages</h3>
<p>Only one child of type <code>XmPAGE</code> is displayed at a time by Notebook. Other page children are hidden off-screen. When Notebook displays a particular page, it positions the previously-displayed page off-screen and puts the new page in its place. The page is resized to fit into the dimensions that Notebook has allocated to display pages.</p>
<h3>Page Numbers</h3>
<p>Notebook uses the <code>XmNcurrentPageNumber</code>, <code>XmNfirstPageNumber</code>, and <code>XmNlastPageNumber</code> resources to determine the current page and available page number range. Only those pages whose page numbers are within the range can be displayed. Other pages cannot be displayed until the range between <code>XmNfirstPageNumber</code> and <code>XmNlastPageNumber</code> is changed to include them or their page numbers are changed to a number within the range. </p>
<p> If <code>XmNfirstPageNumber</code> and <code>XmNlastPageNumber</code> are not set explicitly by the application, they are set to 1 by default; Notebook sets <code>XmNlastPageNumber</code> to the largest page number assigned by the application thereafter by default. However, once <code>XmNlastPageNumber</code> is set by the application, Notebook no longer changes it even when a page with a higher page number is managed. </p>
<p> The <code>XmNpageNumber</code> constraint resource is used for specifying the page number of a page widget. It can be set to any integer. For tab and status area children, the resource is used for linking the child widget to a page. For the page scroller child, the resource has no meaning and is ignored by the Notebook. </p>
<p> When a page without a page number is managed, Notebook assigns it the smallest unallocated page number that is not less than the first page number and greater than the last allocated page number. When a tab or a status area without a page number is managed, the newly managed widget is assigned the page number of the most recently managed page, unless the page already has the same type of child. If the page does have the same type of child, Notebook assigns the newly managed widget a page number one greater than the most recently managed page; this new page number is now occupied. Notebook may generate a default page number greater than <code>XmNlastPageNumber</code>, making those pages inaccessible to the user.</p>
<h3>Duplicate and Empty Pages</h3>
<p>Since an application can create or change page numbers, it is possible to have duplicate page numbers and empty pages. When two pages with the same page number are managed, only the more recently managed page can be displayed. Inserting a page with an existing page number does not cause a warning. The old page widget cannot be displayed until the new page widget is removed from the Notebook or until the page number of the old page widget is changed to some other number. </p>
<p> An empty page is a page slot where no page is inserted. Empty pages occur when a tab or status area is associated with a page number that has no matching page widget. Empty pages display the blank Notebook background unless the application provides visual information to this empty area while processing <code>XmNpageChangedCallback</code>.</p>
<h3>Notebook Visuals</h3>
<p>Notebook draws lines around two sides of the top page to simulate the edges of other pages that are behind the top page. The <code>XmNbackPagePlacement</code> and <code>XmNorientation</code> resources determine which two sides have the lines drawn around them. By default, they are drawn on the bottom and right sides of the top page. The application can set resources to control how many lines are drawn and how wide the area that they are drawn in is. Applications can also choose from three styles of binding visual that simulates the binding of a Notebook. Solid or spiral bindings can be drawn by Notebook, or the application can supply a pixmap that is tiled into the binding.</p>
<h3>Tabs</h3>
<p>A major or minor tab is a Motif widget with the <code>XmQTactivatable</code> trait. If a widget without the trait is created for a tab, Notebook does not provide the page activation callback. As a result, even though the tab is displayed, it cannot automatically move the associated page to the top. </p>
<p> Major tabs divide the Notebook pages into sections. Minor tabs subdivide these sections. Only minor tabs associated with the current section are displayed, where a section consists of the group of pages between the current major tab and the next major tab, including the current major tab but not including the page containing the next major tab. The exception to this is when there is no preceding major tab, in which case the section starts from the <code>XmNfirstPageNumber</code> value. A user in one major tab section does not see the minor tabs in other sections. However, all tabs are used in computing the size of the Notebook. </p>
<p> Unlike regular notebook tabs, tabs in the Notebook are not attached to a physical page (a widget). They are, instead, attached to a logical page (a page number). Therefore, it is possible to have a tab with an empty page. When a page with a tab is removed from the Notebook, the tab is not removed because it is still bound to a logical page. Destroying or unmanaging a page widget only erases the page and leaves an empty page. It does not tear the page out of the Notebook. To remove the tab, the application must explicitly destroy or unmanage it. </p>
<p> Notebook supports the <code>XmQTjoinSide</code> trait. A widget that has the <code>XmQTjoinSide</code> trait can be added to the Notebook as a Major or Minor tab and will appear to be attached to its associated page with no margins or shadows between them.</p>
<h3>Status Areas</h3>
<p>A status area is any widget that is used for describing the associated page. For example, the Label widget as a status area child can hold a simple string or a pixmap that describes a page. A status area widget is also attached to a page by the page number constraint resource. Therefore, it is possible to have multiple status area widgets for one page. Only the most recently managed status area widget for that page can be displayed. All others for that page are not unmanaged, but their sizes are used for computing the size of the Notebook. If no status area widget is provided, the Notebook displays its blank background in the status area&#8217;s reserved space. Notebook does not create any default status area widget.</p>
<h3>Page Scrollers</h3>
<p>The page scroller of the Notebook is any widget that the application creates for scrolling pages. If the application does not create one when the Notebook is realized, Notebook creates a SpinBox widget as the default page scroller. If the application creates a new page scroller, the default page scroller is destroyed. If the application creates multiple page scrollers, only the most recently managed one can be displayed and used. All others are unmanaged. </p>
<p> The default SpinBox page scroller grays out one of the arrow visuals if the current page is a boundary page. If the current page is the first page, the previous arrow of the SpinBox is grayed. If the current page is the last page, the next arrow of the SpinBox is grayed.</p>
<h3>Tab Scrollers</h3>
<p>Tab scrollers are created by the Notebook for scrolling major tabs and minor tabs. When Notebook is initialized, it creates four ArrowButtonGadgets for scrolling to the next major tab, the previous major tab, the next minor tab, and the previous minor tab. The application cannot replace these tab scrollers. The application can change all resources of these widgets except the position and the arrow direction. Tab scrollers are only visible and enabled when there is not enough space to display all the major or minor tabs appropriate to the page. Tab scrollers are also grayed out when scrolling is inappropriate. The following lists the tab scrollers that are created: </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3> <code>Child Widgets that XmNotebook Creates</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Child</code></td>
<td><code>Name</code></td>
<td><code>Widget Class</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Page Scroller</td>
<td>PageScroller</td>
<td>XmSpinBox
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Next Major Tab Scroller</td>
<td>MajorTabScrollerNext</td>
<td>XmArrowButtonGadget
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Previous Major Tab Scroller</td>
<td>MajorTabScrollerPrevious</td>
<td>XmArrowButtonGadget
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Next Minor Tab Scroller</td>
<td>MinorTabScrollerNext</td>
<td>XmArrowButtonGadget
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Previous Minor Tab Scroller</td>
<td>MinorTabScrollerPrevious</td>
<td>XmArrowButtonGadget
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<p> When the user selects the page scroller, a major tab, or a minor tab, the value of <code>XmNcurrentPageNumber</code> is changed to the selected page number and <code>XmNpageChangedCallback</code> is invoked. After the application returns from the callback, the Notebook displays the last page child whose page number is equal to the current page number. It also displays the last matched status area child. All other pages and status areas are automatically hidden. Major tabs and minor tabs that can fit into the Notebook&#8217;s edges are displayed and positioned appropriately. All other tabs are also hidden. The application can also cause a page change by calling <code>XtSetValues</code> on <code>XmNcurrentPageNumber</code> and then calling <code>XtCallCallbacks</code> on <code>XmNpageChangedCallback</code>.</p>
<h3>Orientation</h3>
<p>The Notebook has eight different visual configurations, depending on the value of <code>XmNbackPagePlacement</code> and <code>XmNorientation</code>. These two resources determine the placement of back pages, the binding, major tabs, minor tabs, the status area, and the page scroller. The location of the binding is determined by <code>XmNorientation</code>. Major tabs are always placed on the back page side opposite to the binding; Minor tabs are placed on the back page display area that is visually connected to the binding. Both Major and Minor tabs are ordered so that the page numbers they access increase as they get closer to the corner where the back pages meet. The status area and the page scroller are always located on the bottom of the Notebook, inside the frame. The page scroller is always placed adjacent to a back page side. The following table shows the possible configurations and the locations of each Notebook component within the configuration. The default back page value and the default orientation are based upon <code>XmNlayoutDirection</code>. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Notebook Configurations</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNbackPagePlacement</code></td>
<td><code>XmNorientation</code></td>
<td><code>Major Tabs</code></td>
<td><code>Status Area</code></td>
<td><code>Binding</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td><code>Minor Tabs</code></td>
<td><code>Page Scroller</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmBOTTOM_RIGHT</td>
<td>XmHORIZONTAL</td>
<td>RIGHT</td>
<td>BOTTOM LEFT</td>
<td>LEFT
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>BOTTOM</td>
<td>BOTTOM RIGHT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmBOTTOM_RIGHT</td>
<td>XmVERTICAL</td>
<td>BOTTOM</td>
<td>BOTTOM LEFT</td>
<td>TOP
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>RIGHT</td>
<td>BOTTOM RIGHT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmBOTTOM_LEFT</td>
<td>XmHORIZONTAL</td>
<td>LEFT</td>
<td>BOTTOM RIGHT</td>
<td>RIGHT
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>BOTTOM</td>
<td>BOTTOM LEFT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmBOTTOM_LEFT</td>
<td>XmVERTICAL</td>
<td>BOTTOM</td>
<td>BOTTOM RIGHT</td>
<td>TOP
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>LEFT</td>
<td>BOTTOM LEFT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmTOP_RIGHT</td>
<td>XmHORIZONTAL</td>
<td>RIGHT</td>
<td>BOTTOM LEFT</td>
<td>LEFT
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>TOP</td>
<td>BOTTOM RIGHT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmTOP_RIGHT</td>
<td>XmVERTICAL</td>
<td>TOP</td>
<td>BOTTOM LEFT</td>
<td>BOTTOM
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>RIGHT</td>
<td>BOTTOM RIGHT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmTOP_LEFT</td>
<td>XmHORIZONTAL</td>
<td>LEFT</td>
<td>BOTTOM RIGHT</td>
<td>RIGHT
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>TOP</td>
<td>BOTTOM LEFT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmTOP_LEFT</td>
<td>XmVERTICAL</td>
<td>TOP</td>
<td>BOTTOM RIGHT</td>
<td>BOTTOM
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>LEFT</td>
<td>BOTTOM LEFT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<p> There are three tab groups for tab group traversal inside the Notebook: major tabs, minor tabs, and the page scroller. The application can also create additional types of tab groups within the Notebook; for example, each page added by the application is treated as a separate tab group by the traversal actions.</p>
<h3>Classes</h3>
<p>Notebook inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmNotebookWidgetClass</code>. </p>
<p> The class name is <code>XmNotebook</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmNotebook Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackPageBackground</td>
<td>XmCBackPageBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackPageForeground</td>
<td>XmCBackPageForeground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackPageNumber</td>
<td>XmCBackPageNumber</td>
<td>Cardinal</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackPagePlacement</td>
<td>XmCBackPagePlacement</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackPageSize</td>
<td>XmCBackPageSize</td>
<td>Dimension</td>
<td>8</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbindingPixmap</td>
<td>XmCBindingPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbindingType</td>
<td>XmCBindingType</td>
<td>unsigned char</td>
<td>XmSPIRAL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbindingWidth</td>
<td>XmCBindingWidth</td>
<td>Dimension</td>
<td>25</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcurrentPageNumber</td>
<td>XmCCurrentPageNumber</td>
<td>int</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfirstPageNumber</td>
<td>XmCFirstPageNumber</td>
<td>int</td>
<td>1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNframeBackground</td>
<td>XmCFrameBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNframeShadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinnerMarginHeight</td>
<td>XmCInnerMarginHeight</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinnerMarginWidth</td>
<td>XmCInnerMarginWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlastPageNumber</td>
<td>XmCLastPageNumber</td>
<td>int</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNminorTabSpacing</td>
<td>XmCMinorTabSpacing</td>
<td>Dimension</td>
<td>3</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmajorTabSpacing</td>
<td>XmCMajorTabSpacing</td>
<td>Dimension</td>
<td>3</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNorientation</td>
<td>XmCOrientation</td>
<td>unsigned char</td>
<td>XmHORIZONTAL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpageChangedCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNbackPageBackground</code></p>
<dd>Specifies the background color for drawing back pages. The default is a lower-intensity version of <code>XmNframeBackground</code>.</p>
<dt><code>XmNbackPageForeground</code></p>
<dd>Specifies the forground color for drawing back pages. The default is taken from the application&#8217;s default foreground color.</p>
<dt><code>XmNbackPageNumber</code></p>
<dd>Specifies the number of lines to draw for back pages. The minimum value is 1, and the maximum value is (<code>XmNbackPageSize</code> / 2).</p>
<dt><code>XmNbackPagePlacement</code></p>
<dd>Specifies where to place the back pages. The default is dependent on the <code>XmNlayoutDirection</code> resource of the Notebook&#8217;s instance parents. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmBOTTOM_RIGHT</code></p>
<dd>Displays back pages on the Notebook&#8217;s bottom and right sides.</p>
<dt><code>XmBOTTOM_LEFT</code></p>
<dd>Displays back pages on the Notebook&#8217;s bottom and left sides.</p>
<dt><code>XmTOP_RIGHT</code></p>
<dd>Displays back pages on the Notebook&#8217;s top and right sides.</p>
<dt><code>XmTOP_LEFT</code></p>
<dd>Displays back pages on the Notebook&#8217;s top and left sides.</dl>
</dl>
<dt><code>XmNbackPageSize</code></p>
<dd>Specifies the thickness of the back page rendering.</p>
<dt><code>XmNbindingPixmap</code></p>
<dd>Specifies the pixmap or bitmap for stippling or tiling the binding when <code>XmNbindingType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_OVERLAP_ONLY</code>.</p>
<dt><code>XmNbindingType</code></p>
<dd>Specifies the binding type. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmNONE</code></p>
<dd>Displays no binding.</p>
<dt><code>XmSOLID</code></p>
<dd>Displays a solid binding in the foreground color of the Notebook within the binding area specified by <code>XmNbindingWidth</code>.</p>
<dt><code>XmSPIRAL</code></p>
<dd>Displays a spiral binding in the foreground color of the Notebook within the area specified by <code>XmNbindingWidth</code> and within the area outside of the frame equal to the area specified by <code>XmNbindingWidth</code>.</p>
<dt><code>XmPIXMAP</code></p>
<dd>Displays the binding with the pixmap or bitmap specified by <code>XmNbindingPixmap</code> as a stipple or tile. It uses the foreground color of the Notebook for stippling. The binding width is decided by the larger value of <code>XmNbindingWidth</code> and the width of the pixmap or bitmap.</p>
<dt><code>XmPIXMAP_OVERLAP_ONLY</code></p>
<dd>Displays the binding with the pixmap or bitmap specified by <code>XmNbindingPixmap</code> as a stipple or tile. It uses the foreground color of the Notebook for stippling. The binding is displayed only within the binding area specified by <code>XmNbindingWidth</code>.</dl>
</dl>
<dt><code>XmNbindingWidth</code></p>
<dd>Specifies the width of the Notebook binding. If <code>XmNbindingType</code> is <code>XmPIXMAP</code> and the width of the pixmap specified in <code>XmNbindingPixmap</code> is greater than <code>XmNbindingWidth</code>, then this resource is ignored and the width of the pixmap is used as the width of the Notebook binding instead.</p>
<dt><code>XmNcurrentPageNumber</code></p>
<dd>Specifies the page number of the currently displayed page. Initially, it is set to <code>XmNfirstPageNumber</code>. If it is set to less than <code>XmNfirstPageNumber</code>, then it is set to <code>XmNfirstPageNumber</code>. If it is set to <code>XmNlastPageNumber</code>, then it is set to <code>XmNlastPageNumber</code>.</p>
<dt><code>XmNfirstPageNumber</code></p>
<dd>Specifies the page number for the first page of the Notebook. The Notebook does not scroll to any page numbers below this value.</p>
<dt><code>XmNframeBackground</code></p>
<dd>Specifies the background color for drawing the Notebook&#8217;s frame.</p>
<dt><code>XmNframeShadowThickness</code></p>
<dd>Specifies the shadow thickness around the Notebook&#8217;s frame.</p>
<dt><code>XmNinnerMarginHeight</code></p>
<dd>Specifies the margin on the top and bottom sides of the page, status area, and page scroller widgets.</p>
<dt><code>XmNinnerMarginWidth</code></p>
<dd>Specifies the margin on the left and right sides of the page, status area, and page scroller widgets.</p>
<dt><code>XmNlastPageNumber</code></p>
<dd>Specifies the page number for the last page of the Notebook. The Notebook does not scroll to any page numbers above this value. The default page number is the largest page number of managed page, major tab, or minor tab widgets. If this is set to a value that is less than <code>XmNfirstPageNumber</code>, the behavior of the Notebook is undefined.</p>
<dt><code>XmNmajorTabSpacing</code></p>
<dd>Specifies the spacing distance between major tabs. If <code>XmNframeShadowThickness</code> is greater than <code>XmNmajorTabSpacing</code>, then this resource is ignored and the size of <code>XmNframeShadowThickness</code> is used as the spacing distance between major tabs.</p>
<dt><code>XmNminorTabSpacing</code></p>
<dd>Specifies the spacing distance between minor tabs. If <code>XmNframeShadowThickness</code> is greater than <code>XmNminorTabSpacing</code>, then this resource is ignored and the size of <code>XmNframeShadowThickness</code> is used as the spacing distance between minor tabs.</p>
<dt><code>XmNorientation</code></p>
<dd>Specifies the orientation of the Notebook. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmHORIZONTAL</code></p>
<dd>Places the binding beside the pages, in the left or right side of the frame.</p>
<dt><code>XmVERTICAL</code></p>
<dd>Places the binding above or below the pages, in the top or the bottom of the frame.</dl>
</dl>
<dt><code>XmNpageChangedCallback</code></p>
<dd>Specifies the list of callbacks to call whenever the <code>XmNcurrentPageNumber</code>, representing the current page number, is changed. This includes the point when the widget is realized and the page number is initialized. The callback structure is <code>XmNotebookCallbackStruct</code>. The reason is <code>XmCR_MAJOR_TAB</code>, <code>XmCR_MINOR_TAB</code>, <code>XmCR_PAGE_SCROLLER_INCREMENT</code>, <code>XmCR_PAGE_SCROLLER_DECREMENT</code>, or <code>XmCR_NONE</code>, depending upon what action caused the Notebook to display a new page.</dl>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmNotebook Constraint Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnotebookChildType</td>
<td>XmCNotebookChildType</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpageNumber</td>
<td>XmCPageNumber</td>
<td>int</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNresizable</td>
<td>XmCResizable</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNnotebookChildType</code></p>
<dd>Specifies the child type of the Notebook. It can be one of the following types:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPAGE</code></p>
<dd>The child is a page of the Notebook. This is the default when the child does not have the <code>XmQTactivatable</code>, <code>XmQTaccessTextual</code>, or <code>XmQTnavigator</code> trait.</p>
<dt><code>XmMAJOR_TAB</code></p>
<dd>The child is a major tab. This is the default when the child has the <code>XmQTactivatable</code> trait.</p>
<dt><code>XmMINOR_TAB</code></p>
<dd>The child is a minor tab.</p>
<dt><code>XmSTATUS_AREA</code></p>
<dd>The child is a status area. This is the default when the child has the <code>XmQTaccessTextual</code> trait and does not have the <code>XmQTactivatable</code> trait.</p>
<dt><code>XmPAGE_SCROLLER</code></p>
<dd>The child is the page scroller. The default page scroller is destroyed, if it exists. Any previously created page scrollers are unmanaged. This is the default when the child has the <code>XmQTnavigator</code> trait and does have the <code>XmQTactivatable</code> trait or the <code>XmQTaccessTextual</code> trait.</dl>
</dl>
<dt><code>XmNpageNumber</code></p>
<dd>Specifies the page number associated with the widget. If the widget is a page, the number specifies the page number of the widget. If the widget is not a page, the number specifies the page number of the associated page. If none is supplied by the application, Notebook generates the smallest unallocated page number when the child is managed. This resource is ignored for the page scroller.</p>
<dt><code>XmNresizable</code></p>
<dd>Specifies whether this child can request a resize.</dl>
<h3>Inherited Resources</h3>
<p>Notebook inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmManager Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNforeground</td>
<td>XmCForeground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhelpCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightPixmap</td>
<td>XmCHighlightPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialFocus</td>
<td>XmCInitialFocus</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlayoutDirection</td>
<td>XmCLayoutDirection</td>
<td>XmDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmTAB_GROUP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpopupHandlerCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Composite Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNchildren</td>
<td>XmCReadOnly</td>
<td>WidgetList</td>
<td>NULL</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinsertPosition</td>
<td>XmCInsertPosition</td>
<td>XtOrderProc</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumChildren</td>
<td>XmCReadOnly</td>
<td>Cardinal</td>
<td>0</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Core Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackgroundPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdestroyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNx</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<h3>Callback</h3>
<p>A pointer to the following structure is passed to callbacks for <code>XmNpageChangedCallback</code>. </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>*event</i>;
 int <i>page_number</i>;
 Widget <i>page_widget</i>;
 int <i>prev_page_number</i>;
 Widget <i>prev_page_widget</i>;
} XmNotebookCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Specifies the reason for the callback.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>page_number</i></p>
<dd>Indicates the page number to be displayed.</p>
<dt><i>page_widget</i></p>
<dd>Indicates the page widget that has the new page number. It is NULL if no page widget with the page number is found.</p>
<dt><i>prev_page_number</i></p>
<dd>Indicates the page number of the currently displayed page. If the callback procedure is being called at widget initialization, this page number will be returned as <code>XmUNSPECIFIED_PAGE_NUMBER</code>.</p>
<dt><i>prev_page_widget</i></p>
<dd>Indicates the currently displayed page widget. If the callback procedure is being called at widget initialization, NULL will be returned.</dl>
<h3>Translations</h3>
<p>Notebook inherits translations from Manager.</p>
<h3>Accelerators</h3>
<p>Notebook accelerators are added to all major tab and minor tab children of XmNotebook. Notebook accelerators are listed below. These accelerators might not directly correspond to a translation table.</p>
<dl COMPACT>
<dt><code>&lt;osfBeginLine&gt;</code><code>:</code></p>
<dd>TraverseTab(<code>Home</code>)</p>
<dt><code>&lt;osfEndLine&gt;</code><code>:</code></p>
<dd>TraverseTab(<code>End</code>)</p>
<dt><code>&lt;osfLeft&gt;</code><code>:</code></p>
<dd>TraverseTab(<code>Previous</code>)</p>
<dt><code>&lt;osfRight&gt;</code><code>:</code></p>
<dd>TraverseTab(<code>Next</code>)</p>
<dt><code>&lt;osfUp&gt;</code><code>:</code></p>
<dd>TraverseTab(<code>Previous</code>)</p>
<dt><code>&lt;osfDown&gt;</code><code>:</code></p>
<dd>TraverseTab(<code>Next</code>)</dl>
<h3>Action Routines</h3>
<p>Notebook action routines are described below:</p>
<dl COMPACT>
<dt>TraverseTab(<code>Home|End|Next|Previous</code>)</p>
<dd>Moves the focus on major or minor tabs.</dl>
<h3>Additional Behavior</h3>
<p>The Notebook widget has the additional behavior described below:</p>
<dl COMPACT>
<dt><code>&lt;Tab&gt;</code></p>
<dd>Notebook intercepts tab group traversal when traversal is entering or leaving major or minor tabs. It does this to support major tabs and minor tabs as two separate tab groups when they are actually treated as one by traversal. If a minor tab has keyboard focus and a user or program action specifies <code>XmTRAVERSE_PREV_TAB_GROUP</code>, keyboard focus will go to a major tab. If a major tab has keyboard focus and a user or program action specifies <code>XmTRAVERSE_NEXT_TAB_GROUP</code>, keyboard focus will go to a minor tab.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatenotebook/">XmCreateNotebook</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmnotebookgetpageinfo/">XmNotebookGetPageInfo</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatenotebook/">XmVaCreateNotebook</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagednotebook/">XmVaCreateManagedNotebook</a></code>(3).</p>
