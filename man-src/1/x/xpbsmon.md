---
title: "xpbsmon(1)"
name: "xpbsmon"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpbsmon/"
description: "xpbsmon – GUI for displaying, monitoring the nodes/execution hosts under PBS"
---

<h2 class="name">NAME</h2>
<p> xpbsmon &#8211; GUI for displaying, monitoring the nodes/execution hosts under PBS </p>
<h2>SYNOPSIS</h2>
<p> xpbsmon</p>
<h2>DESCRIPTION</h2>
<p> The <code>xpbsmon</code> command provides a way to graphically display the various nodes that run jobs. A node or execution host can be running a <code>pbs_mom</code> daemon, or not running the daemon. For the latter case, it could just be a nodename that appears in a nodes file that is managed by a main <code>pbs_server </code> running on another host. This utility also provides the ability to monitor values of certain system resources by posting queries to the <code>pbs_mom</code> of a node. With this utility, you can see what job is running on what node, who owns the job, how many nodes assigned to a job, status of each node (color-coded and the colors are user-modifiable), how many nodes are available, free, down, reserved, offline, of unknown status, in use running multiple jobs or executing only 1 job. Please see the sections below for a tour and tutorials of xpbsmon. Also, within every dialog box, a <code>Help</code> button can be found for assistance.</p>
<h2>GETTING STARTED</h2>
<p> Running xpbsmon will initialize the X resource database from various sources in the following order:</p>
<dl>
<dt>1.</p>
<dd> The <code>RESOURCE_MANAGER</code> property on the root window (updated via xrdb) with settings usually defined in the .Xdefaults file</p>
<dt>2.</p>
<dd> Preference settings defined by the system administrator in the global xpbsmonrc file</p>
<dt>3.</p>
<dd> User&#8217;s ~/.xpbsmonrc file &#8211; this file defines various X resources like fonts, colors, list of colors to use to represent the various status of the nodes, list of PBS sites to query, list of server hosts on each site, list of nodes/execution hosts on each server host, list of system resource queries to send to the nodes&#8217; pbs_mom, and various view states. See PREFERENCES section below for a list of resources that can be set.</dl>
<h2>RUNNING XPBSMON</h2>
<p> <code>xpbsmon</code> can be run either as a regular user or superuser. If you run it with less privilege, you may not be able to see all the information for a node. If it is executed as a regular user, you should still be able to see what jobs are running on what nodes, possibly state and properties as these information are obtained by xpbsmon talking directly to the specified server. If you want other system resource values, it may require special privilege since xpbsmon will have to talk directly to the pbs_mom of a node. In addition, the host where xpbsmon was running must also have been given explicit access permission by the mom (unless the GUI is running on the same host where mom is running). This is done done by updating the $clienthost and/or the $restricted parameter on the mom&#8217;s configuration file. </p>
<p> To run <code>xpbsmon</code>, type:</p>
<dl>
<dt>
<dd>
<p> <code> </p>
</dl>
<p> If you are running the GUI and only interested in jobs data, then be sure to set all the nodes&#8217; type to NOMOM in the Pref</code> dialog box.</p>
<h2>THE XPBSMON DISPLAY</h2>
<p> This section describes the main parts of the <code>xpbsmon</code> display. The main window is composed of 3 distinct areas (subwindows) arranged vertically (one on top of another) in the following order:</p>
<dl>
<dt>
<dd> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1) Menu<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2) Site Information<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3) Info
</dl>
<p> <code>Menu</code>. The Menu area is composed of a row of command buttons that signal some action with a click of the left mouse button. The buttons are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Site..</p>
<dd>
&nbsp;<wbr>displays a popup menu containing the list of PBS sites that have been added using the Sites Preferences window. Simply drag your mouse and release to the site name whose servers/nodes information you would like to see.</p>
<dt>Pref..</p>
<dd> brings up various dialog boxes for specifying the list of sites, servers on each site, nodes that are known to a server, and the system resource queries to be sent to a node&#8217;s pbs_mom daemon.</p>
<dt>Auto Update..</p>
<dd> brings up another window for specifying whether or not to do auto updates of nodes information, and also for specifying the interval number of minutes between updates.</p>
<dt>Help</p>
<dd> contains some help information.</p>
<dt>About</p>
<dd> tells who the author is and who to send comments, bugs, suggestions to.</p>
<dt>Close</p>
<dd> for exiting <code>xpbsmon</code> plus saving the current setup information (if anything had changed) in the user&#8217;s $HOME/.xpbsmonrc file. Information saved include the specified list of sites, servers on each site, nodes known to each server, and system resource queries to send to node&#8217;s pbs_mom.</p>
<dt>Minimize Button</p>
<dd> shows the iconized view of Site Information where nodes are represented as tiny boxes, where each box is colored according to status. In order to get more information about a node, you need to double click on the colored box.</p>
<dt>Maximize button</p>
<dd> shows the full view of Site Information where nodes are represented in bigger boxes, still colored depending on the status, and some information on it is displayed.</dl>
</dl>
<p> <code>Site Information</code>. Only one site at a time can be displayed. This area (shown as one huge box referred to as the site box) can be further sub-divided into 3 areas: the site name label at the top, server boxes in the middle, and the color status bar at the bottom. The site name label shows the name of the site as specified in the <code>Pref..</code> window. At the middle of the site box shows a row of big boxes housing smaller boxes. </p>
<p> The big box is an abstraction of a server host (called a server box), showing its server display label at the top of the box, a grid of smaller boxes representing the nodes that the server knows about (where jobs are run), and summary status for the nodes under the server. Status information will show counters for the number of nodes used, available, reserved, offline, or of unknown status and even # of cpus assigned. For a cleaner display, some counters with a value of zero are not displayed. The server boxes are placed in a grid, with a new row being started when either *siteBoxMaxNumServerBoxesPerRow or *siteBoxMaxWidth limit has been reached. </p>
<p> The smaller boxes represent the nodes/execution hosts where jobs are run (referred to as node boxes). Each node box shows the name at the top, and a sub-box (a smaller square) that is is colored according to the status of the node that it represents, and if the view type is FULL, it will will display some node information according to the system resource queries specified on the <code>Pref..</code> window. Clicking on the sub-box will show a much bigger box (called the MIRROR view) with bigger fonts containing nodes information. Another view is called ICON and this shows a tiny box with a colored area. The node boxes are arranged in a grid, where a new row is created if either the *serverBoxMaxNumNodeBoxesPerRow or *serverBoxMaxWidth limit has been reached. ICON view of the node boxes will be constrained by the *nodeBoxIconMaxHeight and *nodeBoxIconMaxWidth pixel values; FULL view of the node boxes will be bounded by *nodeBoxFullMaxWidth and *nodeBoxFullMaxHeight; the mirror view of the node boxes has its size be *nodeBoxMirrorMaxWidth, and *nodeBoxMirrorMaxHeight. </p>
<p> Horizontal and vertical scrollbars for the site box, server box, and node box will be displayed as needed. </p>
<p> Finally, the color bar information shows a color chart displaying what the various colors mean in terms of node status. The color-to-status mapping can be modified by setting the X resources: *nodeColorNOINFO, *nodeColorFREE, *nodeColorINUSEshared, *nodeColorINUSEexclusive, *nodeColorDOWN, *nodeColorRSVD, *nodeColorOFFL. </p>
<p> <code>Info</code>. The Info Area shows the progress of some of the background actions performed by <code>xpbsmon</code>. Look into this box for errors.</p>
<h2>WIDGETS USED IN XPBSMON</h2>
<p> Some of the widgets used in <code>xpbsmon</code> and how they are manipulated are described in the following: </p>
<dl>
<dt>1.</p>
<dd> <code>listbox</code> &#8211; the ones found in this GUI are only single-selectable (one entry can be highlighted/selected at a time via a mouse click).</p>
<dt>2.</p>
<dd> <code>scrollbar</code> &#8211; usually appears either vertically or horizontally and contains 5 distinct areas that are mouse clicked to achieve different effects:</p>
<dl>
<dt>
<dd>
<dl>
<dt>top arrow</p>
<dd> Causes the view in the associated widget to shift up by one unit (i.e. the object appears to move down one unit in its window). If the button is held down the action will auto-repeat.</p>
<dt>top gap</p>
<dd> Causes the view in the associated window to shift up by one less than the number of units in the window (i.e. the portion of the object that used to appear at the very top of the window will now appear at the very bottom). If the button is held down the action will auto-repeat.</p>
<dt>slider</p>
<dd> Pressing button 1 in this area has no immediate effect except to cause the slider to appear sunken rather than raised. However, if the mouse is moved with the button down then the slider will be dragged, adjusting the view as the mouse is moved.</p>
<dt>bottom gap</p>
<dd> Causes the view in the associated window to shift down by one less than the number of units in the window (i.e. the portion of the object that used to appear at the very bottom of the window will now appear at the very top). If the button is held down the action will auto-repeat.</p>
<dt>bottom arrow</p>
<dd> Causes the view in the associated window to shift down by one unit (i.e. the object appears to move up one unit in its window). If the button is held down the action will auto-repeat.</dl>
</dl>
<dt>3.</p>
<dd> <code>entry</code> &#8211; brought into focus with a click of the left mouse button. To manipulate this widget, simply type in the text value. Use of arrow keys, mouse selection of text for deletion or overwrite, copying and pasting with sole use of mouse buttons are permitted. This widget is usually accompanied by a scrollbar for horizontally scanning a long text entry string. </p>
<dt>4.</p>
<dd> <code>box</code> &#8211; made up of 1 or more listboxes displayed adjacent to each other giving the effect of a &quot;matrix&quot;. Each row from the listboxes makes up an element of the box. In order to add items to the box, you need to manipulate the accompanying entry widgets, one for each listbox, and then clicking the <code>add</code> button. Removing items from the box is done by selecting an element, and then clicking <code>delete</code>. </p>
<dt>5.</p>
<dd> <code>spinbox</code> &#8211; a combination of an entry widget and a horizontal scrollbar. The entry widget will only accept values that fall within a defined list of valid values, and incrementing through the valid values is done by clicking on the up/down arrows.</p>
<dt>6.</p>
<dd> <code>button</code> &#8211; a rectangular region appearing either raised or pressed that invokes an action when clicked with the left mouse button. When the button appears pressed, then hitting the &lt;RETURN&gt; key will automatically select the button.</dl>
<h2>UPDATING PREFERENCES</h2>
<dl>
<dt>CASE 1: Time Sharing</p>
<dd>
<p> Suppose you have a time-sharing environment where the front-end is called bower and you have 4 nodes: bower1, bower2, bower3, bower4. bower is the host that runs the server; jobs are submitted to host bower where it enqueues it for future execution. Also, a pbs_mom daemon is running on each of the execution hosts. If the server bower also maintains a nodes list containing information like state, properties for the 4 nodes, then this will also be reported. Then to setup <code>xpbsmon</code>, do the following: </p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Click the <code>Pref..</code> button on the Menu section.</p>
<dt>2.</p>
<dd> On the Sites Preference dialog, enter any arbitrary site name, for example &quot;Local&quot;. Then click the <code>add</code> button.</p>
<dt>3.</p>
<dd> On the Server_Host entry box, enter &quot;bower&quot;, and on the DisplayLabel entry box, put an arbitrary label (as it would appear on the header of the server box) like &quot;Bower&quot;, and then click <code>add</code>.</p>
<dt>4.</p>
<dd> Click the <code>nodes..</code> button that is accompanying the Servers box. This would bring up the Server Preference dialog.</p>
<dt>5.</p>
<dd> Now add the entries &quot;bower1&quot;, &quot;bower2&quot;, &quot;bower3&quot;, &quot;bower4&quot; specifying type MOM for each on the Nodes box.</p>
<dt>6.</p>
<dd> If you need to monitor certain system resource parameters for each of the nodes, you need to specify query expressions containing resource queries to be sent to the individual PBS moms. For example, if you want to obtain memory usage, then select a node from the Nodes list, click on the <code>query..</code> button that accompanies the Nodes list, and this would bring up the Query Table dialog. Specify the following input: </p>
<dl>
<dt>
<dd> Query_Expr: (availmem/totmem) * 100<br />
 Display_Info: Memory Usage:<br />
 Display_Type: SCALE</dl>
<dt>
<dd>
<p> The above says to display the result of the &quot;Query_Expr&quot; in a scale widget calibrated over 100. The queries &quot;availmem&quot; and &quot;totmem&quot; will be sent to the PBS mom, and the expression is evaluated upon receiving all results from the mom. If you want to display the result of another query, say &quot;loadave&quot;, directly, then specify the following: </p>
<dl>
<dt>
<dd> Query_Expr: loadave<br />
 Display_Info: Load Average:<br />
 Display_Type: TEXT</dl>
<dt>
<dd>
<p> NOTE: For a list of queries that can be sent to a pbs_mom, please click on the <code>Help</code> button on the Query table window.</dl>
</dl>
<dt>CASE 2: Jobs Exclusive Environment</p>
<dd> Supposing you have a &quot;space non-sharing&quot; environment where the server maintains a list of nodes that it runs jobs on exclusively (one job at a time outstanding per node). Let&#8217;s call this server b1. Simply update Preferences information as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Click the <code>Pref..</code> button on the Menu section.</p>
<dt>2.</p>
<dd> On the Sites Preference dialog, enter a site name, for example &quot;B System&quot;. Then click the <code>add</code> button.</p>
<dt>3.</p>
<dd> On the Server_Host entry box, enter &quot;b1&quot;, DisplayLabel entry box type &quot;B1&quot; (or whatever label that you would like to appear on the header of the server box), and then click <code>add</code>. </p>
</dl>
</dl>
<dt>CASE 3: Hybrid Time Sharing/Space Sharing Environment</p>
<dd> A cluster of heterogeneous machines, time-sharing or jobs exclusive, could easily be represented in <code>xpbsmon</code> by combining steps in CASE 1 and CASE 2.</dl>
<h2>LEAVING XPBSMON</h2>
<p> Click on the <code>Close</code> button located in the Menu bar to leave <code>xpbsmon</code>. If anything had changed, it will bring up a dialog box asking for a confirmation in regards to saving preferences information about list of sites, their view types, list of servers on each site, the list of nodes known to each server, and the list of queries to be sent to the pbs_mom of each node. The information is saved in ~/.xpbsmonrc file.</p>
<h2>PREFERENCES</h2>
<p> The resources that can be set in the X resources file, ~/.xpbsmonrc, are described in the following: </p>
<p> <code>Node Box Properties</code> </p>
<p> Resource names beginning with &quot;*small&quot; or &quot;*node&quot; apply to the properties of the node boxes. A node box is made of an outer frame where the node label sits on top, the canvas (smaller box) is on the middle, and possibly some horizontal/ vertical scrollbars. </p>
<dl>
<dt>nodeColorNOINFO</p>
<dd> color of node box when information for the node it represents could not be obtained.</p>
<dt>*nodeColorFREE</p>
<dd> color of canvas when node it represents is up.</p>
<dt>*nodeColorINUSEshared</p>
<dd> color when node it represents has more than 1 job running on it, or when node has been marked by the server that manages it as &quot;job-sharing&quot;.</p>
<dt>*nodeColorINUSEexclusive</p>
<dd> list of colors to assign to a node box when host it represents is running only 1 job, or when node has been marked by the server that manages it as &quot;time-sharing&quot;. xpbsmon will use this list to assign 1 distinct color per job unless all the colors have been exhausted, in which case, colors will start getting assigned more than once in a round-robin fashion.</p>
<dt>*nodeColorDOWN</p>
<dd> color when node it represents is down.</p>
<dt>*nodeColorRSVD</p>
<dd> color when node it represents is reserved.</p>
<dt>*nodeColorOFFL</p>
<dd> color when node it represents is offline.</p>
<dt>*smallForeground</p>
<dd> applies to the color of text inside the canvas.</p>
<dt>*smallBackground</p>
<dd> applies to the color of the frame.</p>
<dt>*smallBorderWidth</p>
<dd> distance (in pixels) from other node boxes.</p>
<dt>*smallRelief</p>
<dd> how node box will visually appear (style).</p>
<dt>*smallScrollBorderWidth</p>
<dd> significant only in FULL mode, this is the distance of the horizontal/vertical scrollbars from the canvas and lower edge of the frame.</p>
<dt>*smallScrollBackground</p>
<dd> background color of the scrollbars</p>
<dt>*smallScrollRelief</p>
<dd> how scrollbars would visually appear (style).</p>
<dt>*smallCanvasBackground</p>
<dd> color of the canvas (later overridden depending on status of the node it represents)</p>
<dt>*smallCanvasBorderWidth</p>
<dd> distance of the canvas from the frame and possibly the scrollbars.</p>
<dt>*smallCanvasRelief</p>
<dd> how the canvas is visually represented (style).</p>
<dt>*smallLabelBorderWidth</p>
<dd> the distance of the node label from the canvas and the topmost edge of the frame.</p>
<dt>*smallLabelBackground</p>
<dd> the background of the area of the node label that is not filled.</p>
<dt>*smallLabelRelief</p>
<dd> how the label would appear visually (style).</p>
<dt>*smallLabelForeground</p>
<dd> the color of node label text.</p>
<dt>*smallLabelFont</p>
<dd> the font to use for the node label text.</p>
<dt>*smallLabelFontWidth</p>
<dd> font width (in pixels) of *smallLabelFont</p>
<dt>*smallLabelFontHeight</p>
<dd> font height (in pixels) of *smallLabelFont</p>
<dt>*smallTextFont</p>
<dd> font to use for the text that appear inside a canvas.</p>
<dt>*smallTextFontWidth</p>
<dd> font width (in pixels) of *smallTextFont.</p>
<dt>*smallTextFontHeight</p>
<dd> font height (in pixels) of *smallTextFont.</p>
<dt>*nodeColorTrough</p>
<dd> color of trough part (the /100 portion) of a canvas scale item.</p>
<dt>*nodeColorSlider</p>
<dd> color of slider part (value portion) of a canvas scale item.</p>
<dt>*nodeColorExtendedTrough</p>
<dd> color of extended trough (over 100 portion when value exceeds max) of a canvas scale item.</p>
<dt>*nodeScaleFactor</p>
<dd> tells how much bigger you want the scale item on the canvas to appear. (1 means to keep size as is)</p>
<dt>*nodeBoxFullMaxWidth</p>
<dd>
<dt>*nodeBoxFullMaxHeight</p>
<dd> maximum width and height (in pixels) of a node box in FULL mode.</p>
<dt>*nodeBoxIconMaxWidth</p>
<dd>
<dt>*nodeBoxIconMaxHeight</p>
<dd> maximum width and height (in pixels) of a node box in ICON mode.</p>
<dt>*nodeBoxMirrorMaxWidth</p>
<dd>
<dt>*nodeBoxMirrorMaxHeight</p>
<dd> maximum width and height (in pixels) of a node box displayed on a separate window (after it has been clicked with the mouse to obtain a bigger view)</p>
<dt>*nodeBoxMirrorScaleFactor</p>
<dd> tells how much bigger you want the scale item on the canvas to appear while the node box is displayed on a separate window (1 means to keep size as is)</dl>
<p> <code>Server Box Properties</code> </p>
<p> Resource names beginning with &quot;*medium&quot; apply to the properties of the server boxes. A server box is made of an outer frame where the server display label sits on top, a canvas filled with node boxes is on the middle, possibly some horizontal/vertical scrollbars, and a status label at the bottom.</p>
<dl>
<dt>*mediumLabelForeground</p>
<dd> color of text applied to the server display label and status label.</p>
<dt>*mediumLabelBackground</p>
<dd> background color of the unfilled portions of the server display label and status label.</p>
<dt>*mediumLabelBorderWidth</p>
<dd> distance of the server display label and status label from other parts of the server box.</p>
<dt>*mediumLabelRelief</p>
<dd> how the server display label and status label appear visually (style).</p>
<dt>*mediumLabelFont</p>
<dd> font used for the text of the server display label and status label.</p>
<dt>*mediumLabelFontWidth</p>
<dd> font width (in pixels) of *mediumLabelFont.</p>
<dt>*mediumLabelFontHeight</p>
<dd> font height (in pixels) of *mediumLabelFont.</p>
<dt>*mediumCanvasBorderWidth</p>
<dd> the distance of the server box&#8217;s canvas from the label widgets.</p>
<dt>*mediumCanvasBackground</p>
<dd> the background color of the canvas.</p>
<dt>*mediumCanvasRelief</p>
<dd> how the canvas appear visually (style).</p>
<dt>*mediumScrollBorderWidth</p>
<dd> distance of the scrollbars from the other parts of the server box.</p>
<dt>*mediumScrollBackground</p>
<dd> the background color of the scrollbars</p>
<dt>*mediumScrollRelief</p>
<dd> how the scrollbars appear visually.</p>
<dt>*mediumBackground</p>
<dd> the color of the server box frame.</p>
<dt>*mediumBorderWidth</p>
<dd> the distance of the server box from other boxes.</p>
<dt>*mediumRelief</p>
<dd> how the server box appears visually (style).</p>
<dt>*serverBoxMaxWidth</p>
<dd>
<dt>*serverBoxMaxHeight</p>
<dd> maximum width and height (in pixels) of a server box.</p>
<dt>*serverBoxMaxNumNodeBoxesPerRow</p>
<dd> maximum # of node boxes to appear in a row within a canvas.</dl>
<p> <code>Miscellaneous Properties</code> </p>
<p> Resource names beginning with &quot;*big&quot; apply to the properties of a site box, as well as to widgets found outside of the server box and node box. This includes the dialog boxes that appear when the menu buttons of the main window are manipulated. The site box is the one that appears on the main region of xpbsmon.</p>
<dl>
<dt>*bigBackground</p>
<dd> background color of the outer layer of the main window.</p>
<dt>*bigForeground</p>
<dd> color applied to regular text that appear outside of the node box and server box.</p>
<dt>*bigBorderWidth</p>
<dd> distance of the site box from the menu area and the color information area.</p>
<dt>*bigRelief</p>
<dd> how the site box is visually represented (style)</p>
<dt>*bigActiveColor</p>
<dd> the color applied to the background of a selection, a selected command button, or a selected scroll bar handle.</p>
<dt>*bigShadingColor</p>
<dd> a color shading applied to some of the frames to emphasize focus as well as decoration.</p>
<dt>*bigSelectorColor</p>
<dd> the color applied to the selector box of a radiobutton or checkbutton.</p>
<dt>*bigDisabledColor</p>
<dd> color applied to a disabled widget.</p>
<dt>*bigLabelBackground</p>
<dd> color applied to the unfilled portions of label widgets.</p>
<dt>*bigLabelBorderWidth</p>
<dd> distance from other widgets of a label widget.</p>
<dt>*bigLabelRelief</p>
<dd> how label widgets appear visually (style)</p>
<dt>*bigLabelFont</p>
<dd> font to use for labels.</p>
<dt>*bigLabelFontWidth</p>
<dd> font width (in pixels) of *bigLabelFont.</p>
<dt>*bigLabelFontHeight</p>
<dd> font height (in pixels) of *bigLabelFont.</p>
<dt>*bigLabelForeground</p>
<dd> color applied to text that function as labels.</p>
<dt>*bigCanvasBackground</p>
<dd> the color of the main region.</p>
<dt>*bigCanvasRelief</p>
<dd> how the main region looks like visually (style)</p>
<dt>*bigCanvasBorderWidth:</p>
<dd> distance of the main region from the menu and info regions.</p>
<dt>*bigScrollBorderWidth</p>
<dd> if the main region has a scrollbar, this is its distance from other widgets appearing on the region.</p>
<dt>*bigScrollBackground</p>
<dd> background color of the scrollbar appearing outside a server box and node box.</p>
<dt>*bigScrollRelief</p>
<dd> how the scrollbar that appears outside a server box and node box looks like visually (style)</p>
<dt>*bigTextFontWidth</p>
<dd> the font width (in pixels) of *bigTextFont</p>
<dt>*bigTextFontHeight</p>
<dd> the font height (in pixels) of *bigTextFont</p>
<dt>*siteBoxMaxWidth</p>
<dd> maximum width (in pixels) of the site box.</p>
<dt>*siteBoxMaxHeight</p>
<dd> maximum height (in pixels) of the site box.</p>
<dt>*siteBoxMaxNumServerBoxesPerRow</p>
<dd> maximum number of server boxes to appear in a row inside the site box.</p>
<dt>*autoUpdate</p>
<dd> if set to true, then information about nodes is periodically gathered.</p>
<dt>*autoUpdateMins</p>
<dd> the # of minutes between polling for data regarding nodes when *autoUpdate is set.</p>
<dt>*siteInView</p>
<dd> the name of the site that should be in view</p>
<dt>*rcSiteInfoDelimeterChar</p>
<dd> the separator character for each input within a curly-bracketed line of input of *siteInfo.</p>
<dt>*sitesInfo</p>
<dd> {&lt;site1name&gt;&lt;sep&gt;&lt;site1-display-type&gt;&lt;sep&gt;&lt;server-name&gt;&lt;sep&gt;&lt;server-display-label&gt;&lt;sep&gt;&lt;nodename&gt;&lt;sep&gt;&lt;nodetype&gt;&lt;sep&gt;&lt;node-query-expr&gt;} </p>
<p>&nbsp;<wbr>. . .<br />
 {&lt;site2name&gt;&lt;sep&gt;&lt;site2-display-type&gt;&lt;sep&gt;&lt;server-name&gt;&lt;sep&gt;&lt;server-display-label&gt;&lt;sep&gt;&lt;nodename&gt;&lt;sep&gt;&lt;nodetype&gt;&lt;sep&gt;&lt;node-query-expr&gt;} </p>
<p> information about a site where &lt;site1-display-type&gt; can be either {FULL,ICON}, &lt;nodetype&gt; can be {MOM, NOMOM}, and &lt;node-query-expr&gt; has the format: </p>
<p> { {&lt;expr&gt;} {expr-label} &lt;output-format&gt;} </p>
<p> where &lt;output-format&gt; could be {TEXT, SCALE}. It&#8217;s probably better to use the <code>Pref</code> dialog boxes in order to specify a value for this. </p>
<p> Example: </p>
<p> *rcSiteInfoDelimeterChar ;<br />
 *sitesInfo: {Mars;ICON;newton;Newton;newton3;NOMOM;} {Langley;FULL;db;DB;db.OpenPBS.org;MOM;&#123;&#123; ( availmem / totmem ) * 100} {Memory Usage:} SCALE} &#123;&#123; ( loadave / ncpus ) * 100} {Cpu Usage:} SCALE} {ncpus {Number of Cpus:} TEXT} {physmem {Physical Memory:} TEXT} {idletime {Idle Time (s):} TEXT} {loadave {Load Avg:} TEXT}} {Mars;ICON;newton;Newton;newton4;NOMOM;} {Mars;ICON;newton;Newton;newton1;NOMOM;} {Mars;ICON;newton;Newton;newton2;NOMOM;} {Mars;ICON;b0101;DB;aspasia.OpenPBS.org;MOM;&#123;&#123; ( availmem / totmem ) * 100} {Memory Usage:} SCALE} &#123;&#123; ( loadave / ncpus ) * 100} {Cpu Usage:} SCALE} {ncpus {Number of Cpus:} TEXT} {physmem {Physical Memory:} TEXT} {idletime {Idle Time (s):} TEXT} {loadave {Load Avg:} TEXT}} {Mars;ICON;newton;Newton;newton7;NOMOM;}</dl>
<h2>EXIT STATUS</h2>
<p> Upon successful processing, the <code>xpbsmon</code> exit status will be a value of zero. </p>
<p> If the xpbsmon command fails, the command exits with a value greater than zero. </p>
<p> If xpbsmon is querying a host running a server with an incompatible version, you may see the following messages:</p>
<dl>
<dt>
<dd>
<p> Internal error: pbsstatnode: End of File (15031) </p>
</dl>
<p> The above message can be safely ignored.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/8B-pbs_sched_tcl/">pbs_sched_tcl</a>(8B) and <a href="//www.systutorials.com/docs/linux/man/8B-pbs_mom/">pbs_mom</a>(8B). </p>
<h2>Index</h2>
