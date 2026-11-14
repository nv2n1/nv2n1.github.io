---
title: "mathspic(1)"
name: "mathspic"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mathspic/"
description: "mathsPIC"
---

<h2 class="name">NAME</h2>
<p> <code>mathsPIC</code> </p>
<h2>AUTHORS</h2>
<p> A. Syropoulos and R.W.D. Nickalls (April 26, 2010) </p>
<p>&nbsp;asyropoulos[at]&lt;yahoo&gt;&lt;com&gt;&nbsp;<br />
&nbsp;dick[at]&lt;nickalls&gt;&lt;org&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>mathsPIC</code> is a Perl filter program for PiCTeX. mathsPIC has its own macro and macro library capability, and allows use of mathsPIC, PiCTeX, TeX and LaTeX commands. A significant feature of mathsPIC is that it allows access to the command-line, and so allows the user to extend mathsPIC commands by calling Perl and other programs written to perform particular drawing actions. See the package manual for full details and examples. The latest version can be downloaded from </p>
<p> CTAN: tex-archive/graphics/pictex/mathspic/perl </p>
<p> Commands which can be used in the mathsPIC script file fall into four main groups (a) mathsPIC macro commands (prefixed with %def), (b) regular mathsPIC commands (do not have a backslash), (c) regular PiCTeX commands (all have a backslash), and (d) regular TeX and LaTeX commands (all have a backslash). </p>
<p> The following mathematics functions can used (note that decimal fractions having an absolute value less than 1 must have a leading zero). Note also that all the trignometric functions require their argument in radians. </p>
<p> Trigonometric: sin(), cos(), tan(), asin(), acos(), atan() </p>
<p> Remainder: rem(); eg var r=12 <a href="/docs/linux/man/5-rem/">rem</a>(5) </p>
<p> Integer: int(); eg var r= int(3.87) &#8211;&gt; 3 </p>
<p> Sign (returns -1, 0, +1): sgn(); eg var s=sgn(-3.27) &#8211;&gt; -1 </p>
<p> Square root: sqrt(); eg var s = sqrt(14) </p>
<p> Exponentiation: **; eg var j = r**2 </p>
<p> Pi constant (3.14159&#8230;): _Pi_ and _pi_ </p>
<p> e constant (2.71828&#8230;): _E_ and _e_ </p>
<p> Linethickness: _linethickness_ ; eg var t = _linethickness_ </p>
<h2>COMMAND-LINE USE</h2>
<p> perl mathspic.pl [-b] [-c] [-h] [-o &lt;outfile&gt;] &lt;infile&gt; </p>
<p> <code>-b</code> enables beep if mathsPIC detects an error </p>
<p> <code>-c</code> disables the writing of comments to output file </p>
<p> <code>-h</code> displays the help file </p>
<p> <code>-o</code> defines the output file name</p>
<h2>MACRO COMMANDS</h2>
<p> macro definition commands are prefixed with %def and can take either 0, 1, or more parameters. Macros will generally be used as part of a <code>var</code> command as shown below. Macros are deleted using the <code>%undef</code> command. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;%def MACRONAME(parameters)&lt;macrodefinition&gt;<br />
&nbsp;%undef MACRONAME(parameters) </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;Notes:&nbsp;(a)&nbsp;the&nbsp;()&nbsp;must be used in the definition even if no parameters are used,&nbsp;(b)&nbsp;the name can be any combination of upper and lower case characters and numbers,&nbsp;(c)&nbsp;when the macro is used in a command it is prefixed by a&nbsp;&amp;&nbsp;symbol,&nbsp;(d)&nbsp;it is a good idea to always place a&nbsp;%&nbsp;symbol at the end of the definition,&nbsp;(e)&nbsp;comments&nbsp;(prefixed by a&nbsp;%&nbsp;symbol)&nbsp;can be placed after the macro definition just as in TeX or LaTeX. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;%def d2r()_pi_/180%&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;degrees2radians<br />
&nbsp;%def AreaOfRectangle(x,y)x*y%&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;width x, length y<br />
&nbsp;%undef d2r()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;delete the macro </p>
<p>&nbsp;&#8212;&#8211;use:<br />
&nbsp;var j2=&nbsp;6*(&amp;d2r(45)&nbsp;+&nbsp;23)<br />
&nbsp;var a3&nbsp;=&nbsp;3*&amp;AreaOfRectangle(5,7)</p>
<h2>GENERAL COMMANDS</h2>
<p> <code>NUMERICAL EXPRESSIONS</code><br />
&nbsp;When dealing with commands we will refer frequently to the term&nbsp;`numerical expression&#8217;&nbsp;by which is meant either&nbsp;(a)&nbsp;a number&nbsp;(integer or decimal),&nbsp;(b)&nbsp;a numeric variable or constant&nbsp;(defined using the var or const command),&nbsp;(c)&nbsp;any mathsPIC function, macro, or mathematical expression which evaluates to a number, or&nbsp;(d)&nbsp;a pair of point names&nbsp;(e.g. AB)&nbsp;representing the Pythagorean distance between the two points. A leading zero must be used&nbsp;<wbr>&nbsp;with decimal fractions less than one. </p>
<p>&nbsp;In general, if a command&#8217;s argument accepts a number then it will also accept a&nbsp;`numerical expression&#8217;&nbsp;(&lt;expr&gt;)&nbsp;as defined above. Sometimes a following&nbsp;&lt;unit&gt;&nbsp;is associated with the number or numerical expression, in which case the number or numerical expression can be delimited by a round bracket&nbsp;(or separated from the unit by a&nbsp;&lt;space&gt;), as shown in the following examples. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;ArrowShape(3mm, 20,40)<br />
&nbsp;var h=4<br />
&nbsp;ArrowShape(h mm, 20, 40)<br />
&nbsp;ArrowShape((2*h)mm,20,40) </p>
<p> <code>BACKSLASH</code> \<br />
&nbsp;A leading backslash without a following space indicates that it is part of a PiCTeX, TeX or LaTeX command, in&nbsp;<wbr>&nbsp;which case mathsPIC simply copies the whole line verbatim into the output file. A leading backslash followed by one or more spaces makes mathsPIC copy the whole line verbatim into the output file but without the backslash. </p>
<p> <code>USING THE COLOR PACKAGE</code><br />
&nbsp;The standard COLOR package can be used with mathsPIC, but note that it is important to load the COLOR package&nbsp;<wbr>&nbsp;after the mathsPIC package. </p>
<p>&nbsp;<wbr>&nbsp;It is best to place a comment symbol&nbsp;%&nbsp;at the end of LaTeX and TeX commands to limit white space at the end. </p>
<p>&nbsp;In the event of any colour-spill from a diagram into any following text&nbsp;(this used to be a problem in early TeX implementations)&nbsp;consider using the&nbsp;
ormalcolor&nbsp;<wbr>&nbsp;command as a delimiter within the&nbsp;eginpicture&#8230;ndpicture environment. </p>
<p> ============================== </p>
<p> <code>ARROWSHAPE</code><br />
&nbsp;This command defines the shape of an arrowhead, and allows different arrowheads to be customised. </p>
<p> The default arrow shape is equivalent to the Arrowshape(2mm,30,40) command. This default arrowhead shape can be reset using the Arrowshape(default) command, as shown in the following example. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;arrowshape(&lt;length&gt;[units],&nbsp;&lt;angledeg&gt;,&nbsp;&lt;angledeg&gt;) </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;Arrowshape(4mm,30,60)<br />
&nbsp;drawArrow(AB)<br />
&nbsp;Arrowshape(default) </p>
<p> ============================== </p>
<p> <code>beginLOOP&#8230;endLOOP</code><br />
&nbsp;This is an environment which cycles a block of code a specified number of times. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;beginLoop&nbsp;&lt;expr&gt;<br />
&nbsp;&#8230;<br />
&nbsp;endLoop </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;The block of code which lies within the environment is input&nbsp;&lt;expr&gt;&nbsp;times. </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;beginLoop 5<br />
&nbsp;&#8230;<br />
&nbsp;endLoop </p>
<p> ============================== </p>
<p> <code>beginSKIP&#8230;endSKIP</code><br />
&nbsp;This is an&nbsp;`environment&#8217;&nbsp;within which commands are not actioned. It is useful in development for testing isolated commands and excluding other commands.&nbsp; </p>
<p> ============================== </p>
<p> <code>CONST</code><br />
&nbsp;The const command is used to define&nbsp;<wbr>&nbsp;scalar&nbsp;<wbr>&nbsp;constants. Note that a constant-name must begin with a single letter&nbsp;(either upper or lower case), and may have up to a maximum of three following digits. Note that constants, variables and points have the same name structure, and a constant could have the same name as a point&nbsp;(and so we suggest points have uppercase letters and variables and constants&nbsp;<wbr>&nbsp;have lowercase letters). The scalar argument can be&nbsp;<wbr>&nbsp;any numeric expression. New values cannot&nbsp;<wbr>&nbsp;be re-allocated to existing constant-names. If this occurs mathsPIC will issue an error message. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;const name&nbsp;=&nbsp;&lt;expr&gt; </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;const r&nbsp;=&nbsp;20, r4&nbsp;=&nbsp;r3*tan(0.3) </p>
<p> ============================== </p>
<p> <code>DashArray</code><br />
&nbsp;The dasharray command takes an arbitrary number of paired arguments that are used to specify a dash pattern. </p>
<p>&nbsp;&#8212;&#8211;syntax<br />
&nbsp;dasharray(d1 , g1 , d2 , g2 , &#8230;&nbsp;) </p>
<p>&nbsp;&#8212;&#8211;notes<br />
&nbsp;The ds denotes the length of a dash and the gs denotes the length of the gap between two consecutive dashes. There must be an even number of arguments. If a variable or expression is used then it should be separated from the unit either by a&nbsp;&lt;space&gt;&nbsp;or with round brackets&nbsp;(&nbsp;)&nbsp;as shown below. </p>
<p>&nbsp;&#8212;&#8211;example<br />
&nbsp;dasharray(6pt, 2pt, 1pt, 2pt)<br />
&nbsp;var d=2<br />
&nbsp;dasharray(6pt, 2pt, 1pt, d pt)<br />
&nbsp;dasharray(6pt, 2pt, 1pt,&nbsp;(d)pt)<br />
&nbsp;dasharray(6pt, 2pt, 1pt,&nbsp;(3*d)pt) </p>
<p> ============================== </p>
<p> <code>DrawAngleArc</code><br />
&nbsp;This command draws an arc in the specified angle, a distance&nbsp;&lt;radius&gt;&nbsp;from the angle. The angle is either&nbsp;&lt;internal&gt;&nbsp;(less than 180 deg)&nbsp;or&nbsp;&lt;external&gt;&nbsp;(greater than 180 deg). The direction of the arc is either&nbsp;&lt;clockwise&gt;&nbsp;or&nbsp;&lt;anticlockwise&gt;, and this direction must correspond with the letter sequence specified for the angle. Strange and unexpected results will be produced if the four parameters are not internally consistent. The option order angle/radius/internal or external/clockwise or anticlockwise is important. The &lt;radius&gt; parameter can be any numerical expression. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawAngleArc{angle(), radius(), external, clockwise} </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;DrawAngleArc{angle(ABC),&nbsp;<a href="/docs/linux/man/3-radius/">radius</a>(3), external, clockwise}<br />
&nbsp;var r=3<br />
&nbsp;DrawAngleArc{angle(ABC), radius(r), external, clockwise} </p>
<p> ============================== </p>
<p> <code>DrawAngleArrow</code><br />
&nbsp;This command draws a curved arrow in the specified angle, a distance&nbsp;&lt;radius&gt;&nbsp;from the angle. The angle is either&nbsp;&lt;internal&gt;&nbsp;(less than 180 deg)&nbsp;or&nbsp;&lt;external&gt;&nbsp;(greater than 180 deg). The direction of the arrow is either&nbsp;&lt;clockwise&gt;&nbsp;or&nbsp;&lt;anticlockwise&gt;, and this direction must correspond with the letter sequence specified for the angle. Strange and unexpected results will be produced if the four parameters are not internally consistent. The option order angle/radius/internal/clockwise is important. The &lt;radius&gt; parameter can be any numerical expression. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawAngleArrow{angle(), radius(), external, clockwise} </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;DrawAngleArrow{angle(ABC),&nbsp;<a href="/docs/linux/man/3-radius/">radius</a>(3), external, clockwise}<br />
&nbsp;var r=3<br />
&nbsp;DrawAngleArrow{angle(ABC), radius(r), external, clockwise} </p>
<p> ============================== </p>
<p> <code>DrawArrow</code><br />
&nbsp;This command draws an arrow(s)&nbsp;joining two points. The direction of the arrow is in the point order specified. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;drawArrow(&lt;line&gt;&nbsp;[,&lt;line&gt;]&nbsp;&#8230;&nbsp;) </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;The length option can only refer to one arrow </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;drawArrow(AB)<br />
&nbsp;drawArrow(FG, HJ) </p>
<p> ============================== </p>
<p> <code>DrawCircle</code><br />
&nbsp;This command draws a circle defined by its radius and the point-name of its centre. The&nbsp;&lt;radius&gt;&nbsp;can be any numerical expression. If the units of the X and Y axes are different, circles may be drawn strangely, and mathsPIC therefore generates a warning message to this effect. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawCircle(&lt;center&gt;,&nbsp;&lt;radius&gt;) </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;drawCircle(C2,5)<br />
&nbsp;drawCircle(C2,r2)<br />
&nbsp;drawCircle(C2,r2/tan(1.3))<br />
&nbsp;drawCircle(C2,AB) </p>
<p> ============================== </p>
<p> <code>DrawCircumcircle</code><br />
&nbsp;This command draws the circumcircle of a triangle. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawCircumcircle(&lt;triangle&gt;) </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;drawCircumcircle(ABC) </p>
<p> ============================== </p>
<p> <code>DrawCurve</code><br />
&nbsp;This command draws a smooth quadratic curve through three points in the point order specified. Note that curves drawn using this command do not break to avoid line-free zones associated with the points. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawCurve(&lt;point&gt;&lt;point&gt;&lt;point&gt;) </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;drawCurve(ABC) </p>
<p> ============================== </p>
<p> <code>DrawExcircle</code><br />
&nbsp;This command draws the excircle touching one side of a triangle. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawExcircle(&lt;triangle&gt;,&nbsp;&lt;side&gt;) </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;drawExcircle(ABC, BC) </p>
<p> ============================== </p>
<p> <code>DrawIncircle</code><br />
&nbsp;This command draws the incircle of a triangle. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawIncircle(&lt;triangle&gt;) </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;drawIncircle(ABC) </p>
<p> ============================== </p>
<p> <code>DrawLine</code><br />
&nbsp;This command draws a line joining two or more points. Use the Linethickness command to vary thickness. This command uses the PiCTeX&nbsp;\putrule command for horizontal and vertical lines, and the&nbsp;\plot command for all other orientations. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawLine(&nbsp;&lt;points&gt;&nbsp;[,&nbsp;&lt;points&gt;]&nbsp;) </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;&lt;points&gt;&nbsp;is any sequence of two or more point names.<br />
&nbsp;&lt;expr&gt;&nbsp;is any numerical expression.<br />
&nbsp;Lines are drawn in the order specified.<br />
&nbsp;Lines are separated by a comma. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;drawline(AB)<br />
&nbsp;drawline(BCDE)<br />
&nbsp;drawline(FG, HJK, PQRST) </p>
<p> ============================== </p>
<p> <code>DrawPerpendicular</code><br />
&nbsp;This command draws the perpendicular from a point to a line. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawPerpendicular(&lt;point&gt;,&nbsp;&lt;line) </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;drawPerpendicular(P,AB) </p>
<p> ============================== </p>
<p> <code>DrawPoint</code><br />
&nbsp;This command draws the point-symbol at the&nbsp;<wbr>&nbsp;point-location. Commas must not be used to separate point names. The default point-symbol is&nbsp;ullet, unless an optional point-symbol&nbsp;(or string of characters)&nbsp;is specified in the associated point command. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawPoint(&lt;point&gt;&nbsp;[&lt;point&gt;&nbsp;..]) </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;drawpoint(T4)<br />
&nbsp;drawpoint(ABCDEF)<br />
&nbsp;drawpoint(P1 P2 P3 P4) </p>
<p> ============================== </p>
<p> <code>DrawRightangle</code><br />
&nbsp;This command draws the standard right-angle symbol in the internal angle specified at the size specified by&nbsp;&lt;expr&gt;. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawRightangle(&lt;angle&gt;,&nbsp;&lt;expr&gt;) </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;The&nbsp;&lt;expr&gt;&nbsp;can be any numerical expression. </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;drawRightangle(ABC,3)<br />
&nbsp;drawRightangle(ABC,PQ)<br />
&nbsp;var d=5<br />
&nbsp;drawRightangle(ABC,d) </p>
<p> ============================== </p>
<p> <code>DrawSquare</code><br />
&nbsp;This command draws a square defined by its side and the point-name of its centre. The&nbsp;&lt;sidelength&gt;&nbsp;can be any numerical expression. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;DrawSquare(&lt;centerpoint&gt;,&nbsp;&lt;sidelength&gt;) </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;drawSquare(P,5)<br />
&nbsp;var s2=3, j=2<br />
&nbsp;drawSquare(P,s2)<br />
&nbsp;drawSquare(P, s2*4/(3*j))<br />
&nbsp;drawSquare(P,AB) </p>
<p> ============================== </p>
<p> <code>DrawThickArrow</code><br />
&nbsp;This command draws a thick arrow(s)&nbsp;joining two points. The direction of the arrow is in the point order specified. The shape of the arrowhead is controlled by the ArrowShape command. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;drawThickArrow(&lt;line&gt;&nbsp;[,&lt;line&gt;,&#8230;]) </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;drawThickarrow(BC)<br />
&nbsp;drawThickarrow(PQ, RS) </p>
<p> ============================== </p>
<p> <code>DrawThickLine</code><br />
&nbsp;This command draws a thick line(s)&nbsp;joining two points. The direction of the line is in the point order specified. Use the Linethickness command to vary thickness of a line. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;drawThickLine(&lt;line&gt;&nbsp;[,&lt;line&gt;,&#8230;]) </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;drawThickline(BC)<br />
&nbsp;drawThickline(PQ, RS) </p>
<p> ============================== </p>
<p> <code>InputFile</code><br />
&nbsp;This command inputs a plain text file containing mathsPIC commands. Optionally, the file can be input several times, in which case this command functions like a DO&#8211;LOOP. The &lt;loopnumber&gt; can be any numerical expression. If the &lt;loopnumber&gt; is not an integer then mathsPIC will round the value down to the nearest integer. See also the beginLOOP &#8230; endLOOP commands. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;inputFile[*](&lt;filename&gt;)[&lt;loopnumber&gt;] </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;The inputfile*&nbsp;command is used to input a file in verbatim, i.e. a file with no mathsPIC commands, for example, a file containing only PiCTeX commands or data-points for plotting etc. Note that the inputfile* command has no &lt;loopnumber&gt; option. Note also that PiCTeX requires a ODD number of points. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;inputFile(myfile.dat)[4]<br />
&nbsp;inputFile*(mycurvedata.dat) </p>
<p> ============================== </p>
<p> <code>LineThickness</code><br />
&nbsp;This command sets a particular linethickness. The command linethickness(default)&nbsp;restores the working linethickness to the default value of 0.4pt. The current value of the linethickness (in current units) can be accessed using the var command (this can be useful when drawing figures using thick lines) . </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;LineThickness(&lt;expr&gt;&lt;units&gt;)<br />
&nbsp;LineThickness(default)<br />
&nbsp;var t&nbsp;=&nbsp;_linethickness_ </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;This command also sets the font to cmr and plotsymbol to&nbsp;\CM . and also sets the rule thickness for drawing horizontal and vertical lines. It is important to include a leading zero with decimal fractions less than one. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;linethickness(2pt)<br />
&nbsp;var t=3<br />
&nbsp;linethickness((t)pt)<br />
&nbsp;lineThickness((2*t)pt)<br />
&nbsp;linethickness(default)<br />
&nbsp;var t&nbsp;=&nbsp;_linethickness_ </p>
<p>&nbsp;&#8212;&#8211;caution:<br />
&nbsp;Note that there is a similar PiCTeX&nbsp;<wbr>&nbsp;command&nbsp;<wbr>&nbsp;with the same name&nbsp;(but with a different syntax). </p>
<p> ============================== </p>
<p> <code>PAPER</code><br />
&nbsp;Defines the plotting area in terms of the options units(), xrange(), yrange(), axes(), and ticks(). The units()&nbsp;argument must contain a numeric value and a valid TeX length unit&nbsp;<wbr>&nbsp;mm, cm, pt, pc(pica), in(inch), bp(big point), dd(didot), cc(cicero), sp(scaled point). The X and Y axes can have different units&nbsp;(see second example below). The axes()&nbsp;arguments XYTBLR refer to the X and Y axes, and&nbsp;<wbr>&nbsp;the Top, Bottom, Left and Right axes. A&nbsp;*&nbsp;following one of the axes disables ticks on that axis. The X and Y axes pass through the zeros. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;paper{units(1cm),xrange(0,10),yrange(0,10)}<br />
&nbsp;paper{units(2cm,1cm),xrange(0,10),yrange(0,10),axes(LB)}<br />
&nbsp;paper{units(1mm),xrange(0,100),yrange(0,100),axes(XY)}<br />
&nbsp;paper{units(1cm),xrange(-5,5),yrange(-5,5),axes(LRTBXY),ticks(1,1)}<br />
&nbsp;paper{units(1cm),xrange(-5,5),yrange(-5,5),axes(LRT*B*)} </p>
<p> ============================== </p>
<p> <code>POINT</code><br />
&nbsp;Defines a new point by allocating coordinates to a new point name. The&nbsp;*&nbsp;option re-allocates coordinates to an existing point name. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;POINT[*](&lt;name&gt;){&lt;point&gt;}[symbol=&lt;chars&gt;, radius=&lt;expr&gt;]<br />
&nbsp;POINT[*](&lt;name&gt;){&lt;location&gt;}[symbol=&lt;chars&gt;, radius=&lt;expr&gt;] </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;&lt;name&gt;&nbsp;one leading letter plus maximum of three trailing digits<br />
&nbsp;&lt;chars&gt;&nbsp;any TeX string allowed in an&nbsp;\hbox{}<br />
&nbsp;&lt;expr&gt;&nbsp;any numerical expression<br />
&nbsp;The polar(r,theta)&nbsp;option&nbsp;<wbr>&nbsp;defaults to radians for the angle theta. To work in degrees then must append&nbsp;&lt;deg&gt;&nbsp;eg: polar(r,theta deg). Can use&nbsp;<wbr>&nbsp;&lt;direction()&gt;&nbsp;and&nbsp;&lt;directiondeg()&gt;&nbsp;to replace theta. Note that the term&nbsp;<wbr>&nbsp;vector(AB)&nbsp;means use same&nbsp;(r, theta)&nbsp;as AB. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;point(A){5,5}<br />
&nbsp;point(B2){22,46}[symbol=$\odot$]<br />
&nbsp;point(B2){22,46}[symbol=<a href="/docs/linux/man/2-circle/">circle</a>(2),radius=5]<br />
&nbsp;var r=3<br />
&nbsp;point(B2){22,46}[symbol=<a href="/docs/linux/man/3-square/">square</a>(3),radius=r]<br />
&nbsp;point(B123){22,46}[radius=5]<br />
&nbsp;point(D2){B2, shift(5,5)}<br />
&nbsp;var s&nbsp;=&nbsp;3<br />
&nbsp;point(D2){B2, shift(2*s,4*s)}<br />
&nbsp;point(D3){D2, polar(6,32 deg)}<br />
&nbsp;point(D4){D2, polar(6,1.2 rad)}<br />
&nbsp;point(D4){D2, polar(6, direction(AB))}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%%&nbsp;radians by default<br />
&nbsp;point(D4){D2, polar(6, directiondeg(AB)&nbsp;deg)}<br />
&nbsp;point(G2){Q, rotate(P, 23 deg)}<br />
&nbsp;point(G2){Q, vector(AB)}<br />
&nbsp;point(D2){intersection(AB,CD)}<br />
&nbsp;point(F){PointOnLine(AB,5.3)}<br />
&nbsp;point(G){perpendicular(P,AB)}<br />
&nbsp;point(H){circumcircleCenter(ABC)}<br />
&nbsp;point(J){incircleCenter(ABC)}<br />
&nbsp;point(K){excircleCenter(ABC,BC)}<br />
&nbsp;point*(A){6,3}<br />
&nbsp;point*(P){Q}<br />
&nbsp;point*(B){B, shift(5,0)}<br />
&nbsp;point*(P){xcoord(J),ycoord(K)} </p>
<p> ============================== </p>
<p> <code>PointSymbol</code><br />
&nbsp;This command allows the default point-symbol&nbsp;ullet&nbsp;(with zero line-free radius)&nbsp;to be changed. The PointSymbol command is particularly useful where a set of points uses the same point-symbol, for example, when drawing graphs. The point-symbol can be reset to the default&nbsp;ullet&nbsp;<wbr>&nbsp;using the command PointSymbol(default). </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;PointSymbol(&lt;symbol&gt;,&nbsp;&lt;line-free-radius&gt;)<br />
&nbsp;PointSymbol(default) </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;The PointSymbol command only influences subsequent point commands.<br />
&nbsp;The optional square bracket of the point command overrides the PointSymbol command. </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;PointSymbol($\odot$, 0.7)<br />
&nbsp;PointSymbol(default) </p>
<p> ============================== </p>
<p> <code>SYSTEM</code><br />
&nbsp;This command allows the user to access the command line and execute standard Linux commands. A important use for this command is to run a Perl program. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;System(&quot;&lt;command&gt;&quot;) </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;The&nbsp;&lt;command&gt;&nbsp;string must be in inverted commas. </p>
<p>&nbsp;&#8212;&#8211;example:<br />
&nbsp;system(&quot;dir&nbsp;&gt;&nbsp;mydir-listing.txt&quot;)<br />
&nbsp;system(&quot;perl myperlprogram.pl&quot;) </p>
<p> ============================== </p>
<p> <code>SHOW&#8230;.</code><br />
&nbsp;This command makes mathsPIC return the value of a calculation or specified parameter;&nbsp;for example, the value of a particular angle, or the length of a line. The result is shown in the output-file as a commented line. This allows mathsPIC commands to be adjusted in the light of&nbsp;<wbr>&nbsp;calculations. There are currently five such commands as follows. </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;showLength(AB)<br />
&nbsp;showAngle(ABC)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;returns angle in radians<br />
&nbsp;showAngledeg(ABC)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;returns angle in degrees<br />
&nbsp;showArea(ABC)<br />
&nbsp;showPoints<br />
&nbsp;showVariables </p>
<p> ============================== </p>
<p> <code>TEXT</code><br />
&nbsp;This command places a text-string at a specific location. By default the text is centered vertically and horizontally at the specified point. Optionally, text can be placed relative to a point using appropriate combinations of the PiCTeX&nbsp;<wbr>&nbsp;`position&#8217;&nbsp;options l t r B b to align the&nbsp;(l)eft edge,&nbsp;(r)ight edge,&nbsp;(t)op edge,&nbsp;(B)aseline,&nbsp;(b)ottom edge respectively of the text box with the point-location. </p>
<p>&nbsp;Remember that the default units for the angle argument of the polar()&nbsp;expression is radians;&nbsp;hence you MUST append&nbsp;`deg&#8217;&nbsp;if you want to work in degrees </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;text(&lt;string&gt;){&lt;location&gt;}[&lt;position options&gt;]<br />
&nbsp;text(&lt;string&gt;){&lt;pointname&gt;, shift(&lt;x&gt;,&lt;y&gt;)}[]<br />
&nbsp;text(&lt;string&gt;){&lt;pointname&gt;, polar(&lt;r&gt;,&lt;angle&gt;[rad])}[] </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;text(A){5,6}<br />
&nbsp;text($A_1$){A1, shift(2, 2)}<br />
&nbsp;text(Z2){Z2, shift(5, -5)}[tr]<br />
&nbsp;text(Z3){Z2, polar(5, 20 deg)}[Br]<br />
&nbsp;text(Z4){Z2, polar(5, 1.34 rad)}<br />
&nbsp;text(ramebox{Z5}){Z5} </p>
<p> ============================== </p>
<p> <code>VAR</code><br />
&nbsp;The var command is used to define scalar variables. It can be any numerical expression. A variable-name must begin with a single letter&nbsp;(either upper or lower case), and may have up to a maximum of four following digits. If a more detailed variable name is required, then a simple alternative is to use a mathsPIC macro&#8212;as any string can be allocated via macros&nbsp;(see the beginning of this chapter for details on macros). </p>
<p>&nbsp;<wbr>&nbsp;Note that variables, constants and points have the same name structure, and a variable can have the same name as a point&nbsp;(and so we suggest points have uppercase letters and variables and constants have lowercase letters). New values can be re-allocated to existing variable-names;&nbsp;however, when this occurs then mathsPIC does not issue a warning message to hightlight this fact. </p>
<p>&nbsp;If it is important to be warned if a potential variable is accidentally reallocated then one should consider using the const command instead&nbsp;(since mathsPIC does generate an error message if a constant is reallocated). </p>
<p>&nbsp;&#8212;&#8211;syntax:<br />
&nbsp;var&nbsp;<wbr>&nbsp;&lt;name&gt;&nbsp;=&nbsp;&lt;expr&gt; </p>
<p>&nbsp;&#8212;&#8211;notes:<br />
&nbsp;In addition to the mathematical functions mathsPIC functions which can be used with the var command are: </p>
<p>&nbsp;angle(&lt;three-points&gt;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;returns angle in radians<br />
&nbsp;angledeg(&lt;three-points&gt;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;returns angle in degrees<br />
&nbsp;area(&lt;three-points&gt;)<br />
&nbsp;xcoord(&lt;point&gt;)<br />
&nbsp;ycoord(&lt;point&gt;)<br />
&nbsp;direction(&lt;two-points&gt;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;returns angular direction in radians<br />
&nbsp;directiondeg(&lt;two-points&gt;)&nbsp;<wbr>&nbsp;%&nbsp;returns angular direction in degrees </p>
<p>&nbsp;&#8212;&#8211;examples:<br />
&nbsp;var r&nbsp;=&nbsp;20, r4&nbsp;=&nbsp;r3*tan(0.3), j&nbsp;=&nbsp;(r*2e3)**2,&nbsp;<wbr>&nbsp;r5&nbsp;=&nbsp;AB<br />
&nbsp;var e&nbsp;=&nbsp;_e_, p1&nbsp;=&nbsp;_Pi_<br />
&nbsp;var t&nbsp;=&nbsp;_linethickness_&nbsp;<wbr>&nbsp;%&nbsp;returns linethickness in current units<br />
&nbsp;var g137&nbsp;=&nbsp;angle(ABC)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%(default: returns in radians)<br />
&nbsp;var g&nbsp;=&nbsp;angledeg(ABC)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;angle in degrees<br />
&nbsp;var h&nbsp;=&nbsp;area(ABC)<br />
&nbsp;var x2&nbsp;=&nbsp;xcoord(A), y2&nbsp;=&nbsp;ycoord(A)<br />
&nbsp;var m5&nbsp;=&nbsp;12 rem 3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;remainder after dividing by 3<br />
&nbsp;var r1&nbsp;=&nbsp;direction(PQ)&nbsp;<wbr>&nbsp;<wbr>&nbsp;%&nbsp;in radians<br />
&nbsp;var d1&nbsp;=&nbsp;directiondeg(PQ) </p>
<p> ==============================</p>
<h2>SEE ALSO</h2>
<p> The mathsPIC package manual and examples</p>
<h2>BUGS</h2>
<p> Please report bugs to Dick Nickalls (dick [AT] nickalls [dot] org) or to Apostolos Syropoulos </p>
<h2>Index</h2>
