---
title: "cdk_calendar(3)"
name: "cdk_calendar"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_calendar/"
description: "cdk_calendar – curses calendar widget."
---

<h2>NAME</h2>
<p> cdk_calendar &#8211; curses calendar widget.</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

time_t activateCDKCalendar(CDKCALENDAR *calendar,
                           chtype *actions);
void destroyCDKCalendar(
    CDKCALENDAR *calendar);
void drawCDKCalendar(CDKCALENDAR *calendar,
                     boolean box);
void eraseCDKCalendar(
    CDKCALENDAR *calendar);
boolean getCDKCalendarBox(
    CDKCALENDAR *calendar);
void getCDKCalendarDate(CDKCALENDAR *calendar,
                        int *day,
                        int *month,
                        int *year);
chtype getCDKCalendarDayAttribute(
    CDKCALENDAR *calendar);
chtype getCDKCalendarHighlight(
    CDKCALENDAR *calendar);
chtype getCDKCalendarMarker(
    CDKCALENDAR *calendar,
    int day,
    int month,
    int year);
chtype getCDKCalendarMonthAttribute(
    CDKCALENDAR *calendar);
chtype getCDKCalendarYearAttribute(
    CDKCALENDAR *calendar);
time_t injectCDKCalendar(
    CDKCALENDAR *calendar,
    chtype input);
void moveCDKCalendar(
    CDKCALENDAR *calendar,
    int xpos,
    int ypos,
    boolean relative,
    boolean refresh);
CDKCALENDAR *newCDKCalendar(CDKSCREEN *cdkscreen,
                            int xpos,
                            int ypos,
                            const char *title,
                            int day,
                            int month,
                            int year,
                            chtype dayAttrib,
                            chtype monthAttrib,
                            chtype yearAttrib,
                            chtype highlight,
                            boolean box,
                            boolean shadow);
void positionCDKCalendar(
    CDKCALENDAR *calendar);
void removeCDKCalendarMarker(
    CDKCALENDAR *calendar,
    int day,
    int month,
    int year);
void setCDKCalendar(
    CDKCALENDAR *calendar,
    int day,
    int month,
    int year,
    chtype dayAttrib,
    chtype monthAttrib,
    chtype yearAttrib,
    chtype highlight,
    boolean box);
void setCDKCalendarBackgroundAttrib(
    CDKCALENDAR *calendar,
    chtype attribute);
void setCDKCalendarBackgroundColor(
    CDKCALENDAR *calendar,
    const char *color);
void setCDKCalendarBox(
    CDKCALENDAR *calendar,
    boolean box);
setCDKCalendarBoxAttribute(
    CDKCALENDAR *calendar,
    chtype ch);
void setCDKCalendarDate(
    CDKCALENDAR *calendar,
    int day,
    int month,
    int year);
void setCDKCalendarDayAttribute(
    CDKCALENDAR *calendar,
    chtype attribute);
void setCDKCalendarDaysNames(
    CDKCALENDAR *calendar,
    const char *days);
void setCDKCalendarHighlight(
    CDKCALENDAR *calendar,
    chtype attribute);
void setCDKCalendarHorizontalChar(
    CDKCALENDAR *calendar,
    chtype ch);
void setCDKCalendarLLChar(
    CDKCALENDAR *calendar,
    chtype ch);
void setCDKCalendarLRChar(
    CDKCALENDAR *calendar,
    chtype ch);
void setCDKCalendarMarker(
    CDKCALENDAR *calendar,
    int day,
    int month,
    int year,
    chtype marker);
void setCDKCalendarMonthAttribute(
    CDKCALENDAR *calendar,
    chtype attribute);
void setCDKCalendarMonthsNames(
    CDKCALENDAR *calendar,
    CDK_CONST char **months);
void setCDKCalendarPostProcess(
    CDKCALENDAR *calendar,
    PROCESSFN callback,
    void *data);
void setCDKCalendarPreProcess(
    CDKCALENDAR *calendar,
    PROCESSFN callback,
    void *data);
setCDKCalendarULChar(
    CDKCALENDAR *calendar,
    chtype ch);
setCDKCalendarURChar(
    CDKCALENDAR *calendar,
    chtype ch);
setCDKCalendarVerticalChar(
    CDKCALENDAR *calendar,
    chtype ch);
void setCDKCalendarYearAttribute(
    CDKCALENDAR *calendar,
    chtype attribute);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The Cdk calendar widget creates a pop-up calendar. The calendar widget allows the user to traverse through months/years using the cursor keys.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>activateCDKCalendar</code></p>
<dd> activates the calendar widget and lets the user interact with the widget. The <code>calendar</code> widget is a pointer to a non-NULL calendar widget. If the <code>actions</code> parameter is passed with a non-NULL value, the characters in the array will be injected into the widget. To activate the widget interactively pass in a <i>NULL</i> pointer for <code>actions</code>. If the character entered into this widget is <i>RETURN</i> then this function will return a type of <i>time_t</i>. The <i>time_t</i> type is used in the functions defined in the time.h header file. (see <i>localtime</i> or <i>ctime</i> for more information). If the character entered into this widget was <i>ESCAPE</i> or <i>TAB</i> then this function will return a value of (time_t)-1 and the widget data <i>exitType</i> will be set to <i>vESCAPE_HIT</i>.</p>
<dt><code>destroyCDKCalendar</code></p>
<dd> removes the widget from the screen and frees memory the object used.</p>
<dt><code>drawCDKCalendar</code></p>
<dd> draws the label widget on the screen. If the <code>box</code> parameter is true, the widget is drawn with a box.</p>
<dt><code>eraseCDKCalendar</code></p>
<dd> removes the widget from the screen. This does <i>NOT</i> destroy the widget.</p>
<dt><code>getCDKCalendarBox</code></p>
<dd> returns whether the widget will be drawn with a box around it.</p>
<dt><code>getCDKCalendarDate</code></p>
<dd> returns the current date the calendar is displaying.</p>
<dt><code>getCDKCalendarDayAttribute</code></p>
<dd> returns the attribute of the day attribute of the calendar.</p>
<dt><code>getCDKCalendarHighlight</code></p>
<dd> returns the attribute of the highlight bar of the scrolling list portion of the widget.</p>
<dt><code>getCDKCalendarMarker</code></p>
<dd> returns the marker set on the calendar by <code>setCDKCalendarMarker</code>.</p>
<dt><code>getCDKCalendarMonthAttribute</code></p>
<dd> returns the attribute of the month attribute of the calendar.</p>
<dt><code>getCDKCalendarYearAttribute</code></p>
<dd> returns the attribute of the year attribute of the calendar.</p>
<dt><code>injectCDKCalendar</code></p>
<dd> injects a single character into the widget. The parameter <code>calendar</code> is a pointer to a non-NULL calendar widget. The parameter <code>character</code> is the character to inject into the widget. The return value and side-effect (setting the widget data <i>exitType</i>) depend upon the injected character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>RETURN</i> or <i>TAB</i></p>
<dd> the function returns a value of type <i>time_t</i> (see <i>localtime</i> or <i>ctime</i> for more information). The widget data <i>exitType</i> is set to <i>vNORMAL</i>.</p>
<dt><i>ESCAPE</i></p>
<dd> the function returns (time_t)-1. The widget data <i>exitType</i> is set to <i>vESCAPE_HIT</i>.</p>
<dt>Otherwise</p>
<dd> unless modified by preprocessing, postprocessing or key bindings, the function returns (time_t)-1. The widget data <i>exitType</i> is set to <i>vEARLY_EXIT</i>.</dl>
</dl>
<dt><code>moveCDKCalendar</code></p>
<dd> moves the given widget to the given position. The parameters <code>xpos</code> and <code>ypos</code> are the new position of the widget. The parameter <code>xpos</code> may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>. The parameter <code>ypos</code> may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>. The parameter <code>relative</code> states whether the <code>xpos</code>/<code>ypos</code> pair is a relative move or an absolute move. For example, if <code>xpos</code> = 1 and <code>ypos</code> = 2 and <code>relative</code> = <code>TRUE</code>, then the widget would move one row down and two columns right. If the value of <code>relative</code> was <code>FALSE</code> then the widget would move to the position (1,2). Do not use the values <i>TOP</i>, <i>BOTTOM</i>, <i>LEFT</i>, <i>RIGHT</i>, or <i>CENTER</i> when <code>relative</code> = <i>TRUE</i>. (weird things may happen). The final parameter <code>refresh</code> is a boolean value which states whether the widget will get refreshed after the move.</p>
<dt><code>newCDKCalendar</code></p>
<dd> creates a calendar widget and returns a pointer to it. Parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>screen</code></p>
<dd> is the screen you wish this widget to be placed in.</p>
<dt><code>xpos</code></p>
<dd> controls the placement of the object along the horizontal axis. It may be an integer or one of the pre-defined values <i>LEFT</i>, <i>RIGHT</i>, and <i>CENTER</i>.</p>
<dt><code>ypos</code></p>
<dd> controls the placement of the object along the vertical axis. It may be an integer or one of the pre-defined values <i>TOP</i>, <i>BOTTOM</i>, and <i>CENTER</i>.</p>
<dt><code>title</code></p>
<dd> is the string which will be displayed at the top of the widget. The title can be more than one line; just provide a carriage return character at the line break.</p>
<dt><code>year</code>,</p>
<dd>
<dt><code>month</code> and</p>
<dd>
<dt><code>day</code></p>
<dd>
 set the initial date of the calendar.</p>
<dt><code>yearAttrib</code>,</p>
<dd>
<dt><code>monthAttrib</code> and</p>
<dd>
<dt><code>dayAttrib</code></p>
<dd> represent the attributes of the year, month, and day respectively.</p>
<dt><code>highlight</code></p>
<dd> sets the highlight of the currently selected day.</p>
<dt><code>box</code></p>
<dd> is true if the widget should be drawn with a box around it.</p>
<dt><code>shadow</code></p>
<dd> turns the shadow on or off around this widget.</dl>
</dl>
<dt>
<dd> If the widget could not be created then a <i>NULL</i> pointer is returned.</p>
<dt><code>positionCDKCalendar</code></p>
<dd> allows the user to move the widget around the screen via the cursor/keypad keys. See <code>cdk_position (3)</code> for key bindings.</p>
<dt><code>removeCDKCalendarMarker</code></p>
<dd> removes a marker from the calendar.</p>
<dt><code>setCDKCalendar</code></p>
<dd> lets the programmer modify certain elements of an existing calendar widget. The <code>calendar</code> parameter represents an existing calendar pointer. The other parameter names correspond to the same parameter names listed in the <code>newCDKCalendar</code> function.</p>
<dt><code>setCDKCalendarBackgroundAttrib</code></p>
<dd> sets the background attribute of the widget. The parameter <code>attribute</code> is a curses attribute, e.g., A_BOLD.</p>
<dt><code>setCDKCalendarBackgroundColor</code></p>
<dd> sets the background color of the widget. The parameter <code>color</code> is in the format of the Cdk format strings. See <code>cdk_display (3)</code>.</p>
<dt><code>setCDKCalendarBox</code></p>
<dd> sets whether the widget will be drawn with a box around it.</p>
<dt><code>setCDKCalendarBoxAttribute</code></p>
<dd> sets the attribute of the box.</p>
<dt><code>setCDKCalendarDate</code></p>
<dd> sets the calendar to the given date. If the value of the <code>day</code>, <code>month</code>, or <code>year</code> parameters is -1 then the current day, month, or year is used to set the date.</p>
<dt><code>setCDKCalendarDayAttribute</code></p>
<dd> sets the attribute of the day in the calendar.</p>
<dt><code>setCDKCalendarDaysNames</code></p>
<dd> sets the names of the days of the week. The parameter is a string listing the 2-character abbreviations for the days. The default value is</p>
<dl>
<dt>
<dd> &quot;Su Mo Tu We Th Fr Sa&quot;</dl>
<dt>
<dd> &quot;Su&quot; (Sunday) is numbered zero internally, making it by default the first day of the week. Set the <code>weekBase</code> member of the widget to select a different day. For example, Monday would be 1, Tuesday 2, etc.</p>
<dt><code>setCDKCalendarHighlight</code></p>
<dd> sets the attribute of the highlight bar of the scrolling list portion of the widget.</p>
<dt><code>setCDKCalendarHorizontalChar</code></p>
<dd> sets the horizontal drawing character for the box to the given character.</p>
<dt><code>setCDKCalendarLLChar</code></p>
<dd> sets the lower left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKCalendarLRChar</code></p>
<dd> sets the lower right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKCalendarMarker</code></p>
<dd> allows the user to set a marker which will be displayed when the month is drawn. The <code>marker</code> parameter is the attribute to use when drawing the marker. If more than one marker is set on a single day, then the day will blink with the original marker attribute.</p>
<dt><code>setCDKCalendarMonthAttribute</code></p>
<dd> sets the attribute of the month in the calendar.</p>
<dt><code>setCDKCalendarMonthsNames</code></p>
<dd> sets the names of the months of the year. The parameter is a 13-element array (since indexing starts with 1). The default values are the English month names, e.g., &quot;January&quot;.</p>
<dt><code>setCDKCalendarPostProcess</code></p>
<dd> allows the user to have the widget call a function after the key has been applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about post-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKCalendarPreProcess</code></p>
<dd> allows the user to have the widget call a function after a key is hit and before the key is applied to the widget. The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. To learn more about pre-processing see <i>cdk_process (3)</i>.</p>
<dt><code>setCDKCalendarULChar</code></p>
<dd> sets the upper left hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKCalendarURChar</code></p>
<dd> sets the upper right hand corner of the widget&#8217;s box to the given character.</p>
<dt><code>setCDKCalendarVerticalChar</code></p>
<dd> sets the vertical drawing character for the box to the given character.</p>
<dt><code>setCDKCalendarYearAttribute</code></p>
<dd> sets the attribute of the year in the calendar.</dl>
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
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Left Arrow</td>
<td>Moves the cursor to the previous day.
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td>Moves the cursor to the next day.
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td>Moves the cursor to the next week.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td>Moves the cursor to the previous week.
</td>
</tr>
<tr VALIGN=top>
<td>t</td>
<td>Sets the calendar to the current date.
</td>
</tr>
<tr VALIGN=top>
<td>T</td>
<td>Sets the calendar to the current date.
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>Advances the calendar one month ahead.
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>Advances the calendar six months ahead.
</td>
</tr>
<tr VALIGN=top>
<td>p</td>
<td>Advances the calendar one month back.
</td>
</tr>
<tr VALIGN=top>
<td>P</td>
<td>Advances the calendar six months back.
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>Advances the calendar one year ahead.
</td>
</tr>
<tr VALIGN=top>
<td>+</td>
<td>Advances the calendar one year back.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the widget and returns a value of <i>time_t</i> which represents the day selected at 1 second after midnight. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td> Exits the widget and returns a value of <i>time_t</i> which represents the day selected at 1 second after midnight. This also sets the widget data <i>exitType</i> to <i>vNORMAL</i>.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td> Exits the widget and returns (time_)-1. This also sets the widget data <i>exitType</i> to <i>vESCAPE_HIT</i>.
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
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_position/">cdk_position</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
