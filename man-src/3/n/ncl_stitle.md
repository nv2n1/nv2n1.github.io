---
title: "ncl_stitle(3)"
name: "ncl_stitle"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_stitle/"
---

STITLE - Creates scrolled movie or video titles. It receives all input through the argument list.

<h2>Utility</h2>

This routine is part of the Scrolled_title utility in NCAR Graphics. To see the overview man page for this utility, type &quot;man scrolled_title&quot;.

<h2>Synopsis</h2>

&nbsp;<wbr>CALL STITLE&nbsp;<wbr>(CRDS,NCDS,IYST,IYND,TMST,TMMV,TMND,MTST)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_stitle (char *crds[], int ncds, int iyst, 
 int iynd, float tmst, float tmmv, float tmnd, int mtst)

<h2>Description</h2>

<dl><dt>CRDS
<dd>(an input array, dimensioned NCDS, of type CHARACTER*n, where &quot;n&quot; is greater than or equal to 21) is the &quot;card input buffer&quot;. This array must be filled, prior to calling STITLE, either by internal manipulations or by reading n-character &quot;cards&quot;. Each element of the array CRDS represents one line on the scroll (or, sometimes, a continuation of a previous line) and contains the following:
<dl><dd><dl><dt>&bull;
<dd>Columns 1-5: MX, the X coordinate of the line of text on the scroll. This is normally a value between 1 and 1024, inclusive. Exactly how the line of text is positioned relative to the specified X coordinate depends on the value of ICNT (in columns 14-15). 

 If the value -9999 is used for MX, it indicates a continuation line: characters from columns 21 through &quot;n&quot; are just appended to the characters from the previous card to form the line of text. Any number of continuation cards may be used, but the total number of characters in a line of text must not be greater than 512. 

 Trailing blanks are omitted from each card, including those that are followed by a continuation card; thus, if there are to be blanks between the characters from one card and the characters from a continuation card, those blanks must be placed in columns 21 and following of the continuation card. 

 On a continuation card, columns 6-20 are ignored.
<dt>&bull;
<dd>Columns 6-10: MY, the Y coordinate of the line of text on the scroll. MY may range from -9999 to 99999.
<dt>&bull;
<dd>Columns 11-13: ICLR, the index of the color to be used for the line of text. If this field is blank, the default foreground color specified by the value of the internal parameter 'FGC' will be used.
<dt>&bull;
<dd>Columns 14-15: ICNT, the centering option:
<dl><dd><dl><dt>0
<dd>means &quot;start the text at MX&quot;.
<dt>1
<dd>means &quot;center the text about MX&quot;.
<dt>2
<dd>means &quot;end the text at MX&quot;.</dl></dl><dt>&bull;
<dd>Columns 16-20: SIZE, the desired size of the characters to be used in writing the line. SIZE is given as a multiplier of a default height specified by the value of the internal parameter 'PSZ', the default value of which is 21 (out of 1024). Values of SIZE from .75 to 2.5 are recommended.
<dt>&bull;
<dd>Columns 21-n: Text for this line (or for continuation of a line when MX = -9999).</dl></dl><dt>NCDS
<dd>(an input expression of type INTEGER) is the dimension of the array CRDS (i.e., the number of card images in it).
<dt>IYST
<dd>(an input expression of type INTEGER) is the Y coordinate that will be at the center of the screen when the text is first displayed.
<dt>IYND
<dd>(an input expression of type INTEGER) is the Y coordinate that will be at the center of the screen when the text is last displayed.
<dt>TMST
<dd>(an input expression of type REAL) is the time in seconds that the scroll will be stationary at IYST. One second is recommended.
<dt>TMMV
<dd>(an input expression of type REAL) is the time to move the scroll from IYST to IYND. This should be the time required to read the text aloud at slow to normal speed.
<dt>TMND
<dd>(an input expression of type REAL) is the time that the scroll will be stationary at IYND. One second is recommended.
<dt>MTST
<dd>(an input expression of type INTEGER) is a switch to indicate whether this is a &quot;real&quot; run or a &quot;practice&quot; run.
<dl><dd><dl><dt>0
<dd>means &quot;real run&quot;.
<dt>1
<dd>means &quot;practice run&quot;.</dl></dl><dd>During real runs, frames are created for the fade-in sequence (if the user has turned on fade-in by setting the internal parameter 'FIN' non-zero), the stationary sequence at the start (if TMST is non-zero), the scrolling time (if TMMV is non-zero), the stationary sequence at the end (if TMND is non-zero), and the fade-out sequence (if the user has turned on fade-out by setting the internal parameter 'FOU' non-zero). 

 During practice runs, only selected frames are created: a frame for the fade-in sequence (if fade-in is turned on), a frame for the stationary time at the start, a set of frames representing the scrolling sequence, a frame for the stationary time at the end, and a frame for the fade-out sequence (if fade-out is turned on). Each has a legend indicating either for how many seconds the frame will be shown or, if it is part of a scroll sequence, how many seconds into the scroll time it occurs; during real runs, these legends are omitted, of course. 

 Fade-in and fade-out are also affected by the values of the internal parameters 'BGF', which selects the type of fade-in/fade-out to be used for the background color, and 'FGF', which serves the same function for the foreground color. (The older parameters 'SBK' and 'SFG' may still be referenced, but their use is no longer recommended; setting 'SBK' has the effect of giving 'BGF' an appropriate value and setting 'SFG' has the effect of giving 'FGF' an apprpriate value.)</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Usage</h2>

STITLE takes input through its argument list and generates graphic output that moves a body of text up through the viewing window. This is done by outputting the appropriate number of frames required to generate a movie sequence of a duration specified by you. 

 At each frame STITLE skips plotting lines of text that are completely outside of the viewing window and clips those that are partially outside the window.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: fslfont, slex01, slex02, tstitl.

<h2>Access</h2>

To use STITLE or c_stitle, load the NCAR Graphics libraries ncarg, ncarg_gks, ncarg_c, and ncarg_c, preferably in that order.

<h2>Messages</h2>

See the scrolled_title man page for a description of all Scrolled_title error messages and/or informational messages.

<h2>See Also</h2>

Online: ftitle, scrolled_title, scrolled_title_params, slgeti, slgetr, slogap, slrset, slseti, slsetr, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
