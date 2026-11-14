---
title: "ncl_areas_params(3)"
name: "ncl_areas_params"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_areas_params/"
---

Areas_params - This document briefly describes all Areas parameters. 

<h2>Description</h2>Areas currently supports nine parameters. These parameters are useful mostly for debugging Areas problems. The current values may be retrieved using one of the routines ARGETI or ARGETR. Parameter values may be reset using the routine ARSETI or ARSETR; the parameter 'DI' is for retrieval only and may not be given a new value by the user. 

 The Areas parameter descriptions appear below in alphabetical order. Each description begins with a line giving the parameter name and the intrinsic FORTRAN type of the parameter.
<dl COMPACT><dt>'AL' - Real
<dd>Arrowhead Length. AL specifies the length of each arrowhead used on a debug plot produced by ARDBPA. The value is interpreted as a fraction of the width of the plotter frame. Using a value which is less than or equal to zero causes arrowheads to be omitted. The default value is .008.
<dt>'AT' - Integer
<dd>Arithmetic Type flag. AT allows the user to specify the type of arithmetic Areas is to use or to find out what type it decided to use. A call to set the value of AT should precede any other call to an Areas routine (except, possibly, one to set the value of LC) and it should only be done once. A call to get the value of AT will either return the value you set or a value picked by Areas.
<dl COMPACT><dd><dl COMPACT><dt>&lt; 1
<dd>Areas decides what sort of arithmetic to use.
<dt> 1
<dd>Real arithmetic is to be used.
<dt> 2
<dd>Double-precision arithmetic is to be used.
<dt> 3
<dd>Multiple-precision arithmetic is to be used and Areas is to choose the base value.
<dt>&gt; 3
<dd>Multiple-precision arithmetic is to be used and AT specifies the base value. (For example, the value 100 specifies the use of base-100 multiple-precision integer arithmetic.)</dl></dl>
 

 Default: 0 

 Note: You should use a nonzero value of AT only on the recommendation of an NCAR consultant.
<dt>'AW' - Real
<dd>Arrowhead Width. AL specifies the half-width of each arrowhead used on a debug plot produced by ARDBPA. The value is interpreted as a fraction of the width of the plotter frame. Using a value which is less than or equal to zero causes arrowheads to be omitted. The default value is .002.
<dt>'DB' - Integer
<dd>DeBug-plots flag. DB allows the user to study the area map.
<dl COMPACT><dd><dl COMPACT><dt> 0
<dd>Debugging turned off. This is the default.
<dt>&gt; 0
<dd>Debugging is on. At selected break points, ARPRAM produces plots showing all edge segments in the area map that belong to the edge group with group identifier DB.</dl></dl><dt>'DC' - Integer
<dd>Debug Colors index. ARDBPA uses color indices DC+1 through DC+5 for debug-plot colors. 

 By default, DC=100, so ARDBPA defines and uses color indices 101 through 105.
<dt>'DI' - Integer
<dd>Direction Indicator flag. The value of DI is for retrieval only and cannot be set by the user. A value returned for DI is meaningful only when the call to ARGETI that retrieves it originates from the user-written routine (dummy argument &quot;APR&quot;) that is called by ARSCAM. It then gives you information about the area whose polygonal boundary is defined by the values of APR's arguments. The two possible values of DI are:
<dl COMPACT><dd><dl COMPACT><dt>1
<dd>Edge of the area is given in counterclockwise order (with the interior to the left).
<dt>2
<dd>Edge of the area is given in clockwise order (with the interior to the right). 

</dl></dl><dt>'ID' - Real
<dd>Identifier Distance. ID specifies the distance from an arrow to a left or right area identifier on a debug plot produced by ARDBPA. The value is interpreted as a fraction of the width of the plotter frame. Using a value which is less than or equal to zero causes area identifiers to be omitted. The default value is .004.
<dt>'IS' - Real
<dd>Identifier Size. IS specifies the size of the characters used to write an area identifier on a debug plot produced by ARDBPA. The value is interpreted as a fraction of the width of the plotter frame. Using a value which is less than or equal to zero causes area identifiers to be omitted. The default value is .001.
<dt>'LC' - Integer
<dd>Largest Coordinate. LC lets you specify the largest coordinate allowed in an area map. X and Y coordinates in an area map are represented by integers in the range from 0 to LC, inclusive; the default value of LC is 1000000. 

 The minimum value allowed for LC is 1000; attempting to set LC&lt;1000 gives it the value 1000. The value of LC must not be greater than the largest integer on the machine on which Areas is running; its value must also be exactly representable as a real number on that machine. 

 A call to set the value of LC should precede any other call to an Areas routine and should only be done once.
<dt>'RC' - Integer
<dd>Reconciling Conflicts in area-identifier information. 

 This is an array of 16 values, indexed by group identifier. To set all values in the array to the same value &quot;n&quot;, use &quot;CALL ARSETI('RC',n)&quot;; to set just the first value in the array, use &quot;CALL ARSETI('<a HREF="/docs/linux/man/1-rc/">RC</a>(1)',n)&quot;; to set just the second value, use &quot;CALL ARSETI('<a HREF="/docs/linux/man/2-rc/">RC</a>(2)',n)&quot;; and so on. You can call ARGETI to get the value of <a HREF="/docs/linux/man/1-rc/">RC</a>(1) or <a HREF="/docs/linux/man/2-rc/">RC</a>(2) or <a HREF="/docs/linux/man/3-rc/">RC</a>(3), etc.; if you ask for the value of just RC, you will get the value of <a HREF="/docs/linux/man/1-rc/">RC</a>(1). 

 <a HREF="/docs/linux/man/1-rc/">RC</a>(1) is associated with edge group 1, <a HREF="/docs/linux/man/2-rc/">RC</a>(2) with edge group 2, and so on. An edge group with a group identifier greater than 16 is associated with RC(16). 

 When the set of possible area identifiers for a given area in a given group is contradictory, some algorithm must be used to choose an identifier for the area. The value of that element of RC that is associated with the group determines what algorithm will be used, as follows:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>The default scheme: If any of the possible area identifiers is negative, use -1 as the identifier for the area. Otherwise, if none of the possible values is non-zero, use a zero identifier. Otherwise, from among the non-zero possibilities, use the one most recently seen by AREAS.
<dt>1
<dd>The set of possible identifiers is examined: Zeroes are ignored, negatives are treated as -1's, and the value that occurs most frequently in the resulting set is used as the identifier for the area.
<dt>2
<dd>Using RC = 2 is just like using RC = 1 except that zeroes are not ignored: the area identifier used is simply the one that occurs most frequently in the set of possibilities (all negatives being treated as -1's).
<dt>-1
<dd>Using RC = -1 is just like using RC = 1 except that, if there are any negatives in the set of possible identifiers, a -1 is used.
<dt>-2
<dd>Using RC = -2 is just like using RC = 2 except that, if there are any negatives in the set of possible identifiers, a -1 is used.</dl></dl>
</dl><h2>See Also</h2>Online: argeti, argetr, arseti, arsetr 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
