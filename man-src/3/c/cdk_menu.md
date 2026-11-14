---
title: "cdk_menu(3)"
name: "cdk_menu"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_menu/"
description: "cdk_menu – curses menu widget"
---

<h2>NAME</h2>
<p> cdk_menu &#8211; curses menu widget</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

int activateCDKMenu(
    CDKMENU *menu,
    chtype *actions);
void destroyCDKMenu(
    CDKMENU *menu);
void drawCDKMenu(
    CDKMENU *menu,
    boolean box);
void drawCDKMenuSubwin(
    CDKMENU *menu);
void eraseCDKMenu(
    CDKMENU *menu);
void eraseCDKMenuSubwin(
    CDKMENU *menu);
void getCDKMenuCurrentItem(
    CDKMENU *menu,
    int *menuItem,
    int *submenuItem);
chtype getCDKMenuSubTitleHighlight(
    CDKMENU *menu);
chtype getCDKMenuTitleHighlight(
    CDKMENU *menu);
int injectCDKMenu(
    CDKMENU *menu,
    chtype input);
CDKMENU *newCDKMenu(
    CDKSCREEN *cdkscreen,
    const char *menulist[MAX_MENU_ITEMS][MAX_SUB_ITEMS],
    int menuListLength,
    int *submenuListLength,
    int *menuLocation,
    int menuPos,
    chtype titleAttribute,
    chtype subtitleAttribute);
void setCDKMenu(
    CDKMENU *menu,
    int menuItem,
    int submenuItem,
    chtype titleAttribute,
    chtype subtitleAttribute);
void setCDKMenuBackgroundAttrib(
    CDKMENU *menu,
    chtype attribute);
void setCDKMenuBackgroundColor(
    CDKMENU *menu,
    const char *color);
void setCDKMenuCurrentItem(
    CDKMENU *menu,
    int menuItem,
    int submenuItem);
void setCDKMenuPostProcess(
    CDKMENU *menu,
    PROCESSFN callback,
    void *data);
void setCDKMenuPreProcess(
    CDKMENU *menu,
    PROCESSFN callback,
    void *data);
void setCDKMenuSubTitleHighlight(
    CDKMENU *menu,
    chtype highlight);
void setCDKMenuTitleHighlight(
    CDKMENU *menu,
    chtype highlight);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk menu widget creates a pull-down menu list. The following are functions which create or manipulate the Cdk menu widget.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKMenu</code></p>
<dd> activates the menu widget and lets the user interact with the widget. The parameter <code>menu</code> is a pointer to a non-NULL menu widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> then this then this function returns an integer which is a value of the current menu list * 100 + the sub-menu number. It will also set the widget data <i>exitType</i> to <i>vNORMAL</i>. If the character entered into this widget was <i>ESCAPE</i> then the widget will return a value of -1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>destroyCDKMenu</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKMenu</code></p>
<dd> draws the menu widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>drawCDKMenuSubwin</code></p>
<dd> draws the menu item subwindow.</p>
<dt><code>eraseCDKMenu</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>eraseCDKMenuSubwin</code></p>
<dd> erases the menu item subwindow.</p>
<dt><code>getCDKMenuCurrentItem</code></p>
<dd> returns the values <code>menuItem</code> and <code>submenuItem</code> to the current menu selection.</p>
<dt><code>getCDKMenuSubTitleHighlight</code></p>
<dd> returns the highlight attribute of the sub-menu selection bar.</p>
<dt><code>getCDKMenuTitleHighlight</code></p>
<dd> returns the highlight attributes of the menu title.</p>
<dt><code>injectCDKMenu</code></p>
<dd> injects a single character into the widget. The parameter <code>menu</code> is a pointer to a non-NULL menu widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns the current menu list * 100 + the sub-menu number. The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns -1. to <i>vESCAPE_HIT</i>. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns -1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>newCDKMenu</code></p>
<dd> creates a menu widget and returns a pointer to it. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>screen</code></p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt><code>menuList</code></p>
<dd> is a list of the menu list titles.</p>
<dt><code>menuListLength</code></p>
<dd> is the number of pull down menus.</p>
<dt><code>submenuListLength</code></p>
<dd> is the number of menu items under each menu list.</p>
<dt><code>menuLocation</code></p>
<dd> tells where each menu is to be located. Valid values are <i>LEFT</i> and <i>RIGHT</i>.</p>
<dt><code>menuPos</code></p>
<dd> tells whether the menu is to be on the top of the screen or the bottom. Valid values are <i>TOP</i> and <i>BOTTOM</i>.</p>
<dt><code>titleAttribute</code> and</p>
<dd>
<dt><code>subtitleAttribute</code></p>
<dd> are the character attributes of the title and sub-titles respectively.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>setCDKMenu</code></p>
<dd> lets the programmer modify certain elements of an existing menu widget. The parameters <code>menuItem</code> and <code>submenuItem</code> set which menu list and sub-menu item are going to be highlighted when the widget is activated. The other parameter names correspond to the same parameter names listed in the <code>newCDKMenu</code> function.</p>
<dt><code>setCDKMenuBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKMenuBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKMenuCurrentItem</code></p>
<dd> sets the current item in the menu widget.</p>
<dt><code>setCDKMenuPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKMenuPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKMenuSubTitleHighlight</code></p>
<dd> sets the highlight attribute of the sub-menu selection bar.</p>
<dt><code>setCDKMenuTitleHighlight</code></p>
<dd> sets the highlight attributes of the menu title.</dl>
<h2>KEY BINDINGS</h2>
<p> When the widget is activated there are several default key bindings which will help the user enter or manipulate the information quickly. The following table outlines the keys and their actions for this widget. </p>
<p> <center></p>
<table BORDER>
<tr VALIGN=top>
<td><code>Key</code></td>
<td>Action
</td>
</tr>
<tr VALIGN=top>
<td>Left Arrow</td>
<td> Highlights the menu list to the left of the current menu.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td> Highlights the menu list to the right of the current menu.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td> Moves the current menu selection up one.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td> Moves the current menu selection down one.
</td>
</tr>
<tr VALIGN=top>
<td>Space</td>
<td> Moves the current menu selection down one.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Highlights the menu list to the right of the current menu.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns the index of the selected item. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns -1. This also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl-L</td>
<td>Refreshes the screen.
</td>
</tr>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
